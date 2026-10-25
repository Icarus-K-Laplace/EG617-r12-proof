#!/usr/bin/env python3
"""Exact integer replay for the delta=14 K5-saturated alpha-critical reduction.

This checks only the finite arithmetic constraints in Section 5 of
DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md. It does not verify the
graph-theoretic lemmas or the imported Didin/Brouwer theorems.
"""
from math import comb

def t_floor_square_over_four(n: int) -> int:
    return n * n // 4

candidates = []
for c in range(5, 16):  # ab >= 49 and a+b=29-c imply c <= 15
    total_ab = 29 - c
    for a in range(1, total_ab // 2 + 1):
        b = total_ab - a
        if a * b < 49:
            continue
        e_c = 98 - comb(a, 2) - comb(b, 2)
        e_j = comb(c, 2) - e_c
        if e_c < t_floor_square_over_four(c) - 1:
            continue
        if e_j < 49:
            continue
        candidates.append((a, b, c, e_c, e_j))

assert candidates == [(7, 7, 15, 56, 49)], candidates
print("E407_DELTA14_SATURATED_ALPHA_CRITICAL_ARITHMETIC_OK")
print("unique terminal: a=b=7, c=15, e(C)=56, e(J)=49")
