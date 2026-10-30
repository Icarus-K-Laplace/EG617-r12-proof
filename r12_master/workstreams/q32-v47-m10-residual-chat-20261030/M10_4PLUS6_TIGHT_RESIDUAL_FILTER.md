# 4+6 tight residual and outer-ledger reductions

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL necessary-condition reductions; no full Q32 closure.**

This note tightens both remaining 4+6 branches using the existing complete 371-type residual catalog. It does not assume a residual graph type or fiber profile beyond the registered m=10 contract.

## 1. Common residual constraints

Let R be the seven-vertex residual, e(R)=3+z, alpha(R)<=4, and theta(R)<=4, where theta is the clique-cover number. For r in R, put b_r=sum_i(|N(r) intersect Q_i|-1). Then
\[
B_{\min}(R):=\sum_{r\in R}\max(0,2-d_R(r))\le y=\sum_r b_r.
\]
The full residual catalog M10_RESIDUAL_GRAPH_CATALOG.csv is complete for the broader bound B_min<=14-2z. We now filter it by the sharper component-specific budgets below.

## 2. K4 small-component branch

Suppose the four-block component S has light graph K4, so X_S=0. Let delta be the total multiplicity above the mandatory one extra edge on the 24 cross pairs, and Y_S the residual-incidence excess on the four small blocks.

The exact component ledger is
\[
4+\delta+Y_S\le s_Q\le6,
\]
hence
\[
\delta+Y_S\le2,\qquad s_R=6-s_Q\le2.
\]
Since s_R=y+2z-8, we get
\[
B_{\min}(R)\le y\le10-2z,\qquad 0\le z\le5.
\]
Thus the K4 branch needs only the residual graph types in the generic catalog satisfying B_min<=10-2z.

The filtered catalog contains:

| z | e(R) | Isomorphism types | Labelled residual graphs | Clique-fiber maps | Connected types |
|---:|---:|---:|---:|---:|---:|
| 0 | 3 | 1 | 105 | 24 | 0 |
| 1 | 4 | 3 | 1,785 | 96 | 0 |
| 2 | 5 | 10 | 12,180 | 528 | 0 |
| 3 | 6 | 27 | 43,092 | 2,088 | 6 |
| 4 | 7 | 29 | 53,070 | 4,272 | 18 |
| 5 | 8 | 9 | 11,550 | 2,592 | 8 |
| **Total** | — | **79** | **121,782** | **9,600** | **32** |

All 79 representatives and their fiber-map counts are in M10_4PLUS6_TIGHT_RESIDUAL_FILTER.csv. The only possible sorted nonempty clique-fiber profiles across this branch are
\[
(2,2,2,1),\ (3,2,1,1),\ (3,2,2,0),\ (3,3,1,0).
\]
These are necessary residual profiles, not claims that the corresponding ten-block incidences extend.

### 2.1 Outer weighted-heavy graph ledger

Write T for the six-block component. Let:
- x_T=sum_{j<k in T} k_jk be its internal weighted-heavy total;
- delta_j be the cross-pair multiplicity excess incident with outer block j, with sum_j delta_j=delta;
- y_j be its residual-incidence excess;
- t_j^T=sum_{k in T minus {j}} k_jk;
- s_j=sum_{q in Q_j}(d_H(q)-12)>=0.

Every outer block has four mandatory heavy cross pairs, so its exact degree-sum equation is
\[
t_j^T+\delta_j+y_j=1+s_j.
\tag{2.1}
\]
On the small side, each block has six mandatory heavy cross pairs and hence s_i=1+delta_i+y_i. Summing the four small blocks and using s_Q<=6 gives
\[
\boxed{\delta+Y_S+\sum_{j\in T}s_j\le2.}
\tag{2.2}
\]
Summing (2.1) over T, using sum_j t_j^T=2x_T, yields
\[
Y_T=6+\sum_js_j-2x_T-\delta.
\tag{2.3}
\]
Finally x=24+delta+x_T, y=Y_S+Y_T, and x+y+z=32 give
\[
\boxed{z=2+x_T-Y_S-\sum_js_j.}
\tag{2.4}
\]
Since Y_T>=0, (2.2)-(2.3) imply x_T<=4. The 4+6 component bound gives z<=5.

An exhaustive integer enumeration of the six-vertex weighted graph W=(k_jk), the cross excess allocation (delta_j), Y_S, and the six nonnegative block surpluses (s_j), subject to (2.1)-(2.4) and y_j>=0, gives:

| z | Labelled outer-ledger states | Internal weight x_T values and counts | Weighted-graph isomorphism types |
|---:|---:|---|---:|
| 0 | 28 | 0:28 | 1 |
| 1 | 469 | 0:49, 1:420 | 2 |
| 2 | 2,272 | 0:22, 1:555, 2:1,695 | 5 |
| 3 | 3,540 | 1:165, 2:1,365, 3:2,010 | 8 |
| 4 | 1,110 | 2:180, 3:555, 4:375 | 7 |
| 5 | 15 | 3:15 | 1 |
| **Total** | **7,434** | — | **14** |

Across all z, there are 1,036 distinct labelled weighted outer graphs and only 14 weighted-graph isomorphism types. This is a block-degree-sum normal form; it does not impose the 4-by-6 cell endpoint constraints, residual-map compatibility, or source-color ownership.

## 3. K4-e small-component branches Z=1,2,3

If S is K4-e, the registered ledger
\[
2X_S+\delta+Y_S\le2,\qquad X_S=1
\]
forces delta=Y_S=0. The outer heavy graph is a matching of size Z-1, y=8-2Z, and s_R=0. Hence
\[
B_{\min}(R)\le y=8-2Z.
\]
The Z=4 branch is already closed in M10_K4E_Z4_GLOBAL_GRID_CLOSURE.md; for the remaining Z=1,2,3, filtering the complete residual catalog gives:

| Z | e(R) | Isomorphism types | Labelled residual graphs | Clique-fiber maps | Connected types |
|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 3 | 1,785 | 96 | 0 |
| 2 | 5 | 6 | 5,880 | 384 | 0 |
| 3 | 6 | 6 | 3,997 | 696 | 1 |
| **Total** | — | **15** | **11,662** | **1,176** | **1** |

The six Z=3 residual types are especially small:

| graph6 representative | H[R] component type | Clique-fiber profile(s) and map counts |
|---|---|---|
| FCc\`G | 2C3 union K1 | (3,3,1,0):24; (3,2,1,1):144 |
| F\`__g | C4 union P3 | (2,2,2,1):96 |
| Fh?GW | C3 union P4 | (3,2,2,0):24; (3,2,1,1):72; (2,2,2,1):72 |
| FhCK? | P7 | (2,2,2,1):96 |
| FhEG? | C6 union K1 | (2,2,2,1):48 |
| Fhc?G | C5 union P2 | (2,2,2,1):120 |

In particular, the empty-fiber profiles at Z=3 occur only on 2C3 union K1 and C3 union P4; the sole connected residual type is P7.

## 4. Verification boundary and next interface

verify_m10_4plus6_tight_reductions.py:
1. rechecks every retained graph6 representative, its edge count, B_min, alpha(R)<=4, clique-cover number at most four, and all 4^7 labelled clique-fiber maps;
2. checks orbit-stabilizer sums against the exact labelled residual counts;
3. enumerates the full six-vertex outer weighted-ledger relaxation and verifies all 7,434 states and the 14 isomorphism types.

This is a reproducible necessary-condition reduction. It does not close the K4 small-component branch or K4-e Z=1,2,3, and does not certify full-support m=10 Q32 or the EG617 root.
