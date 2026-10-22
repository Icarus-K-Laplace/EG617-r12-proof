# E406 boundary-bridge status — superseded provenance

Status: `SUPERSEDED / BRIDGE PROVED / E406 CLOSED`.

This file records the former last gap in the E406 proof and is retained only for provenance.

The former open obligation was:

`E406 parent + S31 + hereditary caps -> actual adjacent q30->q31 boundary edge`.

That implication has now been proved independently.

Canonical sources:

- `front_end/E406_LOW_TO_Q30_BRIDGE.md`;
- `front_end/Q30_HEREDITARY_PROMOTION_CANONICAL.md`;
- `front_end/E406_FULL_CLOSURE.md`.

The reconstructed chain is:

1. S31 supplies a degree-13 pivot with `q<=30`.
2. q22/q23 are impossible.
3. q24--q26 promote without jumping directly to q31.
4. q27/q28 are impossible.
5. q29 promotes exactly to q30.
6. Therefore every E406 parent contains a genuine q30 pivot.
7. The independently replayed q30 hereditary theorem reaches q31 within at most two regular repivots.
8. Hence an actual adjacent q30->q31 edge exists.
9. Every possible final-rise distance `d in {1,2,3,10,11,12}` is independently empty.

Therefore

`E406 = EMPTY`.

Do not use the former status `LOCAL_BOUNDARY_COMPLETE / GLOBAL_BRIDGE_OPEN`; it is obsolete.
