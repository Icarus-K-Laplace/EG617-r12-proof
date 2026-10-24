# Stability Conjecture — F-002 update

## KILLED formulation

Edge-edit stability to one fixed standard affine coloring is false. On every affine plane, the leftover parallel class \(Q\) may be colored edge-by-edge arbitrarily while the \(r\) pure classes \(P_i\) preserve balance. This produces \(\Theta(r^3)\) variable edge labels.

## Correct invariant

The target remains recovery of an orthogonal-partition skeleton, not the exact edge coloring of \(Q\).

### Skeleton Stability v2 — counterexample-specific

If a coloring of \(K_{r^2}\) is the restriction of a hypothetical balanced coloring of \(K_{r^2+1}\), then its color graphs and the new-point neighborhoods should jointly force enough near-orthogonal clique partitions to invoke a robust nonextension theorem.

This is still OPEN.

## New quantitative evidence

For a fixed deleted vertex, the color slacks satisfy
\[
s_i\ge0,\qquad \sum_i s_i=r\binom r2.
\]
Taking the two smallest slacks and applying Füredi's partition lemma gives two \(r\)-partitions with
\[
\sum_{a,b}\binom{|P_a\cap Q_b|}{2}\le s_i+s_j\le r(r-1),
\]
and part-size variance at most \(4s_i,4s_j\). The two selected colors both have independence number exactly \(r\).

If two colors have the much stronger condition \(s_i,s_j\le r-2\), Brouwer's theorem yields an exact orthogonal pair. But the slack budget does not guarantee this hypothesis: the arbitrary-leftover affine family can have every \(s_i\ge r-1\).

The collision bound itself is insufficient for matrix stability. For even \(r\), a matrix with entries two on an \(r/2\)-regular bipartite support and zero elsewhere has all row/column sums \(r\) and collision budget \(r^2/2\), yet no entries equal one. This is an abstract block-system obstruction, not a full coloring counterexample.

## Neighborhood-sensitive stability

The missing structure is not just a Turán partition. For each color \(i\), the new-point set \(A_i=N_i(x)\) must hit every \(K_r\) in \(H_i=\overline{G_i}\), equivalently \(H_i[V\setminus A_i]\) is \(K_r\)-free.

A new Brouwer/Kang–Pikhurko reduction proves that any color with \(s_i\le\binom r2\) must have \(|A_i|\ge3\) for \(r\ge4\). The cases \(3\le |A_i|<r\) remain open.

## Status

- Fixed-edge-coloring stability: DISPROVED.
- Quantitative two-color near-partition extraction: PROVED_CONDITIONAL.
- Low-slack exact orthogonal pair: PROVED_CONDITIONAL.
- Neighborhood-sensitive reconstruction: OPEN.
- Robust nonextension and all-large-\(r\) theorem: OPEN.
