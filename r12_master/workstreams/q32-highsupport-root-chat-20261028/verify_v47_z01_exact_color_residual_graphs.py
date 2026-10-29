#!/usr/bin/env python3
"""Exhaustive 7-vertex catalog for the conditional aligned exact-color residual subcase.

Vertices 0,1 / 2,3 / 4,5 are the residual pairs in T1,T2,T3;
vertex 6 is the singleton residual vertex in T0. Edges within a track
part are forbidden. Enumerate all 2^18 cross-part graphs with 9..12 edges,
alpha <= 2, degree >=2 at the six large-track vertices, and T0 degree 3 or 4
(pointwise balanced-coloring cap). Also test whether each graph contains a transversal
K4 plus a K3 on the three large tracks.

This catalog applies only when all ten isolated Type-I K5 components are
single-outside. A source-correct isolated-double placement has an 8-vertex
residual and is audited separately. This is a necessary local relaxation only;
it does not certify global Q32 infeasibility.
"""
from itertools import combinations, product
from collections import Counter

N = 7
part = (0, 0, 1, 1, 2, 2, 3)
edges = [
    (u, v)
    for u in range(N)
    for v in range(u + 1, N)
    if part[u] != part[v]
]
assert len(edges) == 18
edge_bit = {edge: 1 << i for i, edge in enumerate(edges)}

incident = [0] * N
for (u, v), bit in edge_bit.items():
    incident[u] |= bit
    incident[v] |= bit

triple_masks = []
for triple in combinations(range(N), 3):
    mask = 0
    for u, v in combinations(triple, 2):
        mask |= edge_bit.get(tuple(sorted((u, v))), 0)
    triple_masks.append(mask)

base_masks = []
for choice in product((0, 1), repeat=3):
    k4 = [6] + [2 * i + choice[i] for i in range(3)]
    k3 = [2 * i + (1 - choice[i]) for i in range(3)]
    mask = 0
    for clique in (k4, k3):
        for u, v in combinations(clique, 2):
            mask |= edge_bit[tuple(sorted((u, v)))]
    assert mask.bit_count() == 9
    base_masks.append(mask)

graphs_by_gap = Counter()
base_by_gap = Counter()
total_masks_checked = 1 << len(edges)

for graph in range(total_masks_checked):
    e = graph.bit_count()
    if not 9 <= e <= 12:
        continue

    degree = [(graph & incident[v]).bit_count() for v in range(N)]
    if not 3 <= degree[6] <= 4 or any(degree[v] < 2 for v in range(6)):
        continue

    # alpha <= 2 iff every 3-set contains at least one graph edge.
    if any((graph & triple_mask) == 0 for triple_mask in triple_masks):
        continue

    gap = e - 9
    graphs_by_gap[gap] += 1
    has_base = any((graph & base) == base for base in base_masks)
    base_by_gap[(gap, has_base)] += 1

assert graphs_by_gap == Counter({0: 8, 1: 72, 2: 360, 3: 1000})
assert base_by_gap == Counter({
    (0, True): 8,
    (1, True): 72,
    (2, True): 264,
    (2, False): 96,
    (3, True): 520,
    (3, False): 480,
})

print("cross-part edges:", len(edges))
print("all masks checked:", total_masks_checked)
print("graphs by gap:", dict(sorted(graphs_by_gap.items())))
print("K4+K3 base counts:", dict(sorted(base_by_gap.items())))
print("V47_Z01_EXACT_COLOR_RESIDUAL_GRAPH_CATALOG_OK")
print("Scope: single-outside Type-I placement only; necessary relaxation, not global Q32 UNSAT.")
