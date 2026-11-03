#!/usr/bin/env python3
"""Independent replay of the h13 Q30 |X|=3 branch.

Enumerates every distribution of ten regular degree-two outside points among
the three pairs of a weight-11 triangle, and verifies the exact rho=9 identity.
"""
from itertools import product
import json

rows = []
for n_ab in range(1, 9):
    for n_ac in range(1, 9):
        n_bc = 10 - n_ab - n_ac
        if n_bc < 1:
            continue
        # M-degrees of the three weight-11 triangle vertices.
        d_a = 2 + n_ab + n_ac
        d_b = 2 + n_ab + n_bc
        d_c = 2 + n_ac + n_bc
        assert max(d_a, d_b, d_c) <= 11

        # Pick y of type ab. In A\N_M(y), the other nine outside points
        # contribute r_c=n_ac+n_bc edges to c; c's decoration is 9-r_c.
        r_c = n_ac + n_bc
        g_c = 11 - d_c
        assert g_c == 9 - r_c
        rho = r_c + g_c
        assert rho == 9
        q_lower = 2 * (13 - 2) + rho
        assert q_lower == 31

        rows.append({
            "n_ab": n_ab, "n_ac": n_ac, "n_bc": n_bc,
            "hub_degrees": [d_a, d_b, d_c],
            "rho_for_ab_point": rho,
            "q_lower_bound": q_lower,
        })

assert len(rows) == 36
assert all(row["q_lower_bound"] == 31 for row in rows)

print(json.dumps({
    "status": "PASS",
    "outside_pair_type_distributions": len(rows),
    "all_three_pair_types_nonempty": True,
    "rho_identity": "r_c + (9-r_c) = 9",
    "q_lower_bound_for_every_regular_outside_point": 31,
    "scope": "Finite replay of the |X|=3 local charge identity only."
}, indent=2))
