#!/usr/bin/env python3
"""Independent arithmetic replay for the isolated-double residual branch.

Checks the 8-vertex two-transversal-K4 relaxation, including the pointwise
T0 degree cap (each T0 vertex may receive at most one extra edge). The
source gadget star restriction is stronger still; this is not a full Q32
completion solver. The companion verifier with the same capped model is
verify_v47_z01_isolated_double_residual_graphs.py.
"""
from itertools import product, combinations
from collections import Counter

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
    if choice[0] != 0:  # quotient by swapping the two K4s
        continue
    first = [2 * i + choice[i] for i in range(4)]
    second = [2 * i + (1 - choice[i]) for i in range(4)]
    base = mask_of(clique_edges(first) + clique_edges(second))
    assert base.bit_count() == 12
    extra_indices = [i for i in range(len(edges)) if not (base >> i) & 1]
    assert len(extra_indices) == 12
    bases.append((base, extra_indices))

assert len(bases) == 8
t0_vertices = [v for v in range(N) if part[v] == 3]
assert len(t0_vertices) == 2
graphs_by_gap = Counter()

for gap in range(4):
    graphs = set()
    for base, extra_indices in bases:
        for chosen in combinations(extra_indices, gap):
            # Pointwise saturation: each T0 vertex has base degree 3 and
            # therefore may be incident to at most one extra edge.
            if sum(any(v in edges[i] for v in t0_vertices) for i in chosen) > 1:
                continue
            graph = base
            for i in chosen:
                graph |= 1 << i
            assert graph.bit_count() == 12 + gap
            graphs.add(graph)
    assert len(graphs) == {0: 8, 1: 96, 2: 408, 3: 880}[gap]
    # A second two-K4 base needs at least six cross-base edges, impossible
    # with at most three extras.
    for graph in graphs:
        containing_bases = sum((graph & base) == base for base, _ in bases)
        assert containing_bases == 1
    graphs_by_gap[gap] = len(graphs)

# Isolated-double edge accounting: 9 K4s + K3 contribute 57 H-edges.
assert 9 * 6 + 3 == 57
for gap in range(4):
    assert 57 + (12 + gap) == 69 + gap

# Exceptional x in H, y in H placement: b_s+b_t=3, g=3, six gadget H-H
# edges supplement the K4+K3 interiors (9 edges) in G11.
assert 6 - 3 == 3
assert 9 + 6 == 15
assert 57 + 15 == 72

print("two-K4 bases:", len(bases))
print("globally T0-capped relaxed graph counts:", dict(sorted(graphs_by_gap.items())))
print("isolated-double edge accounting: checked")
print("V47_Z01_ISOLATED_DOUBLE_RESIDUAL_GLOBAL_T0_CAP_OK")
print("Scope: globally T0-capped necessary relaxation only; not global Q32 UNSAT.")
