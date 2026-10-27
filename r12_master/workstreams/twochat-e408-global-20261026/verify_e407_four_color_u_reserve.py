#!/usr/bin/env python3
"""Independent arithmetic replay for the E407 four-color U-edge reserve closure.

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
    required_total = selected_edges + unselected_colors * color_floor
    available_total = selected_edges + delta_max

    assert selected_edges == 294
    assert color_floor == 22
    assert unselected_colors == 4
    assert required_total == 382
    assert available_total == 310
    assert required_total > available_total
    assert unselected_colors * color_floor == 88
    assert delta_max == 16
    assert 88 > 16

    print("E407_FOUR_COLOR_U_RESERVE_ARITHMETIC_OK")
    print(f"selected_edges={selected_edges}")
    print(f"p12_29={color_floor}")
    print(f"unselected_colors={unselected_colors}")
    print(f"required_total={required_total}")
    print(f"available_total={available_total}")
    print(f"gap={required_total - available_total}")


if __name__ == "__main__":
    main()
