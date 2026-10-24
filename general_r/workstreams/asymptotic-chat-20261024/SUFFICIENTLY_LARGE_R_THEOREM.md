# Sufficiently-Large-r Theorem

## Status

**CONDITIONAL_ON_Aext_C*_D + ASYMPTOTIC_ANALYTIC.**

This is not an unconditional solution of Problem 617.

Let `P(r)` be Erdős Problem 617 at parameter r.

Define:

- `H_A^ext(r)`: every hypothetical counterexample yields either
  1. an induced `4r+1` residual `F` with `alpha(F)<=4`, `omega(F)<=r-1`, and the inherited least-colour cap, or
  2. a controlled `5r+1` design-like terminal;
- `H_C*(r)`: closure of every surviving residual endpoint terminal after the already-proved endpoint reductions;
- `H_D(r)`: nonextension of every design-like terminal produced by `H_A^ext`.

## Theorem S68-v2 — extraction-only front hypothesis

> **For every `r>=68`,**
>
> `H_A^ext(r) and H_C*(r) and H_D(r)  =>  P(r)`.

Neither the original residual-core minimum-degree part of H_A nor Exact Three-Anchor H_B is assumed.

## Proof

Assume `r>=68` and suppose P(r) fails.

By `H_A^ext`, the counterexample enters one of two branches.

### Branch D: design-like terminal

H_D makes this branch contradictory.

### Branch R: induced `4r+1` residual

The residual-extraction sibling theorem is analytic for every `r>=17`: any induced `4r+1` graph F with

`alpha(F)<=4`, `omega(F)<=r-1`,

and the inherited least-colour cap satisfies

`delta(F)=r+1`.

Hence there is a pivot p of degree `r+1`, and its core

`H=F-N_F[p]`

satisfies

`|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`.

So the full backend residual-core contract is now **derived**, not assumed.

The inherited core cap gives `K<=2r-2`, and direct near-anchor forcing supplies an independent triple with degree pattern

`(r, <=r+1, <=r+1)`.

We claim `K>=8` without assuming H_B. Suppose `K<=7`. Since

`K=2e(H)-r(3r-1)`

is even, `K<=6`. The proved near-anchor reduction converts the independent triple to three exact degree-r anchors. For `r>=68`, the sibling three-anchor analytic theorem excludes this under `K<=7`: in the complement J,

`Delta(J)=2r-2`, `delta(J)>=2r-9`, `|J|=3r-1`,

and

`2r-9 > 5(3r-1)/8`.

Andrasfai-Erdos-Sos makes J 3-partite; one part has at least r vertices, contradicting `omega(H)<=r-1`. Hence `K>=8`.

Write

`epsilon=D_r(4r+1)-e(F)>=0`.

The exact backend conservation law gives

`q+epsilon=3r+3-K/2`,

so

`q<=3r-1-epsilon<=3r-1`.

Every regular repivot of missing degree d has

`q_y>=d(r+1-d)`.

For `4<=d<=r-3`,

`d(r+1-d)>=4(r-3)>3r-1`

for every `r>=12`; hence no medium degree survives.

The imported endpoint theory now gives:

1. d3 common-S is closed;
2. high endpoint `d>=r-2` has at most three owners and reduces to a bounded kernel (shell kernel at most nine, at most eight core incidence signatures);
3. the remaining scalable low-endpoint obstruction is d2, together with d0/d1 and the finite high skeletons.

By H_C*, every remaining terminal is contradictory or admits a legal improvement, contradicting terminal/maximality. Thus Branch R is impossible.

Both branches are impossible, so P(r) holds. QED.

## Threshold accounting

There are now two internal analytic thresholds:

- residual contract from extracted `4r+1` F: `r>=17`;
- H_B-free exact-three-anchor deduction: `r>=68`.

Thus the synthesis threshold remains

> **`r0=68`**, controlled solely by `2r-9>5(3r-1)/8`.

The new residual theorem does not lower r0 numerically because `17<68`, but it removes a load-bearing hypothesis.

## Stronger-hypothesis variant

If the original full H_A and H_B are assumed for all r>=12, the older composition still yields P(r) for every r>=12.

## What remains open before an unconditional infinite-family theorem

1. `H_A^ext`: force the `4r+1` residual or controlled `5r+1` terminal;
2. `H_C*`: close d0/d1, scalable d2, and finite high kernels;
3. `H_D`: robust design-terminal classification/nonextension.

The core minimum-degree theorem and H_B are no longer asymptotic blockers above 68.
