#!/usr/bin/env python3
"""Small independent check of the two-aligned cut combinatorics and outer degree vectors."""
from itertools import combinations

V=tuple(range(6))

def perfect_matchings(items):
    items=tuple(items)
    if not items:
        yield ()
        return
    x=items[0]
    for y in items[1:]:
        rest=tuple(z for z in items[1:] if z!=y)
        for tail in perfect_matchings(rest):
            yield ((x,y),)+tail

def connected_cut(aligned, matching):
    aligned=set(aligned)
    nonaligned=set(V)-aligned
    heavy={frozenset(e) for e in matching}
    adj={x:set() for x in V}
    for a in aligned:
        for b in nonaligned:
            if frozenset((a,b)) not in heavy:
                adj[a].add(b); adj[b].add(a)
    seen=set()
    stack=[next(iter(aligned))]
    while stack:
        x=stack.pop()
        if x in seen: continue
        seen.add(x); stack.extend(adj[x]-seen)
    return seen==set(V)

def main():
    matchings=list(perfect_matchings(V))
    assert len(matchings)==15
    checked=0
    for aligned in combinations(V,2):
        nonaligned=set(V)-set(aligned)
        for M in matchings:
            checked+=1
            assert connected_cut(aligned,M), (aligned,M)
            assert any(set(edge)<=nonaligned for edge in M), (aligned,M)
    # Outer degree vector: m is any labelling of profile (3,2,2,0).
    degree_cases=0
    for m3 in range(4):
        rem=[x for x in range(4) if x!=m3]
        for empty in rem:
            sizes=[2]*4
            sizes[m3]=3; sizes[empty]=0
            for alpha in range(4):
                if sizes[alpha]>2: continue
                c=tuple(3-sizes[t]-(t==alpha) for t in range(4))
                if sorted(c,reverse=True)==[3,1,0,0]:
                    triple=next(t for t,x in enumerate(c) if x==3)
                    single=next(t for t,x in enumerate(c) if x==1)
                    assert sizes[triple]==0
                    assert sizes[single]==2
                    assert sizes[alpha]==2 and alpha!=single
                degree_cases+=1
    print({
        "perfect_matchings":len(matchings),
        "aligned_pairs":15,
        "cut_instances_checked":checked,
        "all_cuts_connected":True,
        "all_have_non_aligned_heavy_pair":True,
        "outer_degree_endpoint_cases":degree_cases
    })

if __name__=="__main__":
    main()
