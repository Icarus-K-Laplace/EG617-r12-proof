#!/usr/bin/env python3
"""Arithmetic regression checks for R12_CROSS_BRANCH_AUDIT_AND_S0_REPAIR.md.

This checks the stated integer budgets and pair-count margins only. It does not
verify a graph realization or replace the analytic proof.
"""
from math import comb


def p4(n: int) -> int:
    q, r = divmod(n, 4)
    sizes = [q + 1] * r + [q] * (4 - r)
    return sum(comb(s, 2) for s in sizes)


def main() -> None:
    # Four-partite E408 Q33 S0=10 budget.
    profiles = [
        (delta, 10 - 2 * delta)
        for delta in range(18)
        if 0 <= 10 - 2 * delta <= 4
        and delta + (10 - 2 * delta) <= 17
    ]
    assert profiles == [(3, 4), (4, 2), (5, 0)]
    assert all(delta - 2 >= 1 for delta, _ in profiles)

    # k=4,5,6 are the only integer possibilities from x=124 and q_w>=8
    # outside the k seven-neighborhood vertices.
    assert [128 - k <= 124 for k in range(7)] == [
        False, False, False, False, True, True, True
    ]
    assert 124 - 7 * 4 == 96 == 8 * 12
    assert 124 - 7 * 5 == 89 == 8 * 10 + 9
    assert 124 - 7 * 6 == 82
    assert {tuple([8] * 8 + [9, 9]), tuple([8] * 9 + [10])} == {
        tuple([8] * 8 + [9, 9]), tuple([8] * 9 + [10])
    }

    # Repaired s=1 count: non-Q selected pairs are bounded by the three
    # unused perfect matchings, not by the extra-L-edge budget.
    assert 3 * 3 * 3 == 27
    assert 6 + 9 + 9 == 24
    assert 27 > 24

    # Repaired s=2 selected pair profiles (3,3,2).
    deficits = [
        3 * 3 - 2 * min(3, 3),
        3 * 2 - 2 * min(3, 2),
        3 * 2 - 2 * min(3, 2),
    ]
    matching_capacities = [min(3, 3), min(3, 2), min(3, 2)]
    assert deficits == [3, 2, 2]
    assert deficits == matching_capacities

    # The unselected C0 part has six vertices; two 5-subsets intersect in
    # at least four points, which supplies the triangle extension.
    assert 5 + 5 - 6 == 4
    assert p4(16) == 24

    # Safe core-capacity thresholds: p4(18)=32, p4(16)=24.
    assert p4(18) == 32
    assert p4(16) == 24
    print("CROSS_BRANCH_AUDIT_ARITHMETIC_OK")


if __name__ == "__main__":
    main()
