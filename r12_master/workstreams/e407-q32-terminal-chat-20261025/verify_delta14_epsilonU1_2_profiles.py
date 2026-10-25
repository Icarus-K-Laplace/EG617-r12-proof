#!/usr/bin/env python3
"""Arithmetic replay for the four epsilon_U=1,2 delta14 profile exclusions.

This checks finite excess-budget inequalities only. It is not a graph
realization or a verifier of the analytic saturation lemmas.
"""
from itertools import product

# K3 + three K5s, no W-cross-edge.
for eps_u in (1, 2):
    ew = 4 - eps_u
    cases = []
    for ET, E1, E2, E3 in product(range(ew + 1), repeat=4):
        if ET + E1 + E2 + E3 != ew:
            continue
        cap_T = 9 + ET + int(ET == 0)
        caps = [5 + E1, 5 + E2, 5 + E3]
        total = cap_T + sum(caps)
        # A non-saturated K5 can only be the unique excess-E_i=E_w component.
        # In eps_U=2, its cap is 8, with the other components at zero excess.
        if eps_u == 2 and max(E1, E2, E3) == 2:
            if sorted((E1, E2, E3)) == [0, 0, 2] and ET == 0:
                total = 10 + 8 + 5 + 5
        cases.append(total)
    assert max(cases) <= 28, (eps_u, max(cases))

# K4^3 + K6, epsilon_U=1.
# Each K4 common-neighbour set has size <=9; S_6 <= floor(E6/2).
assert 3 * 9 + (3 // 2) == 28

# K4 + K4 + K5 + K5, epsilon_U=2.
# K4 caps are 9; saturated K5 caps are 2+E_i.
for E1, E2, E3, E4 in product(range(3), repeat=4):
    if E1 + E2 + E3 + E4 != 2:
        continue
    total = 9 + 9 + (2 + E3) + (2 + E4)
    assert total <= 24, (E1, E2, E3, E4, total)

print("PASS: K3+K5^3 profiles for epsilon_U=1,2 have cover bound <=28.")
print("PASS: K4^3+K6 at epsilon_U=1 has cover bound <=28.")
print("PASS: K4^2+K5^2 at epsilon_U=2 has cover bound <=24.")
print("LIMIT: arithmetic only; graph-theoretic lemmas are not machine-verified.")
