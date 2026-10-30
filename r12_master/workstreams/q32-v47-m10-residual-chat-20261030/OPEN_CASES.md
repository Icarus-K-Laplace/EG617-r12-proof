# M10 open-case register

All items below are full-support |U|=47, m=10. The 3+7 normal form is conditionally closed; the following branches are not.

## A. Ten-block light graph

1. CONNECTED-L: L is connected on ten pivot blocks, with at least 17 light edges. No global matching-holonomy theorem has been proved for this case.
2. DISCONNECTED-1+9: singleton component consumes at least four units of Q excess; Y+2Z<=10, Z<=5, and its residual incidence slack is at most two.
3. DISCONNECTED-2+8: eight-block outer graph has minimum light degree at least four, weighted internal-heavy degree at most three, X_T=8+Z, Y=8-2Z, Z<=4. The two-block blocker and synchronized-switch theorem are local only.
4. DISCONNECTED-4+6: the four-block component is K4 or K4-e; the K4-e branch has all 24 cross pairs exactly five edges and a six-block internal heavy matching. The entire K4-e, Z=4 slice is now CLOSED for every residual profile and every six-column grid by M10_K4E_Z4_GLOBAL_GRID_CLOSURE.md. The remaining 4+6 frontier is the K4 small-component branch and K4-e with Z=1,2,3. The corrected 5,5,5 and 20,842-state one-column catalogs remain valid local inputs; no global two-permutation assumption is made.
5. DISCONNECTED-5+5: 25 cross pairs are heavy; Y+Z<=7, Z>=1, and 2(delta_ST+X_S+X_T)+Y<=6. Each side has an aligned four-block K4/K4-e core; at least 13 of the 16 cross-core pairs are exactly five edges. Need classify the cross-core 4-by-4 matching grid and two fringe attachments.

## B. Source-correct Type-I occupancy modes

The aggregate occupancy catalog is source-complete at 90 labelled factor assignments, but endpoint-labelled source completions remain open.

1. O-I: one isolated double-outside factor; eight H-vertices remain in G_11.
2. O-N_s and O-N_t: one special double-outside factor; seven H-vertices remain in G_11. Keep N_s and N_t distinct.
3. H-SS: both special factors double-outside; seven H-vertices remain in G_11.
4. H-I/N_s and H-I/N_t: one isolated and one special double-outside factor; eight H-vertices remain in G_11.
5. H-II: two isolated double-outside factors; nine H-vertices remain in G_11.
6. H-TI: one isolated triple-outside factor; nine H-vertices remain in G_11. This source mode is NOT excluded by the generic factorization and remains OPEN.
7. H-T/N_s and H-T/N_t: triple-outside special factor; seven H-vertices remain in G_11. Keep N_s and N_t distinct.

The six aggregate outside-count profiles are complete, but the labelled occupancy families are ten rows after preserving special-factor identity. No source row is promoted to a globally feasible candidate without y/A_0 endpoint and target-part compatibility.

## C. Residual/fiber/edge compatibility

The 371-type graph catalog is source-correct after the incidence proof excludes the unique 5-chromatic residual C5 dot-union 2K1. It gives all remaining residual graphs in the scalar alpha/clique-cover/incidence relaxation and all single four-clique-fiber maps. It does not yet enumerate:
- the block-indexed incidence vectors a_ri;
- the compatibility of two fiber maps F,G;
- all ten-block weighted-heavy graphs;
- all pairwise matching permutations and extra-edge endpoints;
- every source gadget edge placement;
- the global outer weighted-heavy graph/residual-fiber compatibility;
- all cross-color edge ownership constraints.

These are the next load-bearing interfaces.

## D. Promotion and root status

Astra's theorem applies only after the 3+7 five-property contract is proved. It does not eliminate any other L profile. The Q32 full-support m=10 terminal is OPEN / NOT_CERTIFIED, and the EG617(r=12) root theorem is not closed.


## 4+6 closed subcase

PROVED_CONDITIONAL: the entire 4+6 K4-e, Z=4 cell is impossible for all residual fiber profiles and all six-column matching/extra-edge patterns. See M10_K4E_Z4_GLOBAL_GRID_CLOSURE.md and verify_m10_k4e_z4_grid_reduction.py. The older two-aligned pattern-10 result is a strict subcase. K4 and K4-e Z=1,2,3 remain OPEN.

## 4+6 tightened residual frontier — 2026-10-30

The K4 small-component branch now has the exact necessary residual filter B_min<=10-2z: 79 graph types / 121,782 labelled residual graphs / 9,600 clique-fiber maps over z=0,...,5. Its six-vertex outer weighted-heavy graph has x_T<=4, a total nonbaseline budget delta+Y_S+sum(s_j)<=2, and 7,434 labelled aggregate degree-ledger states across only 14 weighted-graph isomorphism types.

For K4-e with Z=1,2,3, the residual filter is B_min<=8-2Z, leaving 15 graph types / 11,662 labelled residual graphs / 1,176 clique-fiber maps. The Z=4 slice remains closed by the global grid theorem.

These filters do not yet impose all cross-cell matching endpoints, the full F/G residual compatibility, or source-color edge ownership. Both branches remain OPEN.

### K4-e, Z=3 matched-column update — 2026-10-30

The residual graph frontier is six types. The four zero-slack outer blocks share a common residual map G, and the small K4-e side shares F. Exact pair/triple enumeration removes full/full nonaligned and F-full/G-empty matched-column regimes by the outer pointwise degree cap. Four residual types now force full/full aligned cells; only 2C3+K1 and C3+P4 retain empty-map alternatives.

Still OPEN: coupling the two unmatched outer blocks (each with y_j=1), the complete 4x6 matching/extra-edge matrix, residual incidences, and source-color edge ownership.
