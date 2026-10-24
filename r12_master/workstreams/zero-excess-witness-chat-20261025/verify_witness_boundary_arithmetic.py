#!/usr/bin/env python3
"""Arithmetic audit for R12_WITNESS_PACKING_BOUNDARY_KERNEL.md.

Checks integer edge/degree identities, Turan numbers, support thresholds, and
the forced degree windows in the E407/E408 boundary reductions. It does not
certify a graph realization or substitute for the analytic lemmas.
"""
from math import comb


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
        for delta in range(17):
            if delta + eps > 16 or eps + 2 * delta < 2:
                continue
            e_u = 112 - delta
            cross = 124 + eps + 2 * delta
            e_w = 48 - eps - delta
            assert e_u + cross + e_w == 284
            assert 2 * e_u + cross == 348 + eps
            assert 2 * e_w + cross == 220 - eps
            assert e_w >= 32
            assert 294 + delta <= turan_edges(29)
            feasible.append((eps, delta))
    assert feasible
    print("E407 boundary ledger pairs (epsilon_U, delta):", feasible)

    # Independent transversal theorem excludes delta <= 1.
    assert all(20 - 2 * delta - eps > 12
               for delta in (0, 1) for eps in range(5))


def check_e408_boundary() -> None:
    feasible = []
    for eps in range(5):
        for delta in range(18):
            if delta + eps > 17:
                continue
            e_u = 129 - delta
            cross = 114 + eps + 2 * delta
            e_w = 41 - eps - delta
            assert e_u + cross + e_w == 284
            assert 2 * e_u + cross == 372 + eps
            assert 2 * e_w + cross == 196 - eps
            assert e_w >= 24
            assert 336 + delta <= turan_edges(31)
            feasible.append((eps, delta))
    assert feasible
    print("E408 Q33 boundary ledger pairs (epsilon_U, delta):", feasible)



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


def check_e408_four_partite_s0_exclusion() -> None:
    # S0 = epsilon_U + 2*delta, epsilon_U <= 4, delta+epsilon_U <= 17.
    feasible = {
        s0: [delta for delta in range(18)
             if 0 <= s0 - 2 * delta <= 4
             and delta + (s0 - 2 * delta) <= 17]
        for s0 in (8, 9, 10)
    }
    assert feasible[8] == [2, 3, 4]
    assert feasible[9] == [3, 4]
    assert feasible[10] == [3, 4, 5]

    # The K13 prohibition gives k=#(q_w=7) <= 5 in the four-partite branch:
    # the q=7 vertices form a clique and are complete to the 7-clique D.
    # Since x=114+S0 and all other q_w >= 8, x >= 128-k.
    assert 114 + 8 < 128 - 5  # S0 <= 8 impossible.
    # S0=9: x=123 forces k=5 and eleven q=8 vertices.
    assert 128 - 5 == 123
    assert 123 - 7 * 5 == 11 * 8
    # S0=10: x=124 allows only k=4 or 5.
    assert [k for k in range(6) if 7 * k + 8 * (16-k) <= 124] == [4, 5]
    assert 124 - 7 * 4 == 12 * 8
    assert 124 - 7 * 5 == 10 * 8 + 9

    # A large part G has at least 8+delta-S0 zero-excess vertices with no
    # extra-L incidence. Each has exactly three W-neighbours, so at most
    # three W vertices can have a neighbourhood containing all of G.
    for s0 in (9, 10):
        for delta in feasible[s0]:
            eps_u = s0 - 2 * delta
            assert 8 - delta - eps_u == 8 + delta - s0
            assert 8 + delta - s0 >= 1

    # At most 6-k additional W vertices can have a U-neighbourhood
    # containing all D; the k q=7 vertices already occupy those slots.
    # For S0=9, k=5: at least 11-(6-5)=10 full-large-part neighborhoods.
    assert 11 - (6 - 5) == 10
    # For S0=10, k=4 or 5: in either degree pattern at least ten
    # q=8/9 vertices remain, and at least ten must be full-large-part.
    assert 12 - (6 - 4) == 10
    assert 11 - (6 - 5) == 10
    # Only three W vertices per each of A,B,C can have a full-part neighborhood.
    assert 3 * 3 == 9
    assert 10 > 9
    print("E408 Q33 four-partite branch: S0 >= 11 checked arithmetically.")


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
    check_e408_four_partite_s0_exclusion()
    check_high_support_and_zero_excess()
    print("WITNESS_BOUNDARY_ARITHMETIC_OK")
