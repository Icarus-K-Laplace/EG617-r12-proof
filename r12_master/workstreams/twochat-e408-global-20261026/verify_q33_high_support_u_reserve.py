#!/usr/bin/env python3
"""Independent arithmetic replay for the Q33 support-lifting audit.

This checks only exact Turan/reserve arithmetic and the W-side bound on h.
It does NOT certify parent coverage, graph realizability, or the absent V12 package.
"""
from itertools import product
from math import comb

def p_k(n, k):
    """Minimum edges in an n-vertex graph with independence number <= k."""
    q, r = divmod(n, k)
    return (k - r) * comb(q, 2) + r * comb(q + 1, 2)

def t_k(n, k):
    """Maximum edges in a K_{k+1}-free n-vertex graph."""
    return comb(n, 2) - p_k(n, k)

def min_w_cost(number_of_components, available_u):
    """Min sum C(4-k_i,2), k_i in 0..4, sum k_i <= available_u."""
    best = None
    best_profile = None
    for ks in product(range(5), repeat=number_of_components):
        if sum(ks) <= available_u:
            cost = sum(comb(4 - k, 2) for k in ks)
            if best is None or cost < best:
                best, best_profile = cost, ks
    return best, best_profile

def audit_row(v):
    w = 47 - v
    f0, prof0 = min_w_cost(3, v - 28)
    f1, prof1 = min_w_cost(4, v - 28)
    w_capacity = t_k(w, 4)
    if f1 > f0:
        h_max = min(8, (w_capacity - 8 * f0) // (f1 - f0))
    else:
        h_max = 8
    h_max = max(0, h_max)
    eps_w_max = 0 if w == 0 else 4
    e_l_upper = comb(v, 2) - 284 + 12 * w + eps_w_max - p_k(w, 4)
    reserve_upper = e_l_upper - (336 - 6 * h_max)
    p12 = p_k(v, 12)
    need = {m: (11 - m) * p12 for m in (8, 9, 10)}
    return {
        "v": v, "w": w, "f0": f0, "f1": f1,
        "L_W_cap": w_capacity, "h_max": h_max,
        "eL_upper": e_l_upper, "reserve_upper": reserve_upper,
        "p12": p12, "need_m8": need[8], "need_m9": need[9],
        "need_m10": need[10],
        "reserve_excludes": [m for m in (8, 9, 10) if need[m] > reserve_upper],
        "profile0": list(prof0), "profile1": list(prof1),
    }

def main():
    assert p_k(29, 12) == 22
    assert 49 * comb(4, 2) == 294
    assert 294 + p_k(29, 12) == 316
    assert 294 + p_k(29, 12) > 310
    assert p_k(31, 12) == 26
    rows = [audit_row(v) for v in range(31, 48)]
    assert rows[0]["h_max"] == 4 and rows[0]["reserve_upper"] == 41
    assert rows[1]["h_max"] == 5 and rows[1]["reserve_upper"] == 69
    assert rows[0]["reserve_excludes"] == [8, 9]
    assert rows[1]["reserve_excludes"] == [8]
    assert all(row["reserve_excludes"] == [] for row in rows[2:])
    print("E407_LOCAL_RESERVE: p12(29)=22; 49*C(4,2)=294; 316>310 PASS")
    print("Q33_MIN_SUPPORT: p12(31)=26 PASS")
    print("v w f0 f1 h_max eL_upper reserve_upper p12 exclude_by_reserve")
    for r in rows:
        print(f'{r["v"]:2d} {r["w"]:2d} {r["f0"]:2d} {r["f1"]:2d} '
              f'{r["h_max"]:2d} {r["eL_upper"]:3d} {r["reserve_upper"]:3d} '
              f'{r["p12"]:2d} {",".join(map(str, r["reserve_excludes"])) or "-"}')
    print("RESULT: Q33 reserve closes m=8,9 at v=31 and m=8 at v=32 only;")
    print("        the scalar reserve alone does not close v>=33, nor m=9,10 at v>=32.")
    print("LIMITATION: arithmetic replay only; no graph realization or parent support promotion certified.")

if __name__ == "__main__":
    main()
