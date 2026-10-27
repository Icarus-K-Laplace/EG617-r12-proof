# Dependency audit — fixed r=12 root closure

Updated: 2026-10-27
Status: **root chain closed conditionally; finite coverage computation-certified; no OPEN graph terminal identified.**

## 1. Separation of proof classes

This audit uses four distinct proof classes and does not conflate them.

### Analytic `PROVED` / `PROVED_CONDITIONAL`
Ordinary mathematical derivations under explicit hypotheses.

### `COMPUTATION_CERTIFIED`
Exact finite enumeration / recurrence / state-coverage claims checked by deterministic integer verifiers. A verifier does not by itself certify graph nonexistence unless an analytic theorem maps the finite states to a contradiction.

### External theorem input
Published/extant extremal or Ramsey statements imported with their exact hypotheses. They are not re-proved merely because a local script passes.

### Source-freeze pending
A theorem/interface may be mathematically registered in the project but still lack a branch-local frozen source statement/hash in the final root receipt. This is a proof-engineering obligation and must not be silently treated as formal verification.

The current root promotion therefore remains `PROVED_CONDITIONAL + COMPUTATION_CERTIFIED`, not bare `PROVED`.

## 2. Front-end root dependency

`FRONTEND_BRIDGE_THEOREM.md` proves the dichotomy

\[
\text{balanced K145 counterexample}
\Rightarrow
\text{contextual }R(4,49)\text{ or embedded T61}.
\]

The finite Line-A recurrence is computation-certified:

- package SHA256 `8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac`;
- 1,752 recurrence nodes;
- 144 outer comparisons;
- 73 manifest files checked with zero errors;
- independent replay PASS;
- unique no-R(4,49) stop `(11,6,5,61)`, edge interval397..408.

The historical receipt's `bridge_status=OPEN` reflected the then-unresolved T61 terminal; it is not evidence of a failed recurrence.

The contextual R(4,49) alternative is excluded by the current full-color theorem relative to its named Brouwer/extremal input.

The old `front_end/ASSUMPTION_LEDGER.md` still lists T61/MAIN and several superseded bridge candidates as OPEN. This branch-local root proof does not consume the OPEN K7/K8/S31MAP/S31NEXT/S27MAP/S30MAP/S30REM rows.

## 3. T61 structural split

- h12 is excluded by `T61_H12_CLOSURE.md`.
- h13 E397--E400 are excluded by `T61_H13_LOW_LAYER.md`.
- E401--E404 are excluded by the canonical closure.
- E405 is excluded.
- E406 is excluded.

Thus only E407/E408 remain before the new workstream results.

## 4. E408 whole-layer dependency

The shortest E408 proof is now `E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md`.

It does not depend on q, a 284/285-edge core, support size, or seven outer blocks.

Load-bearing inputs:

1. genuine 61-point h13 T61 residual with E=408;
2. each non-target residual color has alpha<=12 and omega<=5;
3. the 129-edge lower bound and exact-129 Type-I equality structure;
4. registered pointwise degree floors for 130/131/132-edge colors;
5. Brouwer/Kang--Pikhurko second-Turan inequalities on the induced 58-,57-,53-point subgraphs;
6. Turan's p8(49) floor;
7. unique edge ownership and total residual vertex degree60.

The residual edge partition gives sum s_C=3 and exact count m in {8,9,10}. The low-degree capacity lemmas exclude all three values. Therefore E408 is conditionally impossible as an entire energy layer.

The earlier Q32/Q33 terminal closures remain valid independent audits but are no longer load-bearing in the shortest root chain.

## 5. E407 low-charge reduction

For a degree-13 E407 pivot,

\[
407=91+q+e(H),\qquad e(H)\ge284,
\]
so q<=32.

The audited V9 chain reduces maximum charge to Q in {31,32}, relative to retained seeds. The current front-end assumption ledger marks the small Ramsey/core seed statements consumed by V9 as `PROVED`. V9's finite tables remain computation-certified.

## 6. E407 Q31 dependency

The original V10/V11 archives were independently materialized, hash-checked before execution, and replayed.

### V10
- archive SHA256 `e83e2907d541b38304746e855af52b5e21b6500a35cb0fdb676a4f6a7601303a`;
- fresh manifest: all PASS;
- replay: 12 labelled cuts,16 local-neighbourhood cases,14 row-budget cases,1 shell witness;
- analytic result: Q31 regular d3/d10 incidence branches excluded.

The package contains the V8 flat-boundary exchange proof it consumes. It is not merely a source-status pointer.

### V11
- archive SHA256 `27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4`;
- fresh manifest: all PASS;
- 684 kernel weights;
- 349 outside-count states;
- 259 labelled necessary shells;
- Family A=252, Family B=7;
- certificate SHA256 `0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b`.

The finite package proves coverage, not nonexistence. Analytically, `NINE_D2_SUPPORT_CAPACITY.md` excludes both families via common-K10 pair-row capacity, support union at least17, and a zero-capacity matching whose complement yields an independent set at least7>5.

Therefore E407 maximum Q31 is `PROVED_CONDITIONAL` with finite coverage `COMPUTATION_CERTIFIED`.

## 7. E407 Q32 finite coverage

Original V12 archive:

- SHA256 `0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36`;
- fresh package manifest: all PASS;
- 8,677 kernel weights;
- 17,957 count states;
- 1,984 labelled necessary shells;
- 90 d3/rho1 exclusions;
- 1,192 near-K12 exclusions;
- 148 K9 pair-row refinements;
- 554 finite-screen survivors;
- all 554 map to the five V12 rho=0 d3 shell templates;
- certificate SHA256 `cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30`.

The V12 package alone does not exclude the 554 survivors.

## 8. E407 Q32 analytic completion interface

The active E407 sibling is read-only to this workstream. Its later analytic files establish the shared completion contract for the five V12 templates:

- same 47-point,284-edge core H;
- same support U with |U|=29;
- 49 selected independent 4-set blocks;
- seven blocks in each of seven distinct selected exact-129 colors;
- disjointness within color and pairwise linearity across colors;
- `e(overline(H[U]))=294+delta` with `delta<=16`.

`SUPPORT_BLOCK_ANCHOR_IDENTITY.md` proves under the registered exact-129 factor/minimum-support interface that every selected block is genuinely the four-core part of a monochromatic selected-color K5. This is the critical label bridge.

The root closure is conditional on this registered factor/support interface. It does not pretend the selected-block label theorem is a pure consequence of the 284-edge graph alone.

## 9. E407 Q32 decisive one-color capacity contradiction

Let `L_U=overline(H[U])`.

The 49 selected blocks contribute exactly

\[
49\binom42=294
\]

distinct selected-color edges in L_U.

There are eleven non-target colors total and only seven selected colors. Choose one unselected non-target color D. Then

\[
\alpha(D[U])\le12,
\]
so Turan gives

\[
e_D(U)\ge p_{12}(29)=22.
\]

By unique edge ownership these D-edges are disjoint from the selected294. Hence

\[
e(L_U)\ge294+22=316.
\]

But the frozen support ledger gives

\[
e(L_U)=294+\delta\le310.
\]

Contradiction, with exact gap six.

The independent arithmetic replay recomputes `p_12(29)=22`, `selected_edges=294`, `available_total=310`, `one_color_required=316`, and the six-edge gap. The older four-color aggregate `382>310` remains a regression check but is no longer load-bearing.

This shortest route does not use:

- Didin's delta=14 result;
- five-template row-by-row casework;
- the auxiliary E407 seven-exact-color theorem;
- exceptional-vertex degree arguments;
- E408 Q32/Q33 identities;
- support-41.

## 10. Contract firewalls retained

- Q33 284-edge and Q32 285-edge ledgers remain separate.
- E407 uses its own 284-edge V12 support contract.
- Support-31, support-41, support-44/47 are not interchanged.
- The historical false claim “a monochromatic K12 has no same-color external edge” is not used; the valid bound is at most one.
- No scalar feasible table is treated as a graph realization.
- No absence-of-candidates search is promoted without an exhaustive finite certificate and analytic mapping theorem.

## 11. Root promotion status

Under the named dependencies:

- contextual R(4,49): closed;
- T61 h12: closed;
- h13 E397--E406: closed;
- E408: closed;
- E407 Q31: closed;
- E407 Q32: closed.

Therefore no graph terminal remains in the audited root chain.

Current theorem label:

\[
\boxed{\text{EG617 fixed }r=12:\ \text{PROVED_CONDITIONAL + COMPUTATION_CERTIFIED}.}
\]

The remaining obligations are certification/presentation obligations unless a source-freeze audit discovers a hidden premise: clean-environment package replay, frozen external theorem statements, exact source freeze for the Type-I factor/support interface, cross-workstream merge review, and ideally formalization. They are not currently identified as additional graph cases.
