# Quantitative Overlap of Private Witnesses

Status: **PROVED in the matching-number-two case**.

## Setup

Let X be the union of a maximum matching of size two in the robust shell hypergraph H_{-c}. Then |X|=2r, the transversal number is 2r, and every v in X has a private witness T_v of size r with T_v intersect X={v}. Put R=V minus X, so |R|=(r-1)^2. Write Q_v=T_v minus {v}; each Q_v is an (r-1)-subset of R.

## Theorem J.O1 — Dense witness-overlap graph

Define the overlap graph O on vertex set X by joining v,w when Q_v intersect Q_w is nonempty.

Then

\[
\boxed{\alpha(O)\le2,\qquad e(O)\ge r(r-1).}
\]

### Proof

A set of three pairwise nonadjacent vertices in O would give three pairwise disjoint private witnesses T_v, contradicting that the matching number of H_{-c} is two. Thus alpha(O)<=2.

Equivalently, the complement of O is triangle-free. By Mantel's theorem it has at most floor((2r)^2/4)=r^2 edges. Hence

\[
e(O)\ge\binom{2r}{2}-r^2=r(r-1).
\]

All intersections occur in R, because T_v intersect X={v} and T_w intersect X={w} for distinct v,w.

## Corollary J.O2 — A common residual hub exists

Count incidences between the 2r witnesses and R. Every Q_v has size r-1, so the total number of incidences is 2r(r-1), while |R|=(r-1)^2. If every point of R belonged to at most two Q_v, there would be at most 2(r-1)^2 incidences, a contradiction. Therefore

\[
\boxed{\exists z\in R:\ z\in Q_v\text{ for at least three distinct }v\in X.}
\]

This hub conclusion uses only the witness sizes and the size of R; the dense overlap-graph bound additionally uses matching number two.

## Extremal overlap-graph profile

Equality e(O)=r(r-1) can occur only if the disjointness graph is a complete balanced bipartite graph K_{r,r}. Equivalently, O is the disjoint union of two cliques K_r and K_r: witnesses within each of two groups pairwise intersect, while every witness from one group is disjoint from every witness in the other group.

This is a graph-theoretic equality profile, not a claim that it is realizable by the independent-set witnesses of an EG617 coloring.

## What this does not prove

The theorem forces many witness overlaps and a residual point shared by at least three witnesses. It does not show that the shared point has the same witness color, that intersections have size one, or that witness sets form affine lines. Those upgrades remain open.
