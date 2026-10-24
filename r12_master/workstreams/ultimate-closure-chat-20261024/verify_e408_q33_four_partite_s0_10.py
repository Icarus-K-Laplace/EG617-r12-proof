#!/usr/bin/env python3
"""Integer-pattern checks for R12_E408_Q33_FOUR_PARTITE_S0_10_EXCLUSION.

This is an arithmetic/combinatorial case-table audit, not a graph realization
or independent proof certificate.
"""
from itertools import product


def degree_patterns(k: int):
    n = 16 - k
    target = 124 - 7 * k
    out = []

    def rec(prefix, left, slots, min_value=8):
        if slots == 0:
            if left == 0:
                out.append(tuple(prefix))
            return
        for value in range(min_value, 11):
            if value > left:
                break
            if left - value < 8 * (slots - 1):
                continue
            if left - value > 10 * (slots - 1):
                continue
            rec(prefix + [value], left - value, slots - 1, value)

    rec([], target, n)
    return out


def main():
    profiles = [
        (delta, 10 - 2 * delta)
        for delta in range(18)
        if 0 <= 10 - 2 * delta <= 4
        and delta + (10 - 2 * delta) <= 17
    ]
    assert profiles == [(3, 4), (4, 2), (5, 0)]
    assert all(delta - 2 >= 1 for delta, _ in profiles)

    patterns = {k: degree_patterns(k) for k in (4, 5, 6)}
    assert patterns[4] == [(8,) * 12]
    assert patterns[5] == [(8,) * 10 + (9,)]
    assert set(patterns[6]) == {
        (8,) * 8 + (9, 9),
        (8,) * 9 + (10,),
    }

    # Any size-8/9 hitting set that is not all of D must contain a full
    # large part. Thus at least ten group-based W vertices are forced for
    # k=4/5, and also for the (8^8,9^2) k=6 pattern, exceeding capacity 9.
    assert 16 - 4 - (6 - 4) == 10
    assert 16 - 5 - (6 - 5) == 10
    assert 16 - 6 - (6 - 6) == 10

    # Exceptional size-10 hitting set: s=0 gives <=9 large points; s=1
    # forces (3,3,3), with 27 pairs but at most 6+9+delta <= 20 explained;
    # s=2 forces (3,3,2), needing at least 7 extra L edges, while delta<=5.
    assert 3 * 3 + 3 * 2 + 3 * 2 == 21
    assert 6 + 9 + 5 == 20
    assert 3 * 3 - 2 * 3 == 3
    assert 3 * 2 - 2 * 2 == 2
    assert 3 + 2 + 2 == 7
    assert 7 > 5
    print("E408_Q33_FOUR_PARTITE_S0_10_AUDIT_OK")


if __name__ == "__main__":
    main()
