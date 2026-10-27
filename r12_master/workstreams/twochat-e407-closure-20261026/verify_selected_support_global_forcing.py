#!/usr/bin/env python3
"""Arithmetic replay for selected-support global forcing in E407 Q32.

This verifier checks only the finite row-count and anchor-count arithmetic in
SELECTED_SUPPORT_HUB_COMPLETENESS.md and S_ANCHOR_CROSS_LOAD_REFINEMENT.md.
It does not verify the exact-129 factor theorem, alpha-two gadget arguments,
or graph realization.
"""

from itertools import product


def row_floor_A():
    vals=[]
    for n0 in range(11):
        for n1 in range(11-n0):
            n3=10-n0-n1
            if 3*n0+2*n1<=8:
                vals.append((n0,n1,n3))
    return min(v[2] for v in vals)


def row_floor_B():
    vals=[]
    for n0 in range(11):
        for n2 in range(11-n0):
            n3=10-n0-n2
            if 3*n0+n2<=8:
                vals.append((n0,n2,n3))
    return min(v[2] for v in vals)


def row_floor_C():
    vals=[]
    for n0 in range(11):
        for n1 in range(11-n0):
            n3=10-n0-n1
            if 3*n0+2*n1<=9:
                vals.append((n0,n1,n3))
    return min(v[2] for v in vals)


def row_floor_D():
    vals=[]
    for n0 in range(11):
        for na in range(11-n0):
            for nb in range(11-n0-na):
                n3=10-n0-na-nb
                if 3*n0+na+nb<=9:
                    vals.append((n0,na,nb,n3))
    return min(v[3] for v in vals)


def E_no_full_profiles():
    vals=[]
    for n0 in range(11):
        for n1 in range(11-n0):
            for n2 in range(11-n0-n1):
                n3=10-n0-n1-n2
                if 3*n0+2*n1+n2<=10 and n3==0:
                    vals.append((n0,n1,n2,n3))
    return vals


def compositions4(total):
    for a in range(total+1):
        for b in range(total-a+1):
            for c in range(total-a-b+1):
                d=total-a-b-c
                yield a,b,c,d


def main():
    assert row_floor_A()==6
    assert row_floor_B()==2
    assert row_floor_C()==6
    assert row_floor_D()==1
    assert E_no_full_profiles()==[(0,0,10,0)]

    # A fixed full row has exactly three core neighbours, hence at most three
    # disjoint selected B-anchored blocks of one color can fail hub-completeness.
    for b in (5,6,7):
        assert b-3 >= 2
    assert 7*(5-3)==14

    # Enumerate exact-color anchor types:
    # n5 = b=5 (S selected), n6S = b=6 with S selected,
    # n6P = b=6 with p selected, n7 = b=7.
    for n5,n6S,n6P,n7 in compositions4(7):
        sigma=n5+n6S
        bsel=5*n5+6*(n6S+n6P)+7*n7
        mp=n5+n6P  # b=5 selects p; b=6P selects p
        assert bsel+sigma+mp==49

        # Per-color cross-edge floors are 2,2,1,1 respectively.
        qfloor=2*n5+2*n6S+n6P+n7
        assert qfloor==7+sigma

        # Full-row selected hub-complete floor.
        hcfloor=2*n5+3*(n6S+n6P)+4*n7
        assert hcfloor==bsel-21
        assert hcfloor==28-sigma-mp
        assert hcfloor+qfloor==35-mp
        assert hcfloor+qfloor>=28

        for beta in (0,1,2):
            global_cross=max(14-beta,qfloor)
            assert global_cross>=14-beta
            assert global_cross>=7+sigma

    print('E407_SELECTED_SUPPORT_GLOBAL_FORCING_ARITHMETIC_OK')
    print('row n3 floors: A=6 B=2 C=6 D=1')
    print('E no-full-row profile: (n0,n1,n2,n3)=(0,0,10,0)')
    print('full-row selected hub-complete floor: >=2/color, >=14 globally')
    print('cross-load: exact S-B edges >= max(14-beta, 7+sigma)')
    print('scope: arithmetic only; graph-theoretic alpha/6-set proofs are in theorem notes')


if __name__=='__main__':
    main()
