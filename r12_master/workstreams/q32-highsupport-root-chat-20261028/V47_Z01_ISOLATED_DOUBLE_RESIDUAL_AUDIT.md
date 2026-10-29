# E408 Q32 — isolated-double placement and the missing eight-vertex residual branch

Date: 2026-10-29  
Status: **AUDIT CORRECTION + PROVED_CONDITIONAL residual accounting.** This does not close Q32.

## 1. Why the seven-vertex catalog is not universal

The source-correct Type-I factorization is ten isolated \(K_5\) components plus the 11-vertex gadget \(G_{11}\). The twelve \(K_5\) factors (ten isolated components and two special cliques in \(G_{11}\)) have outside-count profiles:
- \(x_C\in O\): \((2,1^{11})\);
- \(x_C\in H\), two-double: \((2,2,1^{10})\);
- \(x_C\in H\), triple: \((3,1^{11})\).

These profiles do **not** force every isolated component to be single-outside. In particular, HIGH_SUPPORT_NEAR_TURAN.md, Section 3, records a source-correct 69-edge placement with the unique double-outside \(K_5\) among the isolated components. Therefore the earlier seven-vertex residual graph catalog is valid only in the subcase where all ten isolated components are single-outside.

## 2. Exact residual accounting when one isolated component is double-outside

A double-outside isolated \(K_5\) has three H-vertices. None can lie in \(T_0\): an H-vertex there would have only two same-color neighbors in H, contradicting the degree floor \(d_C(v,H)\ge3\). Thus its three H-vertices occupy one each of \(T_1,T_2,T_3\).

When one isolated component is double-outside, the ten isolated components consist of nine single-outside \(K_5\)s and one double-outside \(K_5\). Their H-induced graph is
\[
9K_4\;\dot\cup\;K_3,
\qquad e=9\binom42+\binom32=57.
\]
They use nine vertices of each track in the nine \(K_4\)s, plus one vertex in each large track from the \(K_3\). Hence the remaining H-vertices in \(G_{11}\) have track profile
\[
(|G_{11}\cap T_1|,|G_{11}\cap T_2|,|G_{11}\cap T_3|,|G_{11}\cap T_0|)
=(2,2,2,2).
\]
Write \(J_C=C[H\cap G_{11}]\). Since \(e_C(H)=69+g_C\),
\[
\boxed{|V(J_C)|=8,\quad e(J_C)=69+g_C-57=12+g_C.}
\]
The ten isolated H-components contribute independence number exactly 10; since \(\alpha(C[H])\le12\), one still has \(\alpha(J_C)\le2\). Every \(T_0\)-vertex in \(J_C\) has C-degree at least 3 and every large-track vertex has C-degree at least 2.

This is a different local object from the old seven-vertex graph \((2,2,2,1)\) with \(9+g_C\) edges.

## 3. Source placements and the aligned two-\(K_4\) subcase

### 3.1 \(x_C\in O\), double factor isolated

Both special \(K_5\)s are single-outside. Their H-parts are two disjoint transversal \(K_4\)s partitioning the eight vertices of \(J_C\). Thus \(J_C\) is those two \(K_4\)s plus \(g_C\) extra H-edges. Since \(x_C\in O\), the only gadget edges that can add H-H edges are the \(y-A_0\) edges; if \(y\in H\), these extras are all incident to \(y\). The registered aligned-cell bound gives \(0\le g_C\le3\).

### 3.2 \(x_C\in H\), two-double, exactly one double factor isolated

The other double factor must be one of the two special \(K_5\)s in \(G_{11}\), and the remaining special \(K_5\) is single-outside.

If \(y\in O\), then \(N_t\) is the double-outside special clique and \(N_s\) is single-outside. The three H-vertices of \(N_t\setminus\{y\}\), together with \(x_C\), form a transversal \(K_4\); the H-part of \(N_s\) is a second transversal \(K_4\). So \(J_C\) again contains a disjoint two-\(K_4\) base, with the \(g_C\) extra H-edges supplied by the \(x_C-(N_s\setminus A_0)\) family. They are all incident to \(x_C\). This subcase permits \(0\le g_C\le3\).

If \(y\in H\), then \(N_t\) is single-outside and \(N_s\) is double-outside. Here \(b_s+b_t=3\), and the registered source formula gives
\[
g_C=6-(b_s+b_t)=3.
\]
The H-part of \(N_s\) is a \(K_3\), the H-part of \(N_t\) is a \(K_4\), and the gadget supplies six H-H edges: three from \(x_C\) to \(N_t\setminus\{y\}\), plus one edge from \(x_C\) or \(y\) to each of the three H-vertices of \(N_s\). The T0-centered subcase is excluded in Section 3.3; the large-track-centered subcase remains open.

### 3.3 T0-centered subcase is impossible

In the exceptional \(x_C\in H,y\in H\) branch of Section 3.2, \(N_t\) is single-outside and its four H-vertices form a transversal \(K_4\). The three H-vertices of \(N_t\setminus\{y\}\) occupy the three target tracks other than the track containing \(y\). Since \(x_C\) is C-adjacent to all three, \(x_C\) must lie in the same target track as \(y\); otherwise one of those C-edges would lie inside a target-color clique. Write this common track as \(T_k\).

The H-part of \(N_s\) is a C-colored \(K_3\), so its vertices occupy three distinct target tracks. Each has a C-colored gadget edge from either \(x_C\) or \(y\), and neither center can be in the same target track as that vertex.

If \(T_k=T_0\), both \(x_C,y\in T_0\). Each already has three C-neighbors in H among the H-part of \(N_t\): \(x_C\) via the three gadget edges to \(N_t\setminus\{y\}\), and \(y\) via the three internal edges of \(N_t\). Pointwise saturation caps each T0 color-degree at four, so each center can receive at most one additional C-edge. But the three H-vertices of \(N_s\) lie one each in \(T_1,T_2,T_3\) and require three distinct gadget edges from \(x_C\) or \(y\). Three edges cannot be assigned to two centers with capacity one each. Contradiction.

Thus the exceptional branch cannot have \(x_C,y\in T_0\). If their common track is one of \(T_1,T_2,T_3\), the per-vertex cross-track degree is only one **in total**, not one into each other track. The balanced-coloring argument therefore does not yet exclude that case; it remains OPEN and must not be treated as closed.

Although this large-track-centered graph branch remains open, the placement-sensitive T0 repeat-owner count is determined: the residual profile (2,2,2,2) puts one T0 vertex in the special N_t H-K4 and the other in the special N_s H-K3. The former has three internal C-neighbors plus the x_C gadget edge, so degree four; the latter has two triangle neighbors plus its unique gadget edge, so degree three. Hence t_C=1 in this exceptional branch. This is the global bound proved in V47_T0_POINTWISE_COLOR_SATURATION.md; it does not close the graph branch.

## 4. Exact count of the two-\(K_4\) local relaxation with the global T0 cap

For the two-\(K_4\) subcases above, each \(K_4\) is transversal across \(T_1,T_2,T_3,T_0\). There are eight labeled unordered two-\(K_4\) bases (choose which of the two vertices in each track belongs to the first \(K_4\), modulo swapping the two \(K_4\)s). Between the two \(K_4\)s there are 12 allowed cross-part edges; the four same-track pairs are forbidden because each track is a target-color clique.

The pointwise theorem alone allows one extra edge at each T0 residual vertex, hence up to two T0-incident extras. In these two-K4 source subcases, however, all extra edges form a star centered at y or x_C. A star center lies in one target track, so among the 12 cross-K4 edges it has at most one edge to the opposite K4's T0 vertex (and a center in T0 has no T0--T0 cross edge). Thus source star geometry, not the global pointwise theorem, imposes at most one T0-incident extra edge in total. Among the 12 allowed cross-part edges, six are T0-incident and six join large-track vertices. Choosing \(g_C\) extras with at most one from the T0-incident group gives per-base counts
\[
1,\ 12,\ 51,\ 110
\]
for \(g_C=0,1,2,3\), respectively. Across eight unordered bases, the exact counts are
\[
\boxed{8,\ 96,\ 408,\ 880}.
\]
These supersede the weaker per-T0-vertex-cap counts \(8,96,480,1312\) and the earlier uncapped counts \(8,96,528,1760\). For \(g_C\le3\), the disjoint two-\(K_4\) base is unique, so the counts do not double-count graphs.

The source-derived extra-edge set is stricter still: in the \(x_C\in O\) case, extras form a star centered at \(y\); in the \(x_C\in H,y\in O\) case, extras form a star centered at \(x_C\). If that star center lies in T0, the pointwise cap forces \(g_C\le1\). If the center lies in a large track, up to three star edges may survive, subject to the detailed source incidence restrictions.

These are counts of a necessary relaxation, **not** counts of source-realizable gadget completions. The companion verifier is verify_v47_z01_isolated_double_residual_graphs.py.
## 5. Correct scope of the seven-vertex holonomy theorem

The seven-vertex catalog and its four holonomy classes apply only when all ten isolated components are single-outside. In the isolated-double branch, the eight-vertex accounting above replaces it.

The global low-gap conclusion \(g_C\le1\Rightarrow\) aligned large-track matching composition remains available, but its proof must use the global 69/70 near-Turan classification or the two-\(K_4\) case split—not an unconditional application of the seven-vertex holonomy catalog. The exceptional isolated-double case with \(x_C\in H,y\in H\) has \(g_C=3\), so it does not affect that low-gap implication.

No Q32 completion or UNSAT certificate is claimed. E408/Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
