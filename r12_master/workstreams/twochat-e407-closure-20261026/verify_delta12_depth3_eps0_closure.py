#!/usr/bin/env python3
"""Arithmetic audit for DELTA12_DEPTH3_EPS0_CLOSURE.md."""

from math import comb


def p3(n):
    q, r = divmod(n, 3)
    sizes = [q + 1] * r + [q] * (3 - r)
    return sum(comb(s, 2) for s in sizes)


def main():
    assert p3(17) == 40
    assert p3(16) == 35
    assert 36 < p3(17)
    assert comb(2, 2) + 2 * comb(5, 2) + comb(6, 2) == 36

    # If xy is restored, one restored edge contributes to both incidence
    # counts, so d_W(x)+d_W(y)<=5-2=3, while the degree-two lemma gives >=4.
    assert 5 - 2 == 3 < 4

    # If xy is not restored, sum<=5 and each degree>=2, so one endpoint has
    # degree exactly two and forces the K2+K5+K5+K6 W kernel.
    possible = [(a,b) for a in range(2,6) for b in range(2,6) if a+b<=5]
    assert all(min(a,b)==2 for a,b in possible)

    print("DELTA12_DEPTH3_EPS0_CLOSURE_OK")
    print("possible degree pairs before terminal contradiction:", possible)
    print("Scope: arithmetic only; analytic extremal proof is in theorem file.")


if __name__ == "__main__":
    main()
