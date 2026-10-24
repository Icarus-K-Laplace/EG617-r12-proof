# Assumption Ledger — EG617 general-r asymptotic synthesis

Status policy: every statement below is tagged as proved, conditional, or open. No conditional theorem here is a claim that Problem 617 is solved.

Let `P(r)` denote Erdős Problem 617 at parameter r.

## H_A^ext — upstream extraction/design dichotomy

For a hypothetical minimal counterexample, force either:

1. an induced `4r+1` residual `F` with `alpha(F)<=4`, `omega(F)<=r-1`, and the inherited least-colour cap on every induced subgraph; or
2. a controlled `5r+1` design-like terminal.

Status: **OPEN** as an all-large-r theorem.

This is now strictly weaker than the original H_A residual-core contract. The sibling residual-extraction workstream proves analytically that for every `r>=17`, once such a `4r+1` residual exists, the complete backend pivot/core contract follows automatically:

- `delta(F)=r+1`;
- a degree-`(r+1)` pivot exists;
- its core has `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`.

Therefore **core minimum-degree certification is no longer an asymptotic hypothesis above 17**. The only front obstruction is upstream extraction versus the `5r+1` terminal.

Sibling source: `general_r/workstreams/residual-core-extraction-chat-20261024/RESIDUAL_BRANCH_CLOSURE.md`, head `07cd8fb58ffd93d234b1e8b6104f939175d7fbda`.

## H_B — exact/near three-anchor excess

Desired statement under the residual-core contract:

`K_r=2e(H)-r(3r-1) >= 8`

once the low-excess independent-triple branch is entered.

Status:

- **PROVED_ANALYTIC for r>=68** by the sibling three-anchor workstream using the Andrasfai-Erdos-Sos theorem on the complement;
- **OPEN for 12<=r<=67** as a complete theorem.

Thus H_B is not a required asymptotic hypothesis once `r>=68`.

Latest sibling head checked: `a98ef900be419993e3fe63d37a0cf82fa104c455`; the global threshold remains 68 while additional constant-skeleton cases are being closed.

## H_C* — endpoint terminal closure

A full global repivot potential is stronger than needed. Define H_C* to mean:

> every legal residual backend satisfying the core contract and `K_r>=8` has no terminal state after the already-proved medium-degree exclusion, d3 common-S closure, and high-endpoint bounded-kernel reduction.

Status: **OPEN**.

Already proved under the residual contract plus K>=8:

- no medium degree `4<=d<=r-3`;
- d3 common-S closes;
- total high owners `<=3`;
- high shell kernel `<=9`, core incidence signatures `<=8`;
- d2 one-loss identity `W=K+2r-2+a+b`, with three-class barrier `K+a+b>=r`.

Remaining scalable content is concentrated in d2, plus d0/d1 and finitely encoded high skeletons.

Sibling repivot head imported: `2974fd80882a4545a3a1a569418405ec4e3bdebc`.

## H_D — design terminal nonextension/stability

Desired statement:

> every `5r+1` design-like terminal produced by H_A^ext is nonextendable / contradictory for all sufficiently large r.

Status: **OPEN** in the required robust classification form.

Already proved for the exact affine-plane model: the standard affine-plane colouring of `K_(r^2)` cannot be extended by one vertex for any `r>=3` for which the construction exists. Hence the missing work is stability/classification, not the final exact extension contradiction.

## External analytic inputs already imported

1. Classical Andrasfai-Erdos-Sos theorem in the residual `r>=17` closure and three-anchor `r>=68` theorem.
2. Quantitative Turan stability in the multicolour fixed-deficit owner/clique bounds.

## Current minimal-hypothesis infinite-family statement

For every `r>=68`:

> **`H_A^ext(r) + H_C*(r) + H_D(r) => P(r)`.**

Status: **CONDITIONAL_ON_Aext_C_D + ASYMPTOTIC_ANALYTIC**.

The original core-certification part of H_A and all of H_B are both eliminated from the asymptotic hypothesis list.

A stronger-hypothesis finite-threshold variant remains:

for every `r>=12`, original `H_A + H_B + H_C* + H_D => P(r)`.
