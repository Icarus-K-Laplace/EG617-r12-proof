# Front-Recurrence Workstream — Canonical State

Date: 2026-10-24
Branch: `workstream/general-r-front-recurrence-20261024`
Scope: symbolic decompilation/termination of the r=12 contextual front recurrence. This workstream does not replace the separate residual-core extraction proof.

## Headline status

- **H1 (<10 symbolic transitions): ACHIEVED.** The 1752 r=12 nodes compress to seven transition schemas.
- **H2 (general termination conditional on symbolic seeds): PROVED for every `r>3`.** The natural-number potential `Phi_r(a,n)=(r^2+2)a+n` strictly decreases on every genuine recursive dependency.
- **H3 (all sufficiently large r front recurrence): OPEN.** The cutoffs `M_r(2)<=2r-1` and `M_r(3)<=3r` are now proved for `r>=6`, but the uniform edge-floor seed envelope and all-state dominance remain open.
- **H4 (`4r+1` residual OR `5r+1` terminal): CONDITIONAL THEOREM PROVED.** It follows once the recurrence floors dominate every symbolic outer budget except the extraction/design coordinates.

## Current symbolic state

The contextual state is

`S_r(a,n)=(a,n,B_r(a,n),M_r(<a); D_r)`

for induced residual graphs with

`alpha<=a`, `omega<=r-1`,

and inherited hereditary cap

`D_r(n)=C(n,2)-(r-1)p_r(n)`.

The proof state need not retain individual fixed-r node labels, concrete 145/61/49 constants, or an explicit degree sequence. A minimum-degree h is a finite row variable evaluated inside a state.

## Transition rules

Seven schemas suffice:

1. base/cutoff/seed injection;
2. vertex-deletion averaging `(a,n)->(a,n-1)`;
3. minimum-degree pivot/core restriction `(a,n)->(a-1,n-h-1)`;
4. shell-complement hereditary-cap forcing;
5. pair-cover + matching forcing using `M_r(a-2)`;
6. triangle-free / triangle dichotomy using `M_r(a-3)`;
7. cap overflow / emptiness / outer terminal recognition.

No transition depends on a same-or-larger state coordinate.

## Candidate potential

**Accepted:**

`Phi_r(a,n)=(r^2+2)a+n`.

It is strictly monotone decreasing on every recursive dependency.

**Rejected as universal termination potentials:**

`e-lambda n`, `e-D_r(n)`, degree-deficit/excess sums, and convex degree energies. These may plateau or move in the wrong direction under deletion/core restriction.

## Equality / plateau cases

Numerical floor plateaus are allowed and harmless because coordinate descent remains strict. Equality in Turan, matching, Mantel, pair-cover, triangle-cover, inherited cap, or outer budget is deferred to terminal rigidity analysis. No infinite plateau chain is possible.

## Finite terminal family

Internal recurrence terminals reduce to seven constant schemas: base/cutoff, core-empty, pair-density failure, triangle-alternative failure, no surviving degree, cap overflow, and outer-budget survivor.

The desired outer terminal family contains only:

- extraction: `d=r-1`, `j=r-5`, `(a,n)=(4,4r+1)`;
- design terminal: `d=r-1`, `j=r-6`, `(a,n)=(5,5r+1)`.

At r=12 the exact certificate proves this reduction, with the latter equal to T61.

## External seed interface

The r=12 recurrence architecture uses, beyond automatic bases and contextual `a=4` exclusion, only:

- cutoffs `M_r(2)<=2r-1`, `M_r(3)<=3r` proved for all `r>=6` (the abstract-contract cutoff fails at r=4,5);
- five edge-floor coordinates `(2,2r-1)`, `(3,3r-1)`, `(3,3r)`, `(4,4r-1)`, `(4,4r)`.

At r=12 the floor values are 131,210,234,284,308. This is a structurally sufficient seed interface; mathematical minimality among all possible interfaces is not claimed.

## Current provable r range

- **Abstract recurrence termination:** every `r>3`, conditional on any finite sound seed/cutoff package.
- **Conditional extraction/design dichotomy:** every `r>3` satisfying the symbolic outer-budget dominance inequalities.
- **Verified quantitative dominance with the stored exact seeds:** `r=12` only.
- **Unconditional all-sufficiently-large-r result:** not yet proved.

## Unique blocker

The blocker is now singular and quantitative:

> Prove an all-r or asymptotic low-order seed envelope strong enough that the recurrence closure satisfies
> `B_r(r-1-j,r^2-d-jr)>U_r(d,j)`
> for every outer state except the `4r+1` extraction and `5r+1` design terminal.

The recurrence architecture and its termination are no longer blockers.

## H+I Joint Audit — 2026-10-24

A rigorous hereditary multicolor-to-residual transfer lemma is now proved and documented in `ASYMPTOTIC_SEED_ENVELOPE.md`. The stronger target-color avoidance floor is valid on each induced residual, but the derived moment inequality currently supplies an upper constraint on its edge count rather than the lower edge floor needed by the recurrence. Therefore no general-r improvement to the five seed floors is claimed.

The outer-budget comparison has an exact symbolic gap formula in `OUTER_BUDGET_DOMINANCE.md`. With `a=r-1-j`, `t=r-d`, `n=ar+t`, and `b=t mod a`,
`U_r(d,j)-p_a(n)=C(r,2)-(a+1)t^2/(2a)+t-b(a-b)/(2a)`.
At `t=1`, the gap is exactly `C(r,2)`. The all-state dominance theorem and an explicit asymptotic threshold remain OPEN; no `r_0` is certified.


## Round 2 — Low-order cutoff advance (2026-10-24)

The new `LOW_ORDER_CUTOFF_THEOREMS.md` proves:
- `M_r(2)<=2r-1` for `r>=6`, using the inherited cap on the complement, a triangle-free maximum-degree bound, and the Andrásfai–Erdős–Sós theorem at the boundary `n=2r`.
- `M_r(3)<=3r` for `r>=6`, using a minimum-degree pivot to an `a=2` core and the exact inequality `2(r-1)p_r(n)>n(2r-1)`.
- Consequently the outer `t=1` states `(a,n)=(2,2r+1)` and `(3,3r+1)` are eliminated for `r>=6`.

The stronger `M_r(2)<=2r-1` claim is not all-r: explicit graphs in the abstract state contract show it fails at `r=4,5`. The `a=4,n=4r+1` coordinate remains the intended extraction terminal, not an unconditional exclusion. The five seed edge-floor excesses and all-state outer dominance remain OPEN; no EG617 threshold `r_0` is claimed.