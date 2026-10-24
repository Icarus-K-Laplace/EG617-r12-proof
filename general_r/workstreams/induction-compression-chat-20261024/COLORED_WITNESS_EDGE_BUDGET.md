# Colored Witness Edge Budget: Case A and the Fixed-Merge Interface

Status: **PROVED colored-packing inequalities; Case A remains OPEN.**

## Setup

Let \(S_1,\ldots,S_t\) be pairwise disjoint r-sets, each independent in every color in a nonempty required-color set \(C_a\). In the robust Case A, \(C_a=\{i_a\}\) with \(i_a\ne c\). In the fixed-merge hypergraph, \(C_a\) is either a singleton required color or \(\{c,j\}\) when the set is independent in both merge colors.

Every required-color independent r-set dominates all vertices outside it in each required color.

## Theorem J.CP1 — Pairwise colored edge budget

For every pair a != b and every color \(i\in C_a\cup C_b\), there are at least r color-i edges between \(S_a\) and \(S_b\).

If \(i\in C_a\cap C_b\), the color-i bipartite graph between \(S_a,S_b\) contains a **perfect matching**.

### Proof

If \(i\in C_a\), then \(S_a\) is independent in color i. Every vertex of \(S_b\) outside \(S_a\) must have at least one color-i edge into \(S_a\), giving at least r distinct edges. If also \(i\in C_b\), then both sides are independent r-sets in a graph with independence number at most r. In the induced graph on \(S_a\cup S_b\), all color-i edges run between the two sides. Its independence number is at most r, so its bipartite vertex-cover number is at least r; by König's theorem there is a matching of size r, hence a perfect matching.

Edges belonging to different unordered block pairs \((S_a,S_b)\) are disjoint edge sets, so these lower bounds can be summed across block pairs without double charging.

## Theorem J.CP2 — Global per-color bound for a disjoint packing

Let \(t_i=|\{a:i\in C_a\}|\). Since every pair with at least one endpoint block requiring color i costs at least r distinct color-i edges, and each vertex outside the packed union needs a color-i edge into every block requiring i,

\[
\boxed{
e(G_i)\ge
r\left[\binom{t_i}{2}+t_i(t-t_i)\right]
+t_i(N-tr),
}
\]

where \(N=r^2+1\). The first term counts edges between packed blocks; the second counts edges from the \(N-tr\) outside vertices to the packed blocks. These edge sets are disjoint.

This inequality is valid for both robust packing and fixed-merge packing, using the corresponding required-color sets \(C_a\).

## Three-set color-pattern audit

For Case A with \(t=3\), put \(m_r=r\binom r2\) and \(u=N-3r=r^2+1-3r\). The direct domination/cross-edge lower bounds are:

| Witness-color pattern | Required color-i edge lower bound | Small-r value | Universal full-graph floor |
|---|---:|---:|---:|
| All three labels equal i | \(3r+3u=3r^2-6r+3\) | r=3: 12; r=4: 27; r=5: 48 | \(m_r+2r-1\): 14, 31, 59 |
| Exactly two labels i, one j | \(e_i\ge3r+2u=2r^2-3r+2\) | r=3: 11; r=4: 22; r=5: 37 | \(m_r+2r-1\): 14, 31, 59 |
| Exactly two labels i, one j | \(e_j\ge2r+u=r^2-r+1\) | r=3: 7; r=4: 13; r=5: 21 | \(m_r+2r-1\): 14, 31, 59 |
| All three labels distinct | Each required color \(i\): \(2r+u=r^2-r+1\) | r=3: 7; r=4: 13; r=5: 21 | \(m_r+2r-1\): 14, 31, 59 |

The universal floor follows from the K-line result \(e_i=m_r+r+a_i\) and \(a_i\ge r-1\). The displayed Case A inequalities are all weaker than this floor for r=3,4,5; asymptotically they are also too small to contradict the \(m_r=\Theta(r^3)\) baseline. Thus the three-set packing bounds alone do not close Case A.

## Same-color strengthening

When \(i_a=i_b=i\), the pairwise perfect matching is stronger than merely requiring r edges. The matching edge set is unique to that pair of disjoint blocks, so it is safe to count at least r distinct color-i edges for each same-label pair. For different labels, each of the two designated colors contributes at least r edges, again on disjoint edge-color classes.

## Exact open interface

The packing constraints do not by themselves imply an affine plane or any pairwise-intersection-one property. They also do not exceed the full color-edge budgets. A completion must add a genuinely graph-level constraint coupling the packed sets to the rest of the coloring, or prove that the residual/private-witness Case B is forced.
