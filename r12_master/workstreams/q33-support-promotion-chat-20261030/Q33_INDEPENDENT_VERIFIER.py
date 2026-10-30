#!/usr/bin/env python3
"""Exact arithmetic and grouped-profile replay for Q33 all-support reserves.

This checks necessary scalar/profile constraints only. It is not a graph
realization or a complete Q33 UNSAT certificate.
"""
from itertools import product
from math import comb

SUPPORT_MIN = {8: 31, 9: 32, 10: 34}


def p_k(n, k):
    if n <= k:
        return 0
    q, r = divmod(n, k)
    return (k-r)*comb(q, 2) + r*comb(q+1, 2)


def t_k(n, k):
    return comb(n, 2) - p_k(n, k)


def min_w_cost(num, cap):
    best = None
    profiles = []
    for ks in product(range(5), repeat=num):
        if sum(ks) <= cap:
            cost = sum(comb(4-x, 2) for x in ks)
            if best is None or cost < best:
                best, profiles = cost, [ks]
            elif cost == best:
                profiles.append(ks)
    assert best is not None
    return best, profiles


def l_u_upper(v):
    w = 47-v
    if w == 0:
        return comb(47, 2)-284
    return comb(v, 2)-280+12*w-p_k(w, 4)


def group_options(num, cap):
    """All (U-pair cost,W-pair cost) pairs for one color's unselected sets."""
    return {
        (sum(comb(x, 2) for x in ks),
         sum(comb(4-x, 2) for x in ks))
        for ks in product(range(5), repeat=num)
        if sum(ks) <= cap
    }


def grouped_profile_dp(m, v, h, bu, bw):
    """Independent grouped-profile feasibility replay."""
    cap = v-28
    opts3, opts4 = group_options(3, cap), group_options(4, cap)
    states = {(0, 0)}
    for num in [3]*(m-h)+[4]*h:
        opts = opts3 if num == 3 else opts4
        states = {
            (u0+u1, w0+w1)
            for u0, w0 in states
            for u1, w1 in opts
            if u0+u1 <= bu and w0+w1 <= bw
        }
        if not states:
            return False
    return bool(states)


def row(m, v):
    n, w = 11-m, 47-v
    rho = min(6, 4*n)
    f0, prof0 = min_w_cost(3, v-28)
    f1, prof1 = min_w_cost(4, v-28)
    bw = t_k(w, 4)-n*p_k(w, 12)
    w_h, u_h, charge_h = [], [], []
    for h in range(m+1):
        bu = l_u_upper(v)-42*m-n*p_k(v, 12)+rho*h
        if (m-h)*f0+h*f1+n*p_k(w, 12) <= t_k(w, 4):
            w_h.append(h)
        if bu >= 0:
            u_h.append(h)
        if bu >= 0 and 3*(3*m+h) <= bw+2*bu:
            charge_h.append(h)
    joint = sorted(set(w_h)&set(u_h)&set(charge_h))

    # Verify that the three scalar tests exactly match the grouped profile
    # model for this finite parameter cell.
    dp_h = []
    for h in range(m+1):
        bu = l_u_upper(v)-42*m-n*p_k(v, 12)+rho*h
        if grouped_profile_dp(m, v, h, bu, bw):
            dp_h.append(h)
    assert joint == dp_h, (m, v, joint, dp_h)

    return {"m":m,"v":v,"w":w,"f0":f0,"f1":f1,
            "W_h":w_h,"U_h":u_h,"charge_h":charge_h,
            "joint":joint,"profiles0":prof0,"profiles1":prof1}


def main():
    assert p_k(31,12)==26 and p_k(32,12)==28
    assert p_k(33,12)==30 and p_k(34,12)==32
    assert t_k(31,4)==360 and t_k(33,4)==408

    rows={}
    for m,v0 in SUPPORT_MIN.items():
        rows[m]=[row(m,v) for v in range(v0,48)]

    assert rows[8][0]["joint"]==[]
    assert rows[8][1]["joint"]==[]
    assert rows[8][2]["joint"]==[]
    assert rows[8][3]["joint"]==[4,5,6,7]
    assert rows[9][0]["joint"]==[]
    assert rows[9][1]["joint"]==[]
    assert rows[9][2]["joint"]==[]
    assert rows[9][3]["joint"]==list(range(3,10))
    assert rows[10][0]["joint"]==[]
    assert rows[10][1]["joint"]==[]
    assert rows[10][2]["joint"]==list(range(3,11))

    print("m v w f0 f1 H_W H_U H_charge joint")
    for m, rr in rows.items():
        for r in rr:
            print(m,r["v"],r["w"],r["f0"],r["f1"],
                  r["W_h"],r["U_h"],r["charge_h"],r["joint"])
    print("EXCLUDED: m=8 v=31,32,33; m=9 v=32,33,34; m=10 v=34,35")
    print("FIRST SURVIVORS: (8,34,h=4..7); (9,35,h=3..9); (10,36,h=3..10)")
    print("LIMITATION: necessary scalar/profile constraints only; Q33 remains OPEN.")


if __name__ == "__main__":
    main()
