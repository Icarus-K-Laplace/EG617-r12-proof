# E407 Q32 — proof dependency audit

Date: 2026-10-27  
Status: **Current dependency ledger; E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.**

## A. Pure graph contract

Assume the frozen E407 core/support object:

- |H|=47, e(H)=284, alpha(H)<=4, omega(H)<=11, delta(H)>=12;
- sum_H(d_H-12)=4;
- U subset H, |U|=29, W=H\U, |W|=18;
- exact U/W edge ledger.

Pure consequences include the support omission-degree identity once the 49-block incidence counts are supplied, the W-side edge ledger, alpha(H[W])=4, and graph-theoretic consequences that explicitly cite no color-factor theorem.

The clique bound omega(H)<=11 is inherited from the T61 parent and is not implied by e(H)=284 alone.

## B. Labelled support contract

The minimum-support E407 boundary supplies 49 independent 4-set blocks on U, seven per exact-129 color class. They are disjoint within each color and pairwise linear across colors.

`SUPPORT_BLOCK_ANCHOR_IDENTITY.md` proves, under the frozen exact-129 factor/minimum-support identity, that every selected support block is the H-four-set of a selected isolated exact-color K5 component and has a genuine anchor in {p} union A.

This resolves the previous firewall for the **selected 49 blocks**. It does not identify every auxiliary no-S component witness with a selected support block.

## C. Exact-129 factorization dependency

The following newest results are conditional on the registered exact-129 Type-I factor theorem:

1. `SELECTED_B_ANCHOR_FLOOR.md`: every exact color has b_c in {5,6,7}; b_c=5 forces selected anchors p + one S + five B; every exact color has at most one selected S anchor.
2. `SHELL_COLOR_EDGE_LOAD.md`: every exact color owns at least two shell missing edges whose endpoints are unselected by that color.
3. The 26-vertex residual identity `3K5 + G11` after deleting the seven selected K5 components.

The factor theorem gives ten isolated K5 components plus an 11-vertex exceptional gadget whose color independence number is two. These statements are not pure consequences of the 284-edge target core.

The new b_c>=5 proof uses only this factorization, the selected-component identity, B being a target K10, and p being target-adjacent to the shell. It does **not** use Brouwer, Didin, or any low-delta W-profile theorem.

## D. Row-transversal / lower-order dependencies

The registered row-transversal theorem for a missing shell edge uses retained lower-order inputs including R(3,35) / R(2,24) exclusions under its stated hypotheses. Whenever a proof says a selected S-anchored block must hit a B row, or invokes the repaired A/C hub-complete component capacity, that lower-order dependency must be recorded.

The direct six-set lemma is sufficient only when the independent Q is known anticomplete to both shell endpoints in question. It may not be silently substituted for the stronger row-transversal theorem.

## E. Brouwer / Kang–Pikhurko / Turan dependencies

- Brouwer second-Turan results are used in several four-partite/non-four-partite profile reductions; exact hypotheses and equality thresholds must be retained.
- Turan equality is used in exact W-profile classifications.
- Kang–Pikhurko equality classifications are used in registered non-four-partite extremal branches and in the exact-129 factor interface as recorded by the source theorem stack.

No new result in Rounds 13–15 upgrades any external theorem dependency to a self-contained proof.

## F. Didin-dependent delta=14 saturated branch

The delta=14 non-four-partite K5-saturated branch remains only **PROVED_CONDITIONAL**. Its alpha-critical reduction invokes the theorem stated in Maksim Didin's 2026 author-prepared preprint concerning graphs with fixed independence number and the maximum number of components of a spanning alpha-critical subgraph.

This workstream has checked the dependency statement and source metadata, but has not independently re-proved the external theorem. Therefore this branch must not be labelled unconditional.

## G. V12 finite screen

The supplied V12 certificate has been independently replayed in sibling work. It certifies the finite state coverage and reduction of E407 Q32 survivors to five rho=0 shell templates under the analytic screen/lower-order contracts.

It does **not** prove:

- that every analytic screen theorem is self-contained;
- that any completed parent graph exists;
- that the five templates are impossible against the same legal 284-edge core.

The current workstream treats A–E as exhaustive only under that retained V12 dependency chain.

## H. Original K145 bridge

The original balanced K145 counterexample -> legal residual/T61 chain is outside the local E407 core theorem. Main/root state still treats the full theorem as NOT_CERTIFIED and retains additional obligations beyond E407.

Closing E407 Q32 would therefore not, by itself, certify EG617(r=12).

## I. Route-audit correction

`SHELL_LIST_RELAXATION_AUDIT.md` proves that the newest shell-only constraints have a coarse label relaxation for every M with at least fourteen edges. This is not a graph counterexample; it certifies that a terminal proof must use support/core/row geometry rather than rearranging the same shell scalar constraints.

## J. Current dependency-safe conclusion

The highest-leverage unresolved implication is:

> combine the genuine selected support-component labels, the b_c>=5 anchor theorem, exact D_a row constraints, support-block disjointness/linearity, residual 3K5+G11 factors, and the same four-excess 284-edge H into a contradiction for each A–E template.

No step in this workstream is allowed to treat the Didin-dependent branch, V12 analytic screen, or original K145 bridge as unconditional merely because a local verifier passes.
