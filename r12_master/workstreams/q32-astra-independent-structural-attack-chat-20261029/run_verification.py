"""Run deterministic replay and record commands, output and SHA256 hashes."""
import hashlib,json,platform,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parent
logs=["Python "+platform.python_version(),
      "No external solver; no full Q32 SAT/UNSAT claim."]
for name in ("verify_outside_reserve.py","verify_residual_types.py"):
    command=[sys.executable,"-B",str(root/name)]
    r=subprocess.run(command,capture_output=True,text=True,encoding="utf-8")
    logs += ["COMMAND: "+json.dumps(command),"EXIT: "+str(r.returncode),
             r.stdout,r.stderr]
    if r.returncode: raise RuntimeError(name+" failed")
(root/"verification_log.txt").write_text("\n".join(logs)+"\n",encoding="utf-8")
hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(root.iterdir()) if p.is_file() and p.name!="SHA256.json"}
(root/"SHA256.json").write_text(json.dumps(
    dict(algorithm="SHA256",files=hashes),indent=2)+"\n",encoding="utf-8")
print("REPLAYS_PASS; verification_log.txt and SHA256.json written")

