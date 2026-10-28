# E408 Q32 — v=45 source-correct two-point multiplicity

Date: 2026-10-28  
Status: **m=8 CLOSED; m=10 CLOSED; m=9 forced to a rigid shell-ownership profile, still OPEN.**

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

Thus `sum_{C:x_C=w}(5-a_C) <= r_m`, and in particular (n_w\le r_m).

## 2. Zero-shell lemma and the target-shell correction

Fix (w\in W). If an exact color C has (x_C=w) and no C-colored edge from w to A, then (pw) has color C. The source-correct Type-I gadget contains the C-colored K5 `{x_C} union (N_t minus {y})`. Since `alpha(H)<=4`, at least one of the four vertices in (N_t\setminus\{y\}) lies outside H. Under the zero-shell hypothesis it cannot lie in A, so it must be p. Thus pw is C-colored. Since pw has a unique color, at most one special exact color at a fixed w can have zero shell-A degree.

Let (t_w) be the number of target-colored edges from w to A. The (m-n_w) non-special exact colors each use at least two distinct w--A edges. At least (n_w-1) special exact colors must use at least one shell edge. Therefore
`n_w-1 <= 13-t_w-2(m-n_w)`,
so
`n_w >= 2m-14+t_w`. `(2.1)`

This is stronger than the shell-only bound because it reserves target-colored shell edges explicitly.

## 3. m=8 and m=10 closures for every non-full support

For m=8, the three-unit pointwise budget forces every exact Type-I parameter to (a\in\{2,3\}), so each special incidence costs at least two surplus units. Since (n_w\ge m-6=2), at least four units are needed against budget3. Thus m=8 is impossible whenever W is nonempty.

For m=10, (2.1) gives (n_w\ge6+t_w\ge6), while the pointwise budget gives (n_w\le5). Thus m=10 is impossible whenever W is nonempty, including v=45 and v=46.

## 4. m=9 rigid shell-ownership normal form

For m=9, the pointwise budget first gives (n_w\le4), while (2.1) gives (n_w\ge4+t_w). Hence
- (n_w=4);
- (t_w=0): no target-colored edge from w to A;
- the target degree at w is exactly13, so (d_H(w)=13) and the core excess (epsilon_w=d_H(w)-12=1);
- all four special exact colors at w have surplus1, hence parameter (a=4).

There are five non-special exact colors, each using at least two w--A edges. The four special colors have at most three shell edges left, but at most one special color can be zero-shell. Therefore equality is forced throughout:
- each of the five non-special exact colors uses exactly two shell edges at w;
- exactly three special exact colors use one shell edge each;
- exactly one special exact color has zero shell degree and owns pw;
- the target color and both nonexact colors use zero shell edges at w.

The pointwise degree ledger also gives full residual degrees 4 and 3 for the 130- and 131-edge nonexact colors. Because they have zero shell degree, all their neighbors at w lie in H.

## 5. Gap consequences and W-edge ownership

For a special exact color with `a=4`, full residual degree at w is5. Each of the three positive-shell special colors has exactly one A-neighbor and does not own pw; the unique zero-shell special color owns pw. Thus **every one of the four special colors has exactly one neighbor in O={p} union A**, and hence `d_C^H(w)=4`. The deletion-Turán inequality `d_C^H(w)<=3+g_C`, where `g_C=e_C(H)-69`, gives `g_C>=1` for each of the four colors.

So each W-point forces at least four gap units into its four special exact colors. The special-color sets at `w_1,w_2` are disjoint, because each exact color has only one special point. Therefore
`sum_{C exact} g_C >= 8`.
This is a genuine global two-point bound, not two charges to the same exact colors.

At both W-points the 130-edge color has degree4 and all its neighbors in H. The source-correct 130-color W-pair rigidity lemma therefore forces (w_1w_2) to have that 130-edge color. In particular,
`e_H(W)=0`.
Since each W-point carries one core-excess unit, (E_W=2) and (E_U=4). The exact core identity gives
`e(bar(H[U])) = 735 - E_U - e_H(W) = 731`.

These are necessary conditions, not yet a contradiction against the 285-edge core.

## 6. Two-point multi-outside placement without injectivity

For any exact color with (x_C\notin W), both (w_1,w_2) are non-special and each lies in a multi-outside K5. Relative to H, the source-correct Type-I placement has:
- (x_C\in O): one double-outside K5;
- (x_C\in H), two-double type: two double-outside K5s;
- (x_C\in H), triple type: one triple-outside K5.

Except for at most one color owning (w_1w_2), an exact color with (x_C\notin W) must use the two-double type and place the two W-points in its two different multi-outside K5s. This recovers the useful split-two-point conclusion without exceptional injectivity.

## 7. Remaining v=45 frontier

- m=8: **CLOSED**;
- m=10: **CLOSED**;
- m=9: **OPEN**, with (n_{w_i}=4), all special parameters (a=4), no target shell edges at either W-point, exact shell usage (10+3=13), at least8 total exact-color gap units in the eight disjoint special colors, (e_H(W)=0), and (e(\overline{H[U]})=731).

The next step must combine this rigid two-point shell profile with the M-edge pool, exact Type-I placement types, and the full eleven-color edge partition.

No retracted degree-nine assertion or exceptional-injectivity statement is used.
