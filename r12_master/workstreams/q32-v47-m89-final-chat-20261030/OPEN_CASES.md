# Open cases — full-support m=8,9

## Current status

**OPEN / NOT_CERTIFIED.** The previous closure is retracted: it assumed omega(H)<=5 and omega(C)<=5, while EG617 only supplies omega(H)<=11 and omega(C)<=12. It also assumed every exact-129 color is Type I. See AUDIT_RETRACTION_BALANCED_PREMISES.md.

The scalar frontiers and pivot matching search remain conditional intermediate work. The 69/70 exclusion and Type-I analytic closure are not valid under the actual EG617 hypotheses. The remaining task is a source-complete Q32 attack under alpha(C),omega(C)<=12 and omega(H)<=11.

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

## Current next action — rebuild under actual EG617 hypotheses

1. Do not assume omega(C)<=5 or omega(H)<=5. The actual balanced-coloring bounds are omega(C)<=12 and, for the Q32 core in R(4,49), omega(H)<=11.
2. Classify exact-129 colors including the complement 12-partite case and both size-six Kang–Pikhurko equality profiles.
3. Replace the K6/K7 contradiction by an obstruction valid when omega(H)<=11.
4. Rebuild the solver/verifier to include all source modes; the current candidate format is Type-I-only and the optional --check-omega mode is an augmented problem. Do not promote anything to the root branch from this workstream.


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


## Withdrawn result: 69/70 layer exclusion under an extra K6-free assumption

The tight-part matching argument proves that any 11K4+K3 partition of H forces an independent 5-set or a K7. The 69/70 near-Turán theorem does supply such a partition, but the resulting K7 is allowed under the actual omega(H)<=11 contract. Therefore the claimed universal e_C(H)>=71 floor and the 37-unit ledger above 71 are withdrawn for EG617. The solver's 71-edge cut belongs only to the augmented K6-free submodel.


## Final analytic terminal — exact Type-I source obstruction

The former 71+ source-placement attack was incorrectly marked superseded. **Conditionally**, if an exact-129 color is Type I, it induces one of:
- \(11K_4+K_3\) if x lies in O;
- \(10K_4+2K_3+K_1\) if x lies in H with two double-outside factors;
- \(11K_4+K_2+K_1\) if x lies in H with one triple-outside factor.

A unified Hall/tight-part lemma excludes all three partitions under the frozen H-core contract. Therefore no exact-129 Type-I color can exist. Since m=8 and m=9 both require at least one such color, both full-support Q32 branches are **ANALYTICALLY CLOSED / IMPOSSIBLE** conditional on the published Kang–Pikhurko exact-129 classification, the balanced-coloring alpha<=12 premise, global monochromatic-K6 exclusion, and the H-core contract.

No full SMT run or UNSAT proof log is claimed or needed. The next work is dependency promotion: independently audit the imported Type-I factorization and H-core contract against the parent E408/Q32 theorem, then update the root dependency DAG/receipt through the appropriate parent workstream. This isolated branch does not claim that E408 as a whole, Q33, E407, or the original Erdős r=12 theorem is closed.


## Parent-level scope audit — previous promotion withdrawn

The Type-I obstruction cannot be promoted to any support row: its required omega(H)<=5 and omega(C)<=5 hypotheses are absent, and universal Type-I source coverage is unproved. The former all-support/m-independent closure claim is withdrawn. The parent root branch remains unchanged.

## Current load-bearing gaps

1. **Completed structural gate:** V47_EXACT129_UNIVERSAL_PARTITION.md proves that every exact-129 color, including the 12-partite complement and all three non-12-partite Kang–Pikhurko profiles, induces one of the three H-partition shapes.
2. **Live mathematical gate:** the Hall/tight-part theorem now gives omega(H)>=6 for every exact-129 color. Find a contradiction or stronger structure using the actual omega(H)<=11 cap, e(H)=285, delta(H)>=12, and total excess six.
3. **Model gate:** if a full graph-coloring CSP is still used, include all source modes; the current solver/verifier remain Type-I and K6-free restricted diagnostics.


## Critical audit correction (2026-10-30)

The actual EG617 counterexample hypothesis is balancedness: every 13-set contains all twelve colors. Therefore each color C satisfies alpha(C)<=12 and omega(C)<=12; monochromatic K6 is allowed. The Q32 core is in R(4,49), so omega(H)<=11. No global K6-free premise exists.

The exact-129 Type-I factorization requires the non-12-partite complement gate and the clique cap used to eliminate size-six equality profiles. These do not follow from balancedness. The local graph C0=5K6 dot-union 3K5 dot-union 4K4 has 61 vertices, 129 edges, alpha=12, omega=6 and a 12-partite complement, demonstrating the missing gate at the one-color level.

Thus the current verifier/solver are restricted Type-I/K6-free diagnostics, not full EG617 encodings. The previous m=8/9 closure and all-support parent promotion are retracted. See AUDIT_RETRACTION_BALANCED_PREMISES.md.

## New source-complete theorem

The exact-129 source classification is no longer an open blocker at the partition level. The 12-partite complement case gives 11K4+K3 directly; the non-12-partite case gives one of the three partitions via all Kang–Pikhurko equality profiles. The remaining obstruction is not source coverage but the fact that the resulting K6/K7 in H is allowed by omega(H)<=11.


## Source-complete witness interface repaired

V47_EXACT129_UNIVERSAL_PARTITION.md and V47_EXACT129_CORE_EDGE_BOUNDS.md now prove that every exact-129 color supplies at least ten disjoint core K4 witnesses and satisfies 69<=e_C(H)<=75, including the 12-partite complement and all three non-12-partite Kang–Pikhurko profiles. This is enough to justify the ten-witness input of Q32_U_COLOR_RESERVE.md.

It does not supply a canonical special point x or a fixed-pivot K4 Q_C for the 12-partite branch. The full-support CSP still hard-codes Type-I K5 factors and K6-free cuts, so it is not a complete encoding of EG617. The live gap is to exploit the source-complete partition/witness system under omega(H)<=11 and to replace the Type-I-only pivot interface.
