#!/usr/bin/env python3
"""Exact integer-profile regression checks for the S0=11 theorem.

This verifies only the degree-profile enumeration and numerical margins. It
does not certify a graph realization or substitute for the analytic proof.
"""
from math import comb


def nondecreasing_patterns(n: int, total: int, lo: int = 8, hi: int = 30):
    out = []

    def rec(prefix, left, slots, minimum):
        if slots == 0:
            if left == 0:
                out.append(tuple(prefix))
            return
        for value in range(minimum, hi + 1):
            if value > left:
                break
            if left - value < lo * (slots - 1):
                continue
            if left - value > hi * (slots - 1):
                continue
            rec(prefix + [value], left - value, slots - 1, value)

    rec([], total, n, lo)
    return out


def main():
    # S0=11 forces delta=4,5 and epsilon_U=3,1.
    profiles = [
        (delta, 11 - 2 * delta)
        for delta in range(18)
        if 0 <= 11 - 2 * delta <= 4
        and delta + (11 - 2 * delta) <= 17
    ]
    assert profiles == [(4, 3), (5, 1)]

    # Cross-edge count x=125 forces k>=3; the zero-excess D cap gives k<=6.
    assert [128 - k <= 125 for k in range(7)] == [
        False, False, False, True, True, True, True
    ]

    expected = {
        3: [(8,) * 13],
        4: [(8,) * 11 + (9,)],
        5: [(8,) * 10 + (10,), (8,) * 9 + (9, 9)],
        6: [
            (8,) * 9 + (11,),
            (8,) * 8 + (9, 10),
            (8,) * 7 + (9, 9, 9),
        ],
    }
    for k, patterns in expected.items():
        got = nondecreasing_patterns(16 - k, 125 - 7 * k)
        assert got == patterns, (k, got, patterns)

    # For delta=4,5 the per-large-part full-neighborhood capacity is three.
    assert [8 - delta - (11 - 2 * delta) for delta in (4, 5)] == [1, 2]

    # For the exceptional size-10/11 hitting sets, t_i <= q-7; after removing
    # at most one spillover, all three outside parts still have at least 4 points.
    assert 8 - (10 - 7) - 1 == 4
    assert 8 - (11 - 7) == 4
    # Two subsets of size at least 4 in C0 have at least 2 common points.
    assert 4 + 4 - 6 == 2

    print("S0_11_PROFILE_AUDIT_OK")


if __name__ == "__main__":
    main()
