#!/usr/bin/env python3
"""Finite replay for DELTA13_EPS0_KP_KERNEL_CLOSURE.md.

Enumerates the five KP target kernels, all high-vertex sets whose minimum
excess cost is at most four, and proper four-colourings of the low graph with
capacities (4,4,4,3). It checks the finite terminal case split only.
"""

from itertools import combinations


def kp_target(parts,a):
    groups=[]; idx=0
    for n in parts:
        groups.append(list(range(idx,idx+n))); idx+=n
    x=idx; verts=list(range(idx+1))
    N1,N2,N3,N4=groups; A=set(N1[:a]); y=N2[0]
    EH=set()
    for g in groups:
        for uv in combinations(g,2): EH.add(tuple(sorted(uv)))
    for u in A: EH.add(tuple(sorted((y,u))))
    for u in (set(N1)-A)|(set(N2)-{y}): EH.add(tuple(sorted((x,u))))
    allpairs={tuple(sorted(uv)) for uv in combinations(verts,2)}
    EJ=allpairs-EH
    deg={v:0 for v in verts}
    for u,v in EH: deg[u]+=1; deg[v]+=1
    return verts,EJ,EH,groups,x,y,A,deg


def colourable(verts,EJ,removed,caps=(4,4,4,3)):
    vs=[v for v in verts if v not in removed]
    adj={v:set() for v in vs}
    for u,v in EJ:
        if u in adj and v in adj:
            adj[u].add(v); adj[v].add(u)
    color={}; used=[0]*4

    def rec():
        if len(color)==len(vs): return True
        rem=[v for v in vs if v not in color]
        z=max(rem,key=lambda v:(len({color[w] for w in adj[v] if w in color}),len(adj[v])))
        forbidden={color[w] for w in adj[z] if w in color}
        for c in range(4):
            if c in forbidden or used[c]>=caps[c]: continue
            # symmetry among the three equal-capacity colours
            if used[c]==0 and any(j<c and caps[j]==caps[c] and used[j]==0 for j in range(4)):
                continue
            color[z]=c; used[c]+=1
            if rec(): return True
            used[c]-=1; del color[z]
        return False
    return rec()


def main():
    kernels=[]
    for parts in ((3,4,5,5),(4,4,4,5)):
        for a in range(1,parts[0]):
            kernels.append((parts,a))
    assert len(kernels)==5

    for parts,a in kernels:
        verts,EJ,EH,groups,x,y,A,deg=kp_target(parts,a)
        assert len(EH)==35
        cost={v:max(0,deg[v]-2) for v in verts}
        tested=0; feasible=[]
        # At least three high vertices are analytically necessary; enumerate
        # every subset of size 3 or 4 with minimum excess cost <=4.
        for r in (3,4):
            for R in combinations(verts,r):
                c=sum(cost[v] for v in R)
                if c>4: continue
                tested+=1
                if colourable(verts,EJ,set(R)):
                    feasible.append((R,c))
        assert not feasible, (parts,a,feasible)
        print('kernel',parts,'a=',a,'tested_high_sets=',tested,'NO_CAPACITATED_4_COLORING')

    print('E407_DELTA13_EPS0_KP_CLOSURE_REPLAY_OK')
    print('scope: finite high-set/capacitated-colouring replay only')


if __name__=='__main__': main()
