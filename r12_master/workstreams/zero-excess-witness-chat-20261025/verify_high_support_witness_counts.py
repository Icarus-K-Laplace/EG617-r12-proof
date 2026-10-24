#!/usr/bin/env python3
"""Integer checks for the R12 exact-129 high-support witness dichotomy.

This verifies the row-count inequalities and the m vs c-m pigeonhole split.
It does not certify any graph completion or terminal exclusion.
"""
from math import ceil


def min_high_labels(c_s: int) -> int:
    # Sum k_b <= 10 + 2h when ten labels have k_b in {0,1,2,3}.
    return ceil((c_s - 10) / 2)


def check() -> None:
    # E407 Q32 templates A/B, C/D, E: beta=e(M[S]) is 0,1,2.
    e407 = {0: 22, 1: 21, 2: 20}
    for beta, c_s_floor in e407.items():
        h_floor = min_high_labels(c_s_floor)
        assert h_floor == (6 if beta in (0, 1) else 5)
        print(f"E407 beta={beta}: c_S>={c_s_floor}, h>={h_floor}")

    # E408 Q33 exact budget: c_S >= 22-beta.
    for beta in range(4):
        c_s_floor = 22 - beta
        h_floor = min_high_labels(c_s_floor)
        assert h_floor == (6 if beta in (0, 1) else 5)
        print(f"E408 Q33 beta={beta}: c_S>={c_s_floor}, h>={h_floor}")

    # In the h=5 boundary, c exact-129 colors split into m low-only
    # and c-m hub-forced colors. For c>=7, one side has at least four.
    for c in (7, 8, 9, 10, 11):
        for m in range(c + 1):
            assert max(m, c - m) >= 4
        print(f"c={c}: max(m,c-m)>=4 for every m")


if __name__ == "__main__":
    check()
    print("HIGH_SUPPORT_COUNT_AUDIT_OK")
