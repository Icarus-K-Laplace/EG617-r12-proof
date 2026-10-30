# Open cases — full-support m=8,9

## Current status

**NO OPEN MATHEMATICAL CASE REMAINS IN THIS ISOLATED m=8/9 FULL-SUPPORT TERMINAL.** The exact-129 Type-I factorization forces one of three independent-part partitions of H; a unified Hall/tight-part theorem excludes all three. See V47_TYPEI_PARTITION_OBSTRUCTION.md. The solver was not run and no SMT UNSAT certificate is claimed.

The scalar frontiers, pivot matching search, and 69/70 layer material below are historical intermediate work, superseded by the final analytic Type-I obstruction at the end of this file. The only remaining action in this branch is dependency promotion/audit by the parent root workstream.

## Historical scalar relaxation (superseded)

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

## Historical unresolved obstacle (superseded)

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

## Current next action — parent dependency promotion

1. Audit the imported exact-129 Type-I factorization against its primary source and the sibling high-support source interface.
2. Audit that the parent Q32 terminal legally supplies all five H-core premises: order 47, 285 edges, minimum degree 12, alpha at most four, and clique number at most five.
3. Promote the theorem and verifier receipt into the parent root dependency DAG only after those dependencies are confirmed. Do not modify sibling workstreams from this branch.


## Historical low-layer partition-code obstruction (superseded)

If k non-target colors are in the 69/70 layer, their 11K4+K3 partitions are pairwise orthogonal. Equivalently, the 47 vertices form a 12-ary code of length k with pairwise agreement at most one. The exact agreement count gives 69k<=C(47,2)=1081, hence k<=15. This is not restrictive for k<=11, so it does not close m=8/9. The remaining attack must use the Type-I source labels, the 71+ core-edge colors, and the target-degree/excess ledger together with the partition code.


## Historical low-layer source-placement closure (superseded)

For exact colors in the 69/70 layer, the K3/K2 alignment now removes all x-in-H placements except those with the overfull source factor in Nt and y outside H:
- two-double: Nt has outside occupancy 2;
- triple: Nt has outside occupancy 3;
- the Nt H-interior is in x's part;
- at most one H vertex of Ns\A0 remains, and it is exactly the core excess above 69.

The x-outside profile has its unique double K3 in the size-three part and core excess exactly \(1_{y\in H}|A_0\cap H|\). The solver and verifier encode/replay these necessary conditions. They do not force a color into the 69/70 layer.

## Historical 69/70 matching-skeleton analysis (superseded)

Any low-layer partition admits a 253-edge target subgraph M built from pairwise Hall matchings between parts. The 32-edge residual F has degree \(1+s_v\) on 36 vertices and \(2+s_v\) on 11 vertices, where \(\sum s_v=6\); hence F has at least 30 leaves. The key unresolved question is whether this sparse residual can coexist with the K6-free target graph and the cross-color source constraints. The matching skeleton is currently a theorem, not an explicit CSP matching-choice encoding.


The 32-edge residual has a sharper exact form. Let q be the number of the 36 M-degree-11 vertices receiving positive degree excess, and t the number of isolated K2 components of F. Then q≤6, q+t≥4, the non-leaf core has 11+q≤17 vertices, and its induced edge count is exactly q+t-4. The remaining 36-q vertices are leaves, with 2t of them paired into the isolated K2 components. This leaf-core identity is now in MATH_PROOF.md §9.6.


## Historical intermediate result: 69/70 layer exclusion

The tight-part matching argument proves that any 11K4+K3 partition of H forces an independent 5-set or a K7. Hence, using the registered near-Turán theorem, every non-target color satisfies \(e_C(H)\ge71\). The exact 37-unit ledger is now \(\sum_c(e_C(H)-71)=15\).

The solver has removed the conditional near-Turán partition variables and asserts the 71-edge lower bound. The independent verifier reconstructs the partition when needed and replays the matching/tight-part dichotomy. The remaining research target is the 71+ layer, not the already-excluded 69/70 layer.


## Final analytic terminal — exact Type-I source obstruction

The former remaining 71+ source-placement attack is superseded. Any exact-129 Type-I color induces one of:
- \(11K_4+K_3\) if x lies in O;
- \(10K_4+2K_3+K_1\) if x lies in H with two double-outside factors;
- \(11K_4+K_2+K_1\) if x lies in H with one triple-outside factor.

A unified Hall/tight-part lemma excludes all three partitions under the frozen H-core contract. Therefore no exact-129 Type-I color can exist. Since m=8 and m=9 both require at least one such color, both full-support Q32 branches are **ANALYTICALLY CLOSED / IMPOSSIBLE** conditional on the registered Type-I factorization and H-core contract.

No full SMT run or UNSAT proof log is claimed or needed. The next work is dependency promotion: independently audit the imported Type-I factorization and H-core contract against the parent E408/Q32 theorem, then update the root dependency DAG/receipt through the appropriate parent workstream. This isolated branch does not claim that E408 as a whole, Q33, E407, or the original Erdős r=12 theorem is closed.
