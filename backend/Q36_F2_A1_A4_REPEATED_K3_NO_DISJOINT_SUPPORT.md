# q36 f=2, 2K1 far, a_F=1 — repeated-K3 cannot coexist with any disjoint support

Status: `PROVED` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, common-S row closure, CORE211, lexicographic q36 maximality, and `alpha(H[R])<=2`.

Scope: allowance four in the c=8 and c=9 residuals.

## Theorem

Let `D subset R` be a repeated support class of size three and suppose `H[D]=K3`. Then there is no distinct support class `E subset R` with `D intersect E=empty`.

Consequently the multiplicity-three branches in both `c=8,A=4` and `c=9,A=4` are empty, because their existing multiplicity reductions force respectively at least three and at least four outside owner incidences into supports disjoint from the multiplicity-three K3.

## 1. Weight and row-closure setup

Write

`w_v = kappa_v + e_F(v,x0)`

for vertices of the 12-point remainder R. Vertices of R are target-anticomplete to the far pair, so this is the full non-missing charge relevant to the common missing triple.

Since D repeats, lexicographic maximality forces its repivot to lose at least one q-unit. Under allowance four and `H[D]=K3`, this gives

`u(D):=sum_(d in D) w_d <= 3`.                              (1)

For every support T and every vertex v outside T, common-S row closure gives

`e_H(v,T) <= w_v`.                                          (2)

Hence for disjoint supports D,E,

`e_H(D,E) <= min(u(D),u(E))`.                               (3)

Also, since `alpha(H[R])<=2`, no support triple is independent, so every support E has at least one internal target edge.

## 2. A one-edge support E is impossible

Assume `e_H(E)=1`. Then the internal missing graph of E has two edges and therefore every `d in D` must be target-adjacent to at least one vertex of E; otherwise d together with the endpoints of an internal target-nonedge of E would form an independent triple.

Thus

`e_H(D,E) >= 3`.                                            (4)

But `mu(E)=2`, so allowance four gives

`u(E) <= 2`.                                                (5)

Equations (3)--(5) contradict each other.

Therefore any disjoint support E would have

`e_H(E)>=2`.                                                (6)

## 3. The D--E target-nonedge graph has at least six edges

By (1) and (3),

`e_H(D,E) <= 3`.                                            (7)

There are nine possible cross pairs between the two triples. Let B be the bipartite graph whose edges are the target-nonedges between D and E. Then

`|E(B)| = 9-e_H(D,E) >= 6`.                                 (8)

Let

`L = R\(D union E)`,

so `|L|=6`.

Fix `v in L`. For every nonedge `de in E(B)`, the triple `{v,d,e}` cannot be independent. Hence

`N_H(v) intersect (D union E)`

is a vertex cover of B.                                    (9)

A set containing at most one vertex of D and at most one vertex of E can cover at most five edges of a bipartite graph on 3+3 vertices: if the selected pair is itself an edge, their incident-edge union has size at most `3+3-1=5`; if it is a nonedge, each selected vertex has degree at most two toward the opposite side after that missing pair, so the union is even smaller.

Since B has at least six edges, every cover in (9) must therefore contain at least two vertices from D or at least two vertices from E. Thus

`e_H(v,D)>=2` or `e_H(v,E)>=2`.                              (10)

By row closure (2),

`w_v>=2` for every `v in L`.                                (11)

## 4. CORE211 excess contradiction

For vertices of R,

`w_v=kappa_v+e_F(v,x0)`

with `e_F(v,x0)<=1`. Therefore (11) implies

`kappa_v>=1` for every `v in L`.

Hence

`sum_(v in R) kappa_v >= sum_(v in L) kappa_v >= 6`.         (12)

But CORE211 has total core excess exactly at most two. Contradiction.

This proves the theorem.

## 5. Immediate c=8 and c=9 consequences

The retained `c=8,A=4` multiplicity reduction says that if a support has multiplicity three, it is a target K3 and at least three of the five remaining owner incidences lie in supports disjoint from it. The theorem forbids even one such support. Therefore

> `c=8,A=4`: the entire multiplicity-three branch is EMPTY.

Likewise the retained `c=9,A=4` reduction forces at least four outside owner incidences into supports disjoint from any multiplicity-three target K3. Therefore

> `c=9,A=4`: the entire multiplicity-three branch is EMPTY.

Together with the earlier exclusion of multiplicity four, both A=4 layers now reduce to systems in which every support class has multiplicity at most two.

## Boundary

This theorem does not yet exclude the remaining multiplicity-at-most-two support systems, `c=9,A=5`, or `c=10,A=6`. It is a strict closure of the multiplicity-three residual.