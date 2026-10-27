#!/usr/bin/env python3
"""Arithmetic replay for the delta=12 frontier reductions.

Checks only:
- saturated alpha-critical integer kernels at G-edge counts 100,99,98;
- unique four-partite U part profile compatible with 49 support K4s;
- exact W four-partite profiles for epsilon_U=2,3,4;
- leave-edge totals for the (7,7,7,8) support kernel.

External extremal theorems and analytic graph arguments are not verified here.
"""

from itertools import combinations_with_replacement
from math import comb


def saturated_survivors(edge_count_g):
    out = []
    for a in range(1, 30):
        for b in range(a, 30):
            c = 29 - a - b
            if c < 5 or a * b < 49:
                continue
            e_c = edge_count_g - comb(a, 2) - comb(b, 2)
            if e_c < 0:
                continue
            e_j = comb(c, 2) - e_c
            if e_j < 49:
                continue
            if e_c < (c * c) // 4 - 1:
                continue
            out.append((a, b, c, e_c, e_j))
    return out


def fourpartite_u_profiles():
    out = []
    for parts in combinations_with_replacement(range(1, 30), 4):
        if sum(parts) != 29:
            continue
        if min(parts[i] * parts[j] for i in range(4) for j in range(i + 1, 4)) < 49:
            continue
        complete = sum(parts[i] * parts[j] for i in range(4) for j in range(i + 1, 4))
        if complete < 306:
            continue
        out.append((parts, complete, complete - 306))
    return out


def w_profiles(eps):
    comp_edges = 117 + eps
    out = []
    for parts in combinations_with_replacement(range(1, 19), 4):
        if sum(parts) != 18:
            continue
        t = sum(parts[i] * parts[j] for i in range(4) for j in range(i + 1, 4))
        if comp_edges <= t <= 121:
            out.append((parts, t - comp_edges))
    return out


def main():
    assert saturated_survivors(100) == []
    assert saturated_survivors(99) == []
    assert saturated_survivors(98) == [(7, 7, 15, 56, 49)]

    assert fourpartite_u_profiles() == [((7, 7, 7, 8), 315, 9)]

    expected_w = {
        2: [
            ((3, 4, 5, 6), 0),
            ((3, 5, 5, 5), 1),
            ((4, 4, 4, 6), 1),
            ((4, 4, 5, 5), 2),
        ],
        3: [
            ((3, 5, 5, 5), 0),
            ((4, 4, 4, 6), 0),
            ((4, 4, 5, 5), 1),
        ],
        4: [((4, 4, 5, 5), 0)],
    }
    for eps, want in expected_w.items():
        assert w_profiles(eps) == want, (eps, w_profiles(eps), want)

    # Four-partite U support accounting.
    assert 3 * 7 * 7 + 3 * 7 * 8 == 315
    assert 315 - 306 == 9  # target cross edges
    assert 49 * 6 == 294   # support-pair edges in L_U
    assert 306 - 294 == 12 # non-support L_U edges
    assert 3 * (7 * 8 - 49) == 21 # total leave pairs T_i-R
    assert 21 == 9 + 12

    print("DELTA12_FRONTIER_ARITHMETIC_OK")
    print("saturated G=100:", saturated_survivors(100))
    print("saturated G=99:", saturated_survivors(99))
    print("saturated G=98:", saturated_survivors(98))
    print("fourpartite U:", fourpartite_u_profiles())
    for eps in (2, 3, 4):
        print(f"epsilon_U={eps} W profiles:", w_profiles(eps))
    print("Scope: arithmetic only; no external theorem verification.")


if __name__ == "__main__":
    main()
