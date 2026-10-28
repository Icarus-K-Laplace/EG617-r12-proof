# Q32 130-edge color: no core-only degree-four vertex

Date: 2026-10-28
Status: PROVED_CONDITIONAL under the registered 61-point residual contract, the 130-edge minimum-degree-four theorem, and Kang–Pikhurko Theorem 1 at (56,11).

## Contract

Let D be a non-target color on the 61-point residual with e(D)=130, alpha(D)<=12, omega(D)<=5 and delta(D)>=4. Let H be the 47-point target core with alpha(H)<=4. A core-only degree-four vertex is a vertex u in H with d_D(u)=4 and all four D-neighbors in H.

## Lemma 1: every degree-four vertex has at least five edges in its neighborhood

For any x with d_D(x)=4, put S=N_D(x) and let N be its 56 nonneighbors. Then alpha(D[N])<=11 and omega(D[N])<=5. The complement of D[N] is K12-free and not 11-partite: an 11-partition would partition N into eleven D-cliques of size at most five, covering at most 55 vertices.

Kang–Pikhurko Theorem 1 at (56,11) gives p_11(56)=1421. Therefore e(D[N])>=C(56,2)-1421=1540-1421=119.

Write a=e(D[S]) and b=e_D(S,N). The 130-edge total gives a+b<=7. Minimum degree four gives 2a+b>=12. Hence a>=5, so e(D[N_D(x)])>=5. (1)

## Theorem: no core-only degree-four vertex exists

Suppose u is a core-only degree-four vertex and S=N_D(u). Since S lies in H, it cannot induce K4: otherwise {u} union S would be a D-colored K5 inside H, contradicting alpha(H)<=4. By (1), e(D[S])=5, so D[S]=K4-e.

The edge budget forces e(D[N])=119 and exactly two S–N edges. The two endpoints a,b of the missing edge each have degree three in {u} union S, so each receives exactly one S–N edge; the two central vertices c,d receive none.

Let z be the unique external D-neighbor of endpoint a. Then N_D(a)={u,c,d,z}. The vertices u,c,d form a triangle. Since z lies in N, it is nonadjacent to u; since c,d have no neighbors in N, z is nonadjacent to c,d. Thus D[N_D(a)] is a triangle plus an isolated vertex, with only three edges. But a has degree four, contradicting (1).

Therefore no vertex of H can have degree four in D with all four D-neighbors in H. QED.

## Dependencies and scope

The proof uses no exceptional-vertex injectivity and no universal degree-nine claim. The external extremal input is Kang–Pikhurko Theorem 1 at (56,11); the minimum-degree-four premise is the registered 130-edge theorem. The argument is analytic, not an SAT/ILP claim.

This lemma was independently developed in sibling branch `workstream/r12-q32-caseII-v44-final-20261028`, file `Q32_130_NO_CORE_ONLY_DEG4.md`; this local copy is included to make the high-support dependency chain explicit and self-contained.
