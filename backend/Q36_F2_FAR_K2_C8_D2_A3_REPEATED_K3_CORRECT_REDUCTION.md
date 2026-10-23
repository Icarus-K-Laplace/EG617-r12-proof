# q36 f=2 far-target-K2 — c=8, one d2 row, A=3 repeated-K3 correct reduction

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_A3_MULTIPLICITY_REDUCTION.md`, common-S row closure, q36 lexicographic maximality, and the induced `alpha(H[U])<=2` property.

This replaces the retracted fixed-remainder closure with a valid support-hypergraph reduction.

## 1. Setup

Let D be a target K3 support of multiplicity3. Repetition forbids full defect3 at q36, so

`u(D)=kappa(D)+e_F(S,D)<=2`,

where the common missing set is `S=F union {x}`.

The multiplicity reduction proves:

- at least two of the four external owner incidences lie in supports disjoint from D;
- every support disjoint from D is itself a target K3.

Let U be the union of all d3 supports. The unique pure d2 support D0 is target-anticomplete to U, hence

`alpha(H[U])<=2`.                                           (1)

For any core vertex v write

`w_v=kappa_v+e_F(v,S)`.

Since every disjoint support E is a K3, its defect is simply

`u(E)=sum_(v in E) w_v<=3`,

and if E repeats then `u(E)<=2` by lexicographic maximality.

## 2. Every disjoint K3 has at most two target cross-edges to D

For a support E disjoint from D, common-S joint row closure gives

`e_H(D,E)<=u(D)<=2`.                                        (2)

Thus the bipartite target-nonedge graph between D and E is K3,3 with at most two edges deleted from its complement, and therefore has matching number3 and vertex-cover number3.

## 3. Two distinct disjoint-from-D support classes must overlap in two points

Let E and E' be two distinct support classes, both disjoint from D.

They are both target K3s. Suppose

`|E intersect E'|<=1`.

Then at least two vertices of E' lie outside `D union E`. Let v be any such vertex.

Because `alpha(H[U])<=2`, the target neighbourhood of v in `D union E` must cover every target-nonedge between D and E. Otherwise some target-nonedge de would give the independent triple {d,e,v} in U.

By Section2, that bipartite nonedge graph has minimum vertex-cover size3. Hence

`e_H(v,D)+e_H(v,E)>=3`.                                    (3)

Row closure against D and E gives

`e_H(v,D)<=w_v`,
`e_H(v,E)<=w_v`,

so (3) implies

`w_v>=2`.                                                    (4)

There are at least two such vertices in `E'\E`, hence

`u(E')=sum_(z in E') w_z>=4`,

contradicting the universal allowance3 bound.

Therefore

> any two distinct support classes disjoint from D intersect in exactly two points.  (5)

## 4. 3-uniform 2-intersecting classification

Let F_D be the set of distinct support classes disjoint from D.

By (5), F_D is a 3-uniform family with pairwise intersection exactly2.

A direct classification gives two possibilities.

### Type P — common pair

There is a fixed two-point set P such that every E in F_D has

`P subset E`.

Thus every class is `P union {z_i}` for some petal z_i.

### Type Q — four-set family

There is a four-point set Q such that every E in F_D is one of the four triples `Q\{q}`.

Indeed, take two distinct triples `{a,b,c}` and `{a,b,d}`. Any third triple meeting each in two points either contains the common pair {a,b}, or is one of `{a,c,d}`, `{b,c,d}`. If one of the latter occurs, every further triple satisfying pairwise two-intersection lies in the same four-set.

Therefore

> the repeated-K3 terminal has collapsed to a common-pair family or a four-set family.   (6)

## 5. D14 multiplicity interface

For a disjoint K3 class E with owner multiplicity m_E, the K11 base `{p} union C union F` gives

`3m_E + O_E + e_F(F,E) + 3 <=14`,

hence

> `3m_E+O_E+e_F(F,E)<=11`.                                 (7)

In particular every such class has multiplicity at most3.

If the disjoint owner multiplicity sum is M and the family is Type P with common pair P={u,v}, then each of u,v belongs to all M owners. D14 applied to a class `P union {z_i}` gives the crude but useful incidence constraint

`2M + m_i + 3 <=14`,

so

> `2M+m_i<=11`.                                             (8)

The total number of external owner incidences is four, while the original repeated K3 D satisfies

`O_D+e_F(F,D)<=2`.

Hence the total owner multiplicity carried by F_D is at least2.

## 6. Correct current terminal

The c=8,n2=1,A=3 multiplicity-three repeated-K3 sector is not closed, but it is now finite in support geometry:

- D is a repeated target K3 of multiplicity3 and defect<=2;
- at least two external owner incidences belong to support classes disjoint from D;
- those disjoint support classes are target K3s;
- every two distinct such classes overlap in exactly two points;
- their distinct-class family is either Type P (common pair) or Type Q (four-set);
- each class multiplicity is at most3 and obeys the D14 incidence bound (7).

The next task is to eliminate Type P and Type Q using owner multiplicities, D14 and the two-unit CORE211 excess budget.