#!/usr/bin/env python3
"""Arithmetic audit for DELTA12_DEPTH2_EPS3_Q1_CLOSURE.md.

Checks the one-defect escape threshold, endpoint/excess rigidity, the local x
cases, and the final binary-label obstruction. It does not verify the
registered depth-2 kernel classification or the analytic graph pair rule.
"""

from itertools import product


def defect_threshold():
    # W base component sizes 4,4,5,5 with one cross edge. An alpha<=2 common
    # nonneighbour set meeting three components may contain only the two cross
    # endpoints in their components, plus one further component. Its maximum
    # size is 1+1+5=7, so the neighbourhood union has size at least 11.
    assert 18 - (1 + 1 + 5) == 11


def endpoint_rigidity():
    survivors = []
    for t0 in range(3):
        TC = 2 - t0
        for eps0 in range(4):
            for EC in range(4 - eps0):
                Erest = 3 - eps0 - EC
                if Erest < 0:
                    continue
                if 2 + eps0 - t0 < 3:
                    continue
                pair_sum = 4 * (2 + eps0 - t0) + (16 + EC - TC)
                if pair_sum >= 32:
                    survivors.append((t0, eps0, EC, Erest))
    assert survivors == [(0, 3, 0, 0)]


def local_x_cases():
    # N(d0) has 5 points in the fixed two-K4 union and N(ci) is the
    # complementary 3-set. For a degree<=6 vertex paired with ci:
    # - covering the same two K4s is invalid because then the d0-pair union
    #   has size <=6;
    # - covering first K4+K5 costs 4+x? In the chosen convention it leaves
    #   x missing points and costs 5+x, so x<=1;
    # - the symmetric branch requires x>=4.
    feasible = []
    for x in range(1, 5):
        left_cost = 5 + x
        right_cost = 10 - x
        if left_cost <= 6 or right_cost <= 6:
            feasible.append(x)
    assert feasible == [1, 4]


def binary_labels(exception_side=None):
    na = 7 - (1 if exception_side == "A" else 0)
    nb = 7 - (1 if exception_side == "B" else 0)
    for A in product((0, 1), repeat=na):
        for B in product((0, 1), repeat=nb):
            if all(a != b for a in A for b in B):
                # A side or B side has seven constrained vertices because
                # there is at most one exception. Opposite labels make that
                # full side uniform, producing K7+K5=K12.
                if na == 7 and len(set(A)) == 1:
                    continue
                if nb == 7 and len(set(B)) == 1:
                    continue
                return True
    return False


def main():
    defect_threshold()
    endpoint_rigidity()
    local_x_cases()
    assert not binary_labels(None)
    assert not binary_labels("A")
    assert not binary_labels("B")
    print("DELTA12_DEPTH2_EPS3_Q1_CLOSURE_OK")
    print("Scope: finite arithmetic only; parent graph reductions are inputs.")


if __name__ == "__main__":
    main()
