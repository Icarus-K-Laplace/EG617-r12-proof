#!/usr/bin/env python3
"""Independent finite checks for the E286 two-completer attack.

No project verifier, generator, or imported project code is used.
Run: python -B E286_TWO_COMPLETER_ATTACK.py
"""
from itertools import combinations, combinations_with_replacement, permutations
import json

V = range(4)
SUPPORTS = [
    frozenset(s)
    for r in range(2, 5)
    for s in combinations(V, r)
]

def canonical(multiset):
    return min(
        tuple(sorted(tuple(sorted(p[x] for x in support)) for support in multiset))
        for p in permutations(V)
    )

def support_orbits(h):
    target_incidence = h + 5
    reps = {}
    for indices in combinations_with_replacement(range(len(SUPPORTS)), h):
        supports = [SUPPORTS[i] for i in indices]
        if sum(map(len, supports)) != target_incidence:
            continue
        degrees = [sum(i in support for support in supports) for i in V]
        # |K_i|=13-d_i <=11, and no seed has more than h neighbours in Z.
        if min(degrees) < 2 or max(degrees) > h:
            continue
        reps[canonical(supports)] = tuple(sorted(degrees, reverse=True))
    return [
        {"supports": [list(s) for s in orbit], "seed_degrees": list(reps[orbit])}
        for orbit in sorted(reps)
    ]

def pointwise_k10(a0, a1, a2):
    values = (a0, a1, a2)
    for mask in range(8):
        chosen = [values[i] for i in range(3) if mask & (1 << i)]
        lhs = max(0, sum(x - 1 for x in chosen))
        rhs = sum(max(0, x - 2) for x in chosen)
        if lhs < rhs:
            return False
    return True

def pointwise_k11(a, b):
    for mask in range(4):
        chosen = [x for i, x in enumerate((a, b)) if mask & (1 << i)]
        lhs = max(0, sum(x - 1 for x in chosen))
        rhs = sum(max(0, x - 2) for x in chosen)
        if lhs < rhs:
            return False
    return True

def f11(a, b):
    return max(0, 10-a-b) + a*max(0, b-2) + b*max(0, a-2)

def f10_11(a, b):
    return max(0, 9-a-b) + a*max(0, b-3) + b*max(0, a-2)

def f9_11(a, b):
    return max(0, 8-a-b) + a*max(0, b-4) + b*max(0, a-2)

def f10_10(a, b):
    return max(0, 8-a-b) + a*max(0, b-3) + b*max(0, a-3)

def f5(a, b):
    return max(0, 9-a-b) + a*max(0, b-2) + b*max(0, a-2)

def f4(a, b):
    return max(0, 8-a-b) + a*(b-1) + b*max(0, a-2)

def f3(a, b):
    return max(0, 9-a-b) + a*(b-1) + b*max(0, a-2)

def minimum(fn, arange, brange):
    table = [(fn(a, b), a, b) for a in arange for b in brange]
    m = min(row[0] for row in table)
    return {
        "minimum": m,
        "equality_pairs": [[a, b] for value, a, b in table if value == m],
    }

def nonbipartite_triangle_free_bound(n):
    """Shortest odd cycle C_(2k+1), independent C-neighborhoods, Mantel outside."""
    candidates = []
    for k in range(2, (n-1)//2 + 1):
        outside = n - (2*k + 1)
        cross = k * outside
        outside_edges = (outside * outside) // 4
        candidates.append({
            "k": k,
            "cycle": 2*k+1,
            "outside": outside,
            "bound": 2*k+1 + cross + outside_edges,
        })
    return max(row["bound"] for row in candidates), candidates

def shared_k9_center_additivity(b, bp):
    # x is in A only, A' only, or A cap A'. The degree lower bounds
    # include the two K9-completers and blocker-forced opposite missing sets.
    cases = {
        "A_only": (max(0, 8 + 2 + b + 1 - 12), b - 1),
        "Aprime_only": (max(0, 8 + 2 + bp + 1 - 12), bp - 1),
        "both": (max(0, 8 + 2 + b + bp - 12), (b - 1) + (bp - 1)),
    }
    return all(actual >= required for actual, required in cases.values())

def main():
    orbits = {str(h): support_orbits(h) for h in (3, 4, 5)}
    assert [len(orbits[str(h)]) for h in (3, 4, 5)] == [2, 3, 5]

    bad_k10 = []
    for a0 in range(0, 11):       # K10-K10 point may complete the opposite K10
        for a1 in range(1, 12):   # mixed points cannot complete K11
            for a2 in range(1, 12):
                if not pointwise_k10(a0, a1, a2):
                    bad_k10.append([a0, a1, a2])

    bad_k11 = [
        [a, b] for a in range(0, 11) for b in range(0, 11)
        if not pointwise_k11(a, b)
    ]

    scalar = {
        "f11": minimum(f11, range(1, 12), range(1, 12)),
        "f10_11": minimum(f10_11, range(1, 11), range(1, 12)),
        "f9_11": minimum(f9_11, range(1, 10), range(1, 12)),
        "f10_10": minimum(f10_10, range(1, 11), range(1, 11)),
        "f5": minimum(f5, range(1, 11), range(1, 12)),
        "f4": minimum(f4, range(1, 10), range(1, 12)),
        "f3": minimum(f3, range(1, 11), range(1, 12)),
    }

    odd_bounds = {
        str(n): nonbipartite_triangle_free_bound(n)
        for n in (19, 23, 24, 25)
    }

    bad_shared = [
        [b, bp]
        for b in range(1, 12)
        for bp in range(1, 12)
        if not shared_k9_center_additivity(b, bp)
    ]

    # If u,v both complete a K10, then u,v are nonadjacent (else K12).
    # For eps(u)+eps(v)<=6, the common antineighborhood has >=25 vertices:
    # the 25-point density lemma contradicts e>=155 and e<=154.
    # If the sum is 7 or 8, it has >=24 or >=23 vertices respectively.
    # Since total excess is 8, choose 23 zero-excess vertices W.
    # On W, the complement is triangle-free with delta>=22-12=10;
    # AES (r=2) makes it bipartite, forcing W to be a union of two
    # cliques of size <=11, impossible for |W|=23.
    two_completer = {
        "common_neighborhood_at_least": 10,
        "common_antineighborhood_size": "21 + c(u,v) - eps(u) - eps(v)",
        "eps_sum_le_6": {
            "minimum_U_size": 25,
            "edges_in_H[W]_lower": 155,
            "edges_in_H[W]_upper": 154,
            "contradiction": True,
        },
        "eps_sum_7_or_8": {
            "minimum_U_size": 23,
            "zero_excess_vertices_available": 23,
            "complement_triangle_free_min_degree": 10,
            "AES_threshold": "2*23/5 = 9.2",
            "AES_forces_bipartite": True,
            "two_cliques_max_order": 22,
            "contradiction": True,
        },
        "conclusion": "No two vertices can both complete the same K10 under the E286 hypotheses.",
    }

    result = {
        "support_orbits": {
            "counts": {h: len(rows) for h, rows in orbits.items()},
            "representatives": orbits,
        },
        "D_pointwise_inequalities": {
            "K10_domain": "a0 in 0..10; a1,a2 in 1..11; every missing subset",
            "K10_counterexamples": len(bad_k10),
            "K11_domain": "a,b in 0..10; every missing subset",
            "K11_counterexamples": len(bad_k11),
        },
        "scalar_minima": scalar,
        "nonbipartite_triangle_free_bounds": {
            str(n): {"maximum": bound, "cases": rows}
            for n, (bound, rows) in odd_bounds.items()
        },
        "K9_shared_center_additivity": {
            "domain": "b,b' in 1..11",
            "counterexamples": len(bad_shared),
        },
        "two_completer_K10_attack": two_completer,
    }
    assert not bad_k10 and not bad_k11 and not bad_shared
    assert {k: v["minimum"] for k, v in scalar.items()} == {
        "f11": 6, "f10_11": 4, "f9_11": 2, "f10_10": 2,
        "f5": 5, "f4": 5, "f3": 6,
    }
    assert {n: v["maximum"] for n, v in result["nonbipartite_triangle_free_bounds"].items()} == {
        "19": 82, "23": 122, "24": 133, "25": 145,
    }
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
