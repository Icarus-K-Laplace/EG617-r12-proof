# Compression-or-Geometry: Current Theorem and Exact Gap

Status: **Compression-or-hypergraph-structure is proved; a conditional low-slack interface is now proved; full finite-geometry dichotomy remains OPEN.**

## 1. Exact alternatives

For a hypothetical counterexample to P(r), let I_i be the family of independent r-sets in color i.

For each eliminated color c:

- If the union of I_i over i != c has a transversal X of size at most 2r-1, then the robust compression criterion yields a counterexample to P(r-1).
- If not, its transversal number is at least 2r. The Noncompressible-Shell Theorem gives either three pairwise disjoint independent-set witnesses with forced colored cross-edges, or a tight 2r-point transversal in which every point has a private witness.

For a fixed merge c -> j, replace the hypergraph by

\[
\mathcal H_{c,j}=
\left(\bigcup_{i\notin\{c,j\}}\mathcal I_i\right)
\cup(\mathcal I_c\cap\mathcal I_j).
\]

A transversal of size 2r-1 is exactly a successful fixed-merge shell. If none exists, the same packing/tight-transversal alternative applies.

## 2. New conditional bridge from tight witnesses to low-slack blocks

Suppose the matching-number-two case holds, X is its 2r-point minimum transversal, x_0 in X, and a color i != c has local slack 1<=s_i(x_0)<=r-2 on W=V minus {x_0}. Let P_1,...,P_r be the low-slack color-i clique blocks and Y=X minus {x_0}.

The set Y hits every independent r-set of G_i[W]. For any private witness T_v of color i with v in Y intersect P_a, T_v is an independent transversal of the P-blocks and its other r-1 points lie in the residual parts B_b=P_b minus Y. Every u in B_a must have a color-i defect edge to T_v minus {v}; otherwise replacing v by u creates an independent r-set disjoint from Y. Hence |B_a|<=s_i.

If some B_a is empty, all color-i private witnesses are based in that one block. Otherwise every block hosting such a witness contains at least r-s_i points of Y, so the number of witness-hosting blocks is at most floor((2r-1)/(r-s_i)).

Also, when every B_a is nonempty, the color-i defect edges induced on the B_a parts form a graph with no independent transversal and satisfy the weighted blocker inequality from the K-line lemma.

Full proof: TIGHT_TRANSVERSAL_LOW_SLACK_BRIDGE.md. Weighted lemma: see the K branch TRANSVERSAL_BLOCKER_LEMMA.md.

## 3. Why this is still not a full geometry theorem

The bridge is conditional on finding a low-slack color i != c at a vertex x_0 belonging to X. No theorem currently guarantees this alignment. Even when it holds, the witnesses are concentrated in a bounded number of clique blocks, but this does not yet force three directions, a net, or a contradiction.

The hypergraph data alone cannot force affine geometry. The abstract example with two disjoint clusters of all r-subsets still shows that matching/transversal data alone are insufficient.

## 4. Kakeya-bridge requirements

To use

\[
|X|\ge tq-\binom t2,
\]

one must first prove t full size-q blocks lie wholly in X and pairwise intersect in at most one point. The current packing theorem and conditional block concentration do not provide these hypotheses. Three distinct-direction full lines would contradict a 2q-1 shell for q>=3, but no such lines have been extracted.

## 5. Current verdict

- Exact robust compression criterion: PROVED.
- Exact fixed-merge criterion: PROVED.
- No-shell => packing or tight critical transversal: PROVED.
- Tight case => same-color private-witness overlap: PROVED.
- Tight case + aligned low-slack color => witness-block concentration and weighted blocker: PROVED.
- Existence of aligned low-slack color: OPEN.
- No-shell => many line-like blocks: NOT PROVED.
- Kakeya contradiction: NOT AUTHORIZED.
- P(r) => P(r-1): NOT ESTABLISHED.
