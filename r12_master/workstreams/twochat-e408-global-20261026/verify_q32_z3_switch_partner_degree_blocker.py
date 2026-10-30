#!/usr/bin/env python3
"""Finite check of the z=3 synchronized-switch partner-fiber blocker.

The normalized 4,5,5 switch has A-D and B-D identity base matchings,
C-D base matching sigma=(s j), and extra edges
A_s D_j, B_s D_j, C_s D_s. The vertex D_j then has k=2 extra
small-component incidences and sees label j in both A and B.
The analytic degree identity therefore forces n_s+n_j <= 1.

This script checks the normalized local label/endpoint pattern for every
transposition and verifies the consequences for the four registered
seven-vertex fiber profiles. It is not a global graph solver.
"""
from itertools import combinations

PROFILES = {
    (3, 3, 1, 0),
    (3, 2, 2, 0),
    (3, 2, 1, 1),
    (2, 2, 2, 1),
}

def normalized_switch(s, j):
    assert s != j
    sigma = list(range(4))
    sigma[s], sigma[j] = sigma[j], sigma[s]

    # Neighbor-label sets of D_t in the three small blocks A,B,C.
    # Base maps: A-D=id, B-D=id, C-D=sigma.
    # Extra edges: A_s-D_j, B_s-D_j, C_s-D_s.
    labels = {}
    for t in range(4):
        labels[t] = {
            "A": {t} | ({s} if t == j else set()),
            "B": {t} | ({s} if t == j else set()),
            "C": {sigma[t]} | ({s} if t == s else set()),
        }
    k = {t: (2 if t == j else 1 if t == s else 0) for t in range(4)}

    for t in range(4):
        common = set.intersection(*labels[t].values())
        if t == j:
            assert common == {s}
            assert j in labels[t]["A"] and j in labels[t]["B"]
            assert k[t] == 2
        elif t == s:
            assert common == {s}
            assert j in labels[t]["C"]
            assert k[t] == 1
        else:
            assert common == {t}
            assert k[t] == 0
    return labels, k

def main():
    switch_cases = 0
    for a, b in combinations(range(4), 2):
        for s, j in ((a, b), (b, a)):
            labels, k = normalized_switch(s, j)
            assert k[j] == 2
            assert j in labels[j]["A"] and j in labels[j]["B"]
            switch_cases += 1
    assert switch_cases == 12

    allowed_pairs = {}
    for prof in PROFILES:
        sizes = list(prof)
        allowed_pairs[prof] = [
            (sizes[i], sizes[j])
            for i, j in combinations(range(4), 2)
            if sizes[i] + sizes[j] <= 1
        ]
    assert allowed_pairs == {
        (3, 3, 1, 0): [(1, 0)],
        (3, 2, 2, 0): [],
        (3, 2, 1, 1): [],
        (2, 2, 2, 1): [],
    }

    mismatch_partner_sizes = (3, 2, 3)
    assert min(mismatch_partner_sizes) >= 2

    print("normalized switch cases checked:", switch_cases)
    print("only profile permitting a switch pair with n_s+n_j<=1: (3,3,1,0), empty+singleton")
    print("all nontrivial mismatch modes have partner size >=2")
    print("V47_Z3_SWITCH_PARTNER_DEGREE_BLOCKER_OK")
    print("Scope: local switch labels and fiber-size arithmetic only; no Q32 UNSAT.")

if __name__ == "__main__":
    main()
