# Independent lower-order gate audit: M1–M6

Date: 2026-11-03  
Frozen source: `frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md` at integration snapshot `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

## Verdict

**NO LOAD-BEARING GAP FOUND.** I re-derived the M1–M6 chain under its exact hereditary graph contract and independently replayed the finite C5-type and 23-vertex neighborhood-cost steps in JavaScript. The conclusion is conditional on the displayed caps and on the external AES theorem used only for CORE211; it is not an uncolored Ramsey statement.

## Contract

Throughout, (R(a,n)) means an induced (n)-vertex graph (J) with:
- (alpha(J)le a);
- (omega(J)le11);
- (e(J[U])le D(|U|)) for every (Usubseteq V(J)), where (D(n)=\binom n2-11p_{12}(n)).

The cap values used below are (D(14)=69), (D(23)=132), (D(24)=144), (D(37)=237), and (D(38)=241). The induced-subgraph condition is essential.

## M1: (R(2,24)) is empty

If (Jin R(2,24)), the nonneighbors of any vertex form a clique, so (delta(J)ge12). The cap gives (e(J)le144), while the degree bound gives (e(J)ge144); hence (J) is 12-regular. Its complement (L) is triangle-free and 11-regular. It is nonbipartite because a bipartition of 24 vertices has a side of size at least12, an independent set in (L), whereas (alpha(L)=omega(J)le11).

A shortest odd cycle (C_{2k+1}) in (L) is chordless. Every outside vertex has at most (k) neighbors on it. Summing degrees on the cycle gives
[
11(2k+1)le 2(2k+1)+k(23-2k),
]
equivalently (2k^2-5k+9le0), impossible because its discriminant is (-47). No hidden regularity or connectedness assumption is needed.

## M2: the 121/122-edge triangle-free 23-point classification

For (W) triangle-free, (|W|=23), (alpha(W)le11), and (e(W)ge121), nonbipartiteness follows from the independence bound. If the shortest odd cycle has length (2k+1), then
[
e(W)le B(23,k)=2k+1+k(23-2k-1)+leftlfloor(23-2k-1)^2/4ightfloor.
]
The independently recomputed values for (k=2,ldots,11) are (122,119,114,107,98,87,74,59,42,23). Thus the shortest odd cycle is (C_5). For its 18-point exterior (X), the cross-edge count is at most36, so (e(W[X])ge121-5-36=80). A nonbipartite triangle-free graph on18 vertices has at most (B(18,2)=73) edges (and smaller bounds for longer shortest odd cycles), so (W[X]) is bipartite. At least80 edges on18 vertices force the exterior to be exactly (K_{9,9}), (K_{9,9}) minus one edge, or (K_{8,10}).

Number (C_5) by (mathbb Z/5mathbb Z) and define a two-neighbor type (T_i={i-1,i+1}). Two exterior vertices joined by an edge must have disjoint types; type compatibility is precisely adjacency of their center labels in (C_5). For nonempty type sets (A,B) on the two sides of a complete bipartite exterior, (A	imes Bsubseteq E(C_5)). Since (C_5) has no (K_{2,2}), one side is a singleton and the other has at most two types. An independent JavaScript enumeration reproduced all 20 compatible nonempty type-set pairs and all 10 incompatible missing-cross-edge endpoint cases.

The three exterior cases close as follows:

1. (K_{9,9}), 122 total edges: all36 cycle-exterior edges are present, so every exterior vertex has a two-neighbor type. The type quotient gives the blow-ups (C_5(10,a,1,1,b)), (a+b=11).
2. (K_{9,9}), 121 total edges: exactly one exterior vertex has a singleton cycle-neighborhood. Removing it leaves a complete (K_{8,9}) type system. The singleton neighbor (p) lies outside the union of opposite-side types. For every compatible type-set pair and every possible (p), an extension (q) exists such that ({p,q}=T_i) and is disjoint from all opposite-side types. The independent replay checked all55 positions with zero failures. Adding the edge to (q) produces a 122-edge member of case1; adding an edge cannot increase the independence number.
3. (K_{8,10}), 121 total edges: all exterior vertices have two-neighbor types. The resulting blow-up has an independent set of size at least (max(8+2,10+2)=12), impossible.
4. (K_{9,9}) minus one cross edge, 121 total edges: all exterior vertices have two-neighbor types. If the missing endpoints have compatible types, add the missing edge and reduce to case1. Otherwise the type sets on both remaining (K_{8,8}) sides must be singletons; the endpoint types are then forced (up to dihedral symmetry), giving (C_5(9,9,2,1,2)).

The case split is exhaustive: the exterior edge count is at least80; its bipartition product leaves only the three stated possibilities, and the total edge count leaves only 121 or122.

## M3: the 12-set cost certificate

For each (C_5(10,a,1,1,11-a)), (1le ale10), and each of the five possible cycle-class edge-deletion types, the source supplies three 12-sets. For (C_5(9,9,2,1,2)), it supplies two. Symmetry within each class reduces every edge deletion to one of these 61 representatives.

I independently enumerated maximal independent sets of all representatives. There were 49 representatives satisfying (alphale11), 12 rejected by the required (alphale11) condition, and 263 maximal independent sets in the valid representatives. For every maximal independent set (I), at least one supplied 12-set (T) satisfies
[
e(W[T])+|Tcap I|le6.
]
This extends to every independent set because the left-hand side is monotone in (I). The maximum observed minimum cost is exactly6. The replay is stored in `RECHECK_LOWER_M2_M3_JS_20261103.js` and its JSON output.

## M4: every (R(3,35)) has minimum degree at least12

A vertex of degree at most10 leaves at least24 nonneighbors; those 24 vertices have independence at most2 (otherwise add the vertex), contradicting M1.

If (d(v)=11), let (W) be the 23 nonneighbors of (v), viewed in the complement (L=overline J). Then (L[W]) is triangle-free, (alpha(L[W])le11), and (e(L[W])ge121) from (D(23)=132), so M2 applies. The 11 neighbors (R=N_J(v)) cannot be independent in (L), since that with (v) would be an independent 12-set in (L); choose an edge (xyin L[R]). Its common (L)-neighbors (I) in (W) are independent in (L[W]), since an edge inside (I) would create a (K_4) in (L), equivalently an independent 4-set in (J).

Choose (Tsubset W), (|T|=12), by M3. Every point of (T\setminus I) is (J)-adjacent to at least one of (x,y). Since (xy
otin E(J)),
[
e(J[Tcup{x,y}])ge 66-e(L[T])+12-|Tcap I|
ge78-6=72>D(14)=69,
]
contradicting the 14-point cap. Hence (delta(J)ge12).

## M5: orders 36 and 37

For (Jin R(3,36)), degree at most11 leaves a 24-set in (R(2,24)). If a vertex has degree12, deleting one of its neighbors produces an (R(3,35)) graph in which that vertex has degree11, contradicting M4. Thus (delta(J)ge13) and (e(J)ge\lceil36\cdot13/2\rceil=234).

For (Jin R(3,37)), degree at most12 leaves a forbidden (R(2,24)). Thus (delta(J)ge13) and (e(J)ge\lceil37\cdot13/2\rceil=241>D(37)=237); the class is empty.

## M6: the 47-point minimum-degree gate

If (Jin R(4,47)) and (e(J)le286), let (v) be a minimum-degree vertex.

- (d(v)le9): its nonneighbors contain an (R(3,37)), impossible.
- (d(v)=10): the 36-point nonneighborhood (C) lies in (R(3,36)), so (e(C)ge234). With (S=N(v)), (|S|=10), the degree sum on (S) gives (10+2e(S)+e(S,C)ge100). Since (e(S)le45), (e(S)+e(S,C)ge45), and (e(J)ge234+10+45=289), contradiction.
- (d(v)=11): the 35-point core (C) lies in (R(3,35)), so (e(C)ge210). Let (M=overline{J[S]}), (z=e(M)), and (g_a=d_J(a)-11ge0). Since (S) cannot be a (K_{11}), (zge1). For any edge (abin M), the union of its two core rows has size at least12; otherwise a 24-set anticomplete to (a,b), together with the nonedge (ab), would be an (R(2,24)). Also (d_M(a)+d_M(b)le z+1). Thus (z+sum g_age t_a+t_b-1ge11), and the exact edge ledger gives (e(J)=e(C)+66+z+sum g_age287>286), contradiction.

Therefore every (R(4,47)) graph with at most286 edges has minimum degree at least12. Combining this with the independently audited 285-edge and exact-286 obstructions yields the 287-edge floor.

## Audit boundary

No mathematical repair to M1–M6 was identified. The finite JavaScript replay checks the type quotient, singleton extension, explicit 23-point representatives and integer values; it does not replace the analytic reductions or the AES theorem. The 287-edge conclusion remains conditional on the stated hereditary cap contract. This note does not certify the full K145 theorem, a Lean kernel proof, or a clean-room run of the entire root verifier.
