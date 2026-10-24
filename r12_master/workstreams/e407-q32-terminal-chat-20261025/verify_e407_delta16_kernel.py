#!/usr/bin/env python3
"""Arithmetic/kernel audit for the E407 Q32 delta=16 four-partite case.

Checks exact edge ledgers, integer partitions, and finite excess inequalities.
It does NOT construct or certify a graph realization or independently prove
the graph-theoretic lemmas.
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
    # In the (5,0) split, 3 non-endpoint D vertices go to 2 K5s, so one K5
    # receives >=2. Each of its 5 vertices needs >=1 excess unit: 7 small-part
    # neighbours plus 2 D neighbours, against baseline U-degree 8.
    assert (3 + 1) // 2 == 2
    assert 5 > 4
    assert 4 * (7 + 5 - 9) > 4

    print("E407_DELTA16_STRUCTURAL_KERNEL_ARITHMETIC_OK")


if __name__ == "__main__":
    main()
