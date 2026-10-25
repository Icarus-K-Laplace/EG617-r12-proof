#!/usr/bin/env python3
"""Arithmetic replay for the explicit saturated-candidate W-extension exclusion.

Checks finite W-profile enumeration, the one-cross-edge transversal fractions,
and the small assignment-capacity arithmetic used in the proof. It does not
machine-check the graph-theoretic independent-set arguments or classify all
admissible local J graphs.
"""
from itertools import product, combinations

def cross_sum(parts):
    return sum(parts[i] * parts[j] for i in range(4) for j in range(i + 1, 4))

def partitions4(n=18):
    out = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                d = n - a - b - c
                if d >= c and d >= 1:
                    out.append((a, b, c, d))
    return out

expected = {
    1: [((3, 5, 5, 5), 120, 0),
        ((4, 4, 4, 6), 120, 0),
        ((4, 4, 5, 5), 121, 1)],
    2: [((4, 4, 5, 5), 121, 0)],
}
for eps_u in (1, 2):
    got = []
    target = 119 + eps_u
    for p in partitions4():
        val = cross_sum(p)
        if val >= target:
            got.append((p, val, val - target))
    assert got == expected[eps_u], (eps_u, got)

# eps_U=1, K3 + 3K5: no disjoint-support assignment of 7 A-vertices and
# 7 B-vertices to the three K5 parts if each part can hold at most 6 from
# one side and no part can be assigned to both sides.
caps3 = (6, 6, 6)
assignments3 = []
for A in product(*(range(c + 1) for c in caps3)):
    if sum(A) != 7:
        continue
    for B in product(*(range(c - A[i] + 1) for i, c in enumerate(caps3))):
        if sum(B) == 7 and all(not (A[i] and B[i]) for i in range(3)):
            assignments3.append((A, B))
assert assignments3 == [], assignments3

# Edge-incidence budget checks behind the A/B assignment lemmas:
# K3 vs K3: six extra incidences cannot fully cover two K5 parts (10 needed).
assert 3 + 3 == 6 < 2 * 5
# K3 vs K5: four extra incidences cannot fully cover a K5.
assert 3 + 1 == 4 < 5
# A/B assigned to the same K5: two extra incidences cannot cover a K5.
assert 1 + 1 == 2 < 5

# One cross-edge in parts (4,4,5,5): deleting at most three vertices leaves
# an independent transversal. The cross-edge forbids fraction 1/(t_i*t_j).
def removals(total, n=4):
    if n == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for rest in removals(total - x, n - 1):
            yield (x,) + rest

parts = (4, 4, 5, 5)
worst = 0.0
for s in range(4):
    for rem in removals(s):
        left = tuple(parts[i] - rem[i] for i in range(4))
        assert min(left) >= 1
        for i, j in combinations(range(4), 2):
            frac = 1 / (left[i] * left[j])
            worst = max(worst, frac)
            assert frac < 1
assert worst <= 0.25

# eps_U=2: A/B assignment supports are disjoint among capacities (7,6,6).
caps = (7, 6, 6)  # P1(K4), P2(K5), P3(K5)
solutions = []
for A in product(*(range(c + 1) for c in caps)):
    if sum(A) != 7:
        continue
    for B in product(*(range(c - A[i] + 1) for i, c in enumerate(caps))):
        if sum(B) == 7 and all(not (A[i] and B[i]) for i in range(3)):
            solutions.append((A, B))
assert len(solutions) == 12, len(solutions)
assert all(
    (A == (7, 0, 0) and B[0] == 0) or
    (B == (7, 0, 0) and A[0] == 0)
    for A, B in solutions
)

# The opposite side's seven vertices split across P2/P3 with 1<=b_i<=6.
b_splits = [(b2, 7 - b2) for b2 in range(1, 7)]
assert len(b_splits) == 6
assert all(1 <= b2 <= 6 and 1 <= b3 <= 6 for b2, b3 in b_splits)
assert all(max(b2, b3) >= 4 for b2, b3 in b_splits)
# If b_i>=4, four A-complete vertices in P_i each require epsilon_w>=3.
assert 4 * 3 == 12 > 2  # total W-excess when epsilon_U=2

print("DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION_ARITHMETIC_OK")
print("eps_U=1: all 3 W profiles exhausted; K3+3K5 A/B assignment impossible")
print("cross-edge transversal forbidden fraction <=", worst)
print("eps_U=2: 12 A/B assignment patterns; every B split forces >=12 excess if compatible")
