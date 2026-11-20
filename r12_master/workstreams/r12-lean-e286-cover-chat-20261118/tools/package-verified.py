"""Package only exact Git-tracked workstream bytes; keep drafts/cache out."""
import hashlib
import json
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parent.parent
tree = json.loads((root / 'logs/remote-project-tree.json').read_text(encoding='utf-8-sig'))
ci = json.loads((root / 'CI_STATUS.json').read_text(encoding='utf-8-sig'))
assert tree.get('truncated') is False
assert ci['cleanLinuxBuild'] == ci['fullAxiomAudit'] == ci['statementInspection'] == 'PASS'
assert ci['localMatchesCISHA256'] == 'PASS'
assert ci['elaboratedProjectDependencyAudit'] == 'PASS'
files = {}
for entry in tree['tree']:
    if entry['type'] != 'blob':
        continue
    rel = entry['path']
    path = (root / rel).resolve()
    path.relative_to(root)
    data = path.read_bytes()
    git_hash = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if git_hash != entry['sha']:
        raise RuntimeError('Local/remote byte mismatch: ' + rel)
    files[rel] = data
for entry in ci['hashes']:
    rel = 'lean/' + entry['file']
    if hashlib.sha256(files[rel]).hexdigest() != entry['sha256']:
        raise RuntimeError('Local/CI source mismatch: ' + rel)
provenance = {
    'repository': 'Icarus-K-Laplace/EG617-r12-proof',
    'branch': 'workstream/r12-lean-e286-cover-chat-20261118',
    'package_tree_commit': tree['commit'],
    'verified_code_commit': ci['sha'],
    'verified_ci': ci['run'],
    'status': 'PARTIAL: actual E286 graph reduced to nine support orbits',
    'E286': 'FORMALIZATION_GAP',
    'MainTheorem': 'ABSENT',
    'tracked_file_count': len(files),
    'all_tracked_bytes_match_github_git_blobs': True,
    'all_lean_source_bytes_match_successful_ci': True,
}
files['PACKAGE_PROVENANCE.json'] = (json.dumps(provenance, indent=2) + '\n').encode()
files['REMOTE_PROJECT_TREE.json'] = (json.dumps(tree, indent=2) + '\n').encode()
manifest = ''.join(hashlib.sha256(data).hexdigest() + '  ' + rel + '\n'
                   for rel, data in sorted(files.items()))
files['SHA256SUMS'] = manifest.encode()
out = root.parent / 'outputs'
out.mkdir(exist_ok=True)
archive = out / ('EG617-r12-Lean-E286-nine-orbits-' + ci['sha'][:7] + '-20261120.zip')
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    for rel, data in sorted(files.items()):
        zf.writestr(rel, data)
with zipfile.ZipFile(archive) as zf:
    assert zf.testzip() is None
    assert set(zf.namelist()) == set(files)
    for rel, data in files.items():
        assert zf.read(rel) == data
digest = hashlib.sha256(archive.read_bytes()).hexdigest()
receipt = {**provenance, 'zip': str(archive), 'sha256': digest,
           'bytes': archive.stat().st_size, 'entries': len(files),
           'zip_crc_and_all_payload_hashes': 'PASS'}
(out / (archive.name + '.sha256')).write_text(digest + '  ' + archive.name + '\n', encoding='ascii')
(out / 'PACKAGE_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt))
