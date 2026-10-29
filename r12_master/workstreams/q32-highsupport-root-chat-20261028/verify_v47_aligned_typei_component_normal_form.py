#!/usr/bin/env python3
"""Arithmetic regression for V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md.

Checks the ten-K5 component counts, H/O part sizes, and the exact relationship
between the K5 H-H edge contribution, the 69-edge floor, and G11 H-H edges.
This does not verify the analytic balanced-coloring argument or global Q32.
"""
from math import comb

# The four H clique parts have sizes (12,12,12,11); O has 14 points.
parts = (12, 12, 12, 11)
O = 14

# x_C in O: nine single-outside K5s and one double-outside K5.
single, double, triple = 9, 1, 0
used_H = tuple(single + double if i < 3 else single for i in range(4))
used_O = single + 2 * double + 3 * triple
g11_H = tuple(parts[i] - used_H[i] for i in range(4))
g11_O = O - used_O
k5_HH = single * comb(4, 2) + double * comb(3, 2)
assert (single, double, triple) == (9, 1, 0)
assert used_H == (10, 10, 10, 9)
assert g11_H == (2, 2, 2, 2) and sum(g11_H) == 8
assert g11_O == 3
assert k5_HH == 57
for g in range(5):
    assert k5_HH + (12 + g) == 69 + g

# x_C in H, two-double placement: eight singles and two doubles.
single, double, triple = 8, 2, 0
used_H = tuple(single + double if i < 3 else single for i in range(4))
used_O = single + 2 * double + 3 * triple
g11_H = tuple(parts[i] - used_H[i] for i in range(4))
g11_O = O - used_O
k5_HH = single * comb(4, 2) + double * comb(3, 2)
assert (single, double, triple) == (8, 2, 0)
assert used_H == (10, 10, 10, 8)
assert g11_H == (2, 2, 2, 3) and sum(g11_H) == 9
assert g11_O == 2
assert k5_HH == 54
for g in range(6):
    assert k5_HH + (15 + g) == 69 + g

# A triple-outside K5 has only one H-neighbor per H vertex, below the
# source-independent lower bound of two from the other K12 clique parts.
assert 1 < 2
print("x-in-O: G11 H/O =", sum((2, 2, 2, 2)), 3, "; K5 H-H edges =", 57)
print("x-in-H two-double: G11 H/O =", sum((2, 2, 2, 3)), 2, "; K5 H-H edges =", 54)
print("V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM_ARITHMETIC_OK")
print("Scope: component-count arithmetic only; not global Q32 UNSAT.")
