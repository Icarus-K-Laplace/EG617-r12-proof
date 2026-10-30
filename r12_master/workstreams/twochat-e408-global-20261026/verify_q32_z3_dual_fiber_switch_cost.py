#!/usr/bin/env python3
"""Exact finite audit of small/outer residual-fiber compatibility in E408 Q32.

This checks the six registered m=10, 3+7, z=3 residual graph types.
It enumerates every labelled four-fiber clique partition F and G, then
minimizes eta_D over the two local 4,5,5 patterns:
  * aligned: all four common labels occur once;
  * synchronized switch: one label occurs twice and one is omitted.

This certifies only the finite combinatorial classification. The per-block
inequality y_D >= eta_D and endpoint-load consequences are proved analytically
in Q32_Z3_DUAL_FIBER_SWITCH_COST_AUDIT.md. It is not a Q32 UNSAT solver.
"""
from collections import Counter
from itertools import combinations, permutations, product

PROFILES = {
    (3, 3, 1, 0),
    (3, 2, 2, 0),
    (3, 2, 1, 1),
    (2, 2, 2, 1),
}
RESIDUAL_GRAPHS = {
    "C6+K1": ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)),
    "2C3+K1": ((0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)),
    "P7": ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)),
    "C3+P4": ((0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 6)),
    "C4+P3": ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6)),
    "C5+P2": ((0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (5, 6)),
}
PERMUTATIONS = tuple(permutations(range(4)))
PATTERNS = {(0, 1, 2, 3)}
for duplicate in range(4):
    for missing in range(4):
        if duplicate != missing:
            others = [i for i in range(4) if i not in (duplicate, missing)]
            PATTERNS.add(tuple(sorted((duplicate, duplicate, *others))))
PATTERNS = tuple(sorted(PATTERNS))
assert len(PATTERNS) == 13

EXPECTED_PARTITION_COUNTS = {
    "C6+K1": 48,
    "2C3+K1": 168,
    "P7": 96,
    "C3+P4": 168,
    "C4+P3": 96,
    "C5+P2": 120,
}
EXPECTED_COST_DISTRIBUTIONS = {
    "C6+K1": {0: 1152, 3: 1152},
    "2C3+K1": {0: 7488, 1: 10368, 2: 10368},
    "P7": {0: 2304, 1: 3456, 2: 2304, 3: 1152},
    "C3+P4": {0: 6912, 1: 9792, 2: 9792, 3: 1728},
    "C4+P3": {0: 2304, 1: 2304, 2: 2304, 3: 2304},
    "C5+P2": {0: 2880, 1: 5760, 2: 5760},
}
EXPECTED_NONTRIVIAL_ZERO_COST = {
    ("2C3+K1", (3, 3, 1, 0), (3, 2, 1, 1)): 3456,
    ("C3+P4", (3, 2, 2, 0), (2, 2, 2, 1)): 1728,
    ("C3+P4", (3, 2, 2, 0), (3, 2, 1, 1)): 1152,
}

def profile(labels):
    return tuple(sorted((labels.count(i) for i in range(4)), reverse=True))

def unlabeled_partition(labels):
    return frozenset(
        frozenset(v for v in range(7) if labels[v] == i)
        for i in range(4)
        if labels.count(i)
    )

def enumerate_clique_partitions(edges):
    edge_set = {tuple(sorted(e)) for e in edges}
    result = []
    for labels in product(range(4), repeat=7):
        if profile(labels) not in PROFILES:
            continue
        if all(
            labels[u] != labels[v] or tuple(sorted((u, v))) in edge_set
            for u, v in combinations(range(7), 2)
        ):
            result.append(labels)
    return result

def pattern_costs(F, G):
    # M[i][j] = |F_i intersect G_j|.
    M = [
        [
            sum(1 for v in range(7) if F[v] == i and G[v] == j)
            for j in range(4)
        ]
        for i in range(4)
    ]
    f_sizes = [F.count(i) for i in range(4)]
    costs = {}
    for pattern in PATTERNS:
        total = sum(f_sizes[i] for i in pattern)
        best_overlap = max(
            sum(M[pattern[k]][perm[k]] for k in range(4))
            for perm in PERMUTATIONS
        )
        costs[pattern] = total - best_overlap
    return costs

def verify_zero_cost_split(F, G, costs):
    """Check the exact empty-fiber/one-split-fiber switch normal form."""
    zero_patterns = [p for p, value in costs.items() if value == 0]
    assert len(zero_patterns) == 1, (F, G, zero_patterns)
    pattern = zero_patterns[0]
    duplicated = [i for i in range(4) if pattern.count(i) == 2]
    missing = [i for i in range(4) if pattern.count(i) == 0]
    empty_F = [i for i in range(4) if F.count(i) == 0]
    assert len(duplicated) == len(missing) == len(empty_F) == 1
    assert duplicated[0] == empty_F[0]

    F_sets = [{v for v in range(7) if F[v] == i} for i in range(4)]
    G_sets = [{v for v in range(7) if G[v] == j} for j in range(4)]
    intact_F = [i for i in range(4) if i not in (duplicated[0], missing[0])]

    successful_assignments = []
    for perm in PERMUTATIONS:
        overlap = sum(
            len(F_sets[pattern[k]] & G_sets[perm[k]])
            for k in range(4)
        )
        total = sum(len(F_sets[i]) for i in pattern)
        if overlap == total:
            successful_assignments.append(perm)
    assert successful_assignments

    for perm in successful_assignments:
        used_G = {perm[k] for k in range(4) if pattern[k] != duplicated[0]}
        assert len(used_G) == 2
        for i in intact_F:
            assert F_sets[i] == G_sets[perm[pattern.index(i)]]
        remaining_G = set(range(4)) - used_G
        assert len(remaining_G) == 2
        left, right = tuple(remaining_G)
        assert G_sets[left].isdisjoint(G_sets[right])
        assert G_sets[left] | G_sets[right] == F_sets[missing[0]]
    return pattern

def main():
    total_ordered_pairs = 0
    total_zero_same = 0
    total_zero_mismatch = 0
    mismatch_profiles = Counter()

    for name, edges in RESIDUAL_GRAPHS.items():
        partitions = enumerate_clique_partitions(edges)
        assert len(partitions) == EXPECTED_PARTITION_COUNTS[name], (
            name, len(partitions)
        )

        costs = Counter()
        zero_same = 0
        zero_mismatch = 0
        mismatch_by_profile = Counter()
        for F in partitions:
            for G in partitions:
                pc = pattern_costs(F, G)
                minimum = min(pc.values())
                costs[minimum] += 1
                if minimum != 0:
                    continue
                if unlabeled_partition(F) == unlabeled_partition(G):
                    zero_same += 1
                else:
                    zero_mismatch += 1
                    key = (name, profile(F), profile(G))
                    mismatch_by_profile[key] += 1
                    verify_zero_cost_split(F, G, pc)

        assert dict(costs) == EXPECTED_COST_DISTRIBUTIONS[name], (
            name, dict(costs)
        )
        for key, value in mismatch_by_profile.items():
            mismatch_profiles[key] += value

        ordered_pairs = len(partitions) ** 2
        total_ordered_pairs += ordered_pairs
        total_zero_same += zero_same
        total_zero_mismatch += zero_mismatch
        print(
            f"{name}: partitions={len(partitions)}; pairs={ordered_pairs}; "
            f"costs={dict(sorted(costs.items()))}; "
            f"zero_same={zero_same}; zero_mismatch={zero_mismatch}"
        )

    assert dict(mismatch_profiles) == EXPECTED_NONTRIVIAL_ZERO_COST, (
        dict(mismatch_profiles), EXPECTED_NONTRIVIAL_ZERO_COST
    )
    assert total_ordered_pairs == 91584
    assert total_zero_same == 16704
    assert total_zero_mismatch == 6336
    print("nontrivial zero-cost profile pairs:")
    for key, value in sorted(mismatch_profiles.items()):
        print(f"  {key}: {value}")
    print(f"TOTAL_ORDERED_PARTITION_PAIRS={total_ordered_pairs}")
    print(f"ZERO_COST_SAME_PARTITION={total_zero_same}")
    print(f"ZERO_COST_DIFFERENT_PARTITION={total_zero_mismatch}")
    print("V47_Z3_DUAL_FIBER_SWITCH_COST_ENUMERATION_OK")
    print("Scope: exact 7-vertex partition-pair enumeration only; no Q32 UNSAT.")

if __name__ == "__main__":
    main()
