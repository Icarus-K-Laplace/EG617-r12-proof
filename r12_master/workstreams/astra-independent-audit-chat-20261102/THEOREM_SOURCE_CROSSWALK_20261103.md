# EG617(r=12) theorem-to-source crosswalk

Date: 2026-11-03  
Frozen integration audited: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`  
Audit branch: `workstream/r12-astra-independent-audit-20261102`  
Corrected proposal: `PROOF_DAG_CORRECTED_PROPOSAL.json` (28 nodes)

## Audit convention

Here `PROVED` means that the source gives an analytic derivation under the displayed graph contract and this audit pass found no counterexample or load-bearing inference defect in the reviewed derivation. It does **not** mean Lean kernel certification, clean-room execution of the entire root script, or external referee approval. A theorem with an explicit graph-contract hypothesis is still a theorem; `PROVED_CONDITIONAL` is reserved for an unclosed premise, not for ordinary theorem hypotheses.

## 1. Crosswalk of all 28 corrected-DAG nodes

| Node | Exact statement / role | Source and proof location | Parent nodes | Audit disposition |
|---|---|---|---|---|
| `TURAN` | Complement form: α(H)≤k implies e(H)≥p_k(n); equivalently K_{k+1}-free graphs have at most t_k(n) edges. Mantel is k=2. | `K145_TO_T61_FRONTEND_AUDIT.md` §1; `DIRECT_UNIFORM_PROOF.md` §1; `RECURRENCE_PROOF.md` §4; E286 §1. | external leaf | PROVED (classical theorem; arithmetic applications checked) |
| `BROOKS` | A graph of maximum degree 12 with no K13 component is 12-vertex-colorable. | `K145_TO_T61_FRONTEND_AUDIT.md` §1; only used to force δ(G)≤11 in the least-color graph. | external leaf | PROVED (standard theorem; application checked) |
| `AES` | K4-free graph on 35 vertices with minimum degree strictly greater than 5n/8 is 3-partite. | `COVER_THEOREM.md` §8; `H12_AND_EXCEPTIONAL_PARENT_AUDIT.md` intro and §4. Exact threshold 22>175/8. | external leaf | PROVED (statement and strict numerical hypothesis checked) |
| `SECOND_TURAN` | A K13-free, non-12-partite graph on 49 vertices has at most t_12(49)-floor(49/12)+1=1097 edges. | `K145_TO_T61_FRONTEND_AUDIT.md` §2. Complementary color graph has α≤12 and ω≤4, hence the hypotheses. | external leaf | PROVED (Theorem 1 hypotheses checked) |
| `COLOR_CAPS` | Under the assumed 12-coloring, a least color graph G has e(G)≤870, α(G)≤12, ω(G)≤12 and every induced U obeys e(G[U])≤D(|U|). | `K145_TO_T61_FRONTEND_AUDIT.md` §1. The 12-coloring hypothesis is implicit input to the DAG. | TURAN + original counterexample hypothesis | PROVED |
| `LOWER_ORDER` | R(2,24) empty; every R(2,23) has at least131 edges; every R(3,35) has δ≥12; every R(3,36) has δ≥13 and e≥234; R(3,37) empty. | `frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md` M1–M5. M2 enumerates the C5 blow-up/edge-deletion cases; M3 gives the 12-set cost; M4–M5 propagate the bounds. | COLOR_CAPS, TURAN | PROVED (analytic chain reviewed; finite type checks independently reproduced) |
| `CORE211` | Every R(3,35) has at least211 edges. | `frozen/cover/COVER_THEOREM.md` §8; equality e=210 makes the complement 22-regular K4-free and AES applies. | LOWER_ORDER, AES | PROVED |
| `ABSTRACT_LOW285` | No 47-vertex graph has e≤285, δ≥12, α≤4, ω≤11. | `frozen/low/DIRECT_UNIFORM_PROOF.md` §§1–7; common-neighbor tools in `COMMON_NEIGHBORHOOD_CAPACITY.md` C1–C3. Primary route uses the elementary shortest-odd-cycle/Mantel 25-point bound, not Kang–Pikhurko. | TURAN (Mantel included) | PROVED (analytic support/blocker accounting reviewed; finite minima reproduced) |
| `ABSTRACT_286` | No 47-vertex graph has exactly286 edges, δ≥12, α≤4, ω≤11. | `frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md` §§1–12; the missing D zero-completer lemma is supplied separately in `E286_D_SUPPORT_REPAIR.md`; shared-center derivations in `E286_CENTER_CHARGE_AUDIT.md`. | TURAN (Mantel included) | PROVED_CONDITIONAL for the frozen package: analytic repair exists and was checked, but is not included in the frozen theorem file or its SOURCE_MANIFEST. Integrate the lemma before treating the frozen source as self-contained. |
| `GATE47` | Every R(4,47) with e≤286 has δ≥12. | `frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md` Theorem M, especially M6. | LOWER_ORDER | PROVED |
| `R447_FLOOR287` | Every R(4,47) has e≥287. | Combine GATE47, ABSTRACT_LOW285, ABSTRACT_286. If e≤285, LOW285; if e=286, EX286 after GATE47 supplies δ≥12. | GATE47, ABSTRACT_LOW285, ABSTRACT_286 | PROVED_CONDITIONAL on integrating the E286 D-support repair into the frozen theorem source. |
| `CONTEXTUAL49_EMPTY` | No induced 49-set in the original least-color graph can be R(4,49), where R(a,n) means α≤a, ω≤11 and all D caps. | `K145_TO_T61_FRONTEND_AUDIT.md` §2. Lower-order chain gives δ≥13 and e≥319; each of the other 11 colors has at least79 edges, giving target e≤307. | COLOR_CAPS, LOWER_ORDER, SECOND_TURAN | PROVED (contextual only; no generic uncolored R(4,49) claim) |
| `D48` | Every R(4,48) has δ≥12, without an edge-count hypothesis. | `H12_AND_EXCEPTIONAL_PARENT_AUDIT.md` §1. | LOWER_ORDER | PROVED |
| `SHELL_MATCHING_BOUNDS` | The matching lower bounds used by Q20, COVER and the recurrence: h=12 triangle-free shell has a 2-matching; h=13 with z≥22,α(M)≤10 has a 3-matching; h=14 with z≥33 has a 3-matching; h≥15 has ν(M)≥ceil((h-10)/2). | `H12_AND_EXCEPTIONAL_PARENT_AUDIT.md` §2; `COVER_THEOREM.md` §4; `K145_TO_T61_FRONTEND_AUDIT.md` §4. Kőnig's cover lemma is proved inline by alternating paths. | COLOR_CAPS | PROVED |
| `Q20_CLASSIFICATION` | For a degree-12 pivot shell with z≥11, α(M)≤10, pair-row sums≥12 and triangle-row union≥24: q≥20; equality iff M=K_{2,r} plus isolates, 6≤r≤10, hub weights10 and low weights2. | `H12_AND_EXCEPTIONAL_PARENT_AUDIT.md` §2; finite equality replay in `H12_INDEPENDENT_AUDIT.md`. | LOWER_ORDER, TURAN, SHELL_MATCHING_BOUNDS | PROVED under the explicit shell contract |
| `R448_FLOOR310` | Every R(4,48) has e≥310. | `H12_AND_EXCEPTIONAL_PARENT_AUDIT.md` §4: D48, CORE211, q≥20, and repivot exclusion of q=20. | LOWER_ORDER, D48, CORE211, Q20_CLASSIFICATION | PROVED |
| `H12_EMPTY` | No genuine T61 graph with 61 vertices, δ=12, α≤5, ω≤11, all caps and E≤408 exists. | `H12_AND_EXCEPTIONAL_PARENT_AUDIT.md` §5. Every 48-core has e≥310; q≥20; equality q20 is excluded by the inserted-center repivot and D48. | D48, R448_FLOOR310, LOWER_ORDER, Q20_CLASSIFICATION | PROVED under the T61 contract |
| `COVER_Q29_GENERAL` | For every 61-vertex F with δ=13, α≤5, ω≤11 and all D caps, Q=max q_p over all degree-13 pivots is at least29. | `frozen/cover/COVER_THEOREM.md` §§ 1–7. Includes the 47-core δ≥11 gate, deficient-clique lemma, EDGE12, q≤28 shell classification and B1/non-B1 elimination. | LOWER_ORDER, SHELL_MATCHING_BOUNDS | PROVED under the stated contract |
| `COVER_407_408` | Under the same contract, E=407 implies Q≥30; E=408 implies Q≥31. | `frozen/cover/COVER_THEOREM.md` §§8–13; AES gives CORE211; ≤288-core gate and EDGE13 support q29 promotion and q30 Family I/II elimination. | COVER_Q29_GENERAL, CORE211 | PROVED under the stated contract |
| `H13_E_LE406_EMPTY` | No h13 T61 graph with E≤406 exists. | `FINAL_GLOBAL_PROOF.md`: E=91+q_p+e(C), COVER gives q_p≥29, R447_FLOOR287 gives e(C)≥287, so E≥407. | COVER_Q29_GENERAL, R447_FLOOR287 | PROVED_CONDITIONAL on integrating the E286 D-support repair. |
| `H13_E407_EMPTY` | No h13 T61 graph at E=407 exists. | `E407_H13_FINAL_ROOT_CERTIFICATE.md`; every regular pivot gives q_p≥29 from the 287 floor, while COVER gives Q≥30. | COVER_407_408, R447_FLOOR287 | PROVED_CONDITIONAL on integrating the E286 D-support repair. |
| `H13_E408_EMPTY` | No h13 T61 graph at E=408 exists. | `E408_H13_FINAL_ROOT_CERTIFICATE.md`; every regular pivot gives q_p≥30, while COVER gives Q≥31. | COVER_407_408, R447_FLOOR287 | PROVED_CONDITIONAL on integrating the E286 D-support repair. |
| `T61_OTHER_DEGREES` | A genuine T61 parent with 397≤E≤408 cannot have δ≤11 or δ≥14. | `H12_AND_EXCEPTIONAL_PARENT_AUDIT.md` §6 and `FINAL_GLOBAL_PROOF.md`: δ≤11 yields a contextual R(4,49); δ≥14 forces E≥427. | CONTEXTUAL49_EMPTY | PROVED |
| `T61_EMPTY` | No genuine T61 graph under the extracted contract and 397≤E≤408 exists. | `FINAL_GLOBAL_PROOF.md`; combines h12, h13 low, E407, E408 and other-degree exclusions. | H12_EMPTY, H13_E_LE406_EMPTY, H13_E407_EMPTY, H13_E408_EMPTY, T61_OTHER_DEGREES | PROVED_CONDITIONAL on integrating the E286 D-support repair. |
| `RECURRENCE` | The analytic recurrence rules give the finite lower bounds and the unique outer survivor; the 1,752-node evaluation is a finite computation certificate. | `frozen/frontend/RECURRENCE_PROOF.md` §§4 plus `FRONTEND_REPLAY.json`; three independent integer implementations agree on 1,752 nodes and all144 stops. | LOWER_ORDER, CONTEXTUAL49_EMPTY, R447_FLOOR287, R448_FLOOR310, TURAN, SHELL_MATCHING_BOUNDS | PROVED (rules); COMPUTATION_CERTIFIED (evaluation) |
| `EXTRACTION` | From the least-color graph, choose a minimum-degree vertex and a maximal packing of j disjoint target K12s; 0≤d,j≤11, residual order 144-d-12j and α≤11-j, with exact nonnegative edge ledger. | `K145_TO_T61_FRONTEND_AUDIT.md` §3. | COLOR_CAPS, BROOKS | PROVED |
| `K145_TO_T61` | Every hypothetical counterexample produces a residual 61-vertex graph with 397≤E≤408 and the T61 contract. | `K145_TO_T61_FRONTEND_AUDIT.md` §§1–5. | EXTRACTION, RECURRENCE | PROVED (unique survivor also computation-certified) |
| `K145_EMPTY` | No 12-edge-coloring of K145 has every 13-set containing all12 colors. | `FINAL_GLOBAL_PROOF.md`. | K145_TO_T61, T61_EMPTY | PROVED_CONDITIONAL for the frozen package: the proof closes once the E286 D-support repair is inserted into the frozen equality theorem; not Lean-certified or externally refereed |

## 2. Stale H13 documentation is not a hidden dependency

The repository also contains `front_end/T61_H13_LOW_LAYER.md`, whose header says E397–E400 are closed and E401–E408 remain open. Its last modification is 2026-10-21. The frozen integration package is dated 2026-10-31 and contains newer, independently sourced closure documents:
- `frozen/cover/COVER_THEOREM.md` (§§ 1–13);
- `E407_H13_FINAL_ROOT_CERTIFICATE.md`;
- `E408_H13_FINAL_ROOT_CERTIFICATE.md`.

The old H13 low-layer file is **not** included in the integration `SOURCE_MANIFEST.json` and is not a parent in the corrected DAG. It is stale status documentation, not a load-bearing premise and not a mathematical contradiction. It should be updated or explicitly archived before the repository is presented publicly as a clean final proof tree. This audit does not modify it or any sibling workstream.

## 3. Remaining graph/ledger granularity notes

1. The corrected 28-node DAG has all parent references resolved, is acyclic, and all nodes are reachable from `K145_EMPTY`.
2. The original counterexample hypothesis is an implicit input/root assumption to `COLOR_CAPS`; the JSON does not create a separate `ORIGINAL_HYPOTHESIS` node. This is a documentation convention, not a missing mathematical lemma, but a public DAG should label the input assumption.
3. The ledger row `REPLAY` is packaged inside `RECURRENCE`; no separate node is necessary if `RECURRENCE` is explicitly defined to include the finite replay receipt.
4. `Q32` and `Q33` are not separate load-bearing nodes because the direct LOW285 route supplies the needed strict floor. `GEN49` remains OPEN outside the fixed K145 dependency path.
5. `KONIG` is not an external leaf: the matching-cover lemma is proved in the frontend text. Mantel is a special case of Turán and also has an elementary derivation in the common-neighborhood note.

## 4. Bottom line

The corrected proposal gives a semantically coherent mapping for all 28 nodes and their sources. The older 25-node frozen DAG remains incomplete as a dependency map, although its acyclicity check is valid. No new counterexample or missing mathematical implication was identified in this crosswalk pass.

This crosswalk is an independent source/contract audit, not a fresh clean-room run of the complete root verifier. The exact full-root command execution, Lean kernel certification, and external referee review remain separate tasks.


## 5. Load-bearing frozen-source repair: E286 D support

A critical source-completeness distinction emerged in this pass. The frozen `286_EDGE_EQUALITY_CLASSIFICATION.md` Section9 eliminates support pattern D after assuming that each K10 has at least one mixed point completing it. The frozen text does not prove that assertion. The missing zero-completer case is load-bearing: without it, the D branch is not exhaustive.

The audit branch contains the separate analytic proof `E286_D_SUPPORT_REPAIR.md`. It divides each K10 into three exhaustive cases for its K10/K10 support point P: P misses both K10s; P completes the other K10 but misses this one; or P completes this K10. The first case charges at least 2+4+4=10; the second, under the only possible budget-eight equality, forces two common missing sets and a degree at least16; the third gives two additive mixed blockers of at least5 each. Therefore every K10 has a mixed completer. The lemma was re-read and its pointwise shared-center accounting is consistent.

This is a **repairable proof-text gap in the frozen package**, not a counterexample to E286. But the repair file is not part of the frozen 47-file checksum package or 26-entry source manifest. Therefore the strict 287-edge floor and the final K145 conclusion must remain `PROVED_CONDITIONAL` for the frozen snapshot until the lemma is merged into the E286 theorem source and the manifest/checksums are regenerated. The audit branch must not be silently treated as if it were already part of the frozen publication artifact.

## 6. Correction to an earlier h13 matching note

The source's h=13 mixed König-cover bound of12 cross edges is correct. If the two cover vertices s (in the four matched endpoints) and i (in the unmatched nine-set) are adjacent, their incident-edge stars have at most9+4-1=12 edges; if they are not adjacent, the maxima are8+3=11. An earlier audit note claiming13 counted the absent si edge and is withdrawn. See the correction appended to `H13_Q29_Q30_INDEPENDENT_AUDIT.md`. No COVER source correction is needed for this subcase.
