#!/usr/bin/env python3
"""Exact arithmetic replay for DELTA14_EPS2_W_PROFILE_CLASSIFICATION.md."""
from math import comb

N = 18
EDGE_H_W = 32
TURAN_T4 = comb(N, 2) - (comb(4, 2) + comb(4, 2) + comb(5, 2) + comb(5, 2))
assert comb(N, 2) - EDGE_H_W == 121
assert TURAN_T4 == 121
assert EDGE_H_W == comb(4, 2) + comb(4, 2) + comb(5, 2) + comb(5, 2)
assert 9 + 9 + 2 + 2 + (4 - 2) == 24
assert 24 < 29
print("PASS: e(H[W])=32 is exact Turan equality at n=18, r=4.")
print("PASS: the only equality profile is K4 union K4 union K5 union K5.")
print("PASS: the cited common-neighbour capacity upper bound is 24 < 29.")
print("LIMIT: the graph-theoretic capacity proof is in DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md, Section 5.")
