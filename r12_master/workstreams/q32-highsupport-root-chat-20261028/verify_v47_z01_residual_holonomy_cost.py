#!/usr/bin/env python3
"""Exhaustive residual holonomy-cost verifier for exact colors.

The seven residual vertices are 0,1 / 2,3 / 4,5 in T1,T2,T3 and 6 in T0.
A baseline has two disjoint matching edges between each pair of large parts
and one T0 edge into each large part: 64 baselines total. Extra C-edges must
form a matching within each track pair, have size at most 3, and make the
seven-vertex graph have independence number at most 2.

This is the exact local model induced by the ten isolated transversal K4s
and the residual one-factorizations. It is not a full Q32 completion solver.
"""
from itertools import combinations, product
from collections import Counter, defaultdict

N = 7
part = (0, 0, 1, 1, 2, 2, 3)
edges = [
    (u, v)
    for u in range(N)
    for v in range(u + 1, N)
    if part[u] != part[v]
]
assert len(edges) == 18
edge_bit = {e: 1 << i for i, e in enumerate(edges)}

def mask_of(edge_set):
    out = 0
    for u, v in edge_set:
        out |= edge_bit[tuple(sorted((u, v)))]
    return out

def alpha(mask):
    adj = [0] * N
    for (u, v), bit in edge_bit.items():
        if mask & bit:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    best = 0
    for subset in range(1 << N):
        size = subset.bit_count()
        if size <= best:
            continue
        if all(not ((subset >> v) & 1 and (adj[v] & subset)) for v in range(N)):
            best = size
    return best

def big_part_alpha(base_edges):
    mask = mask_of([e for e in base_edges if e[0] < 6 and e[1] < 6])
    adj = [0] * 6
    for (u, v), bit in edge_bit.items():
        if u < 6 and v < 6 and mask & bit:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    best = 0
    for subset in range(1 << 6):
        size = subset.bit_count()
        if size <= best:
            continue
        if all(not ((subset >> v) & 1 and (adj[v] & subset)) for v in range(6)):
            best = size
    return best

def baseline(matching_switches, t0_choices):
    big = ((0, 1), (2, 3), (4, 5))
    out = []
    for (i, j), switch in zip(((0, 1), (0, 2), (1, 2)), matching_switches):
        for a in range(2):
            b = a ^ switch
            out.append((big[i][a], big[j][b]))
    for i, choice in enumerate(t0_choices):
        out.append((6, big[i][choice]))
    assert len(out) == 9
    return out

def extra_is_pairwise_matching(extra):
    for i in range(4):
        for j in range(i + 1, 4):
            pair = [e for e in extra if {part[e[0]], part[e[1]]} == {i, j}]
            used = set()
            for u, v in pair:
                if u in used or v in used:
                    return False
                used.add(u)
                used.add(v)
    return True

baseline_counts = Counter()
repair_counts = Counter()
minimum_gap = {}
minimum_repairs = Counter()
baselines = 0

for switches in product((0, 1), repeat=3):
    for t0_choices in product((0, 1), repeat=3):
        base_edges = baseline(switches, t0_choices)
        base_mask = mask_of(base_edges)
        assert base_mask.bit_count() == 9
        big_alpha = big_part_alpha(base_edges)
        full_alpha = alpha(base_mask)

        if big_alpha == 2 and full_alpha == 2:
            cls = "A"
        elif big_alpha == 2 and full_alpha == 3:
            cls = "B"
        elif big_alpha == 3 and full_alpha == 3:
            cls = "C"
        elif big_alpha == 3 and full_alpha == 4:
            cls = "D"
        else:
            raise AssertionError((switches, t0_choices, big_alpha, full_alpha))

        baselines += 1
        baseline_counts[cls] += 1
        available = [e for e in edges if not (base_mask & edge_bit[e])]

        for gap in range(4):
            for extra in combinations(available, gap):
                if not extra_is_pairwise_matching(extra):
                    continue
                if alpha(base_mask | mask_of(extra)) > 2:
                    continue
                repair_counts[(cls, gap)] += 1
                old = minimum_gap.get(cls, 4)
                if gap < old:
                    minimum_gap[cls] = gap
                if gap == minimum_gap[cls]:
                    minimum_repairs[cls] += 1

assert baselines == 64
assert baseline_counts == Counter({"A": 8, "B": 24, "C": 24, "D": 8})
assert minimum_gap == {"A": 0, "B": 1, "C": 2, "D": 3}
assert minimum_repairs == Counter({"A": 8, "B": 24, "C": 72, "D": 72})
assert repair_counts == Counter({
    ("A", 0): 8, ("A", 1): 72, ("A", 2): 288, ("A", 3): 672,
    ("B", 1): 24, ("B", 2): 288, ("B", 3): 1152,
    ("C", 2): 72, ("C", 3): 720,
    ("D", 3): 72,
})

print("baselines:", baselines)
print("baseline classes:", dict(sorted(baseline_counts.items())))
print("minimum gap by class:", dict(sorted(minimum_gap.items())))
print("minimum-size repairs:", dict(sorted(minimum_repairs.items())))
print("all repair counts:", dict(sorted(repair_counts.items())))
print("V47_Z01_RESIDUAL_HOLONOMY_COST_OK")
print("Scope: exact local residual model only; not global Q32 UNSAT.")
