# E407 Q32: exclude the same-pair disjoint K4–K5 two-cross-edge placement

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained (delta=13,epsilon_U=1), four-partite-U/core contract and the component-capacity theorem in DELTA13_EPS1_TWO_CROSS_EDGE_PROFILE_REDUCTION.md.

## Theorem

Suppose (H[W]) consists of (2K_4dotcup2K_5) plus two **disjoint** cross-edges joining the same K4 component (P) to the same K5 component (Q). Then no E407 Q32 core exists under the stated contract.

## Proof

The exact transversal-blocker classification in DELTA13_EPS1_TWO_CROSS_EDGE_PROFILE_REDUCTION.md says that every U-vertex not complete to a W clique component is either:

- Type I: one cross-edge blocks every independent transversal, so the non-neighbour sets in its endpoint parts are exactly the two singleton endpoints; or
- Type II: the two W-cross-edges form a star between the same pair of parts, with a two-element non-neighbour set in one part and a singleton in the other.

Because the two edges in the present placement are disjoint, Type II is impossible. Thus every W-unsaturated U-vertex is Type I.

A Type-I blocker across a K4 and a K5 has at least
[
(4-1)+(5-1)=7
]
W-neighbours. The retained degree ledger gives (d_H(u,W)le7) for every (uin U), with equality only if (u) is a small-part vertex, (epsilon_u=1), and (t_u=0). The eight-vertex D part has (d_H(d,W)le6), so no D-vertex can be such an exception. Since (epsilon_U=1), there is at most one U-vertex with (epsilon_u=1). Therefore
[
k:=|{uin U:u	ext{ is W-unsaturated}}|le1.
]

On the other hand, at least one cross-edge is incident to a K4. The capacity theorem in Section 4 of DELTA13_EPS1_TWO_CROSS_EDGE_PROFILE_REDUCTION.md gives
[
sum_i |S_i|le24,
]
where (S_i) is the set of U-vertices complete to the (i)-th W clique part. Since the (S_i) are disjoint and cover every W-saturated U-vertex, (29-kle24), hence (kge5). This contradicts (kle1).

Therefore the same-pair disjoint K4–K5 placement is excluded. (square)

## Scope

This closes one of the five same-pair placements left by DELTA13_EPS1_TWO_CROSS_EDGE_PLACEMENT_REDUCTION.md. The remaining same-pair placements are: K4–K4 matching, K4–K4 star, K4–K5 star centred in the K4, and K4–K5 star centred in the K5. The overall (delta=13,epsilon_U=1) two-cross-edge profile, E407 Q32, and EG617((r=12)) remain OPEN / NOT_CERTIFIED.
