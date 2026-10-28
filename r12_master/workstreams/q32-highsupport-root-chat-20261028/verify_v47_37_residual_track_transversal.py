#!/usr/bin/env python3
"""Exact integer regression for V47_37_RESIDUAL_TRACK_TRANSVERSAL.md.

For each sorted four-part profile with part sizes in 1..7 and total >=19,
maximize the union-bound count of transversals blocked by at most seven
cross-part edges. Relax actual vertex-degree constraints to the necessary
part-sum constraints sum_j x_ij <= 2*a_i. If even this relaxation blocks
fewer than all transversals, an independent transversal must exist.
"""
from itertools import combinations, combinations_with_replacement
from math import prod

PAIRS = list(combinations(range(4), 2))


def max_forbidden_bound(a):
    edge_weights = []
    edge_caps = []
    for i, j in PAIRS:
        w = prod(a[k] for k in range(4) if k not in (i, j))
        cap = min(7, a[i] * a[j], 2 * a[i], 2 * a[j])
        edge_weights.append(w)
        edge_caps.append(cap)

    best = -1
    best_allocation = None

    def dfs(idx, allocation, part_load, total_edges, objective):
        nonlocal best, best_allocation
        if idx == len(PAIRS):
            if objective > best:
                best = objective
                best_allocation = allocation[:]
            return

        i, j = PAIRS[idx]
        max_here = min(
            edge_caps[idx],
            7 - total_edges,
            2 * a[i] - part_load[i],
            2 * a[j] - part_load[j],
        )
        for count in range(max_here + 1):
            part_load[i] += count
            part_load[j] += count
            dfs(
                idx + 1,
                allocation + [count],
                part_load,
                total_edges + count,
                objective + count * edge_weights[idx],
            )
            part_load[i] -= count
            part_load[j] -= count

    dfs(0, [], [0] * 4, 0, 0)
    return best, best_allocation


profiles = sorted(
    {
        tuple(sorted(a, reverse=True))
        for a in combinations_with_replacement(range(1, 8), 4)
        if sum(a) >= 19
    },
    reverse=True,
)
assert len(profiles) == 64

minimum_margin = None
minimum_profile = None
minimum_pair = None
for a in profiles:
    total_transversals = prod(a)
    bound, allocation = max_forbidden_bound(a)
    margin = total_transversals - bound
    assert margin > 0, (a, total_transversals, bound, allocation)
    if minimum_margin is None or margin < minimum_margin:
        minimum_margin = margin
        minimum_profile = a
        minimum_pair = (total_transversals, bound, allocation)

assert minimum_margin == 63
assert minimum_profile == (7, 7, 4, 1)
assert minimum_pair[0] == 196 and minimum_pair[1] == 133

# Three-part lemma used to prove same-track residual fibers are cliques.
three_part_profiles = list(combinations_with_replacement(range(3, 8), 3))
assert len(three_part_profiles) == 35
for a, b, c in three_part_profiles:
    # Each of at most seven cross-track edges blocks at most max(a,b,c)
    # transversals, while abc >= 9*max(a,b,c).
    assert a * b * c > 7 * max(a, b, c), (a, b, c)

print("sorted part profiles checked:", len(profiles))
print("minimum transversal-count margin:", minimum_margin)
print("worst profile:", minimum_profile)
print("worst profile total / forbidden upper bound:", minimum_pair[0], minimum_pair[1])
print("three-part profiles checked:", len(three_part_profiles))
print("V47_37_RESIDUAL_TRACK_TRANSVERSAL_OK")
print("Scope: relaxed finite integer bound only; not global Q32 UNSAT.")
