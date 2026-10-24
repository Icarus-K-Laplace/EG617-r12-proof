# Low-Slack Coordinatization on a q^2 Restriction

Status: **PROVED for every integer q>=3**, using Brouwer's non-r-partite Turan threshold. No prime-power assumption is needed.

## External theorem and exact assumptions

Brouwer's theorem in the form stated by Popielarz–Sahasrabudhe–Snyder, JCTB 132 (2018), Theorem 2.2, says: if n>=2r+1 and H is a K_(r+1)-free n-vertex graph with

\[
e(H)\ge t_r(n)-\lfloor n/r\rfloor+2,
\]

then H is r-partite. The published source is https://doi.org/10.1016/j.jctb.2018.04.001. The same threshold is related to Kang–Pikhurko, “Maximum K_(r+1)-free graphs which are not r-partite” (2005).

Here n=q^2 and r=q; the hypothesis n>=2q+1 holds for q>=3.

## Setup

Let W be a q^2-vertex subset of a hypothetical counterexample to P(q), and let G_i[W] be one color graph. Then alpha(G_i[W])<=q and omega(G_i[W])<=q.

Set

\[
m_q=q\binom q2=\frac{q^2(q-1)}2,\qquad
s_i=e(G_i[W])-m_q\ge0.
\]

The floor m_q follows from Turan complementarity: a graph with independence number at most q has at least m_q edges on q^2 vertices.

## Theorem K.3 — Low-slack clique-partition extraction

If 0<=s_i<=q-2, then W partitions into q blocks P_1,...,P_q such that:

- each block has size q;
- every block induces a monochromatic K_q of color i;
- exactly s_i additional color-i edges run between distinct blocks.

### Proof

Let H be the complement of G_i[W]. Since alpha(G_i[W])<=q, H is K_(q+1)-free. Also

\[
e(H)=t_q(q^2)-s_i\ge t_q(q^2)-q+2.
\]

Brouwer's theorem makes H q-partite. Its q parts are cliques in G_i; because omega(G_i)<=q, each part has at most q vertices. Since they cover q^2 vertices, there are exactly q parts of size q. The within-part edges contribute m_q color-i edges, leaving exactly s_i cross-block edges.

## Corollary K.4 — Two low-slack colors give exact orthogonal partitions

If distinct colors i,j both have slack at most q-2 on W, their block partitions are orthogonal:

\[
|P_a\cap Q_b|=1\quad\text{for every }a,b.
\]

No intersection can contain two vertices, because their edge would have to carry both colors i and j. There are q^2 intersections and q^2 points, so every intersection has size one.

This produces a q-by-q grid with two directions. It does not by itself produce a full affine plane or field coordinates.

## Theorem K.5 — Strengthened near-line forcing from the extra vertex

Let x be the unique ambient vertex outside W and suppose color i has the partition above with slack s=s_i. For each block P_a, define

\[
B_a:=\{v\in P_a: xv\text{ is not color }i\}.
\]

In a hypothetical counterexample every B_a is nonempty: otherwise P_a union {x} is a monochromatic K_(q+1) of color i.

Let E_i be the set of the s color-i edges crossing between distinct P_a blocks. Then

\[
\boxed{\min_a |B_a|\le s.}
\]

Consequently some block has at least q-s color-i edges to x. This strengthens the previous q-2s bound.

### Proof

Suppose every |B_a|>=s+1. Process the blocks one at a time. In the current B_a, at most s vertices are joined by an E_i edge to a previously selected representative, because E_i has only s edges in total. Choose a vertex not so joined. Greedy selection yields one vertex from each B_a with no color-i cross-edge; there are no within-block pairs because only one vertex is chosen per block. All chosen vertices have non-color-i edges to x. Their union with x is a (q+1)-set missing color i, contradiction.

If s=0, this theorem forces some B_a to be empty, which is already impossible in a counterexample. Therefore every hypothetical counterexample satisfies

\[
s_i(x)\ge1\quad\text{for every vertex }x\text{ and every color }i.
\]

## Two-color transversal-blocking form

When i and j both have low slack, their partitions are orthogonal. Every row block A_a has a nonempty set B_a^i of vertices whose edge to x is not i, and every column block Q_b has a nonempty set B_b^j of vertices whose edge to x is not j.

Every choice of one vertex from each B_a^i must contain an edge of color i between chosen vertices; otherwise adding x gives a forbidden set missing color i. The cross-defect graph E_i, with exactly s_i edges, blocks every such transversal. In particular, some row has |B_a^i|<=s_i. The analogous statement holds for color j and its columns.

This is a precise local constraint on the extra-vertex color matrix. It does **not** yet prove that two low-slack colors cannot coexist when both slacks are positive.

## Current gap

No theorem currently forces two colors into the window 1<=s_i(x)<=q-2 on any common q^2 restriction. Nor has the transversal-blocking condition for two orthogonal partitions been shown to yield a contradiction for positive slacks.
