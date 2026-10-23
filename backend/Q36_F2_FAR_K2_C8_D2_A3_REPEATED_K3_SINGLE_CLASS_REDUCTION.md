# q36 f=2 far-target-K2 — c=8, one d2 row, A=3 repeated-K3 single-class reduction

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CORRECT_REDUCTION.md`, common-S row closure, q36 lexicographic maximality, `alpha(H[U])<=2`, and the target-core K4 prohibition.

This closes the multi-class Type-P/Type-Q part of the repeated-K3 terminal. It does not yet eliminate the final one-class multiplicity terminal.

## 1. Setup

Let `D` be the multiplicity-three target-K3 support from the A=3 repeated-K3 terminal. Put

`w_v = kappa_v + e_F(v,S)`,

where `S=F union {x}` is the common missing set.

Because D repeats, lexicographic q36 maximality gives

`u(D)=sum_(d in D) w_d <= 2`.                              (1)

Every support disjoint from D is a target K3. The correct reduction proves that distinct disjoint-from-D support classes pairwise intersect in exactly two points; hence their distinct-class family is Type P (common pair) or Type Q (four-set).

## 2. Type Q with three distinct classes is impossible

Let Q be the four-point carrier. Three distinct triples of the form `Q\{q}` cover every pair of Q in at least one support. Since every support is a target K3, all six target edges on Q are present. Thus H[Q] is a target K4, forbidden.

Therefore a Type-Q family has at most two distinct classes. Two distinct 3-subsets of a four-set intersect in a common two-set, so this case is already Type P.

Hence it suffices to rule out two distinct Type-P classes.

## 3. Two distinct Type-P classes force the common pair anticomplete to D

Let

`E1=P union {z1}`,
`E2=P union {z2}`,

with `P={u,v}` and `z1!=z2`.

Both E1,E2 are target K3s. Hence uv, uz_i, vz_i are target edges.

If z1z2 were a target edge, then `{u,v,z1,z2}` would be a target K4. Therefore

`z1 z2` is a target nonedge.                                (2)

Write

`A=e_H(D,P)`,
`a_i=e_H(D,{z_i})`.

The joint row-closure bound from the repeated support D gives

`A+a_i=e_H(D,E_i)<=u(D)<=2`                                (3)

for i=1,2.

Because alpha(H[U])<=2 and z1z2 is a target nonedge, every d in D must be target-adjacent to at least one of z1,z2; otherwise `{d,z1,z2}` would be an independent triple in U. Thus

`a_1+a_2>=3`.                                               (4)

If A>=1, (3) gives a_1,a_2<=1, contradicting (4). Hence

`A=0`.                                                       (5)

So the common pair P is target-anticomplete to D.

## 4. Row closure contradicts the repeated-support defect budget

Fix d in D. By (4), d is adjacent to at least one petal, say z_i. By (5), d has no target edge to either vertex of P. Therefore

`e_H(d,E_i)=1`.

Since d lies outside E_i, row closure against E_i gives

`1 <= w_d`.                                                  (6)

This holds for every d in D. Summing over the three vertices of D yields

`u(D)=sum_(d in D)w_d >=3`,

contradicting (1).

Therefore two distinct disjoint-from-D support classes cannot exist.

## 5. Conclusion

All owner incidences carried by supports disjoint from D use one unique target-K3 support E.

Thus the repeated-K3 terminal has collapsed to:

- D is a target K3 of multiplicity3 and u(D)<=2;
- E is the unique support class disjoint from D;
- E is a target K3;
- E carries at least two of the four external owner incidences, hence multiplicity `m_E in {2,3}` (multiplicity4 is already excluded globally);
- the remaining `4-m_E` external owner incidences, if any, belong to supports intersecting D.

The next task is to eliminate the `m_E=2` and `m_E=3` one-class terminals.