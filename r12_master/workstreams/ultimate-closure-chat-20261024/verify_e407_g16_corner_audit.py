#!/usr/bin/env python3
"""Check the local TD(4,7)-with-an-eighth-point counterexample.

This verifies the incidence inference audit only. It does not construct or
claim a full 47-vertex EG617 core.
"""
from itertools import combinations


def blocks_with_extra_point():
    blocks = []
    for a in range(7):
        for b in range(7):
            d = (a + 2 * b) % 7
            if (a, b) == (0, 0):
                d = 7  # eighth point z replaces D_0 in one block
            blocks.append(((0, a), (1, b), (2, (a + b) % 7), (3, d)))
    return blocks


def main():
    blocks = blocks_with_extra_point()
    assert len(blocks) == 49
    assert len(set(blocks)) == 49

    # Every cross-part pair occurs at most once.
    for i, j in combinations(range(4), 2):
        pairs = [(q[i][1], q[j][1]) for q in blocks]
        assert len(set(pairs)) == 49, (i, j)

    # The 4-sets remain linear.
    for q1, q2 in combinations(blocks, 2):
        assert len(set(q1) & set(q2)) <= 1

    # T is seven original D points plus A_0. It hits all blocks but contains
    # no full part.
    T = {(3, d) for d in range(7)} | {(0, 0)}
    assert len(T) == 8
    assert all(set(q) & T for q in blocks)
    assert sum(v[0] == 0 for v in T) == 1
    assert sum(v[0] == 1 for v in T) == 0
    assert sum(v[0] == 2 for v in T) == 0
    assert sum(v[0] == 3 for v in T) == 7

    # Complete K_{7,7,7,8} has 315 edges; five unused cross-part pairs can
    # be deleted while preserving all 49 witness blocks, leaving 310 edges.
    complete_edges = 7*7 + 7*7 + 7*8 + 7*7 + 7*8 + 7*8
    assert complete_edges == 315
    witness_edges = 49 * 6
    assert witness_edges == 294
    unused_pairs = 3 * (7*8 - 49)
    assert unused_pairs == 21
    assert unused_pairs >= 5
    assert complete_edges - 5 == 310
    print("PASS: eighth point can be used; a size-8 transversal need not contain a full part")
    print("PASS: 49 linear K4 blocks survive five deletions from unused pairs")
    print("AUDIT ONLY: no full-core extension or EG617 contradiction claimed")


if __name__ == "__main__":
    main()
