#!/usr/bin/env python3
"""Arithmetic replay for the E407 delta=13, epsilon_U=1 two-cross-edge terminal.

This checks exact ledgers, integer capacity bounds, and the D-part t-vector
count. It does NOT machine-prove the analytic blocker, reverse-saturation,
or independent-set arguments in the companion theorem.
"""
from itertools import product


def allocations(total, n=4):
    for E in product(range(total + 1), repeat=n):
        if sum(E) == total:
            yield E


def cap4(E, e):
    return 8 + int(E >= e)


def cap5(E):
    return 2 + E


profiles = {
    "different_pairs_disjoint": (1, 1, 1, 1),
    "different_pairs_shared_K4": (2, 1, 1, 0),
    "different_pairs_shared_K5": (1, 0, 2, 1),
    "same_pair_K4K4": (2, 2, 0, 0),
    "same_pair_K4K5_disjoint": (1, 0, 1, 0),
    "same_pair_K4K5_star_at_K4": (2, 0, 1, 0),
    "same_pair_K4K5_star_at_K5": (1, 0, 2, 0),
    "same_pair_K5K5": (0, 0, 2, 2),
}
expected_max = {
    "different_pairs_disjoint": 23,
    "different_pairs_shared_K4": 23,
    "different_pairs_shared_K5": 24,
    "same_pair_K4K4": 23,
    "same_pair_K4K5_disjoint": 24,
    "same_pair_K4K5_star_at_K4": 24,
    "same_pair_K4K5_star_at_K5": 24,
    "same_pair_K5K5": 25,
}


def max_capacity(e):
    return max(
        cap4(E[0], e[0]) + cap4(E[1], e[1]) + cap5(E[2]) + cap5(E[3])
        for E in allocations(3)
    )


def check_ledgers():
    assert 2 * 6 + 2 * 10 + 2 == 34
    assert 112 - 13 == 99
    assert 124 + 1 + 2 * 13 == 151
    assert 2 * 284 - 12 * 47 == 4
    assert 4 - 1 == 3
    assert 5 + 3 == 8
    assert 29 - 24 == 5


def check_capacity_profiles():
    for name, e in profiles.items():
        got = max_capacity(e)
        assert got == expected_max[name], (name, got, expected_max[name])
        if name != "same_pair_K5K5":
            assert got <= 24, (name, got)
    assert 29 - 1 == 28 > expected_max["same_pair_K5K5"]


def check_D_t_vectors():
    checked = 0
    for t in product(range(3), repeat=8):
        if sum(t) != 8:
            continue
        for positive in [None, *range(8)]:
            eps = [0] * 8
            if positive is not None:
                eps[positive] = 1
            if any(t[i] > 1 + eps[i] for i in range(8)):
                continue
            good = sum(1 for i in range(8) if t[i] == 1 and eps[i] == 0)
            assert good >= 6, (t, eps, good)
            checked += 1
    assert checked > 0


def main():
    check_ledgers()
    check_capacity_profiles()
    check_D_t_vectors()
    print("DELTA13_EPS1_TWO_CROSS_EDGE_TERMINAL_ARITHMETIC_OK")
    print("All eight placement capacity profiles replayed; every K4-incident profile has cap <=24.")
    print("Every feasible D-part t-vector has at least six vertices with t=1 and epsilon=0.")
    print("Analytic blocker/saturation/independence lemmas remain proof dependencies.")


if __name__ == "__main__":
    main()
