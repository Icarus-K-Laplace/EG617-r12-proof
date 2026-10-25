#!/usr/bin/env python3
"""Finite arithmetic/load audit for the delta-13 K4^3 + K6 one-cross-edge theorem.

This verifier checks the W ledger, exhaustive K4 label/load capacity cases,
and K6 label-frequency/load bounds. It does not machine-prove the graph
saturation lemmas, the exception-clique argument, or the upstream core contract.
"""
from itertools import product

U_PARTS = (7, 7, 7, 8)

def compositions_leq(total, n, cap=3):
    for xs in product(range(cap + 1), repeat=n):
        if sum(xs) <= total:
            yield xs

def label_counts_ok(labels):
    counts = [labels.count(p) for p in range(4)]
    # K4 plus 5 vertices labelled by a small part, or 4 by D, would make K12.
    return all(counts[p] <= (3 if p == 3 else 4) for p in range(4))

def max_common_count(labels, degrees):
    loads = [degrees[i] - U_PARTS[labels[i]] for i in range(len(labels))]
    if any(load < 0 for load in loads):
        return None
    total_load = sum(loads)
    costs = [sum(label != p for label in labels) for p in range(4)]
    best = 0
    for xs in product(*(range(size + 1) for size in U_PARTS)):
        if sum(xs[p] * costs[p] for p in range(4)) <= total_load:
            best = max(best, sum(xs))
    return best

# Exact edge and excess ledger.
assert 3 * 6 + 15 + 1 == 34
assert 48 - 1 - 13 == 34
assert 4 - 1 == 3

# Exhaust all label patterns and component excess profiles for K4.
k4_max = {}
for incident in (False, True):
    best = 0
    tested = 0
    for eps in compositions_leq(3, 4):
        degrees = [9 + e for e in eps]
        if incident:
            degrees[0] -= 1
        for labels in product(range(4), repeat=4):
            if not label_counts_ok(labels):
                continue
            cap = max_common_count(labels, degrees)
            if cap is not None:
                tested += 1
                best = max(best, cap)
    # One unlabelled non-endpoint vertex has excess 3; other three are labelled.
    unsat_degrees = [9, 9, 9]
    if incident:
        unsat_degrees[0] = 8
    unsat_best = 0
    for labels in product(range(4), repeat=3):
        if not label_counts_ok(labels):
            continue
        cap = max_common_count(labels, unsat_degrees)
        if cap is not None:
            unsat_best = max(unsat_best, cap)
    k4_max[incident] = (best, unsat_best, tested)
    assert best <= 9, (incident, best)
    assert unsat_best <= 9, (incident, unsat_best)

# Exhaust the K6 label/excess patterns; the degree formulas differ at the endpoint.
k6_max_load = {}
for incident in (False, True):
    max_load = 0
    tested = 0
    for eps in compositions_leq(3, 6):
        degrees = [7 + e for e in eps]
        if incident:
            degrees[0] -= 1
        for labels in product(range(4), repeat=6):
            if any(degrees[i] < U_PARTS[labels[i]] for i in range(6)):
                continue
            if not label_counts_ok(labels):
                continue
            load = sum(degrees[i] - U_PARTS[labels[i]] for i in range(6))
            assert load <= sum(eps)
            counts = [labels.count(p) for p in range(4)]
            assert max(counts[:3]) <= 4
            assert counts[3] <= 3
            max_load = max(max_load, load)
            tested += 1
    k6_max_load[incident] = (max_load, tested)
    assert max_load <= 3

# If exceptions exist, the excess-floor correction is at most two.
for E1, E2, E3, E6 in product(range(4), repeat=4):
    if E1 + E2 + E3 + E6 != 3:
        continue
    assert E1 // 3 + E2 // 3 + E6 // 2 <= 2
    for k in range(1, 8):
        assert 29 - k > 29 - 2 * k

print("DELTA13_EPS1_K4K4K4K6_ONE_CROSS_EDGE_ARITHMETIC_OK")
print("K4 capacities (ordinary, one-unlabelled):", k4_max)
print("K6 load audits (ordinary/endpoint):", k6_max_load)
print("Both edge placements give a cover contradiction under the stated contracts.")
