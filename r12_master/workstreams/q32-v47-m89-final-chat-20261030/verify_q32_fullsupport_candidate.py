#!/usr/bin/env python3
"""Independent checker for EG617 r=12 full-support Q32 candidate JSON.

The checker does not trust the SMT solver, component labels, or source-mode
classification. It reconstructs every exact-color edge set from the Type-I
witness data, then checks the full K_61 edge coloring and the Q32 contracts.
"""
from __future__ import annotations
import argparse
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

N = 61
H = tuple(range(47))
O = tuple(range(47, 61))
PIVOT = 47
A = tuple(range(48, 61))
ALL_COLORS = tuple(range(12))
TRACKS = (tuple(range(0, 11)), tuple(range(11, 23)),
          tuple(range(23, 35)), tuple(range(35, 47)))


def edge(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def pairs(vertices):
    return itertools.combinations(vertices, 2)


def expected_color_counts(m):
    """Registered global edge-count vector for the 61-point E408 residual."""
    if m not in (8, 9, 10):
        raise ValueError("m must be 8, 9, or 10")
    counts = {0: 408}
    counts.update({c: 129 for c in range(1, m + 1)})
    if m == 8:
        counts.update({9: 130, 10: 130, 11: 130})
    elif m == 9:
        counts.update({10: 130, 11: 131})
    else:
        counts[11] = 132
    return counts


def find_independent_set(adj_masks, vertices, target_size):
    """Return an independent set of target_size, or None after exact search.

    This is a deterministic maximum-clique branch-and-bound on the complement
    graph. Greedy coloring supplies a valid upper bound at every search node.
    The function is exact; it is not a randomized heuristic.
    """
    vertices = tuple(vertices)
    if target_size <= 0:
        return []
    if len(vertices) < target_size:
        return None
    allowed = 0
    for v in vertices:
        allowed |= 1 << v
    comp_adj = {}
    for v in vertices:
        comp_adj[v] = allowed & ~(adj_masks[v] | (1 << v))

    def color_sort(candidates):
        order, bounds = [], []
        remaining = candidates
        color = 0
        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                order.append(v)
                bounds.append(color)
                remaining &= ~bit
                available &= ~bit
                available &= ~comp_adj[v]
        return order, bounds

    def expand(candidates, chosen):
        order, bounds = color_sort(candidates)
        for idx in range(len(order) - 1, -1, -1):
            if len(chosen) + bounds[idx] < target_size:
                return None
            v = order[idx]
            bit = 1 << v
            if not (candidates & bit):
                continue
            new_chosen = chosen + [v]
            if len(new_chosen) >= target_size:
                return new_chosen
            found = expand(candidates & comp_adj[v], new_chosen)
            if found is not None:
                return found
            candidates &= ~bit
        return None

    return expand(allowed, [])


def find_clique(adj_masks, vertices, target_size):
    """Return a clique of target_size, or None after exact search."""
    vertices = tuple(vertices)
    allowed = 0
    for v in vertices:
        allowed |= 1 << v
    complement_adj = list(adj_masks)
    for v in vertices:
        complement_adj[v] = allowed & ~(adj_masks[v] | (1 << v))
    # Independent sets in the complement are cliques in the original graph.
    return find_independent_set(complement_adj, vertices, target_size)


def source_edges(source):
    """Reconstruct the exact Type-I color graph from its labelled witness."""
    x = source["x"]
    y = source["y"]
    comps = [set(map(int, s)) for s in source["components"]]
    a0 = set(map(int, source["A0"]))
    result = set()
    for comp in comps:
        result.update(edge(u, v) for u, v in pairs(sorted(comp)))
    ns, nt = comps[10], comps[11]
    result.update(edge(y, v) for v in a0)
    result.update(edge(x, v) for v in ns - a0)
    result.update(edge(x, v) for v in nt - {y})
    return result


def source_outside_profile_errors(x, components):
    """Check only the source-correct outside occupancy of the 12 K5 factors.

    Isolated factors may contain excess outside vertices in the generic Q32
    source model. The source contract is the aggregate count plus per-factor
    lower/upper bounds, not a blanket single-outside rule on factors 0..9.
    """
    counts = [sum(int(vertex) in O for vertex in block) for block in components]
    errors = []
    if any(count < 1 for count in counts):
        errors.append("every K5 factor must meet O")
    expected = 13 if int(x) in O else 14
    if sum(counts) != expected:
        errors.append(f"K5 outside counts sum to {sum(counts)}, expected {expected}")
    cap = 2 if int(x) in O else 3
    if any(count > cap for count in counts):
        errors.append(f"a K5 factor exceeds the source outside-count cap {cap}")
    return errors


def verify_candidate(data, check_alpha=True, check_omega=True):
    errors = []
    def fail(message):
        errors.append(message)

    if data.get("format") != "EG617-Q32-FULLSUPPORT-v1":
        fail("format must be EG617-Q32-FULLSUPPORT-v1")
    m = data.get("m")
    if m not in (8, 9):
        return ["this isolated verifier accepts only m=8,9"]
    exact_colors = list(range(1, m + 1))
    nonexact_colors = list(range(m + 1, 12))
    expected_counts = expected_color_counts(m)

    raw_edges = data.get("edge_colors", [])
    colors = {}
    for row in raw_edges:
        if not isinstance(row, list) or len(row) != 3:
            fail("edge_colors entries must be [u,v,color]")
            continue
        u, v, c = map(int, row)
        if not (0 <= u < N and 0 <= v < N and u != v):
            fail(f"invalid edge endpoints {(u, v)}")
            continue
        key = edge(u, v)
        if key in colors:
            fail(f"duplicate edge row for {key}")
        if c not in ALL_COLORS:
            fail(f"invalid color {c} on edge {key}")
        colors[key] = c
    expected_edge_set = set(edge(u, v) for u, v in pairs(range(N)))
    if set(colors) != expected_edge_set:
        fail(f"edge table incomplete/extra: expected {len(expected_edge_set)}, got {len(colors)}")
        return errors

    counts = Counter(colors.values())
    for c, expected in expected_counts.items():
        if counts[c] != expected:
            fail(f"color {c} has {counts[c]} edges, expected {expected}")

    sources = {int(s["color"]): s for s in data.get("source", [])}
    if set(sources) != set(exact_colors):
        fail(f"source witness colors must be exactly {exact_colors}")
        return errors

    comp_of = {}
    gadget = {}
    for c in exact_colors:
        s = sources[c]
        x, y = int(s["x"]), int(s["y"])
        comps = [set(map(int, block)) for block in s["components"]]
        a0 = set(map(int, s["A0"]))
        if len(comps) != 12 or any(len(block) != 5 for block in comps):
            fail(f"color {c}: must provide 12 disjoint 5-sets")
            return errors
        if any(not block <= set(range(N)) for block in comps):
            fail(f"color {c}: component has an invalid vertex")
        if x in set().union(*comps):
            fail(f"color {c}: special vertex x lies in a K5 factor")
        if len(set().union(*comps)) != 60 or sum(map(len, comps)) != 60:
            fail(f"color {c}: K5 factors do not partition V minus x")
        if set().union(*comps) != set(range(N)) - {x}:
            fail(f"color {c}: K5 factors do not cover exactly V minus x")
        if y not in comps[11]:
            fail(f"color {c}: y is not in special K5 Nt")
        if not a0 <= comps[10] or not (1 <= len(a0) <= 4):
            fail(f"color {c}: A0 must be a nonempty proper subset of Ns")
        for issue in source_outside_profile_errors(x, comps):
            fail(f"color {c}: {issue}")
        comp_of[c] = {}
        for k, block in enumerate(comps):
            for v in block:
                comp_of[c][v] = k
        for v in range(N):
            gadget[c, v] = (v == x or comp_of[c].get(v, -1) in (10, 11))
        expected = source_edges(s)
        actual = {e for e, color in colors.items() if color == c}
        if actual != expected:
            fail(f"color {c}: edge set differs from reconstructed Type-I graph "
                 f"(missing={len(expected-actual)}, extra={len(actual-expected)})")
        if len(expected) != 129:
            fail(f"color {c}: reconstructed source graph has {len(expected)} edges, not 129")

    # Target-color core H.
    h_edges = [edge(u, v) for u, v in pairs(H) if colors[edge(u, v)] == 0]
    if len(h_edges) != 285:
        fail(f"target H has {len(h_edges)} edges, expected 285")
    h_adj = [0] * N
    h_degree = {v: 0 for v in H}
    for u, v in h_edges:
        h_adj[u] |= 1 << v
        h_adj[v] |= 1 << u
        h_degree[u] += 1
        h_degree[v] += 1
    if any(h_degree[v] < 12 for v in H):
        fail(f"delta(H)={min(h_degree.values())}, expected at least 12")
    if sum(h_degree[v] - 12 for v in H) != 6:
        fail("core degree excess does not sum to six")
    if any(colors[edge(PIVOT, a)] != 0 for a in A):
        fail("all 13 pivot-shell edges pA must have target color 0")

    # Exact 37-unit gap ledger on H.
    core_counts = {}
    for c in range(1, 12):
        core_counts[c] = sum(colors[edge(u, v)] == c for u, v in pairs(H))
        if core_counts[c] < 69:
            fail(f"non-target color {c} has only {core_counts[c]} H-edges (<69)")
    for c in exact_colors:
        if core_counts.get(c, 0) > 75:
            fail(f"exact color {c} exceeds the source gap cap g_C<=6")
    if sum(core_counts.get(c, 0) - 69 for c in range(1, 12)) != 37:
        fail("sum_C (e_C(H)-69) is not 37")

    # Full support: every core vertex lies in a K5 factor with exactly one O vertex,
    # so its four H vertices form a source-correct core K4 witness. The factor may
    # be one of the two special K5s inside G11; do not restrict to indices 0..9.
    for v in H:
        covered = False
        for c in exact_colors:
            for k, block in enumerate(sources[c]["components"]):
                if v in set(map(int, block)) and sum(u in O for u in map(int, block)) == 1:
                    covered = True
                    break
            if covered:
                break
        if not covered:
            fail(f"full-support U=H fails at vertex {v}")

    # Pivot-neighborhood K4 packing and pointwise residual constraints.
    qsets = {}
    for c in exact_colors:
        s = sources[c]
        x, y = int(s["x"]), int(s["y"])
        comps = [set(map(int, block)) for block in s["components"]]
        if x != PIVOT:
            k = comp_of[c].get(PIVOT, -1)
            q = comps[k] - {PIVOT} if k >= 0 else set()
        else:
            q = comps[11] - {y}
        if len(q) != 4 or not q <= set(H):
            fail(f"color {c}: pivot K4 is not a 4-set contained in H")
        qsets[c] = q
    for c1, c2 in itertools.combinations(exact_colors, 2):
        if qsets.get(c1, set()) & qsets.get(c2, set()):
            fail(f"pivot K4 blocks for colors {c1},{c2} overlap")
    union_q = set().union(*(qsets.get(c, set()) for c in exact_colors))
    residual = set(H) - union_q
    if len(residual) != 47 - 4 * m:
        fail(f"pivot residual has size {len(residual)}, expected {47-4*m}")
    # Independent replay of the m=8,9 pivot-pair matching system.
    pair_edge_counts = {}
    light_maps = {}
    for c1, c2 in itertools.combinations(exact_colors, 2):
        q1, q2 = sorted(qsets.get(c1, set())), sorted(qsets.get(c2, set()))
        if len(q1) != 4 or len(q2) != 4:
            continue
        cross = [(u, v) for u in q1 for v in q2 if colors[edge(u, v)] == 0]
        pair_edge_counts[(c1, c2)] = len(cross)
        if len(cross) < 4:
            fail(f"pivot blocks {c1},{c2} have only {len(cross)} target edges (<4)")
        perfect = []
        for perm in itertools.permutations(q2):
            if all(colors[edge(q1[i], perm[i])] == 0 for i in range(4)):
                perfect.append(dict(zip(q1, perm)))
        if not perfect:
            fail(f"pivot blocks {c1},{c2} have no target perfect matching")
        if len(cross) == 4:
            if len(perfect) != 1:
                fail(f"light pivot pair {c1},{c2} does not have a unique perfect matching")
            elif perfect:
                light_maps[(c1, c2)] = perfect[0]

    def pivot_map(c_from, c_to, u):
        key = (min(c_from, c_to), max(c_from, c_to))
        mapping = light_maps[key]
        if c_from < c_to:
            return mapping.get(u)
        return {v: a for a, v in mapping.items()}.get(u)

    mu4 = (0, 4, 6, 8, 8, 10, 10, 12, 12, 12, 13, 13, 14,
           14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16)
    for c2, c3 in itertools.combinations(exact_colors, 2):
        compositions = {}
        for anchor in exact_colors:
            if anchor in (c2, c3):
                continue
            k2 = (min(anchor, c2), max(anchor, c2))
            k3 = (min(anchor, c3), max(anchor, c3))
            if k2 not in light_maps or k3 not in light_maps:
                continue
            mapping = {}
            for u in sorted(qsets[c2]):
                middle = pivot_map(c2, anchor, u)
                v = pivot_map(anchor, c3, middle) if middle is not None else None
                if v is None:
                    mapping = {}
                    break
                mapping[u] = v
            if len(mapping) == 4 and len(set(mapping.values())) == 4:
                signature = tuple((u, mapping[u]) for u in sorted(mapping))
                compositions[signature] = mapping
        t = len(compositions)
        if t:
            pair_edges = pair_edge_counts.get((c2, c3), 0)
            if pair_edges < mu4[t]:
                fail(f"pivot pair {c2},{c3} has {pair_edges} H-edges but {t} forced matchings require >= {mu4[t]}")
            for mapping in compositions.values():
                for u, v in mapping.items():
                    if colors[edge(u, v)] != 0:
                        fail(f"pivot matching composition forces H-edge {(u,v)} for blocks {c2},{c3}")

    # Exact six-unit degree ledger on each pivot block:
    # X_i + Y_i = 5 + epsilon_i.
    n_residual = len(residual)
    for c in exact_colors:
        q = qsets.get(c, set())
        if len(q) != 4:
            continue
        x_i = sum(pair_edge_counts.get((min(c, d), max(c, d)), 0) - 4
                  for d in exact_colors if d != c)
        y_i = sum(colors[edge(u, v)] == 0
                  for u in q for v in residual) - n_residual
        eps_i = sum(h_degree[v] - 12 for v in q)
        if y_i < 0 or x_i + y_i != 5 + eps_i:
            fail(f"pivot block {c} degree ledger fails: X={x_i}, Y={y_i}, epsilon={eps_i}")

    for r in residual:
        q_degree = sum(colors[edge(r, q)] == 0 for q in union_q)
        if q_degree < m:
            fail(f"residual vertex {r} has only {q_degree} H-neighbors in pivot blocks, expected >= {m}")

    # The complete coloring/alpha checks below are the authority. Derived pointwise
    # reserve quotas are deliberately not hard-coded here, so this verifier cannot
    # reject a genuine source-correct coloring because of an unverified strengthening.

    # Optional explicit common-P / matching certificate for the aligned m=10 z=0,1 cell.
    if data.get("aligned_z01"):
        if m != 10:
            fail("aligned_z01 certificate is only defined for m=10")
        tracks = [set(t) for t in TRACKS]
        for i, track in enumerate(tracks):
            if any(colors[edge(u, v)] != 0 for u, v in pairs(sorted(track))):
                fail(f"aligned track T{i} is not a target-color clique")
        if [sum(v in residual for v in t) for t in tracks] != [1, 2, 2, 2]:
            fail("aligned pivot residual profile is not (1,2,2,2) on T0,T1,T2,T3")

        # Independent replay of the exact nonexact-gap saturation theorem.
        for c in exact_colors:
            if core_counts[c] != 72:
                fail(f"aligned color {c} has {core_counts[c]} H-edges, expected 72")
        if core_counts[11] != 76:
            fail(f"aligned nonexact color 11 has {core_counts[11]} H-edges, expected 76")
        for o in O:
            for i in range(1, 4):
                count = sum(colors[edge(o, v)] == 11 for v in tracks[i])
                if count != 1:
                    fail(f"outside vertex {o} has {count} color-11 edges into T{i}, expected 1")
        d_a = sum(colors[edge(u, v)] == 11 for u, v in pairs(A))
        d_t0 = {o: sum(colors[edge(o, v)] == 11 for v in tracks[0]) for o in O}
        if d_a not in (2, 3):
            fail(f"aligned D[A] has {d_a} edges, expected 2 or 3")
        if any(d_t0[o] > 1 for o in O):
            fail("an outside vertex has more than one color-11 edge into T0")
        if d_t0[PIVOT] != 1:
            fail(f"pivot p has {d_t0[PIVOT]} color-11 edges into T0, expected 1")
        if sum(d_t0.values()) + d_a != 14:
            fail("color-11 outside/T0 saturation identity sum d_D(o,T0)+e_D(A)=14 fails")
        for a, b in pairs(A):
            if d_t0[a] == 0 and d_t0[b] == 0 and colors[edge(a, b)] != 11:
                fail(f"two A vertices with no color-11 T0-neighbor are not adjacent in D: {(a,b)}")

        # Independent replay of the outside-component bijection theorem.
        d_a_degrees = {
            a: sum(colors[edge(a, b)] == 11 for b in A if b != a)
            for a in A
        }
        z_vertices = {a for a in A if d_t0[a] == 0}
        if d_a == 2:
            if any(deg > 1 for deg in d_a_degrees.values()):
                fail("the two D[A] edges are not disjoint")
            if len(z_vertices) != 2 or not all(
                colors[edge(a, b)] == 11 for a, b in pairs(sorted(z_vertices))
            ):
                fail("the 2K2 case does not have a zero-T0-neighbor edge component")
        elif d_a == 3:
            if len(z_vertices) != 3 or sum(
                colors[edge(a, b)] == 11 for a, b in pairs(A)
            ) != 3:
                fail("the K3 case does not have exactly three zero-T0-neighbor vertices")
            if any(colors[edge(a, b)] != 11
                   for a, b in pairs(sorted(z_vertices))):
                fail("the three zero-T0-neighbor vertices do not form a D-triangle")

        for a, b in pairs(A):
            if colors[edge(a, b)] == 11:
                for h in H:
                    if (colors[edge(a, h)] == 11) != (colors[edge(b, h)] == 11):
                        fail(f"D[A] edge {(a,b)} endpoints do not have identical D-neighborhoods in H at {h}")

        for i in range(1, 4):
            degrees = sorted(
                sum(colors[edge(o, v)] == 11 for o in O)
                for v in tracks[i]
            )
            expected = ([1] * 10 + [2] * 2) if d_a == 2 else ([1] * 11 + [3])
            if degrees != expected:
                fail(f"T{i} outside-D degree multiset {degrees} differs from {expected}")

        t0_degrees = sorted(
            sum(colors[edge(o, v)] == 11 for o in O)
            for v in tracks[0]
        )
        expected_t0 = ([1] * 10 + [2]) if d_a == 2 else ([1] * 11)
        if t0_degrees != expected_t0:
            fail(f"T0 outside-D degree multiset {t0_degrees} differs from {expected_t0}")

        # Independent replay: corresponding vertices of any shared O-component
        # must be joined in D across every track pair.
        for o in O:
            large_neighbors = {}
            for i in range(1, 4):
                ns = [v for v in tracks[i] if colors[edge(o, v)] == 11]
                if len(ns) != 1:
                    fail(f"outside vertex {o} has {len(ns)} D-neighbors in T{i}, expected one")
                else:
                    large_neighbors[i] = ns[0]
            for i in range(1, 4):
                for j in range(i + 1, 4):
                    if i in large_neighbors and j in large_neighbors:
                        if colors[edge(large_neighbors[i], large_neighbors[j])] != 11:
                            fail(f"the D-neighbors of outside vertex {o} in T{i},T{j} are not D-adjacent")
            t0_neighbors = [v for v in tracks[0] if colors[edge(o, v)] == 11]
            if len(t0_neighbors) > 1:
                fail(f"outside vertex {o} has multiple D-neighbors in T0")
            if t0_neighbors:
                for i in range(1, 4):
                    if i in large_neighbors and colors[edge(t0_neighbors[0], large_neighbors[i])] != 11:
                        fail(f"the D-neighbors of outside vertex {o} in T0,T{i} are not D-adjacent")

        z_cross = sum(colors[edge(u, v)] == 0 for i in range(4) for j in range(i+1,4)
                      for u in residual & tracks[i] for v in residual & tracks[j])
        if z_cross not in (0, 1):
            fail(f"aligned residual cross-fiber target-edge count z={z_cross}, expected 0 or 1")
        # H cross-track degree restrictions.
        for i in range(1, 4):
            for j in range(i+1, 4):
                for u in tracks[i]:
                    if sum(colors[edge(u, v)] == 0 for v in tracks[j]) > 1:
                        fail(f"H[T{i},T{j}] is not a matching at vertex {u}")
                for v in tracks[j]:
                    if sum(colors[edge(u, v)] == 0 for u in tracks[i]) > 1:
                        fail(f"H[T{i},T{j}] is not a matching at vertex {v}")
            for u in tracks[0]:
                if sum(colors[edge(u, v)] == 0 for v in tracks[i]) > 1:
                    fail(f"H[T0,T{i}] exceeds the T0-side matching bound at {u}")

        pair_data = data.get("matchings", {})
        if set(pair_data) != {"0-1", "0-2", "0-3", "1-2", "1-3", "2-3"}:
            fail("aligned certificate must include P and M for all six track pairs")
        p_sets, m_sets = {}, {}
        for i in range(4):
            for j in range(i+1, 4):
                key = f"{i}-{j}"
                block = pair_data.get(key, {})
                p_edges = {edge(*map(int, e)) for e in block.get("P", [])}
                mm = {int(c): {edge(*map(int, e)) for e in es}
                      for c, es in block.get("M", {}).items()}
                if set(mm) != set(range(1, 12)):
                    fail(f"pair {key}: M must include colors 1..11")
                pair_edges = {edge(u, v) for u in tracks[i] for v in tracks[j]}
                union = set(p_edges)
                for es in mm.values():
                    if union & es:
                        fail(f"pair {key}: duplicate edge across P/M")
                    union |= es
                if union != pair_edges:
                    fail(f"pair {key}: P and M do not partition all track-pair edges")
                for c, es in mm.items():
                    if any(colors[e] != c for e in es):
                        fail(f"pair {key}: M color {c} contains an edge of another color")
                    for u in tracks[i]:
                        if sum(u in e for e in es) != 1:
                            fail(f"pair {key}: M color {c} does not saturate left vertex {u}")
                    if i != 0:
                        for v in tracks[j]:
                            if sum(v in e for e in es) != 1:
                                fail(f"pair {key}: M color {c} does not saturate right vertex {v}")
                if i == 0:
                    for u in tracks[0]:
                        if sum(u in e for e in p_edges) != 1:
                            fail(f"pair {key}: P does not have degree one at T0 vertex {u}")
                else:
                    for u in tracks[i]:
                        if sum(u in e for e in p_edges) != 1:
                            fail(f"pair {key}: P is not a perfect matching at left vertex {u}")
                    for v in tracks[j]:
                        if sum(v in e for e in p_edges) != 1:
                            fail(f"pair {key}: P is not a perfect matching at right vertex {v}")
                p_sets[i, j] = p_edges
                m_sets[i, j] = mm

                # Exact colors: all non-gadget cross-track edges are selected into M.
                for c in exact_colors:
                    for e in pair_edges:
                        u, v = e
                        if colors[e] == c and not (gadget[c, u] and gadget[c, v]) and e not in mm[c]:
                            fail(f"pair {key}: non-gadget color-{c} edge {e} omitted from M")
                        if e in p_edges and colors[e] == c and not (gadget[c, u] and gadget[c, v]):
                            fail(f"pair {key}: P contains non-gadget color-{c} edge {e}")

        # Every exact color's gadget vertices must match within G11 on large pairs.
        for c in exact_colors:
            for i in range(1, 4):
                gi = {v for v in tracks[i] if gadget[c, v]}
                if len(gi) != 2:
                    fail(f"color {c}: G11 has {len(gi)} vertices on T{i}, expected 2")
            g0 = {v for v in tracks[0] if gadget[c, v]}
            if len(g0) not in (1, 2):
                fail(f"color {c}: G11 has {len(g0)} vertices on T0, expected 1 or 2")
            for i in range(1, 4):
                key = (0, i)
                for u in tracks[0]:
                    chosen = [v for v in tracks[i] if edge(u, v) in m_sets[key][c]]
                    if len(chosen) != 1 or ((u in g0) != (chosen[0] in {v for v in tracks[i] if gadget[c, v]})):
                        fail(f"color {c}: T0-T{i} matching does not preserve gadget/non-gadget status at {u}")
            for i in range(1, 4):
                for j in range(i+1, 4):
                    key = (i, j)
                    for u in tracks[i]:
                        chosen = [v for v in tracks[j] if edge(u, v) in m_sets[key][c]]
                        if len(chosen) != 1 or ((u in {v for v in tracks[i] if gadget[c, v]}) !=
                                                (chosen[0] in {v for v in tracks[j] if gadget[c, v]})):
                            fail(f"color {c}: T{i}-T{j} matching does not preserve gadget status at {u}")

        # Pair-projection packing: a P-hit K2,2 block has multiplicity at most one;
        # a P-free block has multiplicity at most two; two colors share at most one key.
        for i in range(1, 4):
            for j in range(i+1, 4):
                left_pairs = list(itertools.combinations(sorted(tracks[i]), 2))
                right_pairs = list(itertools.combinations(sorted(tracks[j]), 2))
                p_edges = p_sets[i, j]
                projection_keys = {}
                for c in exact_colors:
                    ri = {v for v in tracks[i] if gadget[c, v]}
                    rj = {v for v in tracks[j] if gadget[c, v]}
                    projection_keys[c, i, j] = (tuple(sorted(ri)), tuple(sorted(rj)))
                for aa in left_pairs:
                    for bb in right_pairs:
                        owners = [c for c in exact_colors
                                  if projection_keys[c, i, j] == (tuple(aa), tuple(bb))]
                        hit = any(edge(u, v) in p_edges for u in aa for v in bb)
                        if len(owners) > (1 if hit else 2):
                            fail(f"pair {i}-{j}: projection {(aa,bb)} has multiplicity {len(owners)} with P_hit={hit}")
                for c1, c2 in itertools.combinations(exact_colors, 2):
                    shared = sum(projection_keys[c1, i, j] == projection_keys[c2, i, j]
                                 for i, j in ((1,2),(1,3),(2,3)))
                    if shared > 1:
                        fail(f"colors {c1},{c2} share {shared} pair projections")

        for c in exact_colors:
            t_count = sum(colors[e] == c and e in p_sets[0, i]
                          for i in range(1, 4) for e in p_sets[0, i])
            if t_count > 1:
                fail(f"exact color {c} has {t_count} T0-pair repeat edges, expected at most one")

    if check_alpha:
        # H has independence number at most four.
        h_adj = [0] * N
        for u, v in h_edges:
            h_adj[u] |= 1 << v
            h_adj[v] |= 1 << u
        independent = find_independent_set(h_adj, H, 5)
        if independent is not None:
            fail(f"H has an independent 5-set: {independent}")
        # The balanced-coloring premise is alpha(C)<=12 for every color.
        for c in ALL_COLORS:
            adj = [0] * N
            for (u, v), color in colors.items():
                if color == c:
                    adj[u] |= 1 << v
                    adj[v] |= 1 << u
            independent = find_independent_set(adj, range(N), 13)
            if independent is not None:
                fail(f"color {c} has an independent 13-set: {independent}")

    if check_omega:
        # The 61-point residual contract also excludes monochromatic K6s.
        for c in ALL_COLORS:
            adj = [0] * N
            for (u, v), color in colors.items():
                if color == c:
                    adj[u] |= 1 << v
                    adj[v] |= 1 << u
            clique = find_clique(adj, range(N), 6)
            if clique is not None:
                fail(f"color {c} has a monochromatic K6: {clique}")

    if check_alpha and check_omega:
        # Recheck registered nonexact minimum-degree consequences and safe quota.
        for c in nonexact_colors:
            floor = 4 if expected_counts[c] == 130 else 3
            degrees = [sum(colors[edge(v, u)] == c for u in range(N) if u != v)
                       for v in range(N)]
            if min(degrees) < floor:
                fail(f"nonexact color {c} has minimum degree {min(degrees)}, expected >= {floor}")
        safe_q_cap = {8: 4, 9: 5, 10: 5}[m]
        conditional_q_cap = {8: 3, 9: 4, 10: 4}[m]
        for z in residual:
            q_z = sum(bool(gadget[c, z]) for c in exact_colors)
            if q_z > safe_q_cap:
                fail(f"residual vertex {z} has gadget multiplicity {q_z}, safe cap {safe_q_cap}")
            target_degree = sum(colors[edge(z, u)] == 0 for u in range(N) if u != z)
            if target_degree >= 13 and q_z > conditional_q_cap:
                fail(f"residual vertex {z} has gadget multiplicity {q_z} despite target degree {target_degree}")

    return errors


def self_test():
    # Empty graph has a full independent set; do not assume the search order.
    empty_adj = [0] * 5
    assert set(find_independent_set(empty_adj, range(5), 5)) == set(range(5))
    complete_adj = [(sum(1 << j for j in range(5) if j != i)) for i in range(5)]
    assert find_independent_set(complete_adj, range(5), 2) is None
    # A path on four vertices has an independent set of size two.
    path_adj = [0] * 4
    for u, v in ((0,1),(1,2),(2,3)):
        path_adj[u] |= 1 << v
        path_adj[v] |= 1 << u
    found = find_independent_set(path_adj, range(4), 2)
    assert found is not None and all(not (path_adj[u] & (1 << v)) for u, v in pairs(found))

    # Malformed source witnesses must be rejected cleanly, not crash later
    # when the pivot-packing checker reads a missing comp_of entry.
    malformed = {
        "format": "EG617-Q32-FULLSUPPORT-v1",
        "m": 8,
        "edge_colors": [[u, v, 0] for u, v in pairs(range(N))],
        "source": [
            {"color": c, "x": 0, "y": 1, "A0": [], "components": []}
            for c in range(1, 9)
        ],
    }
    malformed_errors = verify_candidate(malformed, check_alpha=False)
    assert any("must provide 12 disjoint 5-sets" in item for item in malformed_errors)

    # Exact registered global color-count vectors all partition K_61.
    expected8 = {0: 408, **{c: 129 for c in range(1, 9)},
                 9: 130, 10: 130, 11: 130}
    expected9 = {0: 408, **{c: 129 for c in range(1, 10)},
                 10: 130, 11: 131}
    expected10 = {0: 408, **{c: 129 for c in range(1, 11)}, 11: 132}
    assert expected_color_counts(8) == expected8
    assert expected_color_counts(9) == expected9
    assert expected_color_counts(10) == expected10
    assert all(sum(expected_color_counts(m).values()) == N * (N - 1) // 2
               for m in (8, 9, 10))

    # Clique search is the exact complement-dual of independent-set search.
    assert find_clique(complete_adj, range(5), 5) is not None
    assert find_clique(empty_adj, range(5), 2) is None

    # The generic Type-I outside profile accepts excess O-points in isolated factors.
    # x in O: one double plus eleven singles (13 outside points total).
    assert source_outside_profile_errors(47, [[48,49,0,1,2]] + [[50+i, 3+4*i, 4+4*i, 5+4*i, 6+4*i] for i in range(11)]) == []
    # x in H: two doubles plus ten singles, or one triple plus eleven singles.
    assert source_outside_profile_errors(0, [[47,48,1,2,3], [49,50,4,5,6]] +
                                         [[51+i, 10+i, 20+i, 30+i, 40+i] for i in range(10)]) == []
    assert source_outside_profile_errors(0, [[47,48,49,1,2]] +
                                         [[50+i, 10+i, 20+i, 30+i, 40+i] for i in range(11)]) == []
    assert source_outside_profile_errors(47, [[48+i, i, 12+i, 24+i, 35+i] for i in range(12)])
    assert source_outside_profile_errors(0, [[47,48,49,50,1]] +
                                         [[51+i, 10+i, 20+i, 30+i, 40+i] for i in range(11)])

    # Exhaustively compare the exact branch-and-bound search with brute force
    # on every simple graph with at most five vertices and every target size.
    checked = 0
    for n in range(1, 6):
        edge_list = list(pairs(range(n)))
        for mask in range(1 << len(edge_list)):
            adj = [0] * n
            for i, (u, v) in enumerate(edge_list):
                if mask & (1 << i):
                    adj[u] |= 1 << v
                    adj[v] |= 1 << u
            for k in range(1, n + 1):
                found = find_independent_set(adj, range(n), k)
                expected = None
                for candidate in itertools.combinations(range(n), k):
                    if all(not (adj[u] & (1 << v))
                           for u, v in pairs(candidate)):
                        expected = candidate
                        break
                assert (found is None) == (expected is None), (n, mask, k, found, expected)
                if found is not None:
                    assert len(found) == k
                    assert all(not (adj[u] & (1 << v))
                               for u, v in pairs(found))
                found_clique = find_clique(adj, range(n), k)
                expected_clique = None
                for candidate in itertools.combinations(range(n), k):
                    if all(adj[u] & (1 << v) for u, v in pairs(candidate)):
                        expected_clique = candidate
                        break
                assert (found_clique is None) == (expected_clique is None), (
                    "clique", n, mask, k, found_clique, expected_clique)
                if found_clique is not None:
                    assert len(found_clique) == k
                    assert all(adj[u] & (1 << v) for u, v in pairs(found_clique))
                checked += 1
    assert checked == 5405
    print("Q32_CANDIDATE_VERIFIER_SELF_TEST_OK; independent-set and clique cases=5405 each")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--skip-alpha", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not args.candidate:
        parser.error("candidate JSON path is required unless --self-test is used")
    data = json.loads(Path(args.candidate).read_text(encoding="utf-8"))
    errors = verify_candidate(data, check_alpha=not args.skip_alpha)
    if errors:
        print("Q32_CANDIDATE_INVALID")
        for item in errors:
            print(" - " + item)
        return 1
    print("Q32_FULLSUPPORT_CANDIDATE_VERIFIED")
    print(f"m={data['m']}; aligned_z01={bool(data.get('aligned_z01'))}; "
          f"vertices={N}; edges={N*(N-1)//2}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
