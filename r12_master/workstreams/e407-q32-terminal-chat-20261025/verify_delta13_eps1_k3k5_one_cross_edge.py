#!/usr/bin/env python3
"""Arithmetic replay for DELTA13_EPS1_K3K5K5K5_ONE_CROSS_EDGE.md.

This checks the exact component-capacity totals and the strict gap in the
unsaturated-U contradiction. It does not prove the graph-theoretic lemmas.
"""
def compositions(total, k, prefix=()):
    if k == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from compositions(total - x, k - 1, prefix + (x,))

def check_capacity_totals():
    for E0, E1, E2, E3 in compositions(3, 4):
        triangle_k35 = (9 + E0) + (4 + E1) + (5 + E2) + (5 + E3)
        two_k5 = (10 + E0) + (4 + E1) + (4 + E2) + (5 + E3)
        assert triangle_k35 == 26, (E0, E1, E2, E3, triangle_k35)
        assert two_k5 == 26, (E0, E1, E2, E3, two_k5)

def check_unsaturated_u_gap():
    for eps_u in (0, 1):
        lower = 15 - eps_u
        upper = 13
        assert lower > upper, (eps_u, lower, upper)
        assert lower - upper == 2 - eps_u

if __name__ == "__main__":
    check_capacity_totals()
    check_unsaturated_u_gap()
    print("DELTA13_EPS1_K3K5K5K5_ONE_CROSS_EDGE_ARITHMETIC_OK")
