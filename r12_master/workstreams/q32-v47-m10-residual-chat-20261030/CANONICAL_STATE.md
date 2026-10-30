# EG617 r=12 — Q32 m=10 residual closure workstream

Date: 2026-10-30  
Branch: workstream/r12-q32-v47-m10-residual-final-20261030  
Write scope: r12_master/workstreams/q32-v47-m10-residual-chat-20261030/  
Base commit: 1de8a37556ba98ccbb8651f39a5192629453f0f1 (high-support root branch)

## Mission and firewall

This workstream attacks only the full-support Q32 terminal with m=10 exact-129 colors. It does not modify or replace the m=8,9 work of sibling Chat A, and it does not modify the high-support, case-II, Astra, or root workstreams.

The parent 47-core contract is:
- |H|=47, e(H)=285;
- alpha(H)<=4, delta(H)>=12;
- sum over v in H of (d_H(v)-12)=6;
- ten disjoint independent pivot blocks Q_1,...,Q_10, each of order four, with residual R of order seven;
- the pivot/residual slack variables satisfy the exact ledger recorded below.

The Type-I exact-color source is the published-source factorization 10 isolated K5 components plus an 11-vertex gadget G_11. This workstream preserves all source outside-count placements; it does not impose the old, invalid assumption that all ten isolated K5s are single-outside.

## Verified results entering this workstream

1. The disconnected light-block graph L has exactly two components, with sizes 1+9, 2+8, 3+7, 4+6, or 5+5. Three or more components are impossible.
2. The 3+7 graph-theoretic normal form is excluded by the Astra theorem once its five upstream properties are established. This is conditional on the 3+7 split, not a universal m=10 closure.
3. The aligned z=0,1 cell has its registered K6 contradiction.
4. The m=10 high-chromatic residual cell is excluded; the general residual graph is 4-clique-coverable.
5. The source-correct isolated-double audit identifies an eight-vertex residual branch; its exceptional large-track-centered subcase remains open.
6. The source-correct Type-I occupancy patterns also admit a two-isolated-double, nine-vertex G_11 residual mode at the aggregate outside-count level. It is not covered by the eight-vertex audit.
7. The low-support Q32 layers |U|=44,45,46 are closed on the case-II branch. This does not close full support |U|=47.

## New result in this workstream

A complete seven-vertex residual-graph relaxation catalog has been generated and independently replayed.

Necessary conditions used:
- e(H[R])=3+z, 0<=z<=7;
- alpha(H[R])<=4;
- clique-cover-number(H[R])<=4;
- B_min(R):=sum_r max(0,2-d_R(r)) <= 14-2z.

The catalog contains 371 non-isomorphic residual graphs, represented in M10_RESIDUAL_GRAPH_CATALOG.csv. It contains 797,072 labelled residual graphs in the corresponding relaxation, 93,120 ordered four-clique-fiber maps on canonical representatives, and 34,794,144 ordered pairs of such maps before joint source/matching constraints.

This is a necessary-condition catalog, not a full 47-vertex Q32 enumeration. It does not enumerate the ten-block weighted-heavy graph, source endpoint placements, all global color edge ownership, or all compatible F/G pairs.

## Current status

Status: OPEN. Full-support m=10 Q32 is not closed.

The disconnected component-size catalog is complete. The 3+7 branch is conditionally closed. The 1+9, 2+8, 4+6, 5+5 and connected-light-graph branches remain open. The source K5 occupancy catalog is complete at the aggregate outside-count level, but several endpoint-labelled source placements still need integration with the pivot-block graph.

No full-model SAT/UNSAT certificate is claimed. No root EG617(r=12) closure is claimed.
