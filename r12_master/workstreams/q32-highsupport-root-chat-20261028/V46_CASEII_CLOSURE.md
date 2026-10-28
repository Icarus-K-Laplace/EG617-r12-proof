# E408 Q32 — v=46 Case-II source-correct closure work

Date: 2026-10-28
Status: **m=8 CLOSED; m=10 CLOSED by the general zero-shell bound; m=9 forced to n_w=4 and all a=4, with a quantified core-gap row still OPEN.**

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

## 3. m=9 normal form after the zero-shell bound

The pointwise budget initially gives (n_w\in\{3,4\}). Section 10 proves the stronger source-correct inequality (n_w\ge2m-14=4), so (n_w=4) exactly. All four special incidences must use their minimum surplus1, hence every special Type-I parameter is (a=4).

Thus the (n_w=3) rows ((4,4,4)) and ((4,4,3)) are excluded. The five non-special exact colors consume at least ten of the thirteen shell edges at w. At most three remain for the four special colors, so at least one special color is zero-shell; the zero-shell lemma permits at most one, hence this count is tight rather than contradictory. The remaining n=4 row still forces at least four global near-Turan gap units into the four special colors (Section 7.3).

## 4. m=10 closure

The pointwise budget initially gives (n_w\in\{4,5\}). Section 10 proves (n_w\ge2m-14=6), a contradiction. Hence

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

Thus every surviving v=46,m=9 Case-II row forces at least four of the global 37 near-Turan gap units into the exact colors special at the unique W-point; the `(4,4,3)` row forces at least five.

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

Thus every surviving v=46,m=10 Case-II row forces at least six core-gap units into the special exact colors; the `(4,4,4,3)` row forces at least seven.

## 9. Remaining v=46 status

- m=8: CLOSED in both Case I and Case II;
- m=9: Case I CLOSED; Case II OPEN only in the n=4, all-a4 row, spending at least four special core-gap units;
- m=10: CLOSED in both Case I and Case II.

No root promotion follows: the m=9 core-gap lower bound does not exhaust the global 37-unit gap ledger.


## 10. General zero-shell special-incidence bound

For any (w\in W), let (n_w=\#\{C:x_C=w\}).

**Lemma 10.1.** At most one special exact color at w can have zero shell-A degree. If (N_C(w)\cap A=\varnothing), the source-correct Type-I gadget contains the C-colored K5 ({x_C\}\cup(N_t\setminus\{y\})). Since (alpha(H)\le4), one of its four vertices other than w lies outside H. Under the zero-shell hypothesis it cannot lie in A, so it is p; hence pw has color C. Edge pw has a unique color.

Every non-special exact color at w consumes at least two distinct w--A edges. Thus the (m-n_w) non-special exact colors use at least (2(m-n_w)) of the thirteen shell edges. At least (n_w-1) special exact colors must have positive shell degree, so

`n_w-1 <= 13-2(m-n_w)`,
hence
`n_w >= 2m-14`.

Combining this with the pointwise budgets (n_w\le r_m), (r_8=3,r_9=4,r_{10}=5), gives:
- m=8: n_w>=2, and every special incidence costs at least2 surplus units, contradicting budget3 (the existing closure);
- m=9: n_w=4 and all four special parameters are a=4;
- m=10: n_w>=6>5, contradiction.

This proof uses the source-correct Type-I factorization and shell edge uniqueness only; it does not use the retracted degree-nine claim or exceptional-vertex injectivity.
