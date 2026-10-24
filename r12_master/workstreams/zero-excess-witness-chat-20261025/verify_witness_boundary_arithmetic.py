#!/usr/bin/env python3
"""Arithmetic audit for R12_WITNESS_PACKING_BOUNDARY_KERNEL.md.

This checks integer edge/degree identities, Turan numbers, and witness-count
thresholds. It does not certify a graph realization or the analytic theorems.
"""
from itertools import product


def turan_edges(n: int, r: int = 4) -> int:
    q, rem = divmod(n, r)
    parts = [q + 1] * rem + [q] * (r - rem)
    return (n * n - sum(x * x for x in parts)) // 2


def check_turan_values() -> None:
    expected = {
        13: 63, 14: 73, 15: 84, 16: 96, 18: 121, 19: 135,
        27: 273, 28: 294, 29: 315, 30: 337, 31: 360, 32: 384,
    }
    for n, e in expected.items():
        assert turan_edges(n) == e, (n, turan_edges(n), e)


def check_e407_boundary() -> None:
    feasible = []
    for eps in range(5):
        for g in range(17):
            if g + eps > 16 or eps + 2 * g < 2:
                continue
            e_star = 112 - g
            cross = 124 + eps + 2 * g
            e_w = 48 - eps - g
            assert e_star + cross + e_w == 284
            assert 2 * e_star + cross == 348 + eps
            assert 2 * e_w + cross == 220 - eps
            assert e_w >= 32
            assert 294 + g <= turan_edges(29)
            feasible.append((eps, g))
    assert feasible
    assert all(g + eps <= 16 and eps + 2 * g >= 2 for eps, g in feasible)
    print("E407 boundary feasible (epsilon_*, g) pairs:", feasible)


def check_e408_boundary() -> None:
    feasible = []
    for eps in range(5):
        for g in range(18):
            if g + eps > 17:
                continue
            e_star = 129 - g
            cross = 114 + eps + 2 * g
            e_w = 41 - eps - g
            assert e_star + cross + e_w == 284
            assert 2 * e_star + cross == 372 + eps
            assert 2 * e_w + cross == 196 - eps
            assert e_w >= 24
            assert 336 + g <= turan_edges(31)
            feasible.append((eps, g))
    assert feasible
    print("E408 Q33 boundary feasible (epsilon_*, g) pairs:", feasible)


def check_support_thresholds() -> None:
    # Seven selected Q blocks per exact-129 color; each contributes six
    # distinct complement edges, and alpha(H)<=4 makes the complement K5-free.
    assert 6 * 7 == 42
    assert 6 * 8 * 7 == 336
    assert 6 * 9 * 7 == 378
    assert turan_edges(27) < 294 <= turan_edges(28)
    assert turan_edges(29) < 336 <= turan_edges(30)
    assert 6 * 9 * 7 > turan_edges(31)
    # Brouwer thresholds used in the recorded proof: non-4-partite maxima.
    assert turan_edges(29) - (29 // 4) + 1 == 309
    assert turan_edges(30) - (30 // 4) + 1 == 331
    print("Witness support thresholds checked.")


def check_high_support_and_zero_excess() -> None:
    # Six distinct B labels cannot all lie among at most five labels with k<=1.
    for h in range(5, 11):
        low_labels = 10 - h
        assert low_labels <= 5
        assert 6 > low_labels
    # Six disjoint B-labelled four-sets and at most four excess vertices
    # leave at least two four-sets wholly outside the excess set.
    for high_vertices in range(5):
        assert 6 - high_vertices >= 2
    print("High-support and zero-excess count checks passed.")


if __name__ == "__main__":
    check_turan_values()
    check_e407_boundary()
    check_e408_boundary()
    check_support_thresholds()
    check_high_support_and_zero_excess()
    print("WITNESS_BOUNDARY_ARITHMETIC_OK")
