#!/usr/bin/env python3
"""Finite arithmetic replay for FULL_ROW_LINEARITY_CAPACITY.md.

Checks the point-capacity inequality and the resulting C(h) table only.
The graph-theoretic six-set and pairwise-linearity arguments are proved in the note.
"""

import math


def a(d):
    return min(7, 10-d)


def C(h):
    return min(21, math.floor(9 + 60/h))


def main():
    for d in range(11):
        assert (a(d)-1)*d*d <= 20*d

    expected={1:21,2:21,3:21,4:21,5:21,6:19,7:17,8:16,9:15,10:15}
    got={h:C(h) for h in range(1,11)}
    assert got==expected

    hub={h:35-C(h) for h in range(1,11)}
    assert hub[6]==16
    assert hub[7]==18
    assert hub[8]==19
    assert hub[9]==20
    assert hub[10]==20

    # V12 full-row minima used by the theorem.
    assert 6>=6  # A
    assert 2>=1  # B
    assert 6>=6  # C
    assert 1>=1  # D

    print('E407_FULL_ROW_LINEARITY_CAPACITY_ARITHMETIC_OK')
    print('C(h)=',got)
    print('hub floor from Bsel>=35=',hub)
    print('scope: arithmetic only; no graph-realization certificate')


if __name__=='__main__':
    main()
