#!/usr/bin/env python3
"""Exact normalized verifier for V47_LIGHT_CYCLE_HOLONOMY.md.

The four cycle-pair matchings are fixed, and the final one has holonomy sigma.
Both diagonals must contain the identity and sigma^{-1} matchings by the
two-light composition theorem. Their edge counts are capped at seven.
"""
from itertools import combinations, permutations

PERMS = list(permutations(range(4)))
ID = (0, 1, 2, 3)


def moved_count(p):
    return sum(p[i] != i for i in range(4))


def cycle_edges(sigma, extra_ac=None, extra_bd=None):
    # A=0..3, B=4..7, C=8..11, D=12..15.
    edges = set()

    def add(u, v):
        edges.add(tuple(sorted((u, v))))

    for i in range(4):
        add(i, 4 + i)          # AB matching I
        add(4 + i, 8 + i)       # BC matching I
        add(8 + i, 12 + i)      # CD matching I
        add(12 + i, sigma[i])   # DA matching sigma
        add(i, 8 + i)           # AC path through B
        j = sigma.index(i)      # sigma^{-1}(i): AC path through D
        add(i, 8 + j)
        add(4 + i, 12 + i)     # BD path through C
        add(4 + i, 12 + j)      # BD path through A

    if extra_ac is not None:
        add(extra_ac[0], 8 + extra_ac[1])
    if extra_bd is not None:
        add(4 + extra_bd[0], 12 + extra_bd[1])
    return edges


def has_independent_five(edges):
    adj = [0] * 16
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    for S in combinations(range(16), 5):
        mask = sum(1 << v for v in S)
        if all(not (adj[v] & mask) for v in S):
            return True, S
    return False, None


transposition_configs = 0
three_cycle_configs = 0
for sigma in PERMS:
    moved = moved_count(sigma)
    base = cycle_edges(sigma)

    if moved == 0:
        # Same-track vertices form K4; identity holonomy is compatible.
        continue

    if moved == 2:
        # Union of I and sigma^{-1} has six edges on each diagonal.
        existing = {
            (i, i) for i in range(4)
        } | {
            (i, sigma.index(i)) for i in range(4)
        }
        assert len(existing) == 6
        ac_options = [None] + [
            (i, j) for i in range(4) for j in range(4)
            if (i, j) not in existing
        ]
        bd_options = ac_options[:]
        assert len(ac_options) == len(bd_options) == 11
        for ea in ac_options:
            for eb in bd_options:
                independent, _ = has_independent_five(
                    cycle_edges(sigma, ea, eb)
                )
                assert not independent, (sigma, ea, eb)
                transposition_configs += 1

    elif moved == 3:
        # The two matchings occupy all seven permitted edges per diagonal.
        independent, witness = has_independent_five(base)
        assert independent, (sigma, "expected independent 5-set")
        three_cycle_configs += 1

    else:
        # A derangement has support four, so I union sigma^{-1} uses eight
        # edges on each diagonal, violating the seven-edge cap.
        assert moved == 4
        assert len({
            (i, i) for i in range(4)
        } | {
            (i, sigma.index(i)) for i in range(4)
        }) == 8

assert transposition_configs == 6 * 11 * 11 == 726
assert three_cycle_configs == 8
print("transposition diagonal configurations checked:", transposition_configs)
print("3-cycle forced configurations rejected:", three_cycle_configs)
print("V47_LIGHT_CYCLE_HOLONOMY_EXHAUSTIVE_OK")
print("Scope: normalized 16-vertex local contract only; not global Q32 UNSAT.")
