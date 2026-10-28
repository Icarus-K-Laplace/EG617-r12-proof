#!/usr/bin/env python3
"""Arithmetic verifier for the 3+7 double-track residual edge floor.

Under the 3+7 contract, a double-track vertex has no R-neighbors. Its two
track fibers must be completely joined, so e(R) >= sum C(n_h,2)+n_h*n_j.
The residual edge count is e(R)=3+z, with z in {0,...,4}.
This checks the four admissible fiber-size partitions and the resulting
necessary z thresholds; it is not a global Q32 solver.
"""
from itertools import combinations

PARTITIONS = [
    (3, 3, 1, 0),
    (3, 2, 2, 0),
    (3, 2, 1, 1),
    (2, 2, 2, 1),
]

def fiber_edges(ns):
    return sum(n * (n - 1) // 2 for n in ns)

expected = {
    (3, 3, 1, 0): {(3, 0): 3, (1, 0): 3},
    (3, 2, 2, 0): {(3, 0): 2, (2, 0): 2},
    (3, 2, 1, 1): {(2, 1): 3, (1, 1): 2},
    (2, 2, 2, 1): {(2, 1): 2},
}

for ns in PARTITIONS:
    base = fiber_edges(ns)
    got = {}
    for i, j in combinations(range(4), 2):
        a, b = ns[i], ns[j]
        if a + b <= 3:
            min_eR = base + a * b
            z_min = min_eR - 3
            got[tuple(sorted((a, b), reverse=True))] = max(0, z_min)
    assert got == expected[ns], (ns, got, expected[ns])
    print(f"fibers={ns}: allowed double-track pairs / z_min={got}")

assert all(z >= 2 for table in expected.values() for z in table.values())
print("V47_3PLUS7_DOUBLE_TRACK_EDGE_FLOOR_OK")
print("Scope: necessary fiber-size/edge-count arithmetic only; no global closure.")
