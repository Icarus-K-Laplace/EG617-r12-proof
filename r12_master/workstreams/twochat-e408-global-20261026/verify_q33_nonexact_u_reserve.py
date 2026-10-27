#!/usr/bin/env python3
"""Arithmetic verifier for Q33_NONEXACT_U_RESERVE_CLOSURE.md.

This verifies the Turan floor and the final capacity inequalities only.
Graph-theoretic ownership and witness-label hypotheses remain explicit theorem
inputs.
"""
from math import comb


def turan_edges(n, r):
    q, rem = divmod(n, r)
    sizes = [q + 1] * rem + [q] * (r - rem)
    internal = sum(comb(s, 2) for s in sizes)
    return comb(n, 2) - internal, tuple(sorted(sizes, reverse=True))


def main():
    t, sizes = turan_edges(31, 12)
    p = comb(31, 2) - t
    assert sizes == (3,) * 7 + (2,) * 5
    assert p == 26

    delta_max = 17
    h_preliminary_max = 4
    remaining_capacity = delta_max + 6 * h_preliminary_max
    assert remaining_capacity == 41

    # m=10 was independently excluded by the exact-color component-capacity theorem.
    for m in (8, 9):
        required = 26 * (11 - m)
        assert required > remaining_capacity, (m, required, remaining_capacity)

    assert 26 * 2 == 52
    assert 26 * 3 == 78

    print("PASS: Q33 nonexact U-reserve arithmetic")
    print("T_12(31) part sizes:", sizes)
    print("p_12(31) =", p)
    print("available nonexact U-edge capacity <= delta+6h <=", remaining_capacity)
    print("m=9 requires", 52, ">", remaining_capacity)
    print("m=8 requires", 78, ">", remaining_capacity)
    print("Conclusion under theorem inputs: no m in {8,9} survives after m=10 exclusion.")


if __name__ == "__main__":
    main()
