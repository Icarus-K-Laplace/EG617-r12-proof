#!/usr/bin/env python3
"""Exact gadget-alignment verifier for the P_C=50 profiles (5,2,1^5)
and (4,3,1^5).

The finite predicate builds a K12 and finds an external gadget vertex with
at least two C-edges into it. It uses the valid star-capacity bound
d_C(z,K12) <= 1; it does not assume that a monochromatic K12 is isolated.

This script verifies gadget alignment and the finite incidence-budget split.
It does not machine-verify the exact-129 factor theorem or row classifications.
"""
from itertools import combinations

ALLOWED_PROFILES = {
    1: {(5, 5)},
    2: {(5, 5), (5, 4)},
    3: {(5, 5), (5, 4), (5, 3), (4, 4)},
    4: {(5, 5), (5, 4), (5, 3), (4, 4), (5, 2), (4, 3)},
    5: {
        (5, 5), (5, 4), (5, 3), (4, 4), (5, 2),
        (4, 3), (5, 1), (4, 2), (3, 3),
    },
}


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


def allowed_pairs_for_r(vertices, adjacency, r):
    by_size = {k: cliques(vertices, adjacency, k) for k in range(1, 6)}
    out = []
    seen = set()
    for s, t in ALLOWED_PROFILES[r]:
        for H in by_size[s]:
            for J in by_size[t]:
                if not H.isdisjoint(J):
                    continue
                key = tuple(sorted((tuple(sorted(H)), tuple(sorted(J)))))
                if key not in seen:
                    seen.add(key)
                    out.append((H, J))
    return out


def has_alignment_for_fixed_rows(H, Q, low_pair_types, low_pairs,
                                 K5, vertices, adjacency):
    """Find D and z for fixed selected row complements H and Q."""
    U = set(vertices)
    if not H.intersection(Q):
        return False

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

        # z is outside H, so it sees the selected high row. If z sees D or
        # lies outside any selected low-row complement, it has a second
        # C-edge into the constructed K12.
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


def verify_profile(r_high, r_mid):
    totals = {"easy": 0, "risky": 0}
    summary = []
    failures = []

    for b in range(1, 5):
        vertices, adjacency = make_gadget(b)
        K5 = cliques(vertices, adjacency, 5)
        low_pairs = disjoint_pairs(K5)
        low_pair_type_subsets = [
            frozenset(i for i in range(len(low_pairs)) if mask & (1 << i))
            for mask in range(1, 1 << len(low_pairs))
            if sum(1 for i in range(len(low_pairs)) if mask & (1 << i)) <= 5
        ]
        high_pairs = allowed_pairs_for_r(vertices, adjacency, r_high)
        mid_pairs = allowed_pairs_for_r(vertices, adjacency, r_mid)
        easy_checks = risky_checks = 0

        for Hp in high_pairs:
            high_a = 11 - len(Hp[0]) - len(Hp[1])
            high_budget = r_high - high_a
            for Qp in mid_pairs:
                mid_a = 11 - len(Qp[0]) - len(Qp[1])
                mid_budget = r_mid - mid_a
                risky = high_budget + mid_budget > 4

                for low_types in low_pair_type_subsets:
                    # Cache the finite gadget predicate for each row choice.
                    align = [
                        [
                            has_alignment_for_fixed_rows(
                                H, Q, low_types, low_pairs, K5, vertices, adjacency
                            )
                            for Q in Qp
                        ]
                        for H in Hp
                    ]

                    if not risky:
                        easy_checks += 1
                        if not any(any(row) for row in align):
                            failures.append((b, Hp, Qp, low_types, "easy"))
                            return False, totals, summary, failures
                        continue

                    risky_checks += 1
                    # The only possible excess-budget risk is that selected
                    # rows could jointly cover all five vertices of a K5
                    # component. Enumerate every allocation p1+p2<=budget_H
                    # and q1+q2<=budget_Q; require an aligned choice with
                    # p_H+q_Q<=4 for each allocation.
                    for p1 in range(high_budget + 1):
                        for p2 in range(high_budget - p1 + 1):
                            for q1 in range(mid_budget + 1):
                                for q2 in range(mid_budget - q1 + 1):
                                    p = (p1, p2)
                                    q = (q1, q2)
                                    ok = any(
                                        align[i][j] and p[i] + q[j] <= 4
                                        for i in range(2)
                                        for j in range(2)
                                    )
                                    if not ok:
                                        failures.append((
                                            b, Hp, Qp, low_types, p, q, "risky"
                                        ))
                                        return False, totals, summary, failures

        totals["easy"] += easy_checks
        totals["risky"] += risky_checks
        summary.append((
            b, len(high_pairs), len(mid_pairs), len(low_pairs),
            len(low_pair_type_subsets), easy_checks, risky_checks
        ))

    return True, totals, summary, failures


def main():
    # P_C=50, R_C=12, r=(5,2,1,1,1,1,1).
    ok_52, totals_52, summary_52, failures_52 = verify_profile(5, 2)
    assert ok_52, failures_52

    # P_C=50, R_C=12, r=(4,3,1,1,1,1,1).
    ok_43, totals_43, summary_43, failures_43 = verify_profile(4, 3)
    assert ok_43, failures_43

    print("Profile (5,2,1^5):")
    for row in summary_52:
        print("  b | high-pairs | mid-pairs | low-pairs | low-type subsets | easy | risky =", row)
    print("  totals:", totals_52)
    print("Profile (4,3,1^5):")
    for row in summary_43:
        print("  b | high-pairs | mid-pairs | low-pairs | low-type subsets | easy | risky =", row)
    print("  totals:", totals_43)
    grand = sum(totals_52.values()) + sum(totals_43.values())
    print(f"PASS: {grand} exact gadget/incidence configurations, zero failures.")
    print("Scope: gadget alignment plus finite incidence-budget split only.")


if __name__ == "__main__":
    main()
