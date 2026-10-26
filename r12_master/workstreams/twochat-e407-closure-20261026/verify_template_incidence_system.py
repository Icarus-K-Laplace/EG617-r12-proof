#!/usr/bin/env python3
"""Arithmetic audit for the unified E407 five-template incidence theorem.

This checks only the finite row-count floors and the h-4 component-count
arithmetic. The graph-theoretic exact-129 factorization, alpha/clique
arguments, and edge-color uniqueness proof remain in the theorem note.
"""

TEMPLATES = {
    "A": {"high_k_floor": 6, "k3_floor": 6},
    "B": {"high_k_floor": 8, "k3_floor": 0},
    "C": {"high_k_floor": 6, "k3_floor": 6, "min_hub_hits": 3},
    "D": {"high_k_floor": 7, "k3_floor": 0},
    "E": {"high_k_floor": 5, "k3_floor": 0},
}
EXACT129_COLORS = 7
B_ROWS = 10
MIN_B_LABELLED_NO_S = 6


def main():
    assert B_ROWS - MIN_B_LABELLED_NO_S == 4
    results = {}
    for template, row in TEMPLATES.items():
        h = row["high_k_floor"]
        selected = h + MIN_B_LABELLED_NO_S - B_ROWS
        assert selected == h - 4
        assert selected > 0
        k3_selected = max(0, row["k3_floor"] + MIN_B_LABELLED_NO_S - B_ROWS)
        assert k3_selected <= selected
        per_color_shell_hits = selected * 3
        all_color_witnesses = selected * EXACT129_COLORS
        all_color_shell_hits = per_color_shell_hits * EXACT129_COLORS
        # Every high-k witness hits at least two S rows; each guaranteed k=3
        # witness contributes one additional hit.
        hub_hits_per_color = selected * 2 + k3_selected
        assert all_color_witnesses == selected * 7
        assert all_color_shell_hits == all_color_witnesses * 3
        results[template] = (
            selected, all_color_witnesses, hub_hits_per_color * 7,
            all_color_shell_hits
        )

    expected = {
        "A": (2, 14, 42, 42),
        "B": (4, 28, 56, 84),
        "C": (2, 14, 42, 42),
        "D": (3, 21, 42, 63),
        "E": (1, 7, 14, 21),
    }
    assert results == expected

    # Shell-support lemma: a 4-set hitting at most two of 13 shell rows
    # leaves at least 11 shell vertices; with pivot p these form K12.
    assert 13 - 2 == 11
    assert 11 + 1 == 12
    # Missing-hub lemma: Q independent, b nonadjacent to s, and Q anticomplete
    # to both b and s would yield an independent six-set.
    assert 4 + 2 == 6

    # Conditional on the registered row-transversal theorem, a non-hub-
    # complete witness hits all h full B rows. The incidence budget gives at
    # most three such witnesses; its own label also forces every full-label
    # witness to be hub-complete, so the floor is max(3,h-4).
    for h in range(6, 11):
        c_s_upper = 2 * h + 10
        assert c_s_upper < 4 * h
        hub_complete_floor = 6 - min(3, 10 - h)
        assert hub_complete_floor == max(3, h - 4)
    print("E407_FIVE_TEMPLATE_LABELLED_INCIDENCE_ARITHMETIC_OK")
    for template in "ABCDE":
        print(
            f"{template}: high-k no-S witnesses/color={results[template][0]}, "
            f"witnesses>= {results[template][1]}, "
            f"hub-hit incidences>= {results[template][2]}, "
            f"total shell-row hits>= {results[template][3]}"
        )
    print("A/C hub-complete floor (conditional on row-transversal theorem):", {h: max(3, h - 4) for h in range(6, 11)})
    print("Scope: arithmetic only; no graph-realization or template-exclusion certificate.")


if __name__ == "__main__":
    main()
