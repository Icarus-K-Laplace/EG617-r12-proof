# E408 Q32 — conditional residual holonomy cost for exact colors

Date: 2026-10-29  
Status: **PROVED_CONDITIONAL finite local theorem with exhaustive verifier, restricted to placements where all ten isolated K5s are single-outside.** No Q32 closure claimed.

> **Scope correction (2026-10-29):** this seven-vertex baseline is not universal. The registered source-correct isolated-double placement leaves an eight-vertex gadget residual, audited in V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md. The classes and minimum-cost table below apply only to the seven-vertex subcase.

## 1. The nine-edge baseline on the seven residual vertices

Fix an exact non-target color C and assume all ten isolated K5 components are single-outside. Their H-parts are ten isolated transversal K4s, using ten vertices from each target track. The remaining set R_C has profile (2,2,2,1), and the induced graph J_C=C[R_C] has
\[
e(J_C)=9+g_C,\qquad 0\le g_C\le3,\qquad \alpha(J_C)\le2.
\]

Choose the color-C baseline matching on each track pair from the residual 1-factorizations. The ten isolated K4s contribute ten edges on every track pair. The baseline matching therefore leaves:
- two edges forming a perfect matching between each pair of residual two-vertex parts T1,T2,T3;
- one edge from the singleton residual vertex in T0 to one of the two residual vertices in each of T1,T2,T3.

These nine residual edges form a graph B_C. The g_C remaining C-edges form an extra set E_C^+ with
\[
J_C=B_C\cup E_C^+,\qquad |B_C|=9,\qquad |E_C^+|=g_C.
\]
On each large-part pair, E_C^+ is a matching, because it is a subset of the residual perfect matching P_ij. On a T0--Ti pair, an extra C-edge can only use the singleton residual vertex of T0. Pointwise saturation says every T0 vertex has C-degree 3 or 4, so the singleton can support **at most one extra C-edge across all three T0--Ti pairs combined**. The verifier now enforces this cross-pair cap; the earlier counts that allowed two or three T0 extras were too permissive.

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

The companion verifier enumerates every extra-edge set of size 0,1,2,3 from the nine edges not in B_C, requiring a matching within each large-track pair and at most one T0-incident extra edge in total, then checks alpha(B_C union E_C^+)<=2.

| Baseline class | Minimum g_C | Number of minimum repairs across all baselines | Consequence |
|---|---:|---:|---|
| A | 0 | 8 | Fully aligned K4+K3 base is already valid |
| B | 1 | 24 | A single extra edge can repair T0 misalignment |
| C | 2 | 72 | Nontrivial six-cycle holonomy costs at least two repeat edges |
| D | 3 | 72 | The alpha-four six-cycle pattern requires all three surplus units |

The complete admissible repair counts by surplus are:
- A: g=0: 8; g=1: 72; g=2: 264; g=3: 520.
- B: g=1: 24; g=2: 216; g=3: 696.
- C: g=2: 72; g=3: 720.
- D: g=3: 72.

The verifier also partitions every valid repair by how many surplus edges lie on T0--Ti pairs versus the three large-track pairs:

| Class | \(g_C\) | T0-pair extras | Large-pair extras | Count |
|---|---:|---:|---:|---:|
| A | 0 | 0 | 0 | 8 |
| A | 1 | 0 | 1 | 48 |
| A | 1 | 1 | 0 | 24 |
| A | 2 | 0 | 2 | 120 |
| A | 2 | 1 | 1 | 144 |
| A | 3 | 0 | 3 | 160 |
| A | 3 | 1 | 2 | 360 |
| B | 1 | 1 | 0 | 24 |
| B | 2 | 0 | 2 | 24 |
| B | 2 | 1 | 1 | 192 |
| B | 3 | 0 | 3 | 96 |
| B | 3 | 1 | 2 | 600 |
| C | 2 | 0 | 2 | 72 |
| C | 3 | 0 | 3 | 216 |
| C | 3 | 1 | 2 | 504 |
| D | 3 | 1 | 2 | 72 |

This gives two useful forced placement statements:
- **Class B at minimum cost \(g_C=1\)** must spend its only surplus edge on a T0--Ti pair.
- **Class C at minimum cost \(g_C=2\)** spends both surplus edges on large-track pairs and has no T0 surplus; **class D at \(g_C=3\)** has exactly one T0 surplus and two large-track surpluses.

These constraints are stricter than the scalar minimum-cost table and can be imposed directly in a future multicolor edge-packing model.

These are exact local counts after imposing the T0 pointwise degree cap, not asymptotic estimates. The minimum costs and the minimum-repair counts are unchanged; the full A/B repair counts are lower than in the first, uncapped enumeration. They verify that:
\[
\boxed{g_C\le1\Longrightarrow\text{the three large-part baseline matchings are aligned}.}
\]
Moreover, if the large-part matchings have nontrivial six-cycle holonomy, then g_C>=2; if the baseline has alpha four, then g_C=3.

## 4. Shape of the minimum repairs in the two nonaligned classes

The verifier also checks the independent-set geometry of the minimum repairs.

- **Class C (six-cycle, baseline alpha 3):** every baseline has exactly three independent triples. Two share a common pair of large-track vertices; the third is disjoint and consists of one vertex from each large track. Each of the three minimum two-edge repairs contains the edge joining the common pair, plus one of the three possible edges among the disjoint triple. Thus there is a **mandatory repeated-color edge** for every minimum-cost nonaligned class-C baseline.
- **Class D (six-cycle, baseline alpha 4):** every baseline has a unique independent 4-set consisting of T0's singleton and a transversal triple V of large-track vertices. The three T0 edges in the baseline attach to the complementary transversal triple U. Every minimum three-edge repair consists of one edge among U, an edge from T0 to one vertex w of V, and the edge joining the other two vertices of V. There are exactly 3×3=9 such repairs per baseline.

These repair patterns are stronger than the minimum-cost table alone. They identify which repeated-color edges are forced when a color uses the nonaligned residual holonomy class.

## 5. Global consequence and remaining frontier

For an exact color in this seven-vertex placement subcase, g_C lies in {0,1,2,3}; the global total exact-color gap remains 37-g_D. This conditional theorem sharpens the gap interpretation:
- within this seven-vertex subcase, any exact color with gap 0 or 1 has aligned large-track matching composition;
- within this subcase, a nonaligned exact color must spend at least two of its three allowed surplus units;
- the most obstructive local holonomy pattern spends all three.

This does not by itself rule out the global branch in which all ten exact colors have gaps 2 or 3. Moreover, the isolated-double placement must be handled separately; the table cannot be applied to a color unless all ten isolated components are single-outside. It gives a finite, auditable holonomy-cost ledger for that subcase to combine with the common pairwise 1-factorizations. E408/Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
