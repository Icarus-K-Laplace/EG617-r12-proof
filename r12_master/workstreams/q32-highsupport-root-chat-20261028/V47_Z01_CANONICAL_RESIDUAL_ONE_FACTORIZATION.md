# E408 Q32 — residual 1-factorizations across the aligned tracks

Date: 2026-10-29  
Status: **PROVED_CONDITIONAL exact structural theorem.** No Q32 closure claimed.

> **Residual-scope audit (2026-10-29):** the pairwise Hall/1-factorization statements in Sections 2–3 are unaffected. The global (g_C=0,1) orientation in Section 4 follows from the 69/70 near-Turán classification and remains global. However, the four-class 7-vertex holonomy-cost table in V47_Z01_RESIDUAL_HOLONOMY_COST.md applies only when all ten isolated K5 components are single-outside; an isolated-double placement has an 8-vertex gadget residual, documented in V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md.

> **Audit correction:** the residual factor P is not intrinsically canonical. At a vertex where a color repeats twice, the two same-colored edges are not individually distinguished as “the” repeated edge. The valid theorem is that, after choosing one perfect matching for each non-target color, their complement is a residual perfect matching. Different choices may give different residual factors.

## 1. Contract

Use the aligned z=0,1 cell from `V47_Z01_TRACK_ALIGNMENT.md`. The target-color graph H is partitioned into target cliques
`T_1,T_2,T_3\cong K_{12}` and `T_0\cong K_{11}`.
Let `\mathcal C` be the eleven non-target colors. Every 13-vertex set contains every color, so each C in `\mathcal C` has independence number at most 12.

The cross-track ledger proves that H-edges between two K12 tracks form a matching, and that each vertex of T0 has at most one H-neighbor in any K12 track.

## 2. Hall theorem for each color on a track pair

### Two K12 tracks

Let X,Y be two K12 tracks and fix a non-target color C. Both X and Y are independent sets in the C-colored graph. For any nonempty S subset Y with |S|=k, if its C-neighborhood in X had size at most k-1, then at least
`12-(k-1)=13-k`
vertices of X would have no C-edge to S. Selecting 13-k of them together with S would give a C-independent 13-set, contradiction. Hence
\[
|N_C(S)\cap X|\ge |S|\quad\text{for every }S\subseteq Y.
\]
Hall's theorem gives a perfect matching M_C between X and Y in color C.

Choose one such matching M_C for each of the eleven non-target colors. Since distinct colors have disjoint edge sets, these eleven perfect matchings are edge-disjoint. Their union has degree 11 at every vertex of K12,12. Its complement P therefore has degree one at every vertex and is a perfect matching.

Every H-edge lies in P, because none can belong to a non-target-color matching M_C. Every C-colored edge not selected into M_C also lies in P. Thus
\[
\boxed{K_{12,12}=P\;\dot\cup\;\bigdotcup_{C\in\mathcal C}M_C.}
\]
This is a 1-factorization into twelve edge-disjoint perfect matchings. P depends on the chosen M_C matchings; no uniqueness is asserted.

For a fixed choice, write
\[
s_{C,ij}=|P_{ij}\cap E_C(T_i,T_j)|.
\]
Then
\[
e_C(T_i,T_j)=12+s_{C,ij},\qquad
\sum_C s_{C,ij}=12-e_H(T_i,T_j).
\]
Every C-edge in P is a repeated-color edge relative to the selected baseline matching M_C. Conversely every vertex that repeats C has its second C-edge in P. The set of C-colored edges in P is a matching because P is a matching, and it pairs the repeated-C vertices on the two sides.

The previous degree ledger gives e_H(T_i,T_j)<=9, so every such residual factor P contains at least three H-edges and at least three non-target-colored repeat edges.

## 3. The asymmetric K11--K12 pair

Fix T0 and a K12 track Ti. For every non-target color C, its bipartite graph between T0 and Ti satisfies Hall's condition on the T0 side. If S subset T0 has size k>=1 and its C-neighborhood in Ti has size at most k-1, then at least
`12-(k-1)=13-k`
vertices of Ti avoid S. Selecting 13-k of them with S gives a C-independent 13-set, contradiction. Thus each C has a matching saturating T0.

Choose one such matching M_C for each non-target color. They are edge-disjoint and use eleven edges at every T0 vertex. Their complement P0i has exactly one edge incident to every T0 vertex, hence 11 edges, but it need not be a matching on the Ti side. All H-edges and all unselected C-edges lie in P0i. No symmetric degree-one or matching claim is made for the larger side.

For a fixed choice, if `s_{C,0i}=|P_{0i}\cap E_C(T_0,T_i)|`, then
\[
e_C(T_0,T_i)=11+s_{C,0i},\qquad
\sum_C s_{C,0i}=11-e_H(T_0,T_i).
\]
This is the precise asymmetric counterpart of the K12--K12 factorization.

## 4. Low-gap color orientation forced by the four tracks

Let `g_C=e_C(H)-69`.

### g_C=0

The source-checked Turán equality case gives C[H] = eleven disjoint K4s plus one K3. Every track is independent in C, so each K4 contains one vertex from each of the four tracks. These eleven K4s use all eleven vertices of T0 and eleven vertices in each K12 track. The remaining three vertices must be one each from T1,T2,T3, so the K3 lies entirely in the three K12 tracks.

The six baseline pairwise matchings therefore compose into eleven transversal K4s plus the all-large K3. In particular, the three large-track matchings form a triangle factor.

### g_C=1

The registered 70-edge near-Turan normal form is the same 69-edge base plus exactly one extra cross-part C-edge. The same track-capacity argument forces all eleven K4s to be transversal and the K3 to lie in T1,T2,T3.

For this color, choose its baseline matchings to be the pairwise edges of the 69-edge near-Turan base. This is a valid choice: the base gives a perfect matching on each K12--K12 pair and a matching saturating T0 on each K11--K12 pair. Under a compatible choice of the other colors' matchings, the one extra C-edge lies in the residual factors P/P0i. This statement is **choice-dependent**, not canonical.

The low-gap orientation conclusion uses the registered 69/70 near-Turan classification; it is not claimed for g_C>=2.

### Consequence for the nonexact-color gap split

In the aligned cell, the ten exact colors satisfy 0<=g_C<=3, while the unique nonexact color D satisfies 7<=g_D<=19, and
`\sum_{C\text{ exact}}g_C=37-g_D`.

If g_D>=18, the exact-color gap sum is at most 19, so at least one of the ten exact colors has g_C<=1. The preceding rigid 69/70 orientation then applies to at least one exact color.

The unresolved alternative is g_D<=17. If that branch also has no exact color with gap 0 or 1, then all ten exact colors have g_C in {2,3}; if k of them have gap 3, the exact budget is g_D=17-k, with 0<=k<=10. The global T0 theorem t_C<=1 then forces at least 10+k exact-color surplus edges on the three K12--K12 pairs, leaving the nonexact color at most 16+E0-k such surplus edges. This is a finite budget cut for the remaining multicolor argument, not a contradiction.

## 5. Scope

The 1-factorization is an exact structural constraint on every K12--K12 track pair. The K11--K12 statement is intentionally asymmetric. The results do not yet couple the three large-track factors strongly enough to eliminate the aligned z=0 or z=1 cell. Full-support E408/Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.


## 6. Status update — gap split resolved in aligned z=0,1

The Section 4 interval alternative is superseded for the aligned m=10 z=0,1, (2,2,2,1) cell by the exact gap-saturation theorem and V47_Z01_K6_CONTRADICTION.md. In that cell, g_D=7 and every exact g_C=3, and both outside patterns are impossible by a forced D-K6. This does not assert that the same gap cap or closure applies to nonaligned z=2,3,4 cells or other light-component splits.
