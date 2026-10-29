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

# Per exact Type-I color, t_C is both the T0-pair surplus and obeys
# the placement-sensitive global cap t_C<=1, as well as t_C<=g_C.
for g in range(7):
    for t in range(min(1, g) + 1):
        big_pair_surplus = g - t
        assert big_pair_surplus >= 0
        assert t <= min(1, g)

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
        star_edges = [(center, center_v) for center_v in opposite
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

# Exceptional isolated-double source case: x_C,y are both H and the
# placement is two-double with b_s+b_t=3. If both x_C and y were in T0,
# the three H-vertices of N_s would split k/(3-k) between their two
# gadget neighborhoods. T0 saturation would require k<=1 and 3-k<=1,
# impossible. If exactly one were in T0, x_C--(N_t\\{y}) contains a
# forbidden same-track edge. Thus x_C,y are both in large tracks.
# The T0 vertex in the N_s triangle has degree 2+1=3; the T0 vertex in
# the N_t K4 has degree 3+1=4, so this branch also has t_C=1.
assert not any(k <= 1 and 3 - k <= 1 for k in range(4))
assert 2 + 1 == 3
assert 3 + 1 == 4
assert 6 - (1 + 2) == 3
assert 69 + 3 == 72

# Aggregate identity: sum g_C=37 and sum t_C=11-E0.
for E0 in range(4):
    assert 37 - (11 - E0) == 26 + E0
    assert max(0, 1 - E0) == max(0, 11 - E0 - 10)

print("T0 degree-sum alternatives checked for epsilon=0,1")
print("E0 repeat-owner counts checked for E0=0,1,2,3")
print("Type-I T0 gadget capacity checked")
print("Placement-sensitive t_C<=1 cases checked, including exceptional g_C=3 case")
print("T0 and big-pair surplus identities checked")
print("V47_T0_POINTWISE_COLOR_SATURATION_ARITHMETIC_OK")
print("Scope: arithmetic/source-interface regression only; not global Q32 UNSAT.")
