# Sufficiently-Large-r Synthesis Theorems

## Status

**No unconditional all-large-r theorem is certified.**

Two conditional synthesis routes are now recorded. The newer one has the shorter dependency chain and lower numerical threshold, but replaces the broad C*/D interfaces with a narrower near-anchor terminal theorem.

## Theorem S67-low — shortest route

For every r ≥ 67,
\[
A_{ext}^*(r)\land D_{low}(r)\Longrightarrow P(r).
\]
Status: **CONDITIONAL_ON_Aext_Dlow + ASYMPTOTIC_ANALYTIC**.

### A_ext*

Every hypothetical counterexample produces either:
1. a contextual legal 4r+1 residual with alpha ≤ 4, omega ≤ r−1, and inherited full-colour cap; or
2. an anchored contextual 5r+1 terminal with alpha=5, omega ≤ r−1, delta ≥ r, inherited full-colour cap, and no legal 4r+1 residual.

This is **OPEN**.

### D_low

Every anchored 5r+1 terminal satisfying that contract is contradictory after direct near-anchor extraction and common-antineighbourhood compression, for every remaining offset:
- delta=r: |W| ∈ {2r−4, 2r−3, 2r−2};
- delta=r+1: |W| ∈ {2r−7, …, 2r−2}.

This is **OPEN**. The |W|=2r−1 layer has been eliminated in both anchor-degree branches for r≥25; the remaining D_low cases have |W|≤2r−2.

### Proof

The 4r+1 branch has delta=r+1 for r ≥ 17 by the residual-branch theorem. Its contextual cap is
\[
e(F)\le 2r^2+r+7,
\]
while
\[
e(F)\ge\frac{(4r+1)(r+1)}2,
\]
with gap (3r−13)/2 > 0 for r ≥ 5. Contradiction.

For the 5r+1 branch, delta ≥ r. Its contextual cap is
\[
e(T)\le\frac{5r^2+7r+18}{2}.
\]
If delta ≥ r+2, then e(T) ≥ (5r+1)(r+2)/2, exceeding the cap by 2r−8 > 0. Thus delta ∈ {r,r+1}.

For r ≥ 67, direct near-anchor extraction gives the appropriate independent triple. Common-antineighbourhood compression confines |W| to the windows in the definition of D_low, after eliminating |W|=2r,2r+1. For delta=r+1, the |W|=2r−1 Cell A and Cell B configurations are excluded for r ≥ 25. For delta=r, the new LOW_DEGREE_TOP_LAYER_CLOSURE theorem excludes |W|=2r−1 for r ≥ 25 by a duplicate-anchor-incidence contradiction. This leaves the stated windows. D_low excludes the remaining terminal cases. Both branches are then impossible.

This theorem does not invoke H_B, C*, or a global repivot potential.

## Theorem S68-v2 — legacy backend route

For every r ≥ 68,
\[
A_{ext}(r)\land C^*(r)\land D(r)\Longrightarrow P(r).
\]
Status: **CONDITIONAL_ON_Aext_C*_D + ASYMPTOTIC_ANALYTIC**.

This composition remains valid under its original contracts. It assumes:
- A_ext: contextual 4r+1 residual or controlled 5r+1 design terminal;
- C*: closure of every surviving residual endpoint terminal after the proved medium-degree, d3 and high-endpoint reductions;
- D: robust nonextension of every design-like terminal.

It does not assume the residual minimum-degree contract separately or the exact three-anchor floor K ≥ 8, because those are derived for r ≥ 68.

## Threshold accounting

- Residual branch contract: r ≥ 17.
- Direct near-anchor extraction inside the 5r+1 terminal: r ≥ 67, relative to Liu–Ren–Wang 2025; classical AES fallback gives r ≥ 71.
- High-layer Cell A exclusion: r ≥ 25.
- High-layer Cell B exclusion: r ≥ 16.
- Low-degree |W|=2r−1 closure: r ≥ 25, from LOW_DEGREE_TOP_LAYER_CLOSURE.md.
- Therefore the shortest conditional composition has r0=67, controlled by direct near-anchor extraction, not by the old three-anchor threshold 68.

## Unconditional status

\[
\boxed{r_0^{unconditional}=\texttt{NOT CERTIFIED}.}
\]

The two remaining theorem-sized blockers on the shortest route are A_ext* and D_low. The C* endpoint theorem is a valid alternative route, but is not a dependency of S67-low.
