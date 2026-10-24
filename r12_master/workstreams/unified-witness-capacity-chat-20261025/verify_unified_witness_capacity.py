#!/usr/bin/env python3
"""Exact finite arithmetic checks for the unified R12 witness-capacity line.

This verifies the zero-excess endpoint tables, edge ledgers, omission-profile
bounds, and the two scalar-relaxation examples. It is not a graph search and
does not certify realization of a witness hypergraph or a colored graph.
"""
from math import comb


def p3(n: int) -> int:
    """Minimum edges in an n-vertex graph with alpha <= 3."""
    q, r = divmod(n, 3)
    parts = [q + 1] * r + [q] * (3 - r)
    return sum(comb(x, 2) for x in parts)


def p_alpha4(n: int) -> int:
    """Minimum edges in an n-vertex graph with alpha <= 4."""
    q, r = divmod(n, 4)
    parts = [q + 1] * r + [q] * (4 - r)
    return sum(comb(x, 2) for x in parts)


def partitions(total: int, cap: int, minpart: int = 1):
    """Yield nonincreasing positive integer partitions, parts <= cap."""
    if total == 0:
        yield ()
        return
    for x in range(min(cap, total), minpart - 1, -1):
        for tail in partitions(total - x, x, minpart):
            yield (x,) + tail


def omission_max_e407(s: int) -> int:
    best = -1
    for parts in partitions(7, 6):
        k = len(parts)
        n0 = 29 - k
        n1 = sum(x == 1 for x in parts)
        if 5 * n0 + 2 * n1 <= 124 + s:
            omega = sum(comb(x, 2) for x in parts)
            best = max(best, omega)
    return best


def omission_max_e408(s0: int) -> int:
    best = -1
    for parts in partitions(24, 7):
        k = len(parts)
        n0 = 31 - k
        n1 = sum(x == 1 for x in parts)
        if 6 * n0 + 3 * n1 <= 114 + s0:
            omega = sum(comb(x, 2) for x in parts)
            best = max(best, omega)
    return best


def check_zero_excess_endpoint_tables() -> None:
    # Source theorem: e(H0-T) <= U(E,k,t); Turan lower bound is p3(n).
    e284 = [(40, 217), (39, 212), (38, 208), (37, 205)]
    e285 = [(42, 229), (41, 222), (40, 216),
            (39, 211), (38, 207), (37, 204)]
    gaps284 = [p3(n) - u for n, u in e284]
    gaps285 = [p3(n) - u for n, u in e285]
    assert gaps284 == [30, 22, 14, 5]
    assert gaps285 == [44, 38, 31, 23, 15, 6]

    # Check the monotonic-gap condition used to reduce all t<=tmax to tmax.
    # p3(n)-p3(n-1)=floor((n-1)/3), while U(t)-U(t+1)=12-k-t.
    for k in range(1, 5):
        for t in range(0, 6):
            n = 47 - k - t
            assert (p3(n) - p3(n - 1)) >= (12 - k - t)
    for k in range(1, 7):
        for t in range(0, 4):
            n = 47 - k - t
            assert (p3(n) - p3(n - 1)) >= (12 - k - t)


def check_edge_ledgers() -> None:
    assert comb(29, 2) == 406 and p_alpha4(18) == 32
    assert 406 - 32 - 12 * 29 + 284 == 310
    assert comb(31, 2) == 465 and p_alpha4(16) == 24
    assert 465 - 24 - 12 * 31 + 284 == 353

    # E407 boundary ledgers.
    eps, delta = 3, 3
    assert eps + 2 * delta == 9
    assert eps + delta <= 16
    assert 112 - delta == 109
    assert 124 + eps + 2 * delta == 133
    assert 48 - eps - delta == 42
    assert 294 + delta == 297 <= 310 - eps

    # E408 Q33 boundary ledgers.
    eps, delta = 4, 4
    assert eps + 2 * delta == 12
    assert eps + delta <= 17
    assert 129 - delta == 125
    assert 114 + eps + 2 * delta == 126
    assert 41 - eps - delta == 33
    assert 336 + delta == 340 <= 353 - eps


def check_omission_tables() -> None:
    e407_expected = {
        9: 7, 10: 10, 11: 11, 12: 11,
        **{s: 15 for s in range(13, 33)},
    }
    for s, expected in e407_expected.items():
        assert omission_max_e407(s) == expected, (s, omission_max_e407(s), expected)

    e408_expected = {
        12: 24, 13: 24, 14: 24,
        15: 29, 16: 29, 17: 29,
        18: 31, 19: 31, 20: 31,
        21: 33, 22: 33, 23: 33,
        24: 37, 25: 37, 26: 37,
        27: 41, 28: 41, 29: 41,
        30: 47, 31: 47, 32: 47,
        33: 48, 34: 48,
    }
    for s0, expected in e408_expected.items():
        assert omission_max_e408(s0) == expected, (
            s0, omission_max_e408(s0), expected
        )

    # Witness multiplicity / overlap identities.
    assert 7 * 29 - 196 == 7
    assert 8 * 31 - 224 == 24
    # E407 omission profile (4,2,1,0^26), Omega=7.
    e407_parts = (4, 2, 1)
    assert sum(e407_parts) == 7
    assert sum(comb(x, 2) for x in e407_parts) == 7
    assert 5 * 26 + 2 <= 124 + 9
    # E408 profile (6,2^9,0^21), Omega=24.
    e408_parts = (6,) + (2,) * 9
    assert sum(e408_parts) == 24
    assert sum(comb(x, 2) for x in e408_parts) == 24
    assert 6 * 21 <= 114 + 12


def check_label_count_matrix() -> None:
    # Rows are eight colors, columns are ten B labels. Row sums are one 7
    # and seven 6s; column sums are (6,6,5,5,5,5,4,4,5,4).
    matrix = [
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    ]
    assert [sum(row) for row in matrix] == [7, 6, 6, 6, 6, 6, 6, 6]
    assert [sum(matrix[i][j] for i in range(8)) for j in range(10)] == [
        6, 6, 5, 5, 5, 5, 4, 4, 5, 4
    ]


def main() -> None:
    check_zero_excess_endpoint_tables()
    check_edge_ledgers()
    check_omission_tables()
    check_label_count_matrix()
    print("R12_UNIFIED_WITNESS_CAPACITY_ARITHMETIC_OK")
    print("Scope: exact integer/degree ledgers only; no graph-realization certificate.")


if __name__ == "__main__":
    main()
