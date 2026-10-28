# E408 Q32 — v=45 source-correct two-point multiplicity

Date: 2026-10-28
Status: **m=8 CLOSED; m=10 CLOSED by the general zero-shell bound; m=9 forced to n_w=4 and a=4 at both W-points, still OPEN.**

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

Before the shell argument, the pointwise budget gives `n_w in {3,4}`. The source-correct zero-shell lemma below improves this to `n_w=4`. Consequently all four special incidences have surplus exactly1, so the parameter multiset is `(a_C)=(4,4,4,4)` at each W-point. No exceptional injectivity is needed.

Moreover, when the special surplus reaches4, all remaining pointwise slack is exhausted: the target degree is exactly13, the 130- and 131-edge colors have degrees exactly4 and3, and every non-special exact color has degree exactly4 at that W-point, hence lies there in an isolated K5 rather than the 11-point gadget.

## 5. m=10 normal form

Before the shell argument, the pointwise budget gives `n_w in {4,5}`. The source-correct zero-shell lemma instead forces `n_w>=6`, contradicting the budget `n_w<=5`. Therefore **m=10 is impossible for every non-full-support Q32 realization**, including v=45.

## 6. Two-point multi-outside placement without injectivity

For any exact color with `x_C` different from a fixed W-point w, w belongs to a multi-outside K5 and therefore uses at least two distinct shell neighbours of color C.

If an exact color has `x_C` outside W, then both w_1 and w_2 are non-special. Relative to H the exact Type-I placement has only the following multi-outside resources:

- `x in O`: one double-outside K5;
- `x in H`, two-double: two double-outside K5s;
- `x in H`, triple: one triple-outside K5.

Therefore, except for at most one color owning the edge `w_1w_2`, an exact color with `x_C outside W` must use the two-double type and place w_1,w_2 in its two different multi-outside K5s. This recovers the useful split-two-point conclusion of the old reduction **without** using exceptional injectivity.

## 7. Deletion-Turan shell inequality at either W-point

The following argument applies separately to `w_1` and `w_2` and does not depend on `|W|=1`.

For every non-target color C, deleting a fixed `w in H` leaves 46 vertices with independence number at most12. Therefore

`e_C(H-w)>=p_12(46)=66`.

Writing `e_C(H)=69+g_C` gives

> `d_C^H(w)<=3+g_C`.

For a special exact color with `x_C=w` and source parameter a_C, its residual degree is `9-a_C`, hence

`d_C(w,O)>=max(0,6-a_C-g_C)`.

Among all special colors at the same w, at most one can own the single edge wp. Consequently

> **`sum_{C:x_C=w} d_C(w,A) >= sum_{C:x_C=w} max(0,6-a_C-g_C)-1`.**

Every non-special exact color at w uses at least two distinct A-neighbours through its multi-outside K5. This is exactly the local input used in the v=46 gap calculation, so the same pointwise gap bounds apply here.

## 8. m=9: two disjoint special sets spend at least eight gap units

At each fixed `w_i`, the local alternatives are:

- n=3, `(4,4,4)`: special gap sum at least4;
- n=3, `(4,4,3)`: special gap sum at least5;
- n=4, `(4,4,4,4)`: special gap sum at least4.

The special-color sets at `w_1` and `w_2` are disjoint, because an exact Type-I color has only one special vertex x_C.

Therefore

> **`sum_{C exact} g_C >=8` in every surviving v=45,m=9 Case-II row.**

If either W-point has the `(4,4,3)` profile, the lower bound improves to9; if both do, to10.

This is a genuine global two-point consequence, not two copies charged to the same exact colors.

## 9. m=10: two disjoint special sets spend at least twelve gap units

At each fixed `w_i`, the local alternatives are:

- n=4, `(4,4,4,4)`: special gap sum at least6;
- n=4, `(4,4,4,3)`: special gap sum at least7;
- n=5, all a=4: special gap sum at least6.

Again the two special-color sets are disjoint. Hence

> **`sum_{C exact} g_C >=12` in every surviving v=45,m=10 Case-II row.**

Each occurrence of the `(4,4,4,3)` profile raises this by one, so the aggregate floor is13 or14 if one or both W-points have that profile.

## 10. Remaining v=45 frontier

- m=8: CLOSED;
- m=9: OPEN, but exact colors spend at least8 of the 37 global near-Turan gap units (9/10 in the enhanced rows);
- m=10: OPEN, but exact colors spend at least12 gap units (13/14 in the enhanced rows).

The next load-bearing step must combine these gap floors with the limited shell M-edge pool, exact Type-I placement types, and the global eleven-color edge partition. No exceptional-injectivity statement is used.

## 6. General zero-shell special-incidence bound

### Lemma 6.1 — at most one zero-shell special exact color

Fix `w in W`. If an exact color C has `x_C=w` and no C-colored edge from w to A, then `pw` has color C. Indeed, the source-correct Type-I gadget contains the C-colored K5 `{x_C} union (N_t\\{y})`; because `alpha(H)<=4`, one of the four vertices in `N_t\\{y}` lies outside H. None can be in A under the zero-shell hypothesis, so one is p. The edge `pw` has a unique color, so at most one special exact color at w has zero shell degree.

### Lemma 6.2 — universal lower bound on special multiplicity

Let `n_w` be the number of exact colors with `x_C=w`. The other `m-n_w` exact colors each consume at least two distinct w--A edges, disjoint across colors. Hence at most `13-2(m-n_w)` shell edges remain for the special exact colors. Since all but at most one of those `n_w` colors must use at least one shell edge,

`n_w-1 <= 13-2(m-n_w)`,

so

`n_w >= 2m-14`.

Combining with the pointwise budgets `n_w<=r_m` gives:

- m=8: `n_w>=2`; since every special incidence costs at least2 surplus units, this is the existing m=8 contradiction against budget3;
- m=9: `n_w>=4` and `n_w<=4`, so every W-point has exactly four special colors and all four have `a=4`;
- m=10: `n_w>=6` but `n_w<=5`, contradiction.

Thus m=10 is excluded whenever W is nonempty, not merely for v=45. The argument uses the corrected Type-I gadget and edge uniqueness only; it does not use the retracted degree-nine claim or exceptional injectivity.