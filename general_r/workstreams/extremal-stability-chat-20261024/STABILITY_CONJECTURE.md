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


## F-003 update: neighborhood-sensitive stability

The new-point data now yields a quantitative theorem beyond scalar slack accounting. For each color \(i\) with \(s_i\le\binom r2\), its incident set \(A_i=N_i(x)\) must satisfy
\[
|A_i|\ge\max\!\left\{3,\left\lceil\sqrt{r/1024}\right\rceil\right\}.
\]
The proof derives a \(T_{r-1}\)-deficit upper bound \(t\le r(|A_i|-1)\), then compares Füredi's cross-defect budget with the missing-edge cost needed to block all clique-completion transversals.

This still falls short of \(|A_i|=r\), and it does not force exact orthogonal partitions. The arbitrary-counterexample reconstruction conjecture remains OPEN.


## F-004 — neighborhood-sensitive stability

A weighted transversal lemma gives
1 <= sum_j |A∩V_j|/|V_j| + sum_{j<k} b_jk/(|V_j||V_k|)
whenever A hits every K_q in a graph with a nonempty q-part partition.

Applying it to the Füredi partition of H_i gives, for s_i<r^2/4,
d_i >= r-2sqrt(s_i)-2s_i/(r-2sqrt(s_i)).
In particular s_i<=r^2/100 forces d_i>=31r/40. For d_i<r, inversion gives s_i>=ceil(U_r(d_i)^2), with U_r(d)=(2r-d-sqrt(d^2-2rd+2r^2))/2.

The medium-slack extension also proves that the two smallest-slack colors have d_i>=max(2,ceil sqrt(r/1600)).

The scalar integer program remains feasible at d_i=r and s_i=binom(r,2) for all colors. Thus the next stability theorem must exploit simultaneous cross-color incidence; summing one-color inequalities cannot prove nonexistence.

Status: joint local rigidity PROVED_CONDITIONAL; full skeleton reconstruction OPEN.
