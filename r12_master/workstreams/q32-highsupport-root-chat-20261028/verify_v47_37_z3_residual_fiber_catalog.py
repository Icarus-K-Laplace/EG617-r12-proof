#!/usr/bin/env python3
"""Exact finite audit of the m=10, 3+7, z=3 residual/fiber frontier.

Pure-stdlib verifier. Enumerates all disjoint unions of K1, paths, and cycles
on seven vertices satisfying e(R)=6, alpha(R)<=4, and clique-cover number <=4;
then checks every four-label clique partition with a registered fiber profile.
It also audits the double-track fiber-size floor. This is a local structural
regression, not a Q32 UNSAT certificate.
"""
from itertools import combinations, product
from collections import defaultdict

PROFILES = {
    (3, 3, 1, 0), (3, 2, 2, 0),
    (3, 2, 1, 1), (2, 2, 2, 1),
}
EXPECTED = {
    ("C3", "C3", "K1"): {
        (3, 3, 1, 0): 24, (3, 2, 1, 1): 144,
    },
    ("C6", "K1"): {(2, 2, 2, 1): 48},
    ("C5", "P2"): {(2, 2, 2, 1): 120},
    ("C4", "P3"): {(2, 2, 2, 1): 96},
    ("C3", "P4"): {
        (3, 2, 2, 0): 24, (3, 2, 1, 1): 72,
        (2, 2, 2, 1): 72,
    },
    ("P7",): {(2, 2, 2, 1): 96},
}

def metrics(kind, n):
    if kind == "K":
        return 0, 1, 1
    if kind == "P":
        return n - 1, (n + 1) // 2, (n + 1) // 2
    if kind == "C":
        return n, n // 2, 1 if n == 3 else (n + 1) // 2
    raise ValueError(kind)

TYPES = [("K", 1)] + [("P", n) for n in range(2, 8)] + [
    ("C", n) for n in range(3, 8)
]
TYPES.sort(key=lambda t: (t[1], {"K": 0, "P": 1, "C": 2}[t[0]]))

def enumerate_component_types():
    found = set()
    def rec(start, vertices, edges, alpha, cover, chosen):
        if vertices == 7:
            if edges == 6 and alpha <= 4 and cover <= 4:
                found.add(tuple(sorted(chosen)))
            return
        if vertices > 7:
            return
        for i in range(start, len(TYPES)):
            kind, n = TYPES[i]
            e, a, c = metrics(kind, n)
            if vertices + n > 7 or edges + e > 6:
                continue
            rec(i, vertices+n, edges+e, alpha+a, cover+c,
                chosen+[f"{kind}{n}"])
    rec(0, 0, 0, 0, 0, [])
    return found

def component_edges(kind, n, start):
    if kind == "K":
        return []
    if kind == "P":
        return [(start+i, start+i+1) for i in range(n-1)]
    return [(start+i, start+(i+1) % n) for i in range(n)]

def build_graph(signature):
    edges, start = set(), 0
    for item in signature:
        kind, n = item[0], int(item[1:])
        edges.update(tuple(sorted(e)) for e in component_edges(kind, n, start))
        start += n
    assert start == 7
    return edges

def alpha_number(edges):
    best = 0
    for mask in range(1 << 7):
        vertices = [v for v in range(7) if mask & (1 << v)]
        if all(tuple(sorted((u, v))) not in edges
               for u, v in combinations(vertices, 2)):
            best = max(best, len(vertices))
    return best

def partition_profile_counts(signature):
    edges = build_graph(signature)
    counts = defaultdict(int)
    for labels in product(range(4), repeat=7):
        profile = tuple(sorted((labels.count(i) for i in range(4)),
                               reverse=True))
        if profile not in PROFILES:
            continue
        if any(labels[u] == labels[v]
               and tuple(sorted((u, v))) not in edges
               for u, v in combinations(range(7), 2)):
            continue
        counts[profile] += 1
    return dict(counts)

def double_track_pair_catalog(signature):
    """Small-map profiles/pairs whose two fibers are completely joined."""
    edges = build_graph(signature)
    out = set()
    for labels in product(range(4), repeat=7):
        sizes = tuple(labels.count(i) for i in range(4))
        profile = tuple(sorted(sizes, reverse=True))
        if profile not in PROFILES:
            continue
        if any(labels[u] == labels[v]
               and tuple(sorted((u, v))) not in edges
               for u, v in combinations(range(7), 2)):
            continue
        for i, j in combinations(range(4), 2):
            a, b = sizes[i], sizes[j]
            if a+b > 3:
                continue
            if all(tuple(sorted((u, v))) in edges
                   for u in range(7) if labels[u] == i
                   for v in range(7) if labels[v] == j):
                out.add((profile, tuple(sorted((a, b), reverse=True))))
    return out

def check_double_track_floor():
    expected = {
        (3, 3, 1, 0): {(3, 0, 0), (1, 0, 0)},
        (3, 2, 2, 0): {(3, 0, 1), (2, 0, 1)},
        (3, 2, 1, 1): {(2, 1, 0), (1, 1, 1)},
        (2, 2, 2, 1): {(2, 1, 1)},
    }
    for profile in PROFILES:
        internal = sum(n*(n-1)//2 for n in profile)
        cross_budget = 6 - internal
        got = set()
        for i, j in combinations(range(4), 2):
            a, b = profile[i], profile[j]
            if a+b <= 3:
                required_cross = a*b
                assert required_cross <= cross_budget
                got.add((max(a, b), min(a, b), cross_budget-required_cross))
        assert got == expected[profile], (profile, got, expected[profile])
    return expected

def main():
    types = enumerate_component_types()
    assert types == set(EXPECTED), (types, set(EXPECTED))
    print("z=3 residual component types:", len(types))
    for signature in sorted(types):
        edges = build_graph(signature)
        degree = [sum(tuple(sorted((v, u))) in edges
                      for u in range(7) if u != v) for v in range(7)]
        assert len(edges) == 6 and max(degree) <= 2
        assert alpha_number(edges) <= 4
        counts = partition_profile_counts(signature)
        assert counts == EXPECTED[signature], (signature, counts, EXPECTED[signature])
        deficit = [2-d for d in degree]
        assert sum(deficit) == 2 and all(x >= 0 for x in deficit)
        assert sorted(x for x in deficit if x) in ([2], [1, 1])
        print(f"{'+'.join(signature)}: {sorted(counts, reverse=True)}; "
              f"{sum(counts.values())} labelled partitions")
    floors = check_double_track_floor()
    print("double-track fiber-size/cross-edge floor:")
    for profile in sorted(PROFILES, reverse=True):
        print(f"  {profile}: {sorted(floors[profile], reverse=True)}")
    expected_double = {
        ("C3", "C3", "K1"): {
            ((3, 3, 1, 0), (3, 0)),
            ((3, 3, 1, 0), (1, 0)),
            ((3, 2, 1, 1), (2, 1)),
        },
        ("C3", "P4"): {
            ((3, 2, 2, 0), (3, 0)),
            ((3, 2, 2, 0), (2, 0)),
            ((3, 2, 1, 1), (1, 1)),
            ((2, 2, 2, 1), (2, 1)),
        },
    }
    for signature in types:
        got = double_track_pair_catalog(signature)
        assert got == expected_double.get(signature, set()), (
            signature, got, expected_double.get(signature, set()))
    print("double-track-capable residual types: 2")
    print("V47_37_Z3_RESIDUAL_FIBER_CATALOG_OK")
    print("Scope: local residual/fiber enumeration only; no Q32 closure.")

if __name__ == "__main__":
    main()
