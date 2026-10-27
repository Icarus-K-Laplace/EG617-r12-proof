# E407 Q32 — open contracts

Date: 2026-10-27  
Status: **OPEN / NOT_CERTIFIED. This file lists the minimum remaining obligations after the latest selected-anchor and shell-edge theorems.**

## C1. Five-template same-core labelled support-row incompatibility — primary blocker

For each V12 template A–E, show that no single E407 core/support object can satisfy simultaneously:

- |H|=47, e(H)=284, alpha(H)<=4, omega(H)<=11, delta(H)>=12, total core excess four;
- U of size29, W of size18, and the exact U/W edge ledger;
- 49 selected support blocks, seven per each of seven exact-129 colors, disjoint within color and pairwise linear;
- each support block being the H-four-set of a selected exact-color K5 component;
- selected anchor counts b_c in {5,6,7};
- at most one selected S-anchor per exact color;
- the exact template row sets D_a and missing-edge row-transversal constraints;
- the residual exact-color factor 3K5+G11 after deleting the selected seven K5 components;
- edge-color uniqueness and the four-unit H degree-excess distribution.

This is the unique highest-leverage global E407-Q32 contract.

## C2. Shell-only closure is certified insufficient

Do not attempt to close C1 from only:

- b_c>=5;
- at most one selected S anchor;
- at least two unselected shell edges per exact color;
- shell edge uniqueness.

`SHELL_LIST_RELAXATION_AUDIT.md` constructs a coarse label relaxation for any shell missing graph with at least fourteen edges. All five V12 templates pass this relaxation. A valid terminal proof must use U/H/row/component structure.

## C3. Actual selected high-k blocks

The selected 49-block system, not merely auxiliary component witnesses, satisfies:

- A: at least 7 selected k=3 B-anchored blocks globally;
- B: at least 21 selected k>=2 B-anchored blocks;
- C: at least 7 selected k=3 B-anchored blocks;
- D: at least 14 selected high-k B-anchored blocks;
- E: no positive high-k floor follows from anchor-cardinality intersection alone.

A/C blocks above are hub-complete; B/D blocks hit at least two S rows. The remaining problem is capacity/compatibility inside the same support/core incidence object.

## C4. Low-delta terminal

Still open independently of C1:

- delta=13, four-partite epsilon_U=0;
- delta=13, non-four-partite for all feasible epsilon_U not otherwise excluded;
- every delta<=12 case.

The registered delta=13 classifications may not be extrapolated to delta<=12.

## C5. Minimum-slack fork

At (delta,epsilon_U)=(3,3) or (4,1), if a slack-one independent W-four-set exists, `MINIMUM_SLACK_EXACT_CORE.md` gives a finite exact four-partite U kernel. Otherwise every independent W-four-set has slack at least two. Neither branch is globally excluded.

The new selected-anchor theorem applies to both branches and should be incorporated into any finite kernel analysis.

## C6. Delta=14 conditional dependency

The non-four-partite K5-saturated delta=14 branch remains conditional on the Didin 2026 preprint theorem used by the alpha-critical reduction. A terminal E407 proof cannot call this branch unconditional without independently discharging that dependency or replacing it.

## C7. V12 exhaustiveness dependency

The five templates cover the finite-screen survivors only under the retained V12 analytic/lower-order contracts. Finite replay alone does not certify every analytic screen theorem. This dependency remains in the parent chain.

## C8. Original K145 bridge

Even a complete E407-Q32 closure is only one local T61 obligation. The original K145-to-T61/legal-residual proof chain, E408, and root backend obligations must be assessed separately before claiming EG617(r=12).

## Current minimal theorem statement sought

> **E407 Q32 Same-Core Labelled Compatibility Theorem.** Under the frozen E407 Q32 parent contract and retained V12 screen hypotheses, none of shell templates A–E admits seven exact-129 selected-component classes on a common 29-point support U and 284-edge core H satisfying the selected-anchor, row-transversal, residual-factor, edge-uniqueness, and four-excess constraints.

Proving this theorem would close the five-template global compatibility obstruction, but the conditional delta=14 dependency and parent/root proof chain would still require an audit before a full EG617 claim.
