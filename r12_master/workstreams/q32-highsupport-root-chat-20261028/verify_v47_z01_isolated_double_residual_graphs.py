#!/usr/bin/env python3
"""Exact necessary relaxation for the isolated-double two-K4 residual branch.

The eight residual vertices have parts (2,2,2,2) and are partitioned into
two transversal K4s. Their 12 possible cross-K4 edges are the only possible
extra edges in this relaxation. Each T0 residual vertex has baseline C-degree
3; pointwise balanced-coloring saturation caps it at 4, so at most one extra
edge may be incident to each of the two T0 vertices. Enumerate all bases and
all extra sets of size 0..3 subject to that cap.

This counts a necessary relaxation, not source-realizable gadget completions.
The special x/y star geometry in the source is stricter still.
"""
from itertools import combinations, product
from collections import Counter

parts = (0, 1, 2, 3)  # one vertex per track in each K4
vertices = tuple((track, side) for track in range(4) for side in range(2))
part_of = {v: v[0] for v in vertices}

def base_edges(choice):
    # choice selects which side is in K4 A at each track; the complement is K4 B.
    A = {(i, choice[i]) for i in range(4)}
    B = {(i, 1-choice[i]) for i in range(4)}
    base = set()
    for clique in (A, B):
        for (i, si), (j, sj) in combinations(clique, 2):
            base.add(tuple(sorted(((i, si), (j, sj)))))
    cross = {
        tuple(sorted(((i, choice[i]), (j, 1-choice[j]))))
        for i in range(4) for j in range(4) if i != j
    }
    # Include the reverse direction for every unordered track pair.
    cross = set()
    for i in range(4):
        for j in range(i+1, 4):
            cross.add(tuple(sorted(((i, choice[i]), (j, 1-choice[j])))))
            cross.add(tuple(sorted(((i, 1-choice[i]), (j, choice[j])))))
    assert len(base) == 12 and len(cross) == 12 and base.isdisjoint(cross)
    return base, cross

counts = Counter()
bases = 0
for choice in product((0, 1), repeat=4):
    base, cross = base_edges(choice)
    bases += 1
    # Complementing all four bits swaps A and B, so each unordered base appears twice.
    if choice > tuple(1-x for x in choice):
        continue
    for g in range(4):
        for extra in combinations(sorted(cross), g):
            t0_degree_increment = [0, 0]
            for edge in extra:
                for track, side in edge:
                    if track == 3:
                        t0_degree_increment[side] += 1
            if sum(t0_degree_increment) > 1:
                continue
            # Any added cross-K4 edges preserve the two base K4s, so alpha <= 2.
            counts[g] += 1

assert bases == 16  # 8 unordered bases, each represented by two complementary bit vectors.
assert counts == Counter({0: 8, 1: 96, 2: 408, 3: 880})
print("unordered two-K4 bases:", 8)
print("graphs by surplus:", dict(sorted(counts.items())))
print("V47_Z01_ISOLATED_DOUBLE_RESIDUAL_GRAPHS_OK")
print("Scope: globally T0-capped necessary relaxation only; not global Q32 UNSAT.")
