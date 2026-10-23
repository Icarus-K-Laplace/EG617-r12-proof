# q36 f=2, 2K1 far, a_F=1 — allowance-four disjoint repeated-K3 full closure

Status: `PROVED` under the same contract as `Q36_F2_A1_A4_DISJOINT_REPEATED_K3_RIGIDITY.md`.

Scope: the `c=8,A=4` and `c=9,A=4` repeated-K3 residuals. This theorem closes the branch in which a repeated target-K3 support has a second **disjoint repeated** support class. It does not by itself close either full layer.

## 1. Retained rigidity input

Let all low rows share the common missing triple `S=F union {x0}` with allowance four. Let `D,E subset R` be distinct disjoint repeated support classes, and assume `D` is a target `K3`.

The preceding rigidity theorem proves that any such pair is forced into the following exact state:

- `E` is also a target `K3`;
- the target cross graph `H[D,E]` is a three-edge star;
- after orienting the star centre as `d0 in D`, the bipartite target-nonedge graph between `D` and `E` is exactly `K_(2,3)` with the two-point side `D\{d0}`;
- with `w_v=kappa_v+e_F(v,x0)`, one has `w_(d0)=3`, the other two vertices of `D` have weight zero, every vertex of `E` has weight one;
- the whole CORE211 excess is concentrated at `d0`: `kappa_(d0)=2`, and every vertex of `R\{d0}` has core excess zero.

In particular, for every

`v in L := R\(D union E)`, `|L|=6`,

we have

`w_v = e_F(v,x0) <= 1`.                                      (1)

## 2. Every outside vertex must cover the cross-nonedge graph

Fix `v in L`.

Because `alpha(H[R])<=2`, for every target-nonedge `de` with `d in D`, `e in E`, the triple `{v,d,e}` cannot be independent. Therefore

`N_H(v) intersect (D union E)`

must be a vertex cover of the bipartite target-nonedge graph

`B = K_(2,3)`.                                               (2)

The unique minimum two-vertex cover of `K_(2,3)` is its two-point side `D\{d0}`. Equivalently, any vertex cover using at most one vertex from each side fails to cover all six edges.

## 3. Row closure forbids that cover

Common-S row closure against the two support classes gives, for every `v outside D union E`,

`e_H(v,D) <= w_v`,

`e_H(v,E) <= w_v`.                                          (3)

By (1), each right-hand side is at most one. Hence `v` can select at most one cover vertex from `D` and at most one from `E`.

But by (2) no such set covers `K_(2,3)`: every cover of size two must use the two vertices in `D\{d0}`, which would require

`e_H(v,D) >= 2`,

contradicting (3).

Thus no `v in L` can exist. Since `|L|=6`, contradiction.

## 4. Conclusion

Therefore:

> In the q36 `f=2`, far-`2K1`, `a_F=1`, allowance-four regime, a repeated target-K3 support cannot coexist with any distinct disjoint repeated support class.

Combining this with the existing `c=8,A=4` and `c=9,A=4` multiplicity reductions gives the sharper residual:

- if a multiplicity-three target-K3 support `D` exists, every support class disjoint from `D` is necessarily a singleton support class;
- hence the former repeated-K3 / arbitrary-disjoint-family residual collapses to a repeated-K3 plus singleton-only disjoint family.

For `c=8,A=4`, at least three owner incidences are carried by such disjoint singleton classes.
For `c=9,A=4`, at least four owner incidences are carried by such disjoint singleton classes.

## Boundary

This theorem does **not** exclude singleton support classes, intersecting repeated support classes, the `c=9,A=5` layer, or the `c=10,A=6` layer. It is a strict structural closure inside the A=4 residual, not a claim that E338 is closed.