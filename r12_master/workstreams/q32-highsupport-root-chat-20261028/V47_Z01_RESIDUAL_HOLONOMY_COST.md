# E408 Q32 — exact residual holonomy cost for each exact color

Date: 2026-10-29  
Status: **PROVED_CONDITIONAL finite local theorem with exhaustive verifier.** No Q32 closure claimed.

## 1. The nine-edge baseline on the seven residual vertices

Fix an exact non-target color C. Its source-correct Type-I factorization contains ten isolated K5 components. Their H-parts are ten isolated transversal K4s, using ten vertices from each target track. The remaining set R_C has profile (2,2,2,1), and the induced graph J_C=C[R_C] has
\[
e(J_C)=9+g_C,\qquad 0\\le g_C\\le3,\qquad \\alpha(J_C)\\le2.
\]

Choose the color-C baseline matching on each track pair from the residual 1-factorizations. The ten isolated K4s contribute ten edges on every track pair. The baseline matching therefore leaves:
- two edges forming a perfect matching between each pair of residual two-vertex parts T1,T2,T3;
- one edge from the singleton residual vertex in T0 to one of the two residual vertices in each of T1,T2,T3.

These nine residual edges form a graph B_C. The g_C remaining C-edges form an extra set E_C^+ with
\[
J_C=B_C\\cup E_C^+,\\qquad |B_C|=9,\\qquad |E_C^+|=g_C.
\]
On each large-part pair, E_C^+ is a matching, because it is a subset of the residual perfect matching P_ij. On each T0--Ti pair, there is at most one extra edge, because the residual T0 vertex has only one P0i edge.

Thus every exact color induces one of only 64 possible nine-edge baselines B_C: two choices for each of the three large-part perfect matchings and two choices for each of the three T0 attachments.

## 2. Four baseline holonomy classes

The union of the three large-part perfect matchings is a 2-regular graph on six vertices. It is either two disjoint triangles (aligned composition) or a six-cycle (nontrivial holonomy). The three T0 attachments then give four classes:

| Class | Large-part matching composition | T0 attachment | Baseline alpha | Number of baselines |
|---|---|---|---:|---:|
| A | two triangles | all three T0 edges attach to one triangle | 2 | 8 |
| B | two triangles | attachments split across both triangles | 3 | 24 |
| C | six-cycle | attachment pattern with alpha 3 | 3 | 24 |
| D | six-cycle | attachment pattern with alpha 4 | 4 | 8 |

The counts sum to all 64 baselines.

## 3. Exact minimum surplus needed to restore alpha <= 2

The companion verifier enumerates every admissible extra-edge set of size 0,1,2,3 from the nine edges not in B_C, rejects extra edges that are not a matching within their track pair, and checks alpha(B_C union E_C^+)<=2.

| Baseline class | Minimum g_C | Number of minimum repairs across all baselines | Consequence |
|---|---:|---:|---|
| A | 0 | 8 | Fully aligned K4+K3 base is already valid |
| B | 1 | 24 | A single extra edge can repair T0 misalignment |
| C | 2 | 72 | Nontrivial six-cycle holonomy costs at least two repeat edges |
| D | 3 | 72 | The alpha-four six-cycle pattern requires all three surplus units |

The complete admissible repair counts by surplus are:
- A: g=0: 8; g=1: 72; g=2: 288; g=3: 672.
- B: g=1: 24; g=2: 288; g=3: 1,152.
- C: g=2: 72; g=3: 720.
- D: g=3: 72.

These are exact local counts, not asymptotic estimates. They verify that:
\[
\\boxed{g_C\\le1\\Longrightarrow\\text{the three large-part baseline matchings are aligned}.}
\]
Moreover, if the large-part matchings have nontrivial six-cycle holonomy, then g_C>=2; if the baseline has alpha four, then g_C=3.

## 4. Global consequence and remaining frontier

For the ten exact colors, each g_C lies in {0,1,2,3}; the total exact-color gap is 37-g_D. This local theorem sharpens the gap interpretation:
- any exact color with gap 0 or 1 has aligned large-track matching composition;
- a nonaligned exact color must spend at least two of its three allowed surplus units;
- the most obstructive local holonomy pattern spends all three.

This does not by itself rule out the global branch in which all ten exact colors have gaps 2 or 3. It gives a finite, auditable holonomy-cost ledger to combine with the common pairwise 1-factorizations. E408/Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
