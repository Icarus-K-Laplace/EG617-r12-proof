# q36 f=2 far-target-K2 — A3 single-class correct equality reduction

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_A3_MULTICLASS_CORRECT_CLOSURE.md`, common-S row closure, inherited D14, q36 lexicographic maximality, and `alpha(H[U])<=2`. No K4-freeness is used.

## 1. Setup

Let D be the original target-K3 support of multiplicity3. The correct multiclass closure proves that all owner incidences in supports disjoint from D belong to one target-K3 class E of multiplicity

`M in {2,3}`.

Both D and E are repeated and therefore each has defect at most2. They are disjoint, and joint row closure gives

`e_H(D,E)<=2`.

There are `4-M` remaining owner incidences.

Any remaining support T intersects D. If it also intersects E, then a q36 repivot would retain the two inactive decorated shell vertices and insert at least two globally decorated core vertices (one from D and one from E), raising tau. Hence every such T has defect at most2.

We first prove that every remaining T also intersects E.

## 2. A remaining support cannot be disjoint from E

Assume T is disjoint from E.

Since E is a repeated K3 of defect at most2, T cannot be nonclique: an internal target-nonedge of T would need at least three E--T target edges to avoid an independent triple in U, while row closure from E allows at most2. Hence T is a target K3.

Now D and T are two distinct target-K3 support classes disjoint from the repeated support E. The valid pairwise-2-intersection theorem from `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CORRECT_REDUCTION.md`, applied with E as the repeated base, gives

`|D intersect T|=2`.

Write

`D={a,b,c}`,
`T={a,b,t}`.

Because T contains the globally decorated pair a,b, a q36 repivot of T would retain the two inactive decorated shell vertices and insert at least a,b, increasing tau. Therefore T has defect at most2.

Apply row closure against T to c. Since D is a K3,

`e_H(c,T)=2+1_(ct in E(H)) <= w_c`,

where `w_v=kappa_v+e_F(v,S)` for the common missing set S. Since D is repeated,

`w_a+w_b+w_c=defect(D)<=2`.

Thus necessarily

- `ct` is a target nonedge;
- `w_c=2`;
- `w_a=w_b=0`.                                             (1)

Let

`A=e_H(E,{a,b})`,
`C=e_H(E,{c})`,
`T0=e_H(E,{t})`.

Repeated E gives

`A+C=e_H(E,D)<=2`,
`A+T0=e_H(E,T)<=2`.

Since ct is a target nonedge and `alpha(H[U])<=2`, every vertex of E must be adjacent to c or t, so

`C+T0>=3`.

Hence A=0. Every vertex e of E is adjacent to c or t; row closure against D or T gives `w_e>=1`. Therefore

`defect(E)=sum_(e in E) w_e>=3`,

contradicting repeated-support defect<=2.

Thus every remaining support meets both D and E.                    (2)

## 3. No remaining support uses a vertex outside D union E

Let T contain d in D, e in E, and v outside `D union E`.

The bipartite target-nonedge graph between D and E has at least seven edges and minimum vertex-cover size3 because `e_H(D,E)<=2`.

To avoid an independent triple in U, the target neighbourhood of v in `D union E` must cover that bipartite nonedge graph. Hence

`e_H(v,D)+e_H(v,E)>=3`.

Row closure against D and E gives each term at most `w_v`, so `w_v>=2`.

T has defect at most2, and proper overlap with both repeated classes forces equality. Thus T is a target K3, `w_v=2`, and its two shared D/E vertices have weight0.

Applying row closure against T to the two other D vertices forces each to have weight1 and to be target-nonadjacent to the E-shared vertex and to v. The same holds symmetrically for the two other E vertices.

Consequently v is adjacent inside `D union E` only to the two shared vertices. A two-point neighbourhood cannot cover the D--E target-nonedge graph whose minimum vertex-cover size is3. Contradiction.

Therefore every remaining support is contained in `D union E`.      (3)

## 4. Exact one-edge form

A remaining support has composition 2+1 between D and E. Consider

`T={a,b,e}`, with a,b in D and e in E.

Let k be the number of target edges from e to {a,b}. T already contains the target edge ab. Proper-overlap equality and defect<=2 give `defect(T)=2`, so the total w-weight on T is k.

Let c be the third vertex of D. Row closure against T gives

`2+1_(ce in E(H))<=w_c`.

Since `defect(D)=2`, this forces

- `w_a=w_b=0`;
- `w_c=2`;
- `ce` is a target nonedge.

Hence `w_e=k`. The other two E vertices are each adjacent to e, so row closure against T gives each weight at least1. Since `defect(E)=2`, their total available weight is `2-k`. Therefore k=0.

Thus T has exactly one target edge, namely the same-side clique pair ab. The opposite composition is symmetric.

The exact weight profiles are:

- pair-side repeated K3: `(0,0,2)`;
- singleton-side repeated K3: `(0,1,1)`.

## 5. M=3

If M=3, exactly one owner incidence remains. It is a singleton exact one-edge support. Since D and E both have multiplicity3, the two orientations are symmetric.

Hence M=3 is one exact q35 one-edge equality geometry up to exchanging D and E.

## 6. M=2

If M=2, two owner incidences remain.

Two distinct singleton supports cannot coexist. Every exact one-edge support fixes the zero-weight pair in one repeated K3 and the zero-weight singleton in the other. Opposite orientations impose incompatible weight profiles. Same orientations force the same pair and singleton, hence the same support class.

Therefore the two owner incidences form one repeated support T of multiplicity2.

D14 eliminates the orientation whose pair lies in the multiplicity-three class D: its owner-incidence contribution already reaches14 before adding the mandatory internal target edge.

Thus the only M=2 geometry is:

- D multiplicity3;
- E multiplicity2;
- T multiplicity2;
- T consists of an E-pair and one D vertex;
- the E-pair is the unique target edge of T;
- T has defect2 and zero w-weight;
- the exact weight profiles are `(0,0,2)` on E and `(0,1,1)` on D, in the orientation prescribed above.

## 7. Remaining terminal

The repeated-K3 sector is now reduced, without any K4-free assumption, to two q35 one-edge secondary-shell equality channels:

1. `M=3`: two multiplicity-three K3 classes plus one singleton one-edge support;
2. `M=2`: multiplicities `(3,2,2)` for D,E,T, with T the exact one-edge support described above.

The next step is a secondary-shell closure of these two exact channels.