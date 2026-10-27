#!/usr/bin/env python3
"""Arithmetic regression for Q32_EXACT_COLOR_COUNT_COLLAPSE.md.

This checks only the exact integer/Turan values and local degree-budget
arithmetic. It does not replace the analytic graph-theoretic proof or certify
the external Brouwer/Kang--Pikhurko theorem.
"""
from math import comb


def p_r(n: int, r: int) -> int:
    q, rem = divmod(n, r)
    return rem * comb(q + 1, 2) + (r - rem) * comb(q, 2)


def main() -> None:
    # Complement-form Brouwer lower bounds used in the proof.
    assert p_r(58, 11) == 125
    assert p_r(58, 11) + 58 // 11 - 1 == 129
    assert p_r(57, 11) == 120
    assert p_r(57, 11) + 57 // 11 - 1 == 124
    assert p_r(53, 10) == 115
    assert p_r(53, 10) + 53 // 10 - 1 == 119
    assert p_r(49, 8) == 126

    # 130-edge color: one degree-3 point forces an isolated K4;
    # two isolated K4s leave 53 vertices and only 118 edges <119.
    assert 130 - 2 * comb(4, 2) == 118
    assert 118 < 119

    # 132-edge color: degree-2 points lie in isolated triangles;
    # four triangles leave 49 vertices and 120 edges < p_8(49)=126.
    assert 132 - 4 * comb(3, 2) == 120
    assert 120 < 126

    # m=10 exceptional-vertex budget.
    assert 60 - 13 - 9 - 9 * 4 == 2
    assert 10 > 9  # at most 9 degree-2 vertices in a 132-edge color

    # m=9: s=1 and s=2 colors must both have degree 3 at all 9 exceptions.
    assert 60 - 13 - 9 - 8 * 4 == 6
    assert 3 + 3 == 6
    assert 9 > 4  # 130-edge color has at most four degree-3 vertices

    # m=8: three s=1 colors; at least two degree-3 incidences per exception.
    assert 60 - 13 - 9 - 7 * 4 == 10
    assert 3 + 4 + 4 == 11 > 10
    assert 2 * 8 == 16
    assert 3 * 4 == 12
    assert 16 > 12

    print("Q32_EXACT_COLOR_COUNT_COLLAPSE_ARITHMETIC_OK")


if __name__ == "__main__":
    main()
