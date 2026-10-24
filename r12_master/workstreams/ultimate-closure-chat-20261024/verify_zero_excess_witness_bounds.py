#!/usr/bin/env python3
"""Exact arithmetic replay for zero-excess and shell-support bounds."""
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
        (4, 1): (40, 247, 217, 30), (4, 2): (39, 234, 212, 22),
        (4, 3): (38, 222, 208, 14), (4, 4): (37, 210, 205, 5),
        (6, 1): (42, 273, 229, 44), (6, 2): (41, 260, 222, 38),
        (6, 3): (40, 247, 216, 31), (6, 4): (39, 234, 211, 23),
        (6, 5): (38, 222, 207, 15), (6, 6): (37, 210, 204, 6),
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
    assert 6 - 4 == 2 and 7 * 2 == 14 and 8 * 2 == 16
    assert 6 - 3 == 3 and 7 * 3 == 21 and 6 * 7 == 42
    assert [turan_edges(n, 4) for n in (19, 27, 28, 29, 30, 31)] == [135, 273, 294, 315, 337, 360]
    assert turan_edges(30, 3) == 300 and 300 - (30 // 3) + 1 == 291
    assert 435 - 136 == 299 > 291
    assert 15 - 0 - 4 == 11 and 15 - 1 - 4 == 10
    print("ZERO-EXCESS ENDPOINT GAPS: ALL 10 POSITIVE AND EXACT")
    print("PAIRWISE HUB-COVER FLOORS:", pair_floor)
    print("SAFE COMPONENT WITNESS FLOORS: E407>=14; E408 Q33>=16")
    print("SAFE HUB-COMPLETE FLOORS: 21 if a full row exists; E-no-full endpoints>=42")
    print("FULL-ROW SUPPORT UNION: A>=11; C>=10")
    print("STAR AUDIT: tripartite does not imply complete tripartite")
    print("ARITHMETIC AUDIT PASS; NO GRAPH-THEORETIC CLOSURE CLAIMED")


if __name__ == "__main__":
    main()
