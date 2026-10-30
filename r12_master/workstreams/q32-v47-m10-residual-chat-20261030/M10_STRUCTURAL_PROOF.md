# M10 structural reductions and proved conditional branches

Status: partial structural proof; full-support m=10 Q32 remains OPEN.

## 1. Exact disconnected light-component theorem

Let L be the graph on the ten pivot blocks Q_i, with ij light exactly when e_H(Q_i,Q_j)=4. Put k_ij=e_H(Q_i,Q_j)-4, t_i=sum_j k_ij, and y_i=sum_{r in R}(|N(r) intersect Q_i|-1). The six-unit core excess is

    s_i=t_i+y_i-5>=0
    sum_i s_i=2X+Y-50<=6.

If S is a connected component of L of size k<=5, every pair from S to its complement is heavy. Therefore t_i>=10-k for each i in S and

    s_Q>=k(5-k)+Y_S.

If L had at least three components, two of them would have size at most four and would consume at least 4+4=8 units, contradicting s_Q<=6. Thus, if L is disconnected, it has exactly two components. Their sizes are exactly one of 1+9, 2+8, 3+7, 4+6, 5+5.

This is a theorem about disconnected L only. It does not prove that L is disconnected.

## 2. Component-by-component reductions

### 1+9

The singleton block has t_i>=9 and s_i>=4. Hence s_R<=2, Y+2Z<=10, Z<=5, and (t_i-9)+y_i<=2. Thus the nine cross pairs carry one mandatory heavy unit each and at most two extra multiplicity/slack units in total; the singleton has y_i<=2. OPEN.

### 2+8

The component inequality forces s_Q=6 and s_R=0. The two small blocks A,B form a light edge, have y_A=y_B=0 and t_A=t_B=8. Each of the sixteen A/B-to-outer pairs has exactly five edges. For the eight-block component T,

    t_j^T+y_j=3
    X_T=8+Z
    Y=8-2Z
    Z<=4
    delta(L[T])>=4.

The two-block transversal blocker proves that the unique-neighbor maps of A and B agree after aligning their perfect matching. The 4,5,5 switch lemma restricts each outer block to aligned matchings or a synchronized transposition switch. Singleton and double-track blockers impose the retained fiber-size and residual-degree bounds. These are strong local restrictions, but the weighted outer graph and its eight block completions have not been eliminated. OPEN.

### 3+7

The three-block component is a light triangle; its blocks have zero residual-incidence slack. Each small-to-outer pair has exactly five edges. The outer component satisfies t_j^T+y_j=2, X_T=3+Z, Y=8-2Z, Z<=4, and minimum light degree at least four. The outer light-holonomy theorem aligns all four matching tracks across the seven outer blocks. The Astra five-contract promotion audit is in M10_UPSTREAM_PROMOTION_AUDIT.md. Once those five properties hold, the Astra theorem excludes all eighteen residual path/cycle types, including all empty-fiber cases. PROVED_CONDITIONAL on entering the 3+7 split; not a universal m=10 closure.

### 4+6

For the four-block component S and six-block component T,

    2 X_S + delta_ST + Y_S <= 2.

Thus S has at most one unit of internal heavy-pair weight, and its light graph is K4 or K4 minus one edge. The 24 cross pairs are heavy; their total multiplicity beyond the mandatory one per pair is at most two. The K4/K4-e component is now reduced to four aligned K4 tracks by the dense-component core lemma. In the K4-e subcase, all 24 cross pairs are exactly five edges, the six-block internal heavy graph is a matching, and X_T=Z-1. The 4-by-6 cross matching/extra-edge grid remains OPEN.

### 5+5

There are 25 heavy cross pairs. The ledger gives

    Y+Z<=7
    Z>=1
    2(delta_ST+X_S+X_T)+Y<=6.

Hence at most three weighted heavy units beyond the mandatory cross pairs can be spent on internal heavy pairs or cross multiplicity, and each five-block component has at least seven light pairs. Each five-block component now contains an aligned four-block K4/K4-e core; the fifth fringe block has at least one light neighbor in that core. At least 13 of the 16 cross-core pairs are exactly five edges. The cross-core 4-by-4 matching grid and both fringe attachments remain OPEN.

## 3. Connected light-block graph

If L is connected, it has ten vertices and at least 17 light edges, because X<=28 and the number of heavy pairs is at most X. The disconnected component bound does not apply to a single ten-vertex component. The current source files do not prove a global matching holonomy theorem for this case. OPEN.

## 4. Residual graph classification

The broader necessary-condition catalog is in M10_RESIDUAL_CLASSIFICATION.md and M10_RESIDUAL_GRAPH_CATALOG.csv. It includes connected residual graphs, all residual graphs satisfying the scalar alpha/clique-cover/incidence constraints, and all four-clique-fiber maps on their isomorphism representatives. It does not couple them to the ten-block weighted graph or the Type-I source placements.

## 5. No over-promotion

The local Astra theorem excludes the 3+7 contract only. The eight-vertex isolated-double audit excludes its T_0-centered subcase but retains a large-track-centered exception. The nine-vertex two-isolated-double source mode has not been endpoint-classified. Therefore no contradiction in this file excludes all m=10 Q32 candidates.


## 6. New dense-component core reduction

See M10_DENSE_COMPONENT_CORE_LEMMA.md for the full proof. The 4+6 small component always contains four aligned K4 tracks; its K4-e subcase has exact five-edge cross pairs and a matching as the six-block internal heavy graph. Each side of a 5+5 split contains a four-block aligned K4/K4-e core. These are reductions, not terminal contradictions.


## 7. RETRACTED former 5,5,5 / one-column reduction

The former 1,872-count 5,5,5 classifier and 20,788-state one-column catalog are incorrect. The exact 5,5,5 replay has 2,124 valid configurations, with 66 for each transposition, and the corrected one-column catalog has 20,842 states. See M10_555_CLASSIFICATION_RETRACTION.md and the corrected M10_555_TRIANGLE_AND_CROSS_GRID_SWITCH_LEMMA.md. No six-column endpoint conclusion from the former fixed-switch rule may be imported.


## 8. Corrected 4+6 K4-e local classification

The corrected exact 5,5,5 theorem and one-column enumeration are recorded in M10_555_TRIANGLE_AND_CROSS_GRID_SWITCH_LEMMA.md. The 41,472 normalized 5,5,5 inputs yield 2,124 valid configurations (1,728 identity and 66 per transposition). The corrected one-column catalog has 20,842 states (20,772 AB-aligned, 70 AB-switched). For every fixed row and every fixed column of the 4-by-6 matching matrix, the matching values take at most two distinct permutations. This does not imply a two-permutation global grid. The six-column compatibility, degree equations, and residual-fiber coupling remain OPEN.
