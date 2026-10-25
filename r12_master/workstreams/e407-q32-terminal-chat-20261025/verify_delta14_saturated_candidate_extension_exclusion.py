#!/usr/bin/env python3
"""Arithmetic replay for DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md.

Checks exact W-profile enumeration, finite A/B assignment capacities, and
the incidence-count inequalities used by the proof. It does not independently
verify the graph-theoretic saturation/independent-set lemmas or external
extremal theorems.
"""
from itertools import product, combinations


def cross_sum(parts):
    return sum(parts[i] * parts[j]
               for i in range(4) for j in range(i + 1, 4))


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
    0: [((3, 4, 5, 6), 119, 0),
        ((3, 5, 5, 5), 120, 1),
        ((4, 4, 4, 6), 120, 1),
        ((4, 4, 5, 5), 121, 2)],
    1: [((3, 5, 5, 5), 120, 0),
        ((4, 4, 4, 6), 120, 0),
        ((4, 4, 5, 5), 121, 1)],
    2: [((4, 4, 5, 5), 121, 0)],
}
for eps_u, rows in expected.items():
    target = 119 + eps_u
    got = []
    for p in partitions4():
        value = cross_sum(p)
        if value >= target:
            got.append((p, value, value - target))
    assert got == rows, (eps_u, got)
    assert all(min(p) >= 3 and q <= 2 - eps_u
               for p, _, q in got)

# epsilon_U=0: with |S|=2 removed, the two-edge union bound is strict.
assert 2 * (1 / 3) < 1
assert 2 * (1 / 4) < 1

# epsilon_U=1:
# K3 + 3K5: each K5 vertex must be complete to A, B, or all of C union E.
# A and B each have 42 W incidences, and each complete K5 vertex consumes 7.
assert 42 // 7 == 6
# Each of the four C/E vertices has only one W edge outside the K3,
# so at most one K5 vertex can be complete to all four.
assert 6 + 6 + 1 == 13 < 15
# 3K4 + K6: d0 has at most 3 W-neighbours, below every component size.
assert 2 + 1 < 4
# (4,4,5,5) plus one cross-edge: after deleting up to 3 vertices,
# the single edge forbids at most one quarter of the transversal choices.
assert 1 / (1 * 4) == 0.25 < 1

# epsilon_U=2: A/B assignments use disjoint supports with capacities 7,6,6.
caps = (7, 6, 6)
solutions = []
for A in product(*(range(c + 1) for c in caps)):
    if sum(A) != 7:
        continue
    for B in product(*(range(c - A[i] + 1) for i, c in enumerate(caps))):
        if sum(B) == 7 and all(not (A[i] and B[i]) for i in range(3)):
            solutions.append((A, B))
assert len(solutions) == 12, len(solutions)
assert all((A == (7, 0, 0) and B[0] == 0) or
           (B == (7, 0, 0) and A[0] == 0)
           for A, B in solutions)
# Thus one side fills P1, while the other splits across P2/P3.
assert 7 - 6 == 1  # each side must use P1 or both K5 parts
# A has at most 14 edges outside P1, so at most two K5 vertices can be
# complete to A. B2 and B3 are both nonempty; at most one vertex per K5
# part can be complete to B.
assert 14 // 7 == 2
assert 2 + 2 == 4 < 10

print("DELTA14_SATURATED_CANDIDATE_EXTENSION_ARITHMETIC_OK")
print("epsilon_U=0: transversal union bounds are strict")
print("epsilon_U=1: 3K4+K6 and 4,4,5,5+cross-edge excluded; K3+3K5 capacity 13<15")
print("epsilon_U=2: 12 assignment patterns; at most 4 of 10 K5 vertices can be complete to A or B")
