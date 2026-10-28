#!/usr/bin/env python3
"""Arithmetic-only verifier for V47_PIVOT_NEIGHBORHOOD_PACKING.md.

This script verifies the Turan floors, the 253-edge baseline, the six-unit
degree-excess identity, and the listed integer slack ranges. It does not
enumerate graphs or certify Q32 infeasibility.
"""
from itertools import product


def p4(n: int) -> int:
    q, r = divmod(n, 4)
    sizes = [q + 1] * r + [q] * (4 - r)
    return sum(s * (s - 1) // 2 for s in sizes)


expected = {
    8: {"n": 15, "p4": 21, "D": 18, "count": 79, "xmin": 8, "xmax": 23},
    9: {"n": 11, "p4": 10, "D": 13, "count": 61, "xmin": 13, "xmax": 25},
    10: {"n": 7, "p4": 3, "D": 8, "count": 44, "xmin": 18, "xmax": 28},
}

for m in (8, 9, 10):
    n = 47 - 4 * m
    p = p4(n)
    base = 4 * (m * (m - 1) // 2) + m * n + p
    D = 12 * n - m * n - 2 * p

    assert n == expected[m]["n"]
    assert p == expected[m]["p4"]
    assert base == 253
    assert D == expected[m]["D"]

    states = []
    for x in range(33):
        for y in range(33 - x):
            z = 32 - x - y
            s_q = 2 * x + y - 5 * m
            s_r = y + 2 * z - D
            if s_q >= 0 and s_r >= 0 and s_q + s_r == 6:
                assert x + y + z == 32
                states.append((x, y, z, s_q, s_r))

    assert len(states) == expected[m]["count"]
    assert min(s[0] for s in states) == expected[m]["xmin"]
    assert max(s[0] for s in states) == expected[m]["xmax"]
    assert all(s[0] >= 26 - D for s in states)

    print(
        f"m={m}: n={n}, p4={p}, baseline={base}, D={D}, "
        f"scalar_states={len(states)}, x_range="
        f"[{min(s[0] for s in states)},{max(s[0] for s in states)}]"
    )

print("V47_PIVOT_PACKING_ARITHMETIC_OK")
print("Scope: arithmetic and scalar slack only; not a graph UNSAT certificate.")
