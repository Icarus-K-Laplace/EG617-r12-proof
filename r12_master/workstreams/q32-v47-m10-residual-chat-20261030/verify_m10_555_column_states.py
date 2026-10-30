#!/usr/bin/env python3
"""Enumerate and alpha-check one-column 4+6 K4-e cross-grid states.

Normalization:
- the unique small-side heavy pair A,B has extra edge (A_0,B_1);
- in the selected outer column, the C-to-D matching is identity.

The exact 5,5,5 theorem gives p_B=p_A or p_B=p_A o (0 1), with the
corresponding extra-edge rule. The five small-side light pairs impose the
5,4,5 switch constraints. The verifier enumerates every resulting state.

For the five 4-sets A,B,C,D,E, a 5-set using at most three blocks is
excluded by the 4,5,5 and 5,5,5 local theorems (and by the matching-only
small triples). Thus any independent 5-set must have distribution
1+1+1+1+1 or 2+1+1+1. The script checks all 1,024 and 7,680 such sets.
"""
from itertools import combinations, permutations, product
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

V20=[(b,h) for b in range(5) for h in range(4)]
VID20={v:i for i,v in enumerate(V20)}
E20=[(i,j) for j in range(20) for i in range(j)]
EID20={e:k for k,e in enumerate(E20)}

def edge_add(g,u,v):
    if u>v:u,v=v,u
    return g | (1<<EID20[(u,v)])

def candidate_five_masks():
    masks=[]
    # One vertex from each of the five blocks.
    for labels in product(range(4),repeat=5):
        vs=[VID20[(b,labels[b])] for b in range(5)]
        m=0
        for i,j in combinations(vs,2):
            m |= 1<<EID20[tuple(sorted((i,j)))]
        masks.append(m)
    # Two vertices from one block and one from three other blocks.
    for repeated in range(5):
        others=[b for b in range(5) if b!=repeated]
        for pair in combinations(range(4),2):
            for chosen in combinations(others,3):
                for labels in product(range(4),repeat=3):
                    vs=[VID20[(repeated,pair[0])],VID20[(repeated,pair[1])]]
                    vs += [VID20[(b,h)] for b,h in zip(chosen,labels)]
                    m=0
                    for i,j in combinations(vs,2):
                        m |= 1<<EID20[tuple(sorted((i,j)))]
                    masks.append(m)
    assert len(masks)==8704
    return masks

CANDIDATE_FIVE=candidate_five_masks()

def graph20(ps,es):
    g=0
    # Six small-side pairs: all identity matchings.
    for i,j in combinations(range(4),2):
        for h in range(4):
            g=edge_add(g,VID20[(i,h)],VID20[(j,h)])
    # The fixed extra edge in the heavy A-B pair.
    g=edge_add(g,VID20[(0,0)],VID20[(1,1)])
    # Four cross pairs, each base matching plus one extra edge.
    for i in range(4):
        for h in range(4):
            g=edge_add(g,VID20[(i,h)],VID20[(4,ps[i][h])])
        a,b=es[i]
        g=edge_add(g,VID20[(i,a)],VID20[(4,b)])
    return g

def main():
    light=[(0,2),(0,3),(1,2),(1,3),(2,3)]
    total=aligned=switched=0
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
                extra_iter=((eA,eB,eC,eD)
                            for eB,eC,eD in product(OFF[pB],OFF[ID],OFF[pD]))
            else:
                extra_iter=product(OFF[pA],OFF[pB],OFF[ID],OFF[pD])
            for es in extra_iter:
                if not all(row_switch_valid(ps[i],ps[j],es[i],es[j])
                           for i,j in light):
                    continue
                total+=1
                if is_switch: switched+=1
                else: aligned+=1
                g=graph20(ps,es)
                if any((g&m)==0 for m in CANDIDATE_FIVE):
                    raise AssertionError(("independent five found",ps,es))
    assert total==20788 and aligned==20772 and switched==16
    print(json.dumps({"one_column_states":total,
                      "A_B_aligned":aligned,
                      "A_B_switch":switched,
                      "candidate_five_sets_checked_per_state":len(CANDIDATE_FIVE),
                      "independent_five_found":False},indent=2))

if __name__=="__main__":
    main()
