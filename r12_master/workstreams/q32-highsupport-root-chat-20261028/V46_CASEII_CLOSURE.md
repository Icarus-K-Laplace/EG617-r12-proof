# E408 Q32 — v=46 Case-II source-correct closure work

Date: 2026-10-28
Status: **m=8 CLOSED; m=9,10 reduced to quantified core-gap rows and OPEN.**

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

Each of these k colors places w in a multi-outside K5 and therefore owns at least two distinct shell-A edges from w. Edge-color uniqueness makes the selected shell neighbours disjoint across the k colors. Thus they use at least `2k` of the thirteen A-edges at w.

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

## 6. Deletion-Turan inequality for a special point

For every non-target color C on H, deleting w leaves a 46-vertex graph with independence number at most12. Hence

`e_C(H-w)>=p_12(46)=66`.

Write

`e_C(H)=69+g_C`, `g_C>=0`.

Then

> **`d_C^H(w)<=3+g_C`.**

If `x_C=w` and the Type-I source parameter is a_C, then its residual degree is `9-a_C`. Therefore the number of C-edges from w to the fourteen outside-core points `O={p} union A` is at least

`max(0,6-a_C-g_C)`.

Only one color can own the single edge wp. Thus, for a set S of special exact colors at w,

> **`sum_{C in S} d_C(w,A) >= sum_{C in S} max(0,6-a_C-g_C)-1`.**

This is the key source-correct coupling between the high-a special profiles and the core-gap variables.

## 7. Quantified core-gap spending for m=9

Let `epsilon=d_H(w)-12` be the target-core excess at w. Let Q be the total pointwise surplus above

`target13 + 9*exact4 + nonexact floors7`.

Then

`d_F(w)=17-Q`,

and the target degree from w into A is

`d_F(w,A)=d_F(w)-(12+epsilon)=5-Q-epsilon`.

Hence the total non-target A-edge capacity at w is

> `8+Q+epsilon`,

with `epsilon<=5-Q`.

### 7.1 n=3, profile (4,4,4)

Here the special surplus is3, so `Q in {3,4}`, while the six non-special exact colors already consume12 A-edges.

- if `Q=3`, then `epsilon in {1,2}` and the three special gaps satisfy
  `sum g_C >= 6-epsilon`, hence at least4;
- if `Q=4`, then `epsilon in {0,1}` and
  `sum g_C >= 5-epsilon`, hence at least4.

Therefore

> **n=3, (4,4,4): the three special colors spend at least four core-gap units.**

### 7.2 n=3, profile (4,4,3)

The special surplus is4, so `Q=4` and `epsilon<=1`. The shell-A capacity inequality gives

`sum_special g_C >= 6-epsilon`.

Therefore

> **n=3, (4,4,3): the three special colors spend at least five core-gap units.**

### 7.3 n=4, profile (4,4,4,4)

Here `Q=4`, `epsilon<=1`, and the five non-special exact colors consume at least10 A-edges. The same inequality gives

`sum_special g_C >= 5-epsilon`.

Therefore

> **n=4: the four special colors spend at least four core-gap units.**

Thus every surviving v=46,m=9 Case-II row forces at least four of the global 37 near-Turan gap units into the exact colors special at the unique W-point; the `(4,4,3)` row forces at least five.

## 8. Quantified core-gap spending for m=10

Now write Q for surplus above

`target13 + 10*exact4 + nonexact floor2`.

Then

`d_F(w)=18-Q`,

so

`d_F(w,A)=6-Q-epsilon`

and the total non-target A-edge capacity is

> `7+Q+epsilon`,

with `epsilon<=6-Q`.

### 8.1 n=4, profile (4,4,4,3)

Here `Q=5`, `epsilon<=1`, and the six non-special colors already consume12 A-edges. The special shell inequality gives

`sum_special g_C >= 8-epsilon`.

Therefore

> **(4,4,4,3): the four special colors spend at least seven core-gap units.**

### 8.2 n=4, profile (4,4,4,4)

If `Q=4`, then `epsilon in {1,2}` and

`sum_special g_C >= 8-epsilon`,

so at least6.

If `Q=5`, then `epsilon in {0,1}` and

`sum_special g_C >= 7-epsilon`,

again at least6.

Therefore

> **n=4, all-a4: at least six special core-gap units.**

### 8.3 n=5, all a=4

Here `Q=5`, `epsilon<=1`; the five non-special exact colors consume at least10 A-edges. The shell inequality gives

`sum_special g_C >= 7-epsilon`,

hence

> **n=5: the five special colors spend at least six core-gap units.**

Thus every surviving v=46,m=10 Case-II row forces at least six core-gap units into the special exact colors; the `(4,4,4,3)` row forces at least seven.

## 9. Remaining v=46 status

- m=8: CLOSED in both Case I and Case II;
- m=9: Case I CLOSED, Case II OPEN but now spends >=4 special core-gap units (>=5 in the 443 row);
- m=10: Case I CLOSED, Case II OPEN but now spends >=6 special core-gap units (>=7 in the 4443 row).

These are source-correct necessary conditions. They do not yet exhaust the global 37-unit gap ledger, so no root promotion follows.
