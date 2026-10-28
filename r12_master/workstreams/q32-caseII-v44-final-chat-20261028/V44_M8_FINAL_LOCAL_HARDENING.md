# E408 Q32 v=44,m=8 — final local hardening for the (3,3,2) branch

Date: 2026-10-28
Status: **PROVED_CONDITIONAL / proof-hardening note**

Purpose: make explicit two implications that were compressed in `V44_M8_CLOSURE.md` Section 9. This note changes no hypothesis and introduces no new external theorem.

## 1. Frozen surviving normal form

Assume the surviving m=8 multiplicity branch `(3,3,2)` after Sections 1--8 of `V44_M8_CLOSURE.md`.

We have three W-points `w0,w1,w2` and three 130-edge nonexact colors, say `D0,D1,D2`, with:

1. every `L(wi)` has size exactly two;
2. for distinct W-points u,v, `|L(u) cap L(v)|<=1`;
3. pair rigidity: if `D in L(u) cap L(v)`, then uv has color D;
4. every W--W edge is nonexact;
5. for every `D in L(w)`, `d_D(w)=4` and all four D-neighbors of w lie in H;
6. the local equality package at such a w is the strengthened result of `V44_M8_PAIR_RIGIDITY.md`: if `S=N_D(w)`, then `D[S]=K4-e`, `e_D(S,N)=2`, and the two S--N edges are incident one each with the two missing-pair endpoints; the two central vertices have no D-neighbor outside `{w} union S`.

## 2. The three L-sets determine all three W--W colors

The three `L(wi)` are size-two subsets of a three-color set. If two were equal, their intersection would have size two, contradicting `|L(u) cap L(v)|<=1`. Hence they are the three distinct two-subsets.

After relabelling colors and W-points, necessarily

`L(w0)={D0,D1}`,

`L(w1)={D0,D2}`,

`L(w2)={D1,D2}`.

Pair rigidity and edge-color uniqueness therefore give exactly

`color(w0w1)=D0`,

`color(w0w2)=D1`,

`color(w1w2)=D2`.

Consequently, for each nonexact color D, D owns **exactly one** W--W edge. In particular, if u,v are the two W-points whose L-sets contain D and q is the third W-point, then

`uv in E(D)` but `uq,qv notin E(D)`.

This explicitly rules the third W-point out of `N_D(u)` and `N_D(v)`.

## 3. Missing-endpoint exclusion with the full (a,b) equality

Fix a nonexact color D and let u,v be its unique W--W edge. Put

`S=N_D(u)`.

Because `D in L(u)`, S consists of four core vertices and the local equality theorem gives

`D[S]=K4-e`.

Since `uv` is a D-edge, `v in S`.

Assume v is one of the two endpoints of the unique missing edge in `D[S]`. Let c,d be the two central vertices and r be the other missing endpoint.

Inside the five-vertex graph `{u} union S`:

- v sees `u,c,d`, so it has exactly three D-neighbors there;
- c and d each already see four D-neighbors there;
- r sees `u,c,d`, so it also has degree three there.

The strengthened local equality gives `e_D(S,N)=2`. Minimum degree four forces one S--N edge from v and one from r, exhausting both cross edges. Thus c,d have no D-neighbor in N.

Because `d_D(v)=4`, v has exactly one external D-neighbor z in N. Therefore

`N_D(v)={u,c,d,z}`.

Among these four vertices, `u,c,d` form a D-triangle, while z is D-nonadjacent to each of u,c,d:

- `uz` is absent because z lies in the anti-neighborhood N of u;
- `cz,dz` are absent because c,d have no S--N edges.

Hence `D[N_D(v)]` has exactly three edges, a triangle plus an isolated vertex.

But the same degree-four/core-only local equality applies at v because `D in L(v)`, and requires

`D[N_D(v)]=K4-e`,

which has five edges. Contradiction.

Therefore v is a central vertex of `D[S]=K4-e`.

## 4. The three remaining vertices are in U

Let c be the other central vertex and a,b the missing-pair endpoints of `D[S]`.

All of `c,a,b` lie in H because `u in L(u)` is core-only.

Section 2 proved that D owns exactly one W--W edge, namely uv. Thus the third W-point q is not D-adjacent to u and is not in S.

Since `S` contains v plus exactly three other core vertices, and W contains only `u,v,q`, those three other vertices must all lie in

`U=H\W`.

Hence

`c,a,b in U`.

Inside U the local K4-e gives

`ca,cb in E(D)` but `ab notin E(D)`.

## 5. Contradiction with the saturated nonexact structure

The U-pool saturation already proved in `V44_M8_CLOSURE.md` gives, for every nonexact color D,

`D[U]=8 K4 dot-union 4 K3`.

Every connected component is therefore a clique.

But `c` is adjacent to both `a` and `b`, so c,a,b lie in the same connected component of `D[U]`. That component is a clique, forcing `ab in E(D)`, contradiction.

Thus the `(3,3,2)` branch is impossible.

## 6. Dependency / computation audit

No new external theorem is used in this note. It uses only already-registered consequences:

- W-pair rigidity;
- the strengthened local equality `(a,b)=(5,2)` and its forced S--N edge placement;
- the three-color L-set combinatorics;
- the previously proved U-pool saturation `D[U]=8K4 dot-union 4K3`.

No SAT/ILP claim is made. The only finite set-system assertion is that three size-two subsets of a three-set with pairwise intersections at most one are the three distinct size-two subsets; this is covered by `verify_v44_m8_closure_arithmetic.py`.

This note closes the two implicit logical gaps in the compressed final paragraph of `V44_M8_CLOSURE.md` without changing its verdict.