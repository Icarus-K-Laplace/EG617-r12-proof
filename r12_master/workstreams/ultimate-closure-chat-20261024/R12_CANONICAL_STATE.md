# R12 canonical state — 2026-10-24

## Headline status

**EG617(r=12): OPEN / NOT_CERTIFIED.**

Target: every 12-edge-coloring of K145 has a 13-vertex set missing a color. No complete contradiction has been established in this workstream.

## Repository provenance

- Repository: Icarus-K-Laplace/EG617-r12-proof
- Workstream branch: workstream/r12-ultimate-closure-20261024
- Base main HEAD at branch creation: 22cc93df4fab06ac9761e682ac06746ac42f69f4
- Allowed path: r12_master/workstreams/ultimate-closure-chat-20261024/
- The branch did not exist before creation; it was created from main, not from either Astra branch.

## Current evidence table

| Obligation | Current status | Scope / qualification |
|---|---|---|
| Contextual R(4,49) exclusion | PROVED_CONDITIONAL | Short counting contradiction under the exact F5 residual contract and cited second-Turan theorem; arithmetic independently checked in this workstream. |
| Original counterexample to embedded T61 reduction | PROVED_CONDITIONAL / SOURCE_REPORTED | FRONTEND_BRIDGE_THEOREM F6–F8 plus contextual R(4,49) exclusion. The T61 terminal is not eliminated. |
| T61 E397–E406 | CANONICAL_CLOSED per repository | The repository supplies proof bodies/contracts; this workstream has not rerun the historical recurrence archive. |
| E407, sharp |W|=23 Cell-B | PROVED_RELATIVE_TO_EXTREMAL_INPUTS | E407_CELL_B_FULL_CLOSURE excludes this specific Cell-B completion only. |
| E408, sharp |W|=23 Cell-B | PROVED_RELATIVE_TO_EXTREMAL_INPUTS | Excluded by global target maximum degree at most 19 versus Cell-B degree 20. |
| E407 Q32 | OPEN | V12 finite screen independently replayed: 8,677 weight vectors, 17,957 count states, 1,984 labelled shells, 554 OPEN entries covered by five rho=0 templates. The common regular K11 / same 284-edge core completion remains unproved. |
| E408 Q32 / Q33 | OPEN | Q32 has a 285-edge core (excess 6); Q33 has a 284-edge core (excess 4). Seven-block constraints and Q33 exact budgets remain necessary conditions, not contradictions. V12 does not certify exhaustive E408 coverage. |
| Global support-compatibility theorem | PROVED_ANALYTIC under contract | Requires a legal common-S owner system, row closure, boundary one-loss, and low-cross hypotheses where invoked. |
| Forcing-to-master Bridge A | OPEN | No exhaustive derivation from every legal shell survivor to anchors / master contract / finite residue has been verified. |
| Shallow-loss Bridge B | OPEN | d2 higher-slack and d3 non-triangular-missing-set residues remain. |
| Abstract backend E333–E340 | MIXED / OPEN | E333 is conditional on retained forcing; E334 package-level closure is source-reported pending replay; E335–E340 remain open in the abstract backend program. |
| Original theorem | OPEN / NOT_CERTIFIED | The T61 terminal remains the live obstacle if the contextual R(4,49) exclusion contract is valid. |

## Strongest reusable graph theorem

For a 35-vertex core H with alpha(H) <= 3, omega(H) <= 11, delta(H) >= 12, three pairwise nonadjacent degree-12 vertices force

K = sum_v (d_H(v)-12) >= 8,

hence e(H) >= 214. This is the contract of GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md. It does not create the three anchors in an arbitrary shell survivor.

## Important stale-state reconciliation

The main-branch summaries are not synchronized:

- CANONICAL_STATE.md (dated 2026-10-22) retains the older CORE211 floor.
- LIVE_THREE_LINE_STATE.md includes intermediate e(H) >= 213 / q <= E-304 statements.
- OPEN_FRONTIERS.md and GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md support the stronger e(H) >= 214 / q <= E-305 bound under the three-anchor contract.
- GLOBAL_SUPPORT_COMPATIBILITY_MASTER_THEOREM.md still states the weaker e(H) >= 213 branch. That weaker bound remains valid but is not the strongest bound and must not overwrite the stronger theorem.

## Certification rule

No status is promoted because a report says CLOSED. A result is promoted only after its precise contract, source proof, dependency scope, and any computation certificate are checked. The full theorem stays OPEN until the T61 terminal is excluded and the proof DAG has no unproved edge.

## Round-2 proved cross-cutting lemma

Added R12_SHELL_CORE_WITNESS_LEMMA.md (commit 020b64d5fdf3a4aa3abe66d86be3489565760b22).

Under the retained T61 contextual contract:
- any shell row of size t_a<=7 has an independent 4-set in the 47-core anticomplete to that shell vertex;
- at least eight of the thirteen shell vertices are good in this sense, because bad vertices form an independent set in F[A];
- in the retained E408 Q33/d3 interface, the exact budget beta+X+G_B=3 forces every one of the ten B-vertices to be good;
- each such witness Q_b must hit every support row N_H(a) for which ab is a missing target edge. At least five B-witnesses hit at least two S-rows.

This is a proved compatibility constraint, not a terminal exclusion. EG617(r=12) remains OPEN / NOT_CERTIFIED.


## New witness-capacity cross-cut (2026-10-24)

R12_WITNESS_CAPACITY_CROSSCUT.md proves a universal three-shell-row support lemma for every independent 4-set in H, a hub vertex-cover rule for each Q_b witness, and a defect-sensitive extension lemma for independent triples in H_b. For E408 Q33, it also derives at least five no-S K5-component witnesses per exact-129 color and a 7-beta lower bound on their hub-row hits. These are necessary-structure theorems only; no E407/E408 terminal is eliminated.

The V11 and V12 archives were independently replayed from the Library-delivered ZIPs; SHA256SUMS passed and both independent verifiers returned COMPUTATION_CERTIFIED. See R12_V11_V12_REPLAY.md. This certifies finite enumeration coverage only, not analytic completion exclusion.

Arithmetic correction: E408 Q32 has e(H)=285 and core excess 6; the 284-edge / excess-4 core is E407 Q32 and E408 Q33.
