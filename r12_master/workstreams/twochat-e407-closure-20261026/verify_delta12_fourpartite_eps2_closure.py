#!/usr/bin/env python3
"""Relaxed finite audit for DELTA12_FOURPARTITE_EPS2_CLOSURE.md.

The verifier intentionally relaxes the actual W-cross-edge placement.  For a
low-omission epsilon_r=0 point, all full T-label occurrences in two different
W-components would require their cross pairs to be actual W-edges (the
analytic proof gets this from the support common-neighbour capacity).  Here we
only require that the *number* of such same-label cross pairs is at most the
total available W-cross-edge count q_W, and allow those edges to be placed
wherever desired.  Thus UNSAT in this relaxation is stronger than checking a
particular cross-edge placement.

The exceptional five-point partial label is also relaxed maximally: when it is
possible (h=2 and a degree-two W vertex carries both W-excess units), the one
partial vertex is omitted from all cross-label conflict counts.

This script does NOT re-prove the support-transversal gap lemma, the W-pair
capacity theorem, or the W-profile classification.
"""

from itertools import product


def compositions(n, k, cap):
    if k == 1:
        if n <= cap:
            yield (n,)
        return
    for x in range(min(n, cap) + 1):
        for tail in compositions(n - x, k - 1, cap):
            yield (x,) + tail


def relaxed_no_full_feasible(sizes, q_cross, h, partial_component=None):
    """Return a relaxed no-full-component label state, or None.

    r has epsilon_r=0, hence d_W(r)=5-h.  Every component must contain an
    r-nonneighbour.  Full-labelled nonneighbours are distributed among three
    T-labels, with at most four per W clique (K12 cap).  The total number of
    same-full-label cross-component pairs must fit into q_cross physical
    W-cross edges.  A single optional partial vertex is exempted completely.
    """
    d = 5 - h
    m = len(sizes)
    for neigh in product(*[range(s + 1) for s in sizes]):
        if sum(neigh) != d:
            continue
        non = [s - a for s, a in zip(sizes, neigh)]
        if any(x == 0 for x in non):
            continue

        partial = [0] * m
        if partial_component is not None:
            if non[partial_component] == 0:
                continue
            partial[partial_component] = 1
        full = [non[j] - partial[j] for j in range(m)]

        choices = [list(compositions(full[j], 3, 4)) for j in range(m)]
        for rows in product(*choices):
            required_cross_pairs = 0
            for colour in range(3):
                for a in range(m):
                    for b in range(a + 1, m):
                        required_cross_pairs += rows[a][colour] * rows[b][colour]
            if required_cross_pairs <= q_cross:
                return neigh, rows, required_cross_pairs
    return None


def main():
    # Three profiles with physical W-cross edges.  The (3,5,5,5) profile can
    # have the unique five-point partial exception only in the K3 component
    # and only when h=2.  The other two profiles have no W-internal degree-two
    # vertex, hence no partial exception.
    profiles = [
        ((3, 5, 5, 5), 1, 0),
        ((4, 4, 4, 6), 1, None),
        ((4, 4, 5, 5), 2, None),
    ]
    for sizes, q_cross, partial_comp in profiles:
        for h in (0, 1, 2):
            pc = partial_comp if h == 2 else None
            state = relaxed_no_full_feasible(sizes, q_cross, h, pc)
            assert state is None, (sizes, q_cross, h, state)

    # Global endgame: at least six of eight omission weights are <=2.
    # With only two U-excess units, at least four are epsilon-zero and the
    # analytic local theorem gives h=0 on them.  Five such points would leave
    # at most 3*(baseline 2) + 2 excess = 8 target leave edges, below 9.
    assert 3 * 2 + 2 == 8 < 9

    # Hence exactly four h=0 epsilon-zero low-omission points remain.  All
    # other four points have h>0.  At most two of those can carry positive
    # epsilon, so at least two epsilon-zero active points must have q>=3; the
    # other two active points have q>=1.  This exceeds the omission budget 7.
    assert 3 + 3 + 1 + 1 == 8 > 7

    print("DELTA12_FOURPARTITE_EPS2_RELAXED_AUDIT_OK")
    print("cross-edge profiles UNSAT even with arbitrary placement relaxation")
    print("global omission/target-incidence endgame: 8 > 7")
    print("Scope: finite label/count audit only; analytic support lemmas are inputs.")


if __name__ == "__main__":
    main()
