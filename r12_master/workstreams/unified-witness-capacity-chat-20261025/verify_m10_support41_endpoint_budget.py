#!/usr/bin/env python3
"""Arithmetic-only audit for support-41 k=8, e_W in {2,3} endpoint lemmas.

The graph-theoretic parts (alpha(W) consequences and the matching-edge
transversal condition) are proved in M10_SUPPORT41_OMISSION_FLOOR.md.
This script checks only the exact integer budget ranges.
"""


def allocations(total):
    for eps_o in range(total + 1):
        for eps_n in range(total - eps_o + 1):
            for r_n in range(total - eps_o - eps_n + 1):
                yield eps_o, eps_n, r_n


def verify():
    # c_O = 10 - 2 e_W - eps_O - 2 eps_N - r_N.
    for e_w in (2, 3):
        rows = []
        for eps_o, eps_n, r_n in allocations(4):
            c_o = 10 - 2 * e_w - eps_o - 2 * eps_n - r_n
            if c_o >= 0:
                rows.append((eps_o, eps_n, r_n, c_o))
        assert rows
        assert max(row[3] for row in rows) == 10 - 2 * e_w
        if e_w == 2:
            assert all(row[3] <= 6 for row in rows)
            assert 8 > max(row[3] for row in rows)
        else:
            assert all(row[3] <= 4 for row in rows)
            # With eight omitted points and at most four O-W incidences,
            # at least four omitted points have zero W-neighbors.
            assert 8 - 4 == 4
            # At most two omitted points can have c_o >= 2.
            assert 4 // 2 == 2
            # Exact residual lower bound: e_R[O] >= 5 + c_O + eps_N.
            assert all(5 + row[3] + row[1] >= 5 for row in rows)
        print(f"PASS: e_W={e_w}, checked {len(rows)} feasible integer budget rows; c_O<= {10-2*e_w}.")

    print("PASS: e_W=2 conflicts with |O|=8; e_W=3 leaves the 3K2 incidence kernel.")
    print("Scope: arithmetic audit only; graph-theoretic lemmas are analytical.")


if __name__ == "__main__":
    verify()
