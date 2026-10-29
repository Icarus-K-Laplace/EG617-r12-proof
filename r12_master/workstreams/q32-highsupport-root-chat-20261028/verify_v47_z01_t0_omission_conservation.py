#!/usr/bin/env python3
"""Exact T0--Ti omission audit plus local cross-track excess decomposition.

Scope: E0=0 scalar row y=(7,7,8), exact T0-repeat counts s=(4,3,3),
D-repeat counts d=(0,1,0), and E_i=(2,2,2).

Each T_i has three small-block vertices (indices 0,1,2) and nine non-small
vertices. If h_i(v)=d_H(v,T0) and l_i(v)=d_H(v,T_j union T_k), then
h_i(v)+l_i(v)=1+epsilon_i(v), where epsilon is zero off the three small
vertices and sums to E_i=2. Since each large-pair H graph is a matching,
0<=l_i(v)<=2.

Define:
  u_i = sum_v max(h_i(v)-1,0)       (T0 endpoint multiplicity excess),
  k_i = sum_v max(l_i(v)-1,0)       (overlap of the two large-pair H endpoint sets),
  omega_i = #{v: h_i(v)>0 and l_i(v)>0} (T0/large-H endpoint overlap).
Pointwise degree conservation gives the exact identity E_i=u_i+k_i+omega_i.

The omitted-vertex identity is n_i+delta_D=h_i+r_D. If D repeats on T0--Ti,
its omitted vertex is exactly that repeat endpoint, so delta_D=r_D and n_i=h_i.
If D has no repeat on this pair, z_i(D) must be an H endpoint and
n_i=h_i-delta_D.

This is an endpoint/local-degree relaxation only; it does not impose the
source-labelled residual triangles, actual pairwise matching edges, or full
common-P feasibility.
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
    max_n = 0

    for h in profiles:
        if d_repeat == 0:
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
            # D's repeat endpoint is its omitted vertex; delta_D=r_D.
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

    # Exact local degree-state enumeration: epsilon is distributed among the
    # three small-block vertices; l_i(v)=1+epsilon_i(v)-h_i(v).
    state_count = 0
    decomposition_counts = Counter()
    for h in profiles:
        for eps_small in weak_compositions(excess_budget, 3):
            eps = [0] * vertices
            for j, v in enumerate((0, 1, 2)):
                eps[v] = eps_small[j]
            large_degree = tuple(1 + eps[v] - h[v] for v in range(vertices))
            if any(value < 0 or value > 2 for value in large_degree):
                continue
            assert sum(large_degree) == 12 + excess_budget - y_h
            u = sum(max(value - 1, 0) for value in h)
            k = sum(max(value - 1, 0) for value in large_degree)
            omega = sum(h[v] > 0 and large_degree[v] > 0 for v in range(vertices))
            assert u + k + omega == excess_budget
            assert all(h[v] + large_degree[v] == 1 + eps[v]
                       for v in range(vertices))
            decomposition_counts[(u, k, omega)] += 1
            state_count += 1

    return {
        "track": name,
        "H_T0_edges": y_h,
        "exact_T0_repeat_edges": s_exact,
        "D_T0_repeat_edges": d_repeat,
        "E_i_excess_budget": excess_budget,
        "allowed_H_endpoint_profiles": len(profiles),
        "profile_count_by_H_endpoint_support": dict(sorted(by_support.items())),
        "valid_D_omission_assignments": valid_assignments,
        "max_exact_nonrepeat_omission_multiplicity": max_n,
        "local_degree_states": state_count,
        "local_excess_decomposition_counts": {
            str(key): value for key, value in sorted(decomposition_counts.items())
        },
    }


def main():
    rows = [
        audit_track("T1", 7, 4, 0),
        audit_track("T2", 7, 3, 1),
        audit_track("T3", 8, 3, 0),
    ]
    assert [row["allowed_H_endpoint_profiles"] for row in rows] == [3528, 3528, 3897]
    assert [row["valid_D_omission_assignments"] for row in rows] == [20610, 42336, 25758]
    assert [row["max_exact_nonrepeat_omission_multiplicity"] for row in rows] == [3, 3, 3]
    assert [row["local_degree_states"] for row in rows] == [9270, 9270, 8649]
    assert all(sum(map(int, row["local_excess_decomposition_counts"].values())) ==
               row["local_degree_states"] for row in rows)
    for row in rows:
        print(row)
    print("T0_TI_OMISSION_AND_EXCESS_DECOMPOSITION_AUDIT_OK")
    print("Scope: endpoint/local-degree relaxation only; not full common-P feasibility or Q32 UNSAT.")


if __name__ == "__main__":
    main()
