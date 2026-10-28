# E408 Q32 — v=45 source-correct two-point multiplicity

Date: 2026-10-28
Status: **m=8 CLOSED; m=9,10 reduced.**

This replaces every use of the retracted exceptional-vertex injectivity in the old `Q32_V45_TWOPOINT_REDUCTION.md`.

## 1. Contract

Assume `|U|=45` and put

`W={w_1,w_2}`.

For `w in W`, let

`n_w = # { exact colors C : x_C=w }`.

The corrected multi-outside theorem gives

`n_w>=m-6`.

Use the latest nonexact pointwise floors

`L_8=12, L_9=7, L_10=2`.

For an exact Type-I color with source parameter `a`, the special point x has degree

`d_C(x)=9-a=4+(5-a)`.

## 2. Full pointwise surplus budgets

At every residual point z, after reserving target degree13, exact baseline degree4 in each exact color, and the nonexact floors, the total remaining degree budget is

- m=8: `60-(13+32+12)=3`;
- m=9: `60-(13+36+7)=4`;
- m=10: `60-(13+40+2)=5`.

Hence at a W-point the total special-x surplus satisfies

`sum_{C:x_C=w}(5-a_C) <= r_m`,

where

`r_8=3, r_9=4, r_10=5`.

This bound needs no injectivity assumption.

## 3. m=8 is impossible whenever W is nonempty

For m=8, the same three-unit budget applies at every residual point to **all** exact gadget degrees. In a Type-I color the variable surpluses are

- y: `a`;
- x: `5-a`.

If `a=1`, x alone has surplus4, impossible. If `a=4`, y alone has surplus4, impossible. Therefore every exact color has

> `a in {2,3}`.

In particular every special-x incidence costs at least

`5-a >=2`.

But the corrected non-full-support theorem gives at each `w in W`

`n_w>=m-6=2`.

Two special incidences would cost at least4 surplus units at w, while only3 are available. Contradiction.

Therefore

> **Case II / v=45 / m=8 is CLOSED.**

The proof actually excludes any non-full-support m=8 realization; this workstream only records the v=45/v=46 consequences assigned to it and does not reopen the sibling v=44 analysis.

## 4. m=9 normal form

Here `n_w>=3` and the special surplus budget is4. Hence

> `n_w in {3,4}`.

If `n_w=4`, all four incidences must have surplus1, hence

> parameter multiset `(a_C)=(4,4,4,4)`.

If `n_w=3`, the only possibilities are

> `(4,4,4)` or `(4,4,3)`.

Thus each of the two W-points has one of these two source-correct parameter profiles. No exceptional injectivity is needed.

Moreover, when the special surplus reaches4, all remaining pointwise slack is exhausted: the target degree is exactly13, the 130- and 131-edge colors have degrees exactly4 and3, and every non-special exact color has degree exactly4 at that W-point, hence lies there in an isolated K5 rather than the 11-point gadget.

## 5. m=10 normal form

Here `n_w>=4` and the budget is5. Hence

> `n_w in {4,5}`.

If `n_w=5`, all parameters are4.

If `n_w=4`, the parameter multiset is one of

> `(4,4,4,4)` or `(4,4,4,3)`.

Again, the profile with total special surplus5 exhausts all pointwise slack: target degree13, the 132-edge color at its degree-two floor, and every non-special exact color degree4 at w.

## 6. Two-point multi-outside placement without injectivity

For any exact color with `x_C` different from a fixed W-point w, w belongs to a multi-outside K5 and therefore uses at least two distinct shell neighbours of color C.

If an exact color has `x_C` outside W, then both w_1 and w_2 are non-special. Relative to H the exact Type-I placement has only the following multi-outside resources:

- `x in O`: one double-outside K5;
- `x in H`, two-double: two double-outside K5s;
- `x in H`, triple: one triple-outside K5.

Therefore, except for at most one color owning the edge `w_1w_2`, an exact color with `x_C outside W` must use the two-double type and place w_1,w_2 in its two different multi-outside K5s. This recovers the useful split-two-point conclusion of the old reduction **without** using exceptional injectivity.

## 7. Remaining v=45 frontier

- m=8: CLOSED;
- m=9: OPEN under the `n_w in {3,4}` / high-a profiles above;
- m=10: OPEN under the `n_w in {4,5}` / high-a profiles above.

The next step is to combine these profiles with the 13 shell-edge ownership ledger and the seven-block duplicate system.
