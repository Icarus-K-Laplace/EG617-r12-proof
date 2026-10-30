#!/usr/bin/env python3
"""Independent exact-arithmetic replay for the Q33 minimum-degree/core audit.

This is a finite arithmetic checker, not a graph search and not a formal proof
checker for the analytic Ramsey reductions. The analytic arguments and exact
hypotheses are in MINDEG12_47_SOURCE_COMPLETE_AUDIT.md.

Optional --certificate points to the retained 127-row rational
COMPLETION_CERTIFICATE.csv from FRONTEND_LINE_A_V1.zip.
"""
from __future__ import annotations
import argparse, csv
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb, ceil
from pathlib import Path


def p12(n):
    q, r = divmod(n, 12)
    return 12 * comb(q, 2) + q * r


def D(n):
    return comb(n, 2) - 11 * p12(n)


def triangle_free_shortest_odd_cycle_upper(n):
    out = []
    for k in range(2, (n - 1) // 2 + 1):
        outside = n - (2 * k + 1)
        out.append(2 * k + 1 + k * outside + (outside * outside) // 4)
    return out


def p3(n):
    q, r = divmod(n, 3)
    sizes = [q + 1] * r + [q] * (3 - r)
    return sum(comb(s, 2) for s in sizes), sizes


def support_configs(h):
    supports = [s for k in (2, 3, 4) for s in combinations(range(4), k)]
    out = []
    for cfg in combinations_with_replacement(supports, h):
        if sum(len(s) - 1 for s in cfg) != 5:
            continue
        deg = tuple(sum(i in s for s in cfg) for i in range(4))
        if min(deg) >= 2:
            out.append((cfg, deg))
    return out


def canonical_matrix(matrix):
    return min(tuple(matrix[rp[i]][cp[j]] for i in range(2) for j in range(2))
               for rp in permutations(range(2)) for cp in permutations(range(2)))


def f_pair(a, b):
    return max(0, 10-a-b) + a*max(0, b-2) + b*max(0, a-2)


def f_h4(a, b):
    return max(0, 9-a-b) + a*(b-1) + b*max(0, a-2)


def f_mixed(a, b):
    return max(0, 9-a-b) + a*max(0, b-3) + b*max(0, a-2)


def f_diamond(a, b):
    return max(0, 9-a-b) + a*max(0, b-2) + b*max(0, a-2)


def verify_completion_certificate(path):
    pairs = list(combinations(range(4), 2))
    patterns = [(11, 11, 11, 11), (10, 11, 11, 11)]
    expected = set()
    for s in patterns:
        for n in product(*(range(1, v+1) for v in s)):
            if sum(s) - sum(n) != 12:
                continue
            if any(s[i] == s[j] and n[i] > n[j] for i, j in pairs):
                continue
            expected.add((s, n))
    seen = set()
    per = {s: [0, Fraction(0)] for s in patterns}
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            s = tuple(map(int, row["s"].split(";")))
            n = tuple(map(int, row["n"].split(";")))
            lam = tuple(map(Fraction, row["lambda_"].split(";")))
            assert (s, n) in expected and (s, n) not in seen
            assert len(lam) == 4 and min(lam) >= 0
            assert all(lam[i] + lam[j] >= Fraction(1, n[i]*n[j]) for i, j in pairs)
            value = sum(lam[i] * n[i] * (13-s[i]) for i in range(4)) + 2*max(lam)
            assert value == Fraction(row["bound"]) and value < 1
            seen.add((s, n))
            per[s][0] += 1
            per[s][1] = max(per[s][1], value)
    assert seen == expected
    return {
        "rows": len(seen),
        "patterns": {str(s): {"rows": v[0], "maximum": str(v[1])} for s, v in per.items()},
    }


def verify():
    assert {n: D(n) for n in (13, 14, 23, 24, 25, 37)} == {
        13: 67, 14: 69, 23: 132, 24: 144, 25: 146, 37: 237
    }
    assert 24 * 12 // 2 == D(24)
    assert 2*2 - 5*2 + 9 > 0 and 25 - 4*2*9 < 0

    b23 = triangle_free_shortest_odd_cycle_upper(23)
    b25 = triangle_free_shortest_odd_cycle_upper(25)
    b18 = triangle_free_shortest_odd_cycle_upper(18)
    assert max(b23) == 122
    assert max(b25) == 145
    assert max(b18) == 73
    assert b25 == [145, 142, 137, 130, 121, 110, 97, 82, 65, 46, 25]
    assert comb(25, 2) - max(b25) == 155
    assert (25 * 12 + 4) // 2 == 152
    assert 155 > 152

    max_122_cost = 0
    for a in range(1, 11):
        b = 11-a
        costs = [1, min(a+1, b), min(a, b+1), 2]
        assert max(costs) <= 6
        max_122_cost = max(max_122_cost, max(costs))
    assert max_122_cost == 6
    assert max([3, 2, 1]) <= 3
    assert 2 + 2 <= 4

    assert 35*12//2 == 210
    assert 36*13//2 == 234
    assert ceil(37*13/2) == 241 > D(37)

    for eS in range(46):
        min_cross = max(0, 90 - 2*eS)
        assert eS + min_cross >= 45
    assert 234 + 10 + 45 == 289

    for z in range(1, 56):
        for da in range(1, 11):
            for db in range(1, 11):
                if da + db > z + 1:
                    continue
                for ga in range(0, 5):
                    for gb in range(0, 5-ga):
                        ta, tb = da+ga, db+gb
                        if ta+tb >= 12:
                            assert z + ga + gb >= ta + tb - 1 >= 11
    assert 210 + 66 + 11 == 287

    expected_turan = {1: 346, 2: 342, 3: 338, 4: 333}
    for q, target in expected_turan.items():
        p, parts = p3(47-q)
        lower = p + 12*q + 4 - comb(q, 2)
        assert lower == target and lower > 284

    configs = {h: support_configs(h) for h in (3, 4, 5)}
    assert {h: len(v) for h, v in configs.items()} == {3: 9, 4: 40, 5: 48}
    patterns = {h: sorted(set(tuple(sorted(d)) for _, d in rows)) for h, rows in configs.items()}
    assert patterns == {
        3: [(2,2,2,2)], 4: [(2,2,2,3)],
        5: [(2,2,2,4), (2,2,3,3)]
    }

    matrix_classes = set()
    for cfg, deg in configs[5]:
        high4 = {i for i,d in enumerate(deg) if d == 4}
        if high4:
            assert len(high4) == 1
            assert sum(len(s)==2 and not(set(s)&high4) for s in cfg) == 1
            continue
        high3 = {i for i,d in enumerate(deg) if d == 3}
        low2 = set(range(4))-high3
        if any(len(s)==2 and set(s)<=low2 for s in cfg):
            continue
        assert len(high3)==len(low2)==2
        assert sum(len(s)==2 and set(s)<=high3 for s in cfg)==1
        mixed=[s for s in cfg if len(s)==2 and len(set(s)&high3)==1]
        rows, cols = sorted(high3), sorted(low2)
        mat=[[sum(1 for s in mixed if i in s and j in s) for j in cols] for i in rows]
        assert [sum(row) for row in mat]==[2,2]
        assert [sum(mat[i][j] for i in range(2)) for j in range(2)]==[2,2]
        matrix_classes.add(canonical_matrix(mat))
    assert matrix_classes == {(0,2,2,0),(1,1,1,1)}

    minima = {
        "K11-K11 pair": min((f_pair(a,b),a,b) for a in range(1,11) for b in range(1,11)),
        "h=4 K10-K11": min((f_h4(a,b),a,b) for a in range(1,10) for b in range(1,11)),
        "P mixed": min((f_mixed(a,b),a,b) for a in range(1,10) for b in range(1,11)),
        "D mixed": min((f_diamond(a,b),a,b) for a in range(1,10) for b in range(1,11)),
    }
    assert [minima[k][0] for k in ("K11-K11 pair", "h=4 K10-K11", "P mixed", "D mixed")] == [6,6,4,5]

    for x in range(-1, 20):
        for y in range(-1, 20):
            assert max(0, x+y) >= max(0, x-1)+max(0, y-1)
    for x in range(0, 20):
        for y in range(0, 20):
            assert max(0, x+y-1) >= max(0, x-1)+max(0, y-1)

    return {
        "density_caps": {n: D(n) for n in (13,14,23,24,25,37)},
        "triangle_free_bounds_23_25_18": [max(b23), max(b25), max(b18)],
        "R335_extension_cost_max": max_122_cost,
        "R447_degree10_floor": 289,
        "R447_degree11_floor": 287,
        "support_configs": {h: len(v) for h,v in configs.items()},
        "support_degree_patterns": patterns,
        "mixed_matrix_classes": sorted(matrix_classes),
        "charge_minima": minima,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()
    result = verify()
    if args.certificate:
        result["127_row_certificate"] = verify_completion_certificate(args.certificate)
    print({"status": "PASS_EXACT_ARITHMETIC_REPLAY", **result})
