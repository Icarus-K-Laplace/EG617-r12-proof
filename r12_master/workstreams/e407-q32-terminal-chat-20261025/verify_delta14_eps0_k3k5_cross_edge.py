#!/usr/bin/env python3
"""Arithmetic replay for DELTA14_EPS0_K3K5K5K5_CROSS_EDGE_CLOSURE.md.

This checks all finite degree/capacity arithmetic and all integer excess
allocations. It does not machine-verify the analytic independent-set lemmas.
"""
from itertools import product

N_U = 29
W_SIZES = (3, 5, 5, 5)
TOTAL_EXCESS = 2 * 284 - 12 * 47
assert TOTAL_EXCESS == 4
assert sum(W_SIZES) == 18
assert sum(s * (s - 1) // 2 for s in W_SIZES) + 1 == 34

# If a vertex misses every W component, its non-neighbour sets at the
# cross-edge endpoints are singletons; the other two sets are nonempty.
max_non_neighbours_C3_K5 = 1 + 1 + 5 + 5
max_non_neighbours_K5_K5 = 1 + 1 + 3 + 5
assert max_non_neighbours_C3_K5 == 12
assert max_non_neighbours_K5_K5 == 10
# A D vertex has W degree 5-t_d <= 5, hence >=13 W non-neighbours.
assert 18 - 5 > max_non_neighbours_C3_K5
# U vertices have W degree 5 or 6; degree 5 means 13 non-neighbours.
assert 18 - 5 > max_non_neighbours_C3_K5
assert 18 - 6 == max_non_neighbours_C3_K5

# Exceptional U-vertex branch: S_2 union S_3 must contain >=15-e_y
# vertices, while its capacity is <=10+E_2+E_3 <=14-e_y.
for e_y in range(5):
    lower = 15 - e_y
    upper = 10 + (4 - e_y)
    assert lower == upper + 1
    assert lower > upper

# All weak excess allocations among the four W-components sum to 4.
allocations = []
for E0, E1, E2, E3 in product(range(5), repeat=4):
    if E0 + E1 + E2 + E3 != TOTAL_EXCESS:
        continue
    allocations.append((E0, E1, E2, E3))
    # Cross-edge C3--K5: 9+4+5+5 + total excess = 27.
    cap_c3_k5 = (9 + E0) + (4 + E1) + (5 + E2) + (5 + E3)
    # Cross-edge K5--K5: 10+4+4+5 + total excess = 27.
    cap_k5_k5 = (10 + E0) + (4 + E1) + (4 + E2) + (5 + E3)
    assert cap_c3_k5 == 27
    assert cap_k5_k5 == 27

assert len(allocations) == 35
print("PASS: W has 18 vertices and 34 edges; core excess is 4.")
print("PASS: non-saturation limits are 12 (C3--K5) and 10 (K5--K5).")
print("PASS: exceptional-vertex capacity gap is exactly 1 for every epsilon_y.")
print("PASS: all 35 W-excess allocations give common-neighbour cover capacity 27 < 29.")
print("LIMIT: analytic saturation and edge-label arguments remain in the Markdown proof.")
