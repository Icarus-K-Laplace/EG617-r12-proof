# q36 f=2 far-target-K2 — c=8, one d2 row, A=3 repeated-K3 signature reduction

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_SINGLE_CLASS_REDUCTION.md`, common-S row closure, q36 lexicographic maximality, inherited D14, and `alpha(H[U])<=2`.

This reduces the final one-disjoint-class repeated-K3 terminal to a finite overlap-signature system.

## 1. Setup

Let D be the original target-K3 support of multiplicity3. By the single-class reduction, all external owner incidences carried by supports disjoint from D use one unique target-K3 support E.

Let `m=m_E`. Multiplicity4 is already impossible, while at least two external owner incidences are disjoint from D, so

`m in {2,3}`.                                                (1)

The total number of external owner incidences outside the three D-owners is four. Hence there remain `4-m` owner supports T that intersect D.

Write

`w_v=kappa_v+e_F(v,S)`

for the common missing set `S=F union {x}`.

## 2. The repeated support D has exact defect two

Every remaining support T is distinct from D and intersects D properly. Proper overlap of two triples has overlap cost

`h(3-h)=2`.

Joint row closure therefore gives

`u(D)=sum_(d in D)w_d >=2`.

Since D repeats, lexicographic q36 maximality gives `u(D)<=2`. Hence

> `u(D)=2`.                                                  (2)

In particular the D-repivot is a q35 view.

## 3. Every remaining support has at most one vertex outside D union E

The D--E target cross graph has at most two target edges because joint row closure gives

`e_H(D,E)<=u(D)=2`.

Hence its target-nonedge bipartite graph is K3,3 with at most two edges removed and has minimum vertex-cover number3.

Let T be any remaining support and let `v in T\(D union E)`.

Because `alpha(H[U])<=2`, the target neighbourhood of v in `D union E` must cover every D--E target nonedge. Otherwise one uncovered nonedge de gives an independent triple `{d,e,v}` in U. Thus

`e_H(v,D)+e_H(v,E)>=3`.

Row closure against D and E gives each term at most `w_v`, so

`w_v>=2`.                                                    (3)

If T had two vertices outside `D union E`, then its allowance would satisfy

`u(T)>=4`,

contradicting the universal A=3 bound. Therefore

> `|T\(D union E)|<=1`.                                     (4)

## 4. Finite signature list

Let

`k_D=|T intersect D|`,
`k_E=|T intersect E|`,
`k_o=|T\(D union E)|`.

We have `k_D>=1`, `k_o<=1`, and `k_D+k_E+k_o=3`. Since T is distinct from D and E, the only possibilities are

> `(k_D,k_E,k_o)` in
> `{(2,0,1),(2,1,0),(1,1,1),(1,2,0)}`.                    (5)

Whenever `k_E>=1`, E properly overlaps T. Because E repeats, the same overlap-cost argument gives

> `u(E)=2`.                                                  (6)

## 5. Strong specialization when m_E=2

Suppose `m_E=2`. Then there are exactly two remaining supports T1,T2 intersecting D.

For the repeated K3 D, inherited D14 gives

`9 + O_D + e_F(F,D) + 3 <=14`,

so

`O_D+e_F(F,D)<=2`.                                         (7)

Each T_i contributes at least one unit to O_D. Therefore equality of owner counts forces

- each T_i intersects D in exactly one point;
- `O_D=2`;
- `e_F(F,D)=0`.

Thus signatures `(2,0,1)` and `(2,1,0)` are impossible when `m_E=2`. Each T_i has signature

> `(1,1,1)` or `(1,2,0)`.                                   (8)

In particular both T_i intersect E properly. Hence

> `u(E)=2`.                                                  (9)

So in the m_E=2 terminal both repeated K3 supports D and E have exact defect two, and the two remaining supports each meet D in one point and E in one or two points.

## 6. m_E=3 interface

If `m_E=3`, there is one remaining support T. Equation (7) gives `k_D<=2`, and the possible signatures remain the four cases in (5).

If T intersects E, then u(E)=2 by (6). The sole case in which E need not yet be exact-defect-two is

> `(k_D,k_E,k_o)=(2,0,1)`.                                  (10)

## 7. Current terminal

The repeated-K3 A=3 sector is now finite:

- `m_E=2`: two supports, each signature `(1,1,1)` or `(1,2,0)`, with `u(D)=u(E)=2`, `O_D=2`, and no far incidence on D;
- `m_E=3`: one support with one of the four signatures in (5), with `u(D)=2`, and `u(E)=2` unless the signature is `(2,0,1)`.

The next priority is the `m_E=2` exact-defect-two system.