#!/usr/bin/env python3
"""Arithmetic-only verifier for the source-correct zero-shell bound.

Checks n_w >= 2*m - 14 + t_w, pointwise special-surplus budgets, and the
m=9 shell-ownership saturation. It does not verify the graph-theoretic
zero-shell lemma or any upstream terminal contract.
"""

BUDGET = {8: 3, 9: 4, 10: 5}
MIN_SPECIAL_SURPLUS = {8: 2, 9: 1, 10: 1}

for m in (8, 9, 10):
    for t_w in (0, 1):
        lower = 2 * m - 14 + t_w
        upper = BUDGET[m]
        if m == 8:
            assert lower >= 2
            assert lower * MIN_SPECIAL_SURPLUS[m] > upper
        elif m == 9:
            assert lower <= upper if t_w == 0 else lower > upper
        else:
            assert lower > upper
    print(
        f"m={m}: base multiplicity lower bound={2*m-14}, "
        f"pointwise budget={BUDGET[m]}"
    )

# In m=9, n_w=4 is forced. If t_w=1, the five non-special exact colors
# need 10 shell-A edges, three special colors need at least 3, and the
# target needs 1: total 14 > the 13 shell-A edges. Thus t_w=0.
m, n_w = 9, 4
assert n_w - 1 == 3
non_special_shell_min = 2 * (m - n_w)
special_shell_min = n_w - 1
assert non_special_shell_min == 10
assert special_shell_min == 3
assert non_special_shell_min + special_shell_min == 13
assert non_special_shell_min + special_shell_min + 1 > 13
print("m=9: target shell degree=0; shell ownership is exactly 10 + 3 = 13")
print("m=9: five non-special exact colors use 2 shell edges each; special shell degrees are (0,1,1,1)")
print("ZERO_SHELL_MULTIPLICITY_ARITHMETIC_OK")
print("Scope: arithmetic only; graph lemma and upstream contracts remain proof dependencies.")
