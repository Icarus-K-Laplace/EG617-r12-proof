# E408 Q32 — v=46 Case-II source-correct closure work

Date: 2026-10-28
Status: **m=8 CLOSED; m=9 CLOSED by the direct no-core-only degree-four theorem; m=10 CLOSED by the general zero-shell bound.**

Let `W={w}` be the unique point of `H\U`. Case I at v=46 is already completely closed by the latest 130/131 minimum-degree theorems. This file addresses only the remaining Case-II branch.

## 1. Corrected multiplicity and pointwise budgets

The corrected multi-outside theorem gives

`n_w := # { exact C : x_C=w } >= m-6`.

The latest nonexact floors are

`L_8=12, L_9=7, L_10=3` (see `Q32_132_MINDEG3.md`).

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

## 3. m=9 normal form after the zero-shell bound

The pointwise budget initially gives `n_w in {3,4}`. Section 10 proves the stronger source-correct inequality `n_w >= 2m-14 = 4`, so `n_w=4` exactly. All four special incidences must use their minimum surplus1, hence every special Type-I parameter has `a=4`.

Thus the `n_w=3` rows `(4,4,4)` and `(4,4,3)` are excluded. The five non-special exact colors consume at least ten of the thirteen shell-A edges at w. At least three of the four special colors must use a shell-A edge. Therefore the target color cannot use any w--A edge: if it used one, only twelve non-target shell-A edges would remain for a demand of at least thirteen. Thus the target shell degree is zero and the core excess at w is exactly one. Equality is forced: each non-special exact color uses exactly two shell-A edges; three special colors use one each; one special color uses zero and owns pw; and both nonexact colors use no shell-A edge. All four special colors have exactly one neighbor in O and therefore core degree four; each spends at least one gap unit.

## 4. m=10 closure

The updated pointwise budget gives `n_w<=4`. Section 10 proves `n_w >= 2m-14+t_w >= 6`, a contradiction. Hence

> **Case II / v=46 / m=10 is CLOSED.**

The remaining m=10 core-gap rows in the historical Section 8 are superseded by this stronger contradiction and are not load-bearing.

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

Sections 10's zero-shell bound excludes n=3 entirely. Only n=4 with all four special parameters a=4 remains; its shell inequality forces at least four global core-gap units into these four special colors.

### 7.1 Historical n=3 row (superseded)

Here the special surplus is3, so `Q in {3,4}`, while the six non-special exact colors already consume12 A-edges.

- if `Q=3`, then `epsilon in {1,2}` and the three special gaps satisfy
  `sum g_C >= 6-epsilon`, hence at least4;
- if `Q=4`, then `epsilon in {0,1}` and
  `sum g_C >= 5-epsilon`, hence at least4.

Therefore

> **n=3, (4,4,4): the three special colors spend at least four core-gap units.**

### 7.2 Historical n=3 row (superseded)

The special surplus is4, so `Q=4` and `epsilon<=1`. The shell-A capacity inequality gives

`sum_special g_C >= 6-epsilon`.

Therefore

> **n=3, (4,4,3): the three special colors spend at least five core-gap units.**

### 7.3 n=4, profile (4,4,4,4)

Here `Q=4`, `epsilon<=1`, and the five non-special exact colors consume at least10 A-edges. The same inequality gives

`sum_special g_C >= 5-epsilon`.

Therefore

> **n=4: the four special colors spend at least four core-gap units.**

Thus the only surviving v=46,m=9 Case-II row has `epsilon=1`, target shell degree zero, exact shell-A usage `10+3=13`, both nonexact colors shell-A-free, and at least four of the global 37 near-Turan gap units forced into the four special exact colors. The zero-shell special color owns pw, so its H-degree is4 (not5); all four special colors have H-degree4. The old n=3 rows are superseded.

## 8. Historical m=10 core-gap rows (superseded by Section 10)

The following inequalities were derived for the n=4/n=5 normal forms before applying the general zero-shell bound. They are mathematically necessary for those profiles, but those profiles are now eliminated, so they are no longer load-bearing.

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

These were necessary bounds for the former m=10 profiles. Section 10 eliminates all those profiles, so no v=46,m=10 Case-II row survives.

## 9. Remaining v=46 status

- m=8: CLOSED in both Case I and Case II;
- m=9: Case I CLOSED; Case II OPEN only in the n=4, all-a4 row, spending at least four special core-gap units;
- m=10: CLOSED in both Case I and Case II.

No root promotion follows: the m=9 core-gap lower bound does not exhaust the global 37-unit gap ledger.


## 10. General zero-shell special-incidence bound

For any `w in W`, let `n_w = #{C : x_C=w}`, and let `t_w` be the number of target-colored edges from w to the 13-point shell A.

**Lemma 10.1.** At most one special exact color at w can have zero shell-A degree. If `N_C(w) intersect A = empty`, the source-correct Type-I gadget contains the C-colored K5 `{x_C} union (N_t minus {y})`. Since `alpha(H)<=4`, one of its four vertices other than w lies outside H. Under the zero-shell hypothesis it cannot lie in A, so it is p; hence edge `pw` has color C. The edge `pw` has a unique color.

Every non-special exact color at w consumes at least two distinct `w--A` edges. Thus the `m-n_w` non-special exact colors use at least `2(m-n_w)` shell edges. At least `n_w-1` special exact colors must have positive shell degree. Reserving target-colored shell edges gives

`n_w-1 <= 13-t_w-2(m-n_w)`,

hence

`n_w >= 2m-14+t_w`.

Combining with the pointwise budgets `n_w<=r_m`, `r_8=3`, `r_9=4`, `r_10=4`, gives:
- m=8: n_w>=2; every special incidence costs at least2 surplus units, contradicting budget3 (the existing closure);
- m=9: n_w=4 and all four special parameters are a=4; the refined inequality forces t_w=0, hence epsilon=1;
- m=10: n_w>=6>5, contradiction.

For m=9, t_w=0 plus the thirteen-edge shell count further forces each of the five non-special exact colors to use exactly two shell edges, three special exact colors to use one each, and the remaining special exact color to own pw. Both nonexact colors have no shell-A neighbors at w. The target degree is13 and d_H(w)=13, so epsilon=1.

This proof uses the source-correct Type-I factorization and shell edge uniqueness only; it does not use the retracted degree-nine claim or exceptional-vertex injectivity.


## 11. Superseding m=9 closure

The rigid m=9 normal form in Section 7 already forces the 130-edge nonexact color D to have degree four at w and no neighbor in A. The unique zero-shell special exact color owns pw, so D does not own pw either. Hence all four D-neighbors of w lie in H.

The later source-correct theorem `Q32_130_NO_CORE_ONLY_DEG4.md` rules out even one core-only degree-four vertex in a 130-edge color. Therefore the v=46, m=9 row is **CLOSED**. The quantified core-gap row above is a valid conditional description of a hypothetical row, but the row itself is impossible; it is no longer a live frontier.


## 12. Updated m=10 budget

The 132-edge minimum-degree theorem `Q32_132_MINDEG3.md` upgrades the m=10 nonexact floor from2 to3. Accordingly the pointwise surplus budget is now `r_10=4`, not5. This only strengthens the existing zero-shell contradiction `n_w>=6>4`; no m=10 closure depends on the older weaker value.
