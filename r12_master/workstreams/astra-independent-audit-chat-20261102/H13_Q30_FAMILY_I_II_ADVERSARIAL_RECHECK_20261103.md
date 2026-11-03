# H13 Q30 Family I/II adversarial recheck

Date: 2026-11-03  
Frozen source: `frozen/cover/COVER_THEOREM.md`, Sections10–12, snapshot `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.  
Audit lineage: `workstream/r12-astra-independent-audit-20261102`.

## Verdict

**NO GAP FOUND in the Family I global-excess exclusion or Family II independent-transversal exclusion.** The most delicate local implication in the Family-II normal form was rederived explicitly. An adversarial alternative K4-minus-edge shell was constructed; it satisfies several static local constraints but is excluded by the separate `|X|=3` maximum-charge branch.

This is a focused analytic audit, not whole-EG617 or Lean certification.

## 1. Family I: rederive the row classes and global excess

Let `K` be the regular target K11 and `T_v` the three outside neighbors of `v in K`. For an active low point, the repivot identity at `beta=12` has base term `3(13-3)=30`; since `q_v<=Q=30`, all nonnegative corrections vanish, in particular `kappa=0`. Thus `T_v=N_C(v)` is a triangle. Inactive lows are true twins of the original pivot, so their `T_v` is the original hub triangle. Hence every `T_v` is a triangle.

The q30 Family-I shell is `K_{3,k}` plus isolates, `k in {8,9,10}`. Relative to any `v`, each other K-point is adjacent to all or none of `T_v`; therefore its row is equal to `T_v` or disjoint from it. The distinct row triangles form pairwise disjoint classes with multiplicities
[
1\le c_i\le3,\qquad \sum_i c_i=11.
]
If there are `r` classes, `r>=4` because `c_i<=3`, and `r<=5` because one point from each pairwise anticomplete triangle gives an independent r-set.

For `x` in a row class of multiplicity `c_i`, its degree is
[
d_F(x)=13+(10-k_i)=c_i+12.
]
For a pivot `w` in another row class `j`, x is nonadjacent to w and has exactly `c_i` neighbors in K. The repivoted core therefore has
[
d_{C_w}(x)=d_F(x)-c_i-e_F(x,T_j)
=12-e_F(x,T_j)\ge12.
]
Thus distinct row triangles are anticomplete in F, not merely disjoint.

The total degree excess of F above13 is
[
\sum_{v\in V(F)}(d_F(v)-13)=2E-13\cdot61.
]
The K11 contributes zero. The row triangles contribute exactly
[
3\sum_i(c_i-1)=3(11-r).
]
So the remainder has `50-3r` vertices and excess `2E-793-3(11-r)`.

| E | r | remainder vertices | remainder excess |
|---:|---:|---:|---:|
| 407 | 4 | 38 | 0 |
| 407 | 5 | 35 | 3 |
| 408 | 4 | 38 | 2 |
| 408 | 5 | 35 | 5 |

- **r=5:** every remainder vertex has no K-neighbor. If it failed to be adjacent to all three vertices of at least one row triangle, it could be joined with one nonneighbor from each of the five pairwise anticomplete triangles to form an independent6-set. Hence it completes a row triangle. In the corresponding core, all three of those neighbors are deleted and no K-neighbor is deleted, so `d_F(x)-3>=12`; thus every remainder vertex has excess at least2. The 35 vertices require at least70 excess, versus only3 or5 available.
- **r=4:** each regular remainder vertex has at most one neighbor in each row triangle; otherwise its degree in the corresponding core would be at most11. Any two nonadjacent regular remainder vertices leave at least one common-avoiding point in each of the four triangles, producing an independent6-set. Thus the at least36 regular remainder vertices form a clique, contradicting `omega(F)<=11`.

The r=4 and r=5 multiplicity partitions were also enumerated independently: r=4 has only (3,3,3,2); r=5 has (3,2,2,2,2), (3,3,2,2,1), and (3,3,3,1,1). No multiplicity case is omitted.

## 2. Family II: rederive the K4-minus-edge normal form

In the `|X|=2` branch, let `a,b` be the two weight-11 points, and let `uv` be an edge in the other 11-set. Equality in the subset identity gives:
- `t_a=t_b=11`, `t_u+t_v=13`;
- `S={a,b,u,v}` induces K4 minus one edge, with uv present;
- the other nine points R are independent and regular.

Since `|X|=2`, `t_u,t_v<=10`. Every R-point has at most four M-neighbors, all in S. It is regular, and the no-middle-degree assumption excludes degrees3 and4, so its M-degree is0,1,or2. Degree1 is impossible by EDGE13: its unique neighbor has weight at most11, giving edge-weight sum at most12. Since `z>=22` and `e_M(S)=5`, the nine R-points contribute at least17 incidences. With each degree either0 or2, this forces all nine to have degree2. On each incident edge EDGE13 then requires the S-endpoint to have weight at least11. Only a and b qualify, so every R-point is adjacent in M to both a and b.

Consequently each hub has nine R-neighbors. Since `t_a=t_b=11` and `t=d_M+g`, each hub's internal degree in S is at most2. In K4-e the two degree-2 vertices are exactly the endpoints of the missing edge, so the missing edge is ab. The low vertices u,v each have internal degree3 and no R-neighbors. Hence
[
g_u+g_v=(t_u+t_v)-6=7.
]
Neither decoration can vanish: that would make the corresponding vertex regular with missing degree3, excluded in this branch. Thus u,v are the two positive-decoration exceptional lows.

For every ordinary low y, `N_M(y)={a,b}`; in `A\N_M(y)` the only M-edge is uv and the total decoration is7. Therefore `rho=1+7=8`, and formula(3) gives
[
q_y=2(13-2)+8+h_{12}+\kappa+b
=30+h_{12}+\kappa+b.
]
Maximality `q_y<=Q=30` forces equality. So every ordinary low is itself a maximizing pivot, and its repivoted core has 287 edges and minimum degree12. The original pivot p also has q=30. This licenses the q30 classification at all ten K-points.

## 3. Family II: the ten-pair contradiction

The shell at each `v_i in K` consists of the other nine K-points, u,v, and two further vertices `T_i`. The other nine K-points are regular; u,v are globally decorated and adjacent to every K-point. In a Family-II view, the two decorated lows must therefore be u,v (this is a shell-local statement; it does not assert that the whole 61-vertex parent has only two decorated vertices). The two hubs `T_i` are regular, form an edge in F, are nonadjacent to u,v, and are nonadjacent to every other K-point. Thus each x in T_i has degree13 and is adjacent to `v_i` alone in K.

For `i!=j`, x in T_i is nonadjacent to `v_j`, hence lies in the actual 47-core `C_j=F-N[v_j]`. Its only neighbor in `N[v_j]` from K is `v_i`; the remaining deleted neighbors are exactly its neighbors in `T_j`. Therefore
[
d_{C_j}(x)=13-1-e_F(x,T_j)\ge12,
]
which forces `e_F(x,T_j)=0`. The pairs are disjoint (a shared point would be adjacent to two K-points) and pairwise anticomplete. Selecting one endpoint from each of the ten pairs gives an independent10-set, contradicting `alpha(F)<=5`.

## 4. Adversarial near-witness to the |X|=2 transition

To test whether the `|X|=2` argument was silently assuming the missing edge is ab, I built the following 13-vertex shell:

- S={a,b,u,v} induces K4-e with missing edge au;
- R is independent of size9;
- four R-points have M-neighborhood {a,v}, four have {b,v}, and one has {a,b};
- weights are `(t_a,t_b,t_u,t_v)=(11,11,2,11)`, and every R-point has weight2.

The resulting local shell has `z=23`, `G=7`, `q=30`, `alpha(M)=10`, no K4, and satisfies EDGE13. Its regular vertices have missing degrees only2 or11. Thus it is a genuine adversarial test of the local constraints.

It is **not** a counterexample to the theorem: `t_v=11`, so `|X|=3`, not2. Moreover, for each of the ten regular points outside X (u and the nine R-points), direct calculation gives `rho=9`. Formula(3) at beta12 yields
[
q_y\ge 2(13-2)+9=31>Q=30.
]
It is therefore excluded by the separate `|X|=3` branch. This test confirms why the case split is load-bearing and why the `|X|=2` proof must explicitly retain `t_u,t_v<=10`.

## 5. Disposition and scope

- Family-I row classes, cross-row anticompleteness, and both excess contradictions: **rederived; no gap found**.
- Family-II `|X|=2` normal form: **rederived; no gap found**.
- Family-II ten-pair independent transversal: **rederived; no gap found**.
- Cross-branch near-witness: **constructed and excluded by |X|=3 via q_y>=31**.
- Frozen theorem source: unchanged.

Artifacts:
- `RECHECK_H13_Q30_FAMILY_I_II_ADVERSARIAL.py`
- `RECHECK_H13_Q30_FAMILY_I_II_ADVERSARIAL.json`
- `H13_Q30_FAMILY_I_II_ADVERSARIAL_RECHECK_20261103.md`

This audit does not certify the complete K145 proof, remaining R(4,49) layers, the root verifier from a clean checkout, or Lean kernel certification.
