# E408 Q32 excess-six — canonical state

Updated: 2026-10-25  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-e408-q32-excess6-20261025  
Allowed write scope: r12_master/workstreams/e408-q32-excess6-chat-20261025/

## Headline

**E408 Q32 terminal: OPEN / NOT_CERTIFIED.** This workstream proves a stronger support-capacity reduction under the registered exact-129 and seven-block contracts, but does not yet produce a graph-level contradiction.

## Frozen contract, independently rechecked

The E408 residual is a 61-vertex target graph F with e(F)=408 and a legal degree-13 pivot p. Put A=N_F(p), |A|=13, and H=V(F)\(A∪{p}), |H|=47. The E408 Q32 interface is

- e(H)=285;
- alpha(H)≤4 and delta(H)≥12;
- total core excess Σ_H(d_H(x)-12)=2·285-47·12=6;
- q=32, equivalently e(M)+G_A=32 for M=complement of F[A] and G_A=Σ_{a∈A}(d_F(a)-13).

The 284-edge/excess-four result used for E407 Q32 and E408 Q33 is not imported.

## Main new theorem

Under the registered E408 seven-block equality system and Kang–Pikhurko exact-129 Type-I classification:

1. The number m of exact-129 non-target colors is 8, 9, or 10.
2. Each exact-129 color has ten isolated K5 components plus an 11-point gadget containing two further disjoint K5 cliques. Since alpha(H)≤4, every one of these twelve disjoint K5 cliques meets the 14-point set {p}∪A. Only two outside vertices remain beyond the twelve mandatory intersections.
3. Hence at least eight of the ten isolated K5 components have exactly one vertex outside H. Removing that vertex gives an independent 4-set Q⊂H. Across all exact colors, these witnesses are pairwise linear: distinct sets intersect in at most one core vertex.
4. Therefore there are at least N≥8m witnesses. The 285-edge capacity inequality gives support-union lower bounds:
   - m=8: v=|U|≥33;
   - m=9: v≥35;
   - m=10: v≥37.
   These hold without assuming M[B]=∅ and without an unproved shell-support split.

## Seven-block coupling

For an exact-129 color C, the outer blocker theorem gives M_C≥15+P_C, where P_C is the block-block duplicate count and M_C counts size-five blocker occurrences. At most two isolated K5 components per color fail to be one-outside-H witnesses, and each isolated component can be used as a size-five blocker at most once per outer block. Thus at least ceil((P_C+1)/7) distinct witness components of C are used as outer blockers.

Using Σ_{exact C}P_C≥62m-427, the seven-block system forces at least 9m-61 distinct witness components to be used as blockers across exact colors: at least 11, 20, or 29 for m=8, 9, or 10 respectively. If k exact colors have their exceptional gadget vertex outside H, this lower bound strengthens to 9m-61+k.

This is a genuine cross-interface constraint, not yet a contradiction.

## Shell-support firewall

The target 14-set {p}∪A contains at most 69 edges of the target color: each of the eleven other colors must contribute at least two edges on any 14 vertices, or it would have an independent 13-set. Since e_F({p}∪A)=91-e(M), this gives 22≤e(M)≤32 and 0≤G_A=32-e(M)≤10.

The shell split into S and B with |S|=3, |B|=10 is **not assumed**. The companion classification file treats both the branch where a 10-point B with M[B]=∅ exists and the branch where every 10-point B has M[B]≠∅. The capacity theorem above is uniform across both.

## Dependencies and limits

- The outer decomposition into seven target K12 blocks, e_C(R)=129+s_C, Σs_C=3, and P_C+R_C+s_C=62 is conditional on the registered outer embedding ledger.
- The twelve disjoint K5 cliques per exact-129 color are from the registered Kang–Pikhurko Type-I equality classification recorded in front_end/E408_EXACT129_BLOCKER_DUPLICATE_THEOREM.md. This workstream derives the witness floor from that structure; it does not reprove the external classification.
- No SAT/ILP instance is claimed complete, no graph realization is claimed, and no parent K145-to-T61 bridge is promoted.
- The exact support-capacity arithmetic is independently replayed by verify_core285_capacity.py.

EG617(r=12) remains OPEN / NOT_CERTIFIED.
