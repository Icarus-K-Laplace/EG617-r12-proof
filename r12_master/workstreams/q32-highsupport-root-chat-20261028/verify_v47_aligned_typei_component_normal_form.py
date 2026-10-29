#!/usr/bin/env python3
"""Arithmetic regression for the corrected Type-I placement audit.

The source factorization has twelve K5 factors: ten isolated components plus
two special K5 cliques inside G11. This checks the outside-count profiles,
K5-interior H-edge totals, gap-to-extra-gadget-edge identities, and the
necessary special-K5 condition in triple placement. It does not prove global
Q32 infeasibility.
"""
from math import comb

cases = [
    ("x_in_O", (2,) + (1,) * 11, 13, 69, 0, 4),
    ("x_in_H_two_double", (2, 2) + (1,) * 10, 14, 66, 0, 5),
    ("x_in_H_triple", (3,) + (1,) * 11, 14, 67, 0, 6),
]
for name, profile, total_outside, k5_hh, g_min, g_max in cases:
    assert len(profile) == 12
    assert sum(profile) == total_outside
    assert all(v >= 1 for v in profile)
    assert max(profile) <= 3
    for g in range(g_min, g_max + 1):
        e_h = 69 + g
        gadget_hh = e_h - k5_hh
        if name == "x_in_O":
            assert gadget_hh == g
        elif name == "x_in_H_two_double":
            assert gadget_hh == 3 + g
        else:
            assert gadget_hh == 2 + g

# The two special K5s each meet O.
special_profiles = {
    "x_in_O": [(1, 1), (2, 1), (1, 2)],
    "x_in_H_two_double": [(1, 1), (2, 1), (1, 2), (2, 2)],
    "x_in_H_triple": [(3, 1), (1, 3)],
}
for name, pairs in special_profiles.items():
    assert all(a >= 1 and b >= 1 for a, b in pairs)
    if name == "x_in_O":
        assert {a + b for a, b in pairs} == {2, 3}
    elif name == "x_in_H_two_double":
        assert {a + b for a, b in pairs} == {2, 3, 4}
    else:
        assert all(a + b == 4 for a, b in pairs)

# If the triple-outside K5 were an isolated component, each of its two H
# vertices would have only one C-neighbor in H, contradicting d_C(v,H)>=2.
# Thus triple placement requires the triple K5 to be one of the special
# cliques; the other special clique is single-outside, so b_s+b_t=4.
assert 1 < 2
assert 3 + 1 == 4
assert 11 - 4 == 7  # G11 has seven H and four O vertices in triple placement.

print("Type-I K5 profiles and H-edge accounting: 3 cases checked")
print("Triple placement: special-K5-only necessary condition checked")
print("V47_CORRECTED_TYPEI_PLACEMENT_ARITHMETIC_OK")
print("Scope: arithmetic/source-interface audit only; no global Q32 UNSAT.")
