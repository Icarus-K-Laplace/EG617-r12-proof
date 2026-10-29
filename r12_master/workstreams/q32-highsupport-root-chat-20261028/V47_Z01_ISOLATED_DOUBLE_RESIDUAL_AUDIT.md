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
The H-part of \(N_s\) is a \(K_3\), the H-part of \(N_t\) is a \(K_4\), and the gadget supplies six H-H edges: three from \(x_C\) to \(N_t\setminus\{y\}\), plus one edge from \(x_C\) or \(y\) to each of the three H-vertices of \(N_s\). This \(g_C=3\) source geometry must be handled separately; it is not covered by the two-\(K_4\) baseline count alone.

## 4. Exact count of the two-\(K_4\) local relaxation

For the two-\(K_4\) subcases above, each \(K_4\) is transversal across \(T_1,T_2,T_3,T_0\). There are eight labeled two-\(K_4\) bases (choose which of the two vertices in each track belongs to the first \(K_4\), modulo swapping the two \(K_4\)s). Between the two \(K_4\)s there are 12 allowed cross-part edges; the four same-track pairs are forbidden because each track is a target-color clique.

The source-derived extra-edge set is more restricted (a star centered at \(y\) or \(x_C\)), but the broader pairwise-matching relaxation allows any \(g_C\)-subset of those 12 edges. Each resulting graph has \(\alpha\le2\) and respects the pairwise matching restriction. For \(g_C=0,1,2,3\), the exact number of labeled graphs in this relaxation is
\[
8\binom{12}{g_C}=8,\ 96,\ 528,\ 1760.
\]
For \(g_C\le3\), the two-\(K_4\) base is unique, so these counts do not double-count graphs. They are counts of a necessary relaxation, **not** counts of source-realizable gadget completions.

## 5. Correct scope of the seven-vertex holonomy theorem

The seven-vertex catalog and its four holonomy classes apply only when all ten isolated components are single-outside. In the isolated-double branch, the eight-vertex accounting above replaces it.

The global low-gap conclusion \(g_C\le1\Rightarrow\) aligned large-track matching composition remains available, but its proof must use the global 69/70 near-Turan classification or the two-\(K_4\) case split—not an unconditional application of the seven-vertex holonomy catalog. The exceptional isolated-double case with \(x_C\in H,y\in H\) has \(g_C=3\), so it does not affect that low-gap implication.

No Q32 completion or UNSAT certificate is claimed. E408/Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
