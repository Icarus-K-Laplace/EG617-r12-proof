#!/usr/bin/env python3
"""Arithmetic audit for DELTA12_DEPTH2_EPS1_CLOSURE.md."""

from math import comb


def main():
    # No positive four-clique partition of 18 vertices has 35 edges.
    sols = []
    for a in range(1, 19):
        for b in range(a, 19):
            for c in range(b, 19):
                d = 18 - a - b - c
                if d < c or d < 1:
                    continue
                if sum(comb(x, 2) for x in (a, b, c, d)) == 35:
                    sols.append((a, b, c, d))
    assert sols == []

    # To destroy all base triangles in the five KP equality kernels after
    # deleting base vertices, the only possible escape must empty one of
    # N3,N4, reduce N2 to y, and reduce N1 to A0. Its deletion cost is >6.
    costs = []
    for parts in ((3, 4, 5, 5), (4, 4, 4, 5)):
        n1, n2, n3, n4 = parts
        for a0 in range(1, n1):
            cost = min(n3, n4) + (n2 - 1) + (n1 - a0)
            costs.append((parts, a0, cost))
            assert cost > 6

    # epsilon_U=1 endpoint rigidity: d0 needs eps0>=1+t0, so total excess
    # forces t0=0, eps0=1. A restored C/E endpoint has d_W=3; double-hit
    # would give degree2 and violates the generic d_W>=3 floor.
    assert 2 + 1 - 0 == 3
    assert 4 - 1 == 3
    assert 4 - 2 < 3

    print("DELTA12_DEPTH2_EPS1_CLOSURE_OK")
    print("KP deletion costs:", costs)
    print("Scope: arithmetic only; external KP equality theorem is an input.")


if __name__ == "__main__":
    main()
