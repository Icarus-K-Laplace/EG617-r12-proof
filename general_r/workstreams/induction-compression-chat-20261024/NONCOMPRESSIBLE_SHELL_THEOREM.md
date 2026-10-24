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

Thus every point of the packed 2r-set has a private independent-set witness extending outside X. This is a concrete critical-transversal structure.

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

The packing sets above are pairwise disjoint. They are not affine lines, and no pairwise-intersection-at-most-one property between different families has been proved. Therefore the theorem does **not** yet imply an affine plane, a net, or a Kakeya lower bound.

The remaining graph-specific challenge is to show that the colored domination and private-witness constraints force many additional blocks or constrain their intersections. Without that step, the headline geometric dichotomy remains open.
