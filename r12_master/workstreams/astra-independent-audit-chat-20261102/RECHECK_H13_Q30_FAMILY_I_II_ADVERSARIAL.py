#!/usr/bin/env python3
"""Independent adversarial recheck of h13 Q30 Families I and II.

This checker is intentionally limited to finite arithmetic/finite shell patterns.
It does not construct the 61-vertex parent and does not replace the analytic
core-degree and repivot arguments in COVER_THEOREM.md.
"""
from itertools import combinations, product


def edge(x, y):
    return frozenset((x, y))


def independent_number(vertices, edges):
    best = 0
    for mask in range(1 << len(vertices)):
        chosen = [vertices[i] for i in range(len(vertices)) if mask >> i & 1]
        if all(edge(x, y) not in edges for x, y in combinations(chosen, 2)):
            best = max(best, len(chosen))
    return best


def family_i_partitions():
    result = {}
    for r in (4, 5):
        result[r] = sorted({
            tuple(sorted(row, reverse=True))
            for row in product((1, 2, 3), repeat=r)
            if sum(row) == 11
        })
    assert result[4] == [(3, 3, 3, 2)]
    assert result[5] == [
        (3, 2, 2, 2, 2),
        (3, 3, 2, 2, 1),
        (3, 3, 3, 1, 1),
    ]
    return result


def family_i_excess():
    rows = []
    for E in (407, 408):
        total = 2 * E - 13 * 61
        for r in (4, 5):
            n_rem = 50 - 3 * r
            row_excess = 3 * (11 - r)
            rem_excess = total - row_excess
            rows.append({
                "E": E,
                "r": r,
                "remainder_vertices": n_rem,
                "row_triangle_excess": row_excess,
                "remainder_excess": rem_excess,
                "regular_remainder_lower_bound": n_rem - rem_excess,
            })
            if r == 5:
                # Every remainder vertex must complete a row triangle;
                # then d_F >= 15, so each contributes excess >= 2.
                assert 2 * n_rem > rem_excess
            else:
                # At most rem_excess vertices can be nonregular.
                assert n_rem - rem_excess > 11
    return rows


def family_ii_x2_missing_edge_check():
    V = ("a", "b", "u", "v")
    all_edges = {edge(x, y) for x, y in combinations(V, 2)}
    uv = edge("u", "v")
    rows = []
    for missing in sorted(all_edges - {uv}, key=lambda e: tuple(sorted(e))):
        E4 = all_edges - {missing}
        degree = {
            x: sum(edge(x, y) in E4 for y in V if y != x)
            for x in V
        }
        # With nine outside neighbors, both weight-11 hubs can have
        # internal degree at most 2. This selects only the missing edge ab.
        rows.append({
            "missing_edge": sorted(missing),
            "internal_degrees": degree,
            "compatible_with_both_hubs_degree_at_most_2":
                degree["a"] <= 2 and degree["b"] <= 2,
        })
    survivors = [r for r in rows
                 if r["compatible_with_both_hubs_degree_at_most_2"]]
    assert len(survivors) == 1
    assert survivors[0]["missing_edge"] == ["a", "b"]
    return rows


def adversarial_x3_near_witness():
    # K4-e on {a,b,u,v}, with missing edge au and uv present.
    # Nine independent outside points have types:
    # 4 x {a,v}, 4 x {b,v}, 1 x {a,b}.
    V = ["a", "b", "u", "v"] + [f"r{i}" for i in range(9)]
    E = {
        edge("a", "b"), edge("a", "v"), edge("b", "u"),
        edge("b", "v"), edge("u", "v"),
    }
    types = [("a", "v")] * 4 + [("b", "v")] * 4 + [("a", "b")]
    for x, ns in zip([f"r{i}" for i in range(9)], types):
        for s in ns:
            E.add(edge(x, s))

    t = {"a": 11, "b": 11, "u": 2, "v": 11}
    t.update({f"r{i}": 2 for i in range(9)})
    degree = {
        x: sum(edge(x, y) in E for y in V if y != x)
        for x in V
    }
    g = {x: t[x] - degree[x] for x in V}
    assert min(g.values()) >= 0

    z = len(E)
    G = sum(g.values())
    assert (z, G, z + G) == (23, 7, 30)
    assert sum(t[x] >= 11 for x in V) == 3
    assert independent_number(V, E) == 10

    # K4-freeness.
    k4s = [
        S for S in combinations(V, 4)
        if all(edge(x, y) in E for x, y in combinations(S, 2))
    ]
    assert not k4s

    # EDGE13 on every M-edge.
    assert all(t[x] + t[y] >= 13 for e in E for x, y in [tuple(e)])

    regular = [x for x in V if g[x] == 0]
    assert all(degree[x] not in range(3, 11) for x in regular)

    # For each regular point outside X={a,b,v}, calculate rho exactly.
    # Formula (3): q_y >= d(13-d) + rho = 22 + rho.
    outside_X = ["u"] + [f"r{i}" for i in range(9)]
    rho_by_vertex = {}
    for y in outside_X:
        S = {x for x in V if edge(x, y) in E}
        assert len(S) == 2
        rest = set(V) - S
        e_rest = sum(1 for e in E if e.issubset(rest))
        rho = e_rest + sum(g[x] for x in rest)
        rho_by_vertex[y] = rho
        assert 22 + rho >= 31

    assert set(rho_by_vertex.values()) == {9}
    return {
        "vertices": len(V),
        "edges_z": z,
        "decoration_G": G,
        "q": z + G,
        "alpha_M": independent_number(V, E),
        "K4_count": len(k4s),
        "weights": t,
        "M_degrees": degree,
        "decorations": g,
        "high_set_X": ["a", "b", "v"],
        "regular_outside_points": outside_X,
        "rho_by_regular_outside_point": rho_by_vertex,
        "q_lower_bound_for_each_regular_outside_point": 31,
        "disposition": "excluded by Q=30 in the |X|=3 branch",
    }


def family_ii_rho_check():
    # Standard Family II shell: K_{2,11} plus uv on the low side.
    V = ["a", "b", "u", "v"] + [f"y{i}" for i in range(9)]
    E = set()
    for y in V[2:]:
        E.add(edge("a", y))
        E.add(edge("b", y))
    E.add(edge("u", "v"))
    g = {x: 0 for x in V}
    g["u"], g["v"] = 3, 4
    rho_values = {}
    for y in V[4:]:
        S = {x for x in V if edge(x, y) in E}
        assert S == {"a", "b"}
        rest = set(V) - S
        e_rest = sum(1 for e in E if e.issubset(rest))
        rho = e_rest + sum(g[x] for x in rest)
        rho_values[y] = rho
    assert set(rho_values.values()) == {8}
    # beta=12, d=2: d(13-d)=22, so q_y >= 30.
    assert all(22 + rho == 30 for rho in rho_values.values())
    return {
        "ordinary_lows_checked": len(rho_values),
        "rho_each": 8,
        "repivot_charge_lower_bound_each": 30,
        "decoration_split_example": [3, 4],
    }


def main():
    result = {
        "status": "PASS",
        "family_I": {
            "row_multiplicity_partitions": family_i_partitions(),
            "excess_cases": family_i_excess(),
            "logic": {
                "r5": "35 remainder vertices each need excess >=2; total need >=70",
                "r4": "at least 36 regular remainder vertices form a clique",
            },
        },
        "family_II": {
            "X2_missing_edge_cases": family_ii_x2_missing_edge_check(),
            "ordinary_low_rho": family_ii_rho_check(),
            "pair_argument": (
                "For x in T_i and j != i, x is nonadjacent to v_j and "
                "d_{C_j}(x)=13-1-e(x,T_j)>=12; hence e(x,T_j)=0."
            ),
        },
        "adversarial_near_witness": adversarial_x3_near_witness(),
        "scope": (
            "Independent finite arithmetic and local shell-pattern replay. "
            "Does not certify the analytic EDGE13/INS11 lemmas, 47-core "
            "minimum-degree gate, full 61-vertex theorem, or Lean kernel."
        ),
    }
    import json
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
