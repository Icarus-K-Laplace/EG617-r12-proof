#!/usr/bin/env python3
"""Exact arithmetic checks for R12_WITNESS_TRANSVERSAL_BOUNDARY_THEOREM.md.

This checks integer inequalities and boundary identities only. It is not a
graph realization or terminal-exclusion certificate.
"""
from math import comb


def p_k(n: int, k: int) -> int:
    q, r = divmod(n, k)
    sizes = [q + 1] * r + [q] * (k - r)
    return sum(comb(s, 2) for s in sizes)


def t_k(n: int, k: int) -> int:
    return comb(n, 2) - p_k(n, k)


def transversal_screen(v: int, m: int, t: int):
    n1_max = t * ((v - t) // 3)
    n2_min = max(0, m - n1_max)
    incidence_lower = m + n2_min
    incidence_upper = t * ((v - 1) // 3)
    block_count_upper = n1_max + comb(t, 2)
    return block_count_upper, incidence_lower, incidence_upper


def check_transversal_boundary(v: int, m: int, count_cutoff: int, incidence_ts):
    for t in range(1, count_cutoff + 1):
        count_upper, _, _ = transversal_screen(v, m, t)
        assert count_upper < m, (v, m, t, count_upper)
    for t in incidence_ts:
        _, lower, upper = transversal_screen(v, m, t)
        assert lower > upper, (v, m, t, lower, upper)
    print(f"transversal boundary v={v}, m={m}: tau>=7 verified")


def check_core_budget():
    # E407: v=29, m=49, e(L)=294+delta, epsilon_U in [0,4].
    for delta in range(17):
        for eps_u in range(5):
            if delta + eps_u <= 16 and eps_u + 2 * delta >= 2:
                e_u = 112 - delta
                e_cross = 124 + 2 * delta + eps_u
                e_w = 48 - delta - eps_u
                assert e_cross == 12 * 29 + eps_u - 2 * e_u
                assert e_w == 284 - e_u - e_cross
                assert e_w >= 32
    # E408 Q33: v=31, m=56, e(L)=336+delta.
    for delta in range(18):
        for eps_u in range(5):
            if delta + eps_u <= 17:
                e_u = 129 - delta
                e_cross = 114 + 2 * delta + eps_u
                e_w = 41 - delta - eps_u
                assert e_cross == 12 * 31 + eps_u - 2 * e_u
                assert e_w == 284 - e_u - e_cross
                assert e_w >= 24
                assert e_cross >= 7 * 16
    print("boundary edge/excess identities verified")


def main():
    assert p_k(18, 4) == 32
    assert p_k(16, 4) == 24
    assert t_k(29, 4) == 315
    assert t_k(31, 4) == 360
    assert t_k(29, 4) - 29 // 4 + 1 == 309  # conditional if L is non-four-partite
    assert t_k(31, 4) - 31 // 4 + 1 == 354
    check_transversal_boundary(29, 49, 4, (5, 6))
    check_transversal_boundary(31, 56, 5, (6,))
    check_core_budget()
    print("WITNESS_TRANSVERSAL_BOUNDARY_AUDIT_OK")


if __name__ == "__main__":
    main()
