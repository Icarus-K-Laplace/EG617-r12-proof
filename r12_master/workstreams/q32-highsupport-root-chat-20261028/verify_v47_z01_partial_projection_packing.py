#!/usr/bin/env python3
"""Exhaustive 2x2 block replay for partial residual-projection packing.

Checks every possible intersection of a perfect matching P with a K2,2 block.
Because P is a matching, its block intersection is empty or a subset of one
of the two internal perfect matchings. If nonempty, exactly one internal
matching remains edge-disjoint from P. If empty, both remain available and
at most two edge-disjoint colors can use the projection.
"""
from itertools import combinations

A = (0, 1)
B = (2, 3)
edges = {(a, b) for a in A for b in B}
F0 = frozenset({(0, 2), (1, 3)})
F1 = frozenset({(0, 3), (1, 2)})
assert F0.isdisjoint(F1)
assert F0 | F1 == edges


def is_matching(es):
    seen_left, seen_right = set(), set()
    for a, b in es:
        if a in seen_left or b in seen_right:
            return False
        seen_left.add(a)
        seen_right.add(b)
    return True


# Enumerate every possible P intersection with the block that is itself a
# matching. (There are seven: empty plus the three nonempty subsets of F0/F1.)
valid_intersections = []
for size in range(5):
    for subset in combinations(sorted(edges), size):
        if is_matching(subset):
            valid_intersections.append(frozenset(subset))

assert len(valid_intersections) == 7
for p_block in valid_intersections:
    available = [f for f in (F0, F1) if f.isdisjoint(p_block)]
    if p_block:
        assert len(available) == 1
        max_edge_disjoint_colors = 1
    else:
        assert len(available) == 2
        max_edge_disjoint_colors = 2
    assert len(available) == max_edge_disjoint_colors

print("K2,2 P-intersections checked:", len(valid_intersections))
print("nonempty P-block intersection -> exactly one matching remains")
print("empty P-block intersection -> exactly two complementary matchings remain")
print("V47_Z01_PARTIAL_PROJECTION_PACKING_OK")
print("Scope: local block lemma only; no global Q32 UNSAT claim.")

# Cross-key overlap regression: two distinct 2x2 blocks can select P-disjoint
# matchings that still reuse the same actual edge. Key-local occupancy alone
# would miss this; the edge-level occupancy inequality must reject it.
A1, B1 = {0, 1}, {3, 4}
A2, B2 = {0, 2}, {3, 5}
K1_F0 = frozenset({(0, 3), (1, 4)})
K2_F0 = frozenset({(0, 3), (2, 5)})
P_global = frozenset({(0, 5), (1, 3), (2, 4)})
assert is_matching(K1_F0)
assert is_matching(K2_F0)
assert is_matching(P_global)
assert not (K1_F0 & P_global)
assert not (K2_F0 & P_global)
assert K1_F0 != K2_F0
assert K1_F0 & K2_F0 == {(0, 3)}
print("cross-key overlap regression: caught shared edge (0, 3)")
print("Key-local constraints alone are insufficient; edge-level occupancy is required.")
