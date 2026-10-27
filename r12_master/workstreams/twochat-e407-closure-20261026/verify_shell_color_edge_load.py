#!/usr/bin/env python3
"""Finite arithmetic replay for SHELL_COLOR_EDGE_LOAD.md.

Checks only the integer lower bound in the three pivot-location cases.
It is not a graph-realization or exact-129-factor certificate.
"""

from math import comb


def alpha2_floor(t: int) -> int:
    # A graph on t vertices with alpha<=2 has complement triangle-free.
    return comb(t, 2) - (t * t // 4)


def p_selected_costs():
    out = []
    for r1 in range(1, 8):
        for r2 in range(1, 8 - r1):
            for r3 in range(1, 8 - r1 - r2):
                t = 7 - r1 - r2 - r3
                if t < 0:
                    continue
                cost = comb(r1, 2) + comb(r2, 2) + comb(r3, 2) + alpha2_floor(t)
                out.append((cost, r1, r2, r3, t))
    return out


def p_in_k5_costs():
    out = []
    for r1 in range(1, 7):
        for r2 in range(1, 7 - r1):
            t = 6 - r1 - r2
            if t < 0:
                continue
            cost = comb(r1, 2) + comb(r2, 2) + alpha2_floor(t)
            out.append((cost, r1, r2, t))
    return out


def p_in_gadget_costs():
    out = []
    for r1 in range(1, 7):
        for r2 in range(1, 7 - r1):
            for r3 in range(1, 7 - r1 - r2):
                t = 6 - r1 - r2 - r3
                if t < 0:
                    continue
                # With p in the gadget, its shell co-vertices must form a
                # color-c clique; otherwise p plus a nonadjacent pair is
                # independent of size 3 in the gadget.
                cost = comb(r1, 2) + comb(r2, 2) + comb(r3, 2) + comb(t, 2)
                out.append((cost, r1, r2, r3, t))
    return out


def main():
    cases = {
        "p_selected": p_selected_costs(),
        "p_in_unselected_K5": p_in_k5_costs(),
        "p_in_gadget": p_in_gadget_costs(),
    }
    minima = {name: min(row[0] for row in rows) for name, rows in cases.items()}
    assert minima == {
        "p_selected": 2,
        "p_in_unselected_K5": 2,
        "p_in_gadget": 2,
    }
    assert 7 * min(minima.values()) == 14
    assert 14 + 4 == 18
    print("E407_SHELL_COLOR_EDGE_LOAD_ARITHMETIC_OK")
    print("minima=", minima)
    print("exact_color_shell_edge_floor=14")
    print("all_non_target_color_scalar_floor=18")
    print("Scope: arithmetic only; no graph-realization certificate.")


if __name__ == "__main__":
    main()
