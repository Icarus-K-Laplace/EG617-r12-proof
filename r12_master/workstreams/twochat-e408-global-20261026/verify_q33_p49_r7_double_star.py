#!/usr/bin/env python3
"""Exact 11-point gadget verifier for the Q33 P_C=49 profile (7,1^6).

Checks two finite facts used by the repaired double-star proof:
(1) every universal D has a disjoint member in every low-block K5/K5
    complement pair;
(2) for any two clique complements E,F with |E union F| >= 4, at least one
    of E,F has size >= 2 and is disjoint from a member D of the registered
    universal family.

Only the standard library is used. This verifies the finite gadget statements,
not the upstream exact-129 factorization or row-budget theorems.
"""
from itertools import combinations


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


def cliques(vertices, adjacency, size):
    return [
        frozenset(S)
        for S in combinations(vertices, size)
        if all(v in adjacency[u] for u, v in combinations(S, 2))
    ]


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


def verify_one_form(b):
    vertices, adjacency = make_gadget(b)
    Ds = universal_D_family(b)
    by_size = {k: cliques(vertices, adjacency, k) for k in range(1, 6)}
    all_k5 = by_size[5]
    assert len(all_k5) == {1: 4, 2: 3, 3: 3, 4: 4}[b]
    assert all(D in all_k5 for D in Ds)
    assert max(k for k in range(1, 6) if by_size[k]) == 5

    low_pair_tests = 0
    for H in all_k5:
        for J in all_k5:
            if not H.isdisjoint(J):
                continue
            for D in Ds:
                low_pair_tests += 1
                assert H.isdisjoint(D) or J.isdisjoint(D), (
                    "universal-D low-pair failure", b, H, J, D
                )

    high_pair_tests = 0
    for s in range(1, 6):
        for t in range(1, 6):
            for E in by_size[s]:
                for F in by_size[t]:
                    if len(E | F) < 4:
                        continue
                    high_pair_tests += 1
                    good = any(
                        len(G) >= 2 and any(G.isdisjoint(D) for D in Ds)
                        for G in (E, F)
                    )
                    assert good, (
                        "high-pair alignment failure", b, E, F, Ds
                    )

    return len(all_k5), len(Ds), low_pair_tests, high_pair_tests


def main():
    expected = {
        1: (4, 2, 12, 7376),
        2: (3, 3, 12, 6314),
        3: (3, 3, 12, 6314),
        4: (4, 2, 12, 7376),
    }
    results = {}
    for b in range(1, 5):
        got = verify_one_form(b)
        assert got == expected[b], (b, got, expected[b])
        results[b] = got

    print("PASS: Q33 P_C=49 profile (7,1^6) gadget alignment")
    print("columns: (K5 cliques, universal D, low-pair tests, high-pair tests)")
    for b, result in results.items():
        print(f"normal form {b}: {result}")
    print("total low-pair tests:", sum(x[2] for x in results.values()))
    print("total high-pair tests:", sum(x[3] for x in results.values()))
    print("failures: 0")
    print("Scope: finite gadget certificate only; graph-theoretic contracts remain explicit.")


if __name__ == "__main__":
    main()
