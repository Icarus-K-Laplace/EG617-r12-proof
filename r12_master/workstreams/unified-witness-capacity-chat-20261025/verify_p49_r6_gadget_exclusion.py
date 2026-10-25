#!/usr/bin/env python3
"""Exact finite verifier for the P_C=49, r_i(C)=6 gadget alignment.

This is conditional on the exact-129 factor theorem, the seven-block row
contracts, and the four 11-vertex gadget normal forms. It does NOT use the
false claim that a monochromatic K12 has no external C-edge. Instead it
checks for an external vertex with at least two C-edges into the constructed
K12, which is forbidden by the 12-edge star count.

The component-incidence safety split is explicit:
  * Cases A/B: test every K5 omitted complement H individually. In Case B
    with five partial component incidences, one of the two no-component rows
    has at most two; testing every H guarantees the safe row is covered.
  * Case C: the exact complement-size profiles are listed from the row
    theorem. If |H1|+|H2| is 9 or 10, total partial component incidence is
    at most 4 or 5, so one high row has at most two; both H choices are tested.
    For smaller profiles, total partial component incidence is at most three,
    so either high row is safe and an existential alignment suffices.
  * The r=2 block contributes at most one partial component incidence.
Thus no pair of selected outer rows can cover a full isolated K5 component.

The checker enumerates all four gadget normal forms and all exact omitted-set
profiles, all disjoint r=1 K5/K5 pairs, all r=2 K5/K5 or K5/K4 pairs, every
nonempty subset of r=1 pair types present among five blocks, and every exact
r=6 Case-C complement pair. All graph tests are exact set operations.
"""
from itertools import combinations

# Exact Case-C complement-size profiles from the r_i=6 row theorem.
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


def disjoint_pairs(cliques_a, cliques_b=None):
    if cliques_b is None:
        return [
            (X, Y)
            for i, X in enumerate(cliques_a)
            for Y in cliques_a[i + 1 :]
            if X.isdisjoint(Y)
        ]
    return [(X, Y) for X in cliques_a for Y in cliques_b if X.isdisjoint(Y)]


def has_alignment_for_high_row(H, Q_pair, low_pair_types, low_pairs,
                               K5, vertices, adjacency):
    """Does this fixed high row H admit a safe K5 core and selected r=2 row?"""
    U = set(vertices)
    for Q in Q_pair:
        if not H.intersection(Q):
            continue
        for D in K5:
            if not H.isdisjoint(D) or not Q.isdisjoint(D):
                continue

            # Every low block pair type present among the five r=1 blocks
            # must provide an omitted K5 L disjoint from D and intersecting H.
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

            # H's row sees every z in U\\H. A double C-star is forced if some
            # such z outside D also sees D, the selected r=2 row, or an r=1 row.
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
    summary = []
    total_ab = 0
    total_case_c = 0

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

        # Cases A/B: every possible K5 high complement must align. In Case B,
        # this covers whichever of the two rows has at most two partial hits.
        ab_checks = 0
        for H in K5:
            for Q_pair in r2_pairs:
                for pair_types in pair_type_subsets:
                    ab_checks += 1
                    assert has_alignment_for_high_row(
                        H, Q_pair, pair_types, low_pairs, K5, vertices, adjacency
                    ), (
                        "Case A/B failure", b, tuple(sorted(H)),
                        tuple(tuple(sorted(Q)) for Q in Q_pair), sorted(pair_types)
                    )
        total_ab += ab_checks

        # Deduplicate the exact Case-C complement pairs. The two profiles
        # (5,5) and (5,4) have d_K <= 5 or 4, so one of H1,H2 has <=2 partial
        # component hits; both H choices must therefore admit alignment.
        # Every other profile has d_K <=3, so either high row is safe.
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
            risky = (s + t >= 9)  # exactly (5,5) or (5,4)
            for Q_pair in r2_pairs:
                for pair_types in pair_type_subsets:
                    case_c_checks += 1
                    if risky:
                        ok = (
                            has_alignment_for_high_row(
                                H1, Q_pair, pair_types, low_pairs,
                                K5, vertices, adjacency
                            )
                            and has_alignment_for_high_row(
                                H2, Q_pair, pair_types, low_pairs,
                                K5, vertices, adjacency
                            )
                        )
                    else:
                        ok = (
                            has_alignment_for_high_row(
                                H1, Q_pair, pair_types, low_pairs,
                                K5, vertices, adjacency
                            )
                            or has_alignment_for_high_row(
                                H2, Q_pair, pair_types, low_pairs,
                                K5, vertices, adjacency
                            )
                        )
                    assert ok, (
                        "Case C failure", b,
                        tuple(sorted(H1)), tuple(sorted(H2)),
                        tuple(tuple(sorted(Q)) for Q in Q_pair), sorted(pair_types)
                    )
        total_case_c += case_c_checks
        summary.append((
            b, len(K5), len(K4), len(low_pairs), len(r2_pairs),
            len(pair_type_subsets), len(high_pairs),
            sum(1 for _, _, s, t in high_pairs if s + t >= 9),
            ab_checks, case_c_checks
        ))

    print(
        "b | K5 | K4 | r1-pairs | r2-pairs | low-type subsets | "
        "Case-C pairs | risky Case-C pairs | A/B configs | C configs"
    )
    for row in summary:
        print(" | ".join(str(x) for x in row))
    print(f"PASS: {total_ab} A/B and {total_case_c} exact-profile Case-C configurations.")
    print("The proof still depends on the stated row contracts and gadget normal form.")


if __name__ == "__main__":
    verify()
