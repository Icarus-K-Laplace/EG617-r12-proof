#!/usr/bin/env python3
"""Arithmetic regression checks for the corrected Q32 support reductions.

This verifier checks only the integer implications in
Q32_CORRECTED_NONFULL_SUPPORT_MULTIPLICITY.md,
Q32_CASEI_LOW_SUPPORT_MATCHING_EXCLUSION.md, and
Q32_CASEI_V46_FULL_DEGREE_RIGIDITY.md.
It does not verify the analytic Type-I/shell matching lemmas themselves.
"""


def main() -> None:
    # Universal nonfull-support inequality |W|(m-6) <= m.
    assert 3 * (10 - 6) > 10  # v=44,m=10 impossible
    assert 3 * (9 - 6) == 9   # v=44,m=9 equality

    # Case I improves m-6 to m-3 because nu(M)<=3.
    for m in (8, 9, 10):
        assert 3 * (m - 3) > m  # v=44
        assert 2 * (m - 3) > m  # v=45

    # At Case-I v=46, n>=m-3. Full degree floors:
    # target 13; exact 4m+n; nonexact floors L_m.
    L = {8: 9, 9: 5, 10: 2}
    feasible = {}
    for m in (8, 9, 10):
        vals = []
        for n in range(m - 3, m + 1):
            total = 13 + 4 * m + n + L[m]
            if total <= 60:
                vals.append((n, total))
        feasible[m] = vals

    assert feasible[10] == []
    assert feasible[9] == [(6, 60)]
    assert feasible[8] == [(5, 59), (6, 60)]

    # v=44,m=9: n_w=3 at all three W points. If t triple-type
    # colors exist, each contributes to t_w at two non-special W points;
    # each W has t_w<=1 from 12+t_w<=13.
    for t in range(10):
        if 2 * t <= 3:
            assert t <= 1

    print("Q32_CORRECTED_SUPPORT_REDUCTIONS_ARITHMETIC_OK")


if __name__ == "__main__":
    main()
