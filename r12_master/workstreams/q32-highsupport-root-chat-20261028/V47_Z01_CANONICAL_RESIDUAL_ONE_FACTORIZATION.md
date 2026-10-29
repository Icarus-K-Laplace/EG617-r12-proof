# E408 Q32 — canonical residual 1-factorization between the three K12 tracks

Date: 2026-10-29  
Status: **PROVED_CONDITIONAL exact structural theorem.** No Q32 closure claimed.

## 1. Contract

Use the aligned z=0,1 cell from `V47_Z01_TRACK_ALIGNMENT.md`. The target-color graph H is partitioned into target cliques
`T_1,T_2,T_3cong K_{12}` and `T_0cong K_{11}`.
Let `\mathcal C` be the eleven non-target colors. The frozen balanced-coloring premise is that every 13-vertex set contains every color. In particular, each C in `\mathcal C` has independence number at most 12.

The previous cross-track ledger proves that between two K12 tracks the H-edges form a matching, and between T0 and any K12 track every T0 vertex has at most one H-neighbor.

## 2. Vertex-level color count

Fix two K12 tracks X,Y and a vertex v in Y. The 13-set X union {v} forces every color C in `\mathcal C` to occur among the twelve edges from v to X. If v has an H-neighbor in X, exactly one of the twelve edges is H-colored, so the other eleven edges contain each non-target color exactly once. If v has no H-neighbor in X, all twelve edges are non-target-colored, so exactly one non-target color occurs twice and the other ten occur once.

Thus every vertex of X and Y has exactly one incident edge in the following canonical set P:
- its H-edge into the opposite track, if it has one;
- otherwise, its unique repeated-color edge into the opposite track.

If an edge xy is a repeated-color edge of color C, both x and y see that same edge as their repeated C-edge. Therefore every vertex on both sides has degree exactly one in P. Hence **P is a perfect matching of K12,12**. It contains every H-edge between X,Y, and its remaining edges are precisely the repeated-color edges.

For each C in `\mathcal C`, remove P from the C-colored bipartite graph. Every vertex has exactly one remaining C-edge: it has one C-edge outside P when P is H-colored or has another C-edge outside P when its P-edge is the repeated C-edge. Therefore
`M_C := E_C(X,Y) \setminus P`
is also a perfect matching.

Consequently the complete bipartite graph has the exact edge decomposition
[
\boxed{K_{12,12}=P\;\dot\cup\;\bigdotcup_{C\in\mathcal C}M_C,}
]
a 1-factorization into twelve edge-disjoint perfect matchings: one canonical residual matching P and one baseline matching for each of the eleven non-target colors.

## 3. Exact relationship to the repeat-color ledger

Write `h_{ij}=e_H(T_i,T_j)` for two K12 tracks. Since P contains all H-edges and has size 12:
- `P` contains exactly `h_{ij}` H-edges;
- `P` contains exactly `12-h_{ij}` repeated-color edges;
- for every non-target color C, `e_C(T_i,T_j)=12+s_{C,ij}`, where `s_{C,ij}=|P\cap E_C|`;
- `sum_C s_{C,ij}=12-h_{ij}`.

The earlier degree ledger gives `h_{ij}<=9`, so **each canonical residual matching P contains at least three H-edges and at least three repeated-color edges**.

This is stronger than a count of repeat labels: it identifies all repeat edges as a single matching on the two unmatched H-vertex sets. No repeated-color edge can share an endpoint with an H-edge in the same track pair.

## 4. The asymmetric K11--K12 pair

Fix T0 and a K12 track Ti. For each q in T0, apply the same vertex-level count to Ti union {q}, a 13-set:
- if q has an H-neighbor in Ti, its other eleven edges into Ti contain each non-target color once;
- if q has no H-neighbor in Ti, its twelve edges into Ti contain one repeated non-target color.

Define P0i to consist of the H-edges plus these repeated-color edges. Every vertex of T0 has exactly one incident P0i edge, so P0i has exactly 11 edges and saturates T0. **Do not assume P0i is a matching on the T_i side**; the 13-set argument is asymmetric for a K11--K12 pair.

For every C, its bipartite graph between T0 and Ti satisfies Hall's condition on the T0 side. Indeed, if S subset T0 has size k>=1 and |N_C(S) intersect Ti|<=k-1, then at least 12-(k-1)=13-k vertices of Ti avoid S. Choosing 13-k of them with S gives a C-independent 13-set, contradiction. Hence each C has a matching saturating T0, but it need not be the set of C-edges outside P0i.

## 5. What this adds to the remaining Q32 attack

For the three K12--K12 pairs, any admissible exact completion must simultaneously provide:
1. a canonical residual perfect matching P_ij extending the target-color H-matching;
2. eleven other perfect matchings M_C, one for each non-target color;
3. at least three H-edges and at least three repeated-color edges in each P_ij;
4. for every color C, the surplus edges of C on the pair are exactly the P_ij edges colored C.

Thus the cross-track completion is not an arbitrary collection of pairwise color counts. It is three coupled 1-factorizations, whose residual factors contain the target-color matchings and whose factor labels are constrained by the exact Type-I color structures.

This theorem is a structural reduction, not a graph-level contradiction. It does not close the aligned z=0 or z=1 cell. Full-support E408/Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
