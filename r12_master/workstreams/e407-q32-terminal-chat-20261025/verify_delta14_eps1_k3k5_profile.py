#!/usr/bin/env python3
"""Arithmetic replay for DELTA14_EPS1_K3K5K5K5_NO_CROSS_EDGE.md.

The script checks exact W-edge/excess counts and all possible component-excess
allocations. It does not machine-verify the analytic saturation lemmas.
"""
from itertools import product

N_U = 29
TOTAL_EXCESS = 2 * 284 - 12 * 47
EPS_U = 1
EPS_W = TOTAL_EXCESS - EPS_U
assert TOTAL_EXCESS == 4 and EPS_W == 3
assert 3 * 2 // 2 + 3 * (5 * 4 // 2) == 33
assert sum(s * (s - 1) // 2 for s in (3, 5, 5, 5)) == 33

allocations = []
for E0, E1, E2, E3 in product(range(EPS_W + 1), repeat=4):
    if E0 + E1 + E2 + E3 != EPS_W:
        continue
    allocations.append((E0, E1, E2, E3))
    cap = 10 + E0 // 3 + (5 + E1) + (5 + E2) + (5 + E3)
    assert cap == 28 - E0 + E0 // 3
    assert cap <= 28

assert len(allocations) == 20
assert max(28 - E0 + E0 // 3 for E0 in range(4)) == 28
print("PASS: e(H[W])=33 and W-excess=3.")
print("PASS: all 20 component-excess allocations give cover capacity <=28 < 29.")
print("LIMIT: analytic saturation, reverse-saturation, and edge-label arguments remain in the Markdown proof.")
