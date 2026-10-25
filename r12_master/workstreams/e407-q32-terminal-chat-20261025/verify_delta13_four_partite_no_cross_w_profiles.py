#!/usr/bin/env python3
"""Arithmetic replay only for DELTA13_FOUR_PARTITE_NO_CROSS_W_PROFILES.md.

This checks the finite integer profile list and the stated upper-bound arithmetic.
It does not verify graph-theoretic saturation, label-capacity, or the upstream T61 contract.
"""
from itertools import combinations_with_replacement


def partitions(n, k, minimum=1, prefix=()):
    if k == 1:
        if n >= minimum:
            yield prefix + (n,)
        return
    for x in range(minimum, n // k + 1):
        yield from partitions(n - x, k - 1, x, prefix + (x,))


def compositions(total, k, prefix=()):
    if k == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from compositions(total - x, k - 1, prefix + (x,))


def choose2(x):
    return x * (x - 1) // 2


def check_profile_enumeration():
    expected = {
        1: [(3, 4, 5, 6)],
        2: [(3, 5, 5, 5), (4, 4, 4, 6)],
        3: [(4, 4, 5, 5)],
    }
    for eps_u, target_edges in ((1, 34), (2, 33), (3, 32)):
        actual = [
            p for p in partitions(18, 4)
            if sum(choose2(x) for x in p) == target_edges
        ]
        assert actual == expected[eps_u], (eps_u, actual, expected[eps_u])


def check_epsilon_u_1_capacity():
    # E3+E4+E5+E6 = E_W = 3.
    worst = -1
    for E3, E4, E5, E6 in compositions(3, 4):
        cap = (
            9 + E3 + int(E3 == 0)
            + 8 + E4 + int(E4 == 0)
            + 5 + E5
            + E6 // 2
        )
        worst = max(worst, cap)
        assert cap <= 27, (E3, E4, E5, E6, cap)
    assert worst == 27


def check_epsilon_u_2_capacities():
    # K3 + 3K5: if a K5 has excess 2 and an unsaturated vertex,
    # the exceptional cap is 10+8+5+5=28. Otherwise all are saturated.
    worst_saturated = -1
    for alloc in compositions(2, 4):
        E3, E51, E52, E53 = alloc
        cap = 24 + 2 + int(E3 == 0)
        worst_saturated = max(worst_saturated, cap)
        assert cap <= 27, (alloc, cap)
        if 2 in (E51, E52, E53):
            assert E3 == 0
            other = [x for x in (E51, E52, E53) if x != 2]
            assert other == [0, 0]
            assert 10 + 8 + 5 + 5 == 28
    assert worst_saturated == 27

    # 3K4 + K6: each K4 cap <=9, K6 cap <= floor(E6/2) <=1.
    for E6 in range(3):
        assert 3 * 9 + E6 // 2 <= 28


def check_epsilon_u_3_capacity():
    # E4a+E4b+E5a+E5b = E_W = 1.
    for E4a, E4b, E5a, E5b in compositions(1, 4):
        cap = 9 + 9 + (2 + E5a) + (2 + E5b)
        assert cap <= 23, (E4a, E4b, E5a, E5b, cap)


if __name__ == "__main__":
    check_profile_enumeration()
    check_epsilon_u_1_capacity()
    check_epsilon_u_2_capacities()
    check_epsilon_u_3_capacity()
    print("DELTA13_FOUR_PARTITE_NO_CROSS_W_PROFILES_ARITHMETIC_OK")
