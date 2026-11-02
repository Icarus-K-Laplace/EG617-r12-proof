#!/usr/bin/env python3
"""Arithmetic/finite-structure checks for the h13 q=30 COVER audit.

This is NOT a graph search and NOT a proof-assistant formalization. It checks
small integer consequences used in the analytic q=30 classification and its
Family I/II contradictions.
"""
from itertools import combinations, product
import json


def check_k4_minus_edge():
    records = []
    V = range(4)
    for missing in combinations(V, 2):
        deg = {v: 3 - int(v in missing) for v in V}
        degree_two = {v for v in V if deg[v] == 2}
        assert degree_two == set(missing)
        records.append({"missing_edge": list(missing),
                        "degrees": [deg[v] for v in V]})
    assert len(records) == 6
    return records


def check_d10_branch():
    # S has ten vertices, B has three; S and B are each M-independent.
    # Every B vertex is regular and has degree at most ten.
    z_min = 22
    active_S_min = (z_min + 2) // 3
    assert active_S_min == 8  # z <= 3 * number of active S vertices
    assert 4 * active_S_min > 30
    # Thus some active s has t_s <= 3; an adjacent regular b must have
    # d_M(b) >= 13 - t_s >= 10, hence exactly ten.
    # That b sees all ten S vertices, so every t_s >= 3; sum(t_s)=30.
    assert 10 * 3 == 30
    # Every active B vertex adjacent to a hub of weight 3 has degree >=10.
    assert 13 - 3 == 10
    # z>=22 forces all three B vertices active; the state is K_{3,10}.
    assert 3 * 10 >= z_min
    return {
        "active_S_vertices_at_least": active_S_min,
        "forced_S_weights": [3] * 10,
        "forced_B_degrees": [10] * 3,
        "result": "K_{3,10}, all decorations zero"
    }


def check_X2_branch():
    # The four-set is K4-e. The two high points a,b have weight 11.
    # The other two u,v have weight <11 and internal degree >=2.
    # Nine outside points are independent, regular, and have degree <=2.
    assert 11 + 1 < 13   # degree-one outside point impossible at a hub
    assert 10 + 2 < 13   # degree-two point cannot meet u or v
    # Every active outside point must meet both hubs.
    # z = 5 + 2k >= 22 forces k=9.
    k_min = (22 - 5 + 1) // 2
    assert k_min == 9
    assert 5 + 2 * k_min == 23
    # Each hub has internal degree 2 plus nine outside neighbors.
    assert 2 + 9 == 11
    # The other two points have internal degree 3 each, with decorations
    # summing to 13 - 6 = 7; neither decoration may be zero.
    assert 13 - 3 - 3 == 7
    return {
        "active_outside_vertices": 9,
        "outside_row_type": "both hubs",
        "hub_M_degrees": [11, 11],
        "hub_decorations": [0, 0],
        "exceptional_low_decorations_sum": 7,
        "missing_edge_of_K4_minus_edge": "between the two hubs"
    }


def check_family_I():
    # Row classes have multiplicities c_i in {1,2,3}, sum 11.
    partitions = {
        str(r): sorted({tuple(sorted(row, reverse=True))
                        for row in product((1, 2, 3), repeat=r)
                        if sum(row) == 11})
        for r in (4, 5)
    }
    assert partitions["4"] == [(3, 3, 3, 2)]
    assert partitions["5"] == [
        (3, 2, 2, 2, 2),
        (3, 3, 2, 2, 1),
        (3, 3, 3, 1, 1)
    ]
    rows = []
    for E in (407, 408):
        total_excess = 2 * E - 13 * 61
        for r in (4, 5):
            n_rem = 50 - 3 * r
            row_excess = 3 * (11 - r)
            rem_excess = total_excess - row_excess
            if r == 5:
                assert 2 * n_rem > rem_excess
            else:
                assert n_rem - rem_excess > 11
            rows.append({
                "E": E, "row_classes": r,
                "remainder_vertices": n_rem,
                "remainder_excess": rem_excess
            })
    return {"row_class_partitions": partitions,
            "excess_cases": rows}


def check_family_II():
    # Ten pairwise disjoint, pairwise anticomplete edges have an
    # independent transversal of size ten.
    assert 10 > 5
    # In the q30 view at v_i, each hub x in T_i has d_F(x)=13,
    # exactly one neighbor in K (v_i), and none in {u,v}.
    # In the q30 core at v_j, j != i:
    # d_Cj(x)=13-1-e(x,T_j)>=12, hence e(x,T_j)=0.
    assert 13 - 1 == 12
    return {
        "number_of_pairs": 10,
        "cross_pair_edges_forbidden_by_core_min_degree": True,
        "independent_transversal_size": 10
    }


def check_heavy_set_bounds():
    # Turan ex(n,K4)=floor(n^2/3).
    assert (8 * 8) // 3 == 21
    assert (7 * 7) // 3 == 16
    # K4 case: q_y >= 53 - (t_a+t_b), with each K4 weight <=12.
    assert 53 - 24 == 29
    # X=3: active outside point has degree2 and q_y >=22+9=31.
    assert 22 + 9 == 31
    # X=1, heavy weight >=12: equality on 5-set has at most8 edges;
    # each of eight remaining vertices can add at most one edge to x.
    assert 8 + 8 == 16 < 22


def main():
    check_heavy_set_bounds()
    result = {
        "status": "PASS",
        "K4_minus_edge": check_k4_minus_edge(),
        "d10_branch": check_d10_branch(),
        "X2_branch": check_X2_branch(),
        "Family_I": check_family_I(),
        "Family_II": check_family_II(),
        "scope": (
            "Finite arithmetic and six K4-minus-edge degree patterns only. "
            "The graph-theoretic reductions, EDGE13/INS11, row-class "
            "compatibility, and parent-core minimum-degree theorems remain "
            "analytic dependencies; this script does not prove them."
        )
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
