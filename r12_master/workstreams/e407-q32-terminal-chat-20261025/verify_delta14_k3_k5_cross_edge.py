#!/usr/bin/env python3
"""Arithmetic replay for the final delta=14 K3--K5 cross-edge case.

The script verifies finite excess-budget tables only. It does not verify the
graph-theoretic saturation, all-or-none, or endpoint-placement lemmas.
"""
from itertools import product

rows = []
for ET, EP, EQ, ER in product(range(5), repeat=4):
    if ET + EP + EQ + ER != 4:
        continue
    cap_T = 8 + (5 + ET) // 3
    cap_sum = cap_T + (4 + EP) + (5 + EQ) + (5 + ER)
    Xmax = 2 + ET // 2
    naive = cap_sum + Xmax
    if ET == 3:
        corrected = naive
    elif naive <= 28:
        corrected = naive
    else:
        # If |X| reaches Xmax, the smaller-excess T-vertex has all its
        # small-part neighbours in X, so S_T is only D (size 8).
        corrected = cap_sum - (cap_T - 8) + Xmax
    rows.append((ET, EP, EQ, ER, cap_T, cap_sum, Xmax, naive, corrected))
    assert corrected <= 28, rows[-1]

assert len(rows) == 35
assert max(r[-1] for r in rows) == 28
print("PASS: all 35 excess allocations have corrected cover bound <=28 <29.")
print("PASS: ET=3 is already below 29; equality-bound cases use the S_T=D correction.")
print("LIMIT: arithmetic only; analytic graph lemmas are not machine-verified.")
