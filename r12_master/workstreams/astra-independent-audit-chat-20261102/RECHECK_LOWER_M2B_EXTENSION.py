#!/usr/bin/env python3
"""Independent check of the M2b singleton-neighborhood extension.

For every compatible pair of nonempty type sets on the two sides of K9,9,
and every singleton cycle-neighbor p of the exceptional vertex, find q so
that {p,q} is a valid two-neighbor type disjoint from every opposite-side type.
"""
from itertools import product
import json

T = [frozenset(((i-1) % 5, (i+1) % 5)) for i in range(5)]
def compatible(i, j):
    return T[i].isdisjoint(T[j])

nonempty = [
    tuple(i for i in range(5) if mask & (1 << i))
    for mask in range(1, 32)
]
pairs = [
    (A, B) for A in nonempty for B in nonempty
    if all(compatible(i, j) for i in A for j in B)
]

checks = []
for A, B in pairs:
    union_B = set().union(*(T[j] for j in B))
    available = set(range(5)) - union_B
    assert len(B) in (1, 2)
    if len(B) == 1:
        assert len(available) == 3
    else:
        assert len(available) == 2

    for p in sorted(available):
        valid_q = [
            q for q in sorted(available)
            if q != p
            and frozenset((p, q)) in T
            and all(frozenset((p, q)).isdisjoint(T[j]) for j in B)
        ]
        assert valid_q, (A, B, p, available)
        checks.append({
            "A_types": list(A), "B_types": list(B),
            "singleton_neighbor": p, "extension_choices": valid_q,
        })

assert len(pairs) == 20
assert len(checks) == 55
assert all(len(B) <= 2 for A, B in pairs)

print(json.dumps({
    "status": "PASS",
    "compatible_type_set_pairs": len(pairs),
    "singleton_neighborhood_positions_checked": len(checks),
    "all_extensions_valid": True,
    "scope": "Finite verification of the M2b type-quotient extension step only."
}, indent=2))
