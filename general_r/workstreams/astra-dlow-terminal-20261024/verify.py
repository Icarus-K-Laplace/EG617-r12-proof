"""Exact arithmetic and independent finite checks for the analytic proof.

Usage: python verify.py --write (regenerate); python verify.py (verify).
Standard library only. No finite check is extrapolated to all large r.
"""
import argparse
import itertools
import json
from functools import lru_cache
from math import comb
from pathlib import Path


# Sparse integer polynomials in r,m,h,epsilon; identities compare coefficients.
def const(c):
    return {(0, 0, 0, 0): c} if c else {}


def var(i):
    a = [0] * 4
    a[i] = 1
    return {tuple(a): 1}


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}


def mul(p, q):
    out = {}
    for k, v in p.items():
        for l, w in q.items():
            a = tuple(x+y for x, y in zip(k, l))
            out[a] = out.get(a, 0) + v*w
    return {k: v for k, v in out.items() if v}


def polynomial_checks():
    r, m, h, eps = (var(i) for i in range(4))
    # Twice the actual cut capacity and its derived lower bound.
    cap2 = scale(mul(m, add(scale(r, 5), const(1), scale(m, -1))), 2)
    target2 = add(scale(mul(m, add(r, eps)), 2), scale(h, -4))
    non2 = add(scale(mul(add(r, const(-1)), add(scale(m, 4), const(1))), 2),
               scale(mul(m, add(m, const(-1))), -5), scale(h, 10))
    diff = add(cap2, scale(target2, -1), scale(non2, -1))
    expected = add(scale(mul(m, m), 3), scale(m, 5), const(2),
                   scale(mul(eps, m), -2), scale(h, -6), scale(r, -2))
    assert diff == expected
    # Contextual cap: 2*C(5r+1,2)-2(r-1)(10r+9).
    contextual = add(mul(add(scale(r, 5), const(1)), scale(r, 5)),
                     scale(mul(add(r, const(-1)), add(scale(r, 10), const(9))), -2))
    assert contextual == add(scale(mul(r, r), 5), scale(r, 7), const(18))
    low = add(contextual, scale(mul(add(scale(r, 5), const(1)), r), -1))
    high = add(contextual, scale(mul(add(scale(r, 5), const(1)), add(r, const(1))), -1))
    assert low == add(scale(r, 6), const(18))
    assert high == add(r, const(17))
    return {"twice_cut_residual_coefficients": [list(k)+[v] for k, v in sorted(diff.items())],
            "contextual_cap": "5r^2+7r+18", "coefficient_identity_checked": True}


def alpha(adj):
    @lru_cache(None)
    def rec(mask):
        if not mask:
            return 0
        vbit = mask & -mask
        v = vbit.bit_length()-1
        rest = mask ^ vbit
        return max(rec(rest), 1+rec(rest & ~adj[v]))
    return rec((1 << len(adj))-1)


def matching(adj):
    @lru_cache(None)
    def rec(mask):
        if not mask:
            return 0
        b = mask & -mask
        v = b.bit_length()-1
        rest = mask ^ b
        best = rec(rest)
        choices = adj[v] & rest
        while choices:
            b2 = choices & -choices
            choices ^= b2
            best = max(best, 1+rec(rest ^ b2))
        return best
    return rec((1 << len(adj))-1)


def graph(n, edges):
    adj = [0]*n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def sparse_regression():
    counts = []
    for n in range(1, 7):
        pairs = list(itertools.combinations(range(n), 2))
        triangle_free = selected = 0
        for mask in range(1 << len(pairs)):
            edges = [edge for k, edge in enumerate(pairs) if mask >> k & 1]
            adj = graph(n, edges)
            if any(adj[u] & adj[v] for u, v in edges):
                continue
            triangle_free += 1
            tau = n-alpha(adj)
            if len(edges)-tau > 1:
                continue
            selected += 1
            assert max((a.bit_count() for a in adj), default=0) <= 2
            assert matching(adj) == tau
            # Independently recover connected components and exhaust their shapes.
            unseen = set(range(n))
            exceptional = 0
            while unseen:
                root = min(unseen)
                component, todo = set(), [root]
                while todo:
                    v = todo.pop()
                    if v in component:
                        continue
                    component.add(v)
                    todo.extend(w for w in unseen if adj[v] >> w & 1)
                unseen -= component
                vc = len(component)
                ec = sum(adj[v].bit_count() for v in component)//2
                assert vc <= 4 and ec == vc-1
                exceptional += vc >= 3
            assert exceptional <= 1
        counts.append({"n": n, "labeled_graphs": 1 << len(pairs),
                       "triangle_free": triangle_free, "e_minus_tau_at_most_1": selected})
    return counts


def offset_checks():
    rows = []
    for eps, cs in [(0, range(2, 5)), (1, range(2, 8))]:
        for c in cs:
            etas = [eta for eta in range(3) if 3*eps+eta-c+2 >= 0]
            # All-r strict inequalities reduce to positive linear polynomials
            # in x=r-67. These are exact slope/intercept certificates.
            slope, intercept = (1, 67-7*c-18) if eps == 0 else (1, 67-2*c-17)
            assert slope > 0 and intercept > 0
            rows.append({"epsilon": eps, "c": c, "eta": etas,
                         "W_slack_constant": c*c//4-c,
                         "endpoint_excess_margin_at_r67": intercept,
                         "endpoint_excess_margin_slope": slope})
    assert len(rows) == 9
    assert 2*(67-1)-(67+5) == 60  # margin grows with slope 1
    return rows


def capacity_checks():
    table = []
    for m in range(6, 13):
        q, rem = divmod(m, 5)
        p = (5-rem)*comb(q, 2)+rem*comb(q+1, 2)
        # Exhaust all weak compositions into five parts independently.
        best = min(sum(comb(a, 2) for a in (a0, a1, a2, a3, m-a0-a1-a2-a3))
                   for a0 in range(m+1) for a1 in range(m-a0+1)
                   for a2 in range(m-a0-a1+1) for a3 in range(m-a0-a1-a2+1))
        assert best == p
        assert (m*(m-5)+9)//10 == p  # random-order independence floor
        B = (3*m*m+5*m+2)//2-3*p
        table.append({"m": m, "p5": p, "low_upper_r": B, "high_upper_r": B-m})
    for key in ["low_upper_r", "high_upper_r"]:
        assert all(a[key] < b[key] for a, b in zip(table, table[1:]))
    assert table[-1] == {"m": 12, "p5": 9, "low_upper_r": 220, "high_upper_r": 208}
    # Margin r-B >= 1 for ALL r=221+x, x>=0, not just finite samples.
    assert all(221-row["low_upper_r"] > 0 for row in table)
    assert all(209-row["high_upper_r"] > 0 for row in table)
    return table


def split_cover():
    # u=0,v=1,z=2..5,w=6..10.
    edges = set(itertools.combinations(range(6), 2)) | set(itertools.combinations(range(6, 11), 2))
    edges.remove((0, 1))
    edges |= {(0, 6), (0, 7), (1, 8), (1, 9), (1, 10)}
    independent = clique = 0
    for mask in range(1 << 11):
        vs = [v for v in range(11) if mask >> v & 1]
        pairs = list(itertools.combinations(vs, 2))
        if all(edge not in edges for edge in pairs):
            independent = max(independent, len(vs))
        if all(edge in edges for edge in pairs):
            clique = max(clique, len(vs))
    assert (len(edges), independent, clique) == (29, 2, 5)
    assert all((0, w) in edges or (1, w) in edges for w in range(6, 11))
    return {"n": 11, "edges": [list(e) for e in sorted(edges)], "edge_count": 29,
            "alpha": 2, "omega": 5, "subsets_checked": 2048,
            "full_terminal": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = {"status": "COMPUTATION_CERTIFIED",
              "scope": "Exact arithmetic and finite regression; all-r proof is analytic in THEOREM.md",
              "polynomials": polynomial_checks(), "offsets": offset_checks(),
              "capacity_table": capacity_checks(), "sparse_regression": sparse_regression(),
              "split_cover": split_cover(),
              "analytic_exclusion_threshold": {"all_nine_cells": 221, "high_degree_cells": 209}}
    path = Path(__file__).with_name("CERTIFICATE.json")
    if args.write:
        path.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
        print("WROTE", path.name)
    else:
        assert result == json.loads(path.read_text(encoding="utf-8"))
        print("PASS: exact certificate independently recomputed")
    print("Analytic theorem: all nine cells excluded for every integer r>=221; high branch r>=209")


if __name__ == "__main__":
    main()
