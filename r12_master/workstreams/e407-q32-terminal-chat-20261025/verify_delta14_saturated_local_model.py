#!/usr/bin/env python3
"""Verify the explicit 29-point E407 delta=14 saturated local model.

Standard-library only. This checks the finite graph construction, cell-to-edge
bijection, witness packing, and K5-saturation. It does not construct the
18-vertex W side, the 47-core, or the shell-row extension.
"""
from itertools import combinations, product
from collections import defaultdict

SA = set(range(5))
SB = {0, 1, 2, 4, 5}
X = {f"X{i}" for i in SA}
Y = {f"Y{j}" for j in SB}
C1, C2, D, E1, E2 = "C1", "C2", "D", "E1", "E2"
J_vertices = X | Y | {C1, C2, D, E1, E2}

# Cells not shared by an X-permutation and a Y-permutation.
unique_A = {
    (1, 1): ("X0", "E1"), (4, 4): ("X0", "E2"),
    (2, 3): ("X1", "E1"), (5, 6): ("X1", "E2"),
    (3, 5): ("X2", "E1"), (6, 1): ("X2", "E2"),
    (4, 0): ("X3", "E1"), (0, 3): ("X3", "E2"),
    (5, 2): ("X4", "E1"), (1, 5): ("X4", "E2"),
}
unique_B = {
    (5, 3): ("Y0", "C1"), (6, 5): ("Y0", "C2"),
    (4, 2): ("Y1", "C1"), (5, 4): ("Y1", "C2"),
    (3, 1): ("Y2", "C1"), (4, 3): ("Y2", "C2"),
    (1, 6): ("Y4", "C1"), (2, 1): ("Y4", "C2"),
    (0, 5): ("Y5", "C1"), (1, 0): ("Y5", "C2"),
}
unused = {
    (2, 0): ("D", "C1"), (0, 6): ("D", "C2"),
    (6, 4): ("D", "E1"), (3, 2): ("D", "E2"),
}

def edge(u, v):
    return frozenset((u, v))

cell_to_edge = {}
for x, y in product(range(7), repeat=2):
    i = (y - x) % 7
    j = (y - 2*x) % 7
    if i in SA and j in SB:
        e = edge(f"X{i}", f"Y{j}")
    elif i in SA:
        e = edge(*unique_A[(x, y)])
    elif j in SB:
        e = edge(*unique_B[(x, y)])
    else:
        e = edge(*unused[(x, y)])
    cell_to_edge[(x, y)] = e

# The graph is the blow-up of C5 with part sizes 5,5,2,1,2.
J_edges = set()
for i in SA:
    for j in SB:
        J_edges.add(edge(f"X{i}", f"Y{j}"))
for j in SB:
    for c in (C1, C2):
        J_edges.add(edge(f"Y{j}", c))
for c in (C1, C2):
    J_edges.add(edge(c, D))
for e in (E1, E2):
    J_edges.add(edge(D, e))
for i in SA:
    for e in (E1, E2):
        J_edges.add(edge(f"X{i}", e))

assert len(J_vertices) == 15
assert len(J_edges) == 49
assert len(cell_to_edge) == 49
assert len(set(cell_to_edge.values())) == 49
assert set(cell_to_edge.values()) == J_edges

adjJ = {v: set() for v in J_vertices}
for e in J_edges:
    u, v = tuple(e)
    adjJ[u].add(v)
    adjJ[v].add(u)
assert all(not (adjJ[u] & adjJ[v]) for u, v in J_edges)  # triangle-free
assert all(adjJ[u] & adjJ[v] for u, v in combinations(J_vertices, 2)
           if v not in adjJ[u])  # triangle-saturated

# At every J vertex, row, column, and kappa=x+y are all distinct.
incident_cells = defaultdict(list)
for (x, y), e in cell_to_edge.items():
    for v in e:
        incident_cells[v].append((x, y))
for v, cells in incident_cells.items():
    assert len({x for x, y in cells}) == len(cells), (v, "row repeat")
    assert len({y for x, y in cells}) == len(cells), (v, "column repeat")
    assert len({(x+y) % 7 for x, y in cells}) == len(cells), (v, "color repeat")

A = {f"A{x}" for x in range(7)}
B = {f"B{y}" for y in range(7)}
U = A | B | J_vertices
witnesses = {}
for (x, y), e in cell_to_edge.items():
    u, v = tuple(e)
    witnesses[(x, y)] = frozenset({f"A{x}", f"B{y}", u, v})

assert len(U) == 29 and len(witnesses) == 49
assert set().union(*witnesses.values()) == U
assert all(len(Q) == 4 for Q in witnesses.values())
assert all(len(Q1 & Q2) <= 1
           for Q1, Q2 in combinations(witnesses.values(), 2))
for k in range(7):
    cells = [cell for cell in witnesses if sum(cell) % 7 == k]
    Qs = [witnesses[cell] for cell in cells]
    assert len(cells) == 7
    assert len({x for x, y in cells}) == 7
    assert len({y for x, y in cells}) == 7
    assert all(not (Q1 & Q2) for Q1, Q2 in combinations(Qs, 2))

# H[U] = K7(A) dot-union K7(B) dot-union complement(J).
H_edges = set()
for P in (A, B):
    H_edges.update(edge(u, v) for u, v in combinations(P, 2))
all_J_pairs = {edge(u, v) for u, v in combinations(J_vertices, 2)}
H_edges.update(all_J_pairs - J_edges)
assert len(H_edges) == 98
assert all(not any(edge(u, v) in H_edges for u, v in combinations(Q, 2))
           for Q in witnesses.values())

# L = complement(H[U]): the join of independent A, independent B, and J.
L_edges = {edge(u, v) for u, v in combinations(U, 2)} - H_edges
assert len(L_edges) == 308
adjL = {v: set() for v in U}
for e in L_edges:
    u, v = tuple(e)
    adjL[u].add(v)
    adjL[v].add(u)

def is_clique(S):
    return all(v in adjL[u] for u, v in combinations(S, 2))

assert not any(is_clique(S) for S in combinations(U, 5))
for u, v in combinations(U, 2):
    if v in adjL[u]:
        continue
    common = adjL[u] & adjL[v]
    assert any(is_clique(T) for T in combinations(common, 3)), (u, v)

print("E407_DELTA14_SATURATED_LOCAL_MODEL_OK")
print("J: 15 vertices, 49 edges, triangle-free, saturated, non-bipartite")
print("L: 29 vertices, 308 edges, K5-free, K5-saturated, non-four-partite")
print("H[U]: 98 edges, alpha=4; 49 linear witnesses in 7 disjoint color classes")
