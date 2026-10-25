#!/usr/bin/env python3
"""Arithmetic replay for the E407 Q32 two-cross-edge profile reduction.

Checks finite ledger/capacity arithmetic only; it does not verify the
graph-theoretic transversal-blocker classification or analytic lemmas.
Uses only the Python standard library.
"""
from math import floor


def check_exact_ledger():
    assert 6 + 6 + 10 + 10 == 32
    assert 32 + 2 == 34
    assert 112 - 13 == 99
    assert 124 + 1 + 2 * 13 == 151
    assert 2 * 284 - 12 * 47 == 4
    assert 4 - 1 == 3
    assert 29 - 25 == 4
    assert 29 - 24 == 5


def check_k5_capacity():
    for E_i in range(4):
        assert floor((5 + E_i) / 2) <= 2 + E_i
        assert (1 + E_i) + floor((4 + E_i) / 4) <= 2 + E_i
        assert floor(E_i / 4) == 0


def check_k4_capacity():
    for E_i in range(4):
        load = 8 + E_i
        assert load <= 11
        assert 7 + floor(load / 4) <= 9
        assert (2 + E_i) + floor((6 + E_i) / 3) <= 8
        assert (2 + E_i) + floor(E_i / 3) <= 6
        assert floor(load / 2) <= 5
    assert 7 + floor(6 / 3) == 9
    assert 7 + floor(3 / 3) == 8


def check_global_capacity():
    for E3 in range(4):
        for E4 in range(4):
            if E3 + E4 <= 3:
                assert 9 + 9 + (2 + E3) + (2 + E4) <= 25
                if E3 + E4 <= 2:
                    assert 9 + 9 + (2 + E3) + (2 + E4) <= 24
    assert 18 + 4 + 2 == 24


def main():
    check_exact_ledger()
    check_k5_capacity()
    check_k4_capacity()
    check_global_capacity()
    print("DELTA13_EPS1_TWO_CROSS_EDGE_ARITHMETIC_OK")


if __name__ == "__main__":
    main()
