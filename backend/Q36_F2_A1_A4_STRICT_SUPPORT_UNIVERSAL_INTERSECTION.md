# q36 f=2, 2K1 far, a_F=1 — allowance-four strict-support universal-intersection theorem

Status: `PROVED` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, common-S row closure, CORE211, lexicographic q36 maximality, and `alpha(H[R])<=2`.

Scope: the allowance-four common-S triple-support systems occurring in the c=8 and c=9 residuals. This theorem is independent of support multiplicity.

## 1. Setup

All owner rows have common missing triple

`S=F union {x0}`

and 3-point supports inside the 12-point remainder `R`.

For `v in R` put

`w_v = kappa_v + e_F(v,x0)`.

The far pair F is target-anticomplete to R in this normal form, so this is the complete common-S charge on R.

For a support D define

`w(D)=sum_(v in D) w_v`,
`mu(D)=3-e_H(D)`,
`delta(D)=w(D)+mu(D)<=4`.

A strict q-loss owner has

`delta(D)<=3`.                                               (1)

For disjoint supports D,E, row closure gives

`e_H(D,E)<=min(w(D),w(E))`.                                 (2)

Also `alpha(H[R])<=2`, so every support triple spans at least one target edge.

## 2. One-edge strict supports cannot be disjoint

Suppose D is strict and `e_H(D)=1`. Then `mu(D)=2`, so (1) gives

`w(D)<=1`.                                                   (3)

The target-nonedge graph inside D has two edges. For every `e in E`, the set `N_H(e) intersect D` must cover those two nonedges; otherwise e together with an uncovered target-nonedge of D is an independent triple. Hence every e has at least one target neighbour in D and

`e_H(D,E)>=3`.                                               (4)

This contradicts (2),(3).

## 3. Two-edge strict supports cannot be disjoint

Suppose `e_H(D)=2`. Then `mu(D)=1`, so

`w(D)<=2`.                                                   (5)

D has one internal target-nonedge. Every vertex of E must meet at least one endpoint of that nonedge, again by `alpha(H[R])<=2`. Thus

`e_H(D,E)>=3`,                                               (6)

contradicting (2),(5).

## 4. K3 strict supports cannot be disjoint

Now suppose `H[D]=K3`. Then `mu(D)=0` and

`w(D)<=3`.                                                   (7)

Let E be any disjoint support.

### 4.1 E has one internal target edge

If `e_H(E)=1`, then `mu(E)=2` and the allowance-four bound gives

`w(E)<=2`.

The same uncovered-nonedge argument applied to E forces every d in D to have a target neighbour in E, so `e_H(D,E)>=3`, while (2) gives `e_H(D,E)<=2`. Contradiction.

### 4.2 E has at least two internal target edges

By (2),(7),

`e_H(D,E)<=3`.

Hence the bipartite graph B of target-nonedges between D and E has at least

`9-3=6` edges.                                               (8)

Let

`L=R\(D union E)`,

so `|L|=6`.

Fix `v in L`. For every target-nonedge `de` of B, `{v,d,e}` cannot be independent. Therefore

`N_H(v) intersect (D union E)`

is a vertex cover of B.                                     (9)

A cover containing at most one vertex from D and at most one from E covers at most five edges of a bipartite graph on 3+3 vertices: if the selected cross pair is an edge, its two stars cover at most `3+3-1=5`; if it is a nonedge, each selected vertex has degree at most two toward the opposite side, so the union is at most four.

Since B has at least six edges, (9) forces

`e_H(v,D)>=2` or `e_H(v,E)>=2`.                              (10)

Row closure therefore gives

`w_v>=2` for every `v in L`.                                (11)

But `w_v=kappa_v+e_F(v,x0)` and `e_F(v,x0)<=1`, so

`kappa_v>=1` for all six vertices of L.                     (12)

This forces total core excess at least six, contradicting CORE211, whose total excess is two.

Thus the K3 case is impossible as well.

## 5. Theorem

Combining Sections 2--4:

> **Strict-support universal-intersection theorem.**
>
> In the q36 `f=2`, far-`2K1`, `a_F=1`, allowance-four triple-support regime, every support belonging to a strict q-loss owner intersects every support class in the system.

Equivalently, a pair of disjoint support classes can occur only when both classes are q-plateau singleton classes.

## 6. Immediate owner-count consequence

Here `S=F union {x0}` contains exactly one globally decorated shell vertex, so `s=|S intersect X|=1<3`.

`GLOBAL_PLATEAU_CAPACITY_THEOREM.md` gives at most three plateau owners. Therefore

- in c=8, at least five owner rows are strict;
- in c=9, at least six owner rows are strict.

Since the already-proved A4 multiplicity reductions now give class multiplicity at most two, each layer contains at least three distinct strict support classes, and every one of those classes intersects every support class.

Thus the remaining A4 system is a 3-uniform support hypergraph on 12 core vertices with at least three universal-intersecting strict classes and with disjointness confined entirely to at most three plateau singleton classes.

## Boundary

This theorem does not yet exclude the resulting near-pairwise-intersecting support hypergraph. It is the structural input for the next incidence/packing step.