"""Independent finite checks for the low-edge proof and parent source gate.

No imported sibling code, solver, graph-exhaustion or formal-proof claim.
The analytic reductions are in the accompanying theorem documents.
"""
import itertools as it
import json
import math
import platform
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def floor_edges(r,n):
    q,s=divmod(n,r)
    return r*q*(q-1)//2+q*s

def density(n):
    return math.comb(n,2)-11*floor_edges(12,n)

def cycle_bounds(n):
    return [2*k+1+k*(n-2*k-1)+(n-2*k-1)**2//4
            for k in range(2,(n-1)//2+1)]

def capacity_and_augmentation():
    vals=cycle_bounds(25)
    assert vals==[145,142,137,130,121,110,97,82,65,46,25]
    assert 25>=2+3 and 2<=(25-1)//2
    assert 25**2//4-25//2+1==145
    assert math.comb(25,2)-145==155>153
    chains=[]
    for e0 in range(282,286):
        chain=[]
        for e in range(e0,286):
            excess=2*e-47*12
            assert 0<=excess<=6
            if e<285:
                assert math.comb(47,2)-e>0
                assert 3+excess<=7<10
                assert 2*(e+1)-564==excess+2<=6
            chain.append(dict(edges=e,excess=excess))
        chains.append(chain)
    return dict(bound_table=vals,required_and_available_25_edges=[155,153],chains=chains)

def structural_checks():
    low=[floor_edges(3,47-q)+12*q-math.comb(q,2) for q in range(7)]
    assert low==[345,342,338,334,329,323,317] and min(low)>285
    support_options=[s for k in (2,3,4) for s in it.combinations(range(4),k)]
    classes={h:set() for h in (3,4,5)}
    counts={h:0 for h in classes}
    def canonical(S):
        return min(tuple(sorted(tuple(sorted(pi[i] for i in s)) for s in S))
                   for pi in it.permutations(range(4)))
    for h in classes:
        for S in it.combinations_with_replacement(support_options,h):
            if sum(len(s)-1 for s in S)!=5:continue
            deg=[sum(i in s for s in S) for i in range(4)]
            if min(deg)<2:continue
            counts[h]+=1;classes[h].add(canonical(S))
    assert counts=={3:9,4:40,5:48}
    assert {h:len(c) for h,c in classes.items()}=={3:2,4:3,5:5}
    assert classes[3]=={canonical([(0,1,2,3),(0,1),(2,3)]),
                        canonical([(0,1),(0,2,3),(1,2,3)])}
    for S in classes[4]:
        d=[sum(i in s for s in S) for i in range(4)]
        assert sorted(d)==[2,2,2,3]
        center=d.index(3);leaves=set(range(4))-{center}
        if not any(len(s)==2 and set(s)<=leaves for s in S):
            assert set(S)=={tuple(sorted(leaves))}|{tuple(sorted((center,i))) for i in leaves}
    final=set()
    for S in classes[5]:
        d=[sum(i in s for s in S) for i in range(4)]
        if sorted(d)!=[2,2,3,3]:continue
        lowlabels={i for i in range(4) if d[i]==2}
        if any(set(s)==lowlabels for s in S):continue
        final.add(S)
    assert final=={canonical([(0,1),(0,2),(0,2),(1,3),(1,3)]),
                   canonical([(0,1),(0,2),(0,3),(1,2),(1,3)])}
    functions=[lambda a,b:max(0,10-a-b)+a*max(0,b-2)+b*max(0,a-2),
               lambda a,b:max(0,9-a-b)+a*(b-1)+b*max(0,a-2),
               lambda a,b:max(0,9-a-b)+a*max(0,b-3)+b*max(0,a-2),
               lambda a,b:max(0,9-a-b)+a*max(0,b-2)+b*max(0,a-2)]
    ranges=[(10,10),(9,10),(9,10),(9,10)]
    minima=[]
    for f,(aa,bb) in zip(functions,ranges):
        rows=[(f(a,b),a,b) for a in range(1,aa+1) for b in range(1,bb+1)]
        minima.append(min(v for v,a,b in rows))
        if len(minima)==1:assert [(a,b) for v,a,b in rows if v==6]==[(2,2)]
    assert minima==[6,6,4,5]
    accounting=0
    for domains in ((range(10),range(1,11),range(1,11)),(range(10),range(10))):
        for other_sizes in it.product(*domains):
            for bits in range(1<<len(domains)):
                x=[a for i,a in enumerate(other_sizes) if bits>>i&1]
                assert max(0,sum(a-1 for a in x))>=sum(max(0,a-2) for a in x)
                accounting+=1
    assert accounting==8400
    assert 2*minima[2]>6 and 2*minima[3]>6
    return dict(independent4_bounds=low,support_multisets=counts,
                support_orbits={h:len(c) for h,c in classes.items()},
                intermediate_templates=sorted(final),scalar_minima=minima,
                diamond_accounting_cases=accounting,terminal_required_excess=[8,10])

def type_classification():
    types=[{(i-1)%5,(i+1)%5} for i in range(5)]
    compatible=lambda i,j:not(types[i]&types[j])
    subsets=[tuple(i for i in range(5) if mask>>i&1) for mask in range(1,32)]
    pairs=[(A,B) for A in subsets for B in subsets if all(compatible(a,b) for a in A for b in B)]
    assert len(pairs)==20
    overlap=[];singleton_checks=0
    for A,B in pairs:
        assert min(len(A),len(B))==1 and max(len(A),len(B))<=2
        available=set(range(5))-set().union(*(types[b] for b in B))
        for s in available:
            assert any(s in types[a] and all(compatible(a,b) for b in B) for a in range(5))
            singleton_checks+=1
        for u,v in it.product(range(5),repeat=2):
            if not all(compatible(u,b) for b in B):continue
            if not all(compatible(a,v) for a in A):continue
            if compatible(u,v):continue
            assert len(A)==len(B)==1
            sizes=[1]*5;sizes[A[0]]+=8;sizes[B[0]]+=8;sizes[u]+=1;sizes[v]+=1
            orbit={tuple(sizes[(s+d*i)%5] for i in range(5)) for s in range(5) for d in (-1,1)}
            assert (9,9,2,1,2) in orbit
            overlap.append((A,B,u,v))
    assert len(overlap)==10
    return dict(compatible_type_set_pairs=len(pairs),singleton_extension_checks=singleton_checks,
                missing_cross_edge_overlap_cases=len(overlap))

def make_blowup(sizes):
    groups=[];n=0
    for s in sizes:groups.append(list(range(n,n+s)));n+=s
    edges=set()
    for i in range(5):
        edges.update(tuple(sorted((x,y))) for x in groups[i] for y in groups[(i+1)%5])
    return groups,edges

def maximal_independent_sets(n,edges):
    allbits=(1<<n)-1
    comp=[allbits^(1<<i) for i in range(n)]
    for u,v in edges:comp[u]&=~(1<<v);comp[v]&=~(1<<u)
    out=[]
    def visit(R,P,X):
        if not(P|X):out.append(R);return
        vertices=[i for i in range(n) if (P|X)>>i&1]
        pivot=max(vertices,key=lambda i:(comp[i]&P).bit_count())
        candidates=P&~comp[pivot]
        while candidates:
            bit=candidates&-candidates;v=bit.bit_length()-1
            visit(R|bit,P&comp[v],X&comp[v])
            P&=~bit;X|=bit;candidates&=~bit
    visit(0,allbits,0)
    return out

def neighborhood_extension_costs():
    checked=discarded=independent_sets=0;maxcost=0
    cases=[]
    for a in range(1,11):
        groups,E=make_blowup([10,a,1,1,11-a])
        cases.append((groups,E,[0,1,2]))
        for i in range(5):
            edge=tuple(sorted((groups[i][0],groups[(i+1)%5][0])))
            cases.append((groups,E-{edge},[0,1,2]))
    groups,E=make_blowup([9,9,2,1,2]);cases.append((groups,E,[3,4]))
    for G,E,which in cases:
        mis=maximal_independent_sets(23,E)
        if max(I.bit_count() for I in mis)>=12:
            discarded+=1;continue
        labels=[(0,2,3),(1,4,2),(1,4,3),(0,2,3),(1,3,4)]
        Ts=[set().union(*(G[i] for i in labels[j])) for j in which]
        assert all(len(T)==12 for T in Ts)
        for I in mis:
            for u,v in E:assert not(I>>u&1 and I>>v&1)
            for v in range(23):
                if not(I>>v&1):assert any((min(v,u),max(v,u)) in E for u in range(23) if I>>u&1)
            cost=min(sum(u in T and v in T for u,v in E)+sum(I>>v&1 for v in T) for T in Ts)
            assert cost<=6
            maxcost=max(maxcost,cost);independent_sets+=1
        checked+=1
    assert len(cases)==61 and checked+discarded==61
    assert 78-maxcost>=72>density(14)
    return dict(family_representatives=61,valid_representatives=checked,
                discarded_alpha12=discarded,maximal_independent_sets=independent_sets,
                maximum_cost=maxcost,forced_14_edges=78-maxcost)

def minimum_degree_and_parents():
    caps={n:density(n) for n in (13,14,23,24,25,37)}
    assert caps=={13:67,14:69,23:132,24:144,25:146,37:237}
    assert all(2*k*k-5*k+9>0 for k in range(2,12))
    assert max(cycle_bounds(23))==122 and max(cycle_bounds(23)[1:])==119
    assert max(cycle_bounds(18))==73
    assert 35*12//2==210 and 36*13//2==234 and math.ceil(37*13/2)>density(37)
    assert all(234+10+s+max(0,90-2*s)>=289 for s in range(46))
    assert 210+66+11==287>286
    rows=[]
    for E,q in ((407,31),(407,32),(408,32),(408,33)):
        core=E-91-q
        assert 61-1-13==47 and core in (284,285) and core<=286
        rows.append(dict(parent_edges=E,charge=q,core_edges=core,
                         uses_generic_R447_gate=True,closed_under_parent_contract=True))
    assert 13+math.comb(13,2)==91
    for E in (407,408):assert E-91-(E-377)==286
    return dict(caps=caps,degree10_edge_floor=289,degree11_edge_floor=287,
                parent_rows=rows,hereditary_core_floor=286,pivot_charge_caps={407:30,408:31})

def main():
    result=dict(status='PASS_FINITE_CHECKS',python=platform.python_version(),
        scope='Arithmetic, finite types and explicit neighborhood graph families; analytic theorem is not machine-formalized.',
        capacity=capacity_and_augmentation(),structure=structural_checks(),
        types=type_classification(),neighborhood_costs=neighborhood_extension_costs(),
        minimum_degree=minimum_degree_and_parents())
    (ROOT/'VERIFICATION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result,ensure_ascii=True))

if __name__=='__main__':main()
