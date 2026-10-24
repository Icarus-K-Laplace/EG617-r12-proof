#!/usr/bin/env python3
"""Exact arithmetic replay for zero-excess witness and beta-sensitive bounds.

Standard library only. Checks finite arithmetic, not graph realization,
inherited extremal theorems, or the original K145-to-core reduction.
"""
from math import comb


def turan_edges(n, r):
    q, rem = divmod(n, r)
    parts = [q + 1] * rem + [q] * (r - rem)
    return comb(n, 2) - sum(comb(s, 2) for s in parts)


def p3(n):
    return comb(n, 2) - turan_edges(n, 3)


def upper(E, k, t):
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
    for (E, k), want in expected.items():
        t = 6 if E == 4 else 4
        n = 47 - k - t
        got = (n, p3(n), upper(E, k, t), p3(n) - upper(E, k, t))
        assert got == want, ((E, k), got, want)
        assert got[-1] > 0

    pair_floor = {
        "A": 45 - comb(4, 2), "B": 45 - comb(8, 2),
        "C": 45 - comb(4, 2), "D": 45 - comb(9, 2),
        "E_full": 45 - comb(9, 2),
    }
    assert pair_floor == {"A": 39, "B": 17, "C": 39, "D": 9, "E_full": 9}

    component_count = {0: (7, 6), 1: (8, 7), 2: (8, 7), 3: (9, 8)}
    zero_per_color = {beta: b_labels - 4
                      for beta, (_, b_labels) in component_count.items()}
    assert zero_per_color == {0: 2, 1: 3, 2: 3, 3: 4}
    assert {0: 7 * zero_per_color[0], 1: 7 * zero_per_color[1],
            2: 7 * zero_per_color[2]} == {0: 14, 1: 21, 2: 21}
    assert {0: 8 * zero_per_color[0], 1: 8 * zero_per_color[1],
            2: 8 * zero_per_color[2], 3: 8 * zero_per_color[3]} == {
                0: 16, 1: 24, 2: 24, 3: 32
            }

    assert [turan_edges(n, 4) for n in (19, 27, 28, 29, 30, 31)] == [
        135, 273, 294, 315, 337, 360
    ]
    assert turan_edges(30, 3) == 300
    assert 300 - (30 // 3) + 1 == 291
    assert 435 - 136 == 299 > 291

    print("ZERO-EXCESS ENDPOINT GAPS: ALL 10 POSITIVE AND EXACT")
    print("PAIRWISE HUB-COVER FLOORS:", pair_floor)
    print("BETA-SENSITIVE ZERO-EXCESS FLOORS:", zero_per_color)
    print("E407 GLOBAL FLOORS: beta0=14, beta1=21, beta2=21")
    print("E408 Q33 GLOBAL FLOORS: beta0=16, beta1/2=24, beta3=32")
    print("STAR AUDIT: tripartite does not imply complete tripartite")
    print("ARITHMETIC AUDIT PASS; NO GRAPH-THEORETIC CLOSURE CLAIMED")


if __name__ == "__main__":
    main()
