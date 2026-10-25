#!/usr/bin/env python3
"""Finite arithmetic replay for DELTA14_EPS0_K3K4K5K6_COVER_CAPACITY.md.

Checks the integer excess-profile bound only. It does not verify the graph
saturation lemmas or provide a graph-realization/SAT certificate.
"""
from itertools import product

profiles = []
for E3, E4, E5, E6 in product(range(5), repeat=4):
    if E3 + E4 + E5 + E6 != 4:
        continue
    cap6 = E6 // 2
    cap5 = 5 + E5
    cap4 = 8 + E4 + int(E4 == 0)
    cap3 = 9 + E3 + int(E3 == 0)
    total = cap3 + cap4 + cap5 + cap6
    profiles.append((total, E3, E4, E5, E6))
    assert total <= 28, (total, E3, E4, E5, E6)

max_total = max(p[0] for p in profiles)
max_profiles = [p[1:] for p in profiles if p[0] == max_total]
assert max_total == 28
assert max_profiles == [(0, 0, 4, 0)]

# Exceptional unsaturated-vertex cases used in the proof.
assert 8 <= 5 + 4       # K5: eps=4 leaves a zero-excess companion
for E4 in (3, 4):
    assert 9 <= 8 + E4  # K4: eps>=3 leaves a zero-excess companion
for E3 in (2, 3, 4):
    assert 11 <= 9 + E3 # K3: eps>=2 leaves a companion with eps<=1

print("PASS: all 35 nonnegative excess profiles summing to 4 have cover bound <=28.")
print(f"PASS: maximum bound {max_total}, attained at (E3,E4,E5,E6)={max_profiles[0]}.")
print("PASS: exceptional-component degree-cap inequalities.")
print("LIMIT: arithmetic replay only; analytic saturation/capacity lemmas are not machine-verified.")
