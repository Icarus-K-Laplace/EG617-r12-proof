# E408 Q32 — exact-color seven-vertex residual graph catalog

Date: 2026-10-29  
Status: **PROVED_CONDITIONAL local reduction plus exhaustive 7-vertex catalog.** No Q32 closure claimed.

## 1. Why every exact color leaves a seven-vertex graph

The source-correct Type-I factorization is
\[
C=10K_5\;\dot\cup\;G_{11}.
\]
Each of the ten isolated K5 components meets O in exactly one vertex, so its other four vertices form an isolated C-colored K4 in H. Every such K4 is transversal across the target tracks T0,T1,T2,T3, because each track is a target-color clique and hence C-independent.

The ten isolated K4s use 10 vertices from each track. The remaining seven H vertices, denoted R_C, therefore have track profile
\[
(|R_C\cap T_1|,|R_C\cap T_2|,|R_C\cap T_3|,|R_C\cap T_0|)
=(2,2,2,1).
\]
There are no C-edges from R_C to the ten isolated K4s, since those K5s are isolated components of the full color graph.

Let J_C=C[R_C]. The ten isolated K4s contribute 60 edges to C[H], while
\[
e_C(H)=69+g_C,\qquad 0\le g_C\le3.
\]
Consequently
\[
\boxed{|V(J_C)|=7,\quad e(J_C)=9+g_C,\quad 0\le g_C\le3.}
\]

Since \alpha(C)<=12 and the ten isolated K4s are separate components,
\[
10+\alpha(J_C)=\alpha(C[H])\le12,
\]
so \alpha(J_C)<=2. It is exactly two because each track pair of residual vertices is independent.

The balanced-coloring degree floor also gives
- each of the six vertices in T1,T2,T3 has degree at least two in J_C (one C-neighbor in each of the other two K12 tracks);
- the singleton vertex in T0 has degree at least three in J_C (one C-neighbor in each K12 track).

No edge of J_C can lie within one of its four track parts.

## 2. Exhaustive catalog of the necessary local relaxation

There are exactly 18 possible edges between parts of sizes (2,2,2,1). The companion script enumerates all 2^18 graphs and retains those satisfying:
1. e(J_C) is 9, 10, 11, or 12;
2. alpha(J_C)<=2;
3. the six big-part vertices have degree at least two;
4. the T0 singleton has degree at least three.

It also tests whether the graph contains a disjoint K4+K3 base with the K4 transversal across all four parts and the K3 on T1,T2,T3.

Exact counts:

| g_C | e(J_C) | Labeled graphs satisfying necessary conditions | Contain K4 dot-union K3 base | Do not contain such a base |
|---:|---:|---:|---:|---:|
| 0 | 9 | 8 | 8 | 0 |
| 1 | 10 | 72 | 72 | 0 |
| 2 | 11 | 384 | 288 | 96 |
| 3 | 12 | 1,148 | 668 | 480 |

For g_C=0, the eight graphs are exactly the eight choices of a transversal K4; the remaining vertices form the K3. For g_C=1, every admissible graph is one such K4+K3 base plus one extra cross-part edge. This independently reproduces the 69/70 near-Turan rigidity in the seven-vertex residual.

For g_C=2 or 3, the necessary graph constraints alone no longer force a K4+K3 base. The Type-I gadget incidences and exact placement geometry must be used to screen the 96 and 480 non-base cases further. These counts are a necessary relaxation, not a count of realizable full Q32 colorings.

## 3. How this feeds the multicolor attack

For each exact color C, the ten isolated transversal K4s cover 10 vertices in every target track. Its remaining 7 vertices support J_C, whose edges are the only C-edges in H not already accounted for by those ten isolated components.

The three large-track pairwise color matchings and the T0--Ti matchings from `V47_Z01_CANONICAL_RESIDUAL_ONE_FACTORIZATION.md` must be compatible with these residual seven-vertex graphs. The catalog isolates the exact local frontier:
- gaps 0 and 1 have rigid K4+K3 structure;
- gaps 2 and 3 have a finite set of additional local shapes;
- each exact color has gap at most 3, and the nonexact color has gap at least 7.

The next global step is to couple these per-color residual shapes through edge uniqueness across the common track pairs. The local catalog does not close z=0,1. E408/Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
