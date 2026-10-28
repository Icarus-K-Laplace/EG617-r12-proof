# E408 Q32 — v=45 source-correct two-point multiplicity

Date: 2026-10-28  
Status: **m=8 CLOSED; m=10 CLOSED; m=9 forced to n_w=4 and a=4 at both W-points, with a quantified gap row still OPEN.**

This replaces every use of the retracted exceptional-vertex injectivity in the old `Q32_V45_TWOPOINT_REDUCTION.md`.

## 1. Contract and pointwise budgets

Assume `|U|=45`, so (W=H\setminus U=\{w_1,w_2\}). For (w\in W), define
`n_w = #{ exact colors C : x_C=w }`.

The corrected multi-outside theorem gives (n_w\ge m-6). The current nonexact pointwise floors are
`L_8=12, L_9=7, L_10=2`.

For a source-correct exact Type-I color with parameter (a\in\{1,2,3,4\}), the special point has degree (d_C(x_C)=9-a=4+(5-a)). Reserving target degree13 and the exact/nonexact floors gives special-surplus budgets:
- m=8: (r_8=3);
- m=9: (r_9=4);
- m=10: (r_{10}=5).

Thus
`sum_{C:x_C=w}(5-a_C) <= r_m`,
so in particular (n_w\le r_m).

## 2. Source-correct zero-shell lemma

Fix (w\in W). If an exact color (C) has (x_C=w) and no C-colored edge from (w) to shell (A), then (pw) has color C.

Indeed, the source-correct Type-I gadget contains the C-colored K5 `{x_C} union (N_t minus {y})`. Since `alpha(H)<=4`, at least one of the four vertices in (N_t\setminus\{y\}) lies outside H. Under the zero-shell hypothesis it cannot lie in A, so it must be p. Hence (pw) is C-colored. Since (pw) has a unique color, at most one special exact color at a fixed (w) can have zero shell-A degree.

This uses the correct Type-I factorization only; it uses no degree-nine assertion and no exceptional-vertex injectivity.

## 3. Universal shell-multiplicity inequality

Let (n_w) exact colors have special point (w). The other (m-n_w) exact colors are non-special at (w). Each such color places (w) in a multi-outside K5 and therefore uses at least two distinct (wA) edges. These edge sets are disjoint across colors.

Consequently at most (13-2(m-n_w)) shell edges remain for the special colors. All but at most one of the (n_w) special colors must have positive shell degree, so
`n_w-1 <= 13-2(m-n_w)`,
and hence
`n_w >= 2m-14`.

Combining this with the pointwise budgets gives:
- m=8: (n_w\ge2); but each special incidence costs at least two surplus units because every exact parameter has (a\in\{2,3\}), exceeding budget3. Thus m=8 is impossible whenever W is nonempty.
- m=9: (n_w\ge4) and (n_w\le4), so (n_w=4) at each W-point. All four special incidences have surplus1, forcing (a=4) for every special color at that point.
- m=10: (n_w\ge6) but (n_w\le5), contradiction. Thus m=10 is impossible for every non-full-support realization, including v=45 and v=46.

## 4. The surviving m=9 two-point normal form

At each (w_i\in W):
- exactly four exact colors have (x_C=w_i);
- all four have Type-I parameter (a=4);
- the five non-special exact colors use at least ten of the thirteen shell edges incident with (w_i);
- at least one of the four special colors has zero shell degree, and at most one can have zero shell degree. This is tight, not itself a contradiction.

The two sets of four special colors at (w_1,w_2) are disjoint, because an exact color has only one special vertex. Hence exactly eight of the nine exact colors have their special point in W; one exact color has its special point outside W.

Whenever the four special incidences exhaust their budget, the pointwise ledger also forces target degree13, the 130-edge color degree4, the 131-edge color degree3, and degree4 for every non-special exact color at that W-point.

## 5. Two-point multi-outside placement without injectivity

For any exact color with (x_C\) different from a fixed W-point (w), (w) lies in a multi-outside K5 and has at least two distinct shell neighbors of that color.

If (x_C\notin W), both (w_1,w_2) are non-special. Relative to H, the source-correct Type-I placement has:
- (x_C\in O): one double-outside K5;
- (x_C\in H), two-double type: two double-outside K5s;
- (x_C\in H), triple type: one triple-outside K5.

Except for at most one color owning the edge (w_1w_2), an exact color with (x_C\notin W) must use the two-double type and place (w_1,w_2) in its two different multi-outside K5s. This recovers the useful split-two-point conclusion without exceptional injectivity.

## 6. Deletion-Turán shell inequality at either W-point

Deleting any (w\in H) leaves a 46-vertex graph with independence number at most12, so for each non-target color C,
`e_C(H-w)>=p_12(46)=66`.
Writing (e_C(H)=69+g_C) gives
`d_C^H(w)<=3+g_C`.

For a special exact color with (x_C=w), its residual degree is (9-a_C), hence
`d_C(w,O)>=max(0,6-a_C-g_C)`.
Only one color can own (wp). Therefore
`sum_{C:x_C=w} d_C(w,A) >= sum_{C:x_C=w} max(0,6-a_C-g_C)-1`.

For the surviving m=9 normal form, (a_C=4) for four special colors, so
`sum_special d_C(w,A) >= sum_special max(0,2-g_C)-1`.

The five non-special exact colors consume at least ten shell edges. At most three remain for the four special colors. Combining the inequalities gives
`sum_special max(0,2-g_C) <= 4`,
and thus
`sum_{C:x_C=w} g_C >= 4`.
If the target-core excess at w is zero, the sharper bound is at least5.

Since the two W-points have disjoint special-color sets, every surviving v=45,m=9 row satisfies
`sum_{C exact} g_C >= 8`,
improving to9 or10 if one or both W-points have zero target-core excess.

## 7. Remaining v=45 frontier

- m=8: **CLOSED**;
- m=10: **CLOSED** by the universal zero-shell bound;
- m=9: **OPEN**, with four special colors at each W-point, all (a=4), and at least eight of the 37 global near-Turán gap units forced into the eight distinct special exact colors.

The remaining m=9 gap floor does not exhaust the global 37-unit ledger. The next step must combine it with the M-edge pool, exact Type-I placement types, and the full eleven-color edge partition.

No exceptional-injectivity statement is used.
