# Robust Partition Compatibility — H+I Joint Audit

Date: 2026-10-24  
Status: **QUANTITATIVE MATRIX LEMMA PROVED; ROBUST CONTRADICTION OPEN.**

## 1. Slack forces a pair only at the wrong scale

For $n=r^2+1$, let
$$
s_i=e(G_i)-p_r(n)\ge0,\qquad
\sum_{i=1}^r s_i=\frac{r^2(r-1)}2.
$$
The mean slack is $\binom r2=\Theta(r^2)$. A strict pigeonhole consequence is that at least
$$
r-\left\lfloor\frac{r-2}{2}\right\rfloor
=\left\lceil\frac{r+2}{2}\right\rceil
$$
colors satisfy $s_i\le r^2$.

This is a real pair-existence statement, not an assumption. But it is too weak for asymptotic orthogonality: the recorded Turán-stability edit bound $E_i\le3s_i$ gives only $E_i=O(r^2)$, not $o(r^2)$. The total slack identity cannot guarantee a color with $s_i=o(r^2)$; the balanced slack vector $s_i=\binom r2$ satisfies the identity exactly.

## 2. Intersection-matrix lemma

For a color $i$ with a stability partition $\mathcal P_i=\{A_1,\ldots,A_r\}$, let $F(\mathcal P_i)$ be the union of cliques on its blocks, and let
$$
E_i=|E(G_i)\triangle E(F(\mathcal P_i))|
$$
be the edit count. On $r^2+1$ vertices, the ideal block sizes are $r+1,r,\ldots,r$.

For two colors $i,j$, with blocks $A_a$ and $B_b$, define
$$
M_{ab}=|A_a\cap B_b|.
$$
Every pair in $A_a\cap B_b$ is an edge of both ideal clique unions, but the actual coloring assigns that pair only one color. Thus each such pair contributes at least one disagreement to $E_i+E_j$. Summing disjoint cells gives the exact bound
$$
\boxed{\sum_{a,b}\binom{M_{ab}}2\le E_i+E_j.}
$$
For a pair with $s_i,s_j\le r^2$, the cited stability envelope would give
$$
\sum_{a,b}\binom{M_{ab}}2\le6r^2.
$$
This is the strongest unconditional matrix conclusion obtained in this pass.

For any row whose sum is $r$ or $r+1$, the number of zero cells is at most its sum of $\binom{M_{ab}}2$ terms, and the number of cells at least two is also at most that sum. Therefore
$$
\#\{(a,b):M_{ab}\ne1\}
\le2\sum_{a,b}\binom{M_{ab}}2
\le2(E_i+E_j).
$$
With $E_i+E_j=O(r^2)$ this is only an $O(r^2)$ bound on an $r^2$-cell matrix; it does **not** imply $o(r^2)$ exceptional cells.

## 3. Explicit obstruction to the current stability scale

For even $r$, choose an $r\times r$ zero-one matrix $A$ with every row and column sum $r/2$ and $A_{11}=0$. The nonnegative integer matrix
$$
M=2A+E_{11}
$$
has row and column sums $r$, except the first row and column sums are $r+1$. It is therefore a valid intersection-count matrix for block sizes $r+1,r,\ldots,r$ at the level of margins. It has approximately $r^2/2$ cells equal to $2$, approximately $r^2/2$ cells equal to $0$, and
$$
\sum_{a,b}\binom{M_{ab}}2=\frac{r^2}{2}.
$$
Thus an $O(r^2)$ collision-mass bound is compatible with a matrix having $\Theta(r^2)$ non-orthogonal cells. This is a matrix-level obstruction only, not a claim that such a matrix comes from a valid Problem-617 coloring.

For equal-size partitions of $r^2$ points, orthogonality means the **all-ones matrix**, not a permutation matrix. On $r^2+1$ points, the margins $r+1,r,\ldots,r$ make an all-ones matrix impossible. The affine-plane nonextension route needs a sufficiently accurate restriction to an $r^2$-point subset, not merely a generic matrix approximation.

## 4. Why the row-signature budget has not closed the gap

The established edge statistic obeys
$$
\operatorname{avg}_{xy}b(xy)\le3(r-1)-\frac{3P}{nr^2}.
$$
Markov's inequality says that for $K>3$, at most a $3/K$ fraction of edges can have $b(xy)>Kr$ (using the weaker $3(r-1)$ bound). This is an $O(r)$ typical-edge collision bound, but no proved inequality currently converts it into an $o(r^2)$ edit bound for the two stability partitions.

The obstacle is quantitative: even $O(r^2)$ repeated intersection pairs can account for only $O(r^3)$ edge-extension incidences at scale $r$; the global budget is $O(r^5)$. Hence this crude aggregation is far too weak to contradict the non-rainbow budget.

## 5. Requested dichotomy: status

The desired dichotomy
- a pair with sufficiently small slack and hence $o(r^2)$ partition error, or
- a high-slack distribution violating a verified global inequality,

is **not proved**. The current scalar constraints allow the balanced slack vector $s_i=\binom r2$ and do not exclude it: the variance lower bound
$$
V\ge\frac4n\sum_i\left(s_i-\binom r2\right)^2
$$
then gives only $V\ge0$, consistent with the existing upper bound $V\le nr(r-1)^2$.

The missing theorem must either sharpen the global moment inequality to force slack concentration, or relate the row-signature collision sum directly to the simultaneous partition edit errors at a scale smaller than $r^2$. No such link is certified here.
