#!/usr/bin/env python3
"""Arithmetic replay for the K5--K5 cross-edge cover-capacity bound.

This checks only the integer excess-budget calculation. It does not verify
the graph-theoretic saturation lemmas or the original EG617 reduction.
"""
from itertools import product

profiles = []
for ET, EP, EQ, ER in product(range(5), repeat=4):
    if ET + EP + EQ + ER != 4:
        continue
    cap_T = 9 + ET + int(ET == 0)
    cap_P = 4 + EP
    cap_Q = 4 + EQ
    cap_R = 5 + ER
    total = cap_T + cap_P + cap_Q + cap_R
    profiles.append((total, ET, EP, EQ, ER))
    assert total <= 27, (total, ET, EP, EQ, ER)

maximum = max(row[0] for row in profiles)
assert maximum == 27
print(f"PASS: {len(profiles)} excess profiles checked; maximum cover bound = {maximum} < 29.")
print("LIMIT: arithmetic only; the analytic saturation and component-capacity lemmas remain proof obligations.")
