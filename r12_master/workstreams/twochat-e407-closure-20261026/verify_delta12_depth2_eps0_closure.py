#!/usr/bin/env python3
"""Arithmetic audit for DELTA12_DEPTH2_EPS0_CLOSURE.md."""

from math import comb


def p3(n):
    q, r = divmod(n, 3)
    sizes = [q + 1] * r + [q] * (3 - r)
    return sum(comb(s, 2) for s in sizes)


def main():
    assert p3(17) == 40
    assert p3(16) == 35
    assert 36 < p3(17)

    # Equality W graph forced after deleting the two d0-neighbours.
    assert comb(6, 2) + 2 * comb(5, 2) == 35
    assert comb(2, 2) + comb(6, 2) + 2 * comb(5, 2) == 36

    # t0=0 leaves two restored incidences on C/E. Some C/E point has t_c>=1
    # and epsilon_c=0, hence d_W(c)=4-t_c<=3. In K2+K5+K5+K6 only K2
    # can be fully covered by such a neighbourhood.
    assert 4 - 1 <= 3
    assert min((2, 5, 5, 6)) == 2

    print("DELTA12_DEPTH2_EPS0_CLOSURE_OK")
    print("Scope: extremal arithmetic only; analytic graph argument is in theorem file.")


if __name__ == "__main__":
    main()
