# Q32 130-edge color: no two core-only degree-four vertices

Date: 2026-10-28
Status: PROVED_CONDITIONAL under the registered Q32 contract and Kang–Pikhurko Theorems 1 and 4.

Let D be a non-target color on the 61-point residual with e(D)=130, alpha(D)<=12, omega(D)<=5, delta(D)>=4. Let H be the target core, alpha(H)<=4. Call u core-only degree four if u is in H, d_D(u)=4, and all four D-neighbors lie in H.

## Lemma 1
For any x with d_D(x)=4, let S=N_D(x) and let N be its 56 nonneighbors. Then alpha(D[N])<=11 and omega(D[N])<=5. The complement of D[N] is K12-free and not 11-partite, since eleven D-cliques of size at most five cover at most 55 vertices. Kang–Pikhurko Theorem 1 at (56,11) gives p_11(56)=1421 and e(D[N])>=1540-1421=119.

Writing a=e(D[S]) and b=e_D(S,N), the 130-edge total gives a+b<=7. The minimum degree condition gives 2a+b>=12. Hence a>=5. Therefore every degree-four vertex x has e(D[N_D(x)])>=5. (1)

## Lemma 2
If u is core-only degree four, S=N_D(u) lies in H and cannot be K4, as that would make {u} union S a D-colored K5 inside H. By (1), D[S]=K4-e. The edge budget forces e(D[N])=119 and exactly two S–N edges, one at each missing-edge endpoint; the two central vertices have no neighbors in N and have global degree four. Kang–Pikhurko Theorem 4 then gives D[N]=9 isolated K5 dot-union G11.

## Theorem
No two distinct core-only degree-four vertices u,v can coexist in D.

If uv is not a D-edge, then v lies in N_u. Since D[N_u] has minimum degree four and d_D(v)=4, all four neighbors of v lie in N_u. The equality form puts v in an isolated K5 of D[N_u], giving a D-colored K5 wholly inside H, contradiction.

If uv is a D-edge, use Lemma 2 at u. In S=N_D(u)=K4-e, if v is a missing-edge endpoint, then N_D(v) is a triangle on u and the two central vertices plus an isolated external neighbor z. If v is central, let c be the other center and a an endpoint. Then N_D(a)={u,v,c,z}; u,v,c form a triangle and z is nonadjacent to all three, because z is an external neighbor in N_u, c has no neighbor in N_u, and v's four neighbors are exactly u and the other three vertices of S. Either case gives a degree-four vertex whose neighborhood has only three edges, contradicting (1).

Thus no such pair exists. This is an analytic lemma; no exceptional-vertex injectivity or retracted degree-nine claim is used. External extremal inputs are Kang–Pikhurko Theorems 1 and 4 at (56,11), plus the registered 130-edge minimum-degree-four theorem.
