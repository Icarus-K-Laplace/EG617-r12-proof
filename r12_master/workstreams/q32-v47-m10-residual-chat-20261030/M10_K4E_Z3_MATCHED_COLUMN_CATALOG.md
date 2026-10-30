# K4-e, Z=3 matched-column residual-map catalog

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL local structural catalog; no Z=3 or Q32 closure.**

## 1. Frozen 4+6, K4-e, Z=3 contract

Let S be the four-block K4-e component and T the six-block component. The exact ledger gives:
- all 24 S-T pairs have exactly five H-edges;
- Y_S=0, so each residual vertex has exactly one neighbor in every small block;
- the heavy graph inside T is a matching of size Z-1=2;
- the four endpoints M of this matching have y_j=0, while the two unmatched outer blocks have y_j=1;
- e(H[R])=6, Delta(H[R])<=2, alpha(H[R])<=4, and clique-cover number at most four.

The small-side light graph is K4-e and is connected. The four zero-slack outer blocks M induce K4 minus a perfect matching, namely C4, which is also connected. After matching alignment, the zero-slack map-alignment lemma therefore gives:
- one common small-side residual map F:R->[4] on all four blocks of S;
- one common outer residual map G:R->[4] on the four blocks in M.

The six possible residual graphs and their clique-fiber maps are exactly those in the tightened residual catalog.

## 2. Necessary cell test

Fix one matched outer block E in M. Each of the four small blocks Q_i has exactly five edges to E: a unique perfect matching plus one off-matching edge. Normalize E by the inverse of that matching. For each independent pair {r,s} in R, the two-by-two graph on the labels unused by F(r),F(s) and G(r),G(s) must contain a matching of size two; otherwise those four block vertices and r,s contain an independent five-set. For each independent triple in R, the two labels left unused in the two blocks must be adjacent.

The companion verifier enumerates every clique-fiber map F and G, every p in S4, and all independent pairs and triples. It is a necessary-condition catalog: the aligned free-extra states may still fail a larger independent-set test.

## 3. Exact six-type cell catalog

| H[R] type | F maps | Compatible ordered (F,G) pairs | Pair/triple cell states | Full aligned | Full nonaligned | F-empty/G-full | F-full/G-empty | Both empty, same partition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2C3 union K1 | 168 | 17,856 | 70,848 | 3,456 | 6,912 | 3,456 | 3,456 | 576 |
| C4 union P3 | 96 | 4,608 | 29,952 | 2,304 | 2,304 | 0 | 0 | 0 |
| C3 union P4 | 168 | 15,552 | 67,392 | 3,456 | 5,760 | 2,880 | 2,880 | 576 |
| P7 | 96 | 5,760 | 31,104 | 2,304 | 3,456 | 0 | 0 | 0 |
| C6 union K1 | 48 | 1,152 | 13,824 | 1,152 | 0 | 0 | 0 | 0 |
| C5 union P2 | 120 | 8,640 | 40,320 | 2,880 | 5,760 | 0 | 0 | 0 |

The sorted nonempty fiber profiles are:
- 2C3 union K1: (3,3,1,0) and (3,2,1,1);
- C4 union P3: (2,2,2,1);
- C3 union P4: (3,2,2,0), (3,2,1,1), and (2,2,2,1);
- P7, C6 union K1, C5 union P2: (2,2,2,1).

There are no compatible pairs with two empty maps and different residual partitions.

## 4. Degree-cap elimination in a matched outer column

For E in M, its internal heavy degree is one and y_E=0. Its four vertices have degree sum exactly 48, so every vertex has degree 12. If m_t=|G^{-1}(t)|, alpha_E is the endpoint label of its internal heavy edge, and c_E(t) counts the four cross-extra edges ending at label t, then
\[
c_E(t)=3-m_t-\mathbf 1_{\{t=\alpha_E\}}\le3.
\]

Consequently:
1. **Full/full nonaligned is impossible.** The cell catalog forces the same unique matching and same extra-edge target in all four small rows, giving c_E(t)=4.
2. **F-full/G-empty is impossible.** Every cross-extra edge ends at the empty outer label, again giving c_E(t)=4.

Thus, for each matched outer column, only these cell regimes remain:
- F and G both full and aligned;
- F empty, G full;
- F and G both empty with the same residual partition.

The second and third regimes occur only for residual graphs 2C3 union K1 and C3 union P4. The first regime is the only possibility for the other four residual types.

## 5. Exact endpoint form of the surviving empty-map regimes

If F is empty and G is full, every compatible cell has exactly two matching choices. Their relative permutation is a transposition whose support contains the empty small-side label z, and both forced extra edges start at z. If two light-adjacent columns or rows were to use different matching choices, the 4,5,5 switch theorem would require the two extra endpoints to occupy the two moved labels, whereas both catalogued cell extras start at z. This is the key coupling to the remaining grid.

If F and G are both empty with the same partition, there is one aligned matching p0 with 12 pair/triple-compatible extra-edge choices, plus three switches p0 composed with tau_k, one for each occupied label k. Each switch has its extra edge joining the two empty-label vertices in the original block labels (equivalently, normalized extra edge (z,k)).

## 6. Scope firewall

This result identifies the common residual maps on the four small blocks and four zero-slack outer blocks, enumerates all necessary matched-column cell regimes, and removes two regimes by exact outer degree caps. It does not yet couple the two y_j=1 unmatched outer blocks, the six-column matching matrix, all residual incidences, or the source-color edge ownership. Therefore K4-e, Z=3 remains OPEN; full-support m=10 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.

## 7. Exact unmatched-block residual-incidence interface

Because the K4-e, Z=3 branch has s_R=0, every residual vertex satisfies
\[
d_R(r)+b_r=2,\qquad b_r:=\sum_i(|N(r)\cap Q_i|-1).
\]
Thus b_r=2-d_R(r). The six residual types determine the exceptional vertices of the two unmatched outer blocks:
- 2C3 union K1 and C6 union K1: the isolated vertex has b_r=2, so it is the double-neighbor vertex in both unmatched blocks;
- C4 union P3, C3 union P4, P7, and C5 union P2: the two degree-one path endpoints each have b_r=1, so one endpoint is exceptional in each unmatched block.

For one unmatched block U, y_U=1 means there is exactly one exceptional residual vertex e with two distinct neighbors a,b in U; every other r has a unique neighbor g(r) in U. Let
\[
r_U(t)=|\{r\ne e:g(r)=t\}|+\mathbf1_{\{t=a\}}+\mathbf1_{\{t=b\}}.
\]
The block has no internal heavy pair, all nine base matching incidences, four cross-extra edges, and eight residual incidences. Its degree sum is exactly 48, so every vertex has degree 12 and
\[
\boxed{c_U(t)=3-r_U(t)\ge0.}
\tag{7.1}
\]

Now fix any small block Q_i and any residual vertex r nonadjacent to e in R. Since the small-side residual map has zero slack, e and r have distinct neighbors in Q_i; the two other vertices of Q_i are available. In U the vertices available to both e and r are
\[
V_{e,r}=[4]\setminus(\{a,b\}\cup\{g(r)\}).
\]
The two available Q_i vertices together with e,r and a vertex of V_{e,r} would form an independent five-set unless the cross-pair graph blocks it. In particular:
- if |V_{e,r}|=1, its unique vertex must be adjacent to at least one of the two available Q_i vertices;
- if |V_{e,r}|=2, the induced bipartite graph between the two available Q_i vertices and V_{e,r} must contain a perfect matching;
- if V_{e,r} is empty, this pair gives no further constraint.

A degree-only prefilter enumerating every clique-fiber map g on R minus e and every unordered pair {a,b}, retaining only r_U(t)<=3, gives the following counts (per exceptional vertex):

| H[R] | Exceptional vertex type | g maps | (g,{a,b}) choices | Pass r_U(t)<=3 |
|---|---|---:|---:|---:|
| 2C3 union K1 | isolated vertex | 420 | 2,520 | 1,884 |
| C4 union P3 | either P3 endpoint | 192 | 1,152 | 1,152 |
| C3 union P4 | either P4 endpoint | 216 | 1,296 | 1,080 |
| P7 | either endpoint | 168 | 1,008 | 1,008 |
| C6 union K1 | isolated vertex | 264 | 1,584 | 1,584 |
| C5 union P2 | either P2 endpoint | 120 | 720 | 720 |

This is only the degree-only prefilter. It does not yet impose all pair/triple constraints jointly across the four small rows, the matching/extra-edge compatibility between those rows, or the coupling between the two unmatched blocks. The two unmatched columns are now expressed as a finite exceptional-vertex incidence CSP.
