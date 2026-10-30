#!/usr/bin/env python3
"""Exact 5,5,5 triangle classifier. Enumerates 41,472 normalized inputs."""
from itertools import combinations, permutations, product
from collections import Counter
import json

P4=list(permutations(range(4)))
ID=(0,1,2,3)
TAU01=(1,0,2,3)
OFF_ID=[(a,b) for a in range(4) for b in range(4) if a!=b]
OFF={p:[(a,b) for a in range(4) for b in range(4) if b!=p[a]] for p in P4}
V=[("A",i) for i in range(4)]+[("B",i) for i in range(4)]+[("E",i) for i in range(4)]
VID={v:i for i,v in enumerate(V)}
EDGES=[(i,j) for j in range(12) for i in range(j)]
EID={e:k for k,e in enumerate(EDGES)}
FIVE=[]
for c in combinations(range(12),5):
    m=0
    for i,j in combinations(c,2): m |= 1<<EID[(i,j)]
    FIVE.append(m)

def add(g,u,v):
    if u>v:u,v=v,u
    return g | (1<<EID[(u,v)])

def graph(sig,eab,ead,ebe):
    g=0
    for i in range(4):
        g=add(g,VID[("A",i)],VID[("B",i)])
        g=add(g,VID[("A",i)],VID[("E",i)])
        g=add(g,VID[("B",i)],VID[("E",sig[i])])
    g=add(g,VID[("A",eab[0])],VID[("B",eab[1])])
    g=add(g,VID[("A",ead[0])],VID[("E",ead[1])])
    g=add(g,VID[("B",ebe[0])],VID[("E",ebe[1])])
    return g

def alpha_le4(g):
    return all(g&m for m in FIVE)

def exact_classifier(sig,eab,ead,ebe):
    if sig==ID: return True
    moved=[i for i in range(4) if sig[i]!=i]
    if len(moved)!=2: return False
    u,v=moved
    pi=[None]*4
    pi[u],pi[v]=0,1
    rest=[i for i in range(4) if i not in moved]
    pi[rest[0]],pi[rest[1]]=2,3
    ab=(pi[eab[0]],pi[eab[1]])
    ad=(pi[ead[0]],pi[ead[1]])
    bd=(pi[ebe[0]],pi[ebe[1]])
    c01,c10=(0,1),(1,0)
    if ab==c01:
        return bd in OFF[TAU01] if ad==c10 else bd==(0,0)
    if ab==c10:
        return bd in OFF[TAU01] if ad==c01 else bd==(1,1)
    return (ad==c01 and bd==(0,0)) or (ad==c10 and bd==(1,1))

def main():
    total=valid=0
    by=Counter()
    mismatches=[]
    for sig in P4:
        for eab,ead,ebe in product(OFF_ID,OFF_ID,OFF[sig]):
            total+=1
            actual=alpha_le4(graph(sig,eab,ead,ebe))
            predicted=exact_classifier(sig,eab,ead,ebe)
            if actual:
                valid+=1
                by[sig]+=1
            if actual!=predicted:
                mismatches.append((sig,eab,ead,ebe,actual,predicted))
    trans=[p for p in P4 if sum(p[i]!=i for i in range(4))==2]
    assert total==41472 and valid==2124 and not mismatches
    assert by[ID]==1728 and len(trans)==6 and all(by[p]==66 for p in trans)
    assert all(by[p]==0 for p in P4 if p!=ID and p not in trans)
    witness=((0,1,3,2),(0,1),(2,3),(2,2))
    assert alpha_le4(graph(*witness)) and exact_classifier(*witness)
    print(json.dumps({"normalized_inputs":total,"valid_inputs":valid,
      "identity_valid":by[ID],"transposition_valid_each":66,
      "other_permutations_valid":0,"classifier_mismatches":0,
      "regression_witness_alpha_le4":True},indent=2))

if __name__=="__main__":
    main()
