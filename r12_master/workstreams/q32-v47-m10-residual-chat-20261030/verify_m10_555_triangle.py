#!/usr/bin/env python3
"""Exhaustive verifier for the normalized 5,5,5 triangle theorem."""
from itertools import combinations, permutations, product
import json
from collections import Counter

P4=list(permutations(range(4)))
ID=(0,1,2,3)
TRANS=[p for p in P4 if sum(p[i]!=i for i in range(4))==2]
OFF_ID=[(a,b) for a in range(4) for b in range(4) if a!=b]
V=[("A",i) for i in range(4)]+[("B",i) for i in range(4)]+[("D",i) for i in range(4)]
VID={v:i for i,v in enumerate(V)}
E=[(i,j) for j in range(12) for i in range(j)]
EID={e:k for k,e in enumerate(E)}
FIVE=[]
for c in combinations(range(12),5):
    m=0
    for i,j in combinations(c,2):
        m |= 1<<EID[(i,j)]
    FIVE.append(m)

def add(g,u,v):
    if u>v:u,v=v,u
    return g | (1<<EID[(u,v)])

def graph(sigma,eab,ead,ebd):
    g=0
    for i in range(4):
        g=add(g,VID[("A",i)],VID[("B",i)])
        g=add(g,VID[("A",i)],VID[("D",i)])
        g=add(g,VID[("B",i)],VID[("D",sigma[i])])
    a,b=eab;g=add(g,VID[("A",a)],VID[("B",b)])
    a,d=ead;g=add(g,VID[("A",a)],VID[("D",d)])
    b,d=ebd;g=add(g,VID[("B",b)],VID[("D",d)])
    return g

def alpha_le_4(g):
    return all(g&m for m in FIVE)

def predicted(sigma,eab,ead):
    if sigma==ID:
        return True
    if sigma not in TRANS:
        return False
    return any(eab==(s,sigma[s]) and ead==(sigma[s],s)
               for s in range(4) if sigma[s]!=s)

def main():
    total=0;valid=0;by=Counter()
    for sigma in P4:
        off_sigma=[(a,b) for a in range(4) for b in range(4) if b!=sigma[a]]
        for eab,ead,ebd in product(OFF_ID,OFF_ID,off_sigma):
            total+=1
            ok=alpha_le_4(graph(sigma,eab,ead,ebd))
            assert ok==predicted(sigma,eab,ead),(sigma,eab,ead,ebd,ok)
            if ok:
                valid+=1
                by["identity" if sigma==ID else "transposition"]+=1
    assert total==41472 and valid==1872
    assert by=={"identity":1728,"transposition":144}
    print(json.dumps({"total":total,"valid":valid,"by_type":dict(by)},indent=2))

if __name__=="__main__":
    main()
