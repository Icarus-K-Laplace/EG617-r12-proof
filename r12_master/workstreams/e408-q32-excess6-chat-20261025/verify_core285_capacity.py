#!/usr/bin/env python3
"""Arithmetic regression checks for the E408 Q32 285-edge/excess-six line.

This script checks integer identities and finite profile bounds only. It does
not verify the Kang–Pikhurko classification, graph realizability, or the
original K145-to-T61 reduction.
"""
from math import comb, ceil


def p4(n: int) -> int:
    """Minimum edges in an n-vertex graph with alpha <= 4."""
    q, r = divmod(n, 4)
    parts = [q + 1] * r + [q] * (4 - r)
    return sum(comb(s, 2) for s in parts)


def cap285(v: int) -> int:
    return comb(v, 2) - p4(47 - v) - 12 * v + 285


def check_core_capacity() -> None:
    expected_p4 = {
        10: 8, 9: 6, 8: 4, 7: 3, 6: 2, 5: 1, 4: 0, 3: 0,
    }
    for n, value in expected_p4.items():
        assert p4(n) == value, (n, p4(n), value)

    expected_cap = {
        37: 499, 38: 526, 39: 554, 40: 582,
        41: 611, 42: 641, 43: 672, 44: 703,
    }
    for v, value in expected_cap.items():
        assert cap285(v) == value, (v, cap285(v), value)

    # Capacity-only floors from N >= 10m.
    capacity_profiles = {
        8: (80, 480, 37),
        9: (90, 540, 39),
        10: (100, 600, 41),
    }
    for m, (n_witnesses, six_n, v_min) in capacity_profiles.items():
        assert n_witnesses == 10 * m
        assert six_n == 6 * n_witnesses
        assert cap285(v_min - 1) < six_n
        assert cap285(v_min) >= six_n

    # One exact color gives ten disjoint Q sets, hence v >= 40.
    combined = {8: 40, 9: 40, 10: 41}
    for m, v_min in combined.items():
        n_witnesses, six_n, _ = capacity_profiles[m]
        assert v_min >= 40
        assert cap285(v_min) >= six_n

    # An exact color with 11 disjoint witnesses forces v >= 44.
    assert cap285(43) == 672
    assert 4 * 11 == 44

    # Exact slack budgets at the combined minimum support sizes.
    assert cap285(40) - 6 * 80 == 102
    assert cap285(40) - 6 * 90 == 42
    assert cap285(41) - 6 * 100 == 11


def check_shell_budget() -> None:
    assert comb(14, 2) - 11 * 2 == 69
    assert 13 + (78 - 22) == 69
    assert 22 <= 32
    assert 0 <= 32 - 22 <= 10
    assert 0 <= 32 - 32 <= 10

    # M[B]=empty, |S|=3, |B|=10: c=e(M)-beta, c>=19, c<=30.
    for e_m in range(22, 33):
        for beta in range(4):
            c = e_m - beta
            if c <= 30:
                assert c >= 19
                h_min = ceil((c - 10) / 2)
                assert h_min >= 5
                assert c <= 10 + 2 * h_min


def check_outer_blocker_coupling() -> None:
    # m exact-129 colors, sum s_C=3, total sum P_C=252.
    for m in (8, 9, 10):
        p_exact_min = 62 * m - 427
        assert p_exact_min == {8: 69, 9: 131, 10: 193}[m]
        floor_sum_min = ceil((p_exact_min - 6 * m) / 7)
        assert floor_sum_min == 8 * m - 61
        used_witness_min = m + floor_sum_min
        assert used_witness_min == 9 * m - 61
        assert used_witness_min == {8: 11, 9: 20, 10: 29}[m]

    # M_C >= 15 + P_C; at most 14 occurrences can come from two non-witness
    # isolated components (each component used at most once in each of 7 blocks).
    for p_c in range(56):
        good_occurrences = p_c + 1
        good_components = ceil(good_occurrences / 7)
        assert good_components == p_c // 7 + 1

    assert 15 + 55 == 70
    assert 10 * 7 == 70


if __name__ == "__main__":
    check_core_capacity()
    check_shell_budget()
    check_outer_blocker_coupling()
    print("CORE285_E408_Q32_ARITHMETIC_OK")
