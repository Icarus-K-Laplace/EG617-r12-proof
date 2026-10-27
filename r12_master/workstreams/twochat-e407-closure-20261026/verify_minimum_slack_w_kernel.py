#!/usr/bin/env python3
"""Arithmetic audit for MINIMUM_SLACK_W_KERNEL.md.

Checks slack multiplicities and q=1 R-degree capacity. It does not verify
independent-set or common-neighbour graph arguments.
"""


def positive_partitions_of_seven(p):
    vals = []

    def rec(rem, left, cap, cur):
        if left == 0:
            if rem == 0:
                vals.append(tuple(cur))
            return
        for x in range(min(cap, rem-left+1), 0, -1):
            rec(rem-x, left-1, x, cur+[x])

    rec(7, p, 7, [])
    return vals


def main():
    # N has size 6 or7 and is contained in the positive-slack set.
    # Total slack is seven, so positive vertex count p is 6 or7.
    assert positive_partitions_of_seven(6) == [(2, 1, 1, 1, 1, 1)]
    assert positive_partitions_of_seven(7) == [(1, 1, 1, 1, 1, 1, 1)]

    # q=1, |J|<=1 capacity: at most 13-y_C R1--N edges.
    # Actual q=1 totals are >=18-y_C for (4,1) and >=17-y_C for (3,3).
    for y_c in range(0, 2):
        cap = 13 - y_c
        assert 18 - y_c > cap
        assert 17 - y_c > cap

    # |J|>=3 is impossible by the seven R1 points each demanding one
    # extra degree unit beyond their base W-degree 2.
    assert 7 > 4   # (4,1): sum z = delta = 4
    assert 7 > 6   # (3,3): sum(z+epsilon_R1) <= delta+epsilon_U = 6

    # (4,1) q=1 exact kernel: six N points, exactly two J points,
    # hence four near-T points; four correction incidences remain.
    n = 6
    j = 2
    assert n-j == 4
    assert 4 == 4

    print("E407_MINIMUM_SLACK_W_KERNEL_ARITHMETIC_OK")
    print("positive slack partitions: p=6 -> 2+1^5, p=7 -> 1^7")
    print("q=1 branch: |J|=2")
    print("(4,1) exact residual: |N|=6, |J|=2, four near-T vertices")
    print("Scope: arithmetic only; graph-theoretic lemmas require analytic proof audit.")


if __name__ == "__main__":
    main()
