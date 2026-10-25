#!/usr/bin/env python3
"""Exact gadget/incidence verifier for the P_C=49 profile (6,2,1^5).

The r=6 row classification has Cases A/B/C. Case A has one no-component row
with a K5 omitted gadget clique and zero partial-component incidence in that
row. Cases B/C have a pair of no-component rows whose omitted-clique size
profile is among the registered nine profiles. The r=2 block has a 55 or 54
omitted-pair profile. The checker selects a high-row complement of size >=3
and a middle-row complement of size >=4, both disjoint from a registered
universal D; these complements necessarily intersect inside U\\D. It also
checks the partial-component incidence sum is <=4.

The six r=1 blocks can be aligned to any registered universal D. All selected
omitted sets are proper subsets of the six-point set U\\D, so the seven-set
omission pigeonhole yields an outside vertex with at least two C-edges into
the constructed K12. No single-external-edge isolation inference is used.
"""
from itertools import combinations

ALLOWED_SIZES = {
    1: ((5, 5),),
    2: ((5, 5), (5, 4)),
    3: ((5, 5), (5, 4), (5, 3), (4, 4)),
    4: ((5, 5), (5, 4), (5, 3), (4, 4), (5, 2), (4, 3)),
    5: ((5, 5), (5, 4), (5, 3), (4, 4), (5, 2), (4, 3),
        (5, 1), (4, 2), (3, 3)),
    6: ((5, 5), (5, 4), (5, 3), (4, 4), (5, 2), (4, 3),
        (5, 1), (4, 2), (3, 3)),
}


def make_gadget(b):
    vertices = tuple(range(11))
    A, B, x = set(range(5)), set(range(5, 10)), 10
    A0, B0 = {0}, set(range(5, 5 + b))
    adj = {v: set() for v in vertices}

    def add(u, v):
        adj[u].add(v)
        adj[v].add(u)

    for K in (A, B):
        for u, v in combinations(sorted(K), 2):
            add(u, v)
    for u in A - A0:
        add(x, u)
    for v in B - B0:
        add(x, v)
    for u in A0:
        for v in B0:
            add(u, v)
    return vertices, adj


def cliques(V, adj, size):
    return [
        frozenset(S) for S in combinations(V, size)
        if all(v in adj[u] for u, v in combinations(S, 2))
    ]


def allowed_pairs(V, adj, budget):
    by = {k: cliques(V, adj, k) for k in range(1, 6)}
    out, seen = [], set()
    for s, t in ALLOWED_SIZES[budget]:
        for H in by[s]:
            for J in by[t]:
                if not H.isdisjoint(J):
                    continue
                key = tuple(sorted((tuple(sorted(H)), tuple(sorted(J)))))
                if key not in seen:
                    seen.add(key)
                    out.append((H, J))
    return out


def universal_D_family(b):
    A, B, x = set(range(5)), set(range(5, 10)), 10
    A_prime = frozenset((A - {0}) | {x})
    if b == 1:
        Ds = [frozenset(A), frozenset(B)]
    elif b in (2, 3):
        Ds = [frozenset(A), frozenset(B), A_prime]
    else:
        Ds = [A_prime, frozenset(B)]
    return list(dict.fromkeys(Ds))


def allocations(H, J, r):
    extra_budget = r - (11 - len(H) - len(J))
    return [
        (p, q)
        for p in range(extra_budget + 1)
        for q in range(extra_budget - p + 1)
    ]


def verify_case_A(b):
    V, adj = make_gadget(b)
    Ds = universal_D_family(b)
    K5 = cliques(V, adj, 5)
    pairs2 = allowed_pairs(V, adj, 2)
    checks = 0
    for H in K5:
        # Case A's sole no-component row has no partial component incidences.
        for Q in pairs2:
            for q, q2 in allocations(Q[0], Q[1], 2):
                checks += 1
                found = False
                for J, pj in ((Q[0], q), (Q[1], q2)):
                    if len(J) < 4 or pj > 4 or not H.intersection(J):
                        continue
                    if any(H.isdisjoint(D) and J.isdisjoint(D) for D in Ds):
                        found = True
                        break
                if not found:
                    return False, checks
    return True, checks


def verify_cases_BC(b):
    V, adj = make_gadget(b)
    Ds = universal_D_family(b)
    high_pairs = allowed_pairs(V, adj, 6)
    mid_pairs = allowed_pairs(V, adj, 2)
    high_choices = []
    for P in high_pairs:
        for p, p2 in allocations(P[0], P[1], 6):
            opts = [(H, ph) for H, ph in ((P[0], p), (P[1], p2)) if len(H) >= 3]
            high_choices.append((P, p, p2, opts))
    mid_choices = []
    for Q in mid_pairs:
        for q, q2 in allocations(Q[0], Q[1], 2):
            opts = [(J, pj) for J, pj in ((Q[0], q), (Q[1], q2)) if len(J) >= 4]
            mid_choices.append((Q, q, q2, opts))

    checks = 0
    for P, p, p2, high_opts in high_choices:
        for Q, q, q2, mid_opts in mid_choices:
            checks += 1
            found = False
            for H, ph in high_opts:
                for J, pj in mid_opts:
                    if ph + pj > 4 or not H.intersection(J):
                        continue
                    if any(H.isdisjoint(D) and J.isdisjoint(D) for D in Ds):
                        found = True
                        break
                if found:
                    break
            if not found:
                return False, checks
    return True, checks


def main():
    expected_high_pairs = {1: 940, 2: 794, 3: 794, 4: 940}
    expected_mid_pairs = {1: 31, 2: 22, 3: 22, 4: 31}
    case_a_total = case_bc_total = 0

    for b in range(1, 5):
        V, adj = make_gadget(b)
        assert len(allowed_pairs(V, adj, 6)) == expected_high_pairs[b]
        assert len(allowed_pairs(V, adj, 2)) == expected_mid_pairs[b]

        ok, checks = verify_case_A(b)
        assert ok, ("Case A failure", b)
        case_a_total += checks

        ok, checks = verify_cases_BC(b)
        assert ok, ("Cases B/C failure", b)
        case_bc_total += checks

    assert case_a_total == 452
    assert case_bc_total == 570942

    print("PASS: P_C=49 profile (6,2,1^5)")
    print("Case A single-row alignments:", case_a_total)
    print("Cases B/C pair/allocation alignments:", case_bc_total)
    print("Total exact gadget/incidence configurations:", case_a_total + case_bc_total)
    print("Scope: local profile only; upstream r=6 row classification remains a theorem dependency.")


if __name__ == "__main__":
    main()
