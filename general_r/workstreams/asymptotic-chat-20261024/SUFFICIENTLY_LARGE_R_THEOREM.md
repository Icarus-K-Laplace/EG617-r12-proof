# Sufficiently-Large-r Theorem

## Status

**CONDITIONAL_ON_A_C*_D + ASYMPTOTIC_ANALYTIC.**

This is not an unconditional solution of Problem 617.

## Definition

Let `P(r)` be Erdős Problem 617 at parameter r:

> every r-edge-colouring of `K_(r^2+1)` has an `(r+1)`-vertex set missing at least one colour.

Let:

- `H_A(r)` be the front residual/design dichotomy with the legal residual-core contract on the residual branch;
- `H_C*(r)` be closure of every surviving residual endpoint terminal after the already-proved endpoint reductions;
- `H_D(r)` be nonextension of every design-like terminal produced by H_A.

## Theorem S68 — H_B-free asymptotic synthesis

> **For every `r>=68`,**
>
> `H_A(r) and H_C*(r) and H_D(r)  =>  P(r)`.

Equivalently, if H_A, H_C*, and H_D hold for every r>=68, then

> **`forall r>=68, P(r)`.**

The Exact Three-Anchor hypothesis H_B is not assumed.

## Proof

Assume `r>=68` and suppose, for contradiction, that P(r) fails.

By H_A, the counterexample enters one of two branches.

### Branch D: design-like terminal

H_D says every such terminal is nonextendable/contradictory. Hence this branch is impossible.

### Branch R: legal `4r+1` residual

We have a legal pivot core H with

`|H|=3r-1`,
`alpha(H)<=3`,
`omega(H)<=r-1`,
`delta(H)>=r`.

The inherited core cap gives `K<=2r-2`, and the direct near-anchor forcing theorem supplies an independent triple with degree pattern

`(r, <=r+1, <=r+1)`.

We claim `K>=8` without assuming H_B.

Suppose instead `K<=7`. Since

`K=2e(H)-r(3r-1)`

and `r(3r-1)` is always even, K is even. Therefore `K<=6`.

The proved near-anchor reduction (valid for r>=13) converts the low-excess independent triple to an independent triple of three exact degree-r anchors.

Now invoke the sibling exact-three-anchor analytic theorem: for every r>=68, an exact degree-r independent triple under the core contract cannot coexist with `K<=7`. Its proof passes to the complement J, where

`Delta(J)=2r-2`,
`delta(J)>=2r-9`,
`|J|=3r-1`,

and uses

`2r-9 > 5(3r-1)/8`

which is exactly `r>67`. The Andrasfai-Erdos-Sos theorem then forces J to be 3-partite; a part has size at least r, contradicting `omega(H)<=r-1`.

Thus `K>=8`.

Write the residual deficit as

`epsilon=D_r(4r+1)-e(F)>=0`.

The exact backend conservation law gives

`q+epsilon=3r+3-K/2`,

so

`q<=3r-1-epsilon<=3r-1`.

For every regular repivot of missing degree d,

`q_y>=d(r+1-d)`.

If `4<=d<=r-3`, then

`q_y>=4(r-3)>3r-1`

for every r>=12. Hence no medium degree survives. Only

`d in {0,1,2,3,r-2,r-1,r}`

remains.

The imported endpoint theory then gives:

1. the d3 common-S sector is closed;
2. the high endpoint `d>=r-2` is reduced to a finite bounded-complement kernel with at most three high owners, shell kernel at most nine, and at most eight core incidence signatures;
3. the remaining scalable low-endpoint obstruction is d2, together with d0/d1 and the finitely encoded high kernels.

By H_C*, every such remaining terminal is contradictory or admits a legal improvement, contradicting terminal/maximality. Therefore Branch R is impossible.

Both H_A branches are impossible, contradiction. Hence P(r) holds. QED.

## Controlling threshold

The only numeric threshold introduced while eliminating H_B is

`2r-9 > 5(3r-1)/8`,

so

> **`r0=68`.**

The medium-degree inequality itself only needs r>=12 once K>=8.

## Stronger-hypothesis variant

If H_B is assumed as a theorem for all r>=12, the same proof gives

> `H_A + H_B + H_C* + H_D => P(r)` for every `r>=12`.

Thus 68 is not a backend structural threshold; it is the current cost of deriving H_B analytically rather than assuming it.

## Residual-only corollary

If a future front theorem rules out the design branch and always produces the legal residual branch, H_D disappears as well. Then for r>=68:

> `residual-only H_A + H_C* => P(r)`.

## What remains open before this becomes unconditional

1. H_A: all-large-r front extraction/core certification;
2. H_C*: d0/d1, scalable d2, and finite high-kernel terminal closure;
3. H_D: robust design-like terminal classification/nonextension.

H_B is no longer on this asymptotic blocker list above r=68.
