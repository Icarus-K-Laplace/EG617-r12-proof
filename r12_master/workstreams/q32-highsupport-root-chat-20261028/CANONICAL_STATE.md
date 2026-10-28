# E408 Q32 high-support + root-audit canonical state

Updated: 2026-10-28
Branch: `workstream/r12-q32-highsupport-root-20261028`
Write scope: `r12_master/workstreams/q32-highsupport-root-chat-20261028/`

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED.**

Unique currently identified live root graph gate: **E408 / h13 / Qmax=32 / e(H)=285 / excess6**.

This workstream does not touch sibling-owned `Case II / v=44 / m=8,9`.

## Live Q32 contract

- `|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`;
- `sum_H(d_H-12)=6`;
- exact-color count `m in {8,9,10}`;
- source-correct exact Type-I factorization `10K5 dot-union G11`;
- no universal degree-nine exceptional vertex;
- every exact color has at least ten disjoint core K4 witnesses;
- witness union `U` has `|U|>=44`;
- for `W=H\U`, corrected multiplicity `n_w>=m-6`;
- latest nonexact pointwise floors:
  `L8=12`, `L9=7`, `L10=2`.

## Case I

- v=44 CLOSED;
- v=45 CLOSED;
- v=46,m=10 CLOSED;
- v=46,m=9 CLOSED;
- v=46,m=8 CLOSED by the 130-edge minimum-degree-four theorem;
- v=47 OPEN.

Hence Case I now has only v=47.

## Case II in this workstream

### v=45

- m=8: **CLOSED** by source-correct weighted special-incidence capacity;
- m=9: OPEN, with each W-point special profile `n in {3,4}` and high-a parameter normal form;
- m=10: OPEN, with each W-point `n in {4,5}` and high-a normal form.

### v=46

- m=8: **CLOSED** by the same three-unit surplus contradiction;
- m=9: OPEN, `n in {3,4}`;
- m=10: OPEN, `n in {4,5}`.

### v=47

Full support `U=H`, all m remain OPEN.

## v=47 proved reductions

For an exact color C let

`g_C=e_C(H)-69`.

Source-correct Type-I placement gives

`0<=g_C<=6`.

More precisely:

- `x in O`: outside-count profile `(2,1^11)`, eleven witnesses, `69<=e_C(H)<=73`;
- `x in H`, two-double: `(2,2,1^10)`, ten witnesses, `69<=e_C(H)<=74`;
- `x in H`, triple: `(3,1^11)`, eleven witnesses, `69<=e_C(H)<=75`.

All eleven non-target colors partition `bar H`, so

`sum_C g_C = 37`.

The 69-edge layer is genuinely source-feasible for a single exact color; therefore a false universal strict reserve `e_C(H)>=70` must not be used.

The 69/70 layers have the rigid `4^11,3` near-Turan normal form. At 70 edges there is exactly one cross-part color edge, so every monochromatic K4 still lies in one of the eleven four-parts.

For exact colors, with `mu_C=e_C(A)`, the valid tradeoff is

- x in H: `g_C<=mu_C+2`;
- x in O: `g_C<=mu_C+1`.

Every exact color pays at least two M-edges; x-in-H triple type pays at least three.

## m=8 source-correct rigidity

At every residual point z,

`(d_F(z)-13) + sum_non-target(d_C(z)-4) = 3`.

For every exact Type-I color this forces

`a in {2,3}`.

The two variable gadget surplus weights are therefore `{2,3}`. No residual point can be variable for two exact colors, so all sixteen points

`{x_C,y_C : C exact}`

are pairwise distinct.

This is the mechanism closing the v45/v46 Case-II m=8 rows.

## Root audit

Current source-safe chain:

- contextual R449: closed relative to named input;
- h12: closed;
- E397--E406: closed;
- E407 Q31: replay-backed conditional closure;
- E407 Q32: V12 coverage replay-backed, then closed by the later 29-point U-reserve theorem;
- E408 Q31: replay-backed conditional closure;
- E408 Q33: conditional global 31-point nonexact-U-reserve closure;
- E408 Q32: OPEN.

The old root promotion based on Q32 degree-nine/injectivity is withdrawn.

## Immediate mathematical frontier

1. v=47 multicolor near-Turan packing: combine the exact 37-unit gap ledger, exact Type-I placement normal forms, shell-edge ownership, and pointwise degree/excess-six constraints.
2. Case-II v=45,m=9,10: combine the two W-point high-a profiles with limited multi-outside K5 resources and shell-edge ownership.
3. Case-II v=46,m=9,10: combine the one W-point high-a profiles with the 13 shell-edge pool and core excess.

No root promotion before all of these plus sibling v44 are closed and replayed.
