#!/usr/bin/env python3
"""Exact finite verifier for the P_C=49, r_i(C)=6 gadget contradiction.

No third-party packages are required.  The four gadgets are the exact
11-vertex normal forms from the retained exact-129 gadget theorem.  The
checker exhausts:
  * all K5/K4 cliques in each normal form;
  * all disjoint K5/K5 pairs for r=1 blocks;
  * all disjoint K5/K5 and K5/K4 complement pairs for an r=2 block;
  * all admissible disjoint clique-complement pairs for Case C at r=6.

A PASS means that for every such local configuration, a K5 core K and
high-row complement H can be selected so that the seven outer rows and K
form a monochromatic K12 with an external same-color edge.  The analytic
contradiction then uses the isolated-K12 lemma.
"""
from itertools import combinations


def make_gadget(b):
    vertices = tuple(range(11))
    A = set(range(5))
    B = set(range(5, 10))
    x = 10
    A0 = {0}
    B0 = set(range(5, 5 + b))
    adjacency = {v: set() for v in vertices}

    def add(u, v):
        adjacency[u].add(v)
        adjacency[v].add(u)

    for clique in (A, B):
        for u, v in combinations(sorted(clique), 2):
            add(u, v)
    for u in A - A0:
        add(x, u)
    for v in B - B0:
        add(x, v)
    for u in A0:
        for v in B0:
            add(u, v)
    return vertices, adjacency


def cliques(vertices, adjacency, size):
    if size == 0:
        return [frozenset()]
    return [
        frozenset(S)
        for S in combinations(vertices, size)
        if all(v in adjacency[u] for u, v in combinations(S, 2))
    ]


def disjoint_pairs(cliques_a, cliques_b=None):
    if cliques_b is None:
        cliques_b = cliques_a
        return [
            (X, Y)
            for i, X in enumerate(cliques_a)
            for Y in cliques_a[i + 1 :]
            if X.isdisjoint(Y)
        ]
    return [
        (X, Y)
        for X in cliques_a
        for Y in cliques_b
        if X.isdisjoint(Y)
    ]


def verify():
    summary = []
    for b in range(1, 5):
        vertices, adjacency = make_gadget(b)
        K5 = cliques(vertices, adjacency, 5)
        K4 = cliques(vertices, adjacency, 4)

        # Each r=1 block has one of these disjoint K5-pairs as its two
        # no-component-row complements.
        low_pairs = disjoint_pairs(K5)

        # A core K is good if every possible r=1 pair has a member L
        # disjoint from K.  The corresponding row neighborhood V(U)\\L
        # then contains K.
        good_cores = [
            K
            for K in K5
            if all(any(L.isdisjoint(K) for L in pair) for pair in low_pairs)
        ]
        assert good_cores

        # The r=2 block has complement profile (5,5) or (5,4).
        r2_pairs = disjoint_pairs(K5)
        r2_pairs += disjoint_pairs(K5, K4)

        # Case A/B at r=6: the no-component row has complement H=K5.
        ab_checks = 0
        for H in K5:
            for Q5, Q4 in r2_pairs:
                ab_checks += 1
                found = any(
                    H.isdisjoint(K)
                    and any(
                        Q.isdisjoint(K) and bool(H.intersection(Q))
                        for Q in (Q5, Q4)
                    )
                    for K in good_cores
                )
                assert found, (
                    "Case A/B failure",
                    b,
                    tuple(sorted(H)),
                    tuple(sorted(Q5)),
                    tuple(sorted(Q4)),
                )

        # Case C at r=6: complements H1,H2 are disjoint cliques,
        # each of size <=5, with |H1|+|H2| >=5.
        clique_by_size = {k: cliques(vertices, adjacency, k) for k in range(1, 6)}
        clique_by_size[0] = [frozenset()]
        high_pairs = []
        seen = set()
        for s in range(6):
            for t in range(s, 6):
                for H1 in clique_by_size[s]:
                    for H2 in clique_by_size[t]:
                        if H1.isdisjoint(H2) and s + t >= 5:
                            key = tuple(
                                sorted((tuple(sorted(H1)), tuple(sorted(H2))))
                            )
                            if key not in seen:
                                seen.add(key)
                                high_pairs.append((H1, H2))

        case_c_checks = 0
        for H1, H2 in high_pairs:
            for Q5, Q4 in r2_pairs:
                case_c_checks += 1
                found = any(
                    len(H) >= 2
                    and H.isdisjoint(K)
                    and any(
                        Q.isdisjoint(K) and bool(H.intersection(Q))
                        for Q in (Q5, Q4)
                    )
                    for H in (H1, H2)
                    for K in good_cores
                )
                assert found, (
                    "Case C failure",
                    b,
                    tuple(sorted(H1)),
                    tuple(sorted(H2)),
                    tuple(sorted(Q5)),
                    tuple(sorted(Q4)),
                )

        summary.append(
            (
                b,
                len(K5),
                len(K4),
                len(low_pairs),
                len(good_cores),
                len(high_pairs),
                len(r2_pairs),
                ab_checks,
                case_c_checks,
            )
        )

    print(
        "b | K5 | K4 | r1-pairs | good-cores | r6-C-pairs | r2-pairs "
        "| A/B checks | C checks"
    )
    for row in summary:
        print(" | ".join(str(x) for x in row))
    print("PASS: all exact gadget configurations satisfy the contradiction interface.")


if __name__ == "__main__":
    verify()
