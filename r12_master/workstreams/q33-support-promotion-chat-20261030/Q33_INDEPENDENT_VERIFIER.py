#!/usr/bin/env python3
"""Source-correct Q33 component-only support/reserve verifier.

For each exact-129 color, choose seven guaranteed isolated-K5 component
witnesses. Thus every selected witness is a component K4 and h=0. The
remaining three K5 components have variable core sizes c_i in {0,...,4}.

This verifies a necessary aggregate U/W profile relaxation only. It does
not encode labelled vertices, cross-color pair intersections, or the full
degree ledger, and is not a graph-level Q33 UNSAT certificate.
"""
from itertools import product
from math import comb

SUPPORT_MIN = {8: 31, 9: 32, 10: 34}
CORE_SPLITS = [(c, k) for c in range(5) for k in range(c + 1)]


def p_k(n, k):
    """Minimum edges in an n-vertex graph with independence number <= k."""
    if n <= k:
        return 0
    q, r = divmod(n, k)
    return (k-r) * comb(q, 2) + r * comb(q+1, 2)


def t_k(n, k):
    """Turán maximum for a K_(k+1)-free graph."""
    return comb(n, 2) - p_k(n, k)


def l_u_max(v):
    """Upper bound on e(complement(H[U])) from the 284-edge core ledger."""
    w = 47 - v
    if w == 0:
        return comb(47, 2) - 284
    return comb(v, 2) - 280 + 12*w - p_k(w, 4)


def options_product(v):
    """Cartesian-product enumeration of one exact color's 3 residual K5s."""
    out = set()
    for comps in product(CORE_SPLITS, repeat=3):
        csum = sum(c for c, _ in comps)
        ksum = sum(k for _, k in comps)
        if not 8 <= csum <= 12:
            continue
        gadget_core = 19 - csum
        gadget_u = v - 28 - ksum
        if not 0 <= gadget_u <= gadget_core:
            continue
        gadget_w = gadget_core - gadget_u
        comp_u = sum(comb(k, 2) for _, k in comps)
        comp_w = sum(comb(c-k, 2) for c, k in comps)
        out.add((comp_u + p_k(gadget_u, 2),
                 comp_w + p_k(gadget_w, 2)))
    return out


def options_recursive(v):
    """Independent recursive state enumeration of the same per-color options."""
    states = {(0, 0, 0, 0)}  # (sum c_i, sum k_i, U-pairs, W-pairs)
    for _ in range(3):
        nxt = set()
        for csum, ksum, u_cost, w_cost in states:
            for c, k in CORE_SPLITS:
                nxt.add((csum+c, ksum+k,
                         u_cost+comb(k, 2),
                         w_cost+comb(c-k, 2)))
        states = nxt

    out = set()
    for csum, ksum, comp_u, comp_w in states:
        if not 8 <= csum <= 12:
            continue
        gadget_core = 19 - csum
        gadget_u = v - 28 - ksum
        if not 0 <= gadget_u <= gadget_core:
            continue
        gadget_w = gadget_core - gadget_u
        out.add((comp_u + p_k(gadget_u, 2),
                 comp_w + p_k(gadget_w, 2)))
    return out


def global_screen(m, v, one_color_options):
    """Combine m exact-color costs under the U and W reserve budgets."""
    n = 11 - m
    w = 47 - v
    budget_u = l_u_max(v) - 42*m - n*p_k(v, 12)
    budget_w = t_k(w, 4) - n*p_k(w, 12)
    if budget_u < 0 or budget_w < 0:
        return budget_u, budget_w, 0, False

    states = {(0, 0)}
    for _ in range(m):
        states = {
            (u+a, z+b)
            for u, z in states
            for a, b in one_color_options
            if u+a <= budget_u and z+b <= budget_w
        }
        if not states:
            break
    return budget_u, budget_w, len(states), bool(states)


def main():
    options_by_v = {}
    for v in range(31, 48):
        a = options_product(v)
        b = options_recursive(v)
        assert a == b, (v, sorted(a ^ b))
        options_by_v[v] = a

    all_rows = {}
    for m, v_min in SUPPORT_MIN.items():
        rows = []
        for v in range(v_min, 48):
            bu, bw, nstates, feasible = global_screen(m, v, options_by_v[v])
            rows.append((v, bu, bw, len(options_by_v[v]), nstates, feasible))
        all_rows[m] = rows

    expected_excluded = {
        8: list(range(31, 39)),
        9: list(range(32, 40)),
        10: list(range(34, 41)),
    }
    expected_survivors = {
        8: list(range(39, 48)),
        9: list(range(40, 48)),
        10: list(range(41, 48)),
    }
    for m, rows in all_rows.items():
        excluded = [v for v, _, _, _, _, ok in rows if not ok]
        survivors = [v for v, _, _, _, _, ok in rows if ok]
        assert excluded == expected_excluded[m], (m, excluded)
        assert survivors == expected_survivors[m], (m, survivors)

    print("Q33 COMPONENT-ONLY VARIABLE-CORE SCREEN: PASS")
    print("Per-color Cartesian product and recursive generators agree for v=31..47.")
    for m, rows in all_rows.items():
        print(f"m={m}")
        for v, bu, bw, option_count, state_count, feasible in rows:
            print(f"  v={v}: BU={bu}, BW={bw}, options={option_count}, "
                  f"aggregate_states={state_count}, "
                  f"{'PROFILE_FEASIBLE' if feasible else 'EXCLUDED'}")
    print("All 47 registered (m,v) cells checked.")
    print("Scope: necessary aggregate profile screen only; no graph realization; "
          "Q33 remains OPEN.")


if __name__ == "__main__":
    main()
