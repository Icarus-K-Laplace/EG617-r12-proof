# M10 open-case register

All items below are full-support |U|=47, m=10. The 3+7 normal form is conditionally closed; the following branches are not.

## A. Ten-block light graph

1. CONNECTED-L: L is connected on ten pivot blocks, with at least 17 light edges. No global matching-holonomy theorem has been proved for this case.
2. DISCONNECTED-1+9: singleton component consumes at least four units of Q excess; Y+2Z<=10, Z<=5, and its residual incidence slack is at most two.
3. DISCONNECTED-2+8: eight-block outer graph has minimum light degree at least four, weighted internal-heavy degree at most three, X_T=8+Z, Y=8-2Z, Z<=4. The two-block blocker and synchronized-switch theorem are local only.
4. DISCONNECTED-4+6: four-block component is K4 or K4-e; 24 cross pairs have at most two extra multiplicity units beyond their mandatory heavy unit. The four-block side is reduced to four aligned K4 tracks; in K4-e, all 24 cross pairs are exactly five edges and the six-block heavy graph is a matching. Each column now satisfies the exact 5,5,5 triangle theorem: the A/B matchings are equal or have the single transposition fixed by the heavy A-B extra edge. The former 20,788/16 one-column count is RETRACTED. Corrected exact replay gives 20,842 states (70 AB-switched), after correcting the 5,5,5 theorem to 66 valid configurations per transposition. Each fixed row and column uses at most two matching permutations, but the whole grid may use more than two. Need classify all six-column 4,5,5/5,5,5 compatibilities, degree equations, and residual incidence.
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
