#!/usr/bin/env python3
"""Arithmetic replay for DELTA14_EPS1_K4K4K5K5_ONE_CROSS_EDGE.md.

Checks assignment/excess and K4-load arithmetic only. It does not verify the
analytic alpha-number or reverse-saturation lemmas.
"""
TOTAL_EXCESS = 2 * 284 - 12 * 47
EPS_U = 1
EPS_W = TOTAL_EXCESS - EPS_U
assert TOTAL_EXCESS == 4 and EPS_W == 3
assert 2 * (4 * 3 // 2) + 2 * (5 * 4 // 2) + 1 == 33

for E_D in (0, 1):
    for q5 in range(4):
        if q5 > 1 + E_D:
            continue
        R = 1 - q5 + E_D
        assert R >= 0
        assert R <= 2
        q4 = 8 - q5
        assert q4 >= 6
        assert q4 > 2 * 2  # if each K4 got at most two D assignments, only four fit

for k in range(3, 8):
    m_max = min(4, 2 // (8 - k))
    non_D_complete = 4 - m_max
    required_excess = non_D_complete * (k - 2)
    assert required_excess > EPS_W, (k, m_max, required_excess)

assert 8 > 11  # deliberately false would be a bad check; use the clique size identity instead
