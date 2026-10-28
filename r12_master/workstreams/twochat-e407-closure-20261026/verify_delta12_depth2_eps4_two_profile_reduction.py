#!/usr/bin/env python3
"""Arithmetic audit for DELTA12_DEPTH2_EPS4_TWO_PROFILE_REDUCTION.md.

Checks only the finite endpoint-profile deletion and the local x-cost arithmetic
used after the analytic pair-rule proof. It does not verify the registered
308-edge kernel classification or the graph-theoretic pair-rule argument.
"""

START = {
    (0, 3, 0, 1),
    (0, 3, 1, 0),
    (0, 4, 0, 0),
    (1, 4, 0, 0),
}
CLOSED = {
    (0, 3, 0, 1),
    (0, 3, 1, 0),
}
EXPECTED = {
    (0, 4, 0, 0),
    (1, 4, 0, 0),
}


def main():
    assert START - CLOSED == EXPECTED

    # Local lemma: when d_W(d0)=5 and d_W(c*)=3, write
    # x=|N(d0) cap K4^P|. The two K4+K5 alternatives for a degree<=6
    # A/B point cost 5+x or 10-x neighbours. Hence only x=1 or x=4.
    feasible_x = []
    for x in range(1, 5):
        if 5 + x <= 6 or 10 - x <= 6:
            feasible_x.append(x)
    assert feasible_x == [1, 4]

    # In the final two-partner subcase of (0,3,1,0), each partner contains
    # the same forced 3-set and has only two further neighbours. Their union
    # has common3 + at most four extras. Completing one K4 consumes at least
    # one of those extras, leaving <=3, insufficient for a second K4/K5.
    assert 3 < 4

    print("DELTA12_DEPTH2_EPS4_TWO_PROFILE_REDUCTION_OK")
    print("remaining aggregate profiles:", sorted(EXPECTED))
    print("Scope: finite arithmetic only; analytic graph reductions are inputs.")


if __name__ == "__main__":
    main()
