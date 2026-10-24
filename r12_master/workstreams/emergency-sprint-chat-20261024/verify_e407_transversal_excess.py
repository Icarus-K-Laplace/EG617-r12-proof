#!/usr/bin/env python3
"""Arithmetic regression checks for R12_E407_TRANSVERSAL_EXCESS_BOUND.md.

This verifies edge ledgers and the final integer inequality only. It does not
verify the graph-theoretic transversal lemmas or a graph realization.
"""
from math import comb


def p4(n: int) -> int:
    q, r = divmod(n, 4)
    return sum(comb(s, 2) for s in [q + 1] * r + [q] * (4 - r))


def main() -> None:
    # Exact E407 core ledger.
    assert p4(18) == 32
    for epsilon_u in range(5):
        for delta in range(17):
            if delta + epsilon_u > 16:
                continue
            e_hu = 112 - delta
            cross = 124 + epsilon_u + 2 * delta
            e_hw = 48 - epsilon_u - delta
            assert e_hu + cross + e_hw == 284
            assert e_hw >= 32
            assert delta + epsilon_u <= 16

    # Combine N7 >= 20-S and N7 <= 10+S/7.
    # Every integer S<=8 gives incompatible bounds.
    for S in range(9):
        lower = 20 - S
        upper = 10 + S / 7
        assert lower > upper, (S, lower, upper)

    # With epsilon_U<=4, S=epsilon_U+2*delta>=9 forces delta>=3.
    for delta in range(3):
        for epsilon_u in range(5):
            assert epsilon_u + 2 * delta <= 8

    print("E407_TRANSVERSAL_EXCESS_ARITHMETIC_OK")


if __name__ == "__main__":
    main()
