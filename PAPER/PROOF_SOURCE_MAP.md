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
| 286-edge equality | `LOW_EDGE_AND_286_THEOREM_AUDIT.md`; `frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md` | Include support-orbit exhaustiveness, shared-excess incidence accounting and all equality cases |
| 48-point floor / h12 | `H12_AND_EXCEPTIONAL_PARENT_AUDIT.md` | Include the degree gate, q20 classification, inserted-hub contradiction and exceptional-degree coverage |
| h13 / COVER | `COVER_INDEPENDENT_AUDIT.md`; `frozen/cover/COVER_THEOREM.md`; `E407_H13_FINAL_ROOT_CERTIFICATE.md`; `E408_H13_FINAL_ROOT_CERTIFICATE.md`; `cover/B1_TWO_BASE_POINT_LEMMA.md` | Define all pivots and charges; preserve the exact E407/E408 parent contracts and maximum-pivot quantifiers; distinguish the exceptional Q28 B1 point of degree c+12 from the two base points of degree c+11 in each row triple |
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

## Supplement bundle\n\nSelected pinned proof sources, finite verifiers, replay inputs/results, case matrices and checksums are copied under `PAPER/supplement/`. The bundle is intentionally partial: see `PAPER/REVIEW_FLAGS.md` for the remaining canonical-state, q20, 61-representative, clean-rerun and external-review tasks.\n\n## No silent substitutions

- Q32 is the 285-edge contract; Q33 is the 284-edge contract.
- The final fixed-r12 proof uses the stronger integrated low-edge theorem; do not conflate Q32/Q33 with the original K145 theorem.
- Contextual (R(4,49)) impossibility is not generic uncolored (R(4,49)) nonexistence.
- The Python replay is not Lean formalization.
- AI-assisted audit is not external human peer review.
