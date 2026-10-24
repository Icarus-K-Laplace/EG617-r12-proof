# General-r Program

Status: WORKING RESEARCH PROGRAM. This file deliberately distinguishes r=12-proved facts from symbolic conjectures.

## Objective

Upgrade EG617 from an r=12 fixed-instance proof program into a general-r architecture. The target dependency chain is

`K_{r^2+1} -> front reduction -> F_r -> residual core H_r -> defect transport / repivot -> anchor-or-sunflower dichotomy -> global contradiction`.

Every edge of this chain must be tagged one of:

- `PROVED_FOR_ALL_R`
- `PROVED_FOR_R12_ONLY`
- `PLAUSIBLE_SYMBOLIC`
- `ASYMPTOTIC_ONLY`
- `OPEN`

## Current symbolic candidates

- ambient complete graph size: `r^2+1` — PLAUSIBLE_SYMBOLIC pending derivation from the exact problem statement/reduction.
- front residual size: `5r+1` — PLAUSIBLE_SYMBOLIC pending front-recurrence archaeology.
- Ramsey residual size: `4r+1` — PLAUSIBLE_SYMBOLIC pending derivation.
- backend core size: `3r-1` — PLAUSIBLE_SYMBOLIC; for r=12 this is 35.
- pivot shell size: `r+1` — PLAUSIBLE_SYMBOLIC; for r=12 this is 13.
- backend core degree floor: `delta(H_r)>=r` — PLAUSIBLE_SYMBOLIC pending general lower-order seed.
- backend core clique cap: `omega(H_r)<=r-1` — PLAUSIBLE_SYMBOLIC.
- backend core independence cap: `alpha(H_r)<=3` — likely structural if the residual remains K4-free in the target graph.

## Generalization priority

1. Prove the residual-core source for `|H_r|=3r-1`, `delta(H_r)>=r`, `omega(H_r)<=r-1`, `alpha(H_r)<=3`.
2. Derive the backend edge identity symbolically.
3. Parameterize the exact repivot/allowance transport identities.
4. Parameterize anchor excess and support compatibility.
5. Compare shell-forced owner demand with general hereditary owner capacity and seek a slope contradiction for all sufficiently large r.
6. Only after the symbolic theorem is frozen, use r=13 as a held-out test.

## Candidate general theorem stack

### Residual-core theorem

Candidate: every legal backend pivot produces a core `H_r` on `3r-1` vertices with `alpha<=3`, `omega<=r-1`, and `delta>=r`.

Status: OPEN until provenance is derived symbolically.

### General anchor-excess theorem

For

`K_r(H)=sum_v(d_H(v)-r)`,

seek a bound of the form

`independent low-excess triple => K_r(H)>=f(r)`.

The r=12 theorem gives the data point `f(12)>=8` for total anchor excess <=3. This single data point is not yet a general formula.

### General support-compatibility theorem

The zero-charge incidence-signature lemma is already conceptually parameterized by the core independence number, not by r. The sunflower/collapsed-signature branch should generalize once the common-S row-closure and one-loss defect identity are available symbolically. Owner capacities should be written as `C_r(d, pattern, W)` through the hereditary cap function.

### General repivot potential

Seek a symbolic potential `Psi_r` whose first coordinate is q/charge and whose lower coordinates encode transported slack, repeated-row energy, and anchor deficit. Non-rigid configurations should admit an improving repivot; rigid equality configurations should fall into the anchor/sunflower dichotomy.

## Highest-leverage bridge lemma (current candidate)

**General Defect-Transport Dichotomy.** For the symbolic backend residual core `H_r`, every maximal legal local view either

1. contains an independent triple of total degree excess at most `h_r`, forcing `K_r(H)>=f(r)`;
2. has zero/low-charge incidence signatures collapsed into a bounded sunflower family with owner capacity `C_r(d)`;
3. or admits a legal repivot that strictly increases a bounded symbolic potential `Psi_r`.

If shell forcing demands owner multiplicity `N_r > C_r(d)` whenever the anchor branch is excluded, then the backend is impossible. The key asymptotic target is to prove `N_r-C_r(d)` has positive linear slope.

This is the single bridge that would explain the r=12 pivot/support/anchor machinery as one general stability theorem.
