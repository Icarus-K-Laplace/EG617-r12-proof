# Open cases — full-support m=8,9

## Current status

**OPEN.** The source-correct full 61-point model has been strengthened, but it has not been run to completion. The scalar pivot relaxation is nonempty, so it is not a proof by itself.

## Remaining scalar states

The exact scalar constraints are:
`x+y+z=32`,
`2x+y>=5m`,
`y+2z>=D_m`,
`(2x+y-5m)+(y+2z-D_m)=6`,
with `D_8=18`, `D_9=13`.

Independent enumeration:
- m=8: 79 integer states; x=8..23, y=0..24, z=0..12.
- m=9: 61 integer states; x=13..25, y=0..19, z=0..9.

These are scalar relaxations. They do not assert realizability by H or by the complete edge coloring.

## Minimum unresolved mathematical obstacle

The remaining obstacle is global compatibility of the full family of 10/11 single-outside K4 witnesses per exact color with:
1. the 47-point target graph H;
2. pairwise linearity and complete edge ownership;
3. the pivot pair perfect matchings and their forced compositions;
4. the six-unit degree-excess distribution;
5. the exact Type-I special-gadget residuals;
6. the 130/131-edge nonexact colors and their alpha/clique restrictions.

The m=8/9 pivot-level scalar relaxation has not been eliminated. The guarded matching-composition cuts only apply when two incident pivot pairs remain light; they do not yet force a global contradiction.

A new exact-color reduction now handles the 69/70 near-Turan layers: if an exact color has 69 or 70 edges inside H, its complement on H is 12-partite and the color graph has an 11K4+K3 partition. Every single-outside source witness K4 occupies one of the size-four parts. The source-core edge identity and parameter-dependent bounds are now explicit in the CSP and independent verifier. This still leaves exact colors with 71--75 H-edges structurally open, and does not prove that any particular color lies in the 69/70 layer.

Moreover, the abstract pivot matching layer alone can be made globally consistent by choosing a common labeling of the four vertices across all pivot blocks. In that balanced case every light-edge composition agrees, so the local composition theorem need not create any additional heavy-pair cost. The unresolved obstruction must therefore couple these pivot labels to the full Type-I source factors, the residual assignments, and the 130/131-edge color graphs; the pivot matching layer by itself is not a closure theorem.

## Root-side count-vector audit

The read-only root branch currently has an internal summary conflict: its canonical/dependency summaries still state (L_9=6), while the read-only Case-II canonical/dependency audit says the older value 6 is stale and the correct floor is (4+3=7) (130-edge min degree 4; 131-edge min degree 3). The m=9 solver uses 7. This workstream does not edit root files.

## Shortest next attack

1. Run `q32_fullsupport_m89_solver.py --m 8` and `--m 9` with a recorded Z3 version, preserving the generated manifest, SMT2, and logs.
2. If SAT, independently replay with `verify_q32_fullsupport_candidate.py`; classify it as a genuine source-correct graph or a model bug. Do not call it a counterexample before replay.
3. If UNSAT, export and independently replay the proof, then rebuild the constraints in a second implementation (e.g. a separately written SAT/CP-SAT encoding) before claiming COMPUTATION_CERTIFIED.
4. If the solver is slow, first inspect the distributions `x_ij`, `y_i`, and `epsilon_i` from candidate models; derive stronger cuts only from proved pointwise consequences. Prioritize pairs with multiple forced composed matchings and the 130/131 nonexact color residual structures.

No claim is made that these next steps are already complete.
