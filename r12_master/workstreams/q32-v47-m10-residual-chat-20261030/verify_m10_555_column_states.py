#!/usr/bin/env python3
"""Enumerate one-column 4+6 K4-e cross-grid local states.

Normalize the small-side heavy extra edge to (A_0,B_1) and the C-to-D
matching in the selected outer column to identity. Apply the exact 5,5,5
A-B-D classification and the five 4,5,5 constraints from the K4-e light
pairs A-C,A-D,B-C,B-D,C-D.
"""
from itertools import permutations, product
import json

P=list(permutations(range(4)))
ID=(0,1,2,3)
TAU=(1,0,2,3)
TRANS=[p for p in P if sum(p[i]!=i for i in range(4))==2]
OFF={p:[(a,b) for a in range(4) for b in range(4) if b!=p[a]] for p in P}

def inv(p):
    q=[0]*4
    for i,x in enumerate(p):q[x]=i
    return tuple(q)

def comp(p,q):
    return tuple(p[q[i]] for i in range(4))

def row_switch_valid(p,q,e,f):
    if p==q:return True
    tau=comp(inv(p),q)
    if tau not in TRANS:return False
    return any(e==(s,q[s]) and f==(s,p[s])
               for s in range(4) if tau[s]!=s)

def main():
    light=[(0,2),(0,3),(1,2),(1,3),(2,3)]
    total=0;aligned=0;switched=0
    for pA,pD in product(P,repeat=2):
        for pB in (pA,comp(pA,TAU)):
            ps=(pA,pB,ID,pD)
            if not all(comp(inv(ps[i]),ps[j])==ID or
                       comp(inv(ps[i]),ps[j]) in TRANS
                       for i,j in light):
                continue
            is_switch=(pA!=pB)
            if is_switch:
                eA=(1,pA[0])  # e_AB=(A_0,B_1) fixes tau=(0 1), s=0
                for eB,eC,eD in product(OFF[pB],OFF[ID],OFF[pD]):
                    es=(eA,eB,eC,eD)
                    if all(row_switch_valid(ps[i],ps[j],es[i],es[j])
                           for i,j in light):
                        total+=1;switched+=1
            else:
                for eA,eB,eC,eD in product(OFF[pA],OFF[pB],OFF[ID],OFF[pD]):
                    es=(eA,eB,eC,eD)
                    if all(row_switch_valid(ps[i],ps[j],es[i],es[j])
                           for i,j in light):
                        total+=1;aligned+=1
    assert total==20788 and aligned==20772 and switched==16
    print(json.dumps({"one_column_states":total,
                      "A_B_aligned":aligned,
                      "A_B_switch":switched},indent=2))

if __name__=="__main__":
    main()
