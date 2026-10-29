#!/usr/bin/env python3
"""Exact arithmetic regression for V47_Z01_BALANCED_COLORING_CROSS_TRACK_LEDGER.md.

Enumerate all small-block excess vectors epsilon=(epsilon_0,...,epsilon_3)
with sum 2 and epsilon_0<=1, then all triples for A,B,C. For each triple,
enumerate aggregate track-pair edge counts satisfying the necessary degree
equations, pair-capacity bounds, and total cross-edge count 32.

This checks arithmetic consistency and the size of the aggregate relaxation;
it is not a graph-completion search or a Q32 UNSAT certificate.
"""
from itertools import product

VECTORS = [
    (e0, e1, e2, e3)
    for e0 in range(2)
    for e1 in range(3)
    for e2 in range(3)
    for e3 in range(3)
    if e0 + e1 + e2 + e3 == 2
]
assert len(VECTORS) == 9

epsilon_triples = 0
aggregate_states = 0
states_by_E0 = {0: 0, 1: 0, 2: 0, 3: 0}

for triple in product(VECTORS, repeat=3):
    epsilon_triples += 1
    E = tuple(sum(v[h] for v in triple) for h in range(4))
    E0 = E[0]
    assert 0 <= E0 <= 3
    assert sum(E) == 6

    total_0_big = 22 + E0
    total_big_big = 10 - E0
    assert total_0_big + total_big_big == 32
    assert 7 <= total_big_big <= 10
    assert 22 <= total_0_big <= 25

    # y_i is the number of H edges between T_0 and T_i; each T_0 vertex
    # has at most one neighbor in each T_i, so y_i <= 11.
    for y1 in range(12):
        for y2 in range(12):
            y3 = total_0_big - y1 - y2
            if not 0 <= y3 <= 11:
                continue
            y = (y1, y2, y3)

            # For each big track i, its degree sum is 12+E_i.
            # Subtracting its T_0 incidence y_i leaves the two big-big
            # pair counts incident to i.
            d = tuple(12 + E[i + 1] - y[i] for i in range(3))
            numerators = (
                d[0] + d[1] - d[2],  # 2 e_12
                d[0] + d[2] - d[1],  # 2 e_13
                d[1] + d[2] - d[0],  # 2 e_23
            )
            if any(n % 2 for n in numerators):
                continue
            x12, x13, x23 = (n // 2 for n in numerators)
            x = (x12, x13, x23)
            if any(v < 0 or v > 12 for v in x):
                continue
            if sum(x) != total_big_big:
                continue

            aggregate_states += 1
            states_by_E0[E0] += 1

assert epsilon_triples == 729
assert aggregate_states == 28107
assert states_by_E0 == {0: 9828, 1: 12420, 2: 5157, 3: 702}

print("ordered small-block excess triples:", epsilon_triples)
print("necessary aggregate track-count states:", aggregate_states)
print("aggregate states by E0:", states_by_E0)
print("V47_Z01_CROSS_TRACK_ARITHMETIC_OK")
print("Scope: aggregate integer relaxation only; not global Q32 UNSAT.")
