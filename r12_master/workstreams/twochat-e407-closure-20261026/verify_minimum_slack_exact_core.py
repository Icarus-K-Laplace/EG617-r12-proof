#!/usr/bin/env python3
"""Arithmetic audit for MINIMUM_SLACK_EXACT_CORE.md.

Checks omission partitions, resource inequalities, and the q/|N| reductions.
It does not verify the graph-theoretic independent-set or clique arguments.
"""


def partitions_of_seven(max_len=8):
    out = []

    def rec(rem, cap, cur):
        if rem == 0:
            out.append(tuple(cur + [0] * (max_len - len(cur))))
            return
        if len(cur) == max_len:
            return
        for x in range(min(cap, rem), 0, -1):
            rec(rem - x, x, cur + [x])

    rec(7, 7, [])
    return out


def deficit(part):
    return sum(max(0, 3 * r - 4) for r in part)


def zero_count(part):
    return sum(r == 0 for r in part)


def initial_patterns(delta, eps_u):
    budget = delta + eps_u
    return [p for p in partitions_of_seven() if max(p) <= 3 and deficit(p) <= budget]


def main():
    parts = partitions_of_seven()
    assert len(parts) == 15

    p33 = initial_patterns(3, 3)
    p41 = initial_patterns(4, 1)

    expected33 = [
        (3, 1, 1, 1, 1, 0, 0, 0),
        (2, 2, 2, 1, 0, 0, 0, 0),
        (2, 2, 1, 1, 1, 0, 0, 0),
        (2, 1, 1, 1, 1, 1, 0, 0),
        (1, 1, 1, 1, 1, 1, 1, 0),
    ]
    expected41 = [
        (3, 1, 1, 1, 1, 0, 0, 0),
        (2, 2, 1, 1, 1, 0, 0, 0),
        (2, 1, 1, 1, 1, 1, 0, 0),
        (1, 1, 1, 1, 1, 1, 1, 0),
    ]
    assert p33 == expected33
    assert p41 == expected41

    # Part-complete classes satisfy |C_i|<=4, so |C|<=12 and |N|>=6.
    # Every r=0 point is adjacent to all N, yielding q*|N|<=5q+eps_U.
    # Hence q<=3 for eps_U=3 and q<=1 for eps_U=1.
    assert max(q for q in range(1, 9) if 6 * q <= 5 * q + 3) == 3
    assert max(q for q in range(1, 9) if 6 * q <= 5 * q + 1) == 1

    # Profile (4,1): only q=1 survives.
    final41 = [p for p in p41 if zero_count(p) <= 1]
    assert final41 == [(1, 1, 1, 1, 1, 1, 1, 0)]
    q = 1
    eps_u = 1
    n_max = (5 * q + eps_u) // q
    assert n_max == 6
    assert 18 - n_max == 12

    # Profile (3,3): q=4 is excluded immediately. q=3 forces |N|=6
    # and all three epsilon units onto r=0 points; then delta=3 cannot
    # pay the positive-omission z-deficit for either q=3 pattern.
    survivors33 = []
    for p in p33:
        q = zero_count(p)
        if q > 3:
            continue
        if q == 3:
            # With |N|>=6, q|N|<=5q+3 is equality, so no epsilon remains
            # for positive-omission points. Required z is then the full deficit.
            assert deficit(p) in (4, 5)
            assert deficit(p) > 3
            continue
        survivors33.append(p)

    assert survivors33 == [
        (2, 1, 1, 1, 1, 1, 0, 0),
        (1, 1, 1, 1, 1, 1, 1, 0),
    ]

    # q=2 forces |N|=6, |C|=12; q=1 allows |N|=6 or7 because |C|>=11.
    assert (5 * 2 + 3) // 2 == 6
    assert (5 * 1 + 3) // 1 == 8  # global |N|<=7 tightens this to {6,7}

    print("E407_MINIMUM_SLACK_EXACT_CORE_ARITHMETIC_OK")
    print("initial (3,3) omission patterns:", p33)
    print("initial (4,1) omission patterns:", p41)
    print("final (3,3):", survivors33)
    print("final (4,1):", final41)
    print("Scope: integer omission/resource audit only; no graph realization certificate.")


if __name__ == "__main__":
    main()
