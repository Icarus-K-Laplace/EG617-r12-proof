#!/usr/bin/env python3
"""Arithmetic checks for the S0=14 seven-point-transversal exclusion.

This verifies the finite integer inequalities and omission-count identities in
R12_E408_Q33_S0_14_NO_SEVEN_TRANSVERSAL.md. It is not a graph-realization
certificate and does not replace the analytic clique/independence proof.
"""


def main():
    # S0 = epsilon_U + 2 delta, with total core excess 4.
    feasible = [(eps_u, (14 - eps_u) // 2)
                for eps_u in (0, 2, 4)
                if (14 - eps_u) % 2 == 0]
    assert feasible == [(0, 7), (2, 6), (4, 5)]

    # Under k>=1, sum of high-degree increments d_y is exactly k.
    # With s=k+a<=4 and B=7h+B_low, B_low<=k, the T-incidence
    # equation forces 7h+k >= 7(6-s). Check the integer consequence h>=6-s.
    checked = 0
    for k in range(1, 5):
        for s in range(k, 5):
            for h in range(0, k + 1):
                if 7 * h + k >= 7 * (6 - s):
                    assert h >= 6 - s
                    assert 7 + s + h >= 13
                checked += 1
    assert checked == 30

    # Any two b=7 high vertices have total R-neighborhood size at most k+2<=6;
    # likewise for one such vertex and one T-type point. Eight triples leave
    # at least two untouched, forcing adjacency by alpha(H)<=4.
    assert max(k + 2 for k in range(1, 5)) == 6
    assert min(8 - (k + 2) for k in range(1, 5)) == 2

    # If a seven-point transversal exists but k=0, the R-only multiplicity cap
    # is 4, there are at most three distinct transversals, and a<=4 by omega.
    # Therefore m=16-a<=12 and m>=12, forcing a=4 and three groups of size 4.
    assert 16 - 4 == 12
    assert 16 - 3 > 12
    assert 3 * 4 == 12
    assert 7 + 4 == 11
    assert 8 + 4 == 12

    # All-q=8 terminal: total omission count and degree ledger.
    assert 8 * 31 - 56 * 4 == 24
    for eps_u, delta in feasible:
        assert eps_u + 2 * delta == 14
        assert 6 * 31 - 3 * 24 + 2 * delta + eps_u == 128

    print("E408_Q33_S0_14_NO_SEVEN_TRANSVERSAL_ARITHMETIC_OK")
    print("30 integer inequality states, three excess/delta pairs, and omission/degree identities checked.")
    print("Scope: arithmetic checks only; analytic clique/independence arguments remain in the theorem note.")


if __name__ == "__main__":
    main()
