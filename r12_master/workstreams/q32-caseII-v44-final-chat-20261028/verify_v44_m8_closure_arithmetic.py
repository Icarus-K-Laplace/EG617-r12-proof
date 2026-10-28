#!/usr/bin/env python3
"""Arithmetic/set-system regression checks for the v=44,m=8 closure.

This verifier checks only finite arithmetic and 3-color L-set combinatorics used in
V44_M8_PAIR_RIGIDITY.md and V44_M8_CLOSURE.md. It does NOT verify:
- Kang--Pikhurko Theorems 1/4;
- the source Type-I factorization;
- the analytic W-pair rigidity proof;
- the graph-theoretic Turan equality theorem.
"""

from itertools import combinations, product


def turan_edges(n: int, r: int) -> int:
    q, rem = divmod(n, r)
    parts = [q + 1] * rem + [q] * (r - rem)
    inside = sum(s * (s - 1) // 2 for s in parts)
    return n * (n - 1) // 2 - inside


def main() -> None:
    # m=8 W multiplicity normal form.
    parts = sorted(
        tup for tup in product((2, 3), repeat=3)
        if sum(tup) <= 8
    )
    assert parts == [
        (2, 2, 2),
        (2, 2, 3),
        (2, 3, 2),
        (2, 3, 3),
        (3, 2, 2),
        (3, 2, 3),
        (3, 3, 2),
    ]
    assert sorted({tuple(sorted(t)) for t in parts}) == [
        (2, 2, 2), (2, 2, 3), (2, 3, 3)
    ]

    # KP (56,11) arithmetic in the pair-rigidity lemma.
    assert 56 * 55 // 2 == 1540
    assert turan_edges(56, 11) == 1425
    p_11_56 = 1425 - (56 // 11) + 1
    assert p_11_56 == 1421
    assert 1540 - p_11_56 == 119

    # a+b<=7, 2a+b>=12, a<=5 has unique nonnegative solution at the
    # maximal anti-neighborhood edge count used by the proof.
    feasible = []
    for a in range(7):
        for b in range(20):
            if a <= 5 and a + b <= 7 and 2 * a + b >= 12:
                feasible.append((a, b))
    assert feasible == [(5, 2)]

    # Any two >=2-subsets of three colors intersect.
    colors = range(3)
    large = [set(s) for k in (2, 3) for s in combinations(colors, k)]
    for A in large:
        for B in large:
            assert A & B

    # Three size-2 L-sets with pairwise intersections <=1 must be the
    # three distinct 2-subsets; every color then appears exactly twice.
    twos = [set(s) for s in combinations(colors, 2)]
    triples = []
    for A in twos:
        for B in twos:
            for C in twos:
                if all(len(X & Y) <= 1 for X, Y in ((A, B), (A, C), (B, C))):
                    triples.append((A, B, C))
                    counts = [sum(c in X for X in (A, B, C)) for c in colors]
                    assert counts == [2, 2, 2]
    assert triples

    # U-pool arithmetic in the surviving (3,3,2) normal form.
    assert 703 - 3 - 0 == 700
    exact_floor = 10 * 6 + 2 * 1 + 3
    assert exact_floor == 65
    assert 8 * exact_floor + 3 * 60 == 700

    # Ordinary 44-vertex alpha<=12 equality: balanced 12-partition has
    # 8 parts of size4 and 4 parts of size3, hence complement floor60.
    assert 8 * 4 + 4 * 3 == 44
    inside = 8 * 6 + 4 * 3
    assert inside == 60
    assert turan_edges(44, 12) == 44 * 43 // 2 - 60

    print("V44_M8_CLOSURE_ARITHMETIC_OK")


if __name__ == "__main__":
    main()
