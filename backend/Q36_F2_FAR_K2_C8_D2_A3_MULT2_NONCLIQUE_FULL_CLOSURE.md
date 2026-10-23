# q36 f=2 far-target-K2 — c8 one-d2 A3: multiplicity-two nonclique closure

Status: `PROVED` under the valid c=8 one-d2 A3 contract, common-S row closure, inherited D14, q36 lexicographic maximality, `alpha(H[U])<=2`, and the already proved absence of multiplicity-three supports.

This closes both possible nonclique repeated-support types.

## 1. Two-edge repeated support

Let D={a,b,c} be a multiplicity-two support with target edges ab,bc and target nonedge ac.

Its internal missing count is1. Since repeated supports have total defect at most2,

`w_a+w_b+w_c<=1`.                                           (1)

Five owner incidences remain outside the D-class.

A support disjoint from D is impossible: the internal nonedge ac requires at least3 target edges from D to any disjoint support to avoid an independent triple in U, while D has non-missing cross allowance at most1.

Hence all five owner incidences intersect D.

D14 gives

`6 + O_D + e_F(F,D) + 2 <=14`,

so `O_D+e_F(F,D)<=6`.

### Allowed intersections

- a support meeting D only at b is impossible: both a and c lie outside it and are adjacent to b, forcing `w_a,w_c>=1`, contradicting (1);
- a support meeting D in {a,c} is impossible: b lies outside and is adjacent to both a,c, forcing `w_b>=2`;
- a support meeting D in {a,b} forces `w_c>=1`; then every other legal support type would force a second positive D-weight, so all five owner incidences would have to use {a,b}, giving O_D>=10, impossible;
- similarly for {b,c}.

Therefore every external support meets D in exactly one endpoint a or c. Such a support forces w_b>=1, and (1) gives the exact profile

`w_a=w_c=0`, `w_b=1`.                                       (2)

## 2. The petal union is a clique

Write an external support as `{a} union P` or `{c} union P`, with |P|=2.

For b outside that support, the edge from b to the anchor consumes its full row budget w_b=1. Therefore b is target-anticomplete to every petal vertex.

If two petal vertices were target-nonadjacent, together with b they would form an independent triple in U. Hence the union of all petal vertices is a target clique.            (3)

## 3. Universal-petal collapse

A petal z absent from some support is adjacent to both petals of that support by (3), so row closure gives w_z>=2.

If a support had two non-universal petals its defect would be at least4, impossible. Hence every petal pair contains a universal vertex z common to every external support.

Thus every external support has form

`{anchor,z,t_i}`, with anchor in {a,c}.                       (4)

There are five owner incidences and support multiplicity at most2, so at least three distinct support classes occur.

The anchor belongs to the repeated support D and z belongs to every external class; both are globally decorated. Therefore a full-defect3 q36 repivot of any external support would retain the two inactive decorated shell vertices and insert at least anchor and z, increasing tau. Every external support has defect at most2.

For a non-universal petal t_i, row closure against another support gives w_(t_i)>=2. Thus equality holds: w_(t_i)=2, w_z=0, and the support has zero internal missing count, so it is a target K3.

If two distinct support classes use the same anchor, the petal of one is adjacent to all three vertices of the other (same anchor, universal z, and petal clique), forcing w>=3 by row closure, contradiction.

Hence each of the two anchors supports at most one distinct class. With multiplicity at most2, at most four owner incidences can be carried, fewer than the required five.

Contradiction. Thus no multiplicity-two two-edge support exists.

## 4. One-edge repeated support

Let D={a,b,c} have unique target edge ab, with c isolated in H[D].

Its internal missing count is2, so repeated-support defect<=2 forces

`w_a=w_b=w_c=0`.                                             (5)

Again every external support must intersect D; disjoint support cross allowance is zero while D has internal target-nonedges.

An external support can intersect D only in one of two forms:

- `{c}`;
- `{a,b}`.

Indeed intersection only at a or b makes the other endpoint of ab lie outside the support but adjacent to the shared endpoint, contradicting zero row budget; overlaps {a,c} or {b,c} fail similarly.

Let n_C and n_AB be the owner-incidence counts of these two forms. Then

`n_C+n_AB=5`.

D14 gives

`6 + (n_C+2n_AB) + 1 <=14`,

hence `n_AB<=2` and therefore

`n_C>=3`.                                                     (6)

## 5. The Type-C supports are impossible

Each Type-C support has form `{c} union P_i`.

Because w_a=w_b=0 and a,b are target-nonadjacent to c, row closure against a Type-C support forces a and b target-anticomplete to both petals in P_i.

Thus the union of all Type-C petal vertices is a target clique: any petal nonedge together with a would be an independent triple in U.

There are at least three Type-C owner incidences by (6). With support multiplicity at most2, at least two distinct Type-C classes occur.

Exactly as in Sections2--3, the petal clique forces a universal petal z common to every Type-C class. The anchor c belongs to repeated D and z belongs to at least two support classes, so both are globally decorated. Therefore every Type-C support has defect at most2.

Each non-universal petal then has w=2 and every Type-C support is a target K3. For two distinct Type-C classes, the petal of one is adjacent to c, z and the other petal, so row closure forces w>=3, contradiction.

Thus two distinct Type-C classes cannot coexist, while at least two are required. Contradiction.

## 6. Conclusion

Neither nonclique multiplicity-two support type can occur.

Together with `Q36_F2_FAR_K2_C8_D2_A3_MULT2_K3_FULL_CLOSURE.md`, there are no multiplicity-two supports at all in the c=8, one-d2, A=3 far-K2 branch.