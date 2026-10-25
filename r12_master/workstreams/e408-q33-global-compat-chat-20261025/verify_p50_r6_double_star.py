#!/usr/bin/env python3
"""Exact finite verifier for the P_C=50, r_i(C)=6 double-star corner.

The proof uses the valid star-capacity rule d_C(z,K12) <= 1 and checks for
one outside gadget vertex with at least two C-edges into the constructed K12.
It does not use the false claim that a monochromatic K12 is isolated.

This verifier checks the gadget alignment predicate only. The row-incidence
classification, exact-129 factor theorem, and seven-block contracts remain
explicit mathematical dependencies.
"""
from itertools import combinations

CASE_C_PROFILES = (
    (5, 5), (5, 4), (5, 3), (4, 4), (5, 2),
    (4, 3), (5, 1), (4, 2), (3, 3),
)


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
    return [
        frozenset(S)
        for S in combinations(vertices, size)
        if all(v in adjacency[u] for u, v in combinations(S, 2))
    ]


def disjoint_pairs(cliques_a):
    return [
        (X, Y)
        for i, X in enumerate(cliques_a)
        for Y in cliques_a[i + 1 :]
        if X.isdisjoint(Y)
    ]


def has_alignment_for_high_row(H, Q_pair, low_pair_types, low_pairs,
                               K5, vertices, adjacency):
    """Find D and an external z giving two C-edges into D plus selected rows."""
    U = set(vertices)
    for Q in Q_pair:
        if not H.intersection(Q):
            continue
        for D in K5:
            if not H.isdisjoint(D) or not Q.isdisjoint(D):
                continue

            eligible_by_type = {}
            possible = True
            for pair_type in low_pair_types:
                eligible = [
                    L for L in low_pairs[pair_type]
                    if L.isdisjoint(D) and H.intersection(L)
                ]
                if not eligible:
                    possible = False
                    break
                eligible_by_type[pair_type] = eligible
            if not possible:
                continue

            # H is the omitted gadget set of the high row, so every z outside
            # D union H is C-adjacent to that row. A second edge is supplied
            # by adjacency to D, or by being outside a selected low-row
            # omitted set Q or L.
            for z in U - set(D) - set(H):
                if adjacency[z].intersection(D):
                    return True
                if z not in Q:
                    return True
                if any(
                    z not in L
                    for eligible in eligible_by_type.values()
                    for L in eligible
                ):
                    return True
    return False


def verify():
    total_ab = 0
    total_case_c = 0
    summary = []

    for b in range(1, 5):
        vertices, adjacency = make_gadget(b)
        K5 = cliques(vertices, adjacency, 5)
        low_pairs = disjoint_pairs(K5)

        # One of the six r=1 blocks supplies Q_pair; the other five blocks
        # can realize any nonempty set of at most five distinct pair types.
        pair_type_subsets = [
            {i for i in range(len(low_pairs)) if mask & (1 << i)}
            for mask in range(1, 1 << len(low_pairs))
            if sum(1 for i in range(len(low_pairs)) if mask & (1 << i)) <= 5
        ]

        # Cases A/B: the high r=6 no-component row has a K5 complement H.
        ab_checks = 0
        for H in K5:
            for Q_pair in low_pairs:
                for types in pair_type_subsets:
                    ab_checks += 1
                    assert has_alignment_for_high_row(
                        H, Q_pair, types, low_pairs, K5, vertices, adjacency
                    ), ("Case A/B failure", b, tuple(sorted(H)), Q_pair, types)
        total_ab += ab_checks

        # Case C: enumerate every exact pair of disjoint complement cliques
        # from the registered size profiles.
        by_size = {k: cliques(vertices, adjacency, k) for k in range(1, 6)}
        high_pairs = []
        seen = set()
        for s, t in CASE_C_PROFILES:
            for H1 in by_size[s]:
                for H2 in by_size[t]:
                    if not H1.isdisjoint(H2):
                        continue
                    key = tuple(sorted((tuple(sorted(H1)), tuple(sorted(H2)))))
                    if key not in seen:
                        seen.add(key)
                        high_pairs.append((H1, H2, s, t))

        case_c_checks = 0
        for H1, H2, s, t in high_pairs:
            risky = (s + t >= 9)  # profiles (5,5) and (5,4)
            for Q_pair in low_pairs:
                for types in pair_type_subsets:
                    case_c_checks += 1
                    ok1 = has_alignment_for_high_row(
                        H1, Q_pair, types, low_pairs, K5, vertices, adjacency
                    )
                    ok2 = has_alignment_for_high_row(
                        H2, Q_pair, types, low_pairs, K5, vertices, adjacency
                    )
                    ok = (ok1 and ok2) if risky else (ok1 or ok2)
                    assert ok, (
                        "Case C failure", b, tuple(sorted(H1)), tuple(sorted(H2)),
                        s, t, Q_pair, types
                    )
        total_case_c += case_c_checks
        summary.append((
            b, len(K5), len(low_pairs), len(pair_type_subsets),
            len(high_pairs), ab_checks, case_c_checks
        ))

    print("b | K5 | r1-pairs | low-type subsets | Case-C pairs | A/B checks | C checks")
    for row in summary:
        print(" | ".join(str(x) for x in row))
    print(f"PASS: {total_ab} Case-A/B and {total_case_c} Case-C configurations.")
    print("Scope: exact gadget alignment only; upstream graph/row contracts are not machine-verified.")


if __name__ == "__main__":
    verify()
