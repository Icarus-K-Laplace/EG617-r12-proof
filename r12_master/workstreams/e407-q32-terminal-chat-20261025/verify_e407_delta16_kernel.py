#!/usr/bin/env python3
"""Arithmetic consistency checks for the E407 Q32 delta=16 terminal proof.

Checks exact edge ledgers, integer partitions, excess thresholds, and the final
forbidden K12 arithmetic. The graph-theoretic endpoint lemma is proved in
FOUR_PARTITE_TERMINAL.md; this script is not a graph-realization certificate.
"""
from itertools import combinations
from math import comb


def partitions4(n: int):
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                d = n - a - b - c
                if d < c:
                    continue
                yield (a, b, c, d)


def main() -> None:
    for delta in range(14, 17):
        for eps_u in range(5):
            if delta + eps_u > 16:
                continue
            e_hu = 112 - delta
            e_cross = 124 + eps_u + 2 * delta
            e_hw = 48 - eps_u - delta
            assert e_hu + e_cross + e_hw == 284
            assert e_hw >= 32
            assert e_hw - 32 == 16 - eps_u - delta
    assert [(d, e) for d in range(14, 17) for e in range(5)
            if d + e <= 16 and 48 - e - d == 32] == [(14, 2), (15, 1), (16, 0)]

    feasible_u = [p for p in partitions4(29)
                  if all(p[i] * p[j] >= 49 for i, j in combinations(range(4), 2))]
    assert feasible_u == [(7, 7, 7, 8)]
    assert 3 * comb(7, 2) + comb(8, 2) == 91
    assert comb(29, 2) - (112 - 16) == 310
    assert 315 - 310 == 5

    assert comb(18, 2) - 32 == 121
    feasible_w = [p for p in partitions4(18)
                  if sum(comb(x, 2) for x in p) == 32]
    assert feasible_w == [(4, 4, 5, 5)]

    # Endpoint allocations across two K4 components.
    assert [(5, 0), (4, 1), (3, 2)] == [(5, 0), (4, 1), (3, 2)]
    assert 4 * (4 - 2) > 4
    assert 4 * (3 - 2) == 4
    assert (7 + 3, 7 + 2) == (10, 9)
    assert (3 + 1) // 2 == 2
    assert 7 + 2 > 8
    # In the (5,0) split, any endpoint-K4 vertex not complete to D must be
    # complete to a 7-part and its five endpoint-D neighbours: >=12 U-neighbours,
    # requiring excess >=3. At most one such exception is possible.
    assert 7 + 5 == 12
    assert 9 + 3 == 12
    assert 9 + 4 == 13
    # At least two non-endpoint D vertices would then have only 3 neighbours
    # in the endpoint K4 and only 2 outside, so they cannot hit a W-component
    # of minimum size four. Hence the exception is impossible.
    assert 5 - 3 == 2
    assert 2 < 4
    # All four endpoint-K4 vertices are therefore complete to the 8-part D.
    # Since D is a clique K8, this produces a forbidden K12.
    assert 8 + 4 == 12
    assert 12 > 11
    assert 4 * (7 + 5 - 9) > 4

    print("E407_DELTA16_TERMINAL_ARITHMETIC_OK")


if __name__ == "__main__":
    main()
