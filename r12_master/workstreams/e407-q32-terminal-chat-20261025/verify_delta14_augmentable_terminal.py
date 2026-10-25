#!/usr/bin/env python3
"""Arithmetic replay for the delta-14 augmentable-terminal closure.

The script verifies the integer excess-budget/capacity cases stated in
DELTA14_NONPARTITE_AUGMENTABLE_TERMINAL_CLOSURE.md. It does not verify the
graph-theoretic transversal lemmas or the upstream T61/KP reduction.
"""
from itertools import product


def c3_cap(e0: int) -> int:
    # If E0 <= 2, at least one K3 vertex has zero excess and U-degree 10.
    # If E0=3, the minimum-degree bound gives at most 11 common neighbours.
    return 10 if e0 <= 2 else 11


def check_all_saturated() -> int:
    worst = 0
    for e0, e1, e2, e3 in product(range(4), repeat=4):
        if e0 + e1 + e2 + e3 != 3:
            continue
        total_cap = c3_cap(e0) + sum(4 + e for e in (e1, e2, e3))
        worst = max(worst, total_cap)
        assert total_cap < 29, (e0, e1, e2, e3, total_cap)
    return worst


def check_one_star_unsaturated() -> int:
    worst = 0
    for a in (3, 4):
        min_ei = 5 - a
        for e0, ei, ej, ek in product(range(4), repeat=4):
            if e0 + ei + ej + ek != 3 or ei < min_ei:
                continue
            # A star-only unsaturated K5 component has n_i <= 7;
            # the other two are U-part-saturated and have n <= 4+E.
            total_cap = c3_cap(e0) + 7 + (4 + ej) + (4 + ek)
            worst = max(worst, total_cap)
            assert total_cap < 29, (a, e0, ei, ej, ek, total_cap)
    return worst


def check_mixed_unsaturated() -> int:
    # The exceptional P1-P2 mixed transversal pattern forces E_i=3;
    # all other W excesses are zero.
    total_cap = 10 + 7 + 4 + 4
    assert total_cap == 25 and total_cap < 29
    return total_cap


def main():
    a = check_all_saturated()
    b = check_one_star_unsaturated()
    c = check_mixed_unsaturated()
    print("PASS: all-saturated capacity maximum =", a, "< 29")
    print("PASS: one star-unsaturated component maximum =", b, "< 29")
    print("PASS: exceptional mixed pattern capacity =", c, "< 29")
    print("Scope: arithmetic replay only; the k>=2 contradiction is structural.")


if __name__ == "__main__":
    main()
