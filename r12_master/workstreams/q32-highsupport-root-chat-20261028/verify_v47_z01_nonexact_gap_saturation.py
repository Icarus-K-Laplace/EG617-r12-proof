#!/usr/bin/env python3
"""Exact arithmetic replay for the aligned m=10 nonexact-gap saturation lemma."""
from math import comb

# Case p in Z: Z={p}, so all 13 A vertices need a D-neighbor in T0.
p_in_z_total = 13 + 2
assert p_in_z_total == 15

rows = {}
for k in range(14):  # Z subset A, |Z|=k
    e_o_t0 = 14 - k
    e_a = max(2, comb(k, 2))
    rows[k] = (e_o_t0, e_a, e_o_t0 + e_a)

minimum = min(total for _, _, total in rows.values())
minimizers = [k for k, (_, _, total) in rows.items() if total == minimum]
assert minimum == 14
assert minimizers == [2, 3]
assert rows[2] == (12, 2, 14)
assert rows[3] == (11, 3, 14)
assert all(total > 14 for k, (_, _, total) in rows.items() if k not in (2, 3))
assert 132 - 56 == 76
assert 37 - 10 * 3 == 7
print("V47_Z01_NONEXACT_GAP_SATURATION_ARITHMETIC_OK")
print("minimum additional outside-H edges:", minimum)
print("equality k profiles:", {k: rows[k] for k in minimizers})
print("forced gaps: g_D=7 and all ten exact g_C=3")
