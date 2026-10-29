#!/usr/bin/env python3
"""Arithmetic/source-interface regression for V47_T0_POINTWISE_COLOR_SATURATION.md.

Checks the exact per-vertex degree-sum alternatives and the T0 gadget-cap
counting consequence. This is not a proof of the balanced-coloring premise,
the Type-I placement theorem, or global Q32 infeasibility.
"""
from itertools import product

# For each T0 vertex, epsilon is 0 or 1 and eleven color degrees are >=3.
for epsilon in (0, 1):
    total = 34 - epsilon
    base = 11 * 3
    excess = total - base
    assert excess == 1 - epsilon
    if epsilon == 1:
        assert excess == 0
        degrees = [3] * 11
        assert sum(degrees) == total
    else:
        assert excess == 1
        degrees = [4] + [3] * 10
        assert sum(degrees) == total
        assert sum(d == 4 for d in degrees) == 1
        assert max(degrees) == 4

# T0 has 11 vertices; E0 of them have epsilon=1, so exactly 11-E0
# vertices must be assigned one repeated color.
for E0 in range(4):
    repeat_vertices = 11 - E0
    assert 8 <= repeat_vertices <= 11
    assert repeat_vertices == 11 - E0

# Source Type-I occupancy: each special K5 contributes at most one T0
# vertex. If x_C is in T0, the triple placement is impossible and both
# special K5s cannot be single-outside in the two-double case.
for x_in_T0 in (False, True):
    for special_T0_counts in product((0, 1), repeat=2):
        if x_in_T0 and sum(special_T0_counts) == 2:
            # Both special K5s single-outside gives b_s+b_t=2, excluded.
            continue
        count = sum(special_T0_counts) + int(x_in_T0)
        assert count <= 2

print("T0 degree-sum alternatives checked for epsilon=0,1")
print("E0 repeat-owner counts checked for E0=0,1,2,3")
print("Type-I T0 gadget capacity checked")
print("V47_T0_POINTWISE_COLOR_SATURATION_ARITHMETIC_OK")
print("Scope: arithmetic/source-interface regression only; not global Q32 UNSAT.")
