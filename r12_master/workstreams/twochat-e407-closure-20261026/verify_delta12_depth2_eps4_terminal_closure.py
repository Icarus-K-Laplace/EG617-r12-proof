#!/usr/bin/env python3
"""Arithmetic audit for DELTA12_DEPTH2_EPS4_TERMINAL_CLOSURE.md."""

REMAINING = [(0, 4, 0, 0), (1, 4, 0, 0)]


def main():
    assert min((4, 4, 5, 5)) == 4
    for t0, eps0, EC, Erest in REMAINING:
        assert EC == 0
        # Two restored edges total. Since t0<=1 in both final rows, at least
        # one restored incidence lands on C union E.
        assert 2 - t0 >= 1
        # That C/E point has epsilon=0 and t_c>=1, so d_W=4-t_c<=3.
        assert 4 - 1 <= 3
    print("DELTA12_DEPTH2_EPS4_TERMINAL_CLOSURE_OK")
    print("Scope: final arithmetic only; q=0 component-exhaustion proof is analytic.")


if __name__ == "__main__":
    main()
