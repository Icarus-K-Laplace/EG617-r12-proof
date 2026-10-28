#!/usr/bin/env python3
"""Finite arithmetic audit for the depth-3 epsilon_U=3,4 terminal proofs.

This checks the label-count inequalities and restored-edge incidence budgets.
The registered 309-edge equality model, component/pair lemmas, and W-profile
classification are mathematical inputs and are not re-proved by this script.
"""


def same_binary_cross(a, b):
    """Same-label pairs between 7-side with a A labels and 6-side with b A labels."""
    return a*b + (7-a)*(6-b)


def main():
    # Any genuinely mixed 7-side against an arbitrary 6-side has >=6 same-label pairs.
    for a in range(1, 7):
        floor = min(same_binary_cross(a, b) for b in range(7))
        assert floor >= 6, (a, floor)

    # epsilon=3 nonrestored all-C survivor: only 3 restored edges available.
    assert min(min(same_binary_cross(a,b) for b in range(7)) for a in range(1,7)) == 6
    assert 6 > 3

    # epsilon=4 degree-sum-8 with one exceptional restored edge leaves only two edges.
    assert 6 > 2

    # epsilon=4 AC/all-B branch: three restored edges -> six endpoint incidences.
    # Only A-labelled R vertices can carry those incidences, at most one each,
    # so at least three A labels occur on each side; all A-A cross pairs need restoration.
    assert 3*3 == 9
    assert 9 > 3

    # Restored xy branch: each exceptional vertex must contain a W component of size >=4.
    assert 4+4 == 8
    assert 7 < 8

    print("DELTA12_DEPTH3_EPS3_EPS4_TERMINAL_ARITHMETIC_OK")
    print("mixed 7x6 binary same-label floors:",
          {a:min(same_binary_cross(a,b) for b in range(7)) for a in range(1,7)})
    print("Scope: arithmetic only; equality-model and graph pair rules are proof inputs.")


if __name__ == "__main__":
    main()
