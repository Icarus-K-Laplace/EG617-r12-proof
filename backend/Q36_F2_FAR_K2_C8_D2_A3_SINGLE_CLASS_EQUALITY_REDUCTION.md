# q36 f=2 far-target-K2 — A3 repeated-K3 single-class equality reduction

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_SINGLE_DISJOINT_CLASS.md`, common-S row closure, inherited D14, K4-freeness, q36 lexicographic maximality, and `alpha(H[U])<=2`.

## 1. Setup

Let D be the original target-K3 support of multiplicity3. The preceding theorem proves that all owner incidences carried by supports disjoint from D belong to one target-K3 class E of multiplicity

`M in {2,3}`.

Both D and E are repeated, hence each has defect at most2. They are disjoint and

`e_H(D,E)<=2`.

There are `4-M` remaining owner incidences, all in supports distinct from D and E.

For any support T in this common-S class, a q36 repivot would retain the two inactive decorated shell vertices. If T meets both repeated classes D and E, it inserts at least two globally decorated core vertices and would raise tau. Hence every such T has defect at most2.

## 2. Every remaining support meets E as well as D

By construction every remaining support T meets D; otherwise it would be another disjoint-from-D support class.

Assume T is disjoint from E.

Because E is a repeated K3 of defect at most2, if T were nonclique then an internal target-nonedge of T would have to be covered by all three vertices of E to avoid an independent triple in U, requiring at least3 E--T target edges. Joint row closure allows at most2. Hence T is a target K3.

Now D and T are two distinct K3 support classes disjoint from the repeated K3 E. The same correct 2-intersection argument used in the previous reduction gives

`|D intersect T|=2`.

Write

`D={a,b,c}`,
`T={a,b,t}`.

Since D and T are K3s, K4-freeness gives `ct` a target nonedge.

Let

`A=e_H(E,{a,b})`,
`C=e_H(E,{c})`,
`T0=e_H(E,{t})`.

Because E has defect at most2,

`A+C=e_H(E,D)<=2`,
`A+T0=e_H(E,T)<=2`.

Since `ct` is a target nonedge and `alpha(H[U])<=2`, every vertex of E is adjacent to c or t, so

`C+T0>=3`.

Thus A=0. Every vertex e in E is adjacent to at least one of c,t. Row closure against D or T then gives `w_e>=1`, where `w_e=kappa_e+e_F(e,S)`. Hence

`u(E)=sum_(e in E) w_e>=3`,

contradicting repeated-support defect `u(E)<=2`.

Therefore every remaining support meets both D and E.                 (1)

## 3. No remaining support uses a core vertex outside D union E

Let T contain

- d in D,
- e in E,
- v outside `D union E`.

The bipartite target-nonedge graph between D and E is K3,3 with at most2 target cross-edges removed, so its minimum vertex-cover size is3.

Since `alpha(H[U])<=2`, the target neighbours of v in `D union E` must cover that bipartite nonedge graph. Therefore

`e_H(v,D)+e_H(v,E)>=3`.

Row closure against D and E gives each term at most `w_v`, hence `w_v>=2`.

T has defect at most2. Proper overlap with both repeated classes costs2, so equality is forced: T is a target K3, `w_v=2`, and its two shared vertices d,e have weight0.

Apply row closure against T to the other two vertices of D. Each is adjacent to d, so each has weight at least1. Since `u(D)<=2` and `w_d=0`, both weights are exactly1 and neither can be adjacent to e or v. The same argument on E shows its two vertices outside e each have weight1 and are target-nonadjacent to d and v.

Hence v is adjacent inside `D union E` only to d and e. Its two-point neighbourhood cannot cover the bipartite nonedge graph whose cover number is3, contradiction.

Therefore

> every remaining support is contained in `D union E`.       (2)

## 4. Every remaining support is an exact one-edge 2+1 triple

A remaining support T therefore has composition either

- two vertices from D and one from E, or
- one from D and two from E.

Consider the first case:

`T={a,b,e}`, with a,b in D and e in E.

Let k be the number of target edges from e to {a,b}. T already contains the target edge ab. Proper-overlap equality and defect<=2 give

`u(T)=2`.

Thus the total w-weight on T equals k.

Let c be the third vertex of D. Row closure against T gives

`2 + 1_(ce in E(H)) <= w_c`.

Since `u(D)=2`, this forces

- `w_a=w_b=0`,
- `w_c=2`,
- `ce` is a target nonedge.

Therefore `w_e=k`. The other two vertices of E are each adjacent to e, so row closure against T gives each weight at least1. Since `u(E)=2`, their total available weight is `2-k`. Hence k=0.

Consequently T has exactly one target edge, namely ab, and the selected E-vertex e is target-anticomplete to {a,b}. The exact weight profiles are

- on D: `(0,0,2)`, with the pair vertices the zero-weight points;
- on E: `(0,1,1)`, with the selected singleton the zero-weight point.

The opposite composition is symmetric. Thus:

> every remaining support is an exact one-edge triple whose same-side clique pair is the unique target edge.      (3)

## 5. M=3 channel

If `M=3`, exactly one owner incidence remains outside the E-class. It is a singleton support T.

By (3), T is an exact one-edge support of one of the two orientations:

- pair in D, singleton in E; or
- pair in E, singleton in D.

The two repeated K3 classes both have multiplicity3, so the two orientations are symmetric.

Thus the entire M=3 channel is one q35 one-edge equality geometry up to exchanging D and E.      (4)

## 6. M=2 channel

If `M=2`, two owner incidences remain.

Suppose they belonged to two distinct singleton support classes T1,T2. By (3), every such support imposes an exact weight profile `(0,0,2)` on the clique contributing its pair and `(0,1,1)` on the clique contributing its singleton.

Two supports of opposite orientation impose incompatible weight profiles on D and E. Two supports of the same orientation must use the same zero-weight pair and the same zero-weight singleton, hence have the same three vertices and are the same support class. Therefore two distinct singleton classes cannot occur.

Hence the two owner incidences form one repeated support T of multiplicity2.       (5)

D14 eliminates the orientation with the pair in D: its support-incidence contribution is

`3*2 + 3*2 + 2 =14`

before adding the mandatory internal target edge, already exceeding the D14 allowance.

Therefore the only surviving M=2 geometry is:

- T has multiplicity2;
- T contains a two-point pair from E and one point from D;
- the E-pair is the unique target edge of T;
- T has zero w-weight and defect exactly2;
- the corresponding weight profiles are exact `(0,0,2)` / `(0,1,1)` as in Section4.

## 7. Exact remaining repeated-K3 terminal

The previous Type-P/Type-Q freedom has disappeared. Only two q35 one-edge secondary-shell equality channels remain:

1. `M=3`: D and E both multiplicity3, plus one singleton exact one-edge support (one orientation up to symmetry);
2. `M=2`: D multiplicity3, E multiplicity2, plus one multiplicity2 exact one-edge support whose unique edge is the pair from E.

The next step is to repivot the exact one-edge support and close these two secondary q35 shells.