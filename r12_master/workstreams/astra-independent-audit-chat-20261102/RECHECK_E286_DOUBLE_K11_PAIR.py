#!/usr/bin/env python3
"""Independent intersection-parameter audit of E286 Section 11.

The script does not import project code. It derives degree lower bounds from:
(1) the two blocker-completeness relations A--B and A'--B';
(2) the two K11 internal degrees;
(3) adjacency/nonadjacency of the two mixed points; and
(4) the T=8 nonedge common-neighbor inequality.

Run: python -B RECHECK_E286_DOUBLE_K11_PAIR.py
"""
from itertools import product
import json


def f11(a, b):
    return max(0, 10 - a - b) + a * max(0, b - 2) + b * max(0, a - 2)


def charge_lower(a, ap, b, bp, r, s, adjacent):
    """Lower bound for fixed sizes/intersections.

    X,Y are the two K11s. A,A' subset X; B,B' subset Y.
    r=|A intersect A'|, s=|B intersect B'|.
    """
    eps_x = (
        (a-r) * max(0, b-1)
        + (ap-r) * max(0, bp-1)
        + r * max(0, b+bp-s-2)
    )
    eps_y = (
        (b-s) * max(0, a-1)
        + (bp-s) * max(0, ap-1)
        + s * max(0, a+ap-r-2)
    )
    eps_z = max(0, 10-a-b+int(adjacent))
    eps_zp = max(0, 10-ap-bp+int(adjacent))
    point_charge = eps_z + eps_zp

    common_x = 11-a-ap+r
    common_y = 11-b-bp+s

    if adjacent:
        # Ten common vertices in either K11 would create a K12.
        if common_x >= 10 or common_y >= 10:
            return None
    else:
        # At T=8, nonadjacent z,z' satisfy c(z,z')<=3+eps(z)+eps(z').
        point_charge = max(point_charge, common_x+common_y-3)

    return eps_x + eps_y + point_charge, {
        "X_vertex_excess": eps_x,
        "Y_vertex_excess": eps_y,
        "point_excess": point_charge,
        "individual_point_bounds": [eps_z, eps_zp],
        "common_neighbors_in_X_lower": common_x,
        "common_neighbors_in_Y_lower": common_y,
    }


def main():
    states = []
    adjacency_options = 0
    forced_nonadjacency = 0
    nonadj_values = []
    adjacent_values = []

    for a, ap, b, bp in product(range(1, 12), repeat=4):
        # T=8 implies each individual disjoint f11 charge is at most 8.
        if f11(a, b) > 8 or f11(ap, bp) > 8:
            continue
        for r in range(max(0, a+ap-11), min(a, ap)+1):
            for s in range(max(0, b+bp-11), min(b, bp)+1):
                nonadj = charge_lower(a, ap, b, bp, r, s, False)
                nonadj_values.append(nonadj[0])
                options = [{"relation": "nonadjacent",
                            "lower_bound": nonadj[0]}]
                adj = charge_lower(a, ap, b, bp, r, s, True)
                if adj is not None:
                    adjacency_options += 1
                    adjacent_values.append(adj[0])
                    options.append({"relation": "adjacent",
                                    "lower_bound": adj[0]})
                else:
                    forced_nonadjacency += 1
                best = min(options, key=lambda item: item["lower_bound"])
                states.append({
                    "a": a, "a_prime": ap, "b": b, "b_prime": bp,
                    "intersection_A": r, "intersection_B": s,
                    "options": options, "best": best,
                })

    minimum = min(row["best"]["lower_bound"] for row in states)
    equality = [
        {k: row[k] for k in (
            "a", "a_prime", "b", "b_prime",
            "intersection_A", "intersection_B"
        )} | {"best_relation": row["best"]["relation"]}
        for row in states if row["best"]["lower_bound"] == minimum
    ]

    assert len(states) == 3387
    assert adjacency_options == 2748
    assert forced_nonadjacency == 639
    assert min(nonadj_values) == 15
    assert min(adjacent_values) == 14
    assert minimum == 14
    assert len(equality) == 5

    print(json.dumps({
        "status": "PASS",
        "enumerated_intersection_states": len(states),
        "adjacency_allowed_states": adjacency_options,
        "states_forcing_nonadjacency_by_K12": forced_nonadjacency,
        "minimum_nonadjacent_charge_bound": min(nonadj_values),
        "minimum_adjacent_charge_bound": min(adjacent_values),
        "minimum_over_all_allowed_relations": minimum,
        "equality_parameter_states": equality,
        "scope": (
            "Independent finite verification of the local Section 11 charge "
            "inequalities; not a proof of the global E286 theorem."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
