# Compression-or-Geometry: Current Theorem and Exact Gap

Status: **Compression-or-hypergraph-structure is proved; compression-or-finite-geometry is OPEN**.

## 1. Exact alternatives

For a hypothetical counterexample to P(r), let I_i be the family of independent r-sets in color i.

For each eliminated color c:

- If the union of I_i over i != c has a transversal X of size at most 2r-1, then the robust compression criterion yields a counterexample to P(r-1).
- If not, its transversal number is at least 2r. The Noncompressible-Shell Theorem then gives either three pairwise disjoint independent-set witnesses with forced colored cross-edges, or a tight 2r-point transversal in which every point has a private witness.

For each fixed merge c -> j, replace the hypergraph by

\[
\mathcal H_{c,j}=
\left(\bigcup_{i\notin\{c,j\}}\mathcal I_i\right)
\cup(\mathcal I_c\cap\mathcal I_j).
\]

A transversal of size 2r-1 is exactly a successful fixed-merge shell. If none exists, the same packing/tight-transversal alternative applies.

## 2. Why this is not yet geometric rigidity

The hypergraph implication uses only uniformity:

\[
\tau(\mathcal H)\le r\,\nu(\mathcal H).
\]

It forces a matching of size at least two, and if the matching number is exactly two, it forces a minimum transversal of size exactly 2r with private witnesses. The color-graph domination lemma adds the cross-edge constraints stated in NONCOMPRESSIBLE_SHELL_THEOREM.md.

But uniform-hypergraph data alone cannot force affine geometry. For example, on two disjoint sets A,B each of size 2r-1, take as hyperedges all r-subsets of A and all r-subsets of B. This abstract r-uniform hypergraph has matching number 2 and transversal number 2r: within each cluster every two r-subsets intersect, and each cluster requires r vertices to hit all its r-subsets. It has no affine-direction interpretation.

This is **not** claimed to be realizable as the independent-set hypergraphs of a counterexample coloring. It is an audit example showing that tau/nu alone cannot supply the missing geometry.

## 3. Exact Kakeya-bridge requirements

To use the elementary inequality

\[
|X|\ge tq-\binom t2,
\]

one must already have t subsets of size q, each wholly contained in X, with every pair intersecting in at most one point. For an affine-plane interpretation, these must be full lines in t distinct directions. The present compression theorem yields disjoint independent r-sets, not such lines, so the Kakeya inequality is not yet applicable.

In an affine plane, three full lines from three distinct directions already require at least 3q-3 points. For q>=3,

\[
3q-3>2q-1.
\]

Thus a future bridge need only extract three genuinely distinct line-like directions that the shell must fully contain; it need not extract all q+1 directions. The extraction and pairwise-intersection hypotheses are currently OPEN.

## 4. Current verdict

- Exact robust compression criterion: PROVED.
- Exact fixed-merge criterion: PROVED.
- No-shell => packing or tight critical transversal: PROVED.
- No-shell => many line-like blocks: NOT PROVED.
- Kakeya contradiction: NOT AUTHORIZED until full-line blocks and their intersection hypotheses are derived.
- P(r) => P(r-1): NOT ESTABLISHED.

The correct next theorem is a graph-specific upgrade from the packing/private-witness certificate to either a shell or a family of blocks with proved intersection constraints.