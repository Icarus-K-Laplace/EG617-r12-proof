# EG617(r=12) proof-package publication readiness audit

Date: 2026-11-03  
Scope: isolated review of the 2026-10-31 Astra integration package and the separately named Lean branch. No frozen/global files were modified.

## Summary

The mathematical source package has a detailed analytic proof chain, and the independent audits recorded in this workstream have not found a load-bearing gap in the lower-order M1–M6 gate, the K145-to-T61 interface, or the h13 q29/q30 chain. However, **the repository presentation is not yet publication-clean**. Four issues should be resolved before describing the repository as a complete, independently reproducible, formally certified proof package.

## 1. Misleading “balanced coloring” terminology

The integration frontend explicitly says the original assumption is an arbitrary 12-edge-coloring of K145 in which every 13-set contains all12 colors; it does not assume equal color-class sizes.

Nevertheless:
- `FINAL_GLOBAL_PROOF.md` is titled “no balanced12-coloring of K145”;
- `GLOBAL_THEOREM_LEDGER.md` describes CTX49 as “no induced R449 in a balanced original coloring.”

These phrases invite the false interpretation that color classes have equal size. The theorem body and frontend derivation are more precise. Recommended wording:
- title: “No 12-edge-coloring of K145 in which every 13-set contains all 12 colors”;
- CTX49 domain: “No induced contextual R(4,49) occurs in the hypothesized original coloring.”

This is a statement-presentation correction, not a discovered mathematical gap.

## 2. Frozen dependency DAG is incomplete

The integration package's `PROOF_DAG.json` has 25 nodes and is acyclic, but it omits three load-bearing intermediate nodes:
- `GATE47`;
- `D48`;
- `SHELL_MATCHING_BOUNDS`.

It also omits the corresponding parent edges:
- `R447_FLOOR287) must include `GATE47`;
- `R448_FLOOR310) and `H12_EMPTY) must include `D48);
- `Q20_CLASSIFICATION), `COVER_Q29_GENERAL), and `RECURRENCE) must include `SHELL_MATCHING_BOUNDS).

The isolated audit branch already contains `PROOF_DAG_CORRECTED_PROPOSAL.json`, a 28-node acyclic proposal with all parent references resolved and every node reachable from `K145_EMPTY`. The frozen 25-node file was intentionally not changed. The integration `ROOT_PROMOTION_MATRIX.md` calls its proposed DAG “complete”; that label should not be applied to the current 25-node file until the corrected proposal is promoted.

This is a dependency-documentation defect. The corresponding analytic lemmas are present in source files, and this audit did not identify a missing mathematical implication.

## 3. Lean branch is not a Lean project checkout

Read-only inspection of `workstream/r12-lean-formalization-20261031` at HEAD `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2` found 508 tree entries but zero `.lean` files, zero `lakefile`/`lean-toolchain`/`MainTheorem` paths, and zero GitHub Actions workflows.

Therefore that branch cannot substantiate Lean kernel compilation or theorem certification. This finding is strictly scoped to that branch; a separate local ZIP or untracked directory may contain Lean sources and must be audited separately. The required audit includes the original theorem declaration, no `sorry`/untrusted axioms/weakened statement, clean `lake build`, and a kernel-checked declaration of the original K145 theorem.

## 4. Reproducibility boundary and branch status

The 47-entry frozen root SHA256 manifest and 26-entry source-manifest blob map were independently checked. Component-level low-edge, COVER, E286, and recurrence computations were independently replayed in this audit lineage. But the full root `INDEPENDENT_VERIFIER.py` has not been run from a fresh clean checkout in this session. The saved `VERIFICATION_RESULT.json` is a prior output; source inspection shows that the root verifier does not rerun every nested source-workstream enumerator (including the E286 verifier and the bipartite reconstruction routine).

The 2026-10-31 integration branch contains `FINAL_GLOBAL_PROOF.md` and a theorem ledger claiming the fixed K145 theorem is analytically proved. Its receipt explicitly says this is an isolated integration branch and no global-root files were modified. The older Lean-named branch still carries an older `NOT_CERTIFIED` canonical state. These are branch-specific states, not evidence that the integration package has already been promoted into the global canonical root.

## Recommended order

1. Correct “balanced” wording in the manuscript/ledger.
2. Promote the 28-node corrected DAG (or regenerate the DAG from the exact source crosswalk) and rerun its completeness check.
3. Run the full verifier from a fresh checkout and report exactly which nested checks it does and does not execute.
4. Audit the separate Lean ZIP/local source, if it is intended to support a formalization claim.
5. Only then reconcile the global canonical state and public proof-status language.

## Disposition

No new mathematical counterexample was found in the portions independently re-derived this round. The fixed K145 theorem is claimed as analytically proved by the integration package, but this audit does not certify a Lean proof, full clean-room execution, or external referee acceptance. Do not describe the older Lean-named GitHub branch as a formal proof.
