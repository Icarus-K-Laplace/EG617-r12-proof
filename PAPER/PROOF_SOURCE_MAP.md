# Manuscript-to-proof source map

This map ties each manuscript section to the immutable mathematical sources. The paper is a working draft; no proof section is submission-ready until its detailed derivation has been transcribed and checked against these sources.

## Frozen proof identity

- Integrated proof commit: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`
- Independent certification commit: `09a88cc4fe1e2cf1f3a87475d6484f681910b23e`
- Q30 adversarial report commit: `a0f922ad09af99575bae581864b673aa4d41f00d`

## Section mapping

| Manuscript section | Primary source | Required editorial work |
|---|---|---|
| Introduction and conjecture | Erdős–Gyárfás (1999); Xia–Szeider (2026); `FINAL_GLOBAL_PROOF.md` | Complete priority/literature review, exact statement, distinguish fixed r=12 from general conjecture |
| Notation and hereditary caps | `K145_TO_T61_FRONTEND_AUDIT.md`, §§1–2 | Define cap function and all graph contracts without ambiguity |
| Coloring reduction / T61 | `K145_TO_T61_FRONTEND_AUDIT.md`, §§1–5; `CONTEXTUAL_R449_FULL_COLOR_IMPOSSIBILITY.md`; `RECURRENCE_PROOF.md` | Transcribe all inequalities, packing, exact edge ledger, recurrence-rule proofs and all quantifiers |
| 47-point low-edge theorem | `LOW_EDGE_AND_286_THEOREM_AUDIT.md`; `frozen/low/LOW_EDGE_UNIVERSAL_THEOREM.md`; `DIRECT_UNIFORM_PROOF.md`; `MINIMUM_DEGREE_GATE_SELF_CONTAINED.md` | State the five hypotheses exactly; include direct proof and safe-augmentation route with correct domains |
| 286-edge equality and strict 287 floor | `LOW_EDGE_AND_286_THEOREM_AUDIT.md`; `frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md`; `PAPER/supplement/root/E286_COVER_INTERFACE_AUDIT_20261103.md` | Keep GATE47 -> low-285 exclusion -> E286 equality exclusion in the correct order; do not apply the E286 support classification to a 287-edge core |
| 48-point floor / h12 | `H12_AND_EXCEPTIONAL_PARENT_AUDIT.md` | Include the degree gate, q20 classification, inserted-hub contradiction and exceptional-degree coverage |
| h13 / COVER | `COVER_INDEPENDENT_AUDIT.md`; `frozen/cover/COVER_THEOREM.md`; `E407_H13_FINAL_ROOT_CERTIFICATE.md`; `E408_H13_FINAL_ROOT_CERTIFICATE.md`; `PAPER/supplement/root/E286_COVER_INTERFACE_AUDIT_20261103.md`; `PAPER/supplement/root/H13_Q30_X3_BRANCH_RHO_IDENTITY_20261103.md` | Define all pivots and charges; preserve the exact E407/E408 parent contracts, the q_y >= 29 -> core-degree gate -> EDGE13 sequence, and maximum-pivot quantifiers |
| Q30 classification | `Q30_INDEPENDENT_REFEREE_REPORT.md` at commit `a0f922ad...` | Incorporate only after reconciling with the full COVER proof; Q30 report is under its exact E408 maximum-charge contract |
| Finite verification | `INDEPENDENT_VERIFIER.py`, `FRONTEND_REPLAY.json`, `VERIFICATION_RESULT.json`; certification `INDEPENDENT_REPLAY.py` and results | Explain domain/completeness proofs separately from program execution; report what was and was not rerun |
| Scope and limitations | `UNRESOLVED_OBLIGATIONS.md`; `FINAL_CERTIFICATION_REPORT.md` | State generic uncolored R(4,49), general-r, Lean and external review limitations accurately |

## Required theorem ledger before submission

For every theorem/lemma in the final paper, add a row with:

- exact statement and hypotheses;
- source file and section;
- proof dependencies;
- whether it is analytic or finite-computational;
- whether its finite domain is proved exhaustive;
- any external theorem and exact citation;
- status after independent human review.

## No silent substitutions

- Q32 is the 285-edge contract; Q33 is the 284-edge contract.
- The final fixed-r12 proof uses the stronger integrated low-edge theorem; do not conflate Q32/Q33 with the original K145 theorem.
- Contextual (R(4,49)) impossibility is not generic uncolored (R(4,49)) nonexistence.
- The Python replay is not Lean formalization.
- AI-assisted audit is not external human peer review.


## Post-audit additions (5 November 2026)

The publication branch adds the following source crosswalk and supporting material:

| Claim or clarification | Frozen source | Supplementary location |
|---|---|---|
| Pointwise identity $E=91+q_p+e(C_p)$ and 287-edge floor for every regular pivot | Integration snapshot `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`; `frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md`; `frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md`; `frozen/cover/COVER_THEOREM.md` | `supplement/root/E286_COVER_INTERFACE_AUDIT_20261103.md` |
| E408/Q30, d=2 K4 repivot: EDGE12 first gives q_y >= 29; then e(C_y) <= 288 gives delta(C_y) >= 12; inserted degrees then contradict EDGE13 | `frozen/cover/COVER_THEOREM.md`, Sections 3, 8, 10 | Same interface audit |
| |X|=3 Q30 heavy-set branch: rho=9 and q_y >= 31 | `frozen/cover/COVER_THEOREM.md`, Section 10 | `supplement/root/H13_Q30_X3_BRANCH_RHO_IDENTITY_20261103.md` |
| Family I/II repivots remain inside one fixed 61-vertex parent; excess is not double-counted | `frozen/cover/COVER_THEOREM.md`, Sections 10-12 | Same interface audit |
| Missing explicit dependency nodes GATE47, D48, SHELL_MATCHING_BOUNDS | `PROOF_DAG.json` and `GLOBAL_THEOREM_LEDGER.md` in the frozen integration snapshot | `supplement/root/DAG_DEPENDENCY_CORRECTION_NOTE_20261105.md`; corrected proposal JSON |

The frozen 25-node DAG is not edited by this branch. The 28-node proposal
has been checked for resolved parent references, acyclicity, and reachability
of all nodes as dependencies of K145_EMPTY; this graph-structure check is
not a semantic proof that every mathematical dependency has been identified.
The full root verifier has not been rerun from a fresh clean checkout in
this publication update. The manuscript remains a working draft and is not
submission-ready.
