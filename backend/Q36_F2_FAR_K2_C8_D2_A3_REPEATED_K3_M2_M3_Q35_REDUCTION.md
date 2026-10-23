# q36 f=2 far-target-K2 — c=8, one d2 row, A=3 repeated-K3 M=2/M=3 q35 reduction

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_SINGLE_CLASS_REDUCTION.md`, common-S row closure, inherited D14, q36 lexicographic maximality, and `alpha(H[U])<=2`.

Let D be the multiplicity-three target-K3 support and E the unique support class disjoint from D. The previous reduction proves that E is a target K3 of multiplicity `M in {2,3}`, that both D and E have defect at most2, and that every further support G contains at most one vertex outside `D union E`.

Write

`w_v=kappa_v+e_F(v,S)`, `S=F union {x}`.

Because D and E are disjoint repeated K3s,

`u(D)<=2`, `u(E)<=2`, `e_H(D,E)<=2`.                        (1)

Hence the D--E target-nonedge bipartite graph has vertex-cover number3.

## 1. Every outside point costs at least two units

Let z lie in a further support G but outside `D union E`. Since `alpha(H[U])<=2`, `N_H(z) intersect (D union E)` must cover every D--E target nonedge. Therefore

`e_H(z,D)+e_H(z,E)>=3`.

Row closure against D and E bounds both terms by w_z, so

`w_z>=2`.                                                    (2)

Any further support has total defect at most3, hence it contains at most one such outside point.

Moreover every vertex of a further support is globally decorated:

- D-points occur in the multiplicity-three support D;
- E-points occur in the repeated support E;
- an outside point has w>=2 and also its owner incidence.

Therefore a further support cannot use full defect3 while staying at q36: its q36 repivot would retain the two inactive decorated shell vertices and insert three decorated core vertices. Thus every further support G satisfies

> `Delta(G)<=2` and `q_G<=35`.                               (3)

This extra lexicographic bound is the key strengthening.

## 2. M=2: every remaining support is an exact one-edge q35 triple

Now E has multiplicity2. There are two remaining owner incidences. D14 on D forces their total overlap with D to equal2, so each owner support G meets D in exactly one vertex and `e_F(F,D)=0`.

By Section1, G contains at most one point outside D union E.

### The pattern (1,1,1) is impossible

Suppose

`G={d,e,z}`

with d in D, e in E and z outside D union E.

By (2), w_z>=2. By (3), Delta(G)<=2. Hence equality would force

- w_z=2;
- w_d=w_e=0;
- m(G)=0.

Thus G would be a target K3, in particular de would be a target D--E cross edge. But row closure against E gives

`e_H(d,E)<=w_d=0`,

contradiction.

Therefore (1,1,1) cannot occur.

### The only remaining pattern is (1,2,0)

Hence every remaining support has

`G={d,e1,e2}`

with d in D and `{e1,e2}` subset E.

The E-pair contributes one mandatory internal target edge. Let k be the number of target edges from d to `{e1,e2}`. Then

`m(G)=2-k`.

If k>=1, row closure forces positive w on d and on an E-endpoint of a cross edge. Thus

`Delta(G)=sum_(v in G)w_v+m(G) >= 2 + (2-k) >=3`,

contradicting (3). Therefore k=0.

Then m(G)=2, and Delta(G)<=2 forces

`w_d=w_e1=w_e2=0`.

Thus every remaining support is exactly

> `G={d} union P`, where d in D, P is a 2-subset of E,
> `H[G]` consists of the single edge inside P,
> all three vertices have w=0,
> and `Delta(G)=2`, so `q_G=35`.                              (4)

There are exactly two owner incidences of this type. They may use one repeated support or two distinct supports; no stronger conclusion is claimed here.

## 3. M=3: one remaining support and four raw intersection patterns

Now E has multiplicity3 and one further owner support G remains. The previous reduction gives four possible intersection-count triples

`(h_D,h_E,t)`:

- `(1,1,1)`,
- `(1,2,0)`,
- `(2,0,1)`,
- `(2,1,0)`.

By (3), Delta(G)<=2.

### (1,1,1) is impossible

The outside point z has w_z>=2. Defect<=2 would force w_z=2, the D- and E-points to have w=0, and m(G)=0. Hence G would be a K3 and its D/E points would form a target cross edge, contradicting row closure from either zero-w endpoint.

Thus `(1,1,1)` is impossible.

### The two t=0 mixed patterns collapse to one-edge q35 triples

Consider `(1,2,0)`; the other case is symmetric.

G contains one D-point d and two E-points e1,e2. The E-pair is a target edge. If any d--E selected cross edge existed, row closure would force positive w on both endpoints, while the internal missing count drops by only one; this gives Delta(G)>=3. Hence no selected cross edge exists.

Therefore G has exactly one internal target edge, m(G)=2, and defect<=2 forces all three selected vertices to have w=0.

So the t=0 terminal is exactly

> an exact one-edge q35 support with all selected w=0.         (5)

The D--E target cross edges, if any, are confined to the complementary `2 x 1` star.

### (2,0,1) collapses to a K3 q35 equality geometry

Now G contains two D-points d1,d2 and one outside point z. The D-pair is a target edge and w_z>=2.

Defect<=2 forces

- w_z=2;
- w_d1=w_d2=0;
- m(G)=0.

Hence

> G is a target K3 with q_G=35.                               (6)

The two selected D-points are target-anticomplete to E by row closure from w=0. Thus all D--E target cross edges are emitted by the third D-point. The vertex-cover condition for z forces at least one such D--E cross edge; otherwise z would need three E-neighbours but row closure allows at most w_z=2.

Therefore the `(2,0,1)` terminal has the exact shape:

- G is K3;
- the outside point z has w_z=2;
- the two D-points in G have w=0;
- all D--E cross edges come from the third D vertex;
- at least one and at most two such cross edges exist.

The pattern `(2,1,0)` is already included in the t=0 one-edge case after exchanging D and E.

## 4. Current secondary-q35 frontier

The unique-disjoint-class repeated-K3 terminal is now reduced to secondary q35 exchange systems:

### M=2
Two remaining owner incidences, each an exact one-edge q35 support of the form

`{d} union P`, `d in D`, `P in binom(E,2)`,

with all three selected w-values zero.

### M=3
Exactly one remaining support, in one of two q35 geometries:

1. exact one-edge mixed D/E support with all selected w=0 and D--E cross edges confined to a complementary `2 x 1` star;
2. target-K3 support with two D-points of w=0 plus one outside point z of w=2, with all D--E cross edges emitted by the third D-point and numbering one or two.

No fixed-size remainder is used anywhere in this reduction.