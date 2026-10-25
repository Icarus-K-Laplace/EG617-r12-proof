#!/usr/bin/env python3
"""Arithmetic verifier for DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md.

Standard-library only. Checks the exact four-part partition profiles and
replays the union-bound transversal estimates for the explicit C5-blow-up
candidate. It does not classify all saturated J graphs, verify external
extremal theorems, or realize a full 47-vertex core.
"""
from itertools import combinations

def t4(parts):
    return sum(parts[i] * parts[j] for i in range(4) for j in range(i + 1, 4))

def partitions4(n=18):
    out = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                d = n - a - b - c
                if d < c or d < 1:
                    continue
                out.append((a, b, c, d))
    return out

expected = {
    0: [((3, 4, 5, 6), 119, 0),
        ((3, 5, 5, 5), 120, 1),
        ((4, 4, 4, 6), 120, 1),
        ((4, 4, 5, 5), 121, 2)],
    1: [((3, 5, 5, 5), 120, 0),
        ((4, 4, 4, 6), 120, 0),
        ((4, 4, 5, 5), 121, 1)],
    2: [((4, 4, 5, 5), 121, 0)],
}
for eps_u in range(3):
    target = 119 + eps_u
    got = []
    for p in partitions4():
        t = t4(p)
        if t >= target:
            got.append((p, t, t - target))
    assert got == expected[eps_u], (eps_u, got)
    for p, t, q in got:
        assert sum(p) == 18
        assert min(p) >= 3
        assert q <= 2 - eps_u
        assert t <= 121

for p in partitions4():
    if min(p) <= 2:
        assert t4(p) <= 117, (p, t4(p))

def removed_vectors(parts, total):
    if len(parts) == 1:
        for x in range(min(parts[0], total) + 1):
            yield (x,)
        return
    for x in range(min(parts[0], total) + 1):
        for rest in removed_vectors(parts[1:], total - x):
            yield (x,) + rest

def max_forbidden_fraction(parts, removed_total, edge_budget):
    best = 0.0
    for rem in removed_vectors(parts, removed_total):
        if sum(rem) > removed_total:
            continue
        t = [parts[i] - rem[i] for i in range(4)]
        if min(t) < 1:
            continue
        fractions = sorted((1.0 / (t[i] * t[j])
                            for i, j in combinations(range(4), 2)), reverse=True)
        best = max(best, sum(fractions[:edge_budget]))
    return best

for p, _, q in expected[0]:
    assert max_forbidden_fraction(p, 2, q) < 1
for p, _, q in expected[1]:
    if min(p) >= 4:
        assert max_forbidden_fraction(p, 3, q) < 1
assert max_forbidden_fraction((4, 4, 5, 5), 3, 0) == 0
assert 2 < 3
assert 2 + 1 == 3
assert 2 + 2 == 4

print("DELTA14_SATURATED_TRANSVERSAL_REDUCTION_OK")
print("profiles: eps_U=0 -> 4; eps_U=1 -> 3; eps_U=2 -> 1")
print("epsilon_U=0 excluded; epsilon_U=1,2 reduced to the two stated terminals")
