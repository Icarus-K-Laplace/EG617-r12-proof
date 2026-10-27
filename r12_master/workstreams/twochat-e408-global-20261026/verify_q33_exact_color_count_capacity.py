#!/usr/bin/env python3
"""Independent finite arithmetic checker for the Q33 m=10 exclusion.

This verifies the integer capacity calculations used in
Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md. It does not verify the
upstream graph-theoretic contracts or shell-label theorem.
"""
from math import comb


def max_k_sum(n: int, cost_budget: int) -> int:
    """Maximize sum(k_i), k_i in {0,1,2,3,4}, sum C(k_i,2)<=budget."""
    dp = [-10**9] * (cost_budget + 1)
    dp[0] = 0
    for _ in range(n):
        nxt = [-10**9] * (cost_budget + 1)
        for cost, value in enumerate(dp):
            if value < 0:
                continue
            for k in range(5):
                new_cost = cost + comb(k, 2)
                if new_cost <= cost_budget:
                    nxt[new_cost] = max(nxt[new_cost], value + k)
        dp = nxt
    return max(dp)


def main() -> None:
    # Check the pointwise inequality k <= 3/2 + C(k,2)/2
    # without floating point: 2k <= 3 + C(k,2).
    for k in range(5):
        assert 2 * k <= 3 + comb(k, 2), (k, comb(k, 2))

    # W has 16 vertices; e(H[W]) >= 24 gives e(complement H[W]) <= 96.
    max_h = (96 - 72) // 6
    assert max_h == 4

    # m=10: two unselected exact colors supply 20 four-sets.
    # Their U-incidence sum is at least 48, but their pair-cost budget
    # is at most delta+4h <= 17+16 = 33.
    m10_budget = 17 + 4 * max_h
    m10_capacity = max_k_sum(20, m10_budget)
    assert m10_budget == 33
    assert m10_capacity == 46
    assert m10_capacity < 48

    # m=9 and h=0: one unselected exact color supplies ten four-sets.
    # Pair-cost <= delta <= 17, but U-incidence sum must be >=24.
    m9_h0_capacity = max_k_sum(10, 17)
    assert m9_h0_capacity == 23
    assert m9_h0_capacity < 24

    print("PASS: Q33 exact-color component-witness capacity")
    print("pointwise inequality k <= 3/2 + C(k,2)/2: k=0..4 PASS")
    print("e(complement H[W]) <= 96 -> gadget-witness count h <= 4")
    print(f"m=10: 20 sets, pair-cost <= {m10_budget}, max U-incidence = {m10_capacity} < 48")
    print(f"m=9,h=0: 10 sets, pair-cost <= 17, max U-incidence = {m9_h0_capacity} < 24")
    print("Conclusion: m=10 impossible; m=9 requires h>=1.")
    print("Scope: arithmetic verifier only; upstream graph contracts remain conditional.")


if __name__ == "__main__":
    main()
