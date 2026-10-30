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

A new reduction now handles the 69/70 near-Turan layer for every non-target color: if a color has 69 or 70 edges inside H, its complement on H is 12-partite and the color graph has an 11K4+K3 partition. For exact colors, every single-outside source witness K4 occupies one of the size-four parts. The source-core edge identity and parameter-dependent bounds are explicit for exact colors. Colors with 71+ H-edges remain outside this partition normal form, and no particular color is yet forced into the 69/70 layer.

Moreover, the abstract pivot matching layer alone can be made globally consistent by choosing a common labeling of the four vertices across all pivot blocks. In that balanced case every light-edge composition agrees, so the local composition theorem need not create any additional heavy-pair cost. The unresolved obstruction must therefore couple these pivot labels to the full Type-I source factors, the residual assignments, and the 130/131-edge color graphs; the pivot matching layer by itself is not a closure theorem.

## Root-side count-vector audit

The read-only root branch currently has an internal summary conflict: its canonical/dependency summaries still state (L_9=6), while the read-only Case-II canonical/dependency audit says the older value 6 is stale and the correct floor is (4+3=7) (130-edge min degree 4; 131-edge min degree 3). The m=9 solver uses 7. This workstream does not edit root files.

## Shortest next attack

1. Run `q32_fullsupport_m89_solver.py --m 8` and `--m 9` with a recorded Z3 version, preserving the generated manifest, SMT2, and logs.
2. If SAT, independently replay with `verify_q32_fullsupport_candidate.py`; classify it as a genuine source-correct graph or a model bug. Do not call it a counterexample before replay.
3. If UNSAT, export and independently replay the proof, then rebuild the constraints in a second implementation (e.g. a separately written SAT/CP-SAT encoding) before claiming COMPUTATION_CERTIFIED.
4. If the solver is slow, first inspect the distributions `x_ij`, `y_i`, and `epsilon_i` from candidate models; derive stronger cuts only from proved pointwise consequences. Prioritize pairs with multiple forced composed matchings and the 130/131 nonexact color residual structures.

No claim is made that these next steps are already complete.


## Low-layer partition-code obstruction

If k non-target colors are in the 69/70 layer, their 11K4+K3 partitions are pairwise orthogonal. Equivalently, the 47 vertices form a 12-ary code of length k with pairwise agreement at most one. The exact agreement count gives 69k<=C(47,2)=1081, hence k<=15. This is not restrictive for k<=11, so it does not close m=8/9. The remaining attack must use the Type-I source labels, the 71+ core-edge colors, and the target-degree/excess ledger together with the partition code.


## New low-layer source-placement closure

For exact colors in the 69/70 layer, the K3/K2 alignment now removes all x-in-H placements except those with the overfull source factor in Nt and y outside H:
- two-double: Nt has outside occupancy 2;
- triple: Nt has outside occupancy 3;
- the Nt H-interior is in x's part;
- at most one H vertex of Ns\A0 remains, and it is exactly the core excess above 69.

The x-outside profile has its unique double K3 in the size-three part and core excess exactly \(1_{y\in H}|A_0\cap H|\). The solver and verifier encode/replay these necessary conditions. They do not force a color into the 69/70 layer.

## New matching-skeleton target

Any low-layer partition admits a 253-edge target subgraph M built from pairwise Hall matchings between parts. The 32-edge residual F has degree \(1+s_v\) on 36 vertices and \(2+s_v\) on 11 vertices, where \(\sum s_v=6\); hence F has at least 30 leaves. The key unresolved question is whether this sparse residual can coexist with the K6-free target graph and the cross-color source constraints. The matching skeleton is currently a theorem, not an explicit CSP matching-choice encoding.
