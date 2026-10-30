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

Thus S has at most one unit of internal heavy-pair weight, and its light graph is K4 or K4 minus one edge. The 24 cross pairs are heavy; their total multiplicity beyond the mandatory one per pair is at most two. The matching triangle constraints on the K4/K4-e component are not yet combined with the six-block weighted graph. OPEN.

### 5+5

There are 25 heavy cross pairs. The ledger gives

    Y+Z<=7
    Z>=1
    2(delta_ST+X_S+X_T)+Y<=6.

Hence at most three weighted heavy units beyond the mandatory cross pairs can be spent on internal heavy pairs or cross multiplicity, and each five-block component has at least seven light pairs. The two dense internal light graphs and the cross 5-edge matching system have not yet been jointly classified. OPEN.

## 3. Connected light-block graph

If L is connected, it has ten vertices and at least 17 light edges, because X<=28 and the number of heavy pairs is at most X. The disconnected component bound does not apply to a single ten-vertex component. The current source files do not prove a global matching holonomy theorem for this case. OPEN.

## 4. Residual graph classification

The broader necessary-condition catalog is in M10_RESIDUAL_CLASSIFICATION.md and M10_RESIDUAL_GRAPH_CATALOG.csv. It includes connected residual graphs, all residual graphs satisfying the scalar alpha/clique-cover/incidence constraints, and all four-clique-fiber maps on their isomorphism representatives. It does not couple them to the ten-block weighted graph or the Type-I source placements.

## 5. No over-promotion

The local Astra theorem excludes the 3+7 contract only. The eight-vertex isolated-double audit excludes its T_0-centered subcase but retains a large-track-centered exception. The nine-vertex two-isolated-double source mode has not been endpoint-classified. Therefore no contradiction in this file excludes all m=10 Q32 candidates.
