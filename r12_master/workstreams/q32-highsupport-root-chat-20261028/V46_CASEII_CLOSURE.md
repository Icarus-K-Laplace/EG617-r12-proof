# E408 Q32 — v=46 Case-II source-correct closure work

Date: 2026-10-28
Status: **m=8 CLOSED; m=9,10 rigidified and OPEN.**

Let `W={w}` be the unique point of `H\U`. Case I at v=46 is already completely closed by the latest 130/131 minimum-degree theorems. This file addresses only the remaining Case-II branch.

## 1. Corrected multiplicity and pointwise budgets

The corrected multi-outside theorem gives

`n_w := # { exact C : x_C=w } >= m-6`.

The latest nonexact floors are

`L_8=12, L_9=7, L_10=2`.

After reserving target degree13 and exact baseline degree4, the pointwise surplus budgets are

- m=8: 3;
- m=9: 4;
- m=10: 5.

For a special incidence `x_C=w`, the exact-color surplus above degree4 is `5-a_C`.

## 2. m=8 closure

The global m=8 surplus ledger forces every exact KP parameter to satisfy

`a_C in {2,3}`.

Thus every special incidence costs at least two surplus units. But the corrected multiplicity theorem gives

`n_w>=2`.

Hence the special incidences at w cost at least four units, exceeding the available pointwise surplus three. Contradiction.

Therefore

> **Case II / v=46 / m=8 is CLOSED.**

Together with the already proved Case-I exclusion, v=46,m=8 is completely eliminated.

## 3. m=9 normal form

Now `n_w>=3` while the special surplus budget is4. Therefore

> `n_w in {3,4}`.

If `n_w=4`, then all four special parameters are `a=4`.

If `n_w=3`, the sorted parameter profile is exactly one of

> `(4,4,4)`, `(4,4,3)`.

Let `k=m-n_w` be the number of non-special exact colors at w. Then

- if `n_w=3`, `k=6`;
- if `n_w=4`, `k=5`.

Each of these k colors places w in a multi-outside K5 and therefore owns at least two distinct shell edges from w. Edge-color uniqueness makes the selected shell neighbours disjoint across the k colors. Thus they use at least `2k` of the thirteen shell edges at w.

If the special-x surplus equals4 (the profile `(4,4,3)` or the four-special profile), all pointwise degree slack is exhausted. Then

- target degree at w is exactly13;
- the 130-edge nonexact color has degree exactly4 at w;
- the 131-edge nonexact color has degree exactly3 at w;
- every non-special exact color has degree exactly4 at w, hence w lies in one of that color's ten isolated K5 components.

For `n_w=3`, this gives six isolated multi-outside K5s through w using at least twelve shell neighbours.

## 4. m=10 normal form

Here `n_w>=4` and the special surplus budget is5. Therefore

> `n_w in {4,5}`.

If `n_w=5`, all five parameters are4.

If `n_w=4`, the sorted profile is exactly one of

> `(4,4,4,4)`, `(4,4,4,3)`.

Again put `k=10-n_w`, so `k=6` or5. The k non-special colors consume at least `2k` distinct shell neighbours at w.

Whenever the special surplus totals5 (five a=4 colors, or the four-special `(4,4,4,3)` profile), all pointwise slack is exhausted. Consequently

- target degree at w is exactly13;
- the unique 132-edge color has degree exactly2 at w;
- every non-special exact color has degree exactly4 at w and hence places w in an isolated multi-outside K5.

The source-correct 132-edge low-degree lemma then places w in an isolated triangle of that nonexact color whenever degree2 is attained.

## 5. Matching consequence valid in Case II

For every non-special exact color at w choose two shell neighbours from the multi-outside K5 containing w. Those two shell points are joined by an edge of that same exact color. Across different exact colors the chosen shell-neighbour pairs are vertex-disjoint, because the edges from w to the shell have unique colors.

Hence, without using Case I,

> **`nu(M) >= m-n_w`.**

In the rigid `n_w=m-6` rows this gives a six-edge matching in M covering twelve of the thirteen shell vertices.

Case I used `nu(M)<=3` to contradict this. Case II has no such upper bound, so the matching statement is retained only as a structural input, not a closure certificate.

## 6. Remaining v=46 status

- m=8: CLOSED in both Case I and Case II;
- m=9: Case I CLOSED, Case II OPEN under the profiles above;
- m=10: Case I CLOSED, Case II OPEN under the profiles above.

No root promotion follows until the remaining m=9,10 Case-II rows and v=47 are eliminated.
