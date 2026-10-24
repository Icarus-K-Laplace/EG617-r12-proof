# Assumption Ledger — EG617 general-r asymptotic synthesis

Status policy: every statement below is tagged as proved, conditional, or open. No conditional theorem in this workstream is a claim that Problem 617 is solved.

## Target

Let `P(r)` denote:

> every r-edge-colouring of `K_(r^2+1)` contains `r+1` vertices whose induced graph misses at least one colour.

The headline target is `exists r0 forall r>=r0 P(r)`.

## H_A — front extraction / residual-design dichotomy

For a hypothetical minimal counterexample, force either:

1. a legal `4r+1` residual `F` with `alpha(F)<=4`, `omega(F)<=r-1`, a degree-`r+1` pivot, and every legal pivot core `H` satisfying
   `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`; or
2. a controlled `5r+1` design-like terminal.

Status: **OPEN** as an all-large-r theorem.

Already proved symbolically: the orders `4r+1`, `5r+1`, the hereditary cap, the shell/core sizes and the independence/clique inheritance. The load-bearing missing source is the all-r recurrence/extraction, in particular certification of `delta(H)>=r` in every legal pivot core.

Source: `GENERAL_R_FRONT_STRUCTURAL_SOURCE.md`.

## H_B — exact/near three-anchor excess

Desired statement under the residual-core contract:

`K_r=2e(H)-r(3r-1) >= 8`

once the low-excess independent-triple branch is entered.

Status:

- **PROVED_ANALYTIC for r>=68** after exact-anchor reduction, by the sibling `three-anchor` workstream using the Andrasfai-Erdos-Sos theorem on the complement;
- **OPEN for 12<=r<=67** in the sibling workstream.

Important synthesis consequence: H_B is **not a required asymptotic hypothesis** once `r>=68`; it can be derived from H_A's core contract plus the already-proved direct near-anchor forcing/reduction.

Sibling source commit: `0c226d78e39e3da2a594f8a6121a864d2efa09ea`.

## H_C — endpoint termination

The global repivot termination theorem is still open. For synthesis it is deliberately weakened to the exact remaining endpoint task after importing all already-proved reductions.

Define `H_C*` to mean:

> every legal residual backend satisfying the core contract and `K_r>=8` has no terminal state after the proved medium-degree exclusion, d3 common-S closure, and high-endpoint bounded-kernel reduction.

Equivalently, it is enough to close the surviving endpoint sectors (currently d0/d1, scalable d2 plateau/equality/positive-loss states, and every bounded high-endpoint skeleton not already contradictory).

Status: **OPEN**.

Already proved in sibling repivot workstream under A+B:

- no medium degree `4<=d<=r-3`;
- d3 common-S endpoint closes;
- total high owners `<=3`;
- high endpoint shell kernel `<=9` and core incidence signatures `<=8`;
- d2 exact one-loss identity `W=K+2r-2+a+b` and three-class barrier `K+a+b>=r`.

Sibling source commit: `2974fd80882a4545a3a1a569418405ec4e3bdebc`.

## H_D — design terminal nonextension

Desired statement:

> every `5r+1` design-like terminal produced by H_A is nonextendable / contradictory for all sufficiently large r.

Status: **OPEN** in the required robust classification form.

Already proved unconditionally for the exact affine-plane model: the standard affine-plane colouring of `K_(r^2)` cannot be extended by one vertex for any `r>=3` for which the construction exists. This supplies the exact terminal contradiction once stability/classification reaches two orthogonal clique partitions.

Source: `GENERAL_R_AFFINE_PLANE_NONEXTENSION.md`.

## External analytic inputs already used by imported results

1. Classical Andrasfai-Erdos-Sos theorem in the three-anchor `r>=68` proof.
2. Furedi quantitative Turan stability in the multicolour fixed-deficit owner/clique bounds.

These are external theorem dependencies, not new assumptions invented by this workstream.

## Current minimal-hypothesis infinite-family statement

For every `r>=68`:

`H_A(r) + H_C*(r) + H_D(r) => P(r)`.

Status: **CONDITIONAL_ON_A_C_D + ASYMPTOTIC_ANALYTIC**.

H_B has been eliminated from the hypothesis list for `r>=68`.

A stronger-threshold but stronger-hypothesis version is:

for every `r>=12`,

`H_A(r) + H_B(r) + H_C*(r) + H_D(r) => P(r)`.
