#!/usr/bin/env python3
"""Exact finite classification of C5 blow-ups with n=15, e=49, Delta<=7."""
from itertools import product

def canonical_cycle(t):
    rev = tuple(reversed(t))
    return min(
        [tuple(t[i:] + t[:i]) for i in range(5)] +
        [tuple(rev[i:] + rev[:i]) for i in range(5)]
    )

edge49 = set()
valid = set()
ordered_valid = []
for t in product(range(1, 16), repeat=5):
    if sum(t) != 15:
        continue
    edges = sum(t[i] * t[(i + 1) % 5] for i in range(5))
    if edges != 49:
        continue
    c = canonical_cycle(t)
    edge49.add(c)
    degrees = tuple(t[(i - 1) % 5] + t[(i + 1) % 5] for i in range(5))
    if max(degrees) <= 7:
        valid.add(c)
        ordered_valid.append((t, degrees))

assert len(edge49) == 7, sorted(edge49)
assert valid == {(1, 2, 5, 5, 2)}, sorted(valid)
assert all(max(deg) <= 7 for _, deg in ordered_valid)
assert len(ordered_valid) == 5  # ordered tuples in this one dihedral class
print("C5_BLOWUP_PROFILE_CLASSIFICATION_OK")
print("edge-49 dihedral classes before Delta cap:", len(edge49))
print("classes after Delta<=7:", sorted(valid))
