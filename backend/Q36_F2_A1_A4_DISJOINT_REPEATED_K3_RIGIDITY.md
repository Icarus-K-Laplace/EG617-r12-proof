# q36 f=2, 2K1 far, a_F=1 — allowance-four disjoint repeated-K3 rigidity

Status: `PROVED REDUCTION` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, common-S row closure, CORE211, lexicographic q36 maximality, and `alpha(H[R])<=2`.

Scope: the c=8,A=4 and c=9,A=4 repeated-K3 residuals. This is a structural theorem only; it does not by itself close either layer.

## 1. Setup

Let all low rows have the same three-point missing set `S=F union {x0}` and common-S allowance4. Let D and E be two distinct disjoint support classes, both repeated. Assume D is a target K3.

For any repeated support, full defect4 would repivot to q36 while retaining the inactive decorated shell vertices and inserting three globally decorated support vertices. This strictly raises tau. Hence every repeated support has defect at most3 and repivots to q<=35.

Write

`w_v=kappa_v+e_F(v,x0)`

for v in the 12-point remainder R. Core vertices in R are target-anticomplete to the far pair F, so for a target-K3 support D the non-missing defect is

`u(D)=sum_(v in D) w_v<=3`.

Common-S row closure gives

`e_H(D,E)<=min(u(D),u(E))`.                                 (1)

## 2. A disjoint repeated support E must also be a K3

Suppose E is nonclique.

Because `alpha(H[R])<=2`, every internal target nonedge uv of E must be covered from each vertex d in D: otherwise {d,u,v} is an independent triple. Thus every d in D has a target neighbour in a vertex cover of the internal nonedge graph of E. In particular

`e_H(D,E)>=3`.                                               (2)

If E has one target edge then `m(E)=2`; repeated-support defect<=3 gives

`u(E)<=1`,

contradicting (1)--(2).

If E has two target edges then `m(E)=1`; repeated-support defect<=3 gives

`u(E)<=2`,

again contradicting (1)--(2).

Therefore E is a target K3.                                    (3)

## 3. The cross graph has exactly three target edges

Now both D and E are K3s and `u(D),u(E)<=3`, so

`e_H(D,E)<=3`.                                               (4)

Let B be the bipartite target-nonedge graph between D and E. Thus

`B = K_(3,3) \ E_H(D,E)`

and B has at least6 edges.

Take v in `L=R\(D union E)`, so |L|=6. To avoid an independent triple {d,e,v} for every target-nonedge de in B, the set

`N_H(v) intersect (D union E)`

is a vertex cover of B.

If the matching number of B were3, Konig's theorem would give vertex-cover number3. Hence

`e_H(v,D)+e_H(v,E)>=3`.

Row closure against D and E gives each cut at most w_v, so w_v>=2 for every v in L. Therefore

`sum_L w_v>=12`.

But CORE211 gives `kappa(L)<=2`, while trivially `e_F(x0,L)<=6`, so

`sum_L w_v<=8`,

a contradiction.

Thus B has matching number at most2. Since B is a bipartite graph on 3+3 vertices with at least6 edges, its vertex-cover number is at most2. A two-vertex cover using one vertex from each side covers at most5 edges, so both cover vertices lie on the same side. The maximum is then6, hence equality is forced:

- B has exactly6 edges;
- `e_H(D,E)=3`;
- B is exactly K_(2,3) (or its transpose).

Equivalently:

> the target cross graph H[D,E] is exactly a 3-edge star K_(1,3).          (5)

## 4. Exact w-pattern and CORE211 saturation

Assume the cross star is centred at d0 in D, so d0 is target-adjacent to all three vertices of E and the other two D-vertices have no target neighbour in E.

Row closure against E gives

`3=e_H(d0,E)<=w_(d0)`.

But `u(D)=sum_D w<=3`, so equality holds throughout:

- `w_(d0)=3`;
- the other two vertices of D have w=0;
- `u(D)=3`.

Thus the D-repivot has defect3 and q=35.

For each e in E,

`1=e_H(e,D)<=w_e`.

Since `u(E)=sum_E w<=3`, again equality is forced:

- every e in E has w_e=1;
- `u(E)=3`;
- the E-repivot also has q=35.                                  (6)

Finally CORE211 has total core excess at most2. Since

`w_(d0)=kappa_(d0)+e_F(d0,x0)=3`

and the shell contribution is at most1, necessarily

- `kappa_(d0)=2`;
- `e_F(d0,x0)=1`;
- every other vertex of R has core excess0.

For each e in E, w_e=1 and kappa_e=0, hence

`e_F(e,x0)=1`.

Therefore the exact surviving geometry of a disjoint repeated-K3 pair is:

> one support D has all CORE211 excess concentrated at the star centre d0;
> x0 is target-adjacent to d0 and to all three vertices of E;
> the D--E target cross graph is the star centred at d0;
> both support repivots have q=35.                             (7)

## 5. Interface

Consequences for c=8,A=4 and c=9,A=4:

1. any repeated support disjoint from a repeated K3 must itself be a K3;
2. such a pair is forced into the exact star geometry (7);
3. the pair consumes the entire CORE211 excess budget;
4. any further support compatibility must therefore be analysed with every vertex outside d0 core-regular.

This theorem is intended to replace generic allowance-three cross estimates in the remaining repeated-K3/disjoint-support residuals.