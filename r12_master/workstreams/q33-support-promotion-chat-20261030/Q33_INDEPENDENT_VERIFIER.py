#!/usr/bin/env python3
"""Exact arithmetic replay for the Q33 all-support U/W reserve screen.

Verifies necessary integer inequalities only; it does not certify parent
coverage, graph realizability, or a full Q33 UNSAT proof.
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


def min_w_cost(number_of_components, available_u):
    best = None
    profiles = []
    for ks in product(range(5), repeat=number_of_components):
        if sum(ks) <= available_u:
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


def row(m, v):
    n, w = 11-m, 47-v
    rho = min(6, 4*n)
    f0, prof0 = min_w_cost(3, v-28)
    f1, prof1 = min_w_cost(4, v-28)
    w_h = [h for h in range(m+1)
           if (m-h)*f0+h*f1+n*p_k(w, 12) <= t_k(w, 4)]
    u_h = [h for h in range(m+1)
           if n*p_k(v, 12) <= l_u_upper(v)-42*m+rho*h]
    return {"m":m,"v":v,"w":w,"f0":f0,"f1":f1,
            "W_h":w_h,"U_h":u_h,
            "common":sorted(set(w_h)&set(u_h)),
            "profiles0":prof0,"profiles1":prof1}


def main():
    assert p_k(31,12)==26 and p_k(32,12)==28
    assert p_k(33,12)==30 and p_k(34,12)==32
    assert t_k(31,4)==360 and t_k(33,4)==408

    rows={}
    for m,v0 in SUPPORT_MIN.items():
        rows[m]=[row(m,v) for v in range(v0,48)]

    assert rows[8][0]["common"]==[]
    assert rows[8][1]["common"]==[]
    assert rows[8][2]["common"]==[5]
    assert rows[9][0]["common"]==[]
    assert rows[9][1]["common"]==[]
    assert rows[9][2]["common"]==[4,5,6]
    assert rows[10][0]["common"]==[]
    assert rows[10][1]["common"]==list(range(2,9))

    for m,rr in rows.items():
        threshold={8:33,9:34,10:35}[m]
        for r in rr:
            if r["v"]>=threshold:
                assert r["common"], (m,r["v"])

    print("m v w f0 f1 W-feasible-h U-feasible-h joint-h")
    for m,rr in rows.items():
        for r in rr:
            print(m,r["v"],r["w"],r["f0"],r["f1"],
                  r["W_h"],r["U_h"],r["common"])
    print("EXCLUDED: m=8 v=31,32; m=9 v=32,33; m=10 v=34")
    print("FIRST SURVIVORS: (8,33,h=5); (9,34,h=4..6); (10,35,h=2..8)")
    print("LIMITATION: scalar necessary conditions only; Q33 remains OPEN.")


if __name__ == "__main__":
    main()
