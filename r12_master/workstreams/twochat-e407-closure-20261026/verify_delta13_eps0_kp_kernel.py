#!/usr/bin/env python3
"""Arithmetic replay for DELTA13_EPS0_KP_KERNEL_REDUCTION.md.

Checks the four-clique impossibility, the two KP base sequences, the five
parameter kernels, edge counts, degree multisets, and the forced excess at a
degree-six exceptional W vertex. Does not verify Brouwer/Kang-Pikhurko.
"""

from itertools import combinations, combinations_with_replacement
from collections import Counter


def c2(n): return n*(n-1)//2


def kp_sequences():
    out=[]
    for ns in combinations_with_replacement(range(1,18),4):
        if sum(ns)!=17: continue
        n1,n2,n3,n4=ns
        if n1<2: continue
        if n2>n1+1: continue
        if n4>n1+2: continue
        if n4>n3+1: continue
        out.append(ns)
    return out


def target_kernel(parts,a):
    groups=[]; idx=0
    for n in parts:
        groups.append(list(range(idx,idx+n))); idx+=n
    x=idx
    N1,N2,N3,N4=groups
    A=set(N1[:a]); y=N2[0]
    E=set()
    for g in groups:
        for u,v in combinations(g,2): E.add(tuple(sorted((u,v))))
    for u in A: E.add(tuple(sorted((y,u))))
    for u in (set(N1)-A)|(set(N2)-{y}): E.add(tuple(sorted((x,u))))
    deg=Counter()
    for u,v in E:
        deg[u]+=1; deg[v]+=1
    return len(E), Counter(deg.values()), deg[x], deg[y]


def main():
    # No 4-clique partition of 18 has 35 edges.
    sols=[]
    near=[]
    for ns in combinations_with_replacement(range(1,19),4):
        if sum(ns)!=18: continue
        e=sum(c2(x) for x in ns)
        if e==35: sols.append(ns)
        if 32<=e<=38: near.append((ns,e))
    assert sols==[]

    assert c2(18)-35==118
    assert 121-(18//4)+1==118
    assert kp_sequences()==[(3,4,5,5),(4,4,4,5)]

    expected={
        ((3,4,5,5),1):(35,Counter({4:14,3:3,5:1}),5,4),
        ((3,4,5,5),2):(35,Counter({4:14,3:3,5:1}),4,5),
        ((4,4,4,5),1):(35,Counter({4:13,3:4,6:1}),6,4),
        ((4,4,4,5),2):(35,Counter({4:12,3:4,5:2}),5,5),
        ((4,4,4,5),3):(35,Counter({4:13,3:4,6:1}),4,6),
    }
    got={}
    for parts in ((3,4,5,5),(4,4,4,5)):
        for a in range(1,parts[0]):
            got[(parts,a)]=target_kernel(parts,a)
    assert got==expected

    # W support slack total at delta=13, epsilon_U=0.
    assert 0+2*13-2==24
    # A degree-6 W vertex needs epsilon>=1 to have U-degree >=7.
    assert 12+1-6==7
    assert 12+0-6==6

    print('E407_DELTA13_EPS0_KP_KERNEL_REPLAY_OK')
    print('KP bases:',kp_sequences())
    for k,v in got.items(): print(k,v)
    print('nearby 4-clique edge sums:',near)
    print('scope: arithmetic/kernel replay only; external equality theorem not verified here')


if __name__=='__main__': main()
