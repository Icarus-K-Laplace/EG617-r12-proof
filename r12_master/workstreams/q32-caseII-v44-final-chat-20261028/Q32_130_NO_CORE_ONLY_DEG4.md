# Q32 130-edge color: no core-only degree-four vertex

Date: 2026-10-28
Status: PROVED_CONDITIONAL under the registered 61-point residual contract, the 130-edge minimum-degree-four theorem, and Kang–Pikhurko Theorem 1 at (56,11).

Let D be a 130-edge non-target color with alpha(D)<=12, omega(D)<=5 and delta(D)>=4. Let H be the target core with alpha(H)<=4.

## Lemma: every degree-four vertex has at least five edges in its neighborhood

For any vertex x with d_D(x)=4, let S=N_D(x) and let N be its 56 nonneighbors. Then alpha(D[N])<=11 and omega(D[N])<=5. The complement of D[N] is K12-free and not 11-partite, because eleven D-cliques of size at most five cover at most 55 vertices. Kang–Pikhurko Theorem 1 gives p_11(56)=1421, so e(D[N])>=1540-1421=119.

Write a=e(D[S]) and b=e_D(S,N). The 130-edge total gives a+b<=7. Minimum degree four gives 2a+b>=12. Hence a>=5. Therefore every degree-four vertex x satisfies e(D[N_D(x)])>=5. (1)

## Theorem: no core-only degree-four vertex exists

Suppose u is in H, d_D(u)=4, and all four D-neighbors of u lie in H. Let S=N_D(u). Since S is a four-set in H, it cannot induce K4: otherwise {u} union S would be a D-colored K5 inside H, contradicting alpha(H)<=4. By (1), e(D[S])=5, so D[S]=K4-e.

The edge budget forces e(D[N])=119 and exactly two S–N edges. The two endpoints a,b of the missing edge each have degree three in {u} union S and therefore each receive exactly one S–N edge; the two central vertices c,d receive none.

Let z be the unique external D-neighbor of endpoint a. Then N_D(a)={u,c,d,z}. The vertices u,c,d form a triangle. The vertex z is nonadjacent to u because z is in N, and is nonadjacent to c,d because the two central vertices have no neighbors in N. Thus D[N_D(a)] is a triangle plus an isolated vertex and has only three edges. But a has degree four, so (1) requires at least five edges in its neighborhood, a contradiction.

Therefore no vertex of H can have degree four in D with all four D-neighbors in H. This is stronger than the corollary that no two such vertices can coexist.

## Firewall

The proof uses no exceptional-vertex injectivity and no universal degree-nine assertion. The external extremal input is Kang–Pikhurko Theorem 1 at (56,11); the minimum-degree-four premise is the registered 130-edge theorem. The claim is conditional on the stated full-residual bounds alpha(D)<=12 and omega(D)<=5.
