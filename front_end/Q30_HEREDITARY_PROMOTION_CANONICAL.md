# Canonical q30 hereditary promotion theorem

Status: `PROVED` by independent replay of the full V7 proof body, with the proof reconstructed below under the explicit T61 hereditary-cap contract.

## Statement

Let `R` be a 61-vertex graph with

- `delta(R)>=13`;
- `alpha(R)<=5`;
- `omega(R)<=11`;
- all inherited density caps `D(n)`;
- `405<=e(R)<=408`.

Let `p` be a degree-13 pivot with shell `A=N(p)`, 47-core `C=R-N[p]`, shell complement `M`, decorations `g_a=d_R(a)-13`, weights `t_a=d_M(a)+g_a`, and charge

`q=e(M)+sum_A g`.

Assume `q=30`.

Then there exists a degree-13 pivot `w` reachable from `p` by at most two consecutive regular repivots such that

`q_w>=31`.

If two steps are required, the intermediate pivot also has charge30.

This theorem does **not** assume `p` is a maximum-charge pivot.

## 1. Exact repivot system

For a regular shell vertex `y`, let

- `d=d_M(y)`;
- `S=N_M(y)`;
- `D=N_C(y)`, so `|S|=|D|=d`;
- `rho=e_M(A\S)+G_{A\S}`;
- `h=sum_{x in D}(d_C(x)-12)`;
- `kappa=C(d,2)-e_C(D)`;
- `b=e_R(S,D)`;
- `m=e_M(S)`.

At q30 the old core has 284--287 edges, hence minimum degree at least12. Exact edge accounting gives

`q_y=d(13-d)+rho+h+kappa+b`.                (RP)

If the new core also has minimum degree at least12, then the total inserted excess is

`eta=q-d(13-d)-rho-m-b>=0`.                 (INS)

For a missing edge `uv` with `u` regular, once the `u`-core is within the <=288 minimum-degree interface,

`|N_M(u) union N_M(v)|+g_v >= 13+|D_u intersect D_v|`.  (ZG)

Every repivot with `q_u>=30` is in that interface in the present energy window.

## 2. Classification assuming no immediate upward repivot

Assume every regular neighbour `y` of `p` satisfies `q_y<=30`.

From (RP), regular missing degrees 4--9 are impossible because `d(13-d)>=36`.

For `d=3` or10, equality is forced:

- `q_y=30`;
- `rho=h=kappa=b=0`;
- `m=0` by (INS);
- the exchanged core row is a clique of degree-12 vertices;
- the inserted shell side has zero new-core excess.

For `d=3`, the three missing neighbours all have weight10; every active vertex on the opposite 10-side has missing degree3. Hence

`M=K_(3,k) disjoint_union (10-k)K1`, `k=8,9,10`,

with the three hubs decorated by `10-k` each.

The `d=10` equality is the `k=10` member of the same family.

Call this **Family I**.

Now assume no regular vertex has missing degree3--10. Let

`X={a:t_a>=11}`.

A K4 in `M` is impossible: the 36-row K4 bound, subset charge, and (INS) for a regular degree-2 outside witness contradict each other. Also `|X|<=3`.

- `|X|=0`: all missing edges lie on at most `G<=8` decorated vertices; K4-freeness gives at most21 shell missing edges, below `z>=22`.
- `|X|=1,t_x=11`: every regular outside vertex is isolated, again placing all missing edges on at most8 vertices and giving `z<=21`.
- `|X|=1,t_x>=12`: the remaining 12-vertex graph must contain a triangle or a 2-matching. A triangle with `x` gives charge at least31; a 2-matching forces an equality configuration whose eight outside vertices can contribute at most8 further missing edges, contradicting `z>=22`.
- `|X|=3`: subset charge forces three weight-11 vertices forming a missing triangle with ten independent regular outside vertices. Some outside vertex has missing degree2, and its exact repivot has charge at least31.
- `|X|=2`: the 11-set outside `X` must contain an edge `uv`. Subset charge forces the two X-weights to be11, `t_u+t_v=13`, and the remaining nine shell vertices to be independent and regular. All nine are active and meet both X vertices. The X vertices are nonadjacent in `M`, while `u,v` are the only extra missing edge and carry positive decorations summing7.

Thus the only second no-immediate-rise form is

**Family II:** `M=K_(2,11)` plus one missing edge inside the 11-side; the two hubs are regular weight11, nine ordinary lows are regular weight2, and the exceptional low pair has positive decorations summing7.

This is exhaustive.

## 3. Family I cannot persist

Let `K` be the old pivot together with the ten non-hub shell vertices. It is a target `K11` of regular vertices. Each `v in K` has a 3-set `T_v` of neighbours outside K.

Every active low gives a q30 equality repivot; inactive lows are true twins of the old pivot. Using a disjoint partner row and the d3 equality theorem in each view shows that all distinct `T_v` are pairwise disjoint target triangles.

Let their multiplicities be `c_1,...,c_r`. Then

`1<=c_i<=3`, `sum c_i=11`.

Distinct row triangles are target-anticomplete. Hence `r<=5` from `alpha(R)<=5`.

Their contribution to global degree excess is

`3(11-r)`.

For `405<=E<=408`, total excess above degree13 is at most23, so `r>=4`.

If `r=5`, the remaining 35 vertices have total excess at most5. Every such vertex must be complete to one of the five row triangles, otherwise it plus one avoiding vertex from each triangle gives an independent6-set. The core-degree constraints then force at least2 excess at every one of those 35 vertices, impossible.

If `r=4`, the remaining 38 vertices have total excess at most2, so at least36 are regular. Any two nonadjacent regular remainder vertices together avoid one vertex in each of the four triangles, creating an independent6-set. Hence those regular vertices would form a clique of size at least36, contradicting `omega(R)<=11`.

Therefore Family I is impossible.

## 4. Family II cannot form a closed two-step plateau

Let `K` be the old pivot plus the nine ordinary lows. This is a target `K10` of regular vertices, all adjacent to the two decorated exceptional lows `u,v`, which are target-nonadjacent.

Assume no regular vertex at R-distance at most2 from the old pivot has charge at least31.

For each `v_i in K`, let `T_i` be its two neighbours outside `K union {u,v}`. Repivoting at an ordinary low has charge at least30, hence exactly30. Its new core has minimum degree12, and its pair `T_i` is a target edge.

The q30 no-immediate-rise classification applies again at every `v_i`. Family I is already impossible, so every such view is Family II. Therefore `T_i` are exactly the two weight-11 hubs in that view. In particular each vertex of `T_i` is adjacent to precisely `v_i` among K and is nonadjacent to `u,v`.

The pairs `T_i` are mutually disjoint. If `i!=j` and `x in T_i`, then in the core at `v_j`,

`d_core(x)=13-1-e_R(x,T_j)=12-e_R(x,T_j)>=12`,

so different pairs are target-anticomplete.

Choosing one vertex from each of the ten disjoint pairs gives an independent10-set, contradicting `alpha(R)<=5`.

Hence Family II cannot persist for two regular repivots without an upward move.

## 5. Conclusion

Starting from any q30 pivot:

- either an adjacent regular repivot already has q>=31;
- or the shell is Family I or II;
- Family I is impossible;
- Family II forces an upward regular repivot within the next step.

Therefore every q30 pivot reaches a degree-13 pivot of charge at least31 in at most two regular repivots.

## Provenance

This is an independent replay of `T61_H13_V7/Q30_HEREDITARY_SHELL_THEOREM.md` from the user-supplied V7 package. The source-package theorem has now been reconstructed into the canonical repository and is no longer merely `SOURCE_REPORTED` for this q30 promotion statement.
