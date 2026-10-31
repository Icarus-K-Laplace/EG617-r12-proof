"""Validate artifact consistency and seal/deliver the audit; not a proof checker."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import zipfile

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
PREFIX=HERE.relative_to(REPO).as_posix()
PIN='c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2'
SOURCE='r12_master/workstreams/astra-global-root-integration-chat-20261031'
sha=lambda b:hashlib.sha256(b).hexdigest()

def validate():
    result=json.loads((HERE/'INDEPENDENT_REPLAY_RESULTS.json').read_text())
    assert result['source_sha256']==sha((HERE/'INDEPENDENT_REPLAY.py').read_bytes())
    assert result['replay_status']=='COMPUTATIONALLY_VERIFIED'
    assert not result['execution_failures']
    assert len(result['recurrence']['nodes'])==1752
    assert len(result['recurrence']['stops'])==144
    assert result['q27']['canonical_count']==2 and result['q28']['canonical_count']==8
    assert result['q27']['subset_checks']+result['q28']['subset_checks']==81920
    assert result['dag']['graphs']['independent']['nodes']==58
    obligations=json.loads((HERE/'AUDIT_OBLIGATIONS.json').read_text())
    assert len(obligations)==58
    assert all(o['Status'] in ('PROVED','COMPUTATIONALLY_VERIFIED') for o in obligations)
    assert sum(o['Status']=='COMPUTATIONALLY_VERIFIED' for o in obligations)==3
    decision=json.loads((HERE/'CERTIFICATION_DECISION.json').read_text())
    assert len(decision['conditions'])==14 and set(decision['conditions'].values())=={'PASS'}
    for script in HERE.glob('*.py'):
        compile(script.read_text(),str(script),'exec')
    for line in (HERE/'REMOTE_BRANCH_HEADS.tsv').read_text(encoding='utf-8-sig').splitlines():
        commit,ref=line.split()
        if ref=='refs/heads/workstream/r12-astra-global-root-integration-20261031':assert commit==PIN
        if ref=='refs/heads/workstream/r12-twochat-e408-global-20261026':assert commit==decision['original_global_root']
    names=subprocess.check_output(['git','-C',str(REPO),'diff','--name-only',PIN]).decode().splitlines()
    assert all(n.startswith(PREFIX+'/') for n in names),names
    files=[p for p in sorted(HERE.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.txt']
    checksum=''.join(sha(p.read_bytes())+'  '+p.relative_to(HERE).as_posix()+'\n' for p in files)
    (HERE/'SHA256SUMS.txt').write_bytes(checksum.encode('utf-8'))
    return result,files

def deliver(destination,result):
    destination.mkdir(parents=True,exist_ok=True)
    payload={}
    for p in sorted(HERE.rglob('*')):
        if p.is_file():payload[p.relative_to(REPO).as_posix()]=p.read_bytes()
    for row in result['integrity']['files']:
        raw=subprocess.check_output(['git','-C',str(REPO),'show',PIN+':'+row['path']])
        assert sha(raw)==row['sha256']
        payload[row['path']]=raw
    extra=result['integrity']['supplemental_exact285_source']
    raw=subprocess.check_output(['git','-C',str(REPO),'show',extra['commit']+':'+extra['path']])
    assert sha(raw)==extra['sha256']
    payload[extra['path']]=raw
    audit_head=subprocess.check_output(['git','-C',str(REPO),'rev-parse','HEAD']).decode().strip()
    receipt=dict(audit_commit=audit_head,source_commit=PIN,certification='PASS',
                 source='FINAL_CERTIFICATION_REPORT.md',formalization=False,external_human_peer_review=False)
    payload['PUBLICATION_RECEIPT.json']=(json.dumps(receipt,indent=2)+'\n').encode()
    payload['PACKAGE_README.txt']=(
        'EG617(r=12) independent certification package. Start with '+PREFIX+'/FINAL_CERTIFICATION_REPORT.md.\n'
        'Source proof bytes are pinned to '+PIN+'. Audit commit: '+audit_head+'.\n'
        'CERTIFICATION=PASS is an informal AI-assisted mathematical audit with finite computation.\n'
        'No proof-assistant formalization or external human peer review is claimed.\n'
        'The ZIP contains all48 source files, the audit, and the supplemental exact285 theorem.\n'
        'A full repository clone is required to rerun Git provenance checks. See audit README.md.\n'
    ).encode()
    payload['PACKAGE_SHA256SUMS.txt']=''.join(sha(data)+'  '+name+'\n' for name,data in sorted(payload.items())).encode()
    archive=destination/'EG617_r12_independent_certification.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for name,data in sorted(payload.items()):z.writestr(name,data)
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert all(z.read(name)==data for name,data in payload.items())
    for name in ('FINAL_CERTIFICATION_REPORT.md','ANALYTIC_OBLIGATION_MATRIX.md',
                 'COUNTEREXAMPLE_AND_GAP_REGISTER.md','ROOT_PROMOTION_RECOMMENDATION.md'):
        (destination/name).write_bytes((HERE/name).read_bytes())
    (destination/'PUBLICATION_RECEIPT.json').write_bytes(payload['PUBLICATION_RECEIPT.json'])
    (destination/'DELIVERY_SHA256SUMS.txt').write_bytes((''.join(
        sha(p.read_bytes())+'  '+p.name+'\n' for p in sorted(destination.iterdir())
        if p.is_file() and p.name!='DELIVERY_SHA256SUMS.txt')).encode())
    return dict(archive=str(archive),entries=len(payload),bytes=archive.stat().st_size,
                sha256=sha(archive.read_bytes()),audit_commit=audit_head)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path)
    args=parser.parse_args()
    result,files=validate()
    print(json.dumps(dict(artifact_consistency='PASS',audit_files_hashed=len(files),
                         decision='Manually adjudicated in report; this script checks consistency only.')))
    if args.output_dir:print(json.dumps(deliver(args.output_dir,result)))
