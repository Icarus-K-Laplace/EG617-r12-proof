#!/usr/bin/env python3
"""Exact T0--Ti omitted-vertex audit under the aligned zero-slack degree ledger.

Scope: E0=0 scalar profile (H counts 7,7,8; exact-repeat counts 4,3,3;
D-repeat counts 0,1,0). Each Ti vertex has total H cross-track degree exactly
one in the frozen aligned 3+7 zero-slack cell, so its H degree into T0 is
binary. This binary bound comes from the global degree ledger, not from the
asymmetric 13-set lemma alone.

The enumeration is still only an endpoint-multiplicity relaxation. It does
not impose cross-track triangle-factorization or certify Q32 UNSAT.
"""
from itertools import combinations


def binary_profiles(total, vertices=12):
    """Binary vectors of length vertices with exactly total ones."""
    for support in combinations(range(vertices), total):
        row = [0] * vertices
        for v in support:
            row[v] = 1
        yield tuple(row)


def compositions(total, bins):
    """Weak compositions of total into bins labeled nonnegative parts."""
    if bins == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, bins - 1):
            yield (first,) + tail


def audit_track(name, y_h, s_exact, d_repeat, exact_colors=10, vertices=12):
    # The ten exact colors contribute one omitted vertex each. s_exact exact
    # colors have their own T0 repeat on this pair, so 10-s_exact omitted
    # vertices remain after canceling those repeat owners. D contributes one.
    n_exact_nonrepeat = exact_colors - s_exact
    assert y_h + s_exact + d_repeat == 11
    assert y_h + d_repeat - 1 == n_exact_nonrepeat

    h_profiles = list(binary_profiles(y_h, vertices))
    r_profiles = list(compositions(d_repeat, vertices))
    valid = 0
    max_n_at_vertex = 0
    max_support = 0

    for h in h_profiles:
        assert all(q in (0, 1) for q in h)
        assert sum(h) == y_h
        for r in r_profiles:
            assert sum(r) == d_repeat
            cap = tuple(h[v] + r[v] for v in range(vertices))
            for z_d in range(vertices):
                # The D-omitted vertex must be an H endpoint or a D-repeat
                # endpoint, otherwise n = h+r-delta would be negative.
                if cap[z_d] == 0:
                    continue
                n = tuple(cap[v] - (1 if v == z_d else 0)
                          for v in range(vertices))
                assert all(q >= 0 for q in n)
                assert sum(n) == n_exact_nonrepeat
                assert tuple(n[v] + (1 if v == z_d else 0)
                             for v in range(vertices)) == cap
                # Correct pointwise consequence: away from D-repeat
                # endpoints, at most one exact nonrepeat color omits v.
                for v in range(vertices):
                    if r[v] == 0:
                        assert n[v] <= 1
                    else:
                        assert n[v] <= 1 + r[v]
                valid += 1
                max_n_at_vertex = max(max_n_at_vertex, max(n))
                max_support = max(max_support, sum(q > 0 for q in cap))

    return {
        "track": name,
        "counts": {
            "H_edges": y_h,
            "exact_T0_repeat_edges": s_exact,
            "D_repeat_edges": d_repeat,
            "exact_colors_without_repeat_on_this_pair": n_exact_nonrepeat,
        },
        "binary_H_endpoint_profiles": len(h_profiles),
        "D_repeat_endpoint_profiles": len(r_profiles),
        "valid_endpoint_profiles": valid,
        "max_exact_nonrepeat_omissions_at_one_vertex": max_n_at_vertex,
        "max_endpoint_support": max_support,
        "injectivity_away_from_D_repeat_endpoints": True,
    }


def main():
    # E0=0 scalar row in the all-Class-A owner-only relaxation.
    rows = [
        audit_track("T1", 7, 4, 0),
        audit_track("T2", 7, 3, 1),
        audit_track("T3", 8, 3, 0),
    ]
    expected_counts = [5544, 70488, 3960]
    assert [row["valid_endpoint_profiles"] for row in rows] == expected_counts
    assert [row["max_exact_nonrepeat_omissions_at_one_vertex"] for row in rows] == [1, 2, 1]
    for row in rows:
        print(row)
    print("T0_TI_OMISSION_MULTISETS_ALIGNED_ZERO_SLACK_AUDIT_OK")
    print("Scope: endpoint-multiplicity relaxation only; not full common-P feasibility or Q32 UNSAT.")


if __name__ == "__main__":
    main()
