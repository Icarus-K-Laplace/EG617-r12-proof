#!/usr/bin/env python3
"""Independent finite audit for DELTA12_DEPTH2_EPS2_TERMINAL_CLOSURE.md.

This checks only the final binary K5/K6 label incompatibility after the
analytic terminal reduction. It does not verify the 308-edge saturated-kernel
classification, the unique W-terminal reduction, or the graph-theoretic pair
rule.
"""

from itertools import product


def feasible(exception_side=None):
    """Return a binary label assignment if one survives the final constraints.

    exception_side is None, 'A', or 'B'. An exception represents the unique
    possible vertex that is partner to both restored J-endpoints when the two
    restored edges share their A/B-side endpoint.
    """
    n_a = 7 - (1 if exception_side == "A" else 0)
    n_b = 7 - (1 if exception_side == "B" else 0)

    for labels_a in product((5, 6), repeat=n_a):
        # A K7 plus K5 gives K12 if all seven A-points carry label 5.
        # Six A-points plus K6 already give K12.
        if labels_a.count(5) >= 7 or labels_a.count(6) >= 6:
            continue

        for labels_b in product((5, 6), repeat=n_b):
            if labels_b.count(5) >= 7 or labels_b.count(6) >= 6:
                continue

            # Every constrained A-B pair is nonadjacent in H. The pair rule
            # proved analytically forces opposite K5/K6 labels.
            if all(a != b for a in labels_a for b in labels_b):
                return labels_a, labels_b

    return None


def main():
    # Arithmetic behind the analytic label-forcing step.
    assert 3 + 4 > 6      # one <=6-neighbour vertex cannot cover K3 and K4
    assert 5 + 6 > 6      # it cannot be complete to both K5 and K6
    assert 2 < 3          # two label-5 vertices have <=2 outside-K5 slots

    # Distinct restored A/B endpoints: all 14 vertices are constrained.
    assert feasible(None) is None

    # Shared restored endpoint: one exceptional point can lie on either K7.
    assert feasible("A") is None
    assert feasible("B") is None

    print("DELTA12_DEPTH2_EPS2_TERMINAL_CLOSURE_OK")
    print("Scope: final binary label audit only; parent analytic reductions are external inputs.")


if __name__ == "__main__":
    main()
