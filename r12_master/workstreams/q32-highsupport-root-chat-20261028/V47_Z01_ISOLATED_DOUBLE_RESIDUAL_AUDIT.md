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
The H-part of \(N_s\) is a \(K_3\), the H-part of \(N_t\) is a \(K_4\), and the gadget supplies six H-H edges: three from \(x_C\) to \(N_t\setminus\{y\}\), plus one edge from \(x_C\) or \(y\) to each of the three H-vertices of \(N_s\). This \(g_C=3\) source geometry is closed by the balanced-coloring contradiction in Section 3.3.

### 3.3 Balanced-coloring contradiction closes the exceptional \(x_C\in H,y\in H\) branch

In the exceptional \(x_C\in H,y\in H\) branch of Section 3.2, \(N_t\) is single-outside and its four H-vertices form a transversal \(K_4\). The three H-vertices of \(N_t\setminus\{y\}\) occupy the three target tracks other than the track containing \(y\). The gadget makes \(x_C\) C-adjacent to all three, so \(x_C\) must lie in the same target track as \(y\); otherwise one of these C-edges would lie inside a target-color clique. Write this common track as \(T_k\).

The H-part of \(N_s\) is a C-colored \(K_3\), so its three vertices occupy three distinct target tracks. Each of those vertices has a C-colored gadget edge from either \(x_C\) or \(y\). Neither \(x_C\) nor \(y\) can send such an edge to a vertex in \(T_k\), since that would be a C-edge inside \(T_k\). Therefore the three H-vertices of \(N_s\) occupy exactly the three tracks other than \(T_k\).

**Case 1: \(T_k=T_0\).** Both \(x_C\) and \(y\) lie in \(T_0\). Each already has three C-neighbors in H among the H-part of \(N_t\): for \(x_C\), these are the three gadget neighbors in \(N_t\setminus\{y\}\); for \(y\), these are the three internal neighbors in \(N_t\). Pointwise saturation caps each T0 color-degree at four, so each center can receive at most one additional C-edge. But the three H-vertices of \(N_s\), which lie one each in \(T_1,T_2,T_3\), require three distinct gadget edges from \(x_C\) or \(y\). These three edges cannot be assigned to two centers with capacity one each. Contradiction.

**Case 2: \(T_k=T_i\) for some \(i\in\{1,2,3\}\).** Let \(T_j,T_\ell\) be the other two large tracks. The H-parts of both \(N_t\) and \(N_s\) contain one vertex in each of \(T_j,T_\ell\). Both \(x_C\) and \(y\) already have a C-edge into \(T_j\) and a C-edge into \(T_\ell\), namely their edges to the corresponding vertices of \(N_t\). But every vertex of a large track has exactly one H-neighbor into each other large track. Thus for \(u\in\{x_C,y\}\), the 13-set \(T_j\cup\{u\}\) has exactly one H-colored edge from \(u\) to \(T_j\); the other eleven edges must contain each non-target color exactly once. In particular, \(u\) cannot have a second C-edge into \(T_j\), and similarly cannot have a second C-edge into \(T_\ell\). Yet the H-vertices of \(N_s\) in \(T_j\) and \(T_\ell\) each require a C-colored gadget edge from \(x_C\) or \(y\). Contradiction.

Both cases are impossible. Therefore the source-correct isolated-double placement with \(x_C\in H,y\in H\) is **CLOSED** in the aligned z=0,1 cell. The other isolated-double two-K4 subcases in Sections 3.1 and 3.2 with \(y\in O\) remain open subject to the T0 cap and source star constraints.

## 4. Exact count of the two-\(K_4\) local relaxation with T0 degree cap

For the two-\(K_4\) subcases above, each \(K_4\) is transversal across \(T_1,T_2,T_3,T_0\). There are eight labeled unordered two-\(K_4\) bases (choose which of the two vertices in each track belongs to the first \(K_4\), modulo swapping the two \(K_4\)s). Between the two \(K_4\)s there are 12 allowed cross-part edges; the four same-track pairs are forbidden because each track is a target-color clique.

Each T0 residual vertex has baseline C-degree three. Pointwise balanced-coloring saturation caps its C-degree at four, so at most one extra edge may be incident to each of the two T0 residual vertices. The companion verifier enumerates all subsets of the 12 cross-K4 edges of size \(g_C\le3\) subject to this cap. The six edges not incident to T0 are unrestricted; each of the two T0 vertices has three possible cross-K4 edges, from which at most one may be chosen.

The exact counts in this T0-capped relaxation are
\[
8,\quad 96,\quad 480,\quad 1312
\]
for \(g_C=0,1,2,3\), respectively. For each base, the numbers of allowed extra sets are \(1,12,60,164\). For \(g_C\le3\), the disjoint two-\(K_4\) base is unique, so these counts do not double-count graphs.

The source-derived extra-edge set is stricter still: in the \(x_C\in O\) case, extras form a star centered at \(y\); in the \(x_C\in H,y\in O\) case, extras form a star centered at \(x_C\). If that star center lies in T0, the pointwise cap forces \(g_C\le1\). If the center lies in a large track, up to three star edges may survive, subject to the detailed source incidence restrictions.

These are counts of a necessary relaxation, **not** counts of source-realizable gadget completions. The companion verifier is verify_v47_z01_isolated_double_residual_graphs.py.

## 5. Correct scope of the seven-vertex holonomy theorem

The seven-vertex catalog and its four holonomy classes apply only when all ten isolated components are single-outside. In the isolated-double branch, the eight-vertex accounting above replaces it.

The global low-gap conclusion \(g_C\le1\Rightarrow\) aligned large-track matching composition remains available, but its proof must use the global 69/70 near-Turan classification or the two-\(K_4\) case split—not an unconditional application of the seven-vertex holonomy catalog. The exceptional isolated-double case with \(x_C\in H,y\in H\) has \(g_C=3\), so it does not affect that low-gap implication.

No Q32 completion or UNSAT certificate is claimed. E408/Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
