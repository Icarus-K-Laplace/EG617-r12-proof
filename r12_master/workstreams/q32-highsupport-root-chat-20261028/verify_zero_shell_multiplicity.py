#!/usr/bin/env python3
"""Arithmetic-only verifier for the source-correct zero-shell multiplicity bound.

This checks the algebraic implications of
    n_w >= 2*m - 14
and the pointwise special-surplus budgets r_8=3, r_9=4, r_10=5.
It does not verify the graph-theoretic zero-shell lemma itself.
"""

BUDGET = {8: 3, 9: 4, 10: 5}
MIN_SPECIAL_SURPLUS = {8: 2, 9: 1, 10: 1}

for m in (8, 9, 10):
    lower = 2 * m - 14
    upper = BUDGET[m]
    assert lower == {8: 2, 9: 4, 10: 6}[m]
    assert lower <= upper if m == 9 else True

    if m == 8:
        # Every exact Type-I parameter is a in {2,3}, so each special
        # incidence costs at least 2 against a total budget of 3.
        assert lower >= 2
        assert lower * MIN_SPECIAL_SURPLUS[m] > upper
        print("m=8: n_w>=2; special cost >=4 > budget 3 -> CLOSED")
    elif m == 9:
        assert lower == upper == 4
        # Four positive integer surpluses fit budget 4 only if all equal 1.
        assert 4 * MIN_SPECIAL_SURPLUS[m] == upper
        print("m=9: n_w=4; four special surpluses all equal 1 -> a=4")
    else:
        assert lower > upper
        print("m=10: n_w>=6 > budget 5 -> CLOSED for every nonempty W")

print("ZERO_SHELL_MULTIPLICITY_ARITHMETIC_OK")
print("Scope: arithmetic only; graph lemma and upstream contracts remain proof dependencies.")
