#!/usr/bin/env python3
"""Arithmetic replay for DELTA14_EPS1_K4K4K4K6_NO_CROSS_EDGE.md.

Checks excess, D-assignment, external-incidence, and K4 load arithmetic only;
it does not machine-verify the graph-theoretic saturation lemmas.
"""
from itertools import product

TOTAL_EXCESS = 2 * 284 - 12 * 47
EPS_U = 1
EPS_W = TOTAL_EXCESS - EPS_U
assert TOTAL_EXCESS == 4 and EPS_W == 3
assert 3 * (4 * 3 // 2) + 6 * 5 // 2 == 33

for q in (0, 1):
    E_D = 0 if q == 1 else 1  # if q=1, the K6-assigned D vertex owns epsilon_U=1
    R = 1 - 2 * q + E_D
    assert R == (0 if q == 1 else 2)
    for k in range(3, 8):
        m_max = min(4, R // (8 - k))
        non_D_complete = 4 - m_max
        required_excess = non_D_complete * (k - 2)
        assert required_excess > EPS_W, (q, k, m_max, required_excess)

# k=8 directly gives K12; k<=2 per each of three K4s cannot host 7 or 8 D vertices.
assert 3 * 2 == 6 < 7
assert 3 * 2 == 6 < 8
print("PASS: e(H[W])=33 and W-excess=3.")
print("PASS: external-incidence identity gives R<=2 (q=0) or R=0 (q=1).")
print("PASS: every K4 load k=3,...,7 exceeds the W-excess budget; k=8 gives K12.")
print("PASS: three K4s cannot host the required seven or eight D assignments.")
print("LIMIT: analytic saturation and component-assignment arguments remain in the Markdown proof.")
