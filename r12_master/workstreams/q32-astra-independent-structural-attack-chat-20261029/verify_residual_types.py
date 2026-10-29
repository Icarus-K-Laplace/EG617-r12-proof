"""Enumerate 7-vertex path/cycle types; no global graph solving."""
import itertools as it, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
types=[("P",k) for k in range(1,8)]+[("C",k) for k in range(3,8)]
types.sort(key=lambda t:(t[1],t[0]))
def rec(start,left,chosen):
    if left==0: yield chosen; return
    for i in range(start,len(types)):
        kind,k=types[i]
        if k<=left: yield from rec(i,left-k,chosen+[types[i]])
def exact_numbers(parts):
    E=set(); off=0
    for kind,k in parts:
        E.update((off+i,off+i+1) for i in range(k-1))
        if kind=="C": E.add((off,off+k-1))
        off+=k
    alpha=0; cliques=[]
    for s in range(1,128):
        vertices=[i for i in range(7) if s>>i&1]
        pairs=list(it.combinations(vertices,2))
        if all(p not in E for p in pairs): alpha=max(alpha,len(vertices))
        if all(p in E for p in pairs): cliques.append(s)
    dp=[8]*128; dp[0]=0
    for s in range(1,128):
        bit=s&-s
        dp[s]=min(1+dp[s^c] for c in cliques if c&bit and c&s==c)
    return len(E),alpha,dp[127]
rows=[]
for parts in rec(0,7,[]):
    e,a,k=exact_numbers(parts)
    if 3<=e<=7 and a<=4 and k<=4:
        rows.append(dict(type="+".join(f"{t}{n}" for t,n in parts),
                         edges=e,z=e-3,alpha=a,clique_cover=k,
                         excluded_by_nonempty_fiber_theorem=(k==4)))
assert len(rows)==18
assert sum(r["excluded_by_nonempty_fiber_theorem"] for r in rows)==14
survivors=[r for r in rows if not r["excluded_by_nonempty_fiber_theorem"]]
assert {r["type"] for r in survivors}=={"P2+P2+C3","C3+P4","P1+C3+C3","C3+C4"}
out=dict(status="PASS",scope="component-type enumeration only; conditional graph exclusions use the analytic theorem",
         total_types=len(rows),excluded_types=14,remaining_types=survivors,all_types=rows)
(ROOT/"residual_types.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

