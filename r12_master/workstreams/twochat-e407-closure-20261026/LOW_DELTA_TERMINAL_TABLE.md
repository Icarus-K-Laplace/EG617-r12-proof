# E407 Q32 — low-delta terminal table

Date: 2026-10-27  
Status: **Current audited frontier. Delta=13 four-partite-U is now fully excluded; E407 Q32 remains OPEN.**

Let
\[
L_U=\overline{H[U]},\quad \delta=e(L_U)-294,\quad
\epsilon_U=\sum_{u\in U}(d_H(u)-12).
\]
The exact ledger is
\[
e(H[U])=112-\delta,\qquad
e(H[W])=48-\epsilon_U-\delta,\qquad
e_H(U,W)=124+\epsilon_U+2\delta.
\]
Retained inequalities:
\[
3\le\delta\le16,\quad0\le\epsilon_U\le4,\quad
\delta+\epsilon_U\le16,\quad\epsilon_U+2\delta\ge9.
\]
Every feasible profile has alpha(H[W])=4.

## Exact feasible epsilon_U values

| delta | epsilon_U |
|---:|---|
| 3 | 3,4 |
| 4 | 1,2,3,4 |
| 5-12 | 0,1,2,3,4 |
| 13 | 0,1,2,3 |
| 14 | 0,1,2 |
| 15 | 0,1 |
| 16 | 0 |

There are 56 integer profiles.

## Current mathematical status

| Branch | Status | Dependency / remaining issue |
|---|---|---|
| delta=16 | EXCLUDED | endpoint/kernel analysis and forbidden K12 |
| delta=15, four-partite | EXCLUDED | W-profile saturation / endpoint argument |
| delta=15, non-four-partite | EXCLUDED UNDER REGISTERED KP CONTRACT | second-Turan equality reduction |
| delta=14, four-partite, eps=0,1,2 | EXCLUDED | exact profile closures |
| delta=14, non-four-partite, augmentable | EXCLUDED UNDER REGISTERED EXTREMAL CONTRACT | augmentable-edge reduction |
| delta=14, non-four-partite, K5-saturated | PROVED_CONDITIONAL | Didin 2026 dependency not independently discharged |
| delta=13, four-partite, eps=0 | **EXCLUDED** | new KP five-kernel reduction + low-U-degree label-capacity contradiction |
| delta=13, four-partite, eps=1 | EXCLUDED | registered no-cross/cross profile closures |
| delta=13, four-partite, eps=2 | EXCLUDED under stated profile contract | registered closures |
| delta=13, four-partite, eps=3 | EXCLUDED | registered exact profile closure |
| delta=13, non-four-partite | OPEN | no complete classification at e(L_U)=307 |
| delta<=12 | OPEN | no legal extrapolation from delta=13 |

## New delta=13 eps=0 closure interface

At delta=13, eps=0, and L_U four-partite, U has parts 7,7,7,8 and exactly eight D-to-small H[U] cross edges. The W complement J has 118 edges and is K5-free. A four-partite J would imply a four-clique H[W] decomposition with 35 edges, which has no integer part-size solution. Thus J is a Brouwer equality graph, and Kang-Pikhurko reduces it to five kernels:

- (3,4,5,5;a=1,2);
- (4,4,4,5;a=1,2,3).

The new saturation lemma proves any W vertex not complete to a U part has U-degree at least10. Low vertices therefore carry one of four U-part labels; equal labels force a W-edge, and omega(H)<=11 caps the four classes at 4,4,4,3. Hence at least three W vertices must be high. Their minimum excess costs are d_{H[W]}(w)-2, but total W excess is four. The resulting finite high-set possibilities are analytically incompatible with a capacity-(4,4,4,3) colouring in all five kernels.

Files:
- `DELTA13_EPS0_KP_KERNEL_REDUCTION.md`
- `DELTA13_EPS0_KP_KERNEL_CLOSURE.md`
- `verify_delta13_eps0_kp_kernel.py`
- `verify_delta13_eps0_kp_closure.py`

## Minimum-slack subfrontier

The minimum epsilon_U+2delta=9 occurs at (3,3) and (4,1). If an independent W-four-set has total W-side slack one, `MINIMUM_SLACK_EXACT_CORE.md` forces the exact 7,7,7,8 U-kernel. The complementary branch in which every independent W-four-set has slack at least two remains OPEN.

## Remaining low-delta target

The next local target is the delta=13 non-four-partite L_U branch, followed by delta<=12. No status from the four-partite delta=13 proof is extrapolated to those cases.

The five shell templates remain a separate global same-core compatibility obligation.