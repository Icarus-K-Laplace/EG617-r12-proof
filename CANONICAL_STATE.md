# Canonical state — 2026-10-31

## Fixed-r12 theorem

**STATUS: PROVED** in the frozen integrated proof snapshot, as a conventional informal mathematical proof with finite computational verification and an independent AI-assisted audit.

The theorem is:

> Every 12-edge-coloring of (K_{145}) has a 13-vertex set whose induced edges omit at least one of the 12 colors.

Equivalently, no 12-coloring makes every 13-set contain all 12 colors.

## Frozen proof and certification

- Integrated proof: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`
- Independent certification: `09a88cc4fe1e2cf1f3a87475d6484f681910b23e`
- Independent certification verdict: `CERTIFICATION = PASS`
- Q30 independent adversarial report: `a0f922ad09af99575bae581864b673aa4d41f00d`

Read `PUBLICATION/PROOF_STATUS.md` and `PUBLICATION/WORKSTREAM_INDEX.md` for exact domains, caveats and branch map.

## Canonical proof chain

1. Original (K_{145}) coloring reduction and exact extraction ledger.
2. Contextual (R(4,49)) impossibility in the original full-color setting.
3. Lower-order graph bounds and the 47-point low-edge/equality obstruction, yielding the 287-edge floor.
4. The 48-point 310-edge floor and h12 terminal exclusion.
5. The 61-point h13 repivot/charge argument and COVER terminal inequalities.
6. The 1,752-node recurrence replay and all 144 outer-stop comparisons.
7. Elimination of the unique T61 residual and contradiction to the assumed coloring.

The complete proof is in the pinned integration branch, not reconstructed by reading the historical local workstreams in isolation.

## Certification boundary

The independent audit is AI-assisted and informal. It includes analytic derivations, finite replay, provenance checks and a 58-obligation matrix. It is not Lean/Coq formalization, external human peer review, or journal acceptance.

## Open items outside the fixed-r12 theorem

- Abstract uncolored high-energy (R(4,49)) layers E333–E340 remain outside the scope of this theorem and are not claimed solved.
- The general Erdős–Gyárfás conjecture for all (r) remains open.
- Lean 4/Mathlib formalization remains future work.
- External human specialist review and journal peer review remain future work.
- Preprint and journal submission have not yet occurred.

## Repository state

The old Global Root and historical workstream branches are preserved. The integrated proof is a separate frozen source; the independent certification PR is open and draft. The publication-preparation branch is documentation-only and does not silently promote or merge the historical root.
