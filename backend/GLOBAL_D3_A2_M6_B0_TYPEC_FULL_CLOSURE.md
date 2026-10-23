# Global d=3 A2 M=6, b=0 Type-C Full Closure

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_A2_M6_PAIR_GEOMETRY_REDUCTION.md`;
- zero-charge incidence-signature theorem;
- common-S row closure and overlap saturation;
- `alpha(H)<=3`;
- fully-decorated q32/CORE211 charge ledger `W<=36`.

Purpose: close the unique P3-plus-K3 equality geometry left in the M=6,b=0 window. The proof uses support-incidence signatures and global charge/degree capacity, not owner-attachment enumeration.

## 1. Canonical Type-C setup

Let

`D={a,b,c}`

be a P3 with target edges ab,bc and target nonedge ac. Let E be a target K3. The two supports are target-anticomplete:

`e_H(D,E)=0`.

They form the maximal disjoint pair and carry six owners in total:

`m_D+m_E=6`.

There are no bridge owners (`b=0`).

The two-block inequality is saturated:

`2*6+e_H(D union E)=12+5=17`.

Hence each of the remaining three owner supports meets `C=D union E` in exactly one vertex, and there are no omitted dense-base-to-C incidences.

Every proper overlap point has common-S charge zero.

## 2. Exact one-point attachment hubs

The P3 D has missing-edge defect1, so

`w(D)<=1`.

A distinct support can meet D in exactly one point only in one situation:

> D has charge1 at its center b, while the endpoints a,c have charge0.   (T1)

Indeed:

- if w(D)=0, all three D vertices are zero-charge and the target edges ab,bc force them to have one common incidence signature, so no support can contain exactly one;
- if the unique charge1 lies at endpoint a or c, the center and opposite endpoint are zero-charge and target-adjacent, hence have the same signature, again preventing one-point overlap;
- if the charge lies at b, the zero endpoints a,c are target-nonadjacent and may carry distinct signatures, so either can be a one-point hub.

Likewise a distinct support can meet the K3 E in exactly one point only if

> E has charge distribution `(0,1,1)`, with one unique zero-charge vertex e.   (T2)

Any two zero-charge vertices in the K3 would be target-adjacent and therefore have the same incidence signature, forcing them to appear together.

## 3. Every one-sided support is an H-type K3

Consider a D-side support meeting C only in a zero endpoint h in {a,c}:

`R={h,u,v}`.

Proper overlap forces exact defect2.

If one private point u had charge0, then hu is a target nonedge by distinct zero signatures. The other private point v must have charge1 and be adjacent to both h and u, giving the only possible Z-type P3.

But u lies outside D and E and has zero charge, so it is target-anticomplete to both. Let h' be the other endpoint of the internal nonedge ac and choose any e' in E. Then

`{h,u,h',e'}`

is an independent4-set.

Thus Z-type is impossible. Both private points have charge1 and R is a target K3.

The same argument for an E-side support, using the D nonedge pair {a,c}, shows that every E-side support is also an H-type K3 with hub e and two unit-charge private petals.         (T3)

## 4. Distinct side-support classes cannot coexist

### 4.1 Same hub

Two distinct H-type supports with the same zero hub have private petal pairs target-anticomplete by row closure.

- for two D-side classes, choose one petal from each, any E vertex, and the D endpoint opposite the hub; these four vertices are pairwise target-nonadjacent;
- for two E-side classes, choose one petal from each and the two D endpoints a,c; again an independent4 results.

Hence no two distinct classes share the same hub.

### 4.2 The two different D endpoints

Suppose one support is based at a and one at c. Their private petal pairs are joined by a bipartite matching at most. The E zero vertex e is target-anticomplete to both petal pairs, and the P3 center b is also target-nonadjacent to every private petal because each petal's unit row allowance into D is consumed by its own hub edge.

Choose a target-nonedge petal pair across the two 2-sets (one exists because their cross graph is a matching). Together with e and b it forms an independent4-set.

Thus distinct D-endpoint classes cannot coexist.

### 4.3 One D-side and one E-side class

Let P and Q be their two private petal pairs. The bipartite target graph P--Q is a matching. A D-side petal is target-nonadjacent to the D endpoint opposite its hub and has at most one target neighbour in E; an E-side petal is target-nonadjacent to both nonhub E vertices and to the zero D endpoints.

Choose p in P and q in Q with pq a target nonedge. Choose the D endpoint h' opposite the D-side hub; qh'=0. Choose one of the two nonhub E vertices f target-nonadjacent to p (one exists by row closure). Then

`{p,q,h',f}`

is independent.

Therefore a D-side and E-side distinct class cannot coexist.

Combining the three cases:

> all three remaining owner rows use one and the same H-type K3 support R, of multiplicity3.   (T4)

The repeated support is based either at one zero endpoint of D or at the unique zero vertex e of E.

## 5. D-side repeated support is impossible

Assume R is based at a D endpoint, say a.

Then (T1) applies:

- b has charge1;
- a,c have charge0 and core degree12.

The two private petals of R have charge1 each.

The support union U consists of D, E and those two private petals, so `|U|=8`.

Its total common-S charge is

`W_U = 1 + w(E) + 2 = 3+w(E)`,                              (T5)

where `0<=w(E)<=2`.

The total q32 fully-decorated charge satisfies `W<=36`. Hence the 27 vertices outside U carry total charge at most

`33-w(E)`.

The union C=D union E contains the independent triple `{a,c,e'}` for any e' in E. Therefore any outside zero-charge vertex, being target-anticomplete to every support, would extend this to an independent4-set. Thus every outside vertex has charge at least1.

Consequently at least

> `27-(33-w(E)-27)=21+w(E)`                                  (T6)

outside vertices have charge exactly1.

Let x be any such charge-one outside vertex. If x were target-nonadjacent to both endpoints a,c, row closure gives at most one x-neighbour in the K3 E, so at least one E vertex e' is also a nonneighbour. Then

`{x,a,c,e'}`

is independent. Hence every outside charge-one vertex is target-adjacent to at least one of a,c.

But a and c each have core degree12. Their two edges to the P3 center b consume two degree incidences in total, and the repeated D-side K3 R contributes two further core neighbours to its hub endpoint a. Therefore the two endpoints have at most

`24-2-2=20`

remaining core-neighbour slots for outside vertices.

This cannot accommodate the at least `21+w(E)>=21` distinct charge-one outside vertices.

Contradiction.

Thus

> the repeated side support cannot be D-side.                (T7)

## 6. E-side repeated support is impossible

Assume R is based at the unique zero vertex e of E.

Then (T2) applies and

`w(E)=2`.

Let `d=w(D) in {0,1}`.

The support union U again has eight vertices and now

`W_U=2+d+2=4+d`.                                             (T8)

Thus the 27 outside vertices have total charge at most

`36-(4+d)=32-d`.

As before every outside vertex has charge at least1. Therefore at least

> `27-(32-d-27)=22+d`                                        (T9)

outside vertices have charge exactly1.

Every charge-one outside vertex must hit at least one of the P3 endpoints a,c; otherwise `{x,a,c,e'}` is independent for a suitable x-nonneighbour e' in E.

The two endpoint core degrees sum to at most

`24+(kappa_a+kappa_c)`.

Since their common-S charges are part of w(D),

`kappa_a+kappa_c<=d`.

After subtracting the two endpoint--center edges, the combined outside-neighbour capacity is at most

> `22+d`.                                                     (T10)

Comparing (T9)--(T10), every inequality must be equality. Therefore:

1. `W=36`;
2. exactly `22+d` outside vertices have charge1 and every one is adjacent to exactly one endpoint a or c;
3. every remaining `5-d` outside vertex is target-nonadjacent to both a and c;
4. the endpoint capacity is completely saturated;
5. `kappa_a+kappa_c=d` and there are no omitted endpoint neighbours in U.

Take one of the remaining `5-d` vertices z. Since z is target-nonadjacent to both a,c, the triple `{a,c,z}` is independent.

Every vertex of E is target-nonadjacent to a and c because D--E is target-anticomplete. To avoid an independent4-set, z must therefore be target-adjacent to **every** vertex of E.

Row closure against the support E then gives

> `w_z>=3`.                                                   (T11)

Hence the total charge on the outside vertices is at least

`(22+d)*1 + (5-d)*3`
`=37-2d`.

But from (T8) and `W<=36`, their total charge is at most

`32-d`.

For d=0 or1,

`37-2d > 32-d`.

Contradiction.

Therefore

> the repeated side support cannot be E-side.                (T12)

## 7. Conclusion

Both possible locations of the unique repeated side support are impossible.

Hence the Type-C P3-plus-K3 equality geometry does not exist.

Therefore

> **M=6,b=0 is impossible.**                                 (T13)

Together with `GLOBAL_D3_A2_M6_B1_FULL_CLOSURE.md`, this yields

> **M=6 full closure:** no maximal disjoint support pair in the final nine-owner fully-decorated q32 d3 equality state can carry six owners.   (T14)

Thus every maximal disjoint pair satisfies

> `m_D+m_E<=5`.                                               (T15)

The former high-codegree one-spoke bridge remains valid as a reusable theorem, but it is no longer required to close the M=6 owner-count window.
