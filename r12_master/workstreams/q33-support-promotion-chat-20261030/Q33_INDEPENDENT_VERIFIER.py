#!/usr/bin/env python3
"""Source-correct Q33 component-only support/reserve verifier.

Choose seven guaranteed isolated-K5 component witnesses per exact-129 color,
so h=0. A shell-capacity lemma forces the three unselected component core
sizes to sum to 9..12. This verifies a necessary aggregate U/W profile
relaxation, not a graph-level Q33 UNSAT certificate.
"""
from itertools import product
from math import comb

SUPPORT_MIN = {8: 31, 9: 32, 10: 34}
CORE_SPLITS = [(c, k) for c in range(5) for k in range(c + 1)]


def p_k(n, k):
    if n <= k:
        return 0
    q, r = divmod(n, k)
    return (k-r) * comb(q, 2) + r * comb(q+1, 2)


def t_k(n, k):
    return comb(n, 2) - p_k(n, k)


def l_u_max(v):
    w = 47 - v
    if w == 0:
        return comb(47, 2) - 284
    return comb(v, 2) - 280 + 12*w - p_k(w, 4)


def options_product(v):
    out = set()
    for comps in product(CORE_SPLITS, repeat=3):
        csum = sum(c for c, _ in comps)
        ksum = sum(k for _, k in comps)
        if not 9 <= csum <= 12:
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
    states = {(0, 0, 0, 0)}
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
        if not 9 <= csum <= 12:
            continue
        gadget_core = 19 - csum
        gadget_u = v - 28 - ksum
        if not 0 <= gadget_u <= gadget_core:
            continue
        gadget_w = gadget_core - gadget_u
        out.add((comp_u + p_k(gadget_u, 2),
                 comp_w + p_k(gadget_w, 2)))
    return out


def min_w_shapes(v):
    rows = []
    min_cost = None
    for comps in product(CORE_SPLITS, repeat=3):
        csum = sum(c for c, _ in comps)
        ksum = sum(k for _, k in comps)
        if not 9 <= csum <= 12:
            continue
        gadget_core = 19 - csum
        gadget_u = v - 28 - ksum
        if not 0 <= gadget_u <= gadget_core:
            continue
        gadget_w = gadget_core - gadget_u
        comp_w = sum(comb(c-k, 2) for c, k in comps)
        cost = comp_w + p_k(gadget_w, 2)
        if min_cost is None or cost < min_cost:
            min_cost, rows = cost, []
        if cost == min_cost:
            component_w_sizes = tuple(c-k for c, k in comps)
            rows.append((component_w_sizes, gadget_w))
    return min_cost, rows


def global_states(m, v, one_color_options):
    n = 11 - m
    w = 47 - v
    budget_u = l_u_max(v) - 42*m - n*p_k(v, 12)
    budget_w = t_k(w, 4) - n*p_k(w, 12)
    if budget_u < 0 or budget_w < 0:
        return budget_u, budget_w, set()
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
    return budget_u, budget_w, states


def main():
    options_by_v = {}
    for v in range(31, 48):
        a = options_product(v)
        b = options_recursive(v)
        assert a == b, (v, sorted(a ^ b))
        options_by_v[v] = a

    all_rows = {}
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
    for m, v_min in SUPPORT_MIN.items():
        rows = []
        for v in range(v_min, 48):
            bu, bw, states = global_states(m, v, options_by_v[v])
            rows.append((v, bu, bw, len(options_by_v[v]), len(states), bool(states)))
        all_rows[m] = rows
        excluded = [v for v, _, _, _, _, ok in rows if not ok]
        survivors = [v for v, _, _, _, _, ok in rows if ok]
        assert excluded == expected_excluded[m], (m, excluded)
        assert survivors == expected_survivors[m], (m, survivors)

    # Exact W-boundary equalities at the first profile-feasible support sizes.
    for m, v, expected_min_w, expected_budget_w in [
        (8, 39, 3, 24),
        (9, 40, 2, 18),
        (10, 41, 1, 13),
    ]:
        min_w, shapes = min_w_shapes(v)
        assert min_w == expected_min_w, (m, v, min_w)
        assert all(max(parts) <= 2 for parts, _ in shapes)
        max_gadget_w = max(gw for _, gw in shapes)
        assert max_gadget_w <= (4 if m in (8, 9) else 3)
        bu, bw, states = global_states(m, v, options_by_v[v])
        assert bw == expected_budget_w
        if m in (8, 9):
            assert m*min_w == bw
            assert {z for _, z in states} == {bw}
        else:
            assert m*min_w == 10 and bw-m*min_w == 3
            assert {z for _, z in states} == {10, 11, 12, 13}

    print("Q33 COMPONENT-ONLY VARIABLE-CORE SCREEN: PASS")
    print("Cartesian-product and recursive per-color generators agree for v=31..47.")
    for m, rows in all_rows.items():
        print(f"m={m}")
        for v, bu, bw, nopt, nstates, feasible in rows:
            print(f"  v={v}: BU={bu}, BW={bw}, options={nopt}, "
                  f"aggregate_states={nstates}, "
                  f"{'PROFILE_FEASIBLE' if feasible else 'EXCLUDED'}")
    print("W-boundary checks: m8/v39 -> 8 matchings of 3 edges; "
          "m9/v40 -> 9 matchings of 2 edges; m10/v41 -> W-slack 3.")
    print("All 47 registered (m,v) cells checked.")
    print("Scope: necessary aggregate profile screen only; no graph realization; "
          "Q33 remains OPEN.")


if __name__ == "__main__":
    main()
