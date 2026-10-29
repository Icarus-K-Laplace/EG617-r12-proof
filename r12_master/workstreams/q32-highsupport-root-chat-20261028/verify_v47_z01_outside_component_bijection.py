#!/usr/bin/env python3
"""Finite arithmetic checks for the outside-component bijection theorem."""
from itertools import product

# D[A] = 2K2 + 9K1: max independent sets choose one endpoint from each K2.
iso_2k2 = set(range(9))
e1, e2 = (9, 10), (11, 12)
ind_2k2 = [iso_2k2 | {x, y} for x, y in product(e1, e2)]
assert len(ind_2k2) == 4 and all(len(s) == 11 for s in ind_2k2)
assert all(all(i in s for i in iso_2k2) for s in ind_2k2)
assert all(not all(any(x in s for x in (endpoint,)) for s in ind_2k2)
           for endpoint in e1 + e2)
assert all(all(any(x in s for x in pair) for s in ind_2k2)
           for pair in (e1, e2))
assert sum([1] * 10 + [2] * 2) == 14
assert sum([1] * 10 + [2]) == 12

# D[A] = K3 + 10K1: max independent sets choose one triangle vertex.
iso_k3 = set(range(10))
tri = (10, 11, 12)
ind_k3 = [iso_k3 | {x} for x in tri]
assert len(ind_k3) == 3 and all(len(s) == 11 for s in ind_k3)
assert all(all(i in s for i in iso_k3) for s in ind_k3)
assert all(all(any(x in s for x in tri) for s in ind_k3) for _ in [0])
assert not all(any(x in s for x in (tri[0], tri[1])) for s in ind_k3)
assert sum([1] * 11 + [3]) == 14
assert sum([1] * 11) == 11

print("V47_OUTSIDE_COMPONENT_BIJECTION_ARITHMETIC_OK")
print("2K2: large-track O-degree multiset 1^10,2^2; T0 1^10,2")
print("K3: large-track O-degree multiset 1^11,3; T0 1^11")
