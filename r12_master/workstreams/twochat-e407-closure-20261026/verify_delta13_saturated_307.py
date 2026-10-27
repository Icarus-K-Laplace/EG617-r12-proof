#!/usr/bin/env python3
"""Finite arithmetic replay for DELTA13_SATURATED_307_CONDITIONAL_CLOSURE.md.

This script verifies only the integer kernel enumeration. It does not verify
Didin's theorem, Brouwer's theorem, alpha-criticality, or the 49-support-K4
structural reduction.
"""

from math import comb


def survivors(edge_count_g: int):
    out = []
    for a in range(1, 30):
        for b in range(a, 30):
            c = 29 - a - b
            if c < 5:
                continue
            if a * b < 49:
                continue
            e_c = edge_count_g - comb(a, 2) - comb(b, 2)
            if e_c < 0:
                continue
            e_j = comb(c, 2) - e_c
            if e_j < 49:
                continue
            brouwer_lower = (c * c) // 4 - 1
            if e_c < brouwer_lower:
                continue
            out.append((a, b, c, e_c, e_j))
    return out


def main():
    # Present delta=13 already-saturated fork: G has 99 edges.
    s99 = survivors(99)
    assert s99 == [], s99

    # Audit comparison with the old delta=14 saturated boundary.
    s98 = survivors(98)
    assert s98 == [(7, 7, 15, 56, 49)], s98

    print("DELTA13_SATURATED_307_ARITHMETIC_OK")
    print("G=99 survivors:", s99)
    print("G=98 comparison survivors:", s98)
    print("Scope: arithmetic only; external theorem dependencies not verified.")


if __name__ == "__main__":
    main()
