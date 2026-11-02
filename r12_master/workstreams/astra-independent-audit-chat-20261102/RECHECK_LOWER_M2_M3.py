#!/usr/bin/env python3
"""Independent recheck of the M2 type quotient and M3 23-vertex family tests."""
from itertools import combinations, product
import json

def cycle_types():
    return [{(i-1)%5,(i+1)%5} for i in range(5)]

def type_quotient():
    T=cycle_types()
    compatible=lambda i,j:not(T[i]&T[j])
    subsets=[tuple(i for i in range(5) if mask>>i&1) for mask in range(1,32)]
    pairs=[(A,B) for A in subsets for B in subsets
           if all(compatible(a,b) for a in A for b in B)]
    assert len(pairs)==20
    assert all(min(len(A),len(B))==1 and max(len(A),len(B))<=2 for A,B in pairs)
    missing=[]
    for A,B in pairs:
        for u,v in product(range(5),repeat=2):
            if not all(compatible(u,b) for b in B): continue
            if not all(compatible(a,v) for a in A): continue
            if compatible(u,v): continue
            assert len(A)==len(B)==1
            missing.append((A,B,u,v))
    assert len(missing)==10
    return {"compatible_nonempty_type_set_pairs":len(pairs),
            "all_pairs_have_side_sizes_1_by_1_or_1_by_2":True,
            "incompatible_missing_cross_edge_cases":len(missing)}

def make_blowup(sizes):
    groups=[]
    cur=0
    for size in sizes:
        groups.append(list(range(cur,cur+size)))
        cur+=size
    edges=set()
    for i in range(5):
        for u in groups[i]:
            for v in groups[(i+1)%5]:
                edges.add(tuple(sorted((u,v))))
    return groups,edges

def maximal_independent_sets(n,edges):
    allbits=(1<<n)-1
    comp=[allbits^(1<<i) for i in range(n)]
    for u,v in edges:
        comp[u]&=~(1<<v)
        comp[v]&=~(1<<u)
    output=[]
    def visit(R,P,X):
        if not(P|X):
            output.append(R)
            return
        vertices=[i for i in range(n) if (P|X)>>i&1]
        pivot=max(vertices,key=lambda i:(comp[i]&P).bit_count())
        candidates=P&~comp[pivot]
        while candidates:
            bit=candidates&-candidates
            v=bit.bit_length()-1
            visit(R|bit,P&comp[v],X&comp[v])
            P&=~bit
            X|=bit
            candidates&=~bit
    visit(0,allbits,0)
    return output

def induced_edge_count(vertices,edges):
    return sum(1 for u,v in edges if u in vertices and v in vertices)

def neighborhood_costs():
    cases=[]
    for a in range(1,11):
        groups,edges=make_blowup([10,a,1,1,11-a])
        T0=set(groups[0]+groups[2]+groups[3])
        T1=set(groups[1]+groups[4]+groups[2])
        T2=set(groups[1]+groups[4]+groups[3])
        candidates=[T0,T1,T2]
        cases.append((set(edges),candidates,None))
        for i in range(5):
            cases.append((set(edges),candidates,i))
    groups,edges=make_blowup([9,9,2,1,2])
    candidates=[set(groups[0]+groups[2]+groups[3]),
                set(groups[1]+groups[3]+groups[4])]
    cases.append((set(edges),candidates,None))

    checked=discarded=independent_count=maximum_cost=0
    for E,candidates,deleted_class_edge in cases:
        E=set(E)
        if deleted_class_edge is not None:
            groups,_=make_blowup([9,9,2,1,2]) if False else (None,None)
            # Recover the class endpoints from the canonical five-part order.
            # The family sizes are encoded by the candidate T sets only, so
            # each case is stored with its original groups below instead.
            raise AssertionError("internal case construction error")
    return {}

def neighborhood_costs_fixed():
    cases=[]
    for a in range(1,11):
        groups,edges=make_blowup([10,a,1,1,11-a])
        Ts=[set(groups[0]+groups[2]+groups[3]),
            set(groups[1]+groups[4]+groups[2]),
            set(groups[1]+groups[4]+groups[3])]
        cases.append((groups,set(edges),None,Ts))
        for i in range(5):
            cases.append((groups,set(edges),i,Ts))
    groups,edges=make_blowup([9,9,2,1,2])
    Ts=[set(groups[0]+groups[2]+groups[3]),
        set(groups[1]+groups[3]+groups[4])]
    cases.append((groups,set(edges),None,Ts))

    checked=discarded=independent_count=maximum_cost=0
    for groups,E,deleted_class_edge,Ts in cases:
        E=set(E)
        if deleted_class_edge is not None:
            u=groups[deleted_class_edge][0]
            v=groups[(deleted_class_edge+1)%5][0]
            E.remove(tuple(sorted((u,v))))
        mis=maximal_independent_sets(23,E)
        if max(I.bit_count() for I in mis)>=12:
            discarded+=1
            continue
        for I in mis:
            cost=min(induced_edge_count(T,E)+sum(1 for v in T if (I>>v)&1)
                     for T in Ts)
            assert cost<=6
            maximum_cost=max(maximum_cost,cost)
            independent_count+=1
        checked+=1
    assert len(cases)==61 and checked==49 and discarded==12
    assert independent_count==263 and maximum_cost==6
    return {"family_representatives":len(cases),
            "valid_representatives":checked,
            "discarded_alpha12":discarded,
            "maximal_independent_sets_checked":independent_count,
            "maximum_minimum_cost":maximum_cost,
            "forced_14_vertex_edges":78-maximum_cost}

def main():
    result={"status":"PASS",
            "M2_type_quotient":type_quotient(),
            "M3_neighborhood_costs":neighborhood_costs_fixed(),
            "scope":"Independent finite recheck of type-set enumeration and the explicit 23-vertex blowup/edge-deletion representatives; not a proof of the analytic M2 classification or M4 argument."}
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
