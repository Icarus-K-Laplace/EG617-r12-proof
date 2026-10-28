# EG617 r=12 — E408 Q32 low-support canonical state (v=44,45)

Updated: 2026-10-28
Repository: `Icarus-K-Laplace/EG617-r12-proof`
Branch: `workstream/r12-q32-caseII-v44-final-20261028`
Write scope: `r12_master/workstreams/q32-caseII-v44-final-chat-20261028/`
Source base: `workstream/r12-twochat-e408-global-20261026` at `937a905ed26e54ec10e9bdade1d9b655da8f6176`.

## Headline

> **The complete E408-Q32 support layers `|U|=44` and `|U|=45` are CLOSED for `m=8,9,10`.**

The v=44 proof closes m=8 and m=9 without the Case-I/Case-II shell dichotomy; m=10 is excluded by corrected multiplicity. The new source-correct v=45 proof closes all three m-cases without exceptional-vertex injectivity.

The final v=44 m=8 local contradiction is hardened in `V44_M8_FINAL_LOCAL_HARDENING.md`. A shorter alternate v=44 m=8 proof using the no-pair theorem is in `V44_M8_NO_PAIR_SHORTCUT.md`. The new degree-four obstruction is recorded in `Q32_130_NO_TWO_CORE_ONLY_DEG4.md`, and the v=45 reduction is in `V45_SOURCE_CORRECT_CLOSURE.md`.

This does **not** certify EG617(r=12). The higher-support terminals `|U|=46,47` remain open and require separate source-correct audits.

## Frozen Q32 contract used

`|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`,

`sum_{x in H}(d_H(x)-12)=6`.

`A=N_F(p)`, `|A|=13`, `O={p} union A`.

There are `m in {8,9,10}` exact-129 non-target colors. Each exact color uses the source-correct Kang--Pikhurko Type-I factorization

`10 isolated K5 dot-union G11`,

with source parameter `a in {1,2,3,4}` and special degree `9-a`.

The universal degree-nine exceptional-vertex claim is retracted and is not used.

The registered factor-witness support is U; here `|U|=44`, so `W=H\U` has three vertices.

## Source-correct imported facts

1. Corrected multiplicity: for `w in W`, `n_w>=m-6`.
2. For an exact color non-special at w, w lies in a multi-outside factor K5 and has at least two shell neighbors in that color.
3. Every 130-edge nonexact color has minimum degree at least4.
4. For m=8, the three nonexact colors are all 130-edge colors, so their pointwise floor is12.
5. Exact Type-I special excess over the degree-four baseline is `5-a`.
6. The v=44 core identity is

`e(bar(H[U]))=703-E_U-e_H(W)`.

## Theorem A — zero-shell special-edge obstruction

For an exact color C with `x_C=w in H`, the source gadget contains the C-colored K5

`{x_C} union (N_t\{y})`.

If w has no C-neighbor in A, this K5 cannot lie wholly in H because `alpha(H)<=4`. Its outside vertex must therefore be p, so pw has color C.

Hence at a fixed W-point at most one special exact color can have zero shell degree.

## m=9 closure

Corrected multiplicity gives exactly three special and six non-special exact colors at each W-point.

The six non-special exact colors consume at least twelve distinct shell edges. Therefore at least two of the three special exact colors have zero shell degree.

The zero-shell obstruction allows at most one.

Contradiction.

Thus

> **`|U|=44,m=9` is impossible.**

This simultaneously closes the all-double and one-triple branches and is independent of the previously derived shell-edge floors and parameter-profile list.

## m=8 normal form

Pointwise degree floor:

`target13 + exact 8*4 + nonexact 3*4 =57`.

Only three slack units remain. Therefore each W-point has `n_w in {2,3}` and the only sorted multiplicity partitions are

`(2,2,2)`, `(3,2,2)`, `(3,3,2)`.

At n=2:

- special parameters are `(4,4)` or `(4,3)`;
- six non-special exact colors own exactly twelve shell edges;
- one special exact color owns the thirteenth shell edge;
- the other special exact color has zero shell degree and owns pw;
- no target or nonexact color owns an edge from w to O;
- at least two 130-edge colors are degree4 and core-only.

At n=3:

- special parameters are `(4,4,4)`;
- all three nonexact colors have degree4;
- exact colors own at least thirteen of the fourteen w--O edges;
- therefore at least two 130-edge colors are core-only.

## Theorem B — 130-color W-pair rigidity

Let D be a 130-edge color and let u,v be W-points with

`d_D(u)=d_D(v)=4`,

and all their D-neighbors in H.

Then uv must have color D.

Proof spine:

1. At u, put `S=N_D(u)` and let N be the 56 D-nonneighbors.
2. Kang--Pikhurko Theorem1 at `(56,11)` gives `e(D[N])>=119`.
3. The 130-edge total, `delta(D)>=4`, and `alpha(H)<=4` force

`D[S]=K4-e`, `e_D(S,N)=2`, `e(D[N])=119`.

4. The two S--N edges are forced one each onto the two missing-pair endpoints of `K4-e`; the two central vertices have no S--N edge and have global D-degree exactly4.
5. Equality triggers Kang--Pikhurko Theorem4. Since the eleven old parts cover55 vertices and `omega(D[N])<=5`, all have size5. Thus

`D[N]=9 isolated K5 dot-union G11`,

and every degree-four vertex of D[N] lies in an isolated K5.
6. If uv were not a D-edge, v would lie in N and retain degree4 there, so its four D-neighbors would form a K4. Together with v they would give a D-colored K5 wholly in H, contradicting `alpha(H)<=4`.

The primary Kang--Pikhurko paper was directly rechecked: Theorem1 applies at `(56,11)` and Theorem4 indeed characterizes all extremal graphs by the explicit construction.

## m=8 universal W-edge consequence

For each W-point w define

`L(w)={D among the three 130-edge colors: d_D(w)=4 and N_D(w) subset H}`.

The m=8 normal form gives `|L(w)|>=2` at every W-point.

Any two such subsets of a three-color set intersect. Pair rigidity then forces every W--W edge to be a 130-edge nonexact color.

Thus

> **all three W--W edges are nonexact.**

## m=8 partition closures

### `(2,2,2)`

Two exact colors have special point outside W. Any exact color special outside W must own at least one W--W edge. This contradicts the universal nonexact W-edge conclusion.

### `(3,2,2)`

One exact color has special point outside W and must own at least one W--W edge. Contradiction again.

### `(3,3,2)`

All exact special points lie on W.

Pair rigidity and edge uniqueness force:

- the n=2 profile is `(4,4)`;
- all three L-sets have size exactly2;
- every W-point has target core excess exactly1;
- `E_U=3`, `e_H(W)=0`;
- therefore `e(bar(H[U]))=700`.

All eight exact colors have `a=4`. Since all W--W edges are nonexact, every exact color is double type and its two non-special W-points lie in distinct isolated double-outside K5s. Its special gadget parts are single-outside.

Each exact color therefore uses at least65 U-edges:

`60` from ten witness K4s,

`+2` from the two U-pairs in the isolated double factors,

`+3` from source cross edges `y--P`.

Eight exact colors use at least520 edges. The three nonexact colors use at least180. This exactly fills the 700-edge U-complement pool.

Hence every nonexact color has exactly60 U-edges, so ordinary Turan equality gives

`D[U]=8K4 dot-union 4K3`.

The hardened final local argument is:

- the three size-two L-sets are the three distinct two-subsets of the three nonexact colors;
- hence each nonexact color D owns exactly one W--W edge uv, and the third W-point is not in `N_D(u)`;
- in the local `D[S]=K4-e`, v cannot be a missing endpoint: the forced `(1,1,0,0)` S--N cross-edge distribution would make `D[N_D(v)]` a triangle plus an isolated vertex, contradicting the required local `K4-e` at v;
- so v is central, and the other three vertices `c,a,b` of S lie in U with `ca,cb in E(D)` and `ab notin E(D)`;
- this is impossible in the disjoint union of clique components `8K4 dot-union 4K3`.

Thus `(3,3,2)` is impossible.

Therefore

> **`|U|=44,m=8` is impossible.**

## New source-correct v=45 closure

The note `V45_SOURCE_CORRECT_CLOSURE.md` proves that `|U|=45` is impossible for `m=8,9,10` without exceptional-vertex injectivity. It uses the corrected multiplicity lower bound, pointwise degree budgets, the zero-shell/pivot-edge lemma, and the new 130-edge no-pair theorem.

The valid nonexact pointwise floor sums are `L_8=12`, `L_9=7`, and `L_10=2`. The old global summary value `L_9=6` is stale: a 130-edge color has minimum degree four and a 131-edge color has minimum degree three.

The finite arithmetic regression `verify_v45_source_correct_profiles.py` returned `V45_SOURCE_CORRECT_PROFILE_ARITHMETIC_OK`. This verifies only the finite parameter/profile and shell-count arithmetic, not the graph lemmas or external extremal inputs.

## Full v=44 verdict

- m=10: inherited impossible from corrected multiplicity;
- m=9: impossible by zero-shell special-edge obstruction;
- m=8: impossible by W-pair rigidity and U-pool saturation, with the final local step independently hardened.

Hence

> **E408-Q32 / `|U|=44` is CLOSED without using Case-I or Case-II shell dichotomy.**

## Source-correct v45 closure (2026-10-28)

`V45_SOURCE_CORRECT_CLOSURE.md` closes the full `|U|=45` support layer for `m=8,9,10`. It combines the corrected multiplicity bound, pointwise degree floors `L_8=12,L_9=7,L_10=2`, the zero-shell/pivot-edge obstruction, and the new 130-edge no-pair theorem.

The no-pair theorem `Q32_130_NO_TWO_CORE_ONLY_DEG4.md` proves that a 130-edge color cannot contain two distinct vertices in H, each of degree four with all four color-neighbors in H. The proof uses the (56,11) second-Turan equality and the local K4-e cross-edge structure, without exceptional-vertex injectivity.

The finite profile/shell arithmetic regression returned `V45_SOURCE_CORRECT_PROFILE_ARITHMETIC_OK`. This verifies the finite arithmetic only; the graph lemma and its extremal inputs remain analytic dependencies.

## Current Q32 frontier after this workstream

The source-correct support layers `|U|=44` and `|U|=45` are both closed for all `m in {8,9,10}`.

The remaining higher-support terminals `|U|=46,47` are **not** closed by this workstream. Do not import `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md` as a closure of `|U|=46`: that older proof uses exceptional-vertex injectivity, which was retracted with the false universal degree-nine premise. Any claimed v=46/v=47 closure must be audited from source-correct premises in its own workstream.

EG617(r=12) remains OPEN / NOT_CERTIFIED.

## Verification status

`verify_v44_m8_closure_arithmetic.py` was re-executed after hardening and returned

`V44_M8_CLOSURE_ARITHMETIC_OK`.

It verifies:

- the finite m=8 multiplicity enumeration;
- the `(56,11)` extremal arithmetic;
- the unique local count `(a,b)=(5,2)`;
- the forced S--N distribution `(1,1,0,0)`;
- all six ordered legal three-color L-set assignments and the fact each nonexact color owns exactly one W--W edge;
- the missing-endpoint finite neighbor-edge count (3 rather than 5);
- the final 700-edge saturation arithmetic.

It does not mechanically verify Kang--Pikhurko, the source Type-I construction, Turan equality, or the analytic graph-theoretic implications.

## Dependency status

`DEPENDENCY_AUDIT.md` verdict:

> **PASS_WITH_EXPLICIT_EXTERNAL_THEOREMS / HARDENED.**

The proof uses no retracted degree-nine exceptional point, no exceptional-vertex injectivity, no stale exact-count collapse, no Q33/E407 284-edge identity, no Case-I three-point cover, and no SAT/ILP UNSAT claim.