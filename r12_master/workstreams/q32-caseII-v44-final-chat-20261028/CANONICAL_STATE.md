# EG617 r=12 — E408 Q32 v=44 final canonical state

Updated: 2026-10-28
Repository: `Icarus-K-Laplace/EG617-r12-proof`
Branch: `workstream/r12-q32-caseII-v44-final-20261028`
Write scope: `r12_master/workstreams/q32-caseII-v44-final-chat-20261028/`
Source base: `workstream/r12-twochat-e408-global-20261026` at `937a905ed26e54ec10e9bdade1d9b655da8f6176`.

## Headline

> **The complete E408-Q32 support layer `|U|=44` is CLOSED for `m=8,9,10`.**

The new m=8 and m=9 proofs do not use Case-II's assumption `alpha(M)<=9`; they are stronger support-level exclusions. Together with the inherited corrected multiplicity exclusion of m=10, no source-correct Q32 realization with `|U|=44` remains.

This does **not** certify EG617(r=12). E408-Q32 still has higher-support terminals `|U|=45,46,47`.

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

## New theorem A — zero-shell special-edge obstruction

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

## New theorem B — 130-color W-pair rigidity

Let D be a 130-edge color and let u,v be W-points with

`d_D(u)=d_D(v)=4`,

and all their D-neighbors in H.

Then uv must have color D.

Proof outline:

1. At u, put `S=N_D(u)` and let N be the 56 D-nonneighbors.
2. Kang--Pikhurko Theorem1 at `(56,11)` gives `e(D[N])>=119`.
3. The 130-edge total, `delta(D)>=4`, and `alpha(H)<=4` force

`D[S]=K4-e`, `e_D(S,N)=2`, `e(D[N])=119`.

4. Equality triggers Kang--Pikhurko Theorem4. Since the eleven old parts cover55 vertices and `omega(D[N])<=5`, all have size5. Thus

`D[N]=9 isolated K5 dot-union G11`,

and every degree-four vertex of D[N] lies in an isolated K5.
5. If uv were not a D-edge, v would lie in N and retain degree4 there, so its four D-neighbors would form a K4. Together with v they would give a D-colored K5 wholly in H, contradicting `alpha(H)<=4`.

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

But the three two-element L-sets are the three distinct pairs of nonexact colors, so every nonexact color is core-only degree4 at exactly two W-points. Their pair-rigidity cluster is a `K5-e` whose three U vertices include c,a,b with

`ca,cb in E(D)`, `ab notin E(D)`.

That is impossible in a disjoint union of clique components.

Thus `(3,3,2)` is impossible.

Therefore

> **`|U|=44,m=8` is impossible.**

## Full v=44 verdict

- m=10: inherited impossible from corrected multiplicity;
- m=9: impossible by zero-shell special-edge obstruction;
- m=8: impossible by W-pair rigidity and U-pool saturation.

Hence

> **E408-Q32 / `|U|=44` is CLOSED without using Case-I or Case-II shell dichotomy.**

## Current Q32 frontier after this workstream

The v=44 support layer is gone entirely.

Inherited live structure outside this workstream:

- Case I v=45: closed;
- Case I v=46,m=10: closed;
- Case I v=46,m=9: closed;
- Case I v=46,m=8: closed by the 130-edge minimum-degree-four theorem;
- Case I v=47: open;
- Case II v=45,46,47: open.

Therefore the smallest-support OPEN Q32 layer is

> **Case II / `|U|=45`**

(with its m-subcases requiring a fresh audit before any further promotion).

EG617(r=12) remains OPEN / NOT_CERTIFIED until all remaining E408-Q32 higher-support branches are closed.

## Verification status

`verify_v44_m8_closure_arithmetic.py` was executed successfully in the research session and returned

`V44_M8_CLOSURE_ARITHMETIC_OK`.

It verifies only:

- the finite m=8 multiplicity enumeration;
- the `(56,11)` extremal arithmetic;
- the unique local count `(a,b)=(5,2)`;
- the three-color L-set combinatorics;
- the final 700-edge saturation arithmetic.

It does not mechanically verify Kang--Pikhurko, the source Type-I construction, Turan equality, or the analytic graph-theoretic implications.