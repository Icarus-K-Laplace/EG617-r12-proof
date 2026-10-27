#!/usr/bin/env python3
"""Arithmetic sanity checks for SHELL_LIST_RELAXATION_AUDIT.md.

This verifies only the endpoint-count argument of the shell-label relaxation.
It is not a graph-realization certificate.
"""

from itertools import combinations

B = list(range(10))
S = list(range(10, 13))
A = B + S

# Any two shell edges use at most four B endpoints, hence leave at least six B labels.
all_edges = list(combinations(A, 2))
minimum_free_B = 10
for e1, e2 in combinations(all_edges, 2):
    used_B = (set(e1) | set(e2)) & set(B)
    minimum_free_B = min(minimum_free_B, 10 - len(used_B))
assert minimum_free_B == 6

# The V12 edge floor 22 is strictly above the 14 edges needed by the relaxation.
assert 22 >= 14
assert 7 * 2 == 14

print("E407_SHELL_LIST_RELAXATION_ARITHMETIC_OK")
print("minimum_free_B_for_any_two_edges=", minimum_free_B)
print("Scope: shell-label relaxation only; no support/core realization certificate.")
