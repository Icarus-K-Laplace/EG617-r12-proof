#!/usr/bin/env python3
"""Exact arithmetic replay for zero-excess witness and corrected count bounds.

Standard library only. This checks finite arithmetic, not graph realization,
the inherited extremal theorems, or the original K145-to-core reduction.
"""
from math import comb


def turan_edges(n, r):
    q, rem = divmod(n, r)
    parts = [q + 1] * rem + [q] * (r - rem)
    return (n * n - sum(x * x for x in parts)) // 2


def p3(n):
    return comb(n, 2) - turan_edges(n, 3)


def upper(E, k, t):
    # e(H_0-T) upper bound in the retained zero-excess proof.
    return 282 - E // 2 - 12 * k + comb(k, 2) - t * (12 - k) + comb(t, 2)


def main():
    expected = {
        (4, 1): (40, 247, 217, 30),
        (4, 2): (39, 234, 212, 22),
        (4, 3): (38, 222, 208, 14),
        (4, 4): (37, 210, 205, 5),
        (6, 1): (42, 273, 229, 44),
        (6, 2): (41, 260, 222, 38),
        (6, 3): (40, 247, 216, 31),
        (6, 4): (39, 234, 211, 23),
        (6, 5): (38, 222, 207, 15),
        (6, 6): (37, 210, 204, 6),
    }
    for E, k in expected:
        t = 6 if E == 4 else 4
        n = 47 - k - t
        actual = (n, p3(n), upper(E, k, t), p3(n) - upper(E, k, t))
        assert actual == expected[(E, k)], (E, k, actual)
        assert actual[-1] > 0

    pair_floor = {
        "A": 45 - comb(4, 2),   # n3 >= 6
        "B": 45 - comb(8, 2),   # n3 >= 2
        "C": 45 - comb(4, 2),   # n3 >= 6
        "D": 45 - comb(9, 2),   # n3 >= 1
        "E_full": 45 - comb(9, 2),
    }
    assert pair_floor == {"A": 39, "B": 17, "C": 39, "D": 9, "E_full": 9}

    safe_global = {
        "A": 7 * (6 - 3),
        "B": 7 * (6 - 3),
        "C": 7 * (7 - 3),
        "D": 7 * (7 - 3),
        "E_full": 7 * (7 - 3),
        "E_no_full_endpoint_complete": 7 * 7,
    }
    assert safe_global == {
        "A": 21, "B": 21, "C": 28, "D": 28,
        "E_full": 28, "E_no_full_endpoint_complete": 49,
    }
    print("ZERO-EXCESS ENDPOINT GAPS: ALL 10 POSITIVE AND EXACT")
    print("PAIR-INDEXED HUB-COVER FLOORS:", pair_floor)
    print("CORRECTED GLOBAL LABELLED WITNESS FLOORS:", safe_global)
    print("ARITHMETIC AUDIT PASS; NO GRAPH-THEORETIC CLOSURE CLAIMED")


if __name__ == "__main__":
    main()
