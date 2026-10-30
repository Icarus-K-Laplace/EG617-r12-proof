#!/usr/bin/env python3
"""Build and solve the exact source-labelled K_61 Q32 CSP for m=8,9 only.

The model preserves every source-correct Type-I outside placement and the
canonical E408 color vector. Pairwise pivot perfect-matching existence is
forced by exact alpha(H) separation and independently verified. It adds exact
per-block degree-ledger identities and lazy matching-composition cuts. It deliberately does not import the
m=10-only aligned 3+7 common-P track normal form.

Requires z3-solver. Alpha and clique constraints are separated exactly by
searching every proposed model for an independent 5-set in H, an independent
13-set in each color, and a monochromatic K6. SAT is accepted only after the
independent candidate verifier passes.
"""
from __future__ import annotations
import argparse
import itertools
import json
import platform
import sys
from pathlib import Path

try:
    import z3
except ImportError:
    z3 = None

from verify_q32_fullsupport_candidate import (
    ALL_COLORS, H, N, O, PIVOT, A, edge, pairs,
    expected_color_counts, find_independent_set, find_clique, verify_candidate,
)



def isum(items):
    return z3.Sum(list(items))


def iff_count(predicates):
    return isum(z3.If(p, 1, 0) for p in predicates)


def build_model(m):
    if z3 is None:
        raise RuntimeError("z3-solver is not installed; install z3-solver before solving")
    if m not in (8, 9):
        raise ValueError("this isolated workstream handles only m=8,9")

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
    # Tight-part exclusion theorem: any 69/70 near-Turan partition in H
    # yields either an independent 5-set or a K7. Since the accepted Q32
    # candidates satisfy alpha(H)<=4 and omega(H)<=5, every non-target color
    # must therefore have at least 71 H-edges. This is a valid strengthening
    # of the lazy alpha/omega search, not an m=10-specific import.
    for c in range(1, 12):
        solver.add(core_edges[c] >= 71)
    for c in exact:
        solver.add(core_edges[c] <= 75)
    solver.add(isum(core_edges[c] - 69 for c in range(1, 12)) == 37)

    # Source-correct exact-129 core-edge accounting. The former conditional
    # 69/70 near-Turan partition variables are now unnecessary: the tight-part
    # exclusion theorem above rules out that entire layer for every valid H.
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

    # Exact pivot-p degree-excess ledger. The 13 pA edges are target-colored;
    # all 47 pH edges are distributed among target, exact, and nonexact colors.
    # Each exact Type-I color contributes at least four p-edges, and each
    # nonexact color contributes its registered pointwise degree floor.
    p_degree = {
        c: iff_count(col[edge(PIVOT, v)] == c for v in range(N) if v != PIVOT)
        for c in range(12)
    }
    p_floor = {
        c: (4 if color_counts[c] == 130 else 3)
        for c in nonexact
    }
    p_slack_limit = {8: 3, 9: 4}[m]
    p_excess = (
        p_degree[0] - 13
        + isum(p_degree[c] - 4 for c in exact)
        + isum(p_degree[c] - p_floor[c] for c in nonexact)
    )
    solver.add(p_degree[0] >= 13)
    for c in exact:
        solver.add(p_degree[c] >= 4)
        # p has degree exactly four in C iff it lies in an isolated K5
        # factor. If p=x or p lies in Ns/Nt, the source gadget adds >=1
        # further p-edge; pA target ownership forces that edge into H.
        p_isolated_factor = z3.And(xvar[c] != PIVOT, comp[c][PIVOT] < 10)
        solver.add((p_degree[c] == 4) == p_isolated_factor)
    solver.add(p_excess == p_slack_limit)
    solver.add(iff_count(p_degree[c] >= 5 for c in exact) <= p_slack_limit)
    solver.add(iff_count(p_degree[c] == 4 for c in exact) >= m - p_slack_limit)

    # Safe all-color gadget reserve. For residual z, target degree d_0(z)>=
    # d_H(z)>=12; each exact color contributes >=4 plus one for gadget membership,
    # and the nonexact floors sum to L_m=(12,7,3). This yields q_z<=(4,5,5).
    # The stronger (3,4,4) cap is only conditional on d_0(z)>=13.
    safe_q_cap = {8: 4, 9: 5}[m]
    conditional_q_cap = {8: 3, 9: 4}[m]
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
    p4_floor = {8: 21, 9: 10}[m]
    degree_gap = {8: 18, 9: 13}[m]

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

    # Pairwise pivot matching existence is forced by alpha(H)<=4:
    # each Q_i,Q_j pair is bipartite with alpha<=4, so Kőnig gives a
    # perfect matching. We do not add redundant per-edge matching-choice
    # Booleans; exact alpha separation and the independent verifier check it.
    pair_count = {}
    for c1, c2 in itertools.combinations(exact, 2):
        key = (c1, c2)
        pair_count[key] = iff_count(
            z3.And(
                z3.Or(z3.And(qblock[c1][u], qblock[c2][v]),
                      z3.And(qblock[c1][v], qblock[c2][u])),
                col[edge(u, v)] == 0)
            for u, v in pairs(H))
        solver.add(pair_count[key] >= 4)

    # Explicit per-block six-unit degree ledger.
    # X_i = sum of excess H-edges from Q_i to other pivot blocks;
    # Y_i = excess H-edges from Q_i to R beyond one per residual vertex;
    # epsilon_i = total degree excess on Q_i.
    # The identity X_i + Y_i = 5 + epsilon_i is exact.
    for c in exact:
        x_i = isum(
            pair_count[(min(c, d), max(c, d))] - 4
            for d in exact if d != c)
        qr_i = iff_count(
            z3.And(
                z3.Or(z3.And(qblock[c][u], residual[v]),
                      z3.And(qblock[c][v], residual[u])),
                col[edge(u, v)] == 0)
            for u, v in pairs(H))
        y_i = qr_i - n_residual
        eps_i = isum(z3.If(qblock[c][v], h_degree[v] - 12, 0) for v in H)
        solver.add(y_i >= 0, x_i + y_i == 5 + eps_i)

    # Pointwise no-independent-5 constraints at each pivot block pair:
    # every vertex of Q_i must meet every other Q_j.
    for c1, c2 in itertools.combinations(exact, 2):
        for u in H:
            solver.add(z3.Implies(
                qblock[c1][u],
                iff_count(z3.And(qblock[c2][v], col[edge(u, v)] == 0)
                          for v in H if v != u) >= 1))
            solver.add(z3.Implies(
                qblock[c2][u],
                iff_count(z3.And(qblock[c1][v], col[edge(u, v)] == 0)
                          for v in H if v != u) >= 1))

    variables = {
        "m": m, "solver": solver, "col": col, "exact": exact,
        "nonexact": nonexact, "source": source, "comp": comp, "p_degree": p_degree, "p_excess": p_excess,
        "xvar": xvar, "yvar": yvar, "a0var": a0var,
        "gadget": gadget, "component_outside": component_outside,
        "qblock": qblock, "residual": residual,
        "pair_count": pair_count, "near_turan_part": near_turan_part, "source_core_count": source_core_count,
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
        "edge_colors": edge_rows,
        "source": source_rows,
    }
    return result


def model_adj(model, col, color):
    adj = [0] * N
    for u, v in pairs(range(N)):
        if model.eval(col[edge(u, v)]).as_long() == color:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj



def add_pivot_matching_composition_cuts(vs, model):
    """Add guarded, source-valid light-pair matching-composition cuts.

    A composition is forced only while the *same* three pivot blocks remain
    selected and both incident pairs remain exactly four-edge pairs. The
    guards are essential: an unconditional cut inferred from one model could
    otherwise exclude a legal solution in which an incident pair becomes
    heavy or the source-selected pivot blocks change.
    """
    solver, col = vs["solver"], vs["col"]
    exact = vs["exact"]
    qblock = vs["qblock"]
    pair_count = vs["pair_count"]
    blocks = {
        c: [v for v in H if z3.is_true(model.eval(qblock[c][v]))]
        for c in exact
    }
    if any(len(blocks[c]) != 4 for c in exact):
        return 0

    light_maps = {}
    for c1, c2 in itertools.combinations(exact, 2):
        key = (c1, c2)
        if model.eval(pair_count[key]).as_long() != 4:
            continue
        mapping = {}
        for u in blocks[c1]:
            neighbors = [
                v for v in blocks[c2]
                if model.eval(col[edge(u, v)]).as_long() == 0
            ]
            if len(neighbors) != 1:
                mapping = {}
                break
            mapping[u] = neighbors[0]
        if len(mapping) == 4 and len(set(mapping.values())) == 4:
            light_maps[key] = mapping

    def map_vertex(c_from, c_to, u):
        key = (min(c_from, c_to), max(c_from, c_to))
        mapping = light_maps[key]
        if c_from < c_to:
            return mapping.get(u)
        inverse = {v: a for a, v in mapping.items()}
        return inverse.get(u)

    def anchor_guard(anchor, c2, c3, map2, map3):
        terms = [
            pair_count[(min(anchor, c2), max(anchor, c2))] == 4,
            pair_count[(min(anchor, c3), max(anchor, c3))] == 4,
        ]
        for a in blocks[anchor]:
            b, c = map2[a], map3[a]
            terms.extend([
                qblock[anchor][a], qblock[c2][b], qblock[c3][c],
                col[edge(a, b)] == 0,
                col[edge(a, c)] == 0,
            ])
        return z3.And(*terms)

    # Exact finite K4,4 lookup: min edges needed to contain t distinct
    # perfect matchings, for t=1,...,24. Independently replayed by
    # verify_m89_pivot_matching.py over all 2^16 bipartite edge sets.
    mu4 = (0, 4, 6, 8, 8, 10, 10, 12, 12, 12, 13, 13, 14,
           14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16)

    cuts = 0
    for c2, c3 in itertools.combinations(exact, 2):
        # Each distinct composition matching is grouped with every anchor
        # that currently forces it. Its guard is an OR, so the implication
        # remains valid if one of several equivalent anchors later changes.
        compositions = {}
        for anchor in exact:
            if anchor == c2 or anchor == c3:
                continue
            key2 = (min(anchor, c2), max(anchor, c2))
            key3 = (min(anchor, c3), max(anchor, c3))
            if key2 not in light_maps or key3 not in light_maps:
                continue
            map2 = {a: map_vertex(anchor, c2, a) for a in blocks[anchor]}
            map3 = {a: map_vertex(anchor, c3, a) for a in blocks[anchor]}
            if any(v is None for v in map2.values()) or any(v is None for v in map3.values()):
                continue
            mapping = {}
            for u in blocks[c2]:
                middle = map_vertex(c2, anchor, u)
                v = map_vertex(anchor, c3, middle) if middle is not None else None
                if v is None:
                    mapping = {}
                    break
                mapping[u] = v
            if len(mapping) != 4 or len(set(mapping.values())) != 4:
                continue
            signature = tuple((u, mapping[u]) for u in sorted(blocks[c2]))
            guard = anchor_guard(anchor, c2, c3, map2, map3)
            compositions.setdefault(signature, {"mapping": mapping, "guards": []})
            compositions[signature]["guards"].append(guard)

        active_guards = []
        for item in compositions.values():
            guard = z3.Or(*item["guards"])
            if not z3.is_true(model.eval(guard)):
                continue
            active_guards.append(guard)
            for u, v in item["mapping"].items():
                e = edge(u, v)
                if model.eval(col[e]).as_long() != 0:
                    solver.add(z3.Implies(guard, col[e] == 0))
                    cuts += 1

        # If all t distinct compositions remain forced, their union must
        # contain at least mu_4(t) target edges. This implication is guarded
        # by the conjunction of the corresponding composition conditions.
        t = len(active_guards)
        if t and model.eval(pair_count[(c2, c3)]).as_long() < mu4[t]:
            solver.add(z3.Implies(
                z3.And(*active_guards),
                pair_count[(c2, c3)] >= mu4[t]))
            cuts += 1
    return cuts

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
    parser.add_argument("--m", type=int, choices=(8, 9), required=True)
    parser.add_argument("--max-iterations", type=int, default=10000)
    parser.add_argument("--out-dir", default="q32_fullsupport_m89_run")
    args = parser.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / "run_manifest.json"
    log_path = out_dir / "run.log"

    def log(message):
        with log_path.open("a", encoding="utf-8") as stream:
            stream.write(message + "\n")

    manifest = {
        "workstream": "q32-v47-m89-final-chat-20261030",
        "m": args.m,
        "max_iterations": args.max_iterations,
        "python_version": platform.python_version(),
        "z3_version": z3.get_version_string() if z3 is not None else None,
        "color_counts": expected_color_counts(args.m),
        "model_file": "q32_fullsupport_m89_solver.py",
        "candidate_verifier": "verify_q32_fullsupport_candidate.py",
        "status": "INITIALIZED",
    }
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    if z3 is None:
        manifest["status"] = "NOT_RUN_Z3_SOLVER_UNAVAILABLE"
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        log("Z3_SOLVER_UNAVAILABLE: install z3-solver; no SAT/UNSAT claim made")
        print("Z3_SOLVER_UNAVAILABLE: install z3-solver; no SAT/UNSAT claim made")
        return 2

    vs = build_model(args.m)
    solver = vs["solver"]
    for iteration in range(1, args.max_iterations + 1):
        status = solver.check()
        log(f"iteration={iteration}; solver_status={status}")
        if status == z3.unsat:
            (out_dir / "final_model.smt2").write_text(solver.to_smt2(), encoding="utf-8")
            try:
                (out_dir / "unsat_proof.txt").write_text(str(solver.proof()), encoding="utf-8")
                proof_status = "Z3_PROOF_EXPORTED_REQUIRES_INDEPENDENT_REPLAY"
            except Exception as exc:
                proof_status = f"PROOF_EXPORT_FAILED: {exc}"
            manifest["status"] = "UNSAT_CANDIDATE_REQUIRES_INDEPENDENT_REPLAY"
            manifest["iterations"] = iteration
            manifest["proof_status"] = proof_status
            manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            log(f"UNSAT_CANDIDATE; {proof_status}")
            print(f"Q32_FULLSUPPORT_M{args.m}_UNSAT_CANDIDATE_AFTER_{iteration-1}_VALIDITY_CUTS")
            print(proof_status)
            return 1
        if status != z3.sat:
            (out_dir / "final_model.smt2").write_text(solver.to_smt2(), encoding="utf-8")
            manifest["status"] = "UNKNOWN"
            manifest["iterations"] = iteration
            manifest["reason_unknown"] = solver.reason_unknown()
            manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            log(f"UNKNOWN: {solver.reason_unknown()}")
            print(f"Q32_SOLVER_UNKNOWN: {solver.reason_unknown()}")
            return 3
        model = solver.model()
        candidate = extract_candidate(vs, model)
        local_errors = verify_candidate(candidate, check_alpha=False, check_omega=False)
        if local_errors:
            (out_dir / "model_candidate_invalid.json").write_text(
                json.dumps(candidate, indent=2), encoding="utf-8")
            manifest["status"] = "MODEL_ENCODING_AUDIT_FAILURE"
            manifest["iterations"] = iteration
            manifest["errors"] = local_errors[:50]
            manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            log("MODEL_ENCODING_AUDIT_FAILURE")
            return 4
        cuts = add_alpha_cuts(vs, model)
        cuts += add_pivot_matching_composition_cuts(vs, model)
        if cuts == 0:
            errors = verify_candidate(candidate, check_alpha=True, check_omega=True)
            if errors:
                manifest["status"] = "INDEPENDENT_VERIFIER_DISAGREEMENT"
                manifest["iterations"] = iteration
                manifest["errors"] = errors[:50]
                manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
                log("INDEPENDENT_VERIFIER_DISAGREEMENT")
                print("INDEPENDENT_VERIFIER_DISAGREEMENT")
                print("\n".join(errors[:50]))
                return 5
            candidate_path = out_dir / f"q32_fullsupport_m{args.m}.json"
            candidate_path.write_text(json.dumps(candidate, indent=2), encoding="utf-8")
            (out_dir / "final_model.smt2").write_text(solver.to_smt2(), encoding="utf-8")
            manifest["status"] = "SAT_CANDIDATE_VERIFIED_NOT_A_CLOSURE"
            manifest["iterations"] = iteration
            manifest["candidate_file"] = candidate_path.name
            manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            log(f"SAT_CANDIDATE_VERIFIED: {candidate_path.name}")
            print("Q32_FULLSUPPORT_SAT_CANDIDATE_VERIFIED")
            print(candidate_path)
            return 0
        log(f"iteration={iteration}; validity_cuts_added={cuts}")
        print(f"iteration={iteration}; validity_cuts_added={cuts}")
    manifest["status"] = "ITERATION_LIMIT_REACHED"
    manifest["iterations"] = args.max_iterations
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (out_dir / "final_model.smt2").write_text(solver.to_smt2(), encoding="utf-8")
    log(f"ITERATION_LIMIT_REACHED: {args.max_iterations}; no closure claim")
    print(f"ITERATION_LIMIT_REACHED: {args.max_iterations}; no closure claim")
    return 3


if __name__ == "__main__":
    sys.exit(main())
