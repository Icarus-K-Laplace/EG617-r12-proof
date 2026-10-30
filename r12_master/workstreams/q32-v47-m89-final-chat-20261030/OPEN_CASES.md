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
- m=8: 79 integer states; x=8..23, y=0..24, z=0..24.
- m=9: 61 integer states; x=13..25, y=0..19, z=0..19.

These are scalar relaxations. They do not assert realizability by H or by the complete edge coloring.

## Minimum unresolved mathematical obstacle

The remaining obstacle is global compatibility of the full family of 10/11 single-outside K4 witnesses per exact color with:
1. the 47-point target graph H;
2. pairwise linearity and complete edge ownership;
3. the pivot pair perfect matchings and their forced compositions;
4. the six-unit degree-excess distribution;
5. the exact Type-I special-gadget residuals;
6. the 130/131-edge nonexact colors and their alpha/clique restrictions.

The m=8/9 pivot-level scalar relaxation has not been eliminated. The new matching-composition cuts only apply when two incident pivot pairs are light; they do not yet force a global contradiction.

Moreover, the abstract pivot matching layer alone can be made globally consistent by choosing a common labeling of the four vertices across all pivot blocks. In that balanced case every light-edge composition agrees, so the local composition theorem need not create any additional heavy-pair cost. The unresolved obstruction must therefore couple these pivot labels to the full Type-I source factors, the residual assignments, and the 130/131-edge color graphs; the pivot matching layer by itself is not a closure theorem.

## Shortest next attack

1. Run `q32_fullsupport_m89_solver.py --m 8` and `--m 9` with a recorded Z3 version, preserving the generated manifest, SMT2, and logs.
2. If SAT, independently replay with `verify_q32_fullsupport_candidate.py`; classify it as a genuine source-correct graph or a model bug. Do not call it a counterexample before replay.
3. If UNSAT, export and independently replay the proof, then rebuild the constraints in a second implementation (e.g. a separately written SAT/CP-SAT encoding) before claiming COMPUTATION_CERTIFIED.
4. If the solver is slow, first inspect the distributions `x_ij`, `y_i`, and `epsilon_i` from candidate models; derive stronger cuts only from proved pointwise consequences. Prioritize pairs with multiple forced composed matchings and the 130/131 nonexact color residual structures.

No claim is made that these next steps are already complete.
