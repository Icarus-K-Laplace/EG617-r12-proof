#!/usr/bin/env python3
"""Reproduce the exact local counterexample to the retracted matching proof.

Three independent 4-sets A,B,C:
AB = identity matching;
AC = identity matching plus A_0 C_1;
BC = transposition (0 1) plus B_0 C_0.
This is one of the two valid switch cases from the 4,5,5 theorem.
When A,B are interpreted as outer blocks and C as the fixed small block,
the extra edges hit C_1 and C_0, not one common small-side label.
"""
SIGMA = (1, 0, 2, 3)
EXTRA_AC = (0, 1)
EXTRA_BC = (0, 0)
N = 12
adj = [0] * N


def add(u, v):
    adj[u] |= 1 << v
    adj[v] |= 1 << u


for i in range(4):
    add(i, 4 + i)              # AB identity
    add(i, 8 + i)              # AC identity
    add(4 + i, 8 + SIGMA[i])   # BC transposition
add(EXTRA_AC[0], 8 + EXTRA_AC[1])
add(4 + EXTRA_BC[0], 8 + EXTRA_BC[1])

alpha = 0
max_independent = []
for mask in range(1 << N):
    size = mask.bit_count()
    if size < alpha:
        continue
    if any((mask >> v) & 1 and adj[v] & mask for v in range(N)):
        continue
    if size > alpha:
        alpha = size
        max_independent = []
    max_independent.append(tuple(v for v in range(N) if (mask >> v) & 1))

assert SIGMA == (1, 0, 2, 3)
assert EXTRA_AC == (0, 1) and EXTRA_BC == (0, 0)
assert alpha == 4
assert len(max_independent) == 63
print("sigma=(0 1), extra_AC=(0,1), extra_BC=(0,0)")
print("exact independence number:", alpha)
print("maximum independent sets:", len(max_independent))
print("small-block extra endpoints: C_1 and C_0 (distinct)")
print("V47_37_SWITCH_ENDPOINT_COUNTEREXAMPLE_REPRODUCED")
print("Scope: local 12-vertex counterexample only; no global Q32 conclusion.")
