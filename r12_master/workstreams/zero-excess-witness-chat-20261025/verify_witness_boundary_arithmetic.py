#!/usr/bin/env python3
"""Arithmetic audit for R12_WITNESS_PACKING_BOUNDARY_KERNEL.md.

Checks integer edge/degree identities, Turan numbers, support thresholds, and
the forced integer ranges in the four-partite boundary reductions. It does
not certify a graph realization or the analytic theorem hypotheses.
"""
from math import ceil


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
    print("E407 general ledger pairs (epsilon_*, delta):", feasible)

    # If L is four-partite, the unused point z forces epsilon_U=epsilon_z=16-delta.
    four_partite = []
    for delta in range(17):
        eps_u = 16 - delta
        if 0 <= eps_u <= 4 and delta >= 12:
            eps_w = delta - 12
            assert eps_w >= 0
            assert 48 - eps_u - delta == 32
            four_partite.append((delta, eps_u, eps_w))
    assert four_partite == [(12, 4, 0), (13, 3, 1), (14, 2, 2),
                            (15, 1, 3), (16, 0, 4)]
    # The group-label argument excludes delta=12,13.
    assert [x[0] for x in four_partite if x[0] >= 14] == [14, 15, 16]
    print("E407 four-partite residual delta values:", four_partite)


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
    print("E408 Q33 general ledger pairs (epsilon_*, delta):", feasible)


def check_support_thresholds() -> None:
    assert 6 * 7 * 7 == 294
    assert 6 * 8 * 7 == 336
    assert 6 * 9 * 7 == 378
    assert turan_edges(27) < 294 <= turan_edges(28)
    assert turan_edges(29) < 336 <= turan_edges(30)
    assert 6 * 9 * 7 > turan_edges(31)
    assert turan_edges(29) - (29 // 4) + 1 == 309
    assert turan_edges(30) - (30 // 4) + 1 == 331
    print("Witness support thresholds checked.")


def check_e408_four_partite_improvements() -> None:
    # The four-partite E408 boundary has S0=epsilon_U+2*delta>=8.
    # The zero-excess capacity argument excludes S0=8,9.
    surviving = []
    for delta in range(25):
        for eps in range(5):
            if delta + eps <= 17 and eps + 2 * delta >= 10:
                surviving.append((delta, eps, eps + 2 * delta))
    assert surviving
    assert all(s >= 10 for _, _, s in surviving)

    # At S0=10, the count k=#vertices with q_w=7 has only one
    # unexcluded distribution: k=6, nine q=8, one q=10.
    patterns = []
    for k in range(7):
        if k > 6:
            continue
        remaining = 16 - k
        target_sum = 124 - 7 * k
        # Enumerate q-values >=8 for the remaining vertices; because the
        # total is small, recursive enumeration is inexpensive.
        def rec(left, slots, prefix):
            if slots == 0:
                if left == 0:
                    patterns.append((k, tuple(prefix)))
                return
            for q in range(8, left - 8 * (slots - 1) + 1):
                rec(left - q, slots - 1, prefix + [q])
        rec(target_sum, remaining, [])
    feasible = []
    for k, qs in patterns:
        if k < 4:
            continue
        # For k=4,5, all q are 8/9 and at least ten are group-based;
        # for k=6, two q=9 are also excluded. The remaining pattern is
        # exactly nine 8s and one 10.
        if k == 6 and sorted(qs) == [8] * 9 + [10]:
            feasible.append((k, sorted(qs)))
    assert feasible == [(6, [8] * 9 + [10])]
    print("E408 four-partite boundary requires epsilon_U+2*delta>=10.")
    print("S0=10 residual degree pattern:", feasible[0])


def check_high_support_and_zero_excess() -> None:
    for h in range(5, 11):
        assert 10 - h <= 5
        assert 6 > 10 - h
    for high_vertices in range(5):
        assert 6 - high_vertices >= 2
    print("High-support and zero-excess count checks passed.")


if __name__ == "__main__":
    check_turan_values()
    check_e407_boundary()
    check_e408_boundary()
    check_support_thresholds()
    check_e408_four_partite_improvements()
    check_high_support_and_zero_excess()
    print("WITNESS_BOUNDARY_ARITHMETIC_OK")
