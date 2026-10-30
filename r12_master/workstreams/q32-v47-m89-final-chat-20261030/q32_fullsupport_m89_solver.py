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


def build_model(m):
    if z3 is None:
        raise RuntimeError("z3-solver is not installed; install z3-solver before solving")
    if m not in (8, 9):
        raise ValueError("m must be 8, 9, or 10")

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

    # Global pivot-block perfect matchings.
    # For every pair of disjoint independent pivot K4s, alpha(H)<=4 implies
    # a perfect matching of target edges between them (Kőnig).
    pair_count, pair_match = {}, {}
    for c1, c2 in itertools.combinations(exact, 2):
        key = (c1, c2)
        pair_count[key] = iff_count(
            z3.And(
                z3.Or(z3.And(qblock[c1][u], qblock[c2][v]),
                      z3.And(qblock[c1][v], qblock[c2][u])),
                col[edge(u, v)] == 0)
            for u, v in pairs(H))
        solver.add(pair_count[key] >= 4)

        pair_match[key] = {}
        for u, v in pairs(H):
            e = edge(u, v)
            between = z3.Or(
                z3.And(qblock[c1][u], qblock[c2][v]),
                z3.And(qblock[c1][v], qblock[c2][u]))
            chosen = z3.Bool(f"pivot_match_{c1}_{c2}_{u}_{v}")
            pair_match[key][e] = chosen
            solver.add(z3.Implies(chosen, z3.And(between, col[e] == 0)))

        # A selected perfect matching saturates exactly the eight block vertices.
        for u in H:
            incident = [pair_match[key][edge(u, v)] for v in H if v != u]
            solver.add(iff_count(incident) ==
                       z3.If(z3.Or(qblock[c1][u], qblock[c2][u]), 1, 0))

        # If the pair has exactly four H-edges, its matching is unique and
        # equals the entire H-edge graph between the two pivot blocks.
        for u, v in pairs(H):
            e = edge(u, v)
            between_h = z3.And(
                z3.Or(z3.And(qblock[c1][u], qblock[c2][v]),
                      z3.And(qblock[c1][v], qblock[c2][u])),
                col[e] == 0)
            solver.add(z3.Implies(pair_count[key] == 4,
                                  pair_match[key][e] == between_h))

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

    pair_match = pair_match

    variables = {
        "m": m, "solver": solver, "col": col, "exact": exact,
        "nonexact": nonexact, "source": source, "comp": comp,
        "xvar": xvar, "yvar": yvar, "a0var": a0var,
        "gadget": gadget, "component_outside": component_outside,
        "qblock": qblock, "residual": residual,
        "pair_count": pair_count, "pair_match": pair_match,
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
    """Add the exact light-pair matching-composition consequences of alpha(H)<=4.

    If e_H(Q_a,Q_b)=e_H(Q_a,Q_c)=4, both bipartite graphs are unique
    perfect matchings. For each u in Q_a, if v,w are its matched vertices,
    then vw must be an H-edge; otherwise Q_a\\{u} union {v,w} is an
    independent 5-set. This is a lazy, source-safe strengthening.
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

    cuts = 0
    seen = set()
    for anchor in exact:
        others = [c for c in exact if c != anchor]
        for c2, c3 in itertools.combinations(others, 2):
            key2 = (min(anchor, c2), max(anchor, c2))
            key3 = (min(anchor, c3), max(anchor, c3))
            if key2 not in light_maps or key3 not in light_maps:
                continue
            for u in blocks[anchor]:
                v = map_vertex(anchor, c2, u)
                w = map_vertex(anchor, c3, u)
                if v is None or w is None:
                    continue
                e = edge(v, w)
                if e in seen:
                    continue
                seen.add(e)
                if model.eval(col[e]).as_long() != 0:
                    solver.add(col[e] == 0)
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
    parser.add_argument("--out-dir", default="q32_fullsupport_run")
    args = parser.parse_args()
    if z3 is None:
        print("Z3_SOLVER_UNAVAILABLE: install z3-solver; no SAT/UNSAT claim made")
        return 2
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    vs = build_model(args.m)
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
            print(f"Q32_FULLSUPPORT_M89_UNSAT_AFTER_{iteration-1}_VALIDITY_CUTS")
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
        cuts += add_pivot_matching_composition_cuts(vs, model)
        if cuts == 0:
            errors = verify_candidate(candidate, check_alpha=True, check_omega=True)
            if errors:
                print("INDEPENDENT_VERIFIER_DISAGREEMENT")
                print("\n".join(errors[:50]))
                return 5
            path = out_dir / f"q32_fullsupport_m{args.m}.json"
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
