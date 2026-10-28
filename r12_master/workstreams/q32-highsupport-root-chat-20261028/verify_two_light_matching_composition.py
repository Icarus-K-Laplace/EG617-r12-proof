#!/usr/bin/env python3
"""Exact finite regression for V47_TWO_LIGHT_MATCHING_COMPOSITION.md.

A-C and B-C are fixed identity matchings on three independent 4-sets.
Enumerate every A-B bipartite graph with 4..7 edges and check whether it
contains an independent 5-set. The theorem predicts that alpha<=4 holds
exactly when all four diagonal/composed matching edges A_i B_i are present.
This verifies only the 12-vertex local theorem, not global Q32 infeasibility.
"""
from itertools import combinations
from math import comb

N = 12
FIVE_MASKS = [
    sum(1 << v for v in S)
    for S in combinations(range(N), 5)
]
FIVE_VERTICES = list(combinations(range(N), 5))

BASE = [0] * N
for i in range(4):
    # A_i -- C_i and B_i -- C_i are the two light matchings.
    BASE[i] |= 1 << (8 + i)
    BASE[8 + i] |= 1 << i
    BASE[4 + i] |= 1 << (8 + i)
    BASE[8 + i] |= 1 << (4 + i)


def has_independent_five(edge_mask):
    adj = BASE.copy()
    for edge in range(16):
        if (edge_mask >> edge) & 1:
            i, j = divmod(edge, 4)
            u, v = i, 4 + j
            adj[u] |= 1 << v
            adj[v] |= 1 << u

    for vertices, mask in zip(FIVE_VERTICES, FIVE_MASKS):
        for v in vertices:
            if adj[v] & mask:
                break
        else:
            return True
    return False


tested = 0
valid_by_edge_count = {}
for edge_mask in range(1 << 16):
    e = edge_mask.bit_count()
    if not 4 <= e <= 7:
        continue
    tested += 1
    has_i5 = has_independent_five(edge_mask)
    diagonal_present = all(
        (edge_mask >> (4 * i + i)) & 1
        for i in range(4)
    )

    if not has_i5:
        assert diagonal_present, (
            "counterexample to matching composition theorem",
            e,
            edge_mask,
        )
        valid_by_edge_count[e] = valid_by_edge_count.get(e, 0) + 1

    # If all four composed matching edges are present, each label-track
    # {A_i,B_i,C_i} is a triangle, so alpha is exactly four.
    if diagonal_present:
        assert not has_i5, ("diagonal matching did not certify alpha<=4", e, edge_mask)

assert tested == sum(comb(16, e) for e in range(4, 8)) == 25636
expected = {4: 1, 5: 12, 6: 66, 7: 220}
assert valid_by_edge_count == expected, (valid_by_edge_count, expected)

print("A-B graphs checked:", tested)
for e in range(4, 8):
    print(f"e(A,B)={e}: alpha<=4 graphs={valid_by_edge_count[e]}")
print("V47_TWO_LIGHT_MATCHING_COMPOSITION_EXHAUSTIVE_OK")
print("Scope: exact 12-vertex local theorem only; not global Q32 UNSAT.")
