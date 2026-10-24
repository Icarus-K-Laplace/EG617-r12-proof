# Noncompressible-Shell Theorem

Status: **PROVED hypergraph-structural alternative; geometric rigidity remains OPEN**.

## Setup

Let V have N=r^2+1 vertices and let G_1,...,G_r be the color graphs of a hypothetical counterexample to P(r). For each color i, let I_i be the r-uniform hypergraph of independent r-sets in G_i.

For a fixed eliminated color c, define

\[
\mathcal H_{-c}:=\bigcup_{i\ne c}\mathcal I_i.
\]

A set X of size 2r-1 is a robust compression shell for c precisely when it is a transversal of H_{-c}.

## Theorem J.N1 — No shell forces a packing/critical-transversal alternative

Suppose no robust shell of size 2r-1 exists for this fixed c. Then

\[
\tau(\mathcal H_{-c})\ge 2r.
\]

Let nu be the matching number of H_{-c}. A maximum matching is maximal, so the union of its edges is a transversal; hence tau <= r nu and nu >= 2. Exactly one of the following structural cases applies.

### Case A: At least three disjoint witnesses

There are three pairwise disjoint independent r-sets S_1,S_2,S_3, with designated colors i_a != c.

Each S_a dominates all vertices outside it in color i_a. More generally, for any t pairwise disjoint independent r-sets S_a with designated colors i_a, put R=V minus their union. Then:

- between S_a and S_b, there are at least r edges of color i_a if i_a != i_b, and at least r edges of color i_b as well; if i_a=i_b, there are at least r cross-edges in that common color;
- every vertex of R has at least one edge of color i_a into each S_a, so at least t edges from that vertex into the packed sets.

In compact form, the cross-edges between S_a and S_b number at least

\[
r\,|\{i_a,i_b\}|,
\]

where the set has size one or two. These are genuine colored-incidence constraints, not merely a restatement that a shell was not found.

### Case B: A tight 2r-point transversal with private witnesses

If nu=2, the union X=S_1 union S_2 of any maximum matching has size 2r. Since tau>=2r and X is a transversal, tau=2r and X is a minimum transversal.

Every v in X is essential: X minus {v} is not a transversal. Therefore there exists an independent r-set T_v in some color i_v != c such that

\[
T_v\cap X=\{v\}.
\]

Each T_v has exactly r-1 vertices outside X. The outside set R=V\X has size (r-1)^2.

For r>=3, there are 2r private witnesses but only r-1 possible designated colors. By pigeonhole, at least three witnesses T_u,T_v,T_w have the same designated color i != c. Since the matching number of H_{-c} is exactly two, these three witnesses cannot be pairwise disjoint. Thus at least two of their residual blocks T_z minus {z} intersect at a point of R. This is a genuine same-color overlap forced by noncompressibility, though not yet an affine-line structure.

For any two independent r-sets A,B in the same color i, if |A intersect B|=h, then the bipartite color-i graph between A\B and B\A has minimum degree at least one on both sides, hence at least r-h edges. Indeed, each vertex in B\A is dominated by A, and cannot have a color-i edge to A intersect B because B is independent; the symmetric argument applies to A\B.

## Fixed-merge analogue

For fixed colors c != j, define

\[
\mathcal H_{c,j}:=
\left(\bigcup_{i\notin\{c,j\}}\mathcal I_i\right)
\cup(\mathcal I_c\cap\mathcal I_j).
\]

A shell works for the fixed merge c -> j exactly when it hits every edge of H_{c,j}. If no such shell exists, tau(H_{c,j})>=2r and the same packing-or-tight-transversal alternative holds.

A witness edge of H_{c,j} has a designated required-color set C_a: either a singleton {i}, for an untouched color, or {c,j}, for a set independent in both merged colors. For disjoint witnesses S_a,S_b, every color in C_a union C_b must occur on at least r edges between the two sets. Every outside vertex has at least |C_a|+|C_b| incident edges into S_a union S_b, counted by the required colors and the disjoint endpoint blocks.

## What this theorem does not prove

The packing sets in Case A are pairwise disjoint, not affine lines. In Case B, private residual blocks have a forced overlap somewhere, but no upper bound of one on pairwise intersections and no direction structure have been proved. Therefore the theorem does **not** yet imply an affine plane, a net, or a Kakeya lower bound.

The remaining graph-specific challenge is to show that the colored domination and private-witness constraints force many additional blocks or constrain their intersections. Without that step, the headline geometric dichotomy remains open.


## Round 2 addendum — alignment-free Case B constraints

The new theorem file ALIGNMENT_FREE_WITNESS_RIGIDITY.md proves an unconditional residual budget and dichotomy without assuming any low-slack vertex lies in X:

\[
\sum_{i\ne c}\big(e(G_i[R])-m_{r-1}\big)\le\binom{r-1}{2}.
\]

Writing n_i for the number of private witnesses assigned color i, either:
- some repeated witness color has n_i>=2 and residual excess b_i<=r-3, so Brouwer/Turan gives an (r-1)-clique-block partition of R and every Q_v of that color is a transversal; or
- some color has at least four private witnesses.

For every same-color pair u,v, both the residual difference graph between Q_u\\Q_v and Q_v\\Q_u and the full difference graph between T_u\\T_v and T_v\\T_u contain perfect matchings. The edge-ownership inequality explicitly bounds reuse of one color-i edge by endpoint witness-incidence multiplicities. These are graph-level rigidity constraints, not yet a contradiction.

## Round 2 addendum — residual budget and pairwise matching rigidity

The alignment gap is bypassed by ALIGNMENT_FREE_WITNESS_RIGIDITY.md. In Case B, the residual graph on R=V\\X, of size (r-1)^2, satisfies alpha(G_i[R])<=r-1 for every i!=c. Its excesses b_i=e(G_i[R])-m_{r-1} obey

\[
b_i\ge0,\qquad \sum_{i\ne c}b_i\le\binom{r-1}{2}.
\]

This yields an unconditional alternative: either a repeated witness color has b_i<=r-3 and its residual witnesses are transversals of a q=r-1 clique partition, or one color labels at least four private witnesses.

For any same-color witness pair, the bipartite graph between their residual symmetric differences has a perfect matching; the same holds for the full witness symmetric differences. This strengthens the previous edge lower bound, but does not yet rule out the private-witness configuration.

Case A is separately audited in COLORED_WITNESS_EDGE_BUDGET.md; its colored packing inequalities do not contradict the global color-edge floor.
