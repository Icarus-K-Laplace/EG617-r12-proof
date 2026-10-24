#!/usr/bin/env python3
"""Exact arithmetic regression checks for R12_TRANSVERSAL_BOUNDARY_CLASSIFICATION.

This verifies the integer edge/excess windows and pigeonhole thresholds only.
It is not a graph realization or terminal-exclusion certificate.
"""
from math import comb


def p_k(n: int, k: int) -> int:
    q, r = divmod(n, k)
    sizes = [q + 1] * r + [q] * (k - r)
    return sum(comb(s, 2) for s in sizes)


def check_e407() -> None:
    assert p_k(18, 4) == 32
    # The boundary equations imply e(A,H)=124+2*delta+eps_U.
    # Since 18 outside vertices each have >=7 cross-neighbours, this is >=126.
    for delta in (0, 1):
        for eps_u in range(5):
            e_cross = 124 + 2 * delta + eps_u
            if e_cross < 126:
                # The seven-neighbour floor already excludes this profile.
                continue
            n7_lower = 20 - 2 * delta - eps_u
            assert n7_lower >= 14
            # Distinct 7-transversals are disjoint; the 3-transversal case
            # is excluded by the omitted-vertex count. For delta <= 1,
            # each remaining transversal supports at most six degree-7 W vertices.
            assert n7_lower > 2 * 6
    print("E407: delta <= 1 impossible; hence delta >= 2")


def check_e408_q33() -> None:
    assert p_k(16, 4) == 24
    assert p_k(24, 2) == 132
    # The core edge/excess ledger gives delta + eps_U <= 17.
    for delta in range(18):
        for eps_u in range(5):
            if delta + eps_u > 17:
                continue
            e_cross = 114 + 2 * delta + eps_u
            e_w = 41 - delta - eps_u
            assert e_w >= 24
            assert e_cross >= 112
            n7_lower = 14 - 2 * delta - eps_u
            if 2 * delta + eps_u <= 7:
                assert delta <= 3
                assert n7_lower >= 7
                # In this range, the proof classifies any 7-transversal as
                # a component; k=3 and k=2 are impossible, while k=1
                # supports at most six degree-7 W vertices.
                assert n7_lower > 6
    # The three-component branch would require delta=21, outside delta<=17.
    assert 21 > 17
    # The two-component branch asks for 56 distinct pairs from a 7x7 grid.
    assert 8 * 7 > 7 * 7
    print("E408 Q33: 2*delta + eps_U <= 7 impossible; hence >= 8")


def main() -> None:
    check_e407()
    check_e408_q33()
    print("TRANSVERSAL_BOUNDARY_CLASSIFICATION_AUDIT_OK")


if __name__ == "__main__":
    main()
