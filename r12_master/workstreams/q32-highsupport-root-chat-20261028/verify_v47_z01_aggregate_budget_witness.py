#!/usr/bin/env python3
"""Audit that scalar track-pair budgets alone do not close aligned z=0,1 Q32.

The witness is deliberately an aggregate relaxation, not a graph completion:
it respects the exact degree-ledger equations and uses ten copies of an explicit
source-realizable local class-A mode, but it does not identify shared global
vertices or enforce the common-P endpoint packing across colors.
"""
from itertools import combinations, product
from collections import Counter

N = 7
part = (0, 0, 1, 1, 2, 2, 3)  # T1,T2,T3 each size 2; T0 singleton
edges = [(u, v) for u in range(N) for v in range(u + 1, N)
         if part[u] != part[v]]
edge_bit = {e: 1 << i for i, e in enumerate(edges)}

def mask_of(es):
    out = 0
    for e in es:
        out |= edge_bit[tuple(sorted(e))]
    return out

def alpha(mask, vertices=tuple(range(N))):
    adj = {v: set() for v in vertices}
    for (u, v), bit in edge_bit.items():
        if mask & bit and u in adj and v in adj:
            adj[u].add(v)
            adj[v].add(u)
    best = 0
    vs = tuple(vertices)
    for subset in range(1 << len(vs)):
        size = subset.bit_count()
        if size <= best:
            continue
        chosen = [vs[i] for i in range(len(vs)) if (subset >> i) & 1]
        if all(v not in adj[u] for u, v in combinations(chosen, 2)):
            best = size
    return best

def baseline(switches, t0_choices):
    big = ((0, 1), (2, 3), (4, 5))
    out = []
    for (i, j), switch in zip(((0, 1), (0, 2), (1, 2)), switches):
        for a in range(2):
            out.append((big[i][a], big[j][a ^ switch]))
    for i, choice in enumerate(t0_choices):
        out.append((6, big[i][choice]))
    return out

def class_of(base):
    mask = mask_of(base)
    big_alpha = alpha(mask, tuple(range(6)))
    full_alpha = alpha(mask)
    if big_alpha == 2 and full_alpha == 3:
        return "B"
    if big_alpha == 2 and full_alpha == 2:
        return "A"
    if big_alpha == 3 and full_alpha == 3:
        return "C"
    if big_alpha == 3 and full_alpha == 4:
        return "D"
    raise AssertionError((big_alpha, full_alpha))

def admissible_extra(extra):
    if sum(6 in e for e in extra) > 1:
        return False
    for i in range(4):
        for j in range(i + 1, 4):
            used = set()
            for u, v in extra:
                if {part[u], part[v]} == {i, j}:
                    if u in used or v in used:
                        return False
                    used.update((u, v))
    return True

# Abstract catalog audit: all nine one-large-pair/one-T0-pair vectors occur
# in some class-B baseline repaired by exactly two edges while alpha <= 2.
# This catalog fact is not itself a source-placement classification.
large_pairs = ((0, 1), (0, 2), (1, 2))
t0_pairs = ((0, 3), (1, 3), (2, 3))
support = set()
support_counts = Counter()
local_graphs = 0
for switches in product((0, 1), repeat=3):
    for t0_choices in product((0, 1), repeat=3):
        base = baseline(switches, t0_choices)
        if class_of(base) != "B":
            continue
        bm = mask_of(base)
        available = [e for e in edges if not (bm & edge_bit[e])]
        for extra in combinations(available, 2):
            if not admissible_extra(extra):
                continue
            if alpha(bm | mask_of(extra)) > 2:
                continue
            if sum(6 in e for e in extra) != 1:
                continue
            vec = tuple(sum({part[u], part[v]} == set(pair) for u, v in extra)
                        for pair in large_pairs + t0_pairs)
            if sum(vec[:3]) == 1 and sum(vec[3:]) == 1:
                support.add(vec)
                support_counts[vec] += 1
                local_graphs += 1

expected_support = {
    tuple(1 if i == a or i == 3 + b else 0 for i in range(6))
    for a in range(3) for b in range(3)
}
assert support == expected_support
assert local_graphs == 192

# Verify the actual source K4+K3 baseline in the x_C-outside,
# N_s-single/N_t-double mode. Its three T0 attachments all meet the K4
# triangle, so it is Class A. The two source gadget extras are w-y and y-s_j.
source_constructed_patterns = set()
source_mode_graphs = 0
big = ((0, 1), (2, 3), (4, 5))
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        k = next(t for t in range(3) if t not in (i, j))
        w = 6
        s_i, s_j, s_k = big[i][1], big[j][1], big[k][1]
        y, t_j, t_k = big[i][0], big[j][0], big[k][0]
        k4_edges = list(combinations((w, s_i, s_j, s_k), 2))
        k3_edges = list(combinations((y, t_j, t_k), 2))
        base = k4_edges + k3_edges
        extras = [(w, y), (y, s_j)]
        assert class_of(base) == "A"
        assert alpha(mask_of(base + extras)) == 2
        assert sum(w in e for e in base) == 3
        assert sum(w in e for e in base + extras) == 4
        lp = tuple(sorted((i, j)))
        li = large_pairs.index(lp)
        vec = tuple(1 if z == li else 0 for z in range(3)) + tuple(
            1 if z == i else 0 for z in range(3)
        )
        source_constructed_patterns.add(vec)
        source_mode_graphs += 1
assert source_mode_graphs == 6
assert len(source_constructed_patterns) == 6
assert source_constructed_patterns <= support
assert all(support_counts[p] == 16 for p in source_constructed_patterns)

# A scalar degree-ledger profile.
E0 = 0
E = (2, 2, 2)
eH = (4, 3, 3)  # H edges on T1T2,T1T3,T2T3
assert sum(E) + E0 == 6
assert sum(eH) == 10 - E0
assert all(eH[k] <= 9 - E0 - E[k] for k in range(3))

# Recover y_i from e_H(T_j,T_k) = y_i - 2 - E0 - E_i.
y = (
    eH[2] + 2 + E0 + E[0],
    eH[1] + 2 + E0 + E[1],
    eH[0] + 2 + E0 + E[2],
)
q = tuple(11 - yi for yi in y)        # T0--Ti repeat capacities
r = tuple(12 - e for e in eH)         # Ti--Tj repeat capacities
assert y == (7, 7, 8)
assert q == (4, 4, 3)
assert r == (8, 9, 9)
assert sum(y) == 22 + E0 and sum(q) == 11 - E0
assert sum(eH) == 10 - E0 and sum(r) == 26 + E0
assert sum(q) + sum(r) == 37

# Ten exact colors, each gap 2 and T0 surplus 1:
# four use (T1T2,T0T1), three use (T1T3,T0T2), three use (T2T3,T0T3).
patterns = (
    [(1, 0, 0, 1, 0, 0)] * 4
    + [(1, 0, 0, 0, 1, 0)] * 3
    + [(0, 0, 1, 0, 0, 1)] * 3
)
assert len(patterns) == 10
assert all(p in source_constructed_patterns for p in patterns)
exact_by_pair = tuple(sum(p[i] for p in patterns) for i in range(6))
assert exact_by_pair == (7, 0, 3, 4, 3, 3)
assert sum(sum(p) for p in patterns) == 20
caps = r + q
assert all(exact_by_pair[i] <= caps[i] for i in range(6))

# The residual nonexact-color budget fills the remaining aggregate capacities.
D_by_pair = tuple(caps[i] - exact_by_pair[i] for i in range(6))
assert D_by_pair == (1, 9, 6, 0, 1, 0)
g_D = sum(D_by_pair)
assert g_D == 17 and 7 <= g_D <= 19
assert 37 - sum(sum(p) for p in patterns) == g_D

print("abstract class-B catalog support patterns:", len(support))
print("abstract class-B repaired graphs with (g,t0)=(2,1):", local_graphs)
print("explicit source class-A modes verified:", source_mode_graphs)
print("E0,E1,E2,E3:", (E0, *E))
print("large-pair H edges (12,13,23):", eH)
print("T0-pair H edges (01,02,03):", y)
print("large-pair repeat capacities:", r)
print("T0-pair repeat capacities:", q)
print("source class-A local exact-color surplus:", exact_by_pair)
print("source class-A pattern counts in abstract catalog:", {p: support_counts[p] for p in sorted(source_constructed_patterns)})
print("nonexact-color residual aggregate surplus:", D_by_pair)
print("exact total gap=20; nonexact gap=17; total=37")
print("SOURCE_CLASS_A_AGGREGATE_BUDGET_WITNESS_OK")
print("Scope: source-realizable local Class-A modes plus scalar relaxation only; not a vertex-labelled Q32 coloring.")
