# Live research state — 2026-10-31

## Fixed-r12 result

**The original (K_{145}) twelve-color obstruction is PROVED** in the frozen integrated proof at commit `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

The independent AI-assisted audit at commit `09a88cc4fe1e2cf1f3a87475d6484f681910b23e` reports `CERTIFICATION = PASS` for that exact proof snapshot.

This is an informal mathematical proof with finite computational verification. It is not Lean/Coq formalization, external human peer review, or journal acceptance.

## Fixed-r12 proof path

1. Original coloring caps and least-edge-color reduction.
2. Contextual (R(4,49)) impossibility in the original full-color setting.
3. Exact extraction to the unique 61-point residual, with 1,752 recurrence nodes and 144 outer-stop comparisons.
4. 47-point low-edge obstruction and 286-edge equality classification, giving the 287-edge floor.
5. 48-point 310-edge floor and complete h12 terminal exclusion.
6. h13 repivot/charge argument and COVER theorem: (Q\ge29), with E407 and E408 promotions.
7. All T61 alternatives are excluded, contradicting the original coloring.

## Independent certification evidence

The 58-obligation audit reports:

- Q27 and Q28: 19,448 row vectors per case and exactly 2/8 canonical states;
- 81,920 subset identities and 107 regular INS11 checks;
- all 1,752 recurrence entries and 144 outer stops replayed;
- original source provenance and dependency DAG checked;
- no unclosed load-bearing premise found in the pinned proof.

See `PUBLICATION/PROOF_STATUS.md`, `PUBLICATION/WORKSTREAM_INDEX.md` and the pinned `FINAL_CERTIFICATION_REPORT.md`.

## Workstreams and history

All 44 remote branches in the inventory are preserved. The integrated proof and certification are separate immutable source branches. Q32 (285 edges) and Q33 (284 edges) remain distinct contracts. Historical E407/E408, support, witness and general-r workstreams are retained for provenance.

## Open items outside the fixed-r12 theorem

- General-r Erdős–Gyárfás conjecture.
- Abstract uncolored high-energy (R(4,49)) layers E333–E340.
- Lean 4/Mathlib formalization.
- External human mathematical review and journal peer review.
- Preprint publication and DOI assignment.

The abstract high-energy (R(4,49)) problem is not a hidden dependency: the integrated proof excludes the contextual (R(4,49)) object inside the original full-color setting.
