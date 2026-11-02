#!/usr/bin/env python3
"""Independent finite checks for the frozen Q32 285-edge support reduction."""
from itertools import combinations, combinations_with_replacement, permutations
import json

SUPPORTS = [
    frozenset(s)
    for size in (2,3,4)
    for s in combinations(range(4),size)
]

def canonical(multiset):
    return min(
        tuple(sorted(tuple(sorted(p[i] for i in support)) for support in multiset))
        for p in permutations(range(4))
    )

def orbit_table():
    table={}
    for h in (3,4,5):
        reps={}
        for multiset in combinations_with_replacement(SUPPORTS,h):
            if sum(map(len,multiset)) != h+5:
                continue
            d=[sum(i in s for s in multiset) for i in range(4)]
            if min(d)<2:
                continue
            reps[canonical(multiset)]=d
        table[str(h)]=[
            {"supports":[list(s) for s in orbit],"seed_degrees":reps[orbit]}
            for orbit in sorted(reps)
        ]
    return table

def u4(a,b):
    return max(0,10-a-b)+a*max(0,b-2)+b*max(0,a-2)

def u5(a,b):
    return max(0,9-a-b)+a*max(0,b-3)+b*max(0,a-2)

def d_mixed(a,b):
    return max(0,9-a-b)+a*max(0,b-2)+b*max(0,a-2)

def minima(fn):
    values=[(fn(a,b),a,b) for a in range(1,12) for b in range(1,12)]
    m=min(v for v,_,_ in values)
    return {"minimum":m,"argmin":[[a,b] for v,a,b in values if v==m]}

def pointwise(vals):
    return max(0,sum(a-1 for a in vals)) >= sum(max(0,a-2) for a in vals)

def main():
    table=orbit_table()
    assert [len(table[str(h)]) for h in (3,4,5)] == [2,3,5]
    h5=table["5"]
    candidates=[]
    for row in h5:
        d=row["seed_degrees"]
        if sorted(d) != [2,2,3,3]:
            continue
        k10={i for i,x in enumerate(d) if x==3}
        k11={i for i,x in enumerate(d) if x==2}
        if any(set(edge)<=k11 for edge in row["supports"]):
            continue
        candidates.append(row)
    assert len(candidates)==2

    k10_cases=0
    for x in range(10):       # opposite K10 missing set; zero allowed
        for y in range(1,11): # K11 missing sets are nonempty
            for z in range(1,11):
                k10_cases+=1
                assert pointwise((x,y,z))
    k11_cases=0
    for x in range(10):
        for y in range(10):
            k11_cases+=1
            assert pointwise((x,y))

    scalar={
        "U4_two_K11_pair":minima(u4),
        "U5_mixed_K10_K11":minima(u5),
        "D_mixed_edge":minima(d_mixed),
    }
    assert scalar["U4_two_K11_pair"]["minimum"]==6
    assert scalar["U5_mixed_K10_K11"]["minimum"]==4
    assert scalar["D_mixed_edge"]["minimum"]==5

    print(json.dumps({
        "status":"PASS",
        "support_orbit_counts":{"h3":2,"h4":3,"h5":5},
        "h5_K10_K11_degree_pattern_survivors":candidates,
        "pointwise_D_checks":{"K10_vertices":k10_cases,"K11_vertices":k11_cases},
        "scalar_minima":scalar,
        "scope":"finite support and scalar/pointwise arithmetic only; not a proof of the analytic clique blockers or the full Q32 theorem",
    },indent=2))

if __name__=="__main__":
    main()
