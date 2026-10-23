# q36 f=2 far-target-K2 — c=8, one d2 row, A=3 repeated-K3 closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_A3_MULTIPLICITY_REDUCTION.md`, common-S row closure, CORE211, and the induced `alpha(H[U])<=2` property.

This eliminates the repeated-K3/disjoint-K3 multiplicity-three terminal from the A=3 branch.

## 1. Setup

Let D be a target K3 support of multiplicity3. By q36 lexicographic maximality, a repeated support cannot use full defect3, so D has defect at most2.

The A=3 multiplicity reduction proves that at least two external owner incidences are carried by supports disjoint from D and that every support disjoint from D is itself a target K3. Choose one such distinct support E.

The union U of all d3 supports has `alpha(H[U])<=2` because the unique pure d2 block D0 is target-anticomplete to every d3 support.

Write

`w_v=kappa_v+e_F(v,x)`

for the active decorated missing vertex x. Every remainder vertex is target-anticomplete to the far K2.

## 2. The D--E cross graph has at most two target edges

For the repeated K3 D, internal missing count is0. Defect<=2 gives

`u(D)=kappa(D)+e_F(S,D)<=2`,

where `S=F union {x}`.

Since D and E are disjoint supports of the same common-S class, joint row closure yields

`e_H(D,E)<=u(D)<=2`.                                        (1)

## 3. Six-point vertex-cover contradiction

Let B be the bipartite target-nonedge graph between D and E. Since each side has3 vertices and at most2 target cross edges exist,

`|E(B)|>=7`.

Any bipartite graph obtained from K3,3 by deleting at most2 edges still has matching number3. Hence by Konig its minimum vertex-cover size is3.

Put

`L=R\(D union E)`,

so |L|=6.

For v in L, if `N_H(v) intersect (D union E)` failed to cover B, there would be a target-nonedge de with d in D, e in E and v target-nonadjacent to both, giving an independent triple {d,e,v} in U. Therefore

`e_H(v,D)+e_H(v,E)>=3`.                                    (2)

Row closure against D and E gives

`e_H(v,D)<=w_v`,
`e_H(v,E)<=w_v`.

Thus (2) implies

`w_v>=2`

for every v in L, so

`sum_L w_v>=12`.                                           (3)

But CORE211 gives

`kappa(L)<=2`,

and x can be target-adjacent to at most the six vertices of L, so

`sum_L w_v=kappa(L)+e_F(x,L)<=2+6=8`,                     (4)

contradicting (3).

## 4. Conclusion

The repeated-K3/disjoint-K3 multiplicity-three geometry is impossible.

Therefore in the c=8, one-d2, A=3 branch, the only multiplicity-three support geometry still surviving the current proof chain is the exact one-edge q35 equality terminal

`O_D=4`, `e_H(D)=1`, `kappa(D)=0`, `e_F(F union {x},D)=0`.