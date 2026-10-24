#!/usr/bin/env python3
"""Independent arithmetic cross-checks for the Exact Three-Anchor proof.

This is a finite verifier for local integer inequalities/equality layers only.
It is NOT a graph search and does not certify the all-r theorem by computation.
The all-r inequalities are proved analytically in LEMMA_VERIFICATION.md.
Uses only the Python standard library.
"""
from itertools import product


def R(a: int, b: int, p: int, q: int) -> int:
    return a * max(b - p, 0) + b * max(a - q, 0)


def check_thresholds():
    tests = {
        "R22 >= s-4": lambda a, b: R(a, b, 2, 2) >= a + b - 4,
        "R22 >= s-3 for s>=5": lambda a, b: a + b < 5 or R(a, b, 2, 2) >= a + b - 3,
        "R23 >= s-5": lambda a, b: R(a, b, 2, 3) >= a + b - 5,
        "R23 >= s-4 for s>=6": lambda a, b: a + b < 6 or R(a, b, 2, 3) >= a + b - 4,
        "R24 >= s-6": lambda a, b: R(a, b, 2, 4) >= a + b - 6,
        "R24 >= s-5 for s>=7": lambda a, b: a + b < 7 or R(a, b, 2, 4) >= a + b - 5,
        "R33 >= s-6": lambda a, b: R(a, b, 3, 3) >= a + b - 6,
        "R33 >= s-4 for s>=7": lambda a, b: a + b < 7 or R(a, b, 3, 3) >= a + b - 4,
    }
    for name, test in tests.items():
        bad = [(a, b) for a in range(1, 101) for b in range(1, 101) if not test(a, b)]
        assert not bad, (name, bad[:5])
    zeros = [
        (2, 2, lambda a, b: a <= 2 and b <= 2),
        (2, 3, lambda a, b: a <= 3 and b <= 2),
        (2, 4, lambda a, b: a <= 4 and b <= 2),
        (3, 3, lambda a, b: a <= 3 and b <= 3),
    ]
    for p, q, characterization in zeros:
        for a in range(1, 101):
            for b in range(1, 101):
                assert (R(a, b, p, q) == 0) == characterization(a, b), (p, q, a, b)
    return len(tests), 10000


def c3_r12_boundary():
    # Exact degree relation: a+b = 9 + gamma + n2 - k.
    rows = []
    for k in range(7):
        for gamma in range(3):
            for a in range(1, 11):  # |X1|=10
                for b in range(1, 10):  # |X3|=9
                    n2 = a + b - (9 + gamma - k)
                    if n2 < 0:
                        continue
                    local = k + R(a, b, 2, 2)
                    if local <= 6:
                        rows.append((k, gamma, a, b, n2, local))
    expected = {
        (0, 0, 1, 8, 0, 6), (0, 0, 8, 1, 0, 6),
        (1, 0, 1, 7, 0, 6), (1, 0, 7, 1, 0, 6),
        (2, 0, 1, 6, 0, 6), (2, 0, 6, 1, 0, 6),
        (3, 0, 1, 5, 0, 6), (3, 0, 5, 1, 0, 6),
        (4, 0, 1, 4, 0, 6), (4, 0, 2, 3, 0, 6),
        (4, 0, 3, 2, 0, 6), (4, 0, 4, 1, 0, 6),
        (5, 0, 1, 3, 0, 6), (5, 0, 2, 2, 0, 5),
        (5, 0, 3, 1, 0, 6),
        (6, 0, 1, 2, 0, 6), (6, 0, 2, 1, 0, 6),
        (6, 0, 2, 2, 1, 6),
        (6, 1, 2, 2, 0, 6),
    }
    assert set(rows) == expected, (set(rows) - expected, expected - set(rows))
    assert len(rows) == 19
    return rows


def c3_r13_boundary():
    # Exact degree relation: a+b = 10 + gamma + n2 - k.
    rows = []
    for k in range(7):
        for gamma in range(4):
            for a in range(1, 12):  # |X1|=11
                for b in range(1, 11):  # |X3|=10
                    n2 = a + b - (10 + gamma - k)
                    if n2 < 0:
                        continue
                    if k + R(a, b, 2, 2) <= 6:
                        rows.append((k, gamma, a, b, n2))
    expected = [(6, 0, 2, 2, 0)]
    assert rows == expected, rows
    return rows


def c4_r12_r24_equality():
    # (0,0,2), no focus, adjacent connector gamma>=1:
    # a+b >= 8 + gamma - k, capacities (2,4).
    rows = []
    for k in range(7):
        for gamma in range(1, 4):
            for a in range(1, 11):
                for b in range(1, 9):
                    if a + b >= 8 + gamma - k and k + R(a, b, 2, 4) <= 3:
                        rows.append((k, gamma, a, b, R(a, b, 2, 4)))
    assert rows == [(3, 1, 4, 2, 0)], rows
    return rows


def overlap_patterns_r12(long_size, short_size):
    # Two adjacent same-group nonfocused connectors with two focus slots.
    # For both: a+b >= 8 + gamma - k, gamma>=1, effective capacities (2,2).
    # Global relaxed lower bound: k1+k2+max(R1,R2) <= 6.
    rows = []
    for k1, k2, g1, g2 in product(range(7), range(7), range(1, 4), range(1, 4)):
        opts1 = [
            (a, b, R(a, b, 2, 2))
            for a in range(1, long_size + 1)
            for b in range(1, short_size + 1)
            if a + b >= 8 + g1 - k1
        ]
        opts2 = [
            (a, b, R(a, b, 2, 2))
            for a in range(1, long_size + 1)
            for b in range(1, short_size + 1)
            if a + b >= 8 + g2 - k2
        ]
        for a, b, r1 in opts1:
            for c, d, r2 in opts2:
                if k1 + k2 + max(r1, r2) <= 6:
                    rows.append((k1, k2, g1, g2, (a, b, r1), (c, d, r2)))
    assert len(rows) == 4, rows
    assert all(x[0:4] == (0, 0, 1, 1) for x in rows), rows
    orientations = {(x[4][0], x[4][1], x[5][0], x[5][1]) for x in rows}
    expected = {(1, 8, 1, 8), (1, 8, 8, 1), (8, 1, 1, 8), (8, 1, 8, 1)}
    assert orientations == expected, orientations
    return rows


def main():
    threshold_count, pair_count = check_thresholds()
    r12 = c3_r12_boundary()
    r13 = c3_r13_boundary()
    r24 = c4_r12_r24_equality()
    overlap_002 = overlap_patterns_r12(10, 8)
    overlap_011 = overlap_patterns_r12(9, 9)
    print(f"PASS: {threshold_count} threshold inequalities on {pair_count} positive-integer pairs")
    print("PASS: zero-charge characterizations for R22/R23/R24/R33 on 1<=a,b<=100")
    print(f"PASS: c=3, r=12 relaxed mixed-focus boundary has {len(r12)} rows")
    print("  exceptional rows: gamma=1 only (k,a,b,n2)=(6,2,2,0); gamma=0 includes the (k,a,b,n2)=(6,2,2,1) one-neighbour layer")
    print(f"PASS: c=3, r=13 boundary is uniquely {r13}")
    print(f"PASS: c=4 (0,0,2), r=12 R24 equality is uniquely {r24}")
    print(f"PASS: c=4 (0,0,2), r=12 two-focus overlap has {len(overlap_002)} relaxed orientation pairs")
    print(f"PASS: c=4 (0,1,1), r=12 two-slot overlap has {len(overlap_011)} relaxed orientation pairs")
    print("LIMITATION: this script checks local arithmetic relaxations only; it is not a graph/SAT counterexample search.")


if __name__ == "__main__":
    main()
