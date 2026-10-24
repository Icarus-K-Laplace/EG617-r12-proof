# R12 witness-overlap capacity: exact incidence identity and failed scalar closure

Date: 2026-10-25  
Status: **PROVED_ANALYTIC necessary inequality; scalar contradiction OPEN.**  
Scope: the selected exact-129 K5-component witnesses in E407 Q32 / E408 Q33.

## 1. Frozen family contract

Let \(H\) be the 47-point core with \(\alpha(H)\le4\), \(\delta(H)\ge12\), and \(e(H)=284\). Under the retained exact-129 factor theorem, select five no-S isolated K5 components from each of \(c\) exact-129 non-target colors, where \(c\ge7\) in E407 Q32 and \(c\ge8\) in E408 Q33.

Each selected component has the form \(\{b\}\cup Q_j\), where \(b\in B\) and \(Q_j\subset H\) is an independent 4-set. Within a color the selected \(Q_j\)'s are disjoint; across distinct colors, two selected \(Q\)-sets intersect in at most one vertex by unique edge ownership. Thus the family \(\mathcal Q=\{Q_1,\ldots,Q_m\}\) has
\[
m=5c\in\{35,40,\ldots\},\qquad |Q_i|=4,\qquad |Q_i\cap Q_j|\le1\ (i\ne j).
\]
For the lower-bound calculation below, it suffices to select exactly \(m=35\) or \(m=40\) sets.

## 2. Pairwise witness-crossing lemma

**Lemma.** If \(Q,Q'\) are distinct independent 4-sets in a graph with \(\alpha(H)\le4\) and \(|Q\cap Q'|=s\le1\), then
\[
e_H(Q\setminus Q',Q'\setminus Q)\ge4-s\ge3.
\]

**Proof.** Let \(T=Q\cap Q'\). Every \(x\in Q\setminus Q'\) is nonadjacent to every vertex of \(T\), since \(Q\) is independent. If \(x\) had no neighbour in \(Q'\setminus Q\), then \(x\) would be nonadjacent to all of \(Q'\), and \(Q'\cup\{x\}\) would be an independent 5-set. Hence every vertex of \(Q\setminus Q'\) has at least one neighbour in \(Q'\setminus Q\). Symmetrically every vertex of \(Q'\setminus Q\) has a neighbour in \(Q\setminus Q'\). Both difference sets have size \(4-s\), so the bipartite graph between them has minimum degree at least one and at least \(4-s\) edges. \(\square\)

## 3. Exact edge-load identity

For each \(x\in V(H)\), let
\[
r_x=|\{Q\in\mathcal Q:x\in Q\}|.
\]
Because every selected \(Q\) is independent, an actual edge \(xy\in E(H)\) never has both endpoints in the same \(Q\). Because the family is linear (pairwise intersections at most one), every pair of memberships consisting of one \(Q\) containing \(x\) and one \(Q'\) containing \(y\) corresponds to a distinct pair of witness sets whose crossing graph counts \(xy\).

Therefore the exact double-counting identity is
\[
\sum_{\{Q,Q'\}\subseteq\mathcal Q}
e_H(Q\setminus Q',Q'\setminus Q)
=
\sum_{xy\in E(H)}r_xr_y. \tag{1}
\]
By the crossing lemma,
\[
\boxed{\sum_{xy\in E(H)}r_xr_y
\ge3\binom m2.} \tag{2}
\]
This inequality explicitly counts edge reuse; it does not pretend that the crossing edges for different witness pairs are distinct.

## 4. Why the scalar degree bound is insufficient

Each core vertex belongs to at most one selected component per chosen color, so \(r_x\le c\) after selecting \(c\) exact-129 colors. Also \(\sum_x\epsilon(x)=4\). Since \(d_H(x)=12+\epsilon(x)\),
\[
\begin{aligned}
\sum_{xy\in E(H)}r_xr_y
&\le\frac12\sum_x d_H(x)r_x^2\\
&=6\sum_xr_x^2+\frac12\sum_x\epsilon(x)r_x^2\\
&\le6c\sum_xr_x+\frac12c^2\sum_x\epsilon(x)\\
&=24c^2+\;2c^2=26c^2.
\end{aligned}
\]
Here \(\sum_xr_x=4m=20c\), so the displayed \(26c^2\) bound follows.

For \(c=7\) (\(m=35\)), this gives an upper bound \(1274\), while (2) gives the lower bound \(1785\). This is a contradiction **if** all 35 selected witness sets satisfy the family assumptions and \(r_x\le7\). For \(c=8\) (\(m=40\)), the upper bound is \(1664\), while the lower bound is \(2340\), again a contradiction.

## 5. Exact remaining obstacle

A useful next bound must exploit the labelled shell incidences, not just \(r_x\le8\) and \(d_H(x)\le16\). In particular it must account for:

1. each \(Q\)'s associated B label \(b\) being anticomplete to \(Q\);
2. the template-specific mandatory hits to \(S\) and B rows;
3. the fact that zero-excess vertices have at least one shell neighbour;
4. the degree-12 core neighbourhoods, which give each independent 4-set only \(5+\epsilon(Q)\) duplicate incidences when it dominates the other 43 core vertices;
5. the actual overlap pattern of the five disjoint K5 components within each exact-129 color.

No contradiction is claimed from (1) or (2). This file records a reusable incidence identity and a precise failed scalar closure attempt.
