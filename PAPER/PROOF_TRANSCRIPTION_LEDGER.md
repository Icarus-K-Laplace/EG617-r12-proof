# Proof-transcription ledger

**Manuscript branch:** `workstream/r12-paper-full-manuscript-20261031`  
**Frozen integration source:** `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`  
**Independent AI-assisted audit:** `09a88cc4fe1e2cf1f3a87475d6484f681910b23e`  
**Q30 adversarial report:** `a0f922ad09af99575bae581864b673aa4d41f00d`

This ledger records the provenance of every mathematical section. It is deliberately separate from theorem-status labels: a source file marked PROVED is not, by that label alone, evidence that the manuscript transcription is complete.

| Manuscript file | Frozen mathematical source | Coverage in this draft | Remaining work |
|---|---|---|---|
| `sections/01-introduction.tex` | Erdős–Gyárfás (1999); Xia–Szeider (2026); `FINAL_GLOBAL_PROOF.md` | Problem statement, fixed-r=12 contribution, scope and proof roadmap | Expand literature review; verify priority/history immediately before submission |
| `sections/02-setup.tex` | `K145_TO_T61_FRONTEND_AUDIT.md`, §1 | Balanced-coloring definition, Turán cap, D(n), graph class | Check every cap value against an independent short script |
| `sections/03-frontend.tex` | `K145_TO_T61_FRONTEND_AUDIT.md`; `frozen/frontend/RECURRENCE_PROOF.md`; `frozen/frontend/CONTEXTUAL_R449_FULL_COLOR_IMPOSSIBILITY.md` | Minimum-degree pivot, K12 packing, exact edge ledger including the z term, contextual 49-set contradiction, recurrence rules and unique T61 stop | Machine-readable `FRONTEND_REPLAY.json` and two recurrence implementations are bundled under `supplement/frontend/`; the integrated root verifier is runnable from `supplement/root/` and clean CI now reruns all three recurrence implementations over 1,752 nodes and 144 outer stops. Preserve fresh output hashes with the CI artifact |
| `sections/04-lower-order.tex` | `frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md`; `frozen/low/COMMON_NEIGHBORHOOD_CAPACITY.md`; `LOW_EDGE_AND_286_THEOREM_AUDIT.md` | R(2,24), 23-point triangle-free classification, cost-12 lemma, R(3,35/36/37), 47-point degree gate, CORE211, common-neighborhood capacity | The self-contained 121/122 classification and low-edge verifier are bundled in `supplement/root/frozen/low/`; a raw standalone export of all 61 representatives remains outstanding |
| `sections/05-low-edge.tex` | `frozen/low/DIRECT_UNIFORM_PROOF.md`; `frozen/low/LOW_EDGE_UNIVERSAL_THEOREM.md` | Total-excess-six independent four-set, private cliques, all h=3,4,5 support patterns, common-neighbor blocker | Add explicit elementary verification of the displayed scalar inequalities and the complete support-orbit table |
| `sections/06-equality.tex` | `frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md` | Total-excess-eight reduction, ten support orbits, common-neighborhood bound, scalar charges, all terminal patterns, 286 exclusion and 287 floor | Expand the scalar inequality case splits and each shared-leaf incidence calculation; verify every orbit against the frozen verifier |
| `sections/07-h12.tex` | `H12_AND_EXCEPTIONAL_PARENT_AUDIT.md`; `front_end/R448_FLOOR310.md`; `front_end/T61_H12_CLOSURE.md` | R(4,48) degree gate, q20 shell classification, inserted-center contradiction, 310 floor, h12 exclusion | Include the complete five q20 equality adjacency lists in supplementary data and independently check every repivot degree |
| `sections/08-cover.tex` | `frozen/cover/COVER_THEOREM.md`; `COVER_INDEPENDENT_AUDIT.md`; certification `COVER_ANALYTIC_CERTIFICATE.md`; E407/E408 root certificates | Exact pivot identities, Q27/Q28 reduction, finite-state map, Q29 promotion, Q30 Families I/II, E407/E408 contradictions | Verifier, case matrix, analytic source, and Q30 adversarial report are bundled under `supplement/cover/`; CI now independently reruns the verifier and records the two/eight canonical states. A separate canonical-state key export remains outstanding |
| `sections/09-global-and-computation.tex` | `FINAL_GLOBAL_PROOF.md`; `VERIFICATION_RESULT.json`; certification report and replay outputs | Final contradiction and precise finite-computation trust boundary | Selected scripts, inputs, outputs, source manifests and checksums are bundled under `supplement/`; CI now emits a source ZIP artifact and clean verifier replay. Explicit q20 adjacency-list and raw 61-representative exports remain open |

## Status of source-derived claims

- The theorem statement and all graph contracts are pinned to the integration commit above.
- The exact 47-point graph-only theorems do not assume hereditary caps; the parent-level ℛ(4,47) floor does.
- The contextual (R(4,49)) lemma uses the other eleven color classes and is not a generic uncolored theorem.
- Q32 (285 edges) and Q33 (284 edges) are distinct historical contracts. Neither is silently substituted for the integrated 47-point low-edge theorem.
- The recurrence replay is finite computation; its graph-to-recurrence completeness is an analytic obligation.
- The COVER shell enumeration is not rerun by the final root verifier. The manuscript states this explicitly.

## Frozen artifacts that must accompany a preprint

1. Integration `SOURCE_MANIFEST.json`, `SHA256SUMS.txt`, `PROOF_DAG.json`, `GLOBAL_THEOREM_LEDGER.md`.
2. `FRONTEND_REPLAY.json` and all three recurrence implementations.
3. Low-edge and 286-edge proof files, verifiers and verification results.
4. COVER proof, case matrix, verifier, result and checksums.
5. H12 source proof and all five q20 equality families.
6. Independent certification report, obligation matrix, gap register, independent replay code and replay results.

The manuscript is not submission-ready until the "Remaining work" column has been discharged or the corresponding material is explicitly supplied as a clearly identified supplementary file.
