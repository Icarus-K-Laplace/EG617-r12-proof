# Universal legal-core floor e(H)>=214

Status: **PROVED ANALYTIC** under the full legal backend-core contract. This strengthens CORE211 for legal residual cores, without changing the weaker statement for arbitrary R(3,35) graphs.

## Theorem

Let H be a graph on 35 vertices satisfying

- alpha(H)<=3;
- omega(H)<=11;
- minimum degree at least12.

Write K=sum_v(d_H(v)-12)=2e(H)-420. Then K>=8 and e(H)>=214.

## Proof

The registered GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE theorem says that any such H containing three pairwise nonadjacent degree-12 vertices must have K>=8.

Suppose K<=6. Since every vertex has degree at least12, each vertex whose degree exceeds12 consumes at least one unit of K. Hence at most six vertices have degree greater than12, and at least29 vertices have degree exactly12.

Because omega(H)<=11, the degree-12 vertices cannot all be pairwise adjacent. Choose two nonadjacent degree-12 vertices a,b.

Each open neighbourhood N(a), N(b) has size12, and neither contains a or b because ab is a nonedge. Therefore at least

35 - 2 - 12 - 12 = 9

vertices outside {a,b} are nonadjacent to both a and b. At most six vertices in the entire graph have degree greater than12, so among these nine common nonneighbours at least three have degree exactly12. Choose one and call it c.

Then a,b,c are three pairwise nonadjacent degree-12 vertices. The registered three-anchor theorem forces K>=8, contradicting K<=6. Thus K>=8. Since K=2e(H)-420, this is equivalent to e(H)>=214. QED.

## Backend consequence

For every legal 49-point residual F and every degree-13 pivot p, its 35-point core H_p inherits alpha(H_p)<=3, omega(H_p)<=11, and minimum degree at least12. Therefore e(H_p)>=214.

Using the exact decomposition E=91+q_p+e(H_p), every legal backend pivot obeys the unconditional legal-core ceiling q_p<=E-305.

For E=333,334,...,340 the respective ceilings are q<=28,29,30,31,32,33,34,35.

This does not by itself close every E-layer: it reduces the permitted q range and makes the q=36,37,38 backend states impossible under the full contract. The remaining q<=E-305 equality cases still require their registered shell/extraction proofs.

## Status-discrepancy warning

A reported state labelled “legal core, q=32, e(H)=211” at E=334 cannot satisfy this full contract. The identity E=91+q+e(H) is numerically correct, but at least one inherited hypothesis or the legality of the extracted core must be checked. Do not promote such a reported state to a legal counterexample without replaying the extraction and all core conditions.

The theorem relies essentially on omega(H)<=11 in addition to alpha(H)<=3 and the minimum-degree-12 condition. It does not assert e(H)>=214 for every arbitrary 35-vertex graph with alpha(H)<=3 alone.
