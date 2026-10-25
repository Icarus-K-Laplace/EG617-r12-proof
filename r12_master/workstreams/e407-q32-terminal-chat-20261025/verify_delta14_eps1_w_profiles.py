#!/usr/bin/env python3
"""Exact integer replay for DELTA14_EPS1_W_PROFILE_CLASSIFICATION.md."""
from itertools import combinations_with_replacement
from math import comb

N = 18
EDGE_H_W = 33
EDGE_G = comb(N, 2) - EDGE_H_W
TURAN_T4 = comb(N, 2) - (comb(4, 2) + comb(4, 2) + comb(5, 2) + comb(5, 2))
BROUWER_NONPARTITE_CAP = TURAN_T4 - (N // 4) + 1
assert EDGE_G == 120
assert TURAN_T4 == 121
assert BROUWER_NONPARTITE_CAP == 118
assert EDGE_G > BROUWER_NONPARTITE_CAP

parts = []
for a, b, c, d in combinations_with_replacement(range(1, N + 1), 4):
    if a + b + c + d != N:
        continue
    within = sum(comb(x, 2) for x in (a, b, c, d))
    if within in (32, 33):
        parts.append((within, (a, b, c, d)))
assert sorted(parts) == [
    (32, (4, 4, 5, 5)),
    (33, (3, 5, 5, 5)),
    (33, (4, 4, 4, 6)),
]
print("PASS: e(G)=120, t4(18)=121, Brouwer non-4-partite cap=118.")
print("PASS: exact sorted partition list:", parts)
print("LIMIT: invoking Brouwer's theorem is an explicit external dependency.")
