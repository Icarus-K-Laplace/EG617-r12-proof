#!/usr/bin/env python3
"""Exact-integer arithmetic audit for R12_ZERO_EXCESS_WITNESS_THEOREM.md.

This script checks only the finite Turan-comparison table and the scalar
witness-overlap bounds. It is not a graph-search certificate and is not used
as a substitute for the analytic proof.
"""
from math import comb


def p3(n: int) -> int:
    """Minimum edges in an n-vertex graph with independence number <= 3."""
    q, r = divmod(n, 3)
    return (3 - r) * comb(q, 2) + r * comb(q + 1, 2)


def upper(E: int, k: int, t: int) -> int:
    """Upper bound U(E,k,t) from the analytic proof."""
    return (
        282 - E // 2 - 12 * k + comb(k, 2)
        - t * (12 - k) + comb(t, 2)
    )


def check_zero_excess_table() -> None:
    for E, t_max in ((4, 6), (6, 4)):
        for k in range(1, E + 1):
            gaps = []
            for t in range(t_max + 1):
                n = 47 - k - t
                gap = p3(n) - upper(E, k, t)
                assert gap > 0, (E, k, t, n, gap)
                gaps.append(gap)
            assert all(gaps[t + 1] < gaps[t] for t in range(t_max)), (
                E, k, gaps
            )
            print(
                f"E={E} k={k}: gaps={gaps}; "
                f"minimum={gaps[-1]} at t={t_max}"
            )


def check_overlap_scalar_bounds() -> None:
    for c in (7, 8):
        m = 5 * c
        lower = 3 * comb(m, 2)
        upper_bound = 122 * c * c
        assert lower <= upper_bound
        print(
            f"c={c}, m={m}: crossing lower={lower}, "
            f"scalar upper={upper_bound}; no contradiction"
        )


if __name__ == "__main__":
    check_zero_excess_table()
    check_overlap_scalar_bounds()
    print("ARITHMETIC_AUDIT_OK")
