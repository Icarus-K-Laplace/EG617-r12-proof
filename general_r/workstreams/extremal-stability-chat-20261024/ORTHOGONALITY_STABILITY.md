# Orthogonality Stability — F-002

## 1. Quantitative matrix statement

For a hypothetical counterexample and the two smallest-slack colors \(i,j\), Füredi's lemma gives partitions \(\mathcal P=(P_a)_{a=1}^r\) and \(\mathcal Q=(Q_b)_{b=1}^r\) of the \(r^2\) old vertices. The intersection matrix \(M_{ab}=|P_a\cap Q_b|\) satisfies
\[
\sum_{a,b}\binom{M_{ab}}2\le s_i+s_j\le r(r-1).
\]
Every cell of size at least two spends at least one unit of the collision budget. The part-size variance bounds are
\[
\sum_a(|P_a|-r)^2\le4s_i\le2r^2,\qquad
\sum_b(|Q_b|-r)^2\le4s_j\le2r^2.
\]

This bounds large intersections but does not force most entries to equal one. The even-\(r\) matrix with entries two on an \(r/2\)-regular bipartite support and zero elsewhere has row and column sums \(r\), collision budget \(r^2/2\), and no ones. Hence collision counting alone is insufficient.

## 2. Exact orthogonality under a low-slack hypothesis

Suppose two colors \(i,j\) satisfy \(s_i,s_j\le r-2\). Since \(H_i,H_j\) are \(K_{r+1}\)-free and
\[
e(H_i)\ge T_r(r^2)-r+2,
\]
Brouwer's theorem implies that each is \(r\)-partite (here \(r^2\ge2r+1\) and \(\lfloor r^2/r\rfloor=r\)). Neither partition can have an empty part, since then \(H_i\) would be \((r-1)\)-partite and have at most \(T_{r-1}(r^2)\) edges, far below this threshold.

Taking complements gives partitions of \(V\) into \(r\) monochromatic cliques of colors \(i\) and \(j\). Their blocks intersect in at most one vertex: two common vertices would give an edge with both colors. Therefore every block has size at most \(r\); as there are \(r\) blocks covering \(r^2\) vertices, every block has size exactly \(r\). The intersection matrix is the all-ones matrix.

**Conclusion:** two low-slack colors force an exact orthogonal pair of \(r\)-clique partitions.

This is only a pair, not an \(r\)-net. The affine-skeleton nonextension theorem cannot be invoked until enough additional partitions are reconstructed.

## 3. Why this does not settle the general case

The slack identity does not guarantee two colors with \(s_i\le r-2\). In the affine-skeleton sharp family, \(s_i\) is exactly the number of leftover-class \(Q\)-edges assigned to color \(i\). Distributing those edges nearly evenly gives \(s_i\ge r-1\) for every color, while the exact clique partitions still exist.

Thus:
- low-slack \(\Rightarrow\) exact orthogonal pair is proved;
- high slack \(\not\Rightarrow\) absence of clique partitions;
- the missing information is how the new-point neighborhoods interact with the near-partition defects.

## Status

- Quantitative orthogonality bound: PROVED_CONDITIONAL on Füredi's lemma.
- Low-slack exact orthogonal-pair theorem: PROVED_CONDITIONAL on Brouwer's theorem.
- Collision-budget-only stability to the all-ones matrix: DISPROVED by the explicit abstract matrix above.
- Full skeleton reconstruction: OPEN.
