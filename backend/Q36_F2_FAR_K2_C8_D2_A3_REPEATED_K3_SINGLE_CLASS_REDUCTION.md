# q36 f=2 far-target-K2 — c=8, one d2 row, A=3 repeated-K3 single-class reduction

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CORRECT_REDUCTION.md`, common-S row closure, q36 lexicographic maximality, inherited D14, and the induced `alpha(H[U])<=2` property.

Important correction: an earlier concurrent draft invoked a target-core K4 prohibition. That premise is invalid in this backend (the canonical top-channel theory contains pure K9 core supports). The proof below replaces that step completely and does **not** use any K4 prohibition.

This file proves that the family of support classes disjoint from the multiplicity-three K3 support D contains exactly one distinct support class, and that this class has owner multiplicity 2 or 3.

## 1. Setup

Let D be the target-K3 support of multiplicity3. Since D repeats, full defect3 at q36 is forbidden by lexicographic maximality, hence

`u(D)=sum_(d in D) w_d <=2`,

where

`w_v = kappa_v + e_F(v,S)`, `S=F union {x}`.

At least two of the four external d3-owner incidences lie in supports disjoint from D. Every support disjoint from D is a target K3. Let `F_D` be the set of distinct such support classes.

The unique pure d2 block D0 is target-anticomplete to the d3-support union U, so

`alpha(H[U])<=2`.                                            (1)

The previous correct reduction proves that any two distinct members of F_D intersect in exactly two vertices and that F_D is either a common-pair family (Type P) or a four-set family (Type Q).

## 2. Genuine Type Q is impossible without any K4 prohibition

Assume three distinct Type-Q classes occur inside one four-set Q. Write them as

`E_i = Q\{q_i}`.

Every vertex of Q belongs to at least two of these three support classes, hence every vertex of every E_i is globally decorated.

If some E_i had full defect3, its repivot would remain at q36, remove the active decorated shell vertex x, retain the two inactive decorated vertices in X\{x}, and insert three globally decorated core vertices. The decorated-vertex potential would strictly increase, contradicting lexicographic maximality.

Therefore every such E_i satisfies

`u(E_i)<=2`.                                                 (2)

For two distinct triples E_i,E_j the support overlap has size2. Since both are target K3s, the proper-overlap inequality gives

`2 <= w_(q_i)`

because `E_j\E_i={q_i}`; symmetrically `w_(q_j)>=2`.

With three distinct classes, at least three distinct q_i occur. Choose one support among the three which contains two of those q-vertices. Its defect is then at least

`2+2=4`,

contradicting (2).

Hence a genuine Type-Q family cannot contain three distinct classes. With only two distinct classes, the two triples share one common pair, so the geometry is already Type P.

Thus it suffices to rule out two distinct Type-P classes.

## 3. Two distinct Type-P classes are impossible

Let

`E1=P union {z1}`,
`E2=P union {z2}`,

with `P={u,v}` and `z1!=z2`.

Because u and v occur in at least two low-owner supports, they are globally decorated. The proper-overlap inequality for E1,E2 gives

`w_(z1)>=2`, `w_(z2)>=2`.                                   (3)

Each z_i is also globally decorated: besides its owner incidence, its core excess plus S-incidence contributes at least w_(z_i)>=2.

Thus all three vertices of each E_i are globally decorated. Full defect3 would give a q36 repivot retaining the two inactive decorated shell vertices and inserting three decorated core vertices, increasing the lexicographic decoration potential. Therefore

`u(E1)<=2`, `u(E2)<=2`.                                     (4)

Since E1,E2 are K3s, (3)--(4) force

`w_u=w_v=0`,
`w_(z1)=w_(z2)=2`.                                          (5)

Apply row closure for E2 to z1. The two mandatory target edges z1u,z1v already consume the entire budget w_(z1)=2, so

`z1 z2` is a target nonedge.                                 (6)

Also, w_u=w_v=0 and row closure against D give

`e_H(P,D)=0`.                                                (7)

Because alpha(H[U])<=2 and z1z2 is a target nonedge, every d in D must be target-adjacent to at least one of z1,z2. For such a d, row closure against the corresponding support E_i gives

`w_d>=1`.

Therefore

`u(D)=sum_(d in D) w_d >=3`,

contradicting u(D)<=2.

Hence F_D contains at most one distinct support class.

## 4. The unique disjoint class must repeat

At least two of the four external owner incidences are carried by supports disjoint from D. Since there is at most one distinct disjoint class, call it E and let its owner multiplicity be M. Then

`M>=2`.

E is a target K3. Because it repeats, lexicographic maximality gives

`u(E)<=2`.

The K11 base `{p} union C union F` and inherited D14 give

`3M + O_E + e_F(F,E) + 3 <=14`.

Hence M cannot be4, since `12+3>14`. Therefore

> `M in {2,3}`.                                              (8)

Moreover D and E are disjoint repeated target K3s with

`u(D)<=2`, `u(E)<=2`,
`e_H(D,E)<=2`.                                               (9)

The bipartite target-nonedge graph between D and E is therefore K3,3 with at most two target cross-edges deleted from its complement; its minimum vertex-cover number is3.

## 5. Every remaining support lies almost entirely in D union E

Let G be any further d3 support, distinct from D and E. Since E is the unique support class disjoint from D, G intersects D.

For every vertex z in `G\(D union E)`, alpha(H[U])<=2 forces `N_H(z) intersect (D union E)` to cover every D--E target nonedge. By (9) that nonedge graph has vertex-cover number3, so

`e_H(z,D)+e_H(z,E)>=3`.

Row closure against D and E bounds each term by w_z, hence

`w_z>=2`.                                                    (10)

Since every d3 support has total defect at most3, G can contain at most one vertex outside D union E. Thus

> `|G intersect (D union E)|>=2`.                            (11)

## 6. Owner-intersection normal form

There are `4-M` owner incidences outside the D and E multiplicity classes.

D14 applied to D gives

`O_D + e_F(F,D) <=2`.                                       (12)

Every remaining owner support intersects D.

### M=3

There is one remaining owner support G. It satisfies

- `|G intersect D| in {1,2}`;
- `|G\(D union E)|<=1`.

Thus the only possible intersection-count triples `(h_D,h_E,t)` with `h_D+h_E+t=3` are

- `(1,1,1)`,
- `(1,2,0)`,
- `(2,0,1)`,
- `(2,1,0)`.

### M=2

There are two remaining owner incidences. Their total D-overlap is at least2, while (12) is at most2. Hence equality holds:

- each remaining owner incidence belongs to a support meeting D in exactly one vertex;
- `O_D=2`;
- `e_F(F,D)=0`;
- every such support has at most one vertex outside D union E, and therefore contains at least one vertex of E.

No full contradiction for M=2 or M=3 is claimed here.

## 7. Current exact terminal

The multiplicity-three repeated-K3 branch is now reduced to two finite owner-multiplicity channels:

1. `M=3`: D has multiplicity3, E has multiplicity3, and one support G remains in one of the four explicit intersection patterns above.
2. `M=2`: D has multiplicity3, E has multiplicity2, and two owner incidences remain; each support meets D in exactly one vertex, has at least one E-vertex, and at most one vertex outside D union E.

All fixed-12-point-remainder arguments remain retracted and are not used here.