#!/usr/bin/env python3
"""Corrected exhaustive one-column K4-e 4+6 local-state verifier."""
from itertools import combinations, permutations, product
from collections import Counter
import json

P4=list(permutations(range(4)))
ID=(0,1,2,3)
OFF={p:[(a,b) for a in range(4) for b in range(4) if b!=p[a]] for p in P4}

def inv(p):
    q=[0]*4
    for i,x in enumerate(p): q[x]=i
    return tuple(q)

def comp(p,q):
    return tuple(p[q[i]] for i in range(4))

V12=[("A",i) for i in range(4)]+[("B",i) for i in range(4)]+[("E",i) for i in range(4)]
VID12={v:i for i,v in enumerate(V12)}
EDGES12=[(i,j) for j in range(12) for i in range(j)]
EID12={e:k for k,e in enumerate(EDGES12)}
FIVE12=[]
for c in combinations(range(12),5):
    m=0
    for i,j in combinations(c,2): m|=1<<EID12[(i,j)]
    FIVE12.append(m)

def add12(g,u,v):
    if u>v:u,v=v,u
    return g | (1<<EID12[(u,v)])

def alpha_555(sig,eab,eae,ebe):
    g=0
    for i in range(4):
        g=add12(g,VID12[("A",i)],VID12[("B",i)])
        g=add12(g,VID12[("A",i)],VID12[("E",i)])
        g=add12(g,VID12[("B",i)],VID12[("E",sig[i])])
    g=add12(g,VID12[("A",eab[0])],VID12[("B",eab[1])])
    g=add12(g,VID12[("A",eae[0])],VID12[("E",eae[1])])
    g=add12(g,VID12[("B",ebe[0])],VID12[("E",ebe[1])])
    return all(g&m for m in FIVE12)

ALLOW_555={
 sig:{(eae,ebe) for eae in OFF[ID] for ebe in OFF[sig]
      if alpha_555(sig,(0,1),eae,ebe)}
 for sig in P4
}

def options_455(p,q,e):
    if p==q: return set(OFF[q])
    tau=comp(inv(p),q)
    if sum(tau[i]!=i for i in range(4))!=2: return set()
    return {(s,p[s]) for s in range(4)
            if tau[s]!=s and e==(s,q[s])}

V20=[(b,h) for b in range(5) for h in range(4)]
VID20={v:i for i,v in enumerate(V20)}
EDGES20=[(i,j) for j in range(20) for i in range(j)]
EID20={e:k for k,e in enumerate(EDGES20)}

def add20(g,u,v):
    if u>v:u,v=v,u
    return g | (1<<EID20[(u,v)])

def graph20(ps,es):
    g=0
    for i,j in combinations(range(4),2):
        for h in range(4):
            g=add20(g,VID20[(i,h)],VID20[(j,h)])
    g=add20(g,VID20[(0,0)],VID20[(1,1)])
    for i in range(4):
        for h in range(4):
            g=add20(g,VID20[(i,h)],VID20[(4,ps[i][h])])
        a,b=es[i]
        g=add20(g,VID20[(i,a)],VID20[(4,b)])
    return g

CAND=[]
for labels in product(range(4),repeat=5):
    vs=[VID20[(b,labels[b])] for b in range(5)]
    m=0
    for i,j in combinations(vs,2): m|=1<<EID20[(i,j)]
    CAND.append(m)
for repeated in range(5):
    others=[b for b in range(5) if b!=repeated]
    for pair in combinations(range(4),2):
        for chosen in combinations(others,3):
            for labels in product(range(4),repeat=3):
                vs=[VID20[(repeated,pair[0])],VID20[(repeated,pair[1])]]
                vs += [VID20[(b,h)] for b,h in zip(chosen,labels)]
                m=0
                for i,j in combinations(vs,2): m|=1<<EID20[tuple(sorted((i,j)))]
                CAND.append(m)
assert len(CAND)==8704

def main():
    total=aligned=switched=0
    switch_counts=Counter()
    witness=False
    for pA,pB,pD in product(P4,repeat=3):
        sig=comp(inv(pA),pB)
        for eAn,eBn in ALLOW_555[sig]:
            eA=(eAn[0],pA[eAn[1]])
            eB=(eBn[0],pA[eBn[1]])
            ec=options_455(pA,ID,eA) & options_455(pB,ID,eB)
            for eC in ec:
                ed=(options_455(pA,pD,eA) &
                    options_455(pB,pD,eB) &
                    options_455(ID,pD,eC))
                for eD in ed:
                    ps=(pA,pB,ID,pD)
                    es=(eA,eB,eC,eD)
                    g=graph20(ps,es)
                    if not all(g&m for m in CAND): continue
                    total+=1
                    if pA==pB:
                        aligned+=1
                    else:
                        switched+=1
                        switch_counts[sig]+=1
                    if (pA==ID and pB==(0,1,3,2) and pD==ID and
                        es==((2,3),(2,2),(2,3),(2,3))):
                        witness=True
    expected={
      (1,0,2,3):30,(0,1,3,2):8,(0,2,1,3):8,
      (0,3,2,1):8,(2,1,0,3):8,(3,1,2,0):8}
    assert total==20842 and aligned==20772 and switched==70
    assert dict(switch_counts)==expected and witness
    print(json.dumps({"one_column_states":total,"AB_aligned":aligned,
      "AB_switched":switched,
      "switches_by_relative_permutation":{str(k):v for k,v in switch_counts.items()},
      "independent_five_candidates_per_state":len(CAND),
      "omitted_witness_present":witness},indent=2))

if __name__=="__main__":
    main()
