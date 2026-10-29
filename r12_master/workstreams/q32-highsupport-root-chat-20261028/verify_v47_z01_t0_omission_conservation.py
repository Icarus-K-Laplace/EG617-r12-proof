#!/usr/bin/env python3
"""Exact T0--Ti omitted-vertex audit with the small-block excess budget.

Scope: E0=0 scalar row y=(7,7,8), exact T0-repeat counts s=(4,3,3),
D-repeat counts d=(0,1,0), and E_i=(2,2,2).

In each T_i, the three small-block vertices are indexed 0,1,2 and the other
nine vertices are non-small. Non-small vertices have cross-track H degree 1;
small-block vertices have degree 1+epsilon, with total epsilon E_i=2.
Consequently h_i(v)=d_H(v,T0) is <=1 at non-small vertices and
sum_v max(h_i(v)-1,0) <= E_i. This is NOT a binary H-endpoint condition.

For D with a repeat edge on T0--Ti, its omitted vertex is exactly that
repeat edge's Ti endpoint, so delta_D(v)=r_D(v) and the identity reduces to
n_i(v)=h_i(v). If D has no repeat on this pair, its omitted vertex must be
an H endpoint and n_i(v)=h_i(v)-delta_D(v).

The enumeration is an endpoint-multiplicity relaxation only. It does not
impose the source-labelled residual triangles, cross-track matching edges,
or the full common-P CSP.
"""
from collections import Counter


def weak_compositions(total, bins):
    if bins == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, bins - 1):
            yield (first,) + tail


def allowed_h_profiles(total_h, excess_budget, vertices=12, small_vertices=(0, 1, 2)):
    small_vertices = set(small_vertices)
    for h in weak_compositions(total_h, vertices):
        if any(h[v] > 1 for v in range(vertices) if v not in small_vertices):
            continue
        excess = sum(max(value - 1, 0) for value in h)
        if excess > excess_budget:
            continue
        yield h


def audit_track(name, y_h, s_exact, d_repeat, excess_budget=2, vertices=12):
    n_exact_nonrepeat = 10 - s_exact
    assert y_h + s_exact + d_repeat == 11
    assert y_h - (1 if d_repeat == 0 else 0) == n_exact_nonrepeat

    profiles = list(allowed_h_profiles(y_h, excess_budget, vertices))
    by_support = Counter(sum(value > 0 for value in h) for h in profiles)
    valid_assignments = 0
    max_h = max(max(h) for h in profiles)
    max_n = 0
    max_overage = max(sum(max(value - 1, 0) for value in h) for h in profiles)

    for h in profiles:
        assert sum(h) == y_h
        assert all(h[v] <= 1 for v in range(3, vertices))
        assert sum(max(value - 1, 0) for value in h) <= excess_budget

        if d_repeat == 0:
            # D has no repeat on this pair. Its omitted vertex must be an H
            # endpoint; subtract that one occurrence from the H endpoint multiset.
            for z_d in range(vertices):
                if h[z_d] == 0:
                    continue
                n = tuple(h[v] - (1 if v == z_d else 0)
                          for v in range(vertices))
                assert all(value >= 0 for value in n)
                assert sum(n) == n_exact_nonrepeat
                assert tuple(n[v] + (1 if v == z_d else 0)
                             for v in range(vertices)) == h
                valid_assignments += 1
                max_n = max(max_n, max(n))
        else:
            # Here D has exactly one repeat edge in P_0i. Its endpoint is the
            # unique omitted vertex of D on this pair; delta_D=r_D exactly.
            for d_endpoint in range(vertices):
                r_d = tuple(1 if v == d_endpoint else 0 for v in range(vertices))
                delta_d = r_d
                n = h
                assert sum(n) == n_exact_nonrepeat
                assert tuple(n[v] + delta_d[v] for v in range(vertices)) == tuple(
                    h[v] + r_d[v] for v in range(vertices)
                )
                valid_assignments += 1
                max_n = max(max_n, max(n))

    return {
        "track": name,
        "H_T0_edges": y_h,
        "exact_T0_repeat_edges": s_exact,
        "D_T0_repeat_edges": d_repeat,
        "E_i_excess_budget": excess_budget,
        "allowed_H_endpoint_profiles": len(profiles),
        "profile_count_by_H_endpoint_support": dict(sorted(by_support.items())),
        "valid_D_omission_assignments": valid_assignments,
        "max_H_endpoint_multiplicity": max_h,
        "max_exact_nonrepeat_omission_multiplicity": max_n,
        "max_H_endpoint_excess": max_overage,
    }


def main():
    rows = [
        audit_track("T1", 7, 4, 0),
        audit_track("T2", 7, 3, 1),
        audit_track("T3", 8, 3, 0),
    ]
    assert [row["allowed_H_endpoint_profiles"] for row in rows] == [3528, 3528, 3897]
    assert [row["valid_D_omission_assignments"] for row in rows] == [20610, 42336, 25758]
    assert [row["max_H_endpoint_multiplicity"] for row in rows] == [3, 3, 3]
    assert [row["max_exact_nonrepeat_omission_multiplicity"] for row in rows] == [3, 3, 3]
    assert all(row["max_H_endpoint_excess"] == 2 for row in rows)
    for row in rows:
        print(row)
    print("T0_TI_OMISSION_EXCESS_BUDGET_AUDIT_OK")
    print("Scope: endpoint-multiplicity relaxation only; not full common-P feasibility or Q32 UNSAT.")


if __name__ == "__main__":
    main()
