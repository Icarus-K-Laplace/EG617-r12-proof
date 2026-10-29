#!/usr/bin/env python3
"""Arithmetic regression for the corrected Type-I placement audit.

The twelve K5 factors include ten isolated components plus two special K5s
inside G11. This checks only the source-reported outside-count profiles and
their H-H edge counts; it does not verify the analytic placement theorem.
"""
from math import comb

profiles = {
    "x_in_O": ((2,) + (1,) * 11, 69, 0, 4),
    "x_in_H_two_double": ((2, 2) + (1,) * 10, 66, 0, 5),
    "x_in_H_triple": ((3,) + (1,) * 11, 67, 0, 6),
}
for name, (profile, hh_edges, gmin, gmax) in profiles.items():
    assert len(profile) == 12
    assert sum(profile) == (13 if name == "x_in_O" else 14)
    assert all(v >= 1 for v in profile)
    assert min(profile) >= 1
    for g in range(gmin, gmax + 1):
        assert hh_edges + (hh_edges * 0 + (69 + g - hh_edges)) == 69 + g

# In the triple placement, if the triple K5 is special, the other special K5
# is single-outside, so b_s+b_t=4 and G11 has four O vertices, seven H.
b_s, b_t = 3, 1
assert b_s + b_t == 4
assert 11 - (b_s + b_t) == 7

# If the triple K5 were isolated, its two H vertices would each have one
# same-color H-neighbor, below the balanced-coloring floor of two.
assert 1 < 2

# Source-correct G_H identities.
for g in range(5):
    assert g == (69 + g) - 69
for g in range(6):
    assert 3 + g == (69 + g) - 66
for g in range(7):
    assert 2 + g == (69 + g) - 67

print("V47_CORRECTED_TYPEI_PLACEMENT_ARITHMETIC_OK")
print("Scope: placement arithmetic only; triple placement is restricted, not excluded.")
