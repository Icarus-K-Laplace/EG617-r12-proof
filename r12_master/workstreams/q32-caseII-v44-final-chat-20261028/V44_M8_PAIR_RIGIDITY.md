# E408 Q32 Case-II — v=44,m=8 130-color W-pair rigidity

Date: 2026-10-28
Status: **PROVED_CONDITIONAL** under the registered E408-Q32 contract and the source-audited Kang--Pikhurko equality theorem.

## 1. Statement

Let `D` be one of the three 130-edge nonexact colors in the `m=8` branch. Let `u,v in W` be distinct W-points such that

- `d_D(u)=d_D(v)=4`, and
- all four D-neighbors of u and all four D-neighbors of v lie in the core H.

Then

> **`uv` has color D.**

Equivalently, among W-points at which D is degree four and core-only, every pair is D-adjacent.

No degree-9 exceptional vertex, exceptional injectivity, Case-I shell cover, Q33 identity, or E407 identity is used.

## 2. The degree-four anti-neighborhood equality at u

Put

`S=N_D(u)`, `|S|=4`,

and let N be the 56 vertices other than u that are D-nonneighbors of u.

Because `S subset H`, if `D[S]=K4` then `{u} union S` is a D-colored K5 wholly inside H, hence a target-independent five-set in H, contradicting `alpha(H)<=4`. Thus

`e_D(S)<=5`.

As in the registered 130-edge degree-four local argument:

- `alpha(D[N])<=11`, because an independent 12-set in D[N] together with u would be an independent 13-set in D;
- `omega(D[N])<=5`;
- `bar(D[N])` is K12-free and is not 11-partite, because an 11-partition would cover 56 vertices by eleven D-cliques of size at most5, hence at most55 vertices.

For `(n,r)=(56,11)`, Kang--Pikhurko Theorem 1 gives

`t_11(56)=1425`,

`p_11(56)=1425-floor(56/11)+1=1421`,

so

`e(D[N])>=C(56,2)-1421=119`.

Write

`a=e_D(S)`, `b=e_D(S,N)`.

The total 130-edge count gives

`4+e(D[N])+a+b=130`,

hence `a+b<=7`.

The already proved `delta(D)>=4` theorem gives

`2a+b >= 4*3 =12`,

because each vertex of S already uses the edge to u and needs at least three further D-incidences in `S union N`.

Together with `a<=5`, this forces

> `a=5`, `b=2`, `e(D[N])=119`.

Thus `D[S]=K4-e` and the complement `J=bar(D[N])` has exactly

`C(56,2)-119=1421=p_11(56)`

edges.

## 3. Equality classification of D[N]

The graph J is an equality graph in the Kang--Pikhurko non-11-partite K12-free problem. By Kang--Pikhurko Theorem 4 it comes from the explicit extremal construction.

The eleven old parts contain 55 vertices. In `D[N]=bar J`, every old part is a clique. Since `omega(D[N])<=5`, every old part has size at most5. Their sizes sum to55, so every old part has size exactly5.

Therefore the complement translation has the same source-correct Type-I form at parameter `r=11`:

> `D[N] = 9 isolated K5 dot-union G_11`.

In particular:

- `delta(D[N])=4`;
- every degree-four vertex of `D[N]` lies in one of the nine isolated K5 components;
- the four neighbors of any degree-four vertex of `D[N]` induce a D-colored K4.

The gadget vertices all have degree at least5; this follows from the same source construction used in the exact-129 audit, with the two special old parts again of size5.

## 4. Proof of W-pair rigidity

Assume for contradiction that `uv` is not a D-edge.

Then `v in N`. Since `d_D(v)=4`,

`d_{D[N]}(v)<=4`.

But `delta(D[N])=4`, so equality holds:

- `d_{D[N]}(v)=4`;
- v has no D-neighbor in S;
- all four global D-neighbors of v lie in N.

By the equality classification above, v lies in an isolated K5 component of `D[N]`. Hence its four global D-neighbors induce a D-colored K4.

By hypothesis those four neighbors all lie in H, and `v in H`. Thus v together with its four D-neighbors is a D-colored K5 wholly inside H. This is a target-independent five-set in H, contradicting `alpha(H)<=4`.

Therefore `uv` must have color D. QED.

## 5. Useful set form

For a W-point w define

`L(w)={D among the three 130-edge colors : d_D(w)=4 and N_D(w) subset H}`.

Then the lemma says:

> for distinct W-points u,v, every color in `L(u) cap L(v)` must equal the unique color of edge uv.

Consequently

> `|L(u) cap L(v)|<=1`.

Since any two subsets of a three-element color set of size at least2 intersect, whenever `|L(w)|>=2` at all three W-points, all three W--W edges are forced to be nonexact 130-color edges.

## 6. External theorem / verifier scope

External theorem used:

- Kang--Pikhurko Theorem 1 at `(56,11)` for the exact edge value 119 in the anti-neighborhood;
- Kang--Pikhurko Theorem 4 at `(56,11)` for the equality classification.

Also imported: the already proved 130-edge minimum-degree-four theorem.

No SAT/ILP is used. The arithmetic in Sections 2--3 is exact and elementary once the two published extremal results are admitted.