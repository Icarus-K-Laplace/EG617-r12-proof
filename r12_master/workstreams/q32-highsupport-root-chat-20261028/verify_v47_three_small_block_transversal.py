#!/usr/bin/env python3
"""Exact local regression for V47_ZERO_SLACK_MAP_ALIGNMENT_AND_TRANSVERSAL_BLOCKER.md.

Normalize the three small blocks' light matchings to identity. Each outer block
has one 5-edge pair to each small block: either all three matchings are aligned
with arbitrary legal extra edges, or one matching is a transposition and the
three extra edges are the synchronized switch. For every outer vertex q, this
script computes all excluded labels i for which an independent transversal of
the other three labels can avoid q. It checks the singleton-/double-track
classification only; it does not solve the global Q32 graph.
"""
from itertools import permutations
from collections import Counter

ID = (0, 1, 2, 3)
PERMS = list(permutations(range(4)))
TRANSPOSITIONS = [
    p for p in PERMS
    if sum(p[i] != i for i in range(4)) == 2
    and any(p[i] != i and p[p[i]] == i for i in range(4))
]


def legal_extra_edges(matching):
    # (small-block label, outer-block vertex); not a matching edge.
    return [
        (label, q)
        for label in range(4)
        for q in range(4)
        if label != matching[q]
    ]


def escape_labels(neighbor_label_sets):
    """Excluded label i admits an independent transversal on [4]\{i}
    that avoids q in all three small blocks.
    """
    escapes = []
    for excluded in range(4):
        labels = [x for x in range(4) if x != excluded]
        found = False
        for a in labels:
            for b in labels:
                for c in labels:
                    if len({a, b, c}) != 3:
                        continue
                    if (
                        a not in neighbor_label_sets[0]
                        and b not in neighbor_label_sets[1]
                        and c not in neighbor_label_sets[2]
                    ):
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if found:
            escapes.append(excluded)
    return escapes


def check_configuration(matchings, extras, kind, counters):
    sets_by_q = [
        [set() for _ in range(3)]
        for _ in range(4)
    ]
    for q in range(4):
        for j in range(3):
            sets_by_q[q][j].add(matchings[j][q])
    for j, (label, q) in enumerate(extras):
        assert label != matchings[j][q]
        sets_by_q[q][j].add(label)

    for q, sets in enumerate(sets_by_q):
        common = set.intersection(*sets)
        assert 1 <= len(common) <= 2, (kind, matchings, extras, q, sets)
        escapes = escape_labels(sets)
        if len(common) == 1:
            h = next(iter(common))
            assert escapes == [h], (kind, matchings, extras, q, sets, escapes)
            counters["singleton-track vertices"] += 1
        else:
            assert escapes == [], (kind, matchings, extras, q, sets, escapes)
            # Two common labels mean q receives the extra edge in every pair.
            assert all(edge[1] == q for edge in extras), (
                kind, matchings, extras, q, sets
            )
            assert len({edge[0] for edge in extras}) == 1, (
                kind, matchings, extras, q, sets
            )
            counters["double-track vertices"] += 1
        counters["vertex records"] += 1


counters = Counter()
aligned_count = 0
for ea in legal_extra_edges(ID):
    for eb in legal_extra_edges(ID):
        for ec in legal_extra_edges(ID):
            aligned_count += 1
            check_configuration(
                [ID, ID, ID], [ea, eb, ec], "aligned", counters
            )

switch_count = 0
for tau in TRANSPOSITIONS:
    moved = [i for i in range(4) if tau[i] != i]
    for odd in range(3):
        matchings = [ID, ID, ID]
        matchings[odd] = tau
        for s in moved:
            extras = []
            for j in range(3):
                # Two aligned pairs use (s, tau(s)); the transposed pair
                # uses (s, s), exactly as in the 4,5,5 switch lemma.
                extras.append((s, s if j == odd else tau[s]))
            switch_count += 1
            check_configuration(matchings, extras, "switch", counters)

assert aligned_count == 12 ** 3 == 1728
assert switch_count == 6 * 3 * 2 == 36
assert counters["vertex records"] == 4 * (aligned_count + switch_count) == 7056
assert counters["double-track vertices"] == 12
assert counters["singleton-track vertices"] == 7044

print("aligned normalized configurations:", aligned_count)
print("synchronized switch configurations:", switch_count)
print("vertex records:", counters["vertex records"])
print("singleton-track vertices:", counters["singleton-track vertices"])
print("double-track vertices:", counters["double-track vertices"])
print("V47_ZERO_SLACK_TRANSVERSAL_LOCAL_OK")
print("Scope: exact local label/transversal classification only; not global Q32 UNSAT.")
