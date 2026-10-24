#!/usr/bin/env python3
"""Exact arithmetic/case-ledger checks for R12_E408_Q33_UNIVERSAL_S0_11.md.

This verifier checks numerical identities and finite multiplicity cases only.
It is not a graph-realization certificate and does not replace the analytic
transversal, clique, or independent-set arguments in the theorem note.
"""
from math import comb


def main() -> None:
    # Core edge/degree ledger at |U|=31, |W|=16.
    assert comb(31, 2) == 465
    assert 465 - 336 == 129
    assert 372 - 2 * 129 == 114
    # e(U,W)=114+S0 and sum(q_w) is this cross-edge count.
    for s0 in range(0, 18):
        cross = 114 + s0
        n7_floor = max(0, 128 - cross)
        assert n7_floor == max(0, 14 - s0)
    # If S0=10, N7>=4 and N7<=4, and the remaining 12 degrees are exactly 8.
    s0 = 10
    cross = 114 + s0
    n7 = 14 - s0
    assert cross == 124 and n7 == 4
    assert cross - 7 * n7 == 96 == 12 * 8

    # Seven-point transversal incidence checks:
    # for t<=5, n1 + n2 <= t floor((31-t)/3) + C(t,2) < 56.
    small_t_bounds = {
        t: t * ((31 - t) // 3) + comb(t, 2)
        for t in range(0, 6)
    }
    assert list(small_t_bounds.values()) == [0, 10, 19, 30, 42, 50]
    assert all(bound < 56 for bound in small_t_bounds.values())
    # t=6: incidence lower bound 64 exceeds the point-incidence upper bound 60.
    assert 6 * ((31 - 6) // 3) == 48
    assert 56 + (56 - 48) == 64 > 6 * ((31 - 1) // 3) == 60

    # In the equality kernel, the T-W incidence identity forces a=2:
    # eps_T = 7a - 14, while a<=2 from a zero-excess vertex in T.
    feasible_a = [a for a in range(13) if 7 * a - 14 >= 0 and a <= 2]
    assert feasible_a == [2]
    assert 7 * 2 - 14 == 0

    # Each repeated R-only neighborhood has multiplicity at most four:
    # 8m <= 24 + (eps_U + 2 delta) = 34.
    assert max(m for m in range(1, 10) if 8 * m <= 34) == 4

    # If t distinct 8-sets have pairwise intersections <=1, their union has
    # size at least 8t-C(t,2). Every t>=4 through 10 exceeds |R|=24.
    union_lower = {t: 8 * t - comb(t, 2) for t in range(4, 11)}
    assert union_lower == {
        4: 26, 5: 30, 6: 33, 7: 35, 8: 36, 9: 36, 10: 35
    }
    assert all(v > 24 for v in union_lower.values())

    # Three multiplicities sum to ten and each is at most four.
    patterns = []
    for a in range(1, 5):
        for b in range(a, 5):
            for c in range(b, 5):
                if a + b + c == 10:
                    patterns.append((a, b, c))
    assert patterns == [(2, 4, 4), (3, 3, 4)]
    # The (4,4,2) pattern would require a_T(r)>=1 at all eight points of
    # its multiplicity-two set, impossible with only two T-type vertices.
    assert 8 > 2

    # The final clique contradiction is K8 joined completely to K4 = K12.
    assert 8 + 4 == 12 > 11
    print("E408_Q33_UNIVERSAL_S0_11_ARITHMETIC_OK")
    print("Scope: arithmetic and finite case tables only; analytic proof remains in the theorem note.")


if __name__ == "__main__":
    main()
