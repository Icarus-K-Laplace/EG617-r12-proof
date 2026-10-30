#!/usr/bin/env python3
"""Independent finite arithmetic/support-shape verifier for Q33's 284-edge core.

This program certifies only:
  * the four Turan lower-bound calculations;
  * the exhaustive support-multiset degree patterns for |Z|=3,4,5;
  * the two 2x2 mixed-support matrix classes;
  * the finite integer minima used in the analytic inequalities;
  * the Kang-Pikhurko n=25,r=2 numerical substitution.

It does NOT search for graphs, and no failed search is used as a proof.
The graph-theoretic proof is in the accompanying Markdown assets.
"""

from itertools import combinations, combinations_with_replacement, permutations
from math import comb


def p3(n):
    q, r = divmod(n, 3)
    sizes = [q + 1] * r + [q] * (3 - r)
    return sum(comb(s, 2) for s in sizes), sizes


def canonical_matrix(matrix):
    candidates = []
    for rp in permutations(range(2)):
        for cp in permutations(range(2)):
            candidates.append(tuple(
                matrix[rp[i]][cp[j]]
                for i in range(2) for j in range(2)
            ))
    return min(candidates)


def support_configs(h):
    supports = [
        s for k in (2, 3, 4)
        for s in combinations(range(4), k)
    ]
    out = []
    for cfg in combinations_with_replacement(supports, h):
        if sum(len(s) - 1 for s in cfg) != 5:
            continue
        deg = tuple(sum(i in s for s in cfg) for i in range(4))
        if min(deg) >= 2:
            out.append((cfg, deg))
    return out


def f_pair(a, b):
    return max(0, 10-a-b) + a*max(0, b-2) + b*max(0, a-2)


def f_h4(a, b):
    return max(0, 9-a-b) + a*(b-1) + b*max(0, a-2)


def f_mixed(a, b):
    return max(0, 9-a-b) + a*max(0, b-3) + b*max(0, a-2)


def f_diamond(a, b):
    return max(0, 9-a-b) + a*max(0, b-2) + b*max(0, a-2)


def verify():
    # Attack I: four independent degree-12 vertices.
    expected = {1: 346, 2: 342, 3: 338, 4: 333}
    for q, target in expected.items():
        p, parts = p3(47-q)
        lower = p + 12*q + 4 - comb(q, 2)
        assert lower == target, (q, p, parts, lower)
        assert lower > 284

    # Exact support-multiset enumeration.
    configs = {h: support_configs(h) for h in (3, 4, 5)}
    assert {h: len(v) for h, v in configs.items()} == {
        3: 9, 4: 40, 5: 48
    }

    degree_patterns = {
        h: sorted(set(tuple(sorted(deg)) for _, deg in rows))
        for h, rows in configs.items()
    }
    assert degree_patterns == {
        3: [(2, 2, 2, 2)],
        4: [(2, 2, 2, 3)],
        5: [(2, 2, 2, 4), (2, 2, 3, 3)],
    }

    # h=3: every support family contains a 2-support.
    for cfg, _ in configs[3]:
        assert any(len(s) == 2 for s in cfg)

    # h=4: if no 2-support joins two degree-2 (K11) labels,
    # all three pairs are incident with the unique degree-3 (K10) label.
    for cfg, deg in configs[4]:
        high = {i for i, d in enumerate(deg) if d == 3}
        assert len(high) == 1
        bad = [
            s for s in cfg
            if len(s) == 2 and not (set(s) & high)
        ]
        if not bad:
            assert sum(len(s) == 2 for s in cfg) == 3
            triple = [s for s in cfg if len(s) == 3]
            assert len(triple) == 1
            assert not (set(triple[0]) & high)

    # h=5, (9,11,11,11): exactly one pair lies among the three K11 labels.
    # h=5, (10,10,11,11): absent a K11-K11 pair, one K10-K10
    # edge and four mixed edges remain; the mixed 2x2 matrix has row/column sums 2.
    matrix_classes = set()
    for cfg, deg in configs[5]:
        high4 = {i for i, d in enumerate(deg) if d == 4}
        if high4:
            assert len(high4) == 1
            assert sum(
                len(s) == 2 and not (set(s) & high4)
                for s in cfg
            ) == 1
            continue

        high3 = {i for i, d in enumerate(deg) if d == 3}
        low2 = set(range(4)) - high3
        assert len(high3) == len(low2) == 2

        has_k11_pair = any(
            len(s) == 2 and set(s) <= low2
            for s in cfg
        )
        if has_k11_pair:
            continue

        assert sum(
            len(s) == 2 and set(s) <= high3
            for s in cfg
        ) == 1
        mixed = [
            s for s in cfg
            if len(s) == 2 and len(set(s) & high3) == 1
        ]
        assert len(mixed) == 4

        rows = sorted(high3)
        cols = sorted(low2)
        matrix = [
            [
                sum(1 for s in mixed if i in s and j in s)
                for j in cols
            ]
            for i in rows
        ]
        assert [sum(row) for row in matrix] == [2, 2]
        assert [
            sum(matrix[i][j] for i in range(2))
            for j in range(2)
        ] == [2, 2]
        matrix_classes.add(canonical_matrix(matrix))

    assert matrix_classes == {
        (0, 2, 2, 0),  # double diagonal, up to relabeling
        (1, 1, 1, 1),  # all ones
    }

    # Exact integer minima over the complete feasible ranges.
    minima = {
        "K11 pair": min(
            (f_pair(a, b), a, b)
            for a in range(1, 11)
            for b in range(1, 11)
        ),
        "h=4 K10-K11": min(
            (f_h4(a, b), a, b)
            for a in range(1, 10)
            for b in range(1, 11)
        ),
        "P mixed pair": min(
            (f_mixed(a, b), a, b)
            for a in range(1, 10)
            for b in range(1, 11)
        ),
        "D mixed pair": min(
            (f_diamond(a, b), a, b)
            for a in range(1, 10)
            for b in range(1, 11)
        ),
    }
    assert minima["K11 pair"][0] == 6
    assert minima["h=4 K10-K11"][0] == 6
    assert minima["P mixed pair"][0] == 4
    assert minima["D mixed pair"][0] == 5

    # Kang-Pikhurko Theorem 1 at n=25,r=2.
    t2_25 = 13 * 12
    p2_25 = t2_25 - (25 // 2) + 1
    assert t2_25 == 156
    assert p2_25 == 145
    assert comb(25, 2) - p2_25 == 155

    print("PASS: Q33 284-edge finite arithmetic/support verifier")
    print("Turan lower bounds:", expected)
    print("Support configurations:", {h: len(v) for h, v in configs.items()})
    print("Support degree patterns:", degree_patterns)
    print("Mixed matrix classes:", sorted(matrix_classes))
    print("Integer minima:", minima)
    print("KP(25,2): t2=156, p2=145, H[W] floor=155")


if __name__ == "__main__":
    verify()
