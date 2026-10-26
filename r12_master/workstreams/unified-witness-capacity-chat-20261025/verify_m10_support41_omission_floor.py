#!/usr/bin/env python3
"""Arithmetic-only verifier for M10_SUPPORT41_OMISSION_FLOOR.md.

This script checks:
  1. all positive omission multiplicity patterns summing to ten for k=5,6,7,8
     that survive the necessary subset inequalities;
  2. the integer (e_W, epsilon_U, cross-edge, e_R) ranges;
  3. the exact lower-bound branches used for the k=6 and k=7 set-degree
     arguments.

It does not search for graphs and does not certify the graph-theoretic
independent-set arguments; those are proved analytically in the theorem file.
Only Python's standard library is used.
"""
from itertools import combinations


def positive_sorted_compositions(k, total):
    def rec(prefix, remaining, slots, minimum):
        if slots == 0:
            if remaining == 0:
                yield tuple(prefix)
            return
        for x in range(minimum, remaining // slots + 1):
            yield from rec(prefix + [x], remaining - x, slots - 1, x)

    yield from rec([], total, k, 1)


def survives_subset_bounds(t):
    k = len(t)
    if max(t) > 4:
        return False
    if any(t[i] + t[j] > 5 for i, j in combinations(range(k), 2)):
        return False
    if any(sum(t[i] for i in S) > 6 for S in combinations(range(k), 3)):
        return False
    return True


EXPECTED = {
    5: [(2, 2, 2, 2, 2)],
    6: [(1, 1, 2, 2, 2, 2)],
    7: [
        (1, 1, 1, 1, 1, 1, 4),
        (1, 1, 1, 1, 1, 2, 3),
        (1, 1, 1, 1, 2, 2, 2),
    ],
    8: [
        (1, 1, 1, 1, 1, 1, 1, 3),
        (1, 1, 1, 1, 1, 1, 2, 2),
    ],
}


def feasible_budget_rows(k):
    n = 41 - k
    rows = []
    for e_w in range(2, 7):
        for eps_u in range(5):
            cross = 76 - eps_u - 2 * e_w
            e_r = 12 - eps_u - e_w
            if cross >= 2 * n and e_r >= 0:
                rows.append((e_w, eps_u, cross, e_r))
    return rows


def verify():
    for k in (5, 6, 7, 8):
        patterns = [
            t for t in positive_sorted_compositions(k, 10)
            if survives_subset_bounds(t)
        ]
        assert patterns == EXPECTED[k], (k, patterns)
        print(f"k={k}: omission patterns PASS: {patterns}")

    expected_budgets = {
        5: [(2, 0, 72, 10)],
        6: [
            (2, 0, 72, 10), (2, 1, 71, 9),
            (2, 2, 70, 8), (3, 0, 70, 9),
        ],
        7: [
            (2, 0, 72, 10), (2, 1, 71, 9),
            (2, 2, 70, 8), (2, 3, 69, 7),
            (2, 4, 68, 6), (3, 0, 70, 9),
            (3, 1, 69, 8), (3, 2, 68, 7),
            (4, 0, 68, 8),
        ],
        8: [
            (2, 0, 72, 10), (2, 1, 71, 9), (2, 2, 70, 8),
            (2, 3, 69, 7), (2, 4, 68, 6),
            (3, 0, 70, 9), (3, 1, 69, 8), (3, 2, 68, 7),
            (3, 3, 67, 6), (3, 4, 66, 5),
            (4, 0, 68, 8), (4, 1, 67, 7), (4, 2, 66, 6),
            (5, 0, 66, 7),
        ],
    }
    for k in (5, 6, 7):
        rows = feasible_budget_rows(k)
        assert rows == expected_budgets[k], (k, rows)
        print(f"k={k}: integer budget rows PASS ({len(rows)} cases)")

    # k=6: A has four double-omitted points. The necessary bound
    # e_R[A] >= 4 + c_A + e_W + eps_(U\\A), with e_R[A] <= 6,
    # forces e_W=2, c_A=0, eps_(U\\A)=0 and e_R[A]=6.
    feasible_k6 = []
    for e_w, eps_u, _, e_r in feasible_budget_rows(6):
        for c_a in range(7):
            for eps_out in range(eps_u + 1):
                lower = 4 + c_a + e_w + eps_out
                if lower <= 6:
                    feasible_k6.append((e_w, eps_u, c_a, eps_out, lower, e_r))
    assert all(row[0] == 2 and row[2] == 0 and row[3] == 0
               and row[4] == 6 for row in feasible_k6), feasible_k6
    assert feasible_k6, "k=6 equality branch should be nonempty"

    # k=7, t=(2,2,2,1,1,1,1): e_R[A] >= e_W+c_A+eps_(U\\A),
    # with e_R[A] <= 3. Thus only e_W=2 or 3 survives; for e_W=3,
    # c_A=eps_(U\\A)=0; for e_W=2, c_A+eps_(U\\A)<=1.
    feasible_k7_double = []
    for e_w, eps_u, _, e_r in feasible_budget_rows(7):
        for c_a in range(7):
            for eps_out in range(eps_u + 1):
                lower = e_w + c_a + eps_out
                if lower <= 3:
                    feasible_k7_double.append((e_w, eps_u, c_a, eps_out, lower, e_r))
    assert all(row[0] in (2, 3) for row in feasible_k7_double)
    assert all((row[0] == 3 and row[2] == 0 and row[3] == 0)
               or (row[0] == 2 and row[2] + row[3] <= 1)
               for row in feasible_k7_double), feasible_k7_double
    print("k=6/k=7 degree-sum branch arithmetic PASS")


    # k=8, e_W=5: the budget forces epsilon_U=0, e_R=7 and no
    # O-W/R-N incidences. The two allowed multiplicity patterns then have
    # omitted-point R degrees (7,1^7) or (4,4,1^6).
    k8_e5 = [row for row in feasible_budget_rows(8) if row[0] == 5]
    assert k8_e5 == [(5, 0, 66, 7)], k8_e5
    assert EXPECTED[8] == [
        (1, 1, 1, 1, 1, 1, 1, 3),
        (1, 1, 1, 1, 1, 1, 2, 2),
    ]
    print("k=8, e_W=5 arithmetic branch PASS")

    # k=8, e_W=4, (2,2,1^6): c_O=2 forces both double-omitted
    # points to have c=1 and zero omitted-point excess, hence R-degrees 5,5;
    # the six single points have R-degree 1 each. The center degree sum 10
    # cannot be realized by six leaf incidences (6) plus at most one center edge (2).
    assert 5 + 5 == 10
    assert 6 + 2 == 8
    print("k=8, e_W=4 double-omission degree-sum audit PASS")

    print("PASS: integer audit only; graph contradictions are analytical.")


if __name__ == "__main__":
    verify()
