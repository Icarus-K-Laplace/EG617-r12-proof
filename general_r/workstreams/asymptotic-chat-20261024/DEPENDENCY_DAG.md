# Dependency DAG — Asymptotic Synthesis

Updated: 2026-10-24  
Branch: workstream/general-r-asymptotic-20261024

## Primary route: bypass the scalable d2 backend

Hypothetical Problem-617 counterexample  
→ A_ext*: contextual 4r+1 / anchored 5r+1 dichotomy [OPEN]  
→ either a 4r+1 residual or an anchored 5r+1 terminal.

**4r+1 branch:** residual contract for r ≥ 17 [PROVED] → delta(F)=r+1 → contextual U_(4,1) cap gap (3r−13)/2 > 0 [PROVED] → contradiction.

**5r+1 branch:** delta(T) ≥ r plus contextual cap → delta(T) ∈ {r,r+1} [PROVED] → direct near-anchor triple for r ≥ 67 [PROVED] → common-antineighbourhood compression [PROVED] → |W|=2r, 2r+1 impossible for r ≥ 11 [PROVED] → if delta(T)=r+1, |W|=2r−1 Cell A/B excluded for r ≥ 25 [PROVED] → D_low finite-offset terminal nonextension [OPEN] → P(r).

The exact remaining windows for D_low are:
- delta(T)=r: 2r−4 ≤ |W| ≤ 2r−1;
- delta(T)=r+1: 2r−7 ≤ |W| ≤ 2r−2.

**Do not remove the low-degree |W|=2r−1 case:** the Cell A/B exclusion theorems use the high terminal assumption delta(T)=r+1.

## Conditional theorem S67-low

For every r ≥ 67,
\[
A_{ext}^*(r)\land D_{low}(r)\Longrightarrow P(r).
\]
Status: CONDITIONAL_ON_Aext_Dlow + ASYMPTOTIC_ANALYTIC.

This route does not invoke H_B or C*. It also weakens H_D: only the finite-offset near-anchor terminal family must be excluded, not every design-like terminal in full generality.

## Legacy backend route S68-v2

The earlier route remains valid as a separate conditional composition:
\[
A_{ext}(r)\land C^*(r)\land D(r)\Longrightarrow P(r),
\qquad r\ge68.
\]
Status: CONDITIONAL_ON_Aext_C*_D + ASYMPTOTIC_ANALYTIC.

It is no longer the shortest route because the contextual 4r+1 branch is already killed by the full-colour (k,s) cap and the 5r+1 terminal has a direct near-anchor reduction.

## Shared C/D transversal-cover interface

A single weighted transversal-cover lemma applies to two distinct objects without identifying them:

1. **Clean pair exchange:** for every four clean 2-blocks, alpha(H) ≤ 3 forces every endpoint transversal to contain a target edge. The exact 2-SAT audit strengthens the elementary cover inequality to at least six cross-block target edges.
2. **TD(5,r) terminal:** a missing target pair in one target group plus one point from each of the other four groups is a six-set; alpha(G0) ≤ 5 forces a target cross edge. The weighted cover inequality yields the existing cylinder lower bound and bounded-hub concentration.

The residual-core common-S pivot system is connected by separate exact repivot/owner-capacity identities; no unproved graph isomorphism between it and the TD block system is assumed.

This shared interface is useful accounting, **not** a terminal contradiction by itself. The clean-pair branch still has a linear feasible interval, and the TD branch still has an OPEN defect-chain propagation problem.

## Imported nodes and provenance

- Residual branch closure: theorem source commit 07cd8fb58ffd93d234b1e8b6104f939175d7fbda; current residual source head 7a4fb4c37cefec8d801fc7deb778568bfb24002e.
- Contextual cap plane: current architecture head a922c4d7646eb8d0087bde8547562c8aace02ee2.
- C repivot endpoint: current head 35fec3eaaab70b31e10b41065634b35b02a28e6c.
- D design terminal: current head 5b4162c239d3dfad84d130c3015a0db5919228c4.
