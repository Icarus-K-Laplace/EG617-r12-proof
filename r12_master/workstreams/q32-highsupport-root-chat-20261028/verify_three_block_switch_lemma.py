#!/usr/bin/env python3
"""Finite exhaustive verifier for V47_THREE_BLOCK_SWITCH_LEMMA.md.

Graph: three independent 4-sets A,B,C; AB is the identity matching;
AC is identity plus one extra edge; BC is sigma plus one extra edge.
Enumerates all 24 sigma and all 12x12 legal extra-edge pairs and computes
the exact independence number of the 12-vertex graph.

This certifies only the local finite classification, not a global Q32 graph.
"""
from itertools import permutations
from collections import Counter

PERMS = list(permutations(range(4)))
ID = (0, 1, 2, 3)


def legal_extras(matching):
    return [
        (a, b)
        for a in range(4)
        for b in range(4)
        if b != matching[a]
    ]


def alpha_number(sigma, extra_ac, extra_bc):
    # Vertex ids: A_i=i, B_i=4+i, C_i=8+i.
    adj = [0] * 12

    def add_edge(u, v):
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for i in range(4):
        add_edge(i, 4 + i)          # AB identity matching
        add_edge(i, 8 + i)          # AC identity matching
        add_edge(4 + i, 8 + sigma[i])  # BC sigma matching

    add_edge(extra_ac[0], 8 + extra_ac[1])
    add_edge(4 + extra_bc[0], 8 + extra_bc[1])

    best = 0
    for mask in range(1 << 12):
        size = mask.bit_count()
        if size <= best:
            continue
        independent = True
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            v = bit.bit_length() - 1
            if adj[v] & mask:
                independent = False
                break
            remaining ^= bit
        if independent:
            best = size
    return best


def cycle_type(p):
    seen = set()
    lengths = []
    for i in range(4):
        if i in seen:
            continue
        j, length = i, 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = p[j]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


valid_by_sigma = {}
for sigma in PERMS:
    valid = []
    for e_ac in legal_extras(ID):
        for e_bc in legal_extras(sigma):
            if alpha_number(sigma, e_ac, e_bc) <= 4:
                valid.append((e_ac, e_bc))
    valid_by_sigma[sigma] = valid

assert len(valid_by_sigma[ID]) == 144
assert set(valid_by_sigma[ID]) == {
    (e_ac, e_bc)
    for e_ac in legal_extras(ID)
    for e_bc in legal_extras(ID)
}

for sigma in PERMS:
    ctype = cycle_type(sigma)
    valid = valid_by_sigma[sigma]
    if ctype == (1, 1, 1, 1):
        assert len(valid) == 144
    elif ctype == (2, 1, 1):
        moved = [i for i in range(4) if sigma[i] != i]
        assert len(moved) == 2
        expected = {
            ((s, sigma[s]), (s, s))
            for s in moved
        }
        assert set(valid) == expected and len(valid) == 2, (
            sigma, valid, expected
        )
    else:
        assert len(valid) == 0, (sigma, ctype, valid)

counts = Counter(cycle_type(sigma) for sigma in PERMS if valid_by_sigma[sigma])
assert counts == Counter({
    (1, 1, 1, 1): 1,
    (2, 1, 1): 6,
})
assert sum(map(len, valid_by_sigma.values())) == 156

print("sigma=id: 144/144 extra-edge pairs valid")
print("sigma=transposition: 2/144 pairs valid for each of 6 transpositions")
print("sigma=3-cycle, double-transposition, 4-cycle: 0 valid pairs")
print("V47_THREE_BLOCK_SWITCH_EXHAUSTIVE_OK")
print("Scope: exact alpha-number classification on three 4-sets only.")
