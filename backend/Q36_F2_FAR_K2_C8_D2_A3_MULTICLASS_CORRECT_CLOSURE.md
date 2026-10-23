# q36 f=2 far-target-K2 — A3 repeated-K3 multiclass closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CORRECT_REDUCTION.md`, common-S row closure, q36 lexicographic maximality, `alpha(H[U])<=2`, and the existing c=8 shell contract. No K4-freeness is used.

## Setup

Let D be the multiplicity-three target-K3 support. Its repeated-support defect is at most2.

Let F_D be the distinct target-K3 support classes disjoint from D. The correct preceding reduction proves that any two distinct classes in F_D intersect in exactly two points. Hence F_D is either:

- Type P: a common-pair family `P union {z_i}`; or
- Type Q: triples on a fixed four-set.

We prove that F_D has at most one distinct class.

The original q36 shell has exactly three decorated shell vertices X. Repivoting any d3 support removes its active missing vertex x and retains the other two decorated shell vertices. Therefore:

> if a q36 support contains at least two globally decorated core vertices, its repivot would have at least four decorated shell vertices and would strictly increase the secondary lexicographic potential tau.

Such a support cannot have full defect3.                                      (L)

## 1. Type P

Assume at least two distinct classes exist:

`E_i=P union {z_i}`.

The two vertices of P occur in at least two distinct owner classes, so both are globally decorated. By (L), every class E_i has defect at most2.

Write `w_v=kappa_v+e_F(v,S)` for the common missing set S.

### Petal edges are impossible

For i != j, the petal z_j lies outside support E_i and is target-adjacent to both vertices of P.

If z_i z_j were also a target edge, then

`e_H(z_j,E_i)=3`.

Row closure against E_i gives `w_(z_j)>=3`, but E_j is a target K3 of defect at most2, so `sum_(v in E_j) w_v<=2`. Contradiction.

Therefore all distinct petals are pairwise target-nonadjacent.                 (1)

If there were three distinct classes, three petals would form an independent triple inside U, contradicting `alpha(H[U])<=2`.

Hence only two classes could remain:

`E1=P union {z1}`,
`E2=P union {z2}`,

with z1z2 a target nonedge.

### Two classes are impossible

Because `alpha(H[U])<=2`, every d in D must be adjacent to z1 or z2; otherwise `{d,z1,z2}` is independent. Therefore, with

`a=e_H(D,P)`,
`b_i=e_H(D,{z_i})`,

we have

`b1+b2>=3`.                                                   (2)

Joint row closure from the repeated support D gives

`a+b_i=e_H(D,E_i)<=defect(D)<=2`                             (3)

for i=1,2.

If a>=1, then b1,b2<=1, contradicting (2). Hence a=0.

Now every d in D is adjacent to at least one petal. If d is adjacent to z_i, then d lies outside E_i and row closure against E_i gives

`1<=e_H(d,E_i)<=w_d`.

Thus every d in D has w_d>=1, so

`defect(D)=sum_(d in D) w_d>=3`,

contradicting repeated-support defect<=2.

Therefore Type P cannot contain two distinct classes.

## 2. Type Q

Two distinct classes on a four-set share a common pair, so the two-class case is already Type P and is impossible.

Assume at least three distinct classes occur. Three distinct 3-subsets of a four-set cover every pair of the four-set. Since each support is a target K3, the target graph induced by the four-set is a K4. This is **not** itself a contradiction; K4s are allowed in the backend contract.

However, with at least three distinct classes, every vertex of every support belongs to at least two distinct owner classes. Hence all three vertices of every support are globally decorated. By (L), every support has defect at most2.

Take two distinct support triples E_i,E_j. Their unique difference vertex `z in E_j\E_i` is target-adjacent to all three vertices of E_i, because the four-set is a target K4. Thus

`e_H(z,E_i)=3`.

Row closure against E_i gives `w_z>=3`, while z belongs to the target-K3 support E_j whose total defect is at most2. Contradiction.

Therefore Type Q cannot contain three or more distinct classes.

## 3. Consequence

The family of support classes disjoint from D has exactly one distinct class E.

The correct preceding reduction already gives at least two owner incidences in supports disjoint from D, while D14 bounds one class multiplicity by3. Hence E has owner multiplicity

`M in {2,3}`.

This single-class conclusion is now certified without any K4-free assumption. The next terminal is the finite `M=2,3` compatibility problem.