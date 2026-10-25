#!/usr/bin/env python3
"""Arithmetic verifier for R12_E408_Q33_S0_12_EXCLUSION.md.

This checks the finite degree-pattern exhaustion and multiplicity bookkeeping.
It does not verify the graph-theoretic transversal lemmas or the upstream T61 /
exact-129 reduction contracts; those remain proof dependencies.
"""
from itertools import combinations, product


def min_required_T_excess(n7, a, high_T_sets):
    """Minimum sum eps_t needed when each t has at most 6 W-neighbors if eps_t=0."""
    return sum(
        max(0, n7 + a + sum(t in hs for hs in high_T_sets) - 6)
        for t in range(7)
    )


def choose_T_sets(b_tuple):
    choices = [list(combinations(range(7), b)) for b in b_tuple]
    for sets in product(*choices):
        yield [set(s) for s in sets]


def enumerate_profiles():
    profiles = []
    # Each tuple is (N_7, high q-values, number of q=8 vertices).
    shapes = [
        (2, (), 14),
        (3, (9,), 12),
        (4, (9, 9), 10),
        (4, (10,), 11),
    ]
    for n7, high_qs, n8 in shapes:
        b_domains = []
        for q in high_qs:
            b_domains.append((0, 1, 7) if q == 9 else (0, 1, 2, 7))
        b_tuples = product(*b_domains) if b_domains else [()]
        for b_tuple in b_tuples:
            for a in range(n8 + 1):
                eps_t = 7 * n7 + 7 * a + sum(b_tuple) - 42
                if not 0 <= eps_t <= 4:
                    continue
                feasible = any(
                    min_required_T_excess(n7, a, high_sets) <= eps_t
                    for high_sets in choose_T_sets(b_tuple)
                )
                if not feasible:
                    continue
                m = n8 - a
                A = a + sum(q - b for q, b in zip(high_qs, b_tuple))
                q_sum = 7 * n7 + 8 * n8 + sum(high_qs)
                assert q_sum == 126
                assert 8 * m == 84 - eps_t - A
                profiles.append(
                    (n7, high_qs, tuple(sorted(b_tuple)), a, eps_t, m, A)
                )
    return sorted(set(profiles), key=lambda p: (p[0], p[1], p[2], p[3]))


def partitions_of_m_into_three(m, cap=4):
    out = []
    for x in range(1, cap + 1):
        for y in range(1, x + 1):
            for z in range(1, y + 1):
                if x + y + z == m:
                    out.append((x, y, z))
    return sorted(out, reverse=True)


def main():
    profiles = enumerate_profiles()
    # Expected cases after imposing (i) the exact cross-degree sum,
    # (ii) eps_T in [0,4], and (iii) the zero-excess T-degree constraints.
    expected = {
        (2, (), (), 4, 0, 10, 4),
        (3, (9,), (0,), 3, 0, 9, 12),
        (3, (9,), (1,), 3, 1, 9, 11),
        (3, (9,), (7,), 2, 0, 10, 4),
        (4, (9, 9), (0, 0), 2, 0, 8, 20),
        (4, (9, 9), (0, 1), 2, 1, 8, 19),
        (4, (9, 9), (0, 7), 1, 0, 9, 12),
        (4, (9, 9), (1, 1), 2, 2, 8, 18),
        (4, (9, 9), (1, 7), 1, 1, 9, 11),
        (4, (9, 9), (7, 7), 0, 0, 10, 4),
        (4, (10,), (0,), 2, 0, 9, 12),
        (4, (10,), (1,), 2, 1, 9, 11),
        (4, (10,), (2,), 2, 2, 9, 10),
        (4, (10,), (7,), 1, 0, 10, 4),
    }
    actual = set(profiles)
    assert actual == expected, (
        "degree-profile mismatch\nmissing=%r\nextra=%r"
        % (sorted(expected - actual), sorted(actual - expected))
    )

    expected_mults = {
        8: [(4, 3, 1), (4, 2, 2), (3, 3, 2)],
        9: [(4, 4, 1), (4, 3, 2), (3, 3, 3)],
        10: [(4, 4, 2), (4, 3, 3)],
    }
    for m, pats in expected_mults.items():
        assert partitions_of_m_into_three(m) == pats

    # Audit the case-level special-incidence thresholds used in the proof:
    # a multiplicity-one part needs at least 16 incidences; a multiplicity-two
    # part needs at least 8; multiplicity four creates a K12 under the lemmas.
    for n7, high_qs, b_tuple, a, eps_t, m, A in profiles:
        pats = partitions_of_m_into_three(m)
        if m == 10:
            assert A == 4
            assert pats == [(4, 4, 2), (4, 3, 3)]
            # (4,4,2) needs >=8 incidences on the 2-part; (4,3,3) has a 4-part.
            assert A < 8
        elif m == 9:
            assert A <= 12
            assert pats == [(4, 4, 1), (4, 3, 2), (3, 3, 3)]
            # The (4,4,1) profile needs 16 incidences on its 1-part.
            assert A < 16
        elif m == 8:
            assert n7 == 4 and high_qs == (9, 9) and a == 2
            assert pats == [(4, 3, 1), (4, 2, 2), (3, 3, 2)]
            # The first two profiles have a multiplicity-4 part.
            assert pats[:2] == [(4, 3, 1), (4, 2, 2)]

    # Uncovered-point bounds: an uncovered r needs a_r >= 3. Each of the h
    # high vertices and each of the a T+{r} vertices contributes at most one
    # incidence at any fixed r. Hence each uncovered point consumes at least
    # max(0, 3-h) of the a T-type incidences; the A/3 bound is also necessary.
    for n7, high_qs, b_tuple, a, eps_t, m, A in profiles:
        h = len(high_qs)
        assert h <= 2
        max_uncovered = min(A // 3, a // (3 - h))
        if m == 10:
            assert max_uncovered <= 1
        elif m == 9:
            assert max_uncovered <= 1
        elif m == 8:
            assert max_uncovered <= 2

    print("S0=12 arithmetic verifier: PASS")
    print("feasible degree profiles:", len(profiles))
    for p in profiles:
        print(p)
    print("multiplicity partitions:", expected_mults)
    print("row identity and all case-level incidence thresholds: PASS")
    print("Scope: arithmetic only; graph lemmas and upstream contracts are not machine-verified.")


if __name__ == "__main__":
    main()
