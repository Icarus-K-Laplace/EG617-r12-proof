#!/usr/bin/env python3
"""Arithmetic audit for the E407 W-side support-block transversal theorem.

This checks integer consequences of the frozen ledger. It does not verify
existence of the support design or construct a graph realization.
"""

def feasible_profiles():
    return [
        (delta, eps)
        for delta in range(3, 17)
        for eps in range(5)
        if delta + eps <= 16 and eps + 2 * delta >= 9
    ]


def main():
    profiles = feasible_profiles()
    assert len(profiles) == 56
    for delta, eps_u in profiles:
        sigma = eps_u + 2 * delta
        y_total = sigma - 2
        assert sigma >= 9
        assert y_total >= 7
        # Every W vertex has d_U >= 7, and the total excess over 7 is y_total.
        assert 126 + y_total == 124 + eps_u + 2 * delta

    minimum_slack = [
        (delta, eps)
        for delta, eps in profiles
        if eps + 2 * delta == 9
    ]
    assert minimum_slack == [(3, 3), (4, 1)]
    for delta, eps_u in minimum_slack:
        y_total = eps_u + 2 * delta - 2
        assert y_total == 7
        # Positive y values are positive integers, so their count is at most
        # y_total. This gives a lower bound on the number of zero-slack vertices.
        positive_count_max = min(18, y_total)
        zero_count_min = 18 - positive_count_max
        assert zero_count_min >= 11

    # In a y=0 neighborhood, seven points must account for all 49 blocks:
    # each point occurs in at most seven blocks and every block is hit.
    assert 7 * 7 == 49
    # A y=1 independent W-quadruple has U-degree sum 4*7+1=29,
    # exactly one edge per U point, so its four neighborhoods partition U.
    assert 4 * 7 + 1 == 29
    assert 7 + 7 + 7 + 8 == 29
    # Nonadjacent W-pair capacity: 49 blocks require >=2 incidences each;
    # m_u<=7 implies union size >=14. Therefore intersection <= y+y'.
    assert 2 * 49 <= 7 * 14

    print("E407_SUPPORT_BLOCK_W_TRANSVERSAL_ARITHMETIC_OK")
    print(f"feasible (delta, epsilon_U) profiles: {len(profiles)}")
    print(f"minimum-slack profiles: {minimum_slack}")
    print("minimum total W-side slack: 7; hence at least 11 zero-slack W vertices")
    print("Scope: arithmetic only; no graph-realization certificate.")


if __name__ == "__main__":
    main()
