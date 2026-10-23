# q36 f=2, 2K1 far, a_F=1 — full elimination of multiplicity-three supports in c=7,A=3

Status: `PROVED` under `Q36_F2_2K1_A1_C7_A3_MULTIPLICITY_RIGIDITY.md`, `Q36_F2_2K1_A1_C7_A3_TRIPLE_ONEEDGE_FULL_CLOSURE.md`, row closure, CORE211, and `alpha(H[R])<=2`.

The one-edge multiplicity-three state is already empty. This note eliminates the remaining target-K3 multiplicity-three state. Hence every surviving support class has multiplicity at most2.

## 1. Remaining multiplicity-three state

Suppose D is a support of multiplicity3.

By the previous closure, D must be a target K3. The multiplicity rigidity theorem gives

`O_D + e_F(Y,D) <=2`,                                      (1)

where

`O_D=sum_(E!=D) r(E)*|D intersect E|`.

Because D is a target K3, its internal missing count is zero. Its repeated-support defect bound therefore gives

`u_D:=kappa(D)+e_F(x0,D)<=2`.                              (2)

## 2. Any support disjoint from D would also have to be a K3

Let E be another support disjoint from D.

The common-S joint-row theorem gives

`e_H(D,E)<=u_D<=2`.                                        (3)

Suppose H[E] contained a target nonedge uv. Since `alpha(H[R])<=2`, each of the three vertices of the clique D must be adjacent to at least one of u,v; otherwise that D-vertex together with u,v is an independent triple.

Hence `e_H(D,E)>=3`, contradicting (3).

Therefore every support disjoint from D is itself a target K3.              (4)

## 3. Two disjoint K3 supports are impossible

Assume such a disjoint support E exists. By (3),

`e_H(D,E)<=2`.

Put

`L=R\(D union E)`, so `|L|=6`.

For `v in L`, to avoid an independent triple consisting of v, one vertex of D and one vertex of E, the neighbourhood of v in `D union E` must cover all target-nonedges of the bipartite pair D--E.

That nonedge graph is `K3,3` with at most two edges removed. Its minimum vertex-cover size is3. Therefore

`e_H(v,D)+e_H(v,E)>=3`.                                    (5)

Write

`w_v=kappa_v+e_F(v,x0)`.

All vertices of R are target-nonadjacent to the two far shell vertices, so row closure for both supports gives

`e_H(v,D)<=w_v`,
`e_H(v,E)<=w_v`.

From (5), integer-valuedness gives `w_v>=2` for every v in L. Thus

`sum_L w_v>=12`.                                           (6)

But CORE211 gives `kappa(L)<=2`, and trivially `e_F(x0,L)<=6`. Hence

`sum_L w_v<=2+6=8`,

contradicting (6).

Therefore

> no support is disjoint from D.                           (7)

## 4. The overlap budget is then impossible

There are four owner incidences outside the multiplicity-three D-class.

By (7), every support carrying any of those four owners intersects D. Each such owner incidence contributes at least one to the weighted overlap O_D. Hence

`O_D>=4`.                                                   (8)

This contradicts (1), which gives `O_D<=2`.

Therefore no multiplicity-three target-K3 support exists.

## 5. Conclusion

Combining with the one-edge multiplicity-three closure:

> in the c=7,A=3 terminal, every support class has multiplicity at most2.

The remaining owner partitions are therefore built only from 2s and 1s: `2+2+2+1`, `2+2+1+1+1`, `2+1+1+1+1+1`, or all singletons.