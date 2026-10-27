#!/usr/bin/env python3
"""Verify an explicit realization of the abstract 96-edge endpoint kernel.

This proves only that the current abstract kernel
    K_{4,4,4,4} = 2 K4 + 24 K3 + 3 four-edge matchings
with the required selected-color grouping is combinatorially feasible.
It is therefore an adversarial audit: this kernel alone cannot be used as a
contradiction. It does NOT realize the full Q33 contextual graph.
"""
from itertools import combinations

PART = {c: i for i, c in enumerate("ABCD")}


def vertex(name):
    return PART[name[0]], int(name[1])


def clique_edges(block):
    return {tuple(sorted((vertex(a), vertex(b)))) for a, b in combinations(block, 2)}


K4_GROUPS = [
    [("A0", "B0", "C0", "D0")],
    [("A2", "B3", "C0", "D1")],
]

TRI_GROUPS = [
    [("B2", "C2", "D1"), ("B3", "C3", "D3"), ("A2", "C1", "D2")],
    [("B0", "C3", "D2"), ("B1", "C2", "D3"), ("A1", "B2", "D0")],
    [("A1", "C1", "D1"), ("A2", "C2", "D0"), ("A3", "B2", "C0")],
    [("A0", "B1", "D1"), ("A3", "B3", "D2"), ("A2", "B2", "C3")],
    [("B1", "C0", "D2"), ("A2", "B0", "D3"), ("A0", "B3", "C2")],
    [("B3", "C1", "D0"), ("A1", "C0", "D3"), ("A3", "C3", "D1")],
    [("A0", "B2", "D2"), ("A1", "B1", "C3"), ("A3", "B0", "C1")],
    [("A0", "C1", "D3"), ("A3", "B1", "D0"), ("A1", "B0", "C2")],
]

MATCHINGS = [
    [("A1", "B3"), ("A2", "B1"), ("B2", "D3"), ("C3", "D0")],
    [("A0", "C3"), ("A3", "D3"), ("B2", "C1"), ("C2", "D2")],
    [("A3", "C2"), ("A1", "D2"), ("B1", "C1"), ("B0", "D1")],
]


def main():
    all_edges = {
        tuple(sorted(((p, i), (q, j))))
        for p, q in combinations(range(4), 2)
        for i in range(4)
        for j in range(4)
    }
    assert len(all_edges) == 96

    pieces = []

    # Two gadget-selected exact colors: one K4 plus three triangles, all
    # vertex-disjoint within the color. Six other selected colors: three
    # vertex-disjoint triangles each.
    for g, tris in enumerate(TRI_GROUPS):
        used_vertices = []
        if g < 2:
            assert len(K4_GROUPS[g]) == 1
            block = K4_GROUPS[g][0]
            assert len({vertex(x)[0] for x in block}) == 4
            used_vertices.extend(block)
            pieces.append((f"K4-{g}", clique_edges(block)))
        assert len(tris) == 3
        for j, tri in enumerate(tris):
            assert len({vertex(x)[0] for x in tri}) == 3
            used_vertices.extend(tri)
            pieces.append((f"T-{g}-{j}", clique_edges(tri)))
        assert len(used_vertices) == len(set(used_vertices)), (g, used_vertices)

    # Three four-edge matching classes.
    assert len(MATCHINGS) == 3
    for c, matching in enumerate(MATCHINGS):
        assert len(matching) == 4
        endpoints = [x for edge in matching for x in edge]
        assert len(endpoints) == len(set(endpoints)), (c, matching)
        edges = {tuple(sorted((vertex(a), vertex(b)))) for a, b in matching}
        assert len(edges) == 4
        pieces.append((f"M-{c}", edges))

    union = set()
    for label, edges in pieces:
        assert union.isdisjoint(edges), (label, union & edges)
        union |= edges

    assert union == all_edges
    assert len(union) == 96
    assert sum(len(e) for _, e in pieces) == 96

    print("PASS: abstract Q33 endpoint kernel is FEASIBLE")
    print("partition: 2 K4 + 24 K3 + 3 M4 = 96 edges")
    print("selected-color grouping: 2*(K4+3 disjoint K3) + 6*(3 disjoint K3)")
    print("all three M4 classes are matchings; all 96 edges are used exactly once")
    print("Implication: this abstract endpoint kernel is NOT itself a contradiction.")
    print("Scope: incidence kernel only; no claim of a full Q33 graph realization.")


if __name__ == "__main__":
    main()
