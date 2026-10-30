# Dense-component core lemma for the 4+6 and 5+5 cells

Date: 2026-10-30  
Status: PROVED_CONDITIONAL on the registered pivot-block slack ledger.

## 1. The four-block core in the 4+6 cell

Let S be the four-block component and T the six-block component. The component ledger gives

    2 X_S + delta_ST + Y_S <= 2,

where X_S is the weighted heavy-pair sum internal to S, delta_ST is the cross-pair multiplicity beyond the mandatory one unit on each of the 24 cross pairs, and Y_S is the residual-incidence slack on S. Thus X_S is either zero or one.

**Lemma.** The four blocks in S can be relabelled so that every pair contains the same identity perfect matching. Hence their sixteen vertices contain four aligned K4 tracks.

**Proof.**
- If X_S=0, all six pairs in S are light. Each pair is exactly a perfect matching. Triangle consistency from the two-light matching-composition theorem makes all six matchings globally consistent; relabel the four blocks to make them identity.
- If X_S=1, exactly one pair, say C,D, is heavy with k_CD=1; the other five pairs are light, so L[S]=K4-e. Let A,B be the other two blocks. The paths C-A-D and C-B-D are both two-light paths. Matching composition puts both composed perfect matchings into the C-D pair graph. That pair has exactly five edges and therefore has a unique perfect matching: two distinct perfect matchings would have a union of at least six edges. The two compositions coincide. Relabelling along the five light pairs therefore makes the C-D matching identity as well. Its one extra edge is off the matching. QED.

The K4-e subcase is even more rigid at the scalar level: X_S=1 forces delta_ST=Y_S=0. All 24 cross pairs have exactly five edges. Since s_Q=6, s_T=0; every j in T satisfies t_j^T+y_j=1. Consequently the internal heavy graph on T is a matching, X_T=Z-1, Y=8-2Z, and 1<=Z<=4. Thus L[T] is K6 minus a matching of size Z-1.

The K4-e, Z=4 slice of this grid is now closed by M10_K4E_Z4_GLOBAL_GRID_CLOSURE.md. The K4-e cases Z=1,2,3 and the separate K4 small-component branch remain open; the latter now has a tightened residual and outer-ledger normal form in M10_4PLUS6_TIGHT_RESIDUAL_FILTER.md.

## 2. Four-block cores inside each 5-block component

In the 5+5 cell, write X_S and X_T for the internal weighted-heavy sums. The six-unit ledger gives

    2(delta_ST+X_S+X_T)+Y<=6,

so delta_ST+X_S+X_T<=3. In particular, each five-block component has at most three internal heavy pairs, counted with multiplicity.

**Lemma.** Each five-block component contains a four-block subset whose induced light graph is K4 or K4-e. The four blocks in that subset can be relabelled to give four aligned K4 tracks. The fifth block is light-adjacent to at least one block of the core.

**Proof.** Let W be the simple graph of internal heavy pairs in one five-block component, and let h be its number of edges. Its weighted edge sum is at most three.
- If h=3, all three weights are one. A three-edge graph on five vertices has a vertex incident with at least two of the edges. Delete that vertex; at most one heavy pair remains.
- If h=2, delete an endpoint of a heavier edge; the remaining internal heavy weight is at most one.
- If h=1, delete an endpoint; if h=0, delete any vertex.

The remaining four blocks therefore induce either K4 or K4-e in the light graph. The 4+6 four-block lemma above aligns their matching tracks. The deleted fringe block has at most three heavy neighbors among the other four, so it has at least one light neighbor in the core. Its matching to that neighbor is compatible with the core labels. QED.

Apply this independently to both five-block components. The 25 cross pairs are all heavy, and at most three extra multiplicity units occur across them. Therefore at least 22 of the 25 cross pairs have exactly five edges; in particular at least 13 of the 16 pairs between the two four-block cores have exactly five edges. The cross-core 4-by-4 matching grid, the two fringe blocks, and the residual fibers remain OPEN.

## 3. Scope

These lemmas reduce the 4+6 and 5+5 cells to aligned four-block cores. The K4-e, Z=4 slice is now closed; the remaining 4+6 cases and the 5+5 cross-core grid remain open. They use only the registered component ledger, the exact 4-edge matching property, and the two-light matching-composition theorem.


## 5. K4-e, Z=4 global terminal

The entire K4-e, Z=4 branch is excluded by M10_K4E_Z4_GLOBAL_GRID_CLOSURE.md. The proof covers both possible 2-regular residual graphs, all small/outer residual clique-fiber profiles, and every six-column cross matching/extra-edge grid. It uses the exact pointwise outer degree cap and the corrected local switch theorems. The remaining 4+6 cases are K4 on the small side and K4-e with Z=1,2,3. This does not close full-support m=10.

## 6. Tight 4+6 frontier after the K4-e, Z=4 closure

The remaining 4+6 branches have sharper residual budgets. If the small component is K4, then 4+delta_ST+Y_S<=s_Q<=6, so delta_ST+Y_S<=2, s_R<=2, and B_min(R)<=10-2z. The six-block outer degree equations reduce to x_T<=4 and delta_ST+Y_S+sum(s_j)<=2; see M10_4PLUS6_TIGHT_RESIDUAL_FILTER.md.

If the small component is K4-e, the Z=1,2,3 residual budget is B_min(R)<=8-2Z; the Z=4 case is already closed. The exact filtered catalogs and the outer-ledger replay are in the same new note and verifier.
