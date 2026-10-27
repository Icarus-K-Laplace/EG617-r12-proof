#!/usr/bin/env python3
"""Independent arithmetic replay for the E407 U-edge reserve closure.

This script certifies only the integer arithmetic in E407_FOUR_COLOR_U_RESERVE_CLOSURE.md.
It does not certify the V12 analytic reduction, support-block color identity, or theorem hypotheses.
"""

from math import comb


def p_independence_floor(n: int, alpha: int) -> int:
    q, r = divmod(n, alpha)
    return (alpha - r) * comb(q, 2) + r * comb(q + 1, 2)


def main() -> None:
    support_size = 29
    selected_blocks = 49
    block_size = 4
    selected_colors = 7
    non_target_colors = 11
    delta_max = 16

    selected_edges = selected_blocks * comb(block_size, 2)
    color_floor = p_independence_floor(support_size, 12)
    unselected_colors = non_target_colors - selected_colors
    available_total = selected_edges + delta_max

    # Shortest contradiction: one unselected non-target color already exceeds reserve.
    one_color_required = selected_edges + color_floor

    # Stronger aggregate check retained as a regression.
    all_unselected_required = selected_edges + unselected_colors * color_floor

    assert selected_edges == 294
    assert color_floor == 22
    assert unselected_colors == 4
    assert available_total == 310
    assert one_color_required == 316
    assert one_color_required > available_total
    assert color_floor > delta_max
    assert all_unselected_required == 382
    assert all_unselected_required > available_total

    print("E407_U_RESERVE_ARITHMETIC_OK")
    print(f"selected_edges={selected_edges}")
    print(f"p12_29={color_floor}")
    print(f"unselected_colors={unselected_colors}")
    print(f"available_total={available_total}")
    print(f"one_color_required={one_color_required}")
    print(f"one_color_gap={one_color_required - available_total}")
    print(f"all_unselected_required={all_unselected_required}")
    print(f"aggregate_gap={all_unselected_required - available_total}")


if __name__ == "__main__":
    main()
