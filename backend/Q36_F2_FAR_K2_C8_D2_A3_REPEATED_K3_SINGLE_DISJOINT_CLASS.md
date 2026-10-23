# q36 f=2 far-target-K2 — A3 repeated-K3: only one disjoint support class

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CORRECT_REDUCTION.md`, inherited K4-freeness, common-S row closure, q36 lexicographic maximality, and `alpha(H[U])<=2`.

## Setup

Let D be the multiplicity-three target-K3 support in the c=8, n2=1, A=3 repeated-K3 terminal. Its defect is at most two, so with

`w_v=kappa_v+e_F(v,S)`, `S=F union {x}`,

we have

`u(D)=sum_(d in D) w_d <=2`.

Every support class disjoint from D is a target K3. The correct reduction already proves that any two distinct such classes intersect in exactly two points and hence form either a common-pair family (Type P) or a four-set family (Type Q).

## 1. Type Q with at least three distinct classes is impossible

Three distinct triples from the four triples on a fixed four-set cover every pair of the four-set. Since each support is a target K3, the induced target graph on that four-set is K4, contradicting inherited K4-freeness.

Thus if at least two distinct disjoint-from-D classes exist, there are exactly two, and they may be written

`E1=P union {z1}`,
`E2=P union {z2}`

for a common pair P.

## 2. Two distinct classes are impossible

Both E1 and E2 are target K3s. Hence every vertex of P is target-adjacent to both petals z1,z2.

If z1z2 were a target edge, `P union {z1,z2}` would be a target K4. Therefore

`z1z2` is a target nonedge.                                  (1)

Because `alpha(H[U])<=2`, every d in D must be target-adjacent to at least one of z1,z2; otherwise `{d,z1,z2}` would be an independent triple in U. Therefore, writing

`a=e_H(D,P)`,
`b_i=e_H(D,{z_i})`,

we have

`b1+b2>=3`.                                                   (2)

For each i, common-S row closure against the repeated support D gives

`e_H(D,E_i)=a+b_i <= u(D) <=2`.                              (3)

If a>=1, (3) gives b1,b2<=1, contradicting (2). Hence

`a=0`.                                                        (4)

Now every d in D is adjacent to at least one petal. If d is adjacent to z_i, then d lies outside support E_i and row closure against E_i gives

`1 <= e_H(d,E_i) <= w_d`.

Thus every d in D has `w_d>=1`, and therefore

`u(D)=sum_(d in D) w_d >=3`,

contradicting `u(D)<=2`.

Hence two distinct disjoint-from-D support classes cannot coexist.

## 3. Consequence

All external owner incidences carried by supports disjoint from D belong to one single target-K3 support class E.

The previous reduction gives at least two such owner incidences, while D14 gives multiplicity at most three. Therefore the unique disjoint class E has owner multiplicity

`M in {2,3}`.

The four external owner incidences outside the multiplicity-three class D split as:

- `M=3`: one remaining owner incidence comes from a support intersecting D;
- `M=2`: two remaining owner incidences come from supports intersecting D.

This is now the exact repeated-K3 terminal. The next task is to eliminate the two finite multiplicity channels `M=2,3` using D14, support-overlap and secondary repivot constraints.