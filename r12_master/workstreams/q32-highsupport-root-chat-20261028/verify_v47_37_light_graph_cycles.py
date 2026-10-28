#!/usr/bin/env python3
"""Exact finite regression for V47_37_OUTER_LIGHT_HOLONOMY.md.

Enumerate every weighted heavy-pair graph on seven outer blocks:
  k_ij in {0,1,2}, weighted degree <=2, total weight <=7.
A pair is light iff k_ij=0. Check the finite cycle-structure facts used in
the analytic proof. This does not enumerate vertex labels/matching maps and
does not certify global Q32 infeasibility.
"""
from itertools import combinations, permutations

N = 7
PAIRS = list(combinations(range(N), 2))
ALL_CYCLES = []
for k in range(3, N + 1):
    for seq in permutations(range(N), k):
        if seq[0] != min(seq) or seq[1] > seq[-1]:
            continue
        ALL_CYCLES.append(tuple(seq))

graph_count = 0
cycle_count = {}


def recurse(pos, weights, weighted_degree, total_weight):
    global graph_count
    if pos == len(PAIRS):
        graph_count += 1
        light = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                light[i][j] = light[j][i] = (weights[i][j] == 0)

        assert min(sum(light[i]) for i in range(N)) >= 4

        for cyc in ALL_CYCLES:
            k = len(cyc)
            if not all(light[cyc[i]][cyc[(i + 1) % k]] for i in range(k)):
                continue
            cycle_count[k] = cycle_count.get(k, 0) + 1

            has_light_chord = any(
                light[cyc[i]][cyc[j]]
                for i in range(k)
                for j in range(i + 1, k)
                if j != i + 1 and not (i == 0 and j == k - 1)
            )

            # A chordless C5 saturates every cycle vertex's heavy budget,
            # so both vertices outside it must be light to all five vertices.
            if k == 5 and not has_light_chord:
                outside = set(range(N)) - set(cyc)
                assert len(outside) == 2
                assert all(light[u][v] for u in outside for v in cyc)

            # A chordless C6/C7 would give each cycle vertex >=3 heavy
            # neighbors, violating weighted heavy degree <=2.
            if k in (6, 7):
                assert has_light_chord

            # If a diagonal of a light C4 has weight 2, its endpoints'
            # weighted heavy degree is saturated, so they are light to every
            # block outside that four-cycle.
            if k == 4:
                for i in range(4):
                    u, v = cyc[i], cyc[(i + 2) % 4]
                    if weights[u][v] == 2:
                        outside = set(range(N)) - {
                            u, v, cyc[(i + 1) % 4], cyc[(i + 3) % 4]
                        }
                        assert all(light[u][w] and light[v][w] for w in outside)
        return

    u, v = PAIRS[pos]
    for weight in (0, 1, 2):
        if weighted_degree[u] + weight > 2:
            continue
        if weighted_degree[v] + weight > 2:
            continue
        if total_weight + weight > 7:
            continue

        weights[u][v] = weights[v][u] = weight
        weighted_degree[u] += weight
        weighted_degree[v] += weight
        recurse(pos + 1, weights, weighted_degree, total_weight + weight)
        weighted_degree[u] -= weight
        weighted_degree[v] -= weight
        weights[u][v] = weights[v][u] = 0


recurse(0, [[0] * N for _ in range(N)], [0] * N, 0)

assert graph_count == 22054
assert cycle_count == {3: 326410, 4: 760725, 5: 1450512, 6: 1934100, 7: 1331640}
assert sum(cycle_count.values()) == 5803387

print("weighted heavy graphs checked:", graph_count)
print("light cycles checked by length:", dict(sorted(cycle_count.items())))
print("V47_37_LIGHT_GRAPH_CYCLE_DECOMPOSITION_OK")
print("Scope: weighted outer-block graph combinatorics only; not global Q32 UNSAT.")
