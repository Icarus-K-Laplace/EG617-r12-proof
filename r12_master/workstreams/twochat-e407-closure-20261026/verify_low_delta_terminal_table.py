#!/usr/bin/env python3
"""Finite integer audit of the E407 Q32 delta / epsilon_U ledger."""

def main():
    feasible = []
    for delta in range(3, 17):
        for eps_u in range(0, 5):
            if delta + eps_u <= 16 and eps_u + 2 * delta >= 9:
                e_u = 112 - delta
                e_w = 48 - eps_u - delta
                e_cross = 124 + eps_u + 2 * delta
                assert e_u + e_w + e_cross == 284
                assert e_w >= 32
                feasible.append((delta, eps_u, e_u, e_w, e_cross))

    expected_eps = {
        3: [3, 4],
        4: [1, 2, 3, 4],
        5: [0, 1, 2, 3, 4],
        6: [0, 1, 2, 3, 4],
        7: [0, 1, 2, 3, 4],
        8: [0, 1, 2, 3, 4],
        9: [0, 1, 2, 3, 4],
        10: [0, 1, 2, 3, 4],
        11: [0, 1, 2, 3, 4],
        12: [0, 1, 2, 3, 4],
        13: [0, 1, 2, 3],
        14: [0, 1, 2],
        15: [0, 1],
        16: [0],
    }
    actual_eps = {
        delta: [eps for d, eps, *_ in feasible if d == delta]
        for delta in range(3, 17)
    }
    assert actual_eps == expected_eps
    assert len(feasible) == sum(map(len, expected_eps.values())) == 57

    # Check every table row against the exact cross-edge formula and the
    # fixed total edge count. These assertions are not graph-realization checks.
    for delta, eps_u, e_u, e_w, e_cross in feasible:
        assert e_u == 112 - delta
        assert e_w == 48 - eps_u - delta
        assert e_cross == 124 + eps_u + 2 * delta
        assert e_u + e_w + e_cross == 284

    print("E407_LOW_DELTA_INTEGER_TABLE_OK")
    print(f"feasible (delta, epsilon_U) profiles: {len(feasible)}")
    for delta in range(3, 17):
        print(f"delta={delta}: epsilon_U={actual_eps[delta]}")
    print("Scope: exact budget arithmetic only; no analytic graph terminal is closed by this script.")


if __name__ == "__main__":
    main()
