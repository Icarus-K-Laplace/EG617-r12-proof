#!/usr/bin/env python3
"""Arithmetic-only audit for Lemma 14.4 (support-41 k=8 star terminal).

The analytical proof is in M10_SUPPORT41_OMISSION_FLOOR.md. This script checks
all nonnegative integer allocations of the four excess units between x and W,
and then among the three W-components A, B, {w}. It verifies that the set-cover
upper bound is <33 except for epsilon_x=0, epsilon_w=4, epsilon_A=epsilon_B=0;
in that exceptional equality case, |X_w|=15 but x has only 11 H-neighbors in N.
This is not a graph-realization search or a proof of the analytical set-cover
classification.
"""


def allocations(total):
    for ew in range(total + 1):
        for ea in range(total - ew + 1):
            eb = total - ew - ea
            yield ew, ea, eb


def verify():
    rows = []
    for eps_x in (0, 1):
        eps_w_total = 4 - eps_x
        for eps_w, eps_a, eps_b in allocations(eps_w_total):
            # |X_w| <= 11+eps_w; |X_BB| <= floor((22+eps_B)/2);
            # |X_7| <= 6. The unique degree-three W-neighborhood exists only
            # for eps_x=0 and contributes at most one X_AAA vertex.
            x_aaa = 1 if eps_x == 0 else 0
            upper = 11 + eps_w + (22 + eps_b) // 2 + 6 + x_aaa
            rows.append((eps_x, eps_w, eps_a, eps_b, upper))
            if eps_x == 1 or eps_w <= 3:
                assert upper < 33, (eps_x, eps_w, eps_a, eps_b, upper)
            else:
                assert (eps_x, eps_w, eps_a, eps_b, upper) == (0, 4, 0, 0, 33)
                # In the equality case all four covering sets are disjoint
                # and saturated; hence the degree-three vertex has S=A,
                # while every vertex in X_w has degree two into W.
                assert 11 + eps_x < 11 + eps_w  # d_H(x,N)=11 < |X_w|=15

    exceptional = [row for row in rows if row[-1] == 33]
    assert exceptional == [(0, 4, 0, 0, 33)], exceptional
    print(f"PASS: checked {len(rows)} integer excess allocations.")
    print("PASS: all but one allocation give a cover upper bound <33.")
    print("PASS: exceptional allocation has 15 vertices in X_w but only 11 x-neighbors.")
    print("Scope: arithmetic audit only; Lemma 14.4 supplies the graph-theoretic proof.")


if __name__ == "__main__":
    verify()
