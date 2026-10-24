# Exact Orthogonality from Two Turan-Equality Colors

Status: **PROVED for all q>=2** as a graph statement. For a hypothetical counterexample with q>=3, a stronger consequence rules out even one exact-equality color.

## Setup and equality theorem

Let W have q^2 vertices and let G_i[W] be a color graph with alpha(G_i[W])<=q. The minimum edge count is

\[
m_q=q\binom q2.
\]

Equality holds exactly when G_i[W] is a disjoint union of q copies of K_q.

## Theorem K.1 — Two equality partitions are orthogonal

If distinct colors i,j both have exactly m_q edges on W, their equality partitions A_1,...,A_q and B_1,...,B_q satisfy

\[
|A_a\cap B_b|=1
\]

for every a,b.

Proof: no intersection can contain two vertices, since the edge between them would have both colors i and j. There are q^2 block intersections and q^2 vertices, so every intersection has size one.

## Stronger counterexample corollary — No exact-equality color on any restriction

Let x be the vertex outside W in a hypothetical counterexample on q^2+1 vertices. If one color i had e(G_i[W])=m_q, then K.5 in LOW_SLACK_COORDINATIZATION.md with s=0 forces a block A_a such that every edge from x to A_a has color i. Since A_a itself is a color-i K_q, A_a union {x} is a monochromatic K_(q+1), contradicting the counterexample property.

Therefore

\[
\boxed{s_i(x)=e(G_i-x)-m_q\ge1\quad\text{for every }i,x.}
\]

This is stronger than the earlier “at most one equality color” statement. The two-partition orthogonality theorem remains valid and useful for positive low slacks, but exact equality is individually impossible in a genuine counterexample.
