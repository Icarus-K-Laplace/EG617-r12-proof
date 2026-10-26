#!/usr/bin/env python3
"""Arithmetic/profile audit for R12_E408_Q33_S0_13_EXCLUSION.md.

This verifier enumerates the finite degree/T-incidence parameter cases and
checks the numerical margins used by the proof. It is not a graph-realization
certificate and does not replace the analytic transversal/clique arguments.
"""
from collections import defaultdict
from itertools import product


def b_options(q):
    if q == 9:
        return (0, 1, 7)
    if q == 10:
        return (0, 1, 2, 7)
    if q == 11:
        return (0, 1, 2, 3, 7)
    raise ValueError(q)


def main():
    high_profiles = {
        1: [()],
        2: [(9,)],
        3: [(9, 9), (10,)],
        4: [(9, 9, 9), (9, 10), (11,)],
    }
    rows = []
    for k, profiles in high_profiles.items():
        for qs in profiles:
            n8 = 16 - k - len(qs)
            assert 7 * k + 8 * n8 + sum(qs) == 127
            b_profiles = product(*[b_options(q) for q in qs]) if qs else [()]
            for bs in b_profiles:
                B = sum(bs)
                for a in range(0, 7 - k):
                    eps_T = 7 * (k + a - 6) + B
                    if not (0 <= eps_T <= 3):
                        continue
                    m = n8 - a
                    special = a + sum(q - b for q, b in zip(qs, bs))
                    low_high = sum(b < 7 for b in bs)
                    # Exact finite-contract checks.
                    assert k + a <= 6
                    assert eps_T <= 13 - 2 * 5  # epsilon_U <= 3 at S0=13
                    assert all(b == 7 or b <= q - 8 for q, b in zip(qs, bs))
                    assert m in (7, 8, 9, 10)
                    rows.append((k, qs, bs, a, eps_T, m, special, low_high))

    assert len(rows) == 60
    by_m = defaultdict(list)
    for row in rows:
        by_m[row[5]].append(row)

    assert {m: len(v) for m, v in by_m.items()} == {10: 6, 9: 24, 8: 22, 7: 8}
    assert all(r[6] == 5 and r[7] == 0 for r in by_m[10])
    assert all(10 <= r[6] <= 13 and r[7] >= 1 for r in by_m[9])
    assert all(18 <= r[6] <= 21 and r[7] >= 2 for r in by_m[8])
    assert all(26 <= r[6] <= 29 and r[7] == 3 for r in by_m[7])

    # In m=8,7 cases with only two distinct R-only sets, every low-b high
    # neighborhood must contain one 8-set; its R spill is q-b-8 <= 2.
    # A possible b=7 vertex in the m=8 family has q=9 and only two R points.
    for m in (7, 8):
        for r in by_m[m]:
            k, qs, bs, a, eps_T, _, special, low_high = r
            outside_union_cap = a
            for q, b in zip(qs, bs):
                if b == 7:
                    outside_union_cap += q - b
                else:
                    outside_union_cap += q - b - 8
            assert outside_union_cap <= 5, r
            assert outside_union_cap < 3 * 8

    # If three distinct R-only sets partition R, the possible multiplicity
    # patterns after excluding any group of size four are as stated.
    patterns = {
        10: [(4, 3, 3), (4, 4, 2)],
        9: [(3, 3, 3)],
        8: [(3, 3, 2)],
        7: [(3, 3, 1), (3, 2, 2)],
    }
    for m, ps in patterns.items():
        assert all(sum(p) == m and max(p) <= 4 for p in ps)
    assert all(max(p) == 4 for p in patterns[10])
    assert all(max(p) == 4 for p in patterns[9] if max(p) == 4)  # vacuous audit guard

    # The high-neighborhood degree caps used in Lemma 2.4.
    assert 12 + 4 - 10 == 6
    assert 12 + 4 - 11 == 5
    assert 7 + 2 == 9
    assert 8 + 2 + 2 == 12  # K8 + a size-2 group + two adjacent high vertices
    assert 8 + 1 + 3 == 12  # K8 + singleton group + three adjacent high vertices
    assert 8 + 3 == 11      # K8 + a size-3 group, then one high vertex makes K12

    print("E408_Q33_S0_13_PROFILE_AUDIT_OK")
    print("60 labelled degree/T-incidence cases checked; profile buckets: m=10:6, m=9:24, m=8:22, m=7:8.")
    print("Scope: arithmetic/profile checks only; analytic graph arguments remain in the theorem note.")


if __name__ == "__main__":
    main()
