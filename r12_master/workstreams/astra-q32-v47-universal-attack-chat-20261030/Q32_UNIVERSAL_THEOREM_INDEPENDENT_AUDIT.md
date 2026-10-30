# U6 independent theorem audit

Date: 2026-10-30  
Status: **CORE THEOREM PROVED CONDITIONAL ON THE FIVE-ITEM CORE CONTRACT; PARENT PROMOTION NOT CERTIFIED.**

## 1. Exact scope

The analytic theorem in UNIVERSAL_Q32_THEOREM.md claims that no graph H satisfies all five conditions simultaneously:

- |V(H)|=47;
- e(H)=285;
- delta(H)>=12;
- alpha(H)<=4;
- omega(H)<=11.

The theorem is independent of the source-color partition, m, witness support U, and all exceptional-point placements. Its only use of the 285-edge count beyond the statement is the degree-excess identity

    sum_v (d(v)-12) = 2*285 - 12*47 = 6.

This audit separates correctness of that conditional graph theorem from proof that every genuine E408/Q32 parent supplies delta(H)>=12.

## 2. Adversarial review of the analytic proof

I checked the eight-step argument against the exact five hypotheses. No internal mathematical gap was found in the reduction or final two contradictions.

### 2.1 Low-degree vertices and the independent four-set

If q vertices have positive excess over 12, then q<=6 and their total degree is 12q+6. The remaining 47-q vertices have degree 12 and alpha at most 3 unless an independent four-set exists. The Turan lower bounds for q=1,...,6 are

    348, 344, 340, 335, 329, 323,

all larger than 285 after the incident-edge contribution is included. Thus an independent four-set I consisting entirely of degree-12 vertices exists.

Every vertex outside I has at least one neighbor in I. The five surplus incidences beyond the 43 required incidences give h=3,4,5 multi-neighbor points. For each i, the private class K_i={s_i} union P_i is a clique of size 13-d_i. Since omega(H)<=11, d_i>=2. The resulting profiles are exactly those recorded in U1.

### 2.2 The 25-point common-antineighborhood bound

For every 25-set W,

    e(H[W]) <= (25*12+6)/2 = 153.

If alpha(H[W])<=2, its complement is triangle-free. It cannot be bipartite, since that would cover W by two H-cliques of size at most 11, covering at most 22 vertices. Kang–Pikhurko Theorem 1 at n=25,r=2 gives at most

    t_2(25)-floor(25/2)+1 = 156-12+1 = 145

edges in a non-bipartite triangle-free graph. Hence e(H[W])>=300-145=155, contradiction.

Consequently, for nonadjacent u,v,

    |N(u) intersect N(v)| <= 3 + epsilon(u)+epsilon(v).

The cardinality conversion uses the common antineighborhood excluding u,v and is consistent with |V(H)|=47.

### 2.3 Completion and support reductions

The K10 completion lemma is correctly limited to at most one exterior vertex: two completions either create K12 or violate the common-neighbor bound. The two-K11 pair lemma correctly charges all six excess units to its exceptional point and two missing sets.

I checked the h=3, h=4 and h=5 support multisets, including repeated pairs and zero missing sets. The h=5 survivors are exactly:

- P: 12,13,13,24,24;
- D: 12,13,14,23,24.

The P blocker charges two disjoint mixed pairs at least 4+4=8 excess. The D aggregated pointwise degree inequality preserves overlaps at shared clique vertices and charges two mixed pairs at least 5+5=10. Both exceed the available six. Empty missing sets are retained throughout; no false assumption that every exceptional point misses every supported clique is used.

## 3. Independent finite replay performed in this audit

I independently reimplemented the finite checks in JavaScript rather than relying only on the branch's Python receipt.

- Support-orbit counts under S4 relabelling: h=3 gives 2, h=4 gives 3, h=5 gives 5.
- The only intermediate h=5 templates after the preceding analytic filters are P and D.
- Across the 90 legal mixed-pair integer cases, the P lower bound has minimum 4 at (a,b)=(2,3).
- Across the 90 legal diamond-pair integer cases, the D lower bound has minimum 5 at (a,b)=(2,2).
- Direct edge-list replay of both stored search graphs confirmed 47 vertices, 285 edges, minimum degree 12 and excess six. P has 3,256 independent 5-sets and no K12; D has 1,901 independent 5-sets and two K12s. Neither is a counterexample to U6.

The committed Python verifier receipt additionally records 8,400 D local-accounting cases, all allowed completion masks, the four source-gadget parameters, and all 90 aggregate source outside profiles. The failed searches are diagnostics only, not an UNSAT argument.

## 4. External theorem parameter audit

The only external theorem needed by U6 is Kang–Pikhurko Theorem 1 for a 25-vertex non-bipartite triangle-free graph. The parameter substitution is n=25,r=2 and gives the 145-edge upper bound above. The 61-vertex exact-129 equality classification is not used by U6; it belongs only to the separate source audit.

## 5. Acceptance boundary

Conclusion:

- The abstract five-hypothesis graph theorem U6 is mathematically proved, conditional only on its explicitly stated five-item core contract and the cited 25-point extremal theorem.
- The finite reductions and the two terminal inequalities have been independently replayed.
- This audit does **not** establish that every actual E408/Q32 parent supplies delta(H)>=12. That is a separate upstream proof obligation recorded in Q32_PARENT_CONTRACT_MAPPING.md.
- No full solver, exhaustive 47-vertex graph enumeration, or root-level EG617 closure is claimed.
