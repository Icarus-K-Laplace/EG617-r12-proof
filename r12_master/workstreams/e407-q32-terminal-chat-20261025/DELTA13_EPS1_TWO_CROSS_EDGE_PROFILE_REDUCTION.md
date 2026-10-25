# E407 Q32: exact two-cross-edge reduction for the remaining delta-13, epsilon_U=1 profile

Date: 2026-10-25  
Status: PROVED_CONDITIONAL structural reduction; terminal still OPEN.  
Scope: the 47-vertex, 284-edge core; four-partite L=complement of H[U]; H[W]=2K4 union 2K5 plus exactly two cross-edges.

## 1. Frozen contract and exact ledger

Assume |H|=47, e(H)=284, alpha(H)<=4, omega(H)<=11, delta(H)>=12, and total degree excess sum epsilon_x=4, where epsilon_x=d_H(x)-12>=0. Let U have size 29 and W=H\\U size 18. Under the E407 Q32 49-witness contract,
e(H[U])=112-delta, e(H[W])=48-epsilon_U-delta, and e_H(U,W)=124+epsilon_U+2delta.
Take delta=13 and epsilon_U=1. Then e(H[U])=99, e(H[W])=34, e_H(U,W)=151, and E_W=sum over W of epsilon_w=3.

Assume L=complement of H[U] is four-partite with parts A,B,C,D of sizes 7,7,7,8. The 49 transversals force all small-small pairs to be used, so the eight H[U] cross-edges run from D to A union B union C, and each small-part vertex has at most one such edge. Write t_d=d_H[U](d,A union B union C), so sum_D t_d=8.

The W-profile consists of clique parts C1,C2 isomorphic to K4 and C3,C4 isomorphic to K5, plus two edges between distinct parts. The clique parts have 32 edges, giving the required e(H[W])=34.

For w in W, let q_w be its degree in the two-edge cross-part graph. Then d_H(w,U)=9+epsilon_w-q_w for w in a K4, and 8+epsilon_w-q_w for w in a K5. Every u in U has d_H(u,W)<=7: a small-part vertex has d_H(u,U)=6+t_u and d_H(u,W)=6+epsilon_u-t_u<=7; a D-vertex has d_H(d,W)=5+epsilon_d-t_d<=6.

## 2. Exact transversal-blocker classification for an unsaturated U-vertex

Call u in U W-unsaturated if it is not complete to any of the four clique parts. For each part C_i, let X_i=C_i minus N_H(u), which is nonempty. Every tuple in X1 x X2 x X3 x X4 must contain a W-cross-edge; otherwise that tuple together with u is an independent 5-set.

Each of the two W-cross-edges blocks a cylinder of tuples. If one edge alone blocks every tuple, its two endpoint non-neighbour sets are singletons. Otherwise, the two cylinders must each have exactly half the tuples and be disjoint: each edge has endpoint-set-size product 2, and both must use the same size-two coordinate with its two different values. If their other singleton coordinates were in different parts, then sum_i |X_i| <= 2+1+1+5=9, so d_H(u,W)=18-sum_i|X_i|>=9, contradicting d_H(u,W)<=7. Therefore every W-unsaturated u has exactly one of these forms:

**Type I — single-edge blocker.** For one cross-edge xy between parts C_i,C_j, X_i={x}, X_j={y}; the other two X-sets are arbitrary nonempty sets.

**Type II — same-pair two-edge star blocker.** Both cross-edges join the same pair of parts C_i,C_j and have form xy,x'y, with x not equal to x'. Then X_i={x,x'}, X_j={y}; the other two X-sets are arbitrary nonempty sets.

This classification is exact under the stated two-edge contract; it does not assume H[W] is anticomplete between clique parts.

### Degree consequences

- A Type-I blocker between two K5 parts forces at least 4+4=8 W-neighbours and is impossible.
- A Type-I blocker between a K4 and a K5 forces at least 3+4=7 W-neighbours. Equality is necessary, so u must be a small-part vertex with epsilon_u=1 and t_u=0. There is at most one such u, because epsilon_U=1.
- A Type-II blocker between two K5 parts forces at least 3+4=7 W-neighbours. Again it can occur only for the unique possible positive-excess U-vertex.
- A Type-II blocker between K4 and K5, or between K5 and K4, has base W-degree 6. A Type-II blocker between two K4 parts has base W-degree 5.

Thus, if both W-cross-edges lie between the two K5 parts, there is at most one W-unsaturated U-vertex: only the same-pair Type-II blocker can survive, and it requires epsilon_u=1. That subcase will be ruled out by the cover bound in Section 4.

## 3. Component common-neighbour capacities

For each W clique part C_i, define S_i={u in U: u is adjacent to every vertex of C_i}, and E_i=sum over w in C_i of epsilon_w. A W-vertex cannot be complete to two U-parts because any two U-parts have at least 14 vertices, while d_H(w,U)<=12.

Here is the reverse-saturation proof needed for this W-cross-edge profile. Let A',B',C',D' be the non-neighbour sets of a W-vertex w in the U-parts A,B,C,D. If w is not complete to any U-part, all four sets are nonempty. For each d in D', every triple in A' x B' x C' must contain an H[U] edge to d; otherwise w,d and that triple form an independent 5-set. Hence at least one of A',B',C' is entirely contained in N_H(d), and its size is at most t_d. Every small-part vertex has at most one D-neighbour, so distinct d in D' require distinct small-part sets of size at most t_d. In the present two-cross-edge contract, t_d<=2: if d is W-saturated it has at least four W-neighbours, so t_d<=1+epsilon_d<=2; if d is W-unsaturated, the Type-I/Type-II blocker classification in Section 2 gives t_d<=epsilon_d<=1. Thus |D'|<=3, and the number of U-nonneighbours of w is at most 17, 13, or 9 when |D'| is 1, 2, or 3, respectively. The case D'=empty would make w complete to D. Therefore d_H(w,U)>=12. Every K5-vertex has d_H(w,U)<=11, so all K5-vertices have unique U-part labels. A K4-vertex can be unlabelled only if it is not incident to a W-cross-edge and has epsilon_w=3; hence at most one K4-vertex is unlabelled.

**Lemma 3.1 (K4 capacity).** For either K4 part, |S_i|<=9.

If all four vertices are labelled, let ell(w)=d_H(w,U)-|P(w)| be the label load. Then sum over w in C_i of ell(w) is at most 8+E_i-r_i<=11, where r_i is the number of W-cross-edges incident to that part. If all labels agree on a small U-part, at most seven common neighbours lie in that part and each common neighbour outside it costs four load units, giving 7+floor(11/4)=9. All-D labels would give a forbidden K12. For mixed labels, multiplicity at most two gives |S_i|<=floor(11/2)=5. In the only remaining 3+1 pattern, if the majority label is a small part, its three vertices have total load at least 6-r_i; the other label can support at most 2+E_i common neighbours in the majority part, while common neighbours outside it cost at least three load units from the majority-label vertices. The total is at most (2+E_i)+floor((6+E_i)/3)<=8. If the majority label is D, its total load is at most E_i<=3, so at most one common neighbour lies outside D, while at most 2+E_i lie in D; this is below 9.

If one K4 vertex is unlabelled, it has excess 3 and the other three vertices have zero excess and total label load at most 6. Mixed labels give capacity at most 6. Three identical small-part labels give at most 7+floor(6/3)=9. Three D labels give at most seven common neighbours in D, since the unlabelled vertex is not complete to D, plus at most one outside D. So the bound 9 holds in every case.

**Lemma 3.2 (K5 capacity).** For either K5 part, |S_i|<=2+E_i.

All five vertices are labelled. The total label load is at most 5+E_i-r_i<=5+E_i. If no label occurs four times, every common neighbour costs at least two load units, so |S_i|<=floor((5+E_i)/2)<=2+E_i. A common label on all five vertices is forbidden by omega(H)<=11. If four vertices have a common small-part label P, common neighbours in P are bounded by the load of the fifth vertex, at most 1+E_i; common neighbours outside P cost four units from the four P-labelled vertices, whose total load is at most 4+E_i, allowing at most one. The sum is at most 2+E_i. If the repeated label is D, the fifth small-labelled vertex has load at most 2+E_i, and the four D-labelled vertices have total load at most E_i<=3, so there are no common neighbours outside D. This proves the bound.

The S_i are pairwise disjoint, and every W-saturated U-vertex belongs to exactly one S_i. If k denotes the number of W-unsaturated vertices in U, then
29-k=sum_i |S_i| <=9+9+(2+E_3)+(2+E_4)<=25.
Hence every candidate must have k>=4.

## 4. Stronger bound when a cross-edge meets a K4

If at least one W-cross-edge is incident to a K4, then sum_i |S_i|<=24 and k>=5.

Indeed, if some K4 capacity is at most 8, Lemmas 3.1 and 3.2 give sum_i |S_i|<=8+9+7=24. If both K4 capacities equal 9, then each is either fully labelled by one small U-part, or is the exceptional one-unlabelled pattern with all three remaining labels equal to a small part. In the latter pattern, achieving capacity 9 requires all three labelled vertices to spend their full six load units on two common neighbours outside the label part, so r_i=0 and E_i=3. The other K4 then cannot also have capacity 9 if a W-cross-edge meets a K4. Thus, if both capacities are 9, both K4s are fully labelled by small parts. Capacity 9 requires E_i>=r_i for each K4, because two common neighbours outside its label part need at least eight load units. If r_4 is the total number of cross-edge incidences at the two K4 parts, then r_4>=1, so E_3+E_4<=3-r_4<=2. The K5 capacities sum to at most 4+E_3+E_4<=6, and the total is at most 18+6=24.

If neither cross-edge meets a K4, both edges lie between the two K5 parts. Section 2 shows k<=1, while the cover bound in Section 3 forces k>=4, contradiction. Therefore any surviving candidate must have a cross-edge incident to a K4 and at least five W-unsaturated vertices in U.

## 5. What is and is not closed

**New theorem:** under the retained E407 Q32 core/witness contract and the four-partite-U hypothesis, the delta=13, epsilon_U=1, 2K4 union 2K5 plus two-cross-edge profile has no realization with fewer than five W-unsaturated U-vertices. The all-K5-cross-edge placement is excluded entirely.

This is not yet a contradiction for the full profile: the remaining exact terminal has at least five U-vertices that are not complete to any W clique part, each governed by the Type-I/Type-II blocker classification. The next task is to combine those blocker patterns with the 49-witness labelled incidence system and the component labels to rule out k>=5. E407 Q32, all five shell templates, and the original K145-to-T61 bridge remain OPEN / NOT_CERTIFIED.


## Round 30 placement cross-reference

The same-pair disjoint K4–K5 placement is now separately excluded in DELTA13_EPS1_TWO_CROSS_EDGE_K4K5_DISJOINT_CLOSED.md. In that placement the two edges are disjoint, so Type-II blockers are impossible; a Type-I blocker across K4–K5 forces seven W-neighbours and can occur at most once under epsilon_U=1, contradicting the k>=5 cover bound. The remaining four same-pair placements are listed in DELTA13_EPS1_TWO_CROSS_EDGE_PLACEMENT_REDUCTION.md.
