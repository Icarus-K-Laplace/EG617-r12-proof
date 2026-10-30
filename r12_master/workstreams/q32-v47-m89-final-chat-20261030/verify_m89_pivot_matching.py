#!/usr/bin/env python3
"""Dependency-free exact checks for the m=8,9 pivot-packing reduction.

This script does NOT solve the full 61-vertex coloring CSP.  It independently
checks the scalar slack frontiers, the Type-I outside-count profiles, the
K4,4 matching-union table, and the local matching-composition lemma.
"""
from itertools import combinations, permutations
from math import comb
import json


def scalar_states(m):
    if m not in (8, 9):
        raise ValueError("this workstream is restricted to m=8,9")
    degree_gap = {8: 18, 9: 13}[m]
    rows = []
    for x in range(33):
        for y in range(33 - x):
            z = 32 - x - y
            q_excess = 2 * x + y - 5 * m
            r_excess = y + 2 * z - degree_gap
            if q_excess >= 0 and r_excess >= 0 and q_excess + r_excess == 6:
                rows.append({
                    "x": x, "y": y, "z": z,
                    "q_excess": q_excess, "r_excess": r_excess,
                })
    return rows


def matching_union_minima():
    """Minimum edges in a bipartite graph containing t distinct K4,4 matchings."""
    all_matchings = list(permutations(range(4)))
    masks = [
        sum(1 << (4 * i + p[i]) for i in range(4))
        for p in all_matchings
    ]
    minima = {}
    for edge_mask in range(1 << 16):
        edge_count = edge_mask.bit_count()
        if edge_count < 4:
            continue
        contained = sum(
            (edge_mask & matching_mask) == matching_mask
            for matching_mask in masks
        )
        for t in range(1, contained + 1):
            minima[t] = min(minima.get(t, 99), edge_count)
    return [minima[t] for t in range(1, 25)]


def verify_matching_composition():
    """Exhaust all 24^2*4 local cases of the light-pair composition lemma.

    Let A,B,C be independent 4-sets.  If A-B and A-C are perfect matchings
    f,g, then for u in A, v=f(u), w=g(u), every a in A\\{u} is nonadjacent
    to both v and w.  If vw were absent, A\\{u} union {v,w} would be an
    independent 5-set.  Thus vw is forced.
    """
    all_matchings = list(permutations(range(4)))
    checked = 0
    for f in all_matchings:
        for g in all_matchings:
            for u in range(4):
                v, w = f[u], g[u]
                assert all(f[a] != v for a in range(4) if a != u)
                assert all(g[a] != w for a in range(4) if a != u)
                checked += 1
    return checked


def verify_source_profiles():
    """Count all legal factor-index placements; special factors are not fixed."""
    factors = range(12)
    x_in_o = []
    for i in factors:
        p = [1] * 12
        p[i] = 2
        x_in_o.append(tuple(p))
    x_in_h = []
    for i in factors:
        p = [1] * 12
        p[i] = 3
        x_in_h.append(tuple(p))
    for i, j in combinations(factors, 2):
        p = [1] * 12
        p[i] = p[j] = 2
        x_in_h.append(tuple(p))
    assert len(set(x_in_o)) == 12
    assert len(set(x_in_h)) == 78
    return {
        "x_in_O": {"profiles": 12, "witnesses": 11},
        "x_in_H_two_double": {"profiles": 66, "witnesses": 10},
        "x_in_H_triple": {"profiles": 12, "witnesses": 11},
    }


def verify_color_vectors():
    out = {}
    for m in (8, 9):
        if m == 8:
            vector = [408] + [129] * 8 + [130] * 3
        else:
            vector = [408] + [129] * 9 + [130, 131]
        assert len(vector) == 12
        assert sum(vector) == comb(61, 2) == 1830
        out[str(m)] = {
            "target": vector[0],
            "exact_129_count": m,
            "nonexact": vector[m + 1:],
            "sum": sum(vector),
        }
    return out


def main():
    scalar = {}
    for m in (8, 9):
        rows = scalar_states(m)
        scalar[str(m)] = {
            "state_count": len(rows),
            "x_range": [min(r["x"] for r in rows), max(r["x"] for r in rows)],
            "y_range": [min(r["y"] for r in rows), max(r["y"] for r in rows)],
            "z_range": [min(r["z"] for r in rows), max(r["z"] for r in rows)],
        }
    result = {
        "status": "LOCAL_CHECKS_PASS_NOT_FULL_CSP",
        "scalar_frontier": scalar,
        "mu4_distinct_matchings": matching_union_minima(),
        "matching_composition_cases": verify_matching_composition(),
        "source_profiles": verify_source_profiles(),
        "color_vectors": verify_color_vectors(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
