#!/usr/bin/env python3
"""Exact endpoint-profile audit for T0--Ti omitted-vertex conservation.

Scope: the E0=0 scalar profile (H counts 7,7,8; exact-repeat counts 4,3,3;
D-repeat counts 0,1,0). This enumerates endpoint multiplicities only. It does
NOT impose the cross-track triangle-factorization or prove a Q32 contradiction.

Important: h[v] is the number of H edges from T0 into vertex v of Ti. It is
not known to be <=1; only each T0 vertex has at most one H edge into Ti.
"""
from itertools import product


def compositions(total, bins):
    """All weak compositions of total into bins labeled nonnegative parts."""
    if bins == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, bins - 1):
            yield (first,) + tail


def audit_track(name, y_h, s_exact, d_repeat, exact_colors=10, vertices=12):
    # Every color matching M_C,0i misses one Ti vertex. Of the 10 exact colors,
    # s_exact have their own T0 repeat on this pair; the others contribute one
    # nonrepeat omitted vertex. D contributes one omitted vertex.
    n_exact_nonrepeat = exact_colors - s_exact
    assert y_h + s_exact + d_repeat == 11
    assert y_h + d_repeat - 1 == n_exact_nonrepeat

    h_profiles = list(compositions(y_h, vertices))
    r_profiles = list(compositions(d_repeat, vertices))
    valid = 0
    max_n_at_vertex = 0
    max_support = 0
    d_omission_support_cases = 0

    for h in h_profiles:
        assert sum(h) == y_h
        # h[v] may exceed one: the current theorem bounds H-degree on the T0
        # side, not on the Ti side.
        for r in r_profiles:
            assert sum(r) == d_repeat
            cap = tuple(h[v] + r[v] for v in range(vertices))
            for z_d in range(vertices):
                # Exact multiset identity requires the D-omitted vertex to
                # appear among H endpoints or D-repeat endpoints.
                if cap[z_d] == 0:
                    continue
                n = tuple(cap[v] - (1 if v == z_d else 0)
                          for v in range(vertices))
                assert all(q >= 0 for q in n)
                assert sum(n) == n_exact_nonrepeat
                assert tuple(n[v] + (1 if v == z_d else 0)
                             for v in range(vertices)) == cap
                valid += 1
                max_n_at_vertex = max(max_n_at_vertex, max(n))
                max_support = max(max_support, sum(q > 0 for q in cap))
                d_omission_support_cases += 1

    # A deliberately concentrated local relaxation: it satisfies all scalar
    # endpoint counts and the exact multiset identity, but multiple exact
    # colors omit the same Ti vertex. This refutes any injectivity claim based
    # on this identity alone; it is not a full graph-coloring witness.
    h = (y_h,) + (0,) * (vertices - 1)
    r = (d_repeat,) + (0,) * (vertices - 1)
    z_d = 0
    cap = tuple(h[v] + r[v] for v in range(vertices))
    assert cap[z_d] > 0
    n = tuple(cap[v] - (1 if v == z_d else 0)
              for v in range(vertices))
    assert all(q >= 0 for q in n)
    assert sum(n) == n_exact_nonrepeat
    assert max(n) == y_h + d_repeat - 1
    assert tuple(n[v] + (1 if v == z_d else 0)
                 for v in range(vertices)) == cap

    return {
        "track": name,
        "counts": {
            "H_edges": y_h,
            "exact_T0_repeat_edges": s_exact,
            "D_repeat_edges": d_repeat,
            "exact_colors_without_repeat_on_this_pair": n_exact_nonrepeat,
        },
        "weak_compositions_h": len(h_profiles),
        "weak_compositions_D_repeat_endpoints": len(r_profiles),
        "valid_endpoint_profiles": valid,
        "max_exact_nonrepeat_omissions_at_one_vertex": max_n_at_vertex,
        "max_endpoint_support": max_support,
        "concentrated_local_relaxation": {
            "h": h,
            "r_D": r,
            "D_omitted_vertex": z_d,
            "exact_nonrepeat_omissions": n,
        },
    }


def main():
    # E0=0 candidate scalar profile used in the owner-only audit:
    # y=(7,7,8), exact repeat=(4,3,3), D repeat=(0,1,0).
    rows = [
        audit_track("T1", 7, 4, 0),
        audit_track("T2", 7, 3, 1),
        audit_track("T3", 8, 3, 0),
    ]
    expected = [148512, 2015520, 381888]
    assert [row["valid_endpoint_profiles"] for row in rows] == expected
    assert [row["max_exact_nonrepeat_omissions_at_one_vertex"] for row in rows] == [6, 7, 7]
    for row in rows:
        print(row)
    print("T0_TI_OMISSION_MULTISETS_EXACT_PROFILE_AUDIT_OK")
    print("Scope: endpoint-multiplicity relaxation only; not full common-P feasibility or Q32 UNSAT.")


if __name__ == "__main__":
    main()
