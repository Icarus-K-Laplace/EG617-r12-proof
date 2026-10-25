#!/usr/bin/env python3
"""Arithmetic verifier for the 15-vertex saturated-kernel classification.

The graph-theoretic implications (AES equality case, Brouwer bound, and
saturation arguments) are dependencies stated in the accompanying proof.
This script checks the numerical deductions and the unique integer solution.
"""
from itertools import product

n, e, delta_cap = 15, 49, 7
assert n // 5 == 3
assert 5 * (3 * 3) == 45 < e  # balanced C5 blow-up contradicts e=49
assert 49 - 5 == 44 > 49 - 7 + 1  # any J-v with d<=5 is bipartite

solutions = []
for d in range(1, 6):
    e_del = e - d
    for p in range(5, 10):  # p(14-p) >= e_del
        q = 14 - p
        if p * q < e_del:
            continue
        for a in range(1, min(d, p) + 1):
            b = d - a
            if b < 1 or b > q or a + b != d:
                continue
            missing = p * q - e_del
            if a * b != missing:
                continue
            # Degrees in J: X\\A vertices have degree q, Y\\B vertices p;
            # A vertices have degree q-b+1, B vertices p-a+1.
            if p > a and q > delta_cap:
                continue
            if q > b and p > delta_cap:
                continue
            if a > 0 and q - b + 1 > delta_cap:
                continue
            if b > 0 and p - a + 1 > delta_cap:
                continue
            solutions.append((d, p, q, a, b, missing))

assert solutions == [(4, 7, 7, 2, 2, 4)], solutions
assert 7 * 7 - 2 * 2 == 45  # J-v
assert 45 + 4 == 49
profile = (1, 2, 5, 5, 2)
assert sum(profile) == 15
assert sum(profile[i] * profile[(i + 1) % 5] for i in range(5)) == 49
part_degrees = tuple(profile[(i - 1) % 5] + profile[(i + 1) % 5] for i in range(5))
assert part_degrees == (4, 6, 7, 7, 6)
assert max(part_degrees) <= 7

print("DELTA14_SATURATED_KERNEL_CLASSIFICATION_ARITHMETIC_OK")
print("unique case: d=4, bipartition 7+7, missing K2,2, C5 blow-up (1,2,5,5,2)")
