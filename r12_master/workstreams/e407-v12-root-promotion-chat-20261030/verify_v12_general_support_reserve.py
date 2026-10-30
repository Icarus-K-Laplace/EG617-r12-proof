#!/usr/bin/env python3
"""Arithmetic verifier for V12_GENERAL_SUPPORT_RESERVE.md.

This checks the Turan floors, core-ledger upper bounds, and the finite
support-size comparisons. It does not certify the analytic graph hypotheses.
"""
from itertools import combinations_with_replacement
from math import comb


def p_alpha(n: int, alpha: int) -> int:
    q, r = divmod(n, alpha)
    return (alpha - r) * comb(q, 2) + r * comb(q + 1, 2)


def t4(n: int) -> int:
    return comb(n, 2) - p_alpha(n, 4)


def upper(v: int) -> int:
    return comb(v, 2) - 12 * v + 284 - p_alpha(47 - v, 4)


def lower_seven(v: int) -> int:
    return 294 + 4 * p_alpha(v, 12)


def lower_all_exact(v: int, m: int) -> int:
    return m * max(42, p_alpha(v, 12)) + (11 - m) * p_alpha(v, 12)


def main() -> None:
    rows = []
    for v in range(29, 48):
        rows.append({
            "v": v,
            "p12": p_alpha(v, 12),
            "lower_7": lower_seven(v),
            "upper": upper(v),
            "margin": lower_seven(v) - upper(v),
        })

    excluded_7 = [r["v"] for r in rows if r["margin"] > 0]
    assert excluded_7 == [29, 30, 31, 32, 33]
    assert lower_seven(34) == upper(34) == 422
    assert lower_seven(35) == 430 and upper(35) == 447
    assert p_alpha(19, 4) == 36
    assert p_alpha(13, 4) == 15
    assert p_alpha(34, 12) == 32

    # The m=8 support floor: v=29 is impossible by Turan; v=30
    # is forced four-partite by the second-Turan bound, then ruled out
    # by the pair-product requirement for 56 linear K4 blocks.
    assert 42 * 8 > t4(29)
    assert t4(30) == 337
    assert t4(30) - (30 // 4) + 1 == 331
    admissible_partitions = [
        parts for parts in combinations_with_replacement(range(1, 31), 4)
        if sum(parts) == 30
        and all(parts[i] * parts[j] >= 56 for i in range(4) for j in range(i + 1, 4))
    ]
    assert admissible_partitions == []

    support_floors = {8: 31, 9: 32, 10: 34}
    resulting_floors = {8: 35, 9: 35, 10: 36}
    all_exact_rows = {}
    for m, v0 in support_floors.items():
        impossible = [v for v in range(v0, 48) if lower_all_exact(v, m) > upper(v)]
        assert impossible == list(range(v0, resulting_floors[m]))
        assert all(lower_all_exact(v, m) <= upper(v)
                   for v in range(resulting_floors[m], 48))
        all_exact_rows[m] = {
            "initial_support_floor": v0,
            "excluded_support_sizes": impossible,
            "resulting_support_floor": resulting_floors[m],
        }

    print("V12_GENERAL_SUPPORT_RESERVE_ARITHMETIC_OK")
    print("seven_color_excluded_v=", excluded_7)
    print("v34_equality=", lower_seven(34), upper(34))
    print("all_exact_color_support=", all_exact_rows)


if __name__ == "__main__":
    main()
