#!/usr/bin/env python3
"""Exact finite verifier for the P_C=49, r_i(C)=6 gadget contradiction.

No third-party packages are required. The four gadgets are the exact 11-vertex
normal forms from the retained exact-129 gadget theorem. The checker exhausts:
  * all K4/K5 cliques in each normal form;
  * all disjoint K5/K5 pairs for r=1 blocks;
  * all disjoint K5/K5 and K5/K4 pairs for the r=2 block;
  * all admissible disjoint clique-complement pairs for r=6 Case C.

The final check uses the correct external-star condition: a monochromatic K12
may have one external edge of its color. The verifier therefore requires a
selected external gadget vertex to have at least TWO edges of color C into the
constructed K12 (one to the high-block row and one to the core, r=2 row, or a
selected r=1 row). That violates the 11-other-colors/12-edge star count.
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
        return [
            (X, Y)
            for i, X in enumerate(cliques_a)
            for Y in cliques_a[i + 1 :]
            if X.isdisjoint(Y)
        ]
    return [(X, Y) for X in cliques_a for Y in cliques_b if X.isdisjoint(Y)]


def has_external_second_C_edge(H, D, Q_pair, low_pair_types, low_pairs,
                               vertices, adjacency):
    U = set(vertices)
    if not H.isdisjoint(D):
        return False

    # For every low-block pair type that occurs, choose an omitted K5 L
    # disjoint from the common core D and intersecting the high complement H.
    eligible_by_type = {}
    for pair_type in low_pair_types:
        eligible = [
            L for L in low_pairs[pair_type]
            if L.isdisjoint(D) and H.intersection(L)
        ]
        if not eligible:
            return False
        eligible_by_type[pair_type] = eligible

    # Choose the omitted clique Q' for the r=2 row.
    for Q in Q_pair:
        if not Q.isdisjoint(D) or not H.intersection(Q):
            continue
        # The high-block row has C-edges to every z in this set, including at
        # least one vertex outside the core D.
        for z in U - set(D) - set(H):
            # If z also sees D in C, it has a second C-edge into the K12.
            if adjacency[z].intersection(D):
                return True
            # Otherwise, Q' omits z exactly when z is in Q. If not, the r=2
            # row supplies the second C-edge.
            if z not in Q:
                return True
            # Otherwise, choose a low-block row whose omitted K5 excludes z.
            # This gives z a C-edge to that row as well as to the high row.
            if any(
                z not in L
                for eligible in eligible_by_type.values()
                for L in eligible
            ):
                return True
    return False


def verify():
    summary = []
    for b in range(1, 5):
        vertices, adjacency = make_gadget(b)
        K5 = cliques(vertices, adjacency, 5)
        K4 = cliques(vertices, adjacency, 4)
        low_pairs = disjoint_pairs(K5)
        r2_pairs = disjoint_pairs(K5) + disjoint_pairs(K5, K4)
        pair_type_subsets = [
            {i for i in range(len(low_pairs)) if mask & (1 << i)}
            for mask in range(1, 1 << len(low_pairs))
        ]

        # Cases A/B: the selected high no-component row has a K5 complement H.
        ab_checks = 0
        for H in K5:
            for Q_pair in r2_pairs:
                for pair_types in pair_type_subsets:
                    ab_checks += 1
                    found = any(
                        has_external_second_C_edge(
                            H, D, Q_pair, pair_types, low_pairs,
                            vertices, adjacency
                        )
                        for D in K5
                    )
                    assert found, (
                        "Case A/B failure", b, tuple(sorted(H)),
                        tuple(tuple(sorted(Q)) for Q in Q_pair),
                        sorted(pair_types)
                    )

        # Case C: complements H1,H2 are disjoint cliques of sizes <=5 with
        # |H1|+|H2| >=5. The enumeration includes every such admissible pair.
        clique_by_size = {k: cliques(vertices, adjacency, k) for k in range(1, 6)}
        clique_by_size[0] = [frozenset()]
        high_pairs = []
        seen = set()
        for s in range(6):
            for t in range(s, 6):
                for H1 in clique_by_size[s]:
                    for H2 in clique_by_size[t]:
                        if H1.isdisjoint(H2) and s + t >= 5:
                            key = tuple(sorted((tuple(sorted(H1)), tuple(sorted(H2)))))
                            if key not in seen:
                                seen.add(key)
                                high_pairs.append((H1, H2))

        case_c_checks = 0
        for H1, H2 in high_pairs:
            for Q_pair in r2_pairs:
                for pair_types in pair_type_subsets:
                    case_c_checks += 1
                    found = any(
                        has_external_second_C_edge(
                            H, D, Q_pair, pair_types, low_pairs,
                            vertices, adjacency
                        )
                        for H in (H1, H2)
                        for D in K5
                    )
                    assert found, (
                        "Case C failure", b,
                        tuple(tuple(sorted(H)) for H in (H1, H2)),
                        tuple(tuple(sorted(Q)) for Q in Q_pair),
                        sorted(pair_types)
                    )

        summary.append((
            b, len(K5), len(K4), len(low_pairs), len(K5), len(high_pairs),
            len(r2_pairs), ab_checks, case_c_checks
        ))

    print("b | K5 | K4 | r1-pairs | K5 core candidates | Case-C pairs | r2-pairs | A/B checks | C checks")
    for row in summary:
        print(" | ".join(str(x) for x in row))
    print("PASS: every admissible local configuration yields a K12 with an outside vertex having at least two C-edges into it.")


if __name__ == "__main__":
    verify()
