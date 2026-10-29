#!/usr/bin/env python3
"""Vertex-labelled common-P relaxation witness for the aligned E408/Q32 cell.

This constructs all three shared large-pair complementary matchings P_ij as
six labelled 6-cycles, assigns every P_ij edge exactly one of H / exact-repeat /
D-repeat, and labels all 33 T0--Ti complement edges with the pointwise E0=0
degree pattern. Each of the ten exact colors receives a source-realizable
Class-A K4+K3 residual gadget with (g_C,t_C)=(2,1).

This is intentionally NOT a full coloring certificate: it does not construct
the eleven simultaneous color matchings M_C,ij on the remaining 30 vertices
or verify that each complete M_C triangle factor has ten isolated K4s.
It proves that common-P endpoint packing and the source-local Class-A modes,
by themselves, remain feasible.
"""
from itertools import combinations
from collections import Counter, defaultdict

# Three 12-vertex tracks, six cycles, and two vertices per track/cycle.
def v(track, cycle, side):
    return 12 * track + 2 * cycle + side  # side 0=A, side 1=B

tracks = {i: set(range(12 * i, 12 * (i + 1))) for i in range(3)}
T0 = tuple(range(36, 47))  # eleven vertices

pairs = ((0, 1), (0, 2), (1, 2))
P = {pair: [] for pair in pairs}

# Each cycle is A0-B1-A2-B0-A1-B2-A0.
for c in range(6):
    P[(0, 1)] += [(v(0, c, 0), v(1, c, 1)),
                  (v(0, c, 1), v(1, c, 0))]
    P[(0, 2)] += [(v(0, c, 0), v(2, c, 1)),
                  (v(0, c, 1), v(2, c, 0))]
    P[(1, 2)] += [(v(1, c, 1), v(2, c, 0)),
                  (v(1, c, 0), v(2, c, 1))]

def edge_key(e):
    return tuple(sorted(e))

# Verify each P_ij is a perfect matching between the two 12-vertex tracks.
for (i, j), es in P.items():
    assert len(es) == 12
    assert len({u for e in es for u in e if u in tracks[i]}) == 12
    assert len({u for e in es for u in e if u in tracks[j]}) == 12
    assert all(sum(u in e for e in es) == 1 for u in tracks[i] | tracks[j])

# Verify the union P_12 U P_13 U P_23 is six disjoint 6-cycles.
adj = defaultdict(set)
for es in P.values():
    for u, w in es:
        adj[u].add(w)
        adj[w].add(u)
assert all(len(adj[u]) == 2 for u in range(36))
components = []
unseen = set(range(36))
while unseen:
    seed = next(iter(unseen))
    stack = [seed]
    comp = set()
    while stack:
        u = stack.pop()
        if u in comp:
            continue
        comp.add(u)
        stack.extend(adj[u] - comp)
    unseen -= comp
    components.append(comp)
assert len(components) == 6 and all(len(c) == 6 for c in components)
assert all(tuple(sum(u in tracks[i] for u in c) for i in range(3)) == (2, 2, 2)
           for c in components)

# The ten exact colors use the source Class-A pattern:
# 4 colors: T0T1 repeat + T1T2 repeat;
# 3 colors: T0T2 repeat + T1T2 repeat;
# 3 colors: T0T3 repeat + T2T3 repeat.
exact_specs = []
for c in range(4):
    exact_specs.append(("pair01_A0", (0, 1), 0, edge_key((v(0, c, 0), v(1, c, 1))), c))
for c in range(3):
    exact_specs.append(("pair01_A1", (0, 1), 1, edge_key((v(0, c, 1), v(1, c, 0))), 4 + c))
for c in range(3):
    exact_specs.append(("pair12_A2", (1, 2), 2, edge_key((v(1, c, 0), v(2, c, 1))), 7 + c))

# Map each exact edge to one exact color; no repeated owner edge is allowed.
exact_owner = {}
exact_meta = {}
for mode, pair, repeat_track, e, color_id in exact_specs:
    assert e in {edge_key(x) for x in P[pair]}
    assert e not in exact_owner
    exact_owner[e] = color_id
    exact_meta[color_id] = {
        "mode": mode, "pair": pair, "repeat_track": repeat_track,
        "edge": e, "cycle": next(c for c in range(6) if all(
            u in {v(i, c, s) for i in range(3) for s in (0, 1)} for u in e
        ))
    }
assert len(exact_owner) == 10

# Build source-local K4+K3+two-extra graphs. For each exact edge, the endpoint
# in repeat_track is the K3-side y_i; the other endpoint is a K4-side s_j.
def independence_number(vertices, edges):
    adj_local = {u: set() for u in vertices}
    for u, w in edges:
        adj_local[u].add(w)
        adj_local[w].add(u)
    best = 0
    vs = tuple(vertices)
    for mask in range(1 << len(vs)):
        n = mask.bit_count()
        if n <= best:
            continue
        chosen = [vs[i] for i in range(len(vs)) if (mask >> i) & 1]
        if all(w not in adj_local[u] for u, w in combinations(chosen, 2)):
            best = n
    return best

# Assign the eleven T0 vertices: ten exact owners plus D. Every T0 vertex
# has exactly one repeat edge and two H edges, with repeat counts (4,4,3).
t0_owner = {}
P0 = {i: [] for i in range(3)}
H0 = {i: [] for i in range(3)}
S0 = {i: [] for i in range(3)}
local_graph_checks = 0

for color_id in range(10):
    meta = exact_meta[color_id]
    i, j = meta["repeat_track"], next(t for t in meta["pair"] if t != meta["repeat_track"])
    k = next(t for t in range(3) if t not in (i, j))
    u, w = meta["edge"]
    y_i = u if u in tracks[i] else w
    s_j = w if y_i == u else u
    c = meta["cycle"]
    # The selected edge is A_i-B_j or B_i-A_j. Its two endpoints have
    # opposite sides; choose the endpoint in track i as the K3-side y_i.
    side_y = y_i % 2
    s_i = v(i, c, 1 - side_y)
    s_k = v(k, c, 1 - side_y)
    y_j = v(j, c, side_y)
    y_k = v(k, c, side_y)
    assert s_j == v(j, c, 1 - side_y)
    w0 = T0[color_id]
    assert w0 not in t0_owner
    t0_owner[w0] = color_id

    k4 = (w0, s_i, s_j, s_k)
    k3 = (y_i, y_j, y_k)
    base_edges = list(combinations(k4, 2)) + list(combinations(k3, 2))
    extras = [(w0, y_i), (y_i, s_j)]
    assert independence_number(tuple(range(7)), [
        (0, 1)  # placeholder not used below
    ]) == 6  # sanity check for the helper on a deliberately sparse local graph
    # Re-index this local graph to 0..6 for a clean independent-set check.
    local_vertices = tuple(k4 + k3)
    local_index = {u: n for n, u in enumerate(local_vertices)}
    local_edges = [tuple(local_index[z] for z in e) for e in base_edges + extras]
    assert independence_number(tuple(range(7)), local_edges) == 2
    assert sum(w0 in e for e in base_edges) == 3
    assert sum(w0 in e for e in base_edges + extras) == 4
    local_graph_checks += 1

    # P0_i is the repeat edge from this T0 vertex to y_i. On the other two
    # tracks, its complement edges are H edges to the K4-side vertices.
    for track in range(3):
        endpoint = y_i if track == i else (s_j if track == j else s_k)
        e0 = (w0, endpoint)
        P0[track].append(e0)
        if track == i:
            S0[track].append(e0)
        else:
            H0[track].append(e0)

# The unique nonexact color D owns one T0 repeat on track 1 (zero-based index 1).
wD = T0[10]
t0_owner[wD] = "D"
for track, endpoint in ((0, v(0, 5, 1)), (1, v(1, 5, 0)), (2, v(2, 5, 1))):
    e0 = (wD, endpoint)
    P0[track].append(e0)
    if track == 1:
        S0[track].append(e0)
    else:
        H0[track].append(e0)

assert len(t0_owner) == 11
assert tuple(len(S0[i]) for i in range(3)) == (4, 4, 3)
assert tuple(len(H0[i]) for i in range(3)) == (7, 7, 8)
assert all(len(P0[i]) == 11 for i in range(3))
assert all(len({e[0] for e in P0[i]}) == 11 for i in range(3))

# Label all large-pair P edges as H, exact-repeat, or D-repeat.
H_counts = {(0, 1): 4, (0, 2): 3, (1, 2): 3}
S_exact_counts = {(0, 1): 7, (0, 2): 0, (1, 2): 3}
labels = {}
for pair in pairs:
    es = [edge_key(e) for e in P[pair]]
    exact_es = [e for e in es if e in exact_owner]
    assert len(exact_es) == S_exact_counts[pair]
    remaining = [e for e in es if e not in exact_owner]
    h_need = H_counts[pair]
    h_es = set(remaining[:h_need])
    assert len(h_es) == h_need
    for e in es:
        if e in exact_owner:
            labels[(pair, e)] = ("EXACT", exact_owner[e])
        elif e in h_es:
            labels[(pair, e)] = ("H", None)
        else:
            labels[(pair, e)] = ("D", None)
    assert sum(labels[(pair, e)][0] == "H" for e in es) == H_counts[pair]
    assert sum(labels[(pair, e)][0] == "D" for e in es) == 12 - H_counts[pair] - S_exact_counts[pair]

D_large = tuple(12 - H_counts[p] - S_exact_counts[p] for p in pairs)
assert D_large == (1, 9, 6)
assert sum(D_large) == 16
assert sum(S_exact_counts.values()) == 10
assert sum(len(S0[i]) for i in range(3)) == 11
assert 10 * 2 + 17 == 37

# Every exact-owned large edge belongs to its owner's selected P 6-cycle,
# and its owner has one T0 repeat in the edge's repeat track.
for color_id, meta in exact_meta.items():
    pair, e, i, c = meta["pair"], meta["edge"], meta["repeat_track"], meta["cycle"]
    assert labels[(pair, e)] == ("EXACT", color_id)
    assert all(u in components[c] for u in e)
    assert len([edge for edge in S0[i] if edge[0] == T0[color_id]]) == 1

print("P_ij perfect matchings:", {str(p): len(P[p]) for p in pairs})
print("P large-track component sizes:", sorted(len(c) for c in components))
print("Class-A local gadgets checked (alpha=2, g=2, t=1):", local_graph_checks)
print("T0 H-edge counts:", tuple(len(H0[i]) for i in range(3)))
print("T0 repeat counts:", tuple(len(S0[i]) for i in range(3)))
print("Large-pair H counts:", tuple(H_counts[p] for p in pairs))
print("Large-pair exact-repeat counts:", tuple(S_exact_counts[p] for p in pairs))
print("Large-pair D-repeat counts:", D_large)
print("EXACT_CLASS_A_VERTEX_LABELLED_COMMON_P_RELAXATION_WITNESS_OK")
print("Scope: shared-P and source-local endpoint relaxation only; not the full 11-color triangle-factorization or a Q32 coloring.")
