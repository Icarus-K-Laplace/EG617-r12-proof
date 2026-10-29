#!/usr/bin/env python3
"""Finite replay for V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md.

Enumerates the two-transversal-K4 local relaxation for the eight-vertex
isolated-double branch. It does not enumerate source gadget placements or
prove global Q32 infeasibility.
"""
from itertools import product, combinations
from math import comb

N = 8
part = (0, 0, 1, 1, 2, 2, 3, 3)
edges = [(u, v) for u in range(N) for v in range(u + 1, N)
         if part[u] != part[v]]
assert len(edges) == 24
edge_index = {edge: i for i, edge in enumerate(edges)}

def mask_of(edge_set):
    mask = 0
    for u, v in edge_set:
        mask |= 1 << edge_index[tuple(sorted((u, v)))]
    return mask

def clique_edges(vertices):
    return list(combinations(vertices, 2))

bases = []
for choice in product((0, 1), repeat=4):
    # Quotient by swapping the two K4s.
    if choice[0] != 0:
        continue
    first = [2 * i + choice[i] for i in range(4)]
    second = [2 * i + (1 - choice[i]) for i in range(4)]
    base = mask_of(clique_edges(first) + clique_edges(second))
    assert base.bit_count() == 12
    extra_indices = [i for i in range(len(edges)) if not (base >> i) & 1]
    assert len(extra_indices) == 12
    bases.append((base, extra_indices))

assert len(bases) == 8
for gap in range(4):
    graphs = set()
    for base, extra_indices in bases:
        for chosen in combinations(extra_indices, gap):
            graph = base
            for i in chosen:
                graph |= 1 << i
            assert graph.bit_count() == 12 + gap
            graphs.add(graph)
    assert len(graphs) == 8 * comb(12, gap)
    # No second two-K4 base is possible with at most three cross-base edges:
    # a distinct transversal K4 needs at least three such edges and its
    # complementary K4 needs another three.
    for graph in graphs:
        containing_bases = sum((graph & base) == base for base, _ in bases)
        assert containing_bases == 1

# Isolated-double edge accounting: 9 K4s + K3 contribute 57 H-edges.
assert 9 * 6 + 3 == 57
for gap in range(4):
    assert 57 + (12 + gap) == 69 + gap

# In the exceptional x in H, y in H placement, the source ledger gives
# b_s+b_t=3, g=3, and six H-H gadget edges over K4+K3 interiors (9 edges).
assert 6 - 3 == 3
assert 9 + 6 == 15
assert 57 + 15 == 72

print("two-K4 bases:", len(bases))
print("relaxed graph counts:", {g: 8 * comb(12, g) for g in range(4)})
print("isolated-double edge accounting: checked")
print("V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT_OK")
print("Scope: source-derived residual accounting and local relaxation only; not global Q32 UNSAT.")
