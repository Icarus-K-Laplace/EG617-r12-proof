#!/usr/bin/env python3
"""Arithmetic replay for DELTA13_NONPARTITE_TWO_STEP_AUGMENTABLE.md.

Checks W-profile enumeration and exceptional-degree arithmetic only.
Does not verify Brouwer/Kang-Pikhurko or graph saturation lemmas.
"""
from itertools import combinations_with_replacement

def c2(n): return n*(n-1)//2

def profiles(eH,max_cross=3):
    out=[]
    for ns in combinations_with_replacement(range(1,19),4):
        if sum(ns)!=18: continue
        base=sum(c2(x) for x in ns)
        cr=eH-base
        if 0<=cr<=max_cross:
            out.append((ns,cr))
    return out

def main():
    assert profiles(34)==[
        ((3,4,5,6),0),((3,5,5,5),1),((4,4,4,6),1),((4,4,5,5),2)
    ]
    assert profiles(33)==[
        ((3,5,5,5),0),((4,4,4,6),0),((4,4,5,5),1)
    ]
    assert profiles(32)==[((4,4,5,5),0)]

    # eps=1 equality: x+y degree sum is exactly 6, no added-edge incidence,
    # and excess split gives a=3 or4.
    eps1=[]
    for ex in range(2):
        ey=1-ex
        a1=4-ex
        a2=3+ey
        if a1==a2: eps1.append((a1,ex,ey))
    assert eps1==[(4,0,1),(3,1,0)]

    # eps=3 equality: all U excess on x,y, no incidences, both degree4.
    eps3=[]
    for ex in range(4):
        ey=3-ex
        a1=5-ex
        a2=2+ey
        if a1==a2: eps3.append((a1,ex,ey))
    assert eps3==[(5,0,3),(4,1,2),(3,2,1),(2,3,0)]

    # delta13 W complement edges.
    for eps in range(4):
        eH=35-eps
        eJ=153-eH
        assert eJ==118+eps

    print('E407_DELTA13_TWO_STEP_AUGMENTABLE_ARITHMETIC_OK')
    print('eps1 profiles:',profiles(34))
    print('eps2 profiles:',profiles(33))
    print('eps3 profiles:',profiles(32))
    print('eps1 exceptional splits:',eps1)
    print('eps3 exceptional splits:',eps3)
    print('scope: arithmetic only')

if __name__=='__main__': main()
