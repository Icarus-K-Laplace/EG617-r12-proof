# Independent reconstruction of the hereditary minimum-degree gate

Date: 2026-10-30. Status: **PROVED**.

This document reconstructs the source gate reported by the Q33 workstream, including its 121/122-edge classification. It does not assume that classification as a black box and does not require the archived 127-row certificate. The latter concerns a different low-edge floor argument.

Write p12(n)=12 binom(q,2)+qr for n=12q+r, 0<=r<12, and D(n)=binom(n,2)-11 p12(n). Define R(a,n) to consist of simple n-vertex graphs with alpha<=a, omega<=11 and e(J[U])<=D(|U|) for EVERY vertex subset U. Induced subsets retain the caps and clique bound.

**Theorem M:** J in R(4,47) and e(J)<=286 imply delta(J)>=12.

## M1. R(2,24) is empty

In a putative J, the nonneighbors of any vertex form a clique of order at most11. Thus delta(J)>=12. Since D(24)=144, J is exactly 12-regular. Its complement L is triangle-free and 11-regular. It is non-bipartite because alpha(L)=omega(J)<=11, while a bipartition of 24 vertices has an independent side of size at least12.

Take a shortest odd cycle of length 2k+1, k>=2. It is chordless, and each outside vertex has at most k neighbors on it. Summing L-degrees on the cycle gives

    11(2k+1)<=2(2k+1)+k(23-2k),
    2k^2-5k+9<=0.

The discriminant is -47 and the leading coefficient is positive. Contradiction.

## M2. Near-extremal triangle-free graphs on 23 vertices

Let W be triangle-free, |W|=23, alpha(W)<=11 and e(W)>=121. It is non-bipartite. The shortest-odd-cycle bound B(n,k) proved in COMMON_NEIGHBORHOOD_CAPACITY.md gives max_k B(23,k)=122, with B(23,k)<=119 for k>=3. Thus a shortest odd cycle is C5.

Let X be the other18 vertices. Each x in X has at most two C5-neighbors. Since e(W)>=121,

    e(W[X])>=121-5-36=80.

A non-bipartite triangle-free graph on18 vertices has at most max_k B(18,k)=73 edges, so W[X] is bipartite. Its bipartition sizes and missing edges force exactly three possibilities: K9,9, K8,10, or K9,9 minus one edge. Indeed, 18 vertices with at least80 bipartite edges require part sizes9,9 or8,10; their products are81 and80.

Number the cycle vertices by Z/5Z. A two-neighbor type is T_i={i-1,i+1}; a vertex of this type is a clone of cycle vertex i. Two adjacent exterior vertices must have disjoint types. The compatibility graph on the five T_i is itself C5: T_i and T_j are disjoint exactly when i,j are adjacent cycle labels.

For a complete bipartite exterior with all vertices of two-neighbor type, the nonempty type sets S_A,S_B satisfy S_A x S_B subset E(C5). One side has a single type; the other has at most its two neighboring types. To see this, two distinct types on one side can have a common compatible type only if they are distance two on C5, in which case that common type is unique; three distinct types have none. There are exactly20 ordered nonempty compatible type-set pairs, independently enumerated by the verifier.

### M2a. 122 edges

All bounds are equalities: the exterior is K9,9 and every exterior vertex has two cycle neighbors. The type observation gives exactly the blowups

    C5(10,a,1,1,b), a+b=11, 1<=a,b<=10.               (M2a)

Here C5(s0,...,s4) means independent classes of those sizes, complete between consecutive classes and with no other edges.

### M2b. 121 edges with K9,9 exterior

The cycle-to-exterior count is35, so precisely one exterior vertex u has a singleton cycle-neighborhood and the other17 have two-neighbor types. Removing u leaves a complete K8,9 between two-neighbor vertices. The type sets still obey the preceding observation.

The singleton neighborhood of u extends to a compatible two-neighbor type. If the opposite side uses a single type T_j, each of the three available cycle vertices belongs to an independent pair disjoint from T_j. If it uses two types, their union has three vertices and its two-vertex complement is an independent pair, so again the extension exists. Adding this one cycle edge gives a triangle-free 122-edge graph; it still has alpha<=11 because adding edges cannot increase independence number. Therefore W is an edge-deleted member of (M2a).

### M2c. 121 edges with K8,10 exterior

All exterior vertices have two-neighbor types. If the single-type side has size L and the opposite side size R, the whole graph is C5(L+1,a,1,1,b), a+b=R+2. Its independence number is at least max(L+2,R+2)>=12 for {L,R}={8,10}. This case is impossible.

### M2d. 121 edges with K9,9 minus uv

All exterior vertices have two-neighbor types. Delete the endpoints u,v of the missing cross edge. The remaining K8,8 has type sets S_A,S_B as above. If u,v have compatible types, adding uv gives a 122-edge graph, so again W is an edge-deleted member of (M2a).

If they are incompatible, both S_A and S_B must be singletons. For example, if S_A has two types, S_B is its unique common compatible type; v must have that same type, while u must be compatible with it, contradiction. Label the singleton types 0 and1. The only incompatible choices for u and v consistent with their other cross edges are respectively2 and4 (up to reversing/rotating the cycle). Consequently the whole graph is

    C5(9,9,2,1,2).                                  (M2d)

The verifier checks every compatible S_A,S_B and every endpoint type; exactly ten oriented incompatible endpoint cases occur, all of this form.

This proves the full 121/122 classification used below. No uninspected archive lemma is required.

## M3. A 12-set with low cost against any independent set

For each W in M2 and any independent set I of W, there is a 12-set T with

    e(W[T])+|T intersect I|<=6.                       (M3)

For (M2a), name the consecutive classes P,A,s,t,B with sizes10,a,1,1,b. Use T0=P+s+t, T1=A+B+s, T2=A+B+t; each has12 vertices. Every independent I is contained in one of the maximal class-pairs P+s, P+t, A+B, A+t, B+s.

- I subset P+s: choose between T1,T2, giving cost at most min(a+1,b)<=6.
- I subset P+t: cost at most min(a,b+1)<=6.
- I subset A+B: T0 has cost1.
- I subset A+t or B+s: T0 has cost at most2.

For an edge-deleted member, these choices still work if I was independent before deletion. Otherwise I contains the two deleted endpoints. It contains no further vertex in either endpoint class and is contained in those endpoints together with the unique cycle class nonadjacent to both. For deleted edges of types P-A, A-s, t-B, B-P, T0 has cost at most3,2,2,3 respectively. Deleting s-t would create the independent12-set P+s+t and violates alpha(W)<=11. Any other deletion that creates an independent12-set is also discarded by the same premise.

For (M2d), name the consecutive classes P,Q,C,d,E of sizes9,9,2,1,2. The sets T1=P+C+d and T2=Q+d+E each have12 vertices and exactly two W-edges. Every independent I is contained in P+C, P+d, Q+d, Q+E or C+E. One of T1,T2 then intersects I in at most two vertices. The cost is at most4.

The independent verifier constructs every family member and one deletion representative of every cycle-class edge type, enumerates maximal independent sets directly, and checks the proposed 12-sets. Symmetry within each class covers every edge deletion.

## M4. Every R(3,35) graph has minimum degree12

Let J be in R(3,35). A vertex of degree at most10 has at least24 nonneighbors; any 24 of them belong to R(2,24), contrary to M1. Thus delta(J)>=11.

Suppose d_J(v)=11. Put L=complement(J), W=N_L(v), and R=V(J) minus (W union {v}); their sizes are23 and11. The graph L[W] is triangle-free and has independence number at most11. The cap D(23)=132 gives

    e(L[W])=253-e(J[W])>=121.

Hence M2 applies. Since R union {v} cannot be L-independent of size12, there is an edge xy in L[R]. Its common neighbors I in W form an independent set of L[W], since otherwise xy and an edge of I make K4 in L, contrary to alpha(J)<=3.

Choose T by M3. Each point in T minus I is J-adjacent to at least one of x,y. Therefore

    e(J[T union {x,y}]) >= 66-e(L[T])+12-|T intersect I|
                         >=78-6=72>D(14)=69.

This contradiction proves delta(J)>=12, and hence e(J)>=210. The distinct vertices x,y lie outside W, so the 14-set and every counted edge are legitimate.

## M5. Orders36 and37

For J in R(3,36), a vertex of degree at most11 has a 24-point nonneighborhood, excluded by M1. If a vertex has degree12, delete one of its neighbors: the resulting R(3,35) graph has that vertex of degree11, contrary to M4. Thus delta(J)>=13 and e(J)>=234.

For J in R(3,37), degree at most12 is excluded by M1. Thus e(J)>=ceil(37*13/2)=241>D(37)=237. Consequently R(3,37) is empty.

## M6. Transport to order47

Let v have minimum degree d in J in R(4,47). If d<=9, its nonneighborhood contains a forbidden R(3,37).

If d=10, put S=N(v) and C=V minus N[v]. Then C is in R(3,36), so e(C)>=234. Since every vertex of S has degree at least10,

    10+2e(S)+e(S,C)>=100,
    e(S)+e(S,C)>=90-e(S)>=45,
    e(J)>=234+10+45=289.

No assumption that S is a clique is made.

If d=11, then C is in R(3,35), so e(C)>=210. Let M=complement(J[S]), z=e(M), and g_a=d_J(a)-11>=0. The shell S is not K11, because S+v would be K12, so z>=1. Its rows D_a=N_J(a) intersect C have sizes t_a=d_M(a)+g_a.

For any missing shell edge ab, |D_a union D_b|>=12: otherwise C contains a 24-set anticomplete to nonadjacent a,b, hence a member of R(2,24). Also d_M(a)+d_M(b)<=z+1. Thus

    z+sum_S g >= t_a+t_b-1 >=11.

The disjoint edge partition gives

    e(J)=e(C)+66+z+sum_S g>=210+66+11=287.

Therefore e(J)<=286 excludes every d<=11, proving Theorem M.

## Dependency and promotion scope

Only alpha, omega and the induced caps D(14)=69, D(23)=132, D(24)=144, D(37)=237 are load-bearing. This theorem has no E407/E408, charge, source-color, V11, Q32, Q33, MS-29 or selected-witness hypothesis. It therefore transfers to EACH parent core independently once these caps and e(H)<=286 are established. It does not say minimum degree12 follows from the edge count alone.
