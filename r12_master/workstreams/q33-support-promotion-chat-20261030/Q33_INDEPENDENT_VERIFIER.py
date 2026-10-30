#!/usr/bin/env python3
"""Q33 source-correct variable-component-core profile reserve screen.

Ten K5 components are retained, but their core sizes c_i are variable in
{0,1,2,3,4}; the code does NOT assume one shell vertex per component.
Two independent group-option generators (Cartesian product and recursive
state DP) are cross-checked before the global h/support screen.
This is a necessary profile test, not a graph-level UNSAT certificate.
"""
from itertools import product
from math import comb

SUPPORT_MIN = {8:31, 9:32, 10:34}
CORE_SPLITS = [(c,k) for c in range(5) for k in range(c+1)]


def p_k(n,k):
    if n<=k:
        return 0
    q,r=divmod(n,k)
    return (k-r)*comb(q,2)+r*comb(q+1,2)


def t_k(n,k):
    return comb(n,2)-p_k(n,k)


def l_u_max(v):
    w=47-v
    if w==0:
        return comb(47,2)-284
    return comb(v,2)-280+12*w-p_k(w,4)


def options_product(num,v,gadget):
    out=set()
    for comps in product(CORE_SPLITS,repeat=num):
        csum=sum(c for c,k in comps)
        ksum=sum(k for c,k in comps)
        if gadget:
            if not 12<=csum<=16:
                continue
            g=23-csum
            s_u=v-24-ksum
            if not 4<=s_u<=g:
                continue
            gadget_u=max(0,p_k(s_u,2)-6)
        else:
            if not 8<=csum<=12:
                continue
            g=19-csum
            s_u=v-28-ksum
            if not 0<=s_u<=g:
                continue
            gadget_u=p_k(s_u,2)
        r_w=g-s_u
        comp_u=sum(comb(k,2) for c,k in comps)
        comp_w=sum(comb(c-k,2) for c,k in comps)
        out.add((comp_u+gadget_u,comp_w+p_k(r_w,2)))
    return out


def options_recursive(num,v,gadget):
    # Independent recursion over components; state=(core sum,U sum,U-pairs,W-pairs).
    states={(0,0,0,0)}
    for _ in range(num):
        nxt=set()
        for csum,ksum,uc,wc in states:
            for c,k in CORE_SPLITS:
                nxt.add((csum+c,ksum+k,uc+comb(k,2),wc+comb(c-k,2)))
        states=nxt
    out=set()
    for csum,ksum,uc,wc in states:
        if gadget:
            if not 12<=csum<=16:
                continue
            g=23-csum
            s_u=v-24-ksum
            if not 4<=s_u<=g:
                continue
            gadget_u=max(0,p_k(s_u,2)-6)
        else:
            if not 8<=csum<=12:
                continue
            g=19-csum
            s_u=v-28-ksum
            if not 0<=s_u<=g:
                continue
            gadget_u=p_k(s_u,2)
        out.add((uc+gadget_u,wc+p_k(g-s_u,2)))
    return out


def feasible(m,v,h,opts3,opts4):
    n,w=11-m,47-v
    bu=l_u_max(v)-42*m-n*p_k(v,12)+4*h
    bw=t_k(w,4)-n*p_k(w,12)
    if bu<0 or bw<0:
        return False
    states={(0,0)}
    for opts in [opts3]*(m-h)+[opts4]*h:
        states={(u+a,ww+b) for u,ww in states for a,b in opts
                if u+a<=bu and ww+b<=bw}
        if not states:
            return False
    return bool(states)


def main():
    all_rows={}
    for v in range(31,48):
        assert options_product(3,v,False)==options_recursive(3,v,False)
        assert options_product(4,v,True)==options_recursive(4,v,True)

    for m,v0 in SUPPORT_MIN.items():
        rows=[]
        for v in range(v0,48):
            o3=options_recursive(3,v,False)
            o4=options_recursive(4,v,True)
            hs=[h for h in range(m+1) if feasible(m,v,h,o3,o4)]
            rows.append((v,hs))
        all_rows[m]=rows

    assert dict(all_rows[8]) if False else True
    assert all_rows[8][:4]==[(31,[]),(32,[]),(33,[]),(34,[])]
    assert all_rows[8][4]==(35,[6,7,8])
    assert all_rows[9][:3]==[(32,[]),(33,[]),(34,[])]
    assert all_rows[9][3]==(35,[9])
    assert all_rows[10][:4]==[(34,[]),(35,[]),(36,[]),(37,[])]
    assert all_rows[10][4]==(38,[10])

    print("Q33 VARIABLE-CORE PROFILE SCREEN: PASS")
    for m,rows in all_rows.items():
        print("m=",m,rows)
    print("All 47 (m,v) cells checked; product and recursive group options agree.")
    print("Scope: necessary profile relaxation only; Q33 remains OPEN.")


if __name__=="__main__":
    main()
