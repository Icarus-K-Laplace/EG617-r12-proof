# q36 f=2 far-target-K2 — c8 one-d2 A3: multiplicity-two K3 closure

Status: `PROVED` under the valid c=8 one-d2 A3 contract, common-S row closure, inherited D14, q36 lexicographic maximality, `alpha(H[U])<=2`, and the already proved absence of multiplicity-three supports.

## 1. Setup

Assume D is a target-K3 support of owner multiplicity2.

Repeated-support q36 maximality gives

`defect(D)=sum_(d in D) w_d <=2`,

where `w_v=kappa_v+e_F(v,S)` for the common d3 missing set S.

Five owner incidences remain outside the D-class.

Any support disjoint from D is impossible:

- if it is nonclique, an internal target-nonedge requires at least3 D--support target edges to avoid an independent triple in U, but D has non-missing allowance at most2;
- if it is a target K3, the global-mass argument of `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_GLOBAL_MASS_CLOSURE.md` applies verbatim to D, that disjoint K3, and the pure d2 block D0, contradicting `sum_H w=37`.

Therefore every one of the five remaining owner incidences lies in a support intersecting D.      (1)

## 2. D14 forces one-point overlaps and zero far incidence

D14 on D gives

`3*2 + O_D + e_F(F,D) + 3 <=14`,

hence

`O_D+e_F(F,D)<=5`.

By (1), the five remaining owner incidences contribute at least5 to O_D. Thus equality is forced:

`O_D=5`,
`e_F(F,D)=0`.                                                (2)

Consequently every remaining owner incidence belongs to a support meeting D in exactly one point.

## 3. All five incidences attach to the same D-vertex

Write `D={a,b,c}` and let E be any external support meeting D at a.

The vertices b,c lie outside E but are each target-adjacent to a because D is a K3. Row closure against E gives

`w_b>=1`,
`w_c>=1`.

Since `w_a+w_b+w_c<=2`, equality is forced:

`w_a=0`,
`w_b=w_c=1`.                                                (3)

If another external support met D at b or c, the same argument would force a different zero-weight vertex and contradict (3). Therefore every external owner incidence meets D at the same point a.

Thus every external support has the form

`{a} union P_i`,  |P_i|=2.                                  (4)

## 4. The petal union is a target clique

For any external support E={a,u,v}, row closure against E for b gives

`1+e_H(b,{u,v}) <= w_b=1`,

so b is target-anticomplete to its petal pair. The same holds for c. Hence b and c are target-anticomplete to every petal vertex appearing in any P_i.

If two petal vertices u,v were target-nonadjacent, then `{b,u,v}` would be an independent triple in U, contradicting `alpha(H[U])<=2`.

Therefore the union of all petal vertices is a target clique.        (5)

## 5. A universal petal is forced

Consider a petal vertex z that is not present in every distinct external support class. Choose a support E={a,u,v} not containing z.

By (5), z is target-adjacent to both u and v. Therefore row closure against E gives

`w_z>=2`.                                                     (6)

Suppose some support E={a,u,v} had neither u nor v universal. Then (6) gives `w_u,w_v>=2`, so the support defect is at least4, impossible even for a singleton d3 support.

Hence every petal pair P_i contains a vertex common to all support classes. Therefore there exists a universal petal z and every external support has form

`E_i={a,z,t_i}`.                                              (7)

The five owner incidences are carried by support classes of multiplicity at most2, so there are at least three distinct petals t_i.

## 6. Lexicographic maximality gives the final contradiction

The core vertices a and z each belong to at least two owner support incidences and are therefore globally decorated.

For any support class E_i={a,z,t_i}, a full-defect3 q36 repivot would remove the active decorated shell vertex x, retain the two inactive decorated shell vertices, and insert at least the two globally decorated core vertices a,z. Tau would strictly increase above the original q36 value3.

Therefore every E_i has defect at most2.                       (8)

For a non-universal petal t_i, choose a distinct support E_j not containing t_i. By (5), t_i is adjacent to z and to t_j; (7)--(8) and row closure force

`w_(t_i)>=2`.

Since E_i has defect at most2, equality follows: `w_(t_i)=2`, the universal vertices a,z have zero w-weight, and E_i has zero internal missing count. Hence E_i is a target K3 and in particular a is target-adjacent to every t_i.

Now take another distinct petal t_j. Relative to support E_i={a,z,t_i}, the vertex t_j is target-adjacent to all three support vertices a,z,t_i. Row closure gives

`w_(t_j)>=3`,

contradicting the already forced value `w_(t_j)=2`.

## 7. Conclusion

No multiplicity-two target-K3 support exists in the c=8, one-d2, A=3 far-K2 branch.

Together with the multiplicity-three global-mass closure, every repeated K3 support is now eliminated. Any remaining repeated support must be nonclique.