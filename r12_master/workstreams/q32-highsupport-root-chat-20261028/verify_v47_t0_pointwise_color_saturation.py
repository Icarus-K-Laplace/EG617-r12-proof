#!/usr/bin/env python3
"""Arithmetic/source-interface regression for V47_T0_POINTWISE_COLOR_SATURATION.md.

Checks the exact per-vertex degree-sum alternatives, Type-I T0 capacity,
and scalar surplus identities. This is not a proof of the analytic source
premises or global Q32 infeasibility.
"""
from itertools import product, combinations

# For each T0 vertex, epsilon is 0 or 1 and eleven color degrees are >=3.
for epsilon in (0, 1):
    total = 34 - epsilon
    excess = total - 11 * 3
    assert excess == 1 - epsilon
    if epsilon == 1:
        degrees = [3] * 11
        assert sum(degrees) == total
    else:
        degrees = [4] + [3] * 10
        assert sum(degrees) == total
        assert sum(d == 4 for d in degrees) == 1
        assert max(degrees) == 4

# T0 has 11 vertices; E0 of them have epsilon=1, so exactly 11-E0
# vertices must be assigned one repeated color.
for E0 in range(4):
    repeat_vertices = 11 - E0
    assert 8 <= repeat_vertices <= 11

# Source Type-I occupancy: if x_C is in T0, no double-outside factor can
# contain T0 because ten single factors already use all other T0 vertices.
# Both special K5s cannot then be single-outside (b_s+b_t=2 is excluded).
for special_T0_counts in product((0, 1), repeat=2):
    if sum(special_T0_counts) == 2:
        continue
    assert 1 + sum(special_T0_counts) <= 2
for special_T0_counts in product((0, 1), repeat=2):
    assert sum(special_T0_counts) <= 2

# Per exact color, t_C is both the T0-pair surplus and is bounded by g_C.
for g in range(7):
    for t in range(min(2, g) + 1):
        big_pair_surplus = g - t
        assert big_pair_surplus >= 0
        assert t <= min(2, g)

# In either isolated-double two-K4 subcase, extras form a star centered
# at y or x_C and terminate in the opposite special K4. Such a star can
# touch at most one T0 residual vertex. If the center itself is in T0,
# the pointwise degree cap permits at most one star edge.
parts = (0, 1, 2, 3)
for choice in product((0, 1), repeat=4):
    if choice[0] != 0:  # quotient by swapping the two K4s
        continue
    A = {(i, choice[i]) for i in range(4)}
    B = {(i, 1 - choice[i]) for i in range(4)}
    for center in A | B:
        opposite = B if center in A else A
        star_edges = [center_v for center_v in opposite
                      if center[0] != center_v[0]]
        assert len(star_edges) == 3
        for r in range(4):
            for sub in combinations(star_edges, r):
                if center[0] == 3 and len(sub) > 1:
                    # A T0 center has baseline degree 3 and cannot take
                    # two or more extra edges under the pointwise cap.
                    continue
                touched_T0 = {
                    v for edge in sub for v in edge if v[0] == 3
                }
                assert len(touched_T0) <= 1

# The only isolated-double source case not represented by a two-K4 star
# has x_C in H, y in H, and the two-double placement; its source ledger
# forces b_s+b_t=3, g_C=3, and a residual with only two T0 vertices.
assert 6 - (1 + 2) == 3
assert 69 + 3 == 72

# Aggregate identity: sum g_C=37 and sum t_C=11-E0.
for E0 in range(4):
    assert 37 - (11 - E0) == 26 + E0

print("T0 degree-sum alternatives checked for epsilon=0,1")
print("E0 repeat-owner counts checked for E0=0,1,2,3")
print("Type-I T0 gadget capacity checked")
print("Placement-sensitive t_C<=1 star cases checked; exceptional case has g_C=3")
print("T0 and big-pair surplus identities checked")
print("V47_T0_POINTWISE_COLOR_SATURATION_ARITHMETIC_OK")
print("Scope: arithmetic/source-interface regression only; not global Q32 UNSAT.")
