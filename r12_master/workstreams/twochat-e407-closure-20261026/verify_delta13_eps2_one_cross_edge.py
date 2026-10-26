#!/usr/bin/env python3
"""Arithmetic replay for the delta=13, epsilon_U=2 one-cross-edge proof.

Checks finite excess/assignment and K4-load arithmetic only. It does not
verify the independent-transversal lemmas or graph-theoretic implications.
"""

TOTAL_EXCESS = 2 * 284 - 12 * 47
DELTA = 13
EPS_U = 2
EPS_W = TOTAL_EXCESS - EPS_U
E_U = 112 - DELTA
E_W = 48 - EPS_U - DELTA
E_CROSS = 124 + EPS_U + 2 * DELTA

assert TOTAL_EXCESS == 4
assert EPS_W == 2
assert (E_U, E_W, E_CROSS) == (99, 33, 152)
assert E_U + E_W + E_CROSS == 284

# A single W-cross-edge between parts of sizes 4,4,5,5 has the following
# minimum degrees for a D-vertex not complete to any W part.
assert (4 - 1) + (4 - 1) == 6
assert (4 - 1) + (5 - 1) == 7
assert (5 - 1) + (5 - 1) == 8
MAX_D_W_DEGREE = 5 + EPS_U
assert MAX_D_W_DEGREE == 7

# Sum t_d=8 and epsilon_D<=2. Assigned K4, assigned K5, and unassigned
# D-vertices contribute respectively 1+eps, eps, and at most eps-1.
for z in range(5):
    for q5 in range(5):
        for eps_d in range(EPS_U + 1):
            if 8 <= 8 - q5 - 2 * z + eps_d:
                assert q5 + 2 * z <= eps_d
                assert z <= 1
                assert q5 <= 2
                if z == 1:
                    assert q5 == 0 and eps_d == 2

# In the z=0 case, R<=2 limits the number m of K4 vertices complete to D.
for k in range(3, 8):
    m_max = min(4, 2 // (8 - k))
    non_d_complete = 4 - m_max
    required_excess = non_d_complete * (k - 2)
    assert required_excess > EPS_W
    print(f"z=0, k={k}: m<={m_max}, non-D-complete>={non_d_complete}, "
          f"required W excess>={required_excess}")

# In the z=1 exceptional case, every D row has t_d<=2. A W vertex
# unsaturated to all U-parts then has U-degree at least 12, while every K4
# vertex has U-degree at most 11.
for t_max in (2, 3):
    lower_bounds = []
    for d_nonneighbors in (1, 2, 3):
        if d_nonneighbors == 1:
            nonneighbors = t_max + 7 + 7 + 1
        elif d_nonneighbors == 2:
            nonneighbors = 2 * t_max + 7 + 2
        else:
            nonneighbors = 3 * t_max + 3
        lower_bounds.append(29 - nonneighbors)
    if t_max == 2:
        assert lower_bounds == [12, 16, 20]
    else:
        assert lower_bounds == [11, 14, 17]

# z=1, k=4..6 forces all four K4 vertices to consume at least k-1 excess.
for k in (4, 5, 6):
    assert 4 * (k - 1) > EPS_W

# z=1, k=7: the cross-edge endpoint cannot be complete to D and would need
# at least 7 small-part neighbours plus 7 D-neighbours, exceeding U-degree.
assert 7 + 7 > 8 + EPS_W

print("E407_DELTA13_EPS2_ONE_CROSS_EDGE_ARITHMETIC_OK")
print("Scope: arithmetic only; analytic transversal lemmas require proof audit.")
