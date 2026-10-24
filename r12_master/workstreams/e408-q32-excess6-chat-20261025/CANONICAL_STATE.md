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
- α(H)≤4 and δ(H)≥12;
- total core excess Σ_H(d_H(x)-12)=2·285-47·12=6;
- q=32, equivalently e(M)+G_A=32 for M=complement of F[A] and G_A=Σ_{a∈A}(d_F(a)-13).

The 284-edge/excess-four result used for E407 Q32 and E408 Q33 is not imported.

## Main new theorem

Under the registered E408 seven-block equality system and Kang–Pikhurko exact-129 Type-I classification:

1. The number m of exact-129 non-target colors is 8, 9, or 10.
2. Each exact-129 color has twelve pairwise-disjoint 5-cliques: ten isolated K5 components plus two K5 cliques inside the 11-point exceptional gadget. Every clique meets {p}∪A because α(H)≤4. The outside-H budget is fourteen vertices; depending on whether the gadget exceptional vertex lies in H, at least ten of the twelve cliques have exactly one outside-H vertex.
3. Removing the unique outside vertex from each such clique gives an independent 4-set Q⊂H. Witnesses are disjoint within one color and intersect in at most one core vertex across different colors. Hence N≥10m, without assuming M[B]=∅.
4. The correct 285-edge capacity inequality is (6N\le \binom v2-p_4(47-v)-12v+285-E_U). Capacity alone gives v≥37,39,41 for m=8,9,10; combining with ten disjoint witnesses from one color gives preliminary floors **v≥40,40,41**.
5. The new low-support triple-pair capacity theorem improves this to **v≥44 for every m∈{8,9,10}**. If v≤43, the two double-shell cliques per exact color yield two disjoint core triples, and their pairs inside W=H\U are globally edge-disjoint. The exact pair budget rules out v=40,41,42,43 without assuming M[B]=∅.
6. At v=44, W has three vertices. At most three colors can have their exceptional vertex in O_C=U\Q_C, and at least m−3 colors have each of their two core triples containing exactly one W vertex. This is the current strict terminal, not a complete contradiction.

## Seven-block coupling

For an exact-129 color C, the outer blocker theorem gives M_C≥15+P_C, where P_C is the block-block duplicate count and M_C counts size-five blocker occurrences. At most two isolated K5 components per color fail to be one-outside-H witnesses, and each isolated component can be used as a size-five blocker at most once per outer block. Thus at least ceil((P_C+1)/7) distinct isolated witness components of C are used as outer blockers.

Using Σ_{exact C}P_C≥62m-427, the seven-block system forces at least 9m-61 distinct isolated witness components to be used as blockers across exact colors: at least 11, 20, or 29 for m=8,9,10 respectively. If k exact colors have their exceptional gadget vertex outside H, this lower bound strengthens to 9m-61+k.

This is a genuine cross-interface constraint, not yet a contradiction.

## Shell-support firewall

The target 14-set {p}∪A contains at most 69 edges of the target color: each of the eleven other colors must contribute at least two edges on any 14 vertices, or it would have an independent 13-set. Since e_F({p}∪A)=91-e(M), this gives 22≤e(M)≤32 and 0≤G_A=32-e(M)≤10.

The split into S and B with |S|=3, |B|=10 is **not assumed**. The companion classification file treats both the branch where a 10-point B with M[B]=∅ exists and the branch where every 10-point B has M[B]≠∅. The capacity theorem above is uniform across both.

## Dependencies and limits

- The outer decomposition into seven target K12 blocks, e_C(R)=129+s_C, Σs_C=3, and P_C+R_C+s_C=62 is conditional on the registered outer embedding ledger.
- The twelve disjoint K5 cliques per exact-129 color are from the registered Kang–Pikhurko Type-I equality classification recorded in front_end/E408_EXACT129_BLOCKER_DUPLICATE_THEOREM.md. This workstream derives the witness floor from that structure; it does not reprove the external classification.
- No SAT/ILP instance is claimed complete, no graph realization is claimed, and no parent K145-to-T61 bridge is promoted.
- The exact support-capacity arithmetic is independently replayed by verify_core285_capacity.py.

EG617(r=12) remains OPEN / NOT_CERTIFIED.
