# E408 root promotion and single-terminal reduction

Updated: 2026-10-27
Status: **PROVED_CONDITIONAL REDUCTION**. This file does not claim EG617(r=12) solved.

## 1. Purpose

This file composes the independently registered front-end reductions with the two E408 terminal closures proved in this workstream. The goal is to identify the smallest remaining T61 frontier that any hypothetical balanced 12-coloring of K145 must reach.

All sibling workstreams are read-only. The only new claims here are logical compositions of named source theorems; no sibling proof body is rewritten.

## 2. Root-to-T61 entry

Assume a hypothetical balanced 12-edge-coloring of K145 and choose a least-edge target color G.

The current front-end bridge gives the contextual dichotomy

- an induced contextual R(4,49), or
- an embedded 61-point T61 residual R with 397<=E=e(R)<=408 and minimum degree 12 or 13.

The contextual R(4,49) branch is impossible by `CONTEXTUAL_R449_FULL_COLOR_IMPOSSIBILITY.md`, relative to the stated F5 contract and Brouwer's second-Turan theorem. Hence any surviving counterexample enters T61.

The degree-12 T61 branch is independently closed by `T61_H12_CLOSURE.md`. Therefore every surviving T61 has

\[
\delta(R)=13.
\]

## 3. Energy layers below 407 are already empty

Under the explicit T61 hereditary-cap h13 contract:

- E397--E400 are closed by `T61_H13_LOW_LAYER.md`;
- E401--E404 are `PROVED EMPTY` by `E401_E404_CANONICAL_CLOSURE.md`;
- E405 is `PROVED EMPTY` by `E405_FULL_CLOSURE_CANONICAL.md`;
- E406 is `PROVED EMPTY` by `E406_FULL_CLOSURE.md`.

Thus every surviving T61 counterexample must satisfy

\[
E\in\{407,408\}.
\]

## 4. Charge ceiling at E408

Fix an E408 h13 T61 residual. For any degree-13 pivot p with 13-shell and 47-core H_p,

\[
408=91+q_p+e(H_p).
\]

The universal 47-core floor is

\[
e(H_p)\ge284.
\]

Therefore

\[
q_p\le33.
\]

Because the minimum degree is exactly 13, degree-13 pivots exist. Let

\[
Q=\max\{q_p:d_R(p)=13\}.
\]

Then the exhaustive charge partition is

\[
Q\le31,\qquad Q=32,\qquad Q=33.
\]

No other E408 h13 charge branch exists.

## 5. E408 branch Q<=31

The retained V11 analytic package reports, under its explicit lower-order seed contract, that E408 with maximum charge Q<=31 is excluded. Its finite kernel certificate has also been independently replayed in `R12_V11_V12_REPLAY.md`:

- 684 kernel weight assignments;
- 349 outside-count states;
- 259 labelled necessary shells;
- 252 Family-A and 7 Family-B states;
- completed parent graphs claimed: 0;
- certificate SHA256 `0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b`.

The finite replay certifies the supplied state coverage; the analytic screen rules and retained lower-order seeds retain their named hypotheses. Accordingly this branch is imported as **PROVED_CONDITIONAL / COMPUTATION_CERTIFIED interface**, not as an unconditional theorem reconstructed here.

## 6. E408 equality automatically supplies the seven-block global contract

The generic T61 bridge historically did not automatically turn every T61 into seven unanchored K12 blocks. At E408, however, this gap is eliminated by `E408_GLOBAL_SEVEN_BLOCK_EQUALITY_SYSTEM.md`.

The exact outer ledger is

\[
E+\sigma+z+g+x_6+y_6=408,
\]

with all displayed charges nonnegative. Setting E=408 forces

\[
\sigma=z=g=x_6=y_6=0.
\]

Hence the target graph splits exactly into seven isolated target K12 blocks plus the 61-point E408 residual. Moreover every one of the twelve colors has exactly 870 global edges. For every non-target color C,

\[
e_C(R)=129+s_C,\qquad s_C\ge0,
\]
\[
P_C+R_C+s_C=62,
\]
\[
\sum_C s_C=3,\qquad \sum_C P_C=252,\qquad \sum_C R_C=427.
\]

Therefore the seven-block/exact-residual color ledger used in the Q32 and Q33 workstreams is not an extra E408 hypothesis: it is forced by E=408.

## 7. E408 Q=32 is impossible

Assume Q=32 and choose a degree-13 pivot p with q_p=32. Then

\[
e(H_p)=408-91-32=285,
\]

so the registered Q32 core has 47 vertices, 285 edges and total degree excess six above minimum core degree 12.

The decisive result `Q32_EXACT_COLOR_COUNT_COLLAPSE.md` does not require the later support-size reductions. Under the seven-block equality system, exact-129 Type-I classification, exceptional-vertex injectivity, the registered pointwise degree floors and the Brouwer--Kang--Pikhurko second-Turan input, the number m of exact-129 non-target colors lies in {8,9,10}, while each possibility is impossible:

- m=10 forces at least ten degree-two vertices in the sole 132-edge color, but such a color has at most nine;
- m=9 forces at least nine degree-three vertices in the 130-edge color, but such a color has at most four;
- m=8 forces at least sixteen degree-three incidences across three 130-edge colors, but their total capacity is at most twelve.

Thus

\[
\boxed{E408,\ Q=32\text{ is PROVED_CONDITIONAL impossible}.}
\]

No Q33 284-edge identity is used.

## 8. E408 Q=33 is impossible

Assume Q=33 and choose a degree-13 pivot p with q_p=33. Then

\[
e(H_p)=408-91-33=284.
\]

The registered Q33 reduction places every surviving Q33 completion into the 31-point / 56-labelled-witness minimum-support terminal, split historically into four-partite and non-four-partite branches.

This workstream proves in `Q33_NONEXACT_U_RESERVE_CLOSURE.md` that this entire registered terminal is impossible. Briefly, after excluding m=10 exact colors and writing h for the number of selected gadget witnesses,

\[
26(11-m)\le \delta+6h,
\]

while

\[
\delta\le17,\qquad h\le4,
\]

so the right side is at most 41. The surviving m=9 and m=8 branches require 52 and 78 edges respectively. Contradiction.

Hence

\[
\boxed{E408,\ Q=33\text{ is PROVED_CONDITIONAL impossible}.}
\]

No Q32 285-edge identity is used.

## 9. E408 energy-layer exhaustion theorem

Sections 4--8 form an exhaustive partition of every E408 h13 T61 residual:

\[
Q\le31\quad\text{or}\quad Q=32\quad\text{or}\quad Q=33.
\]

The first branch is excluded by the retained V11 package relative to its named assumptions; the second by the Q32 exact-color-count contradiction; the third by the Q33 nonexact-U reserve contradiction.

Therefore:

> **Theorem E408-EXHAUST.** Under the explicit front-end T61 contract, the retained V11 lower-order/analytic inputs, the E408 seven-block equality theorem, the exact-129 Kang--Pikhurko Type-I classification, and the extremal theorems cited in the Q32/Q33 proofs, no E408 T61 parent exists.

Status: **PROVED_CONDITIONAL**.

This is stronger than the previous statement that the registered Q32 and Q33 terminals were separately closed: it verifies that the charge partition feeding those terminals is exhaustive and that the generic seven-block bridge gap vanishes at E408.

## 10. Root single-terminal reduction

Combine:

1. contextual R(4,49) impossibility -> every original counterexample enters T61;
2. T61 h12 closure -> h=13;
3. E397--E406 closures;
4. E408-EXHAUST above.

Every surviving original counterexample must therefore have

\[
\boxed{E=407,\quad \delta(R)=13.}
\]

For E407, the same pivot identity and 47-core floor give

\[
407=91+q_p+e(H_p),\qquad e(H_p)\ge284,
\]
so
\[
q_p\le32.
\]
Let Q be the maximum charge over degree-13 pivots. The retained V11 package excludes E407 with Q<=31 under its named assumptions. Hence any surviving counterexample must satisfy

\[
\boxed{E=407,\quad h=13,\quad Q=32.}
\]

The independently replayed V12 E407-Q32 finite certificate reduces that branch to 554 open labelled shell states covered by five rho=0 regular-d3 templates. Replay data:

- 8,677 kernel weight vectors;
- 17,957 count states;
- 1,984 labelled necessary shells;
- 90 excluded by D3/rho=1;
- 1,192 by near-K12 capacity;
- 148 by K9 pair-row completion;
- 554 remain open;
- certificate SHA256 `cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30`.

The active E407 workstream currently identifies the live mathematical blocker as compatibility of those five V12 shell templates with one common 284-edge core and the labelled exact-color support-row system.

Thus, relative to the named front-end and retained-seed interfaces, the fixed-r=12 original problem has been reduced to a **single live T61 terminal family**:

\[
\boxed{\text{E407 / h13 / maximum Q32 / V12 five-template common-core compatibility}.}
\]

Status: **PROVED_CONDITIONAL REDUCTION**, not contradiction.

## 11. What remains open

This file does **not** prove EG617(r=12). The live obstruction is E407 Q32. In particular:

- the 554 V12 states are not claimed unrealizable;
- the five template families are not all excluded against the same 284-edge core;
- V11/V12 analytic screening rules retain their lower-order assumptions even though the finite certificates replay;
- external Brouwer/Kang--Pikhurko inputs retain their stated hypotheses;
- no sibling E407 status is silently promoted.

A complete r=12 proof now requires closing the E407 Q32 five-template/common-core compatibility theorem, plus a final dependency audit confirming every retained seed used by the root chain at its claimed status.

## 12. Source heads frozen for this composition

- front-end / V11/V12 audit source: `workstream/r12-emergency-sprint-chat-20261025` at `5258c5fe17af3bf17eb7a2bfb08315c9be9116cd`;
- E408 Q33 source: `workstream/r12-e408-q33-global-compat-20261025` at `0cb2ff3968f005c9cb255958df7c02b220678701`;
- E408 Q32 source: `workstream/r12-e408-q32-excess6-20261025` at `a0ba6db26c7e8b00a4217dcbcbf298895dff93ce`;
- active E407 sibling observed at `workstream/r12-twochat-e407-closure-20261026` commit `2e2e6d15df12c61f7fd15e27e74afd2887ddeb41`.

The E407 sibling remains read-only to this workstream.
