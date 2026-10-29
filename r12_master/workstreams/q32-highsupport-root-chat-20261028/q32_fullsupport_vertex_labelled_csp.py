#!/usr/bin/env python3
"""Build and solve the exact labelled K_61 Q32 CSP with Z3.

Requires z3-solver. The generic model covers m=8,9,10 and all Type-I source
placements. --aligned-z01 adds the explicit six-pair common-P / matching model
for the m=10 aligned residual profile (1,2,2,2), z in {0,1}.

Alpha constraints are added by exact lazy separation: every proposed model is
searched for an independent 5-set in H and an independent 13-set in each color.
A violating set adds the valid clause that at least one of its pairs has that
color. SAT is accepted only after the independent candidate verifier passes.
"""
from __future__ import annotations
import argparse
import itertools
import json
import sys
from pathlib import Path

try:
    import z3
except ImportError:
    z3 = None

from verify_q32_fullsupport_candidate import (
    ALL_COLORS, H, N, O, PIVOT, A, TRACKS, edge, pairs,
    expected_color_counts, find_independent_set, find_clique, verify_candidate,
)



def isum(items):
    return z3.Sum(list(items))


def iff_count(predicates):
    return isum(z3.If(p, 1, 0) for p in predicates)


def build_model(m, aligned_z01=False):
    if z3 is None:
        raise RuntimeError("z3-solver is not installed; install z3-solver before solving")
    if m not in (8, 9, 10):
        raise ValueError("m must be 8, 9, or 10")
    if aligned_z01 and m != 10:
        raise ValueError("--aligned-z01 is defined only for m=10")

    solver = z3.Solver()
    try:
        solver.set(proof=True)
    except Exception:
        pass

    col = {edge(u, v): z3.Int(f"col_{u}_{v}")
           for u, v in pairs(range(N))}
    for value in col.values():
        solver.add(value >= 0, value <= 11)

    exact = tuple(range(1, m + 1))
    nonexact = tuple(range(m + 1, 12))
    source = {}
    comp = {}
    xvar = {}
    yvar = {}
    a0var = {}
    gadget = {}
    component_outside = {}

    for c in exact:
        xvar[c] = z3.Int(f"x_{c}")
        yvar[c] = z3.Int(f"y_{c}")
        solver.add(xvar[c] >= 0, xvar[c] < N, yvar[c] >= 0, yvar[c] < N)
        comp[c] = {v: z3.Int(f"comp_{c}_{v}") for v in range(N)}
        a0var[c] = {v: z3.Bool(f"a0_{c}_{v}") for v in range(N)}
        for v in range(N):
            cv = comp[c][v]
            solver.add(cv >= -1, cv <= 11)
            solver.add((cv == -1) == (xvar[c] == v))
            solver.add(z3.Implies(a0var[c][v], cv == 10))
            solver.add(z3.Implies(cv != 10, z3.Not(a0var[c][v])))
        for k in range(12):
            solver.add(iff_count(comp[c][v] == k for v in range(N)) == 5)
        solver.add(z3.Or([z3.And(yvar[c] == v, comp[c][v] == 11) for v in range(N)]))
        solver.add(iff_count(a0var[c][v] for v in range(N)) >= 1)
        solver.add(iff_count(a0var[c][v] for v in range(N)) <= 4)

        # Source-correct outside-count normal form. Every K5 factor meets O;
        # the 12 factors contain 13 O-points when x is in O, and all 14 when
        # x is in H. This permits the double/triple placements in either the
        # isolated factors or the two special factors; do not hard-code only
        # the (Ns,Nt) profiles where all excess outside vertices lie in G11.
        x_outside = z3.Or([xvar[c] == v for v in O])
        component_outside[c] = {}
        for k in range(12):
            outside_k = iff_count(
                z3.And(comp[c][v] == k, z3.BoolVal(v in O))
                for v in range(N))
            component_outside[c][k] = outside_k
            solver.add(outside_k >= 1)
            solver.add(outside_k <= z3.If(x_outside, 2, 3))
        solver.add(isum(component_outside[c][k] for k in range(12)) ==
                   z3.If(x_outside, 13, 14))

        gadget[c] = {v: z3.Or(xvar[c] == v, comp[c][v] == 10,
                              comp[c][v] == 11) for v in range(N)}

        def source_edge(u, v):
            cu, cv = comp[c][u], comp[c][v]
            same_k5 = z3.And(cu == cv, cu >= 0)
            x_to_ns = z3.Or(
                z3.And(xvar[c] == u, cv == 10, z3.Not(a0var[c][v])),
                z3.And(xvar[c] == v, cu == 10, z3.Not(a0var[c][u])))
            x_to_nt = z3.Or(
                z3.And(xvar[c] == u, cv == 11, v != yvar[c]),
                z3.And(xvar[c] == v, cu == 11, u != yvar[c]))
            y_to_a0 = z3.Or(
                z3.And(yvar[c] == u, cv == 10, a0var[c][v]),
                z3.And(yvar[c] == v, cu == 10, a0var[c][u]))
            return z3.Or(same_k5, x_to_ns, x_to_nt, y_to_a0)

        for u, v in pairs(range(N)):
            solver.add((col[edge(u, v)] == c) == source_edge(u, v))
        solver.add(iff_count(col[e] == c for e in col) == 129)

    # Exact registered edge-count vector for K_61.
    for c, total in expected_color_counts(m).items():
        solver.add(iff_count(col[e] == c for e in col) == total)

    # The 13 pivot-shell edges are target-colored.
    for a in A:
        solver.add(col[edge(PIVOT, a)] == 0)

    # Core H: 285 target edges, minimum degree 12, total excess six.
    h_edge_expr = [col[edge(u, v)] == 0 for u, v in pairs(H)]
    solver.add(iff_count(h_edge_expr) == 285)
    h_degree = {}
    for v in H:
        h_degree[v] = iff_count(col[edge(v, u)] == 0 for u in H if u != v)
        solver.add(h_degree[v] >= 12)
    solver.add(isum(h_degree[v] - 12 for v in H) == 6)

    # The 37-unit near-Turan gap ledger.
    core_edges = {
        c: iff_count(col[edge(u, v)] == c for u, v in pairs(H))
        for c in range(1, 12)
    }
    for c in range(1, 12):
        solver.add(core_edges[c] >= 69)
    for c in exact:
        solver.add(core_edges[c] <= 75)
    solver.add(isum(core_edges[c] - 69 for c in range(1, 12)) == 37)

    # Full support U=H: every core vertex lies in a source K5 factor with
    # exactly one O vertex, including a special factor Ns or Nt when applicable.
    for v in H:
        solver.add(z3.Or([
            z3.And(comp[c][v] == k, component_outside[c][k] == 1)
            for c in exact for k in range(12)
        ]))

    # Pivot K4 packing Q_C and residual R=H\\union Q_C.
    qblock = {}
    for c in exact:
        qblock[c] = {}
        for v in H:
            if_expr = z3.Or(
                z3.And(xvar[c] != PIVOT, comp[c][v] == comp[c][PIVOT],
                       z3.BoolVal(v != PIVOT)),
                z3.And(xvar[c] == PIVOT, comp[c][v] == 11, yvar[c] != v))
            qblock[c][v] = z3.Bool(f"q_{c}_{v}")
            solver.add(qblock[c][v] == if_expr)
        solver.add(iff_count(qblock[c][v] for v in H) == 4)
    for v in H:
        solver.add(iff_count(qblock[c][v] for c in exact) <= 1)
    residual = {v: z3.Bool(f"R_{v}") for v in H}
    for v in H:
        solver.add(residual[v] == z3.Not(z3.Or([qblock[c][v] for c in exact])))
    solver.add(iff_count(residual[v] for v in H) == 47 - 4 * m)

    # Nonexact degree floors from the registered 130/131/132-edge theorems.
    # omega<=5 and alpha<=12 are enforced by lazy cuts; these floors are valid
    # consequences of those premises and strengthen the intermediate model.
    color_counts = expected_color_counts(m)
    for c in nonexact:
        floor = 4 if color_counts[c] == 130 else 3
        for v in range(N):
            solver.add(iff_count(col[edge(v, u)] == c for u in range(N) if u != v) >= floor)

    # Safe all-color gadget reserve. For residual z, target degree d_0(z)>=
    # d_H(z)>=12; each exact color contributes >=4 plus one for gadget membership,
    # and the nonexact floors sum to L_m=(12,7,3). This yields q_z<=(4,5,5).
    # The stronger (3,4,4) cap is only conditional on d_0(z)>=13.
    safe_q_cap = {8: 4, 9: 5, 10: 5}[m]
    conditional_q_cap = {8: 3, 9: 4, 10: 4}[m]
    for v in H:
        q_count = iff_count(gadget[c][v] for c in exact)
        solver.add(z3.Implies(residual[v], q_count <= safe_q_cap))
        target_degree = iff_count(col[edge(v, u)] == 0 for u in range(N) if u != v)
        solver.add(z3.Implies(
            z3.And(residual[v], target_degree >= 13),
            q_count <= conditional_q_cap))

    # Explicit pivot-neighborhood packing constraints. These are necessary
    # consequences of alpha(H)<=4 and the disjoint independent K4 blocks Q_C.
    # They strengthen the search without replacing the full labelled model.
    q_member = {v: z3.Or([qblock[c][v] for c in exact]) for v in H}
    n_residual = 47 - 4 * m
    p4_floor = {8: 21, 9: 10, 10: 3}[m]
    degree_gap = {8: 18, 9: 13, 10: 8}[m]

    # Every pair of disjoint independent K4 blocks has at least four H-edges.
    for c1, c2 in itertools.combinations(exact, 2):
        between = []
        for u, v in pairs(H):
            opposite_blocks = z3.Or(
                z3.And(qblock[c1][u], qblock[c2][v]),
                z3.And(qblock[c1][v], qblock[c2][u]))
            between.append(z3.And(opposite_blocks, col[edge(u, v)] == 0))
        solver.add(iff_count(between) >= 4)

    # Every residual point has a target-color neighbor in each pivot K4.
    for v in H:
        for c in exact:
            neighbors_in_block = iff_count(
                z3.And(qblock[c][u], col[edge(v, u)] == 0)
                for u in H if u != v)
            solver.add(z3.Implies(residual[v], neighbors_in_block >= 1))

    e_q = iff_count(z3.And(q_member[u], q_member[v], col[edge(u, v)] == 0)
                    for u, v in pairs(H))
    e_qr = iff_count(z3.And(
        z3.Or(z3.And(q_member[u], residual[v]),
              z3.And(residual[u], q_member[v])),
        col[edge(u, v)] == 0) for u, v in pairs(H))
    e_r = iff_count(z3.And(residual[u], residual[v], col[edge(u, v)] == 0)
                    for u, v in pairs(H))
    x_slack = e_q - 4 * (m * (m - 1) // 2)
    y_slack = e_qr - m * n_residual
    z_slack = e_r - p4_floor
    solver.add(x_slack >= 0, y_slack >= 0, z_slack >= 0)
    solver.add(x_slack + y_slack + z_slack == 32)
    solver.add(2 * x_slack + y_slack >= 5 * m)
    solver.add(y_slack + 2 * z_slack >= degree_gap)
    solver.add((2 * x_slack + y_slack - 5 * m) +
               (y_slack + 2 * z_slack - degree_gap) == 6)

    # Source-safe residual quota constraints are imposed above; the stronger
    # target-degree-13 quota remains conditional, as documented in the reserve audit.

    matchings, pvars = {}, {}
    tracks = [set(t) for t in TRACKS]
    if aligned_z01:
        # WLOG-labelled aligned cell: T0=K11, T1,T2,T3=K12.
        for i, track in enumerate(tracks):
            for u, v in pairs(sorted(track)):
                solver.add(col[edge(u, v)] == 0)
        for i, track in enumerate(tracks):
            expected_r = (1, 2, 2, 2)[i]
            solver.add(iff_count(residual[v] for v in track) == expected_r)

        # Exact nonexact-gap saturation for the aligned z=0,1 cell:
        # every exact color has 72 core edges (g_C=3), while color 11 has
        # 76 (g_D=7). The proof is in V47_Z01_NONEXACT_GAP_SATURATION.md.
        for c in exact:
            solver.add(core_edges[c] == 72)
        solver.add(core_edges[11] == 76)

        # Equality in the outside-H edge lower bound forces exactly one
        # color-11 edge from each o in O to each large K12 track T1,T2,T3.
        for o in O:
            for i in range(1, 4):
                solver.add(iff_count(col[edge(o, v)] == 11 for v in tracks[i]) == 1)

        # Let Z={o in O : o has no color-11 neighbor in T0}. Equality forces
        # Z subset A with |Z|=2 or 3, Z a clique, and every o outside Z has
        # exactly one color-11 neighbor in T0.
        d_a = iff_count(col[edge(u, v)] == 11 for u, v in pairs(A))
        d_t0 = {o: iff_count(col[edge(o, v)] == 11 for v in tracks[0]) for o in O}
        solver.add(z3.Or(d_a == 2, d_a == 3))
        for o in O:
            solver.add(d_t0[o] <= 1)
        solver.add(d_t0[PIVOT] == 1)
        solver.add(isum(d_t0[o] for o in O) + d_a == 14)
        for a, b in pairs(A):
            solver.add(z3.Implies(
                z3.And(d_t0[a] == 0, d_t0[b] == 0),
                col[edge(a, b)] == 11))

        # The independent-set hitting argument in
        # V47_Z01_OUTSIDE_COMPONENT_BIJECTION.md forces every D[A] component
        # to have identical D-neighborhoods in H, and fixes the O-degree
        # multiplicities seen from each target track.
        for a, b in pairs(A):
            is_d_edge = col[edge(a, b)] == 11
            for h in H:
                solver.add(z3.Implies(
                    is_d_edge,
                    (col[edge(a, h)] == 11) == (col[edge(b, h)] == 11)))

        for a in A:
            solver.add(z3.Implies(
                d_a == 2,
                iff_count(col[edge(a, b)] == 11 for b in A if b != a) <= 1))

        for i in range(1, 4):
            o_degree = {
                v: iff_count(col[edge(o, v)] == 11 for o in O)
                for v in tracks[i]
            }
            solver.add(z3.Implies(
                d_a == 2,
                z3.And(
                    iff_count(o_degree[v] == 1 for v in tracks[i]) == 10,
                    iff_count(o_degree[v] == 2 for v in tracks[i]) == 2)))
            solver.add(z3.Implies(
                d_a == 3,
                z3.And(
                    iff_count(o_degree[v] == 1 for v in tracks[i]) == 11,
                    iff_count(o_degree[v] == 3 for v in tracks[i]) == 1)))

        t0_o_degree = {
            v: iff_count(col[edge(o, v)] == 11 for o in O)
            for v in tracks[0]
        }
        solver.add(z3.Implies(
            d_a == 2,
            z3.And(
                iff_count(t0_o_degree[v] == 1 for v in tracks[0]) == 10,
                iff_count(t0_o_degree[v] == 2 for v in tracks[0]) == 1)))
        solver.add(z3.Implies(
            d_a == 3,
            iff_count(t0_o_degree[v] == 1 for v in tracks[0]) == 11))

        z_cross = iff_count(
            z3.And(residual[u], residual[v], col[edge(u, v)] == 0)
            for i in range(4) for j in range(i + 1, 4)
            for u in tracks[i] for v in tracks[j])
        solver.add(z_cross >= 0, z_cross <= 1)

        # Balanced-coloring cross-track constraints on H edges.
        for i in range(1, 4):
            for j in range(i + 1, 4):
                for u in tracks[i]:
                    solver.add(iff_count(col[edge(u, v)] == 0 for v in tracks[j]) <= 1)
                for v in tracks[j]:
                    solver.add(iff_count(col[edge(u, v)] == 0 for u in tracks[i]) <= 1)
            for u in tracks[0]:
                solver.add(iff_count(col[edge(u, v)] == 0 for v in tracks[i]) <= 1)

        # Explicit common-P factorization: 11 color matchings plus P on every pair.
        for i in range(4):
            for j in range(i + 1, 4):
                key = (i, j)
                matchings[key] = {}
                pvars[key] = {}
                for u in tracks[i]:
                    for v in tracks[j]:
                        e = edge(u, v)
                        pvars[key][e] = z3.Bool(f"P_{i}_{j}_{u}_{v}")
                        for c in range(1, 12):
                            matchings[key][c, e] = z3.Bool(f"M_{c}_{i}_{j}_{u}_{v}")
                            solver.add(z3.Implies(matchings[key][c, e], col[e] == c))
                        solver.add(
                            isum(z3.If(matchings[key][c, e], 1, 0)
                                 for c in range(1, 12)) +
                            z3.If(pvars[key][e], 1, 0) == 1)

                for c in range(1, 12):
                    for u in tracks[i]:
                        solver.add(iff_count(matchings[key][c, edge(u, v)]
                                             for v in tracks[j]) == 1)
                    if i != 0:
                        for v in tracks[j]:
                            solver.add(iff_count(matchings[key][c, edge(u, v)]
                                                 for u in tracks[i]) == 1)
                if i == 0:
                    for u in tracks[0]:
                        solver.add(iff_count(pvars[key][edge(u, v)]
                                             for v in tracks[j]) == 1)
                else:
                    for u in tracks[i]:
                        solver.add(iff_count(pvars[key][edge(u, v)]
                                             for v in tracks[j]) == 1)
                    for v in tracks[j]:
                        solver.add(iff_count(pvars[key][edge(u, v)]
                                             for u in tracks[i]) == 1)

                # Source-aligned matching: isolated K5 edges are selected;
                # all unselected exact-color P edges must lie inside G11.
                for c in exact:
                    for u in tracks[i]:
                        for v in tracks[j]:
                            e = edge(u, v)
                            same_isolated = z3.And(
                                comp[c][u] == comp[c][v],
                                comp[c][u] >= 0, comp[c][u] < 10)
                            solver.add(z3.Implies(same_isolated,
                                                  matchings[key][c, e]))
                            both_gadget = z3.And(gadget[c][u], gadget[c][v])
                            solver.add(z3.Implies(
                                z3.And(col[e] == c, z3.Not(both_gadget)),
                                matchings[key][c, e]))
                            solver.add(z3.Implies(
                                z3.And(pvars[key][e], col[e] == c),
                                both_gadget))
                    # The chosen matching preserves G11 membership.
                    for u in tracks[i]:
                        solver.add(
                            iff_count(z3.And(matchings[key][c, edge(u, v)],
                                             gadget[c][v]) for v in tracks[j]) ==
                            z3.If(gadget[c][u], 1, 0))
                    if i != 0:
                        for v in tracks[j]:
                            solver.add(
                                iff_count(z3.And(matchings[key][c, edge(u, v)],
                                                 gadget[c][u]) for u in tracks[i]) ==
                                z3.If(gadget[c][v], 1, 0))

        # In the aligned cell, source-mode plus Hall matching constraints force
        # exactly two G11 vertices on each K12 track. T0 may contain one or two:
        # the latter is the legitimate 8-vertex gadget-residual source mode.
        for c in exact:
            for i, track in enumerate(tracks):
                gadget_count = iff_count(gadget[c][v] for v in track)
                if i == 0:
                    solver.add(gadget_count >= 1, gadget_count <= 2)
                else:
                    solver.add(gadget_count == 2)
            t_count = isum(
                z3.If(z3.And(pvars[(0, i)][edge(u, v)], col[edge(u, v)] == c), 1, 0)
                for i in range(1, 4) for u in tracks[0] for v in tracks[i])
            solver.add(t_count <= 1)

        # Pair-projection multiplicity and cross-key injectivity on K12 x K12.
        for i in range(1, 4):
            for j in range(i + 1, 4):
                left_pairs = list(itertools.combinations(sorted(tracks[i]), 2))
                right_pairs = list(itertools.combinations(sorted(tracks[j]), 2))
                for aa in left_pairs:
                    for bb in right_pairs:
                        proj = {
                            c: z3.And(*([gadget[c][v] for v in aa] +
                                       [gadget[c][v] for v in bb]))
                            for c in exact
                        }
                        multiplicity = iff_count(proj[c] for c in exact)
                        solver.add(multiplicity <= 2)
                        p_hit = z3.Or([pvars[(i, j)][edge(u, v)]
                                       for u in aa for v in bb])
                        solver.add(z3.Implies(p_hit, multiplicity <= 1))
        for c1, c2 in itertools.combinations(exact, 2):
            same_projection = []
            for i, j in ((1, 2), (1, 3), (2, 3)):
                same_projection.append(z3.And(
                    *[gadget[c1][v] == gadget[c2][v]
                      for v in tracks[i] | tracks[j]]))
            solver.add(iff_count(same_projection) <= 1)

    variables = {
        "m": m, "solver": solver, "col": col, "exact": exact,
        "nonexact": nonexact, "source": source, "comp": comp,
        "xvar": xvar, "yvar": yvar, "a0var": a0var,
        "gadget": gadget, "component_outside": component_outside,
        "qblock": qblock, "residual": residual,
        "matchings": matchings, "pvars": pvars, "aligned_z01": aligned_z01,
    }
    return variables


def extract_candidate(vs, model):
    m = vs["m"]
    edge_rows = [[u, v, model.eval(vs["col"][edge(u, v)]).as_long()]
                 for u, v in pairs(range(N))]
    source_rows = []
    for c in vs["exact"]:
        comp = vs["comp"][c]
        blocks = []
        for k in range(12):
            blocks.append([v for v in range(N)
                           if model.eval(comp[v]).as_long() == k])
        a0 = [v for v in range(N) if z3.is_true(model.eval(vs["a0var"][c][v]))]
        source_rows.append({
            "color": c,
            "x": model.eval(vs["xvar"][c]).as_long(),
            "y": model.eval(vs["yvar"][c]).as_long(),
            "A0": a0,
            "components": blocks,
        })
    result = {
        "format": "EG617-Q32-FULLSUPPORT-v1",
        "m": m,
        "aligned_z01": vs["aligned_z01"],
        "edge_colors": edge_rows,
        "source": source_rows,
    }
    if vs["aligned_z01"]:
        match_data = {}
        for (i, j), pmap in vs["pvars"].items():
            p_edges = [[u, v] for (u, v), var in pmap.items()
                       if z3.is_true(model.eval(var))]
            mdata = {}
            for c in range(1, 12):
                mdata[str(c)] = [[u, v] for (cc, e), var in vs["matchings"][(i, j)].items()
                                 if cc == c and z3.is_true(model.eval(var))
                                 for u, v in [e]]
            match_data[f"{i}-{j}"] = {"P": p_edges, "M": mdata}
        result["matchings"] = match_data
    return result


def model_adj(model, col, color):
    adj = [0] * N
    for u, v in pairs(range(N)):
        if model.eval(col[edge(u, v)]).as_long() == color:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def add_alpha_cuts(vs, model):
    solver, col = vs["solver"], vs["col"]
    cuts = 0
    # The core target graph must have alpha at most four.
    adj0 = model_adj(model, col, 0)
    independent = find_independent_set(adj0, H, 5)
    if independent is not None:
        solver.add(z3.Or([col[edge(u, v)] == 0
                          for u, v in pairs(independent)]))
        cuts += 1
    # Every color in the balanced coloring must have alpha at most twelve
    # and clique number at most five. Add exact valid cuts for both violations.
    for c in range(12):
        adj = model_adj(model, col, c)
        independent = find_independent_set(adj, range(N), 13)
        if independent is not None:
            solver.add(z3.Or([col[edge(u, v)] == c
                              for u, v in pairs(independent)]))
            cuts += 1
        clique = find_clique(adj, range(N), 6)
        if clique is not None:
            solver.add(z3.Or([col[edge(u, v)] != c
                              for u, v in pairs(clique)]))
            cuts += 1
    return cuts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, choices=(8, 9, 10), required=True)
    parser.add_argument("--aligned-z01", action="store_true")
    parser.add_argument("--max-iterations", type=int, default=10000)
    parser.add_argument("--out-dir", default="q32_fullsupport_run")
    args = parser.parse_args()
    if z3 is None:
        print("Z3_SOLVER_UNAVAILABLE: install z3-solver; no SAT/UNSAT claim made")
        return 2
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    vs = build_model(args.m, args.aligned_z01)
    solver = vs["solver"]
    for iteration in range(1, args.max_iterations + 1):
        status = solver.check()
        if status == z3.unsat:
            (out_dir / "final_model.smt2").write_text(solver.to_smt2(), encoding="utf-8")
            try:
                (out_dir / "unsat_proof.txt").write_text(str(solver.proof()), encoding="utf-8")
                proof_status = "PROOF_EXPORTED"
            except Exception as exc:
                proof_status = f"PROOF_EXPORT_FAILED: {exc}"
            print(f"Q32_FULLSUPPORT_UNSAT_AFTER_{iteration-1}_ALPHA_CUTS")
            print(proof_status)
            return 1
        if status != z3.sat:
            (out_dir / "final_model.smt2").write_text(solver.to_smt2(), encoding="utf-8")
            print(f"Q32_SOLVER_UNKNOWN: {solver.reason_unknown()}")
            return 3
        model = solver.model()
        candidate = extract_candidate(vs, model)
        local_errors = verify_candidate(candidate, check_alpha=False, check_omega=False)
        if local_errors:
            (out_dir / "model_candidate_invalid.json").write_text(
                json.dumps(candidate, indent=2), encoding="utf-8")
            print("MODEL_ENCODING_AUDIT_FAILURE")
            print("\n".join(local_errors[:50]))
            return 4
        cuts = add_alpha_cuts(vs, model)
        if cuts == 0:
            errors = verify_candidate(candidate, check_alpha=True, check_omega=True)
            if errors:
                print("INDEPENDENT_VERIFIER_DISAGREEMENT")
                print("\n".join(errors[:50]))
                return 5
            path = out_dir / f"q32_fullsupport_m{args.m}" + ("_aligned_z01" if args.aligned_z01 else "") + ".json"
            path.write_text(json.dumps(candidate, indent=2), encoding="utf-8")
            (out_dir / "final_model.smt2").write_text(solver.to_smt2(), encoding="utf-8")
            print("Q32_FULLSUPPORT_SAT_CANDIDATE_VERIFIED")
            print(path)
            return 0
        print(f"iteration={iteration}; validity_cuts_added={cuts}")
    print(f"ITERATION_LIMIT_REACHED: {args.max_iterations}; no closure claim")
    (out_dir / "final_model.smt2").write_text(solver.to_smt2(), encoding="utf-8")
    return 3


if __name__ == "__main__":
    sys.exit(main())
