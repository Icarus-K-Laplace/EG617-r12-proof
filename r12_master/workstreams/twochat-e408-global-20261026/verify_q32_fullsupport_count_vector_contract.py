#!/usr/bin/env python3
"""Independent exact regression for the fixed E408 K61 color-count vectors.

This checks only edge-count bookkeeping. It is not a graph search, CSP solve,
source-gadget verifier, or Q32 impossibility certificate.
"""
from math import comb

N = 61
TOTAL_EDGES = comb(N, 2)
TARGET_COUNT = 408


def expected_counts(m):
    if m not in (8, 9, 10):
        raise ValueError("m must be 8, 9, or 10")
    counts = {0: TARGET_COUNT}
    counts.update({c: 129 for c in range(1, m + 1)})
    if m == 8:
        counts.update({9: 130, 10: 130, 11: 130})
    elif m == 9:
        counts.update({10: 130, 11: 131})
    else:
        counts[11] = 132
    return counts


def main():
    assert TOTAL_EDGES == 1830
    for m in (8, 9, 10):
        counts = expected_counts(m)
        assert set(counts) == set(range(12)), (m, set(counts))
        assert counts[0] == 408
        assert sum(counts.values()) == TOTAL_EDGES
        assert sum(counts[c] for c in range(1, 12)) == 1422
        assert sum(counts[c] - 129 for c in range(m + 1, 12)) == 3
        assert sum(counts[c] == 129 for c in range(1, 12)) == m
        assert all(counts[c] >= 129 for c in range(1, 12))
        print(f"m={m}: target=408; non-target=1422; excess=3; total=1830 PASS")
    assert 398 + 8 == 406 and 398 + 8 != TARGET_COUNT
    assert 398 + 9 == 407 and 398 + 9 != TARGET_COUNT
    assert 398 + 10 == 408
    print("REGRESSION: stale target formula 398+m is wrong for m=8,9 and right only for m=10")
    print("LIMITATION: count-vector arithmetic only; no graph realization or UNSAT claim")


if __name__ == "__main__":
    main()
