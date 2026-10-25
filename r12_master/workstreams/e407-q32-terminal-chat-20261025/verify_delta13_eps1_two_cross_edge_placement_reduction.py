#!/usr/bin/env python3
"""Finite excess/load enumeration for the delta-13 2K4+2K5, two-cross-edge profile.

Checks only integer excess allocations and component capacity bounds. It does
not certify the analytic transversal/reverse-saturation lemmas or the remaining
same-pair K4/K5 terminals.
"""
from itertools import product

def cap4(E, e):
    return 8 + int(E >= e)

def cap5(E, e):
    return min(5 + E - e, 7)

def max_capacity(edge_incidence):
    best = -1
    arg = None
    for E in product(range(4), repeat=4):
        if sum(E) != 3:
            continue
        caps = [cap4(E[i], edge_incidence[i]) for i in range(2)]
        caps += [cap5(E[i], edge_incidence[i]) for i in range(2, 4)]
        total = sum(caps)
        if total > best:
            best, arg = total, (E, caps)
    return best, arg

# Edge-incidence vectors (C1,C2 are K4; C3,C4 are K5).
expected = {
    "disjoint_different_pairs": ((1, 1, 1, 1), 27),
    "shared_K4_different_pairs": ((2, 1, 1, 0), 28),
    "shared_K5_different_pairs": ((1, 0, 2, 1), 27),
    "same_pair_K4K4": ((2, 2, 0, 0), 29),
    "same_pair_K4K5_disjoint": ((1, 0, 1, 0), 29),
    "same_pair_K4K5_star_at_K4": ((2, 0, 1, 0), 29),
    "same_pair_K4K5_star_at_K5": ((1, 0, 2, 0), 28),
    "same_pair_K5K5": ((0, 0, 2, 2), 27),
}
for name, (incidence, claimed) in expected.items():
    got, witness = max_capacity(incidence)
    assert got == claimed, (name, got, witness)

# The K5-K5 star has at most one nonsaturated U exception (degree 7 requires
# the unique U-excess unit), so its cover demand is at least 28 > capacity 27.
assert 29 - 1 == 28 > expected["same_pair_K5K5"][1]
# The two-edge profile has 32 clique edges plus two cross-edges.
assert 2 * 6 + 2 * 10 + 2 == 34
assert 48 - 1 - 13 == 34
assert 4 - 1 == 3

print("DELTA13_EPS1_TWO_CROSS_EDGE_PLACEMENT_REDUCTION_ARITHMETIC_OK")
for name, (incidence, claimed) in expected.items():
    print(name, "incidence=", incidence, "max_capacity=", claimed)
print("Closed: different component-pair placements and both K5-K5 placements.")
print("Open: K4-K4 matching/star; K4-K5 disjoint/star at either endpoint side.")
