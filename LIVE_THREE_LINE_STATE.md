# Live research state — 2026-10-23

This is the synchronized human-readable live state. It contains research results only, not agent prompts.

## Front end — T61

Canonical unconditional/retained closure remains `E397..E406 = EMPTY` under the stated contracts.

Delivered V11/V12 supersede the older source-level frontier. Independent archive replay of V12 in this assistant session is still pending because the local archive executor is failing at the client level.

Source-reported V12 state, conditional on the retained lower-order seeds:

- E407 maximum `Q=31` is excluded by V11;
- E408 maximum `Q=31` is excluded by V11;
- V12 proves the capacity inequality `Xi >= L + 2k - 2` for `k in {8,9,10}`;
- the common-K10 external pair-row union therefore carries at least 18 units of excess;
- the delivered V12 verifier reportedly replayed 8,677 weight assignments and 17,957 counting states;
- E407 maximum `Q=32` is reduced to five `rho=0` templates with a common regular `K11`;
- the unresolved V12 bridge is whether those five templates can coexist with one 284-edge core;
- E408 `Q=32,33` remain OPEN and are not closed by the E407 argument.

Thus the source-level front-end frontier is:

- E407: only `Q=32` OPEN, reduced to five common-K11 templates;
- E408: `Q=32,33` OPEN.

See `consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md` for the evidence boundary.

## High backend

### E333

`E333 = EMPTY` under the retained legal-backend/V4 forcing contract.

### E334..E337 — Astra-B line

V6 was independently replayed earlier. Delivered V7 was source-reported to force E334 to the unique `q=32`, `e(H)=211` CORE211 channel.

Delivered V8 now source-reports:

> `E334 = EMPTY`, relative to the retained backend and accepted V7 forcing.

The reported V8 closure is global rather than branch-by-branch: three independent degree-12 anchors split the 35-core into three large clique blocks plus at most four connectors, and at least two connectors each require at least two units of degree excess, contradicting the CORE211 total excess `K=2`.

This assistant independently proved the graph-theoretic partition part as `backend/GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`:

- connector count is exactly in `{2,3,4}`;
- connector signatures and clique-block sizes are completely classified;
- the remaining V8-specific local input is the connector-excess lemma, whose package replay is still pending here.

Therefore:

- source-level E334 status: `EMPTY` relative to retained backend/V7;
- independently re-certified interval in this assistant session remains E329..E333 until the V8 package replay succeeds;
- E335..E337 remain OPEN.

See `consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md`.

### Assistant-owned E338..E340

The K4,9 top-channel plateau family is empty. Low-decoration forcing gives q36=>G>=3, q37=>G>=2, q38=>G>=3; all q38,G=2 states are empty. q36 d4/d9 ceiling exchanges are empty.

q36 coverage splits into low-clique and shell-poor regimes. f=3 low-clique is CLOSED; hence f<=2.

#### q36 f=2, far 2K1, a_F=0 — CLOSED

`Q36_F2_2K1_A0_STAR_TERMINALS_FULL_CLOSURE.md` closes the last missing-star equality terminals. The entire `2K1,a_F=0` branch is EMPTY.

#### q36 f=2, far 2K1, a_F=1

Current synchronized layer status before the newest concurrent A4 refinements:

- c=7: CLOSED;
- c=8: A=2 and A=3 CLOSED; A=4 is the active higher-slack sector;
- c=9: A=2 and A=3 CLOSED; A=4,A=5 active;
- c=10: exact A=6 active.

Recent concurrent commits further reduce the A4 repeated-K3 sector, including elimination of disjoint repeated-K3 pairs and multiplicity-three residuals; the top-level theorem is not yet claimed closed.

#### q36 f=2, far target K2

Global d2 reduction gives, for c>=3, at most one d2 row. In c=8 with one d2 row:

- all seven d3 owners form one missing-set class;
- A=2 is CLOSED;
- A=3 multiplicity-four and multiplicity-three one-edge terminals are CLOSED;
- the multiplicity-three target-K3 sector is closed by the global mass contradiction;
- therefore c=8, one-d2, A=3 has support multiplicity at most2;
- A=4 remains OPEN.

Two intermediate far-K2 files that used an invalid K4-freeness assumption remain explicitly RETRACTED.

#### shell-poor / global compatibility

At least five one-spoke pivots carry 22-point anti-neighbourhoods Z with `110<=e_H(Z)<=122`, `alpha(H[Z])<=2`, and exact charge `q_v=133-e_H(Z)+g_a+e(D,A\{a})`.

The repository now also contains a unified global-support architecture: subcritical allowance decomposition, repeated-support dense-block bounds, matching/transversal extraction, fully-decorated escape analysis, signature-code compression, and one-spoke clique forcing. These are intended to replace E-number-by-E-number case enumeration wherever the forcing bridge is available.

## Global state

Independently re-certified closed backend interval in this assistant session: `E329..E333`.

Source-level closed backend interval after delivered V8: `E329..E334`, relative to the retained backend/V7 contract.

Remaining obligations:

- T61 E407 Q32: five common-K11 templates versus a single 284-edge core;
- T61 E408 Q32/Q33;
- backend E335..E340;
- independent replay of delivered V12/V8 packages when the archive executor becomes available.

The full EG617 r=12 theorem remains **OPEN / NOT_CERTIFIED**.