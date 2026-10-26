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

    # Independent-four-set rigidity: e(W) in {32,33,34}, so Caro-Wei
    # forces alpha(H[W]) >= 4; every independent 4-set covers U with 32
    # incidences over 31 vertices, leaving exactly one repeated incidence.
    assert {34 - eps_u // 2 for eps_u in (0, 2, 4)} == {32, 33, 34}
    assert all(256 / (2 * e_w + 16) > 3 for e_w in (32, 33, 34))
    assert 4 * 8 - 31 == 1

    # Cross-pair rigidity: for a duplicated U-vertex u in an independent
    # four-set, each color omitting u contributes 7 distinct P x Q pairs;
    # each other color contributes 6. There are only 49 possible pairs.
    pair_counts = {rho: 7 * rho + 6 * (8 - rho) for rho in range(9)}
    assert pair_counts == {rho: 48 + rho for rho in range(9)}
    assert pair_counts[0] == 48 and 49 - pair_counts[0] == 1
    assert pair_counts[1] == 49 and 49 - pair_counts[1] == 0
    assert all(pair_counts[rho] > 49 for rho in range(2, 9))
    # The two non-duplicated rows hit every witness block exactly once.
    assert 8 * 7 == 56
    # Their tau values are 8, and the duplicated pair has tau-sum 8+rho_u.
    assert 8 + 8 + 8 == 24
    assert all(8 + rho <= 9 for rho in (0, 1))  # duplicated-pair tau sum <= 9

    # Vertexwise deficit identities for P x Q pair graph B.
    # rho_u=1: B=K7,7, all degrees 7, so rho_p+s_p=1 at every vertex.
    assert 7 * 7 == 49
    assert all(8 - 1 == 7 for _ in range(14))
    assert 14 * 1 == 7 + 7  # total omissions in P,Q equal total star partners
    # rho_u=0: B=K7,7 minus one edge, with 12 degree-7 vertices and
    # two degree-6 endpoints; their deficits are twelve 1s and two 2s.
    assert 49 - 1 == 48
    deficits = [1] * 12 + [2, 2]
    assert sum(deficits) == 16
    assert deficits.count(2) == 2 and deficits.count(1) == 12

    # High-omission degree table. For S0=14, g_u=j_u+epsilon_u
    # is at most delta+epsilon_U = 7,8,9 in the three boundary cases.
    degree_caps = {
        (0, 7): {2: 7, 3: 4, 4: 1},
        (2, 6): {2: 8, 3: 5, 4: 2},
        (4, 5): {2: 9, 3: 6, 4: 3, 5: 0},
    }
    for (eps_u, delta), caps in degree_caps.items():
        gmax = eps_u + delta
        for rho, cap in caps.items():
            assert 6 - 3 * rho + gmax == cap
    assert 6 - 3 * 5 + 7 < 0
    assert 6 - 3 * 5 + 8 < 0
    assert 6 - 3 * 6 + 9 < 0
    # rho=5 is possible only at (epsilon_U,delta)=(4,5), with
    # epsilon_u=4 and j_u=5, so d_H(u,W)=0.
    assert 6 - 3 * 5 + 9 == 0
    assert 4 + 5 == 9

    # All-q=8 terminal: total omission count and degree ledger.
    assert 8 * 31 - 56 * 4 == 24
    for eps_u, delta in feasible:
        assert eps_u + 2 * delta == 14
        assert 6 * 31 - 3 * 24 + 2 * delta + eps_u == 128

    print("E408_Q33_S0_14_NO_SEVEN_TRANSVERSAL_ARITHMETIC_OK")
    print("30 integer inequality states, three excess/delta pairs, omission/degree identities, independent-four-set rigidity, rho<=1 cross-pair counts, vertexwise pair-deficit identities, and high-rho degree caps checked.")
    print("Scope: arithmetic checks only; analytic clique/independence arguments remain in the theorem note.")


if __name__ == "__main__":
    main()
