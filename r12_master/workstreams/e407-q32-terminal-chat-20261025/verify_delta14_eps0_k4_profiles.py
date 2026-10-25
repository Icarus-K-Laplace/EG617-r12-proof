#!/usr/bin/env python3
"""Arithmetic replay only for DELTA14_EPS0_K4_PROFILE_EXCLUSIONS.md.

This script checks the exact edge/degree ledgers and endpoint-load case splits.
It does NOT verify the graph-theoretic saturation lemmas or prove EG617.
Uses only the Python standard library.
"""
from itertools import combinations_with_replacement

N_U = 29
SMALL_PARTS = (7, 7, 7)
D_PART = 8
CORE_EDGES = 284
BASE_DEGREE = 12
TOTAL_EXCESS = CORE_EDGES * 2 - BASE_DEGREE * 47  # sum_v(d(v)-12)=4
DELTA = 14

e_h_u = 112 - DELTA
within_part_edges = 3 * (7 * 6 // 2) + (8 * 7 // 2)
cross_edges = e_h_u - within_part_edges
assert TOTAL_EXCESS == 4
assert e_h_u == 98
assert within_part_edges == 91
assert cross_edges == 7

# Seven distinct small-side endpoints, one per cross-edge; t_d<=3.
t_profile = (1,) * 7 + (0,)
assert sum(t_profile) == 7 and max(t_profile) <= 3

def weak_compositions(total, slots, cap=None):
    if slots == 1:
        if cap is None or total <= cap:
            yield (total,)
        return
    for x in range(total + 1 if cap is None else min(total, cap) + 1):
        for rest in weak_compositions(total - x, slots - 1, cap):
            yield (x,) + rest

# W profile (4,4,5,5), two W-cross-edges:
# Seven t=1 vertices have exact K4-neighbourhoods. Enumerate all splits
# between the two K4 parts. For splits 4+3 or 5+2, the high load costs
# at least 4*(k-2)>4 excess; 6+1 costs 16; 7+0 is the K12/t=0 terminal.
splits_2k4 = sorted({tuple(sorted((a, 7-a), reverse=True))
                     for a in range(8)}, reverse=True)
assert splits_2k4 == [(7, 0), (6, 1), (5, 2), (4, 3)]
for k, other in splits_2k4:
    if k in (4, 5):
        assert other >= 2 and 4 * (k - 2) > TOTAL_EXCESS
    elif k == 6:
        assert other == 1 and 4 * 4 > TOTAL_EXCESS
    else:
        assert k == 7 and other == 0

# W profile (4,4,4,6), one W-cross-edge:
# Seven exact K4-neighbourhoods are distributed among three K4 parts.
splits_3k4 = sorted(set(tuple(sorted(p, reverse=True))
                        for p in weak_compositions(7, 3)), reverse=True)
assert all(sum(p) == 7 for p in splits_3k4)
assert all(len(p) == 3 for p in splits_3k4)
for p in splits_3k4:
    k = p[0]
    if k >= 4:
        assert 4 * (k - 2) > TOTAL_EXCESS
    else:
        assert p == (3, 2, 2)

print("PASS: delta=14 ledger gives 7 cross-edges and 4 total core excess.")
print("PASS: t_D profile under epsilon_U=0 is seven 1s and one 0.")
print("PASS: (4,4,5,5)+2-edge endpoint splits:", splits_2k4)
print("PASS: (4,4,4,6)+1-edge high-load profiles reduce to (3,2,2) or excess contradiction.")
print("LIMIT: arithmetic replay only; graph lemmas are proved in the accompanying Markdown.")
