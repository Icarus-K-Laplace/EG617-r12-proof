#!/usr/bin/env python3
"""Finite arithmetic regression for the direct v=44 Q32 closures.

This script checks shell capacities, special-parameter profiles, pointwise
surplus counts, and the integer edge-budget spine of the 130-edge local lemma.
It does NOT prove the source Type-I theorem, corrected multiplicity, the
Kang--Pikhurko extremal bound, or the analytic no-core-only-degree-four lemma.
"""

from itertools import combinations_with_replacement

# The registered residual is 61-vertex, so each point has degree 60.
assert 13 + 8 * 4 + 3 * 4 == 57
assert 60 - 57 == 3

# Corrected multiplicity n_w >= m-6 gives n_w >=2 for m=8.
# The special excess at parameter a is 5-a, with a in {1,2,3,4}.
profiles = {}
for n in (2, 3):
    valid = []
    for A in combinations_with_replacement(range(1, 5), n):
        if sum(5 - a for a in A) <= 3:
            valid.append(A)
    profiles[n] = valid
assert profiles[2] == [(3, 4), (4, 4)]
assert profiles[3] == [(4, 4, 4)]

# m=9 shell contradiction: six non-special colors consume >=12 of 13
# w--A edges; at most one special color can use zero shell edges.
assert 6 * 2 == 12
assert 13 - 12 == 1
assert 3 - 1 == 2  # at least two special colors would have zero shell degree

# m=8, n=2: six non-special colors consume >=12 shell edges; at least one
# special color uses a shell edge, so the unique remaining edge is used.
assert (8 - 2) * 2 + (2 - 1) == 13
# All 13 w--A edges and p-w are exact-owned, so no nonexact color has an O-neighbor.
# Profiles (3,4) and (4,4) leave 0 and 1 slack units, respectively.
assert sum(5 - a for a in (3, 4)) == 3
assert sum(5 - a for a in (4, 4)) == 2
assert 3 - 3 == 0
assert 3 - 2 == 1
# Therefore at least two of the three 130-edge colors stay at degree four.

# m=8, n=3: all exact special parameters are a=4; their three surplus units
# exhaust the budget, so all nonexact colors have degree four.
assert sum(5 - a for a in (4, 4, 4)) == 3
assert (8 - 3) * 2 + (3 - 1) == 12
# At most one of the 14 w--O edges can be nonexact.
assert 14 - 13 == 1

def choose2(n):
    return n * (n - 1) // 2

# The first step of the 130-edge degree theorem: exclude degrees 0,1,2.
# Balanced 11-partition arithmetic for anti-neighborhood sizes 58,59,60.
expected_low_degree = {
    58: (1653, 1528, 1524, 129),
    59: (1711, 1581, 1577, 134),
    60: (1770, 1635, 1631, 139),
}
for n, (choose_n, t_n, p_n, floor_n) in expected_low_degree.items():
    q, rem = divmod(n, 11)
    parts = [q + 1] * rem + [q] * (11 - rem)
    t_calc = choose2(n) - sum(choose2(part) for part in parts)
    p_calc = t_calc - n // 11 + 1
    assert (choose2(n), t_calc, p_calc, choose2(n) - p_calc) == (choose_n, t_n, p_n, floor_n)
assert expected_low_degree[60][3] > 130
assert expected_low_degree[59][3] > 130
assert expected_low_degree[58][3] + 2 > 130

# (56,11) Kang--Pikhurko arithmetic for a degree-four vertex in a 130-edge color.
# Balanced 11-partition of 56 has one part of size6 and ten of size5.
t_11_56 = choose2(56) - (choose2(6) + 10 * choose2(5))
p_11_56 = t_11_56 - 56 // 11 + 1
assert t_11_56 == 1425
assert p_11_56 == 1421
assert choose2(56) - p_11_56 == 119

# If S=N_D(x), a=e(D[S]), b=e_D(S,N), then a+b<=7 and 2a+b>=12.
feasible = [
    (a, b)
    for a in range(7)
    for b in range(8)
    if a <= 5 and a + b <= 7 and 2 * a + b >= 12
]
assert feasible == [(5, 2)]
# For a core-only degree-four point, S is K4-e; each missing-edge endpoint
# has one external edge. Its neighborhood then induces only a triangle (3 edges),
# contradicting the required >=5 edges in every degree-four neighborhood.
assert 3 < 5

print("V44_DIRECT_CLOSURE_ARITHMETIC_OK")
print("Scope: arithmetic only; graph lemmas and published extremal inputs remain explicit dependencies.")
