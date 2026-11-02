# Frozen package checksum and verifier-scope audit

Date: 2026-11-02  
Frozen integration commit: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`  
Audit branch: `workstream/r12-astra-independent-audit-20261102`

## 1. Root SHA-256 manifest

I fetched each of the 47 files named by the frozen integration's root `SHA256SUMS.txt` using GitHub's base64 file-content representation, decoded the bytes, and independently recomputed SHA-256 in a separate JavaScript implementation. The SHA-256 implementation was checked against the standard `abc` test vector:

`ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`.

Results by batches: 8/8, 8/8, 8/8, 8/8, 8/8, 7/7. Total: **47/47 exact matches, zero mismatches**. The checked files total approximately 120 KB. This includes the root `INDEPENDENT_VERIFIER.py`, whose digest matches the frozen receipt/result value `13d2f166305b2fbfa78297a61b7cd2b9d7ef3b72246e653b72ece441c243c63d`.

This is a byte-level SHA-256 check of the exact GitHub file payloads, not a local checkout/build.

## 2. Nested manifests are source-workstream manifests, not complete vendored subpackages

The nested `frozen/cover/SHA256SUMS.txt` has 11 entries. Seven of those files are vendored under `frozen/cover/` in the integration snapshot and are covered by the root 47-file manifest. Four entries are not vendored there: `BIPARTITE_EXPLORATION.json`, `CANONICAL_STATE.md`, `explore_bipartite.py`, and `PROGRESS_LOG.md`.

The nested `frozen/eq286/SHA256SUMS.txt` has 14 entries. Three are vendored under `frozen/eq286/` in the integration snapshot: the theorem, verifier, and verification result. Eleven source-workstream artifacts are not vendored there, including the counterexample-search script, state/progress/receipt files, and auxiliary theorem/dependency documents.

This is not a mismatch in the root package: every file that the root package itself lists passes its checksum. It does mean the nested manifests cannot be treated as evidence that the complete original COVER and E286 workstream directories are contained in the integration package. The 26-entry top-level `SOURCE_MANIFEST.json` authenticates the selected vendored source files by their Git blob identities at source and destination commits. The unvendored nested files need to be fetched from those source commits if a fully self-contained archival copy of those workstreams is desired.



## 2a. Nested source-workstream checksums independently verified

The nested manifests were then checked at their actual source commits, not merely inspected in the vendored copy:

- COVER source workstream `r12_master/workstreams/astra-cover-independent-closure-chat-20261031/`, commit `531e41c79e08dd2bb3892ca9ba8a491a56678565`: **11/11** nested SHA-256 entries match.
- E286 source workstream `r12_master/workstreams/astra-286-edge-parent-equality-chat-20261030/`, commit `c3d07b2ca5912b1b0c1c6998303c19c3c2911340`: **14/14** nested SHA-256 entries match.

Thus the nested manifests are valid for their original source workstreams. The integration snapshot selectively vendors only 7/11 COVER files and 3/14 E286 files; the remaining source files are authenticated at their original source commits but are not physically included under the integration `frozen/` subdirectories. This is a selective-vendoring/self-containment distinction, not a checksum failure.

## 3. What the root verifier actually reruns

Inspection of the exact frozen `INDEPENDENT_VERIFIER.py` shows:

- `verify_sources()` checks the 26 top-level source-manifest destination blobs and records their SHA-256 values.
- `verify_frontend()` imports both frozen recurrence implementations, computes a third recurrence, and compares all 1,752 nodes, maximum orders, 144 outer stops, and T61 minimum-degree rows.
- `verify_cover_retained()` imports the COVER verifier module, authenticates its source SHA against the saved result, compares the saved states with `expected_states(q)`, and directly checks every subset identity and repivot arithmetic on those retained states. It **does not call** `reconstruct_bipartite(q)`; therefore the 19,448 row-count-vector enumeration is not rerun by the root verifier.
- `verify_lower_order_families()` calls the low verifier's `type_classification()`, `neighborhood_extension_costs()`, and `minimum_degree_and_parents()`. It does not call that module's `capacity_and_augmentation()` or `structural_checks()`.
- `verify_new_arithmetic()` independently checks the displayed 47/48/49-point numerical interfaces and the small support-orbit counts.
- It does not import or execute the separate E286 verifier. The E286 theorem's analytic proof is present; its saved verifier/result are hash-authenticated, while the root's own support quotient only recomputes the `[2,3,5]` orbit counts.

These are explicit design boundaries in the code, not hidden defects. The result file also says `shell_search_rerun: false` and describes the finite completeness evidence as the frozen enumeration algorithm, prior authenticated result, and analytic reductions. The root verification output must not be described as a fresh full COVER-shell or E286-search rerun.

## 4. Clean-room execution status

I have **not** executed `python -B INDEPENDENT_VERIFIER.py` in a clean local checkout in this session. The container download endpoint did not permit downloading the GitHub archive, and the connected GitHub file API provides file payloads but not a checked-out filesystem. Thus the frozen `VERIFICATION_RESULT.json` remains a previously recorded result, not a newly reproduced process exit code from this audit.

The frontend recurrence has separately been reimplemented and exactly compared in `FRONTEND_RECURRENCE_INDEPENDENT_AUDIT.md`. The package checksum audit above is newly completed. A genuine clean-room execution of the root, COVER, low, and E286 scripts remains a distinct outstanding check.

## 5. Mathematical spot checks added in this pass

The 5-cycle two-neighbor-type model used in the lower-order proof was independently enumerated:

- Exactly 20 ordered nonempty compatible type-set pairs occur.
- For every admissible singleton cycle-neighborhood in the 121-edge case, a compatible two-neighbor type extension exists; zero failures.
- In the (K_{9,9}) minus one cross-edge case, exactly 10 oriented incompatible endpoint-type cases occur, and each is a relabeling of the stated (C_5(9,9,2,1,2)) configuration.

These checks corroborate the finite type reductions in M2. They do not replace the analytic proof of the M3 neighborhood-cost lemma or the full lower-order theorem.

## 6. Current conclusion

- Root package byte integrity: **PASS (47/47 SHA-256 entries)**.
- Top-level source provenance: **PASS (26/26 Git blob source/destination mappings)**, as recorded in `SOURCE_MANIFEST_AUDIT.json`.
- Frontend recurrence arithmetic: **PASS (1,752/1,752 exact matches)**.
- Proposed proof DAG: **PASS (acyclic; all 28 nodes reachable from the K145 root)**.
- Full root verifier clean-room execution: **NOT RUN in this session**.
- Full COVER shell enumeration rerun: **NOT RUN by the root verifier**.
- E286 verifier rerun: **NOT RUN by the root verifier**.
- Lean kernel certification: **not established by this audit**.

No frozen integration file or sibling workstream was modified.
