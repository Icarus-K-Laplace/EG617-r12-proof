#!/usr/bin/env python3
"""Arithmetic verifier for Q32_V44_EXCEPTIONAL_DEGREE_CLOSURE.md."""
from math import comb


def p_r(n, r):
    q, rem = divmod(n, r)
    sizes = [q + 1] * rem + [q] * (r - rem)
    return sum(comb(s, 2) for s in sizes)


def min_degree_for_residual_edges(e):
    for d in range(61):
        if p_r(60 - d, 11) <= e - d:
            return d
    raise AssertionError


def main():
    assert p_r(60, 11) == 135
    assert p_r(59, 11) == 130
    assert p_r(58, 11) == 125

    assert min_degree_for_residual_edges(130) == 2
    assert min_degree_for_residual_edges(131) == 1
    assert min_degree_for_residual_edges(132) == 1

    nonexact_floor = {8: 6, 9: 3, 10: 1}
    for m in (8, 9, 10):
        room = 60 - 13 - 4 * m - nonexact_floor[m]
        nmax = room // 5
        assert nmax == 1, (m, room, nmax)
        assert 3 * nmax < m - 3

    print("PASS: Q32 v=44 exceptional-degree capacity")
    print("p_11(60), p_11(59), p_11(58) = 135,130,125")
    print("minimum degrees for residual edge counts 130,131,132 = 2,1,1")
    for m in (8, 9, 10):
        print(f"m={m}: nonexact degree floor={nonexact_floor[m]}, exceptional multiplicity per W vertex <=1")
    print("three W vertices can host <=3 exceptional exact colors, but v=44 normal form needs >=m-3>=5")


if __name__ == "__main__":
    main()
