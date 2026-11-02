#!/usr/bin/env python3
"""Independent finite recheck of the E286 seed-support orbit table and scalar bounds."""
from itertools import combinations, combinations_with_replacement, permutations
import json

SUPPORTS = [
    frozenset(s)
    for size in (2, 3, 4)
    for s in combinations(range(4), size)
]

def canonical(multiset):
    forms = []
    for perm in permutations(range(4)):
        forms.append(tuple(sorted(
            tuple(sorted(perm[i] for i in support))
            for support in multiset
        )))
    return min(forms)

def support_orbits():
    output = {}
    for h in (3, 4, 5):
        reps = {}
        for multiset in combinations_with_replacement(SUPPORTS, h):
            if sum(map(len, multiset)) != h + 5:
                continue
            c = canonical(multiset)
            d = [sum(i in support for support in c) for i in range(4)]
            if min(d) < 2:
                continue
            reps[c] = {
                "seed_multiplicities": d,
                "clique_sizes": [13 - x for x in d],
            }
        output[str(h)] = [
            {"supports": [list(s) for s in orbit], **reps[orbit]}
            for orbit in sorted(reps)
        ]
    return output

def f11(a,b):
    return max(0,10-a-b)+a*max(0,b-2)+b*max(0,a-2)

def f1011(a,b):
    return max(0,9-a-b)+a*max(0,b-3)+b*max(0,a-2)

def f911(a,b):
    return max(0,8-a-b)+a*max(0,b-4)+b*max(0,a-2)

def f1010(a,b):
    return max(0,8-a-b)+a*max(0,b-3)+b*max(0,a-3)

def f3(a,b):
    return max(0,9-a-b)+a*(b-1)+b*max(0,a-2)

def f4(a,b):
    return max(0,8-a-b)+a*(b-1)+b*max(0,a-2)

def f5(a,b):
    return max(0,9-a-b)+a*max(0,b-2)+b*max(0,a-2)

def minima(fn, lo=1, hi=11):
    values = [(fn(a,b),a,b) for a in range(lo,hi+1) for b in range(lo,hi+1)]
    minimum = min(x[0] for x in values)
    return {
        "minimum": minimum,
        "argmin": [[a,b] for value,a,b in values if value == minimum],
        "domain": [lo,hi],
    }

def main():
    supports = support_orbits()
    total = sum(len(rows) for rows in supports.values())
    assert [len(supports[str(h)]) for h in (3,4,5)] == [2,3,5]
    assert total == 10
    scalar = {
        "f11": minima(f11),
        "f10_11": minima(f1011),
        "f9_11": minima(f911),
        "f10_10": minima(f1010),
        "star_three_pairs": minima(f3),
        "two_mixed_pairs_K9": minima(f4),
        "mixed_K10_K11": minima(f5),
    }
    assert scalar["f11"]["minimum"] >= 6
    assert scalar["f10_11"]["minimum"] >= 4
    assert scalar["f9_11"]["minimum"] >= 2
    assert scalar["f10_10"]["minimum"] >= 2
    assert scalar["star_three_pairs"]["minimum"] >= 6
    assert scalar["two_mixed_pairs_K9"]["minimum"] >= 5
    assert scalar["mixed_K10_K11"]["minimum"] >= 5
    print(json.dumps({
        "status": "PASS",
        "support_orbit_counts": {k:len(v) for k,v in supports.items()},
        "total_support_orbits": total,
        "support_orbits": supports,
        "scalar_minima": scalar,
        "scope": "finite support-orbit and scalar-inequality checks only; not a proof of the analytic blocker accounting",
    }, indent=2))

if __name__ == "__main__":
    main()
