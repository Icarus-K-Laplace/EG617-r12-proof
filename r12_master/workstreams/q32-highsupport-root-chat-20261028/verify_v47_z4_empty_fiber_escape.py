#!/usr/bin/env python3
"""Arithmetic replay for V47_Z4_EMPTY_FIBER_ESCAPE_CLASSIFICATION.md.

Checks the source-correct count contradiction in the z=4, 3+7, (3,2,2,0)
fiber profile under the all-aligned singleton assumption:
  E0 >= 9;
  at most 21-E0 <= 12 small-to-outer extra edges have nonzero small endpoint;
  the seven empty-track outer vertices need 21 extra Q-Q incidences;
  hence at least 9 internal-heavy incidences hit the empty track, exceeding
  the total outer-heavy weight x_T=7.
This checks arithmetic only, not the graph-theoretic premise that q_0 has
no R-neighbor or the completeness of the surrounding Q32 reduction.
"""
from itertools import product

# Each small block has endpoint slack u_i(h)>=0 with sum_h u_i(h)=2.
slack_vectors = [
    (a, b, c, d)
    for a in range(3)
    for b in range(3)
    for c in range(3)
    for d in range(3)
    if a + b + c + d == 2
]
assert len(slack_vectors) == 10

profiles = list(product(slack_vectors, repeat=3))
assert len(profiles) == 1000

min_E0 = min(sum(3 + u[0] for u in prof) for prof in profiles)
max_nonzero_endpoints = max(21 - sum(3 + u[0] for u in prof) for prof in profiles)
assert min_E0 == 9
assert max_nonzero_endpoints == 12

# In each of seven outer blocks, q_0 has degree 12, nine mandatory Q-neighbors,
# and no R-neighbor, so it needs exactly three extra Q-Q incidences.
required_track0_incidence = 7 * 3
lower_bound_track0_heavy = required_track0_incidence - max_nonzero_endpoints
outer_heavy_weight = 7
assert required_track0_incidence == 21
assert lower_bound_track0_heavy == 9
assert lower_bound_track0_heavy > outer_heavy_weight

print("slack profiles checked:", len(profiles))
print("minimum E0:", min_E0)
print("maximum nonzero-label small endpoints:", max_nonzero_endpoints)
print("required empty-track extra incidences:", required_track0_incidence)
print("forced heavy incidence lower bound:", lower_bound_track0_heavy)
print("available outer-heavy weight:", outer_heavy_weight)
print("V47_Z4_EMPTY_FIBER_ESCAPE_ARITHMETIC_OK")
print("Scope: arithmetic replay only; not global Q32 UNSAT.")
