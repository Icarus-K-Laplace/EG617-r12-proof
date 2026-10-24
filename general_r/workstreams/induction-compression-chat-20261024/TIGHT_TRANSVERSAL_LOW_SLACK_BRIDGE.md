# Tight-Transversal / Low-Slack Bridge

Status: **PROVED conditionally; this is a cross-workstream structural theorem, not yet a contradiction.**

## Setup

Assume a hypothetical counterexample to P(r). Fix an eliminated color c and suppose the robust shell hypergraph H_{-c} has matching number exactly two and transversal number 2r. Let X be the union of a maximum matching, so |X|=2r and X is a minimum transversal. For every v in X, choose a private witness T_v: an independent r-set in a color i_v != c with T_v intersect X={v}.

Choose x_0 in X and a color i != c with local slack

\[
1\le s_i(x_0)\le r-2
\]

on W=V minus {x_0}. By low-slack coordinatization, G_i[W] partitions into r monochromatic K_r blocks P_1,...,P_r, plus exactly s_i cross-block color-i edges. Put Y=X minus {x_0}; then |Y|=2r-1.

Because X hits every independent r-set of color i and x_0 is not in W, Y hits every independent r-set of G_i[W].

Define residual parts B_a=P_a minus Y, with b_a=|B_a|.

## Theorem J.K1 — Witness-block concentration

For every v in Y whose private witness T_v has designated color i, let P_a be the unique block containing v. Then:

1. T_v is an independent transversal of the r blocks: it contains exactly one vertex from each P_b.
2. For b != a, the selected point of T_v in P_b lies in B_b, because T_v intersects X only at v.
3. If B_a is nonempty, then every u in B_a has a color-i edge to at least one of the r-1 points T_v minus {v}. Consequently
   \[
   b_a\le s_i.
   \]
4. If some B_a is empty, then every private witness of color i based in Y must be based in that same block P_a. No witness of color i can be based in any other block.

### Proof

Since T_v is independent in G_i[W] and each P_b is a color-i clique, it meets each P_b in exactly one vertex. The points other than v lie outside X, proving (2).

For (3), suppose u in B_a has no color-i edge to T_v minus {v}. Then (T_v minus {v}) union {u} is an independent r-set in G_i[W], and it is disjoint from Y. This contradicts that Y hits every independent r-set of color i. Thus every u in B_a has a color-i edge to the r-1 selected points in other blocks. Different u require distinct edges, all among the s_i cross-block defect edges, so b_a<=s_i.

For (4), if B_a is empty then P_a is wholly contained in Y. A private witness based in any other block would need one point from P_a, but all such points lie in X, contradicting T_v intersect X={v}. QED.

## Corollary J.K2 — Number of blocks that can host witnesses of a low-slack color

Let J_i be the set of blocks containing at least one v in Y with witness color i. Then

\[
\boxed{|J_i|\le\left\lfloor\frac{2r-1}{r-s_i}\right\rfloor.}
\]

Indeed, if some B_a is empty, J_i is contained in that single block. Otherwise, Theorem J.K1 gives b_a<=s_i for each a in J_i, so |Y intersect P_a|>=r-s_i on every such block. These blocks are disjoint and |Y|=2r-1.

Examples:
- If s_i=1 and r>=3, at most two blocks can host private witnesses of color i.
- More generally, for every s_i<=r-2, the low-slack color's private witnesses are confined to a quantitatively bounded set of blocks.

This is a genuine bridge from the tight-transversal certificates to the K-line block geometry.

## Theorem J.K3 — Weighted transversal-blocker constraint

If every B_a is nonempty, let F_i be the graph of color-i defect edges with both endpoints in the B_a parts. F_i has no independent transversal, because Y hits every independent r-set of color i in W.

For a uniformly random transversal choosing one vertex independently from each B_a, an edge uv between B_a and B_b is selected with probability 1/(b_a b_b). Since every transversal contains an edge of F_i, the union bound gives

\[
\boxed{\sum_{uv\in E(F_i)}\frac{1}{b_{a(u)}b_{a(v)}}\ge1.}
\]

In particular,

\[
\boxed{s_i\ge |E(F_i)|\ge\min_{a<b} b_a b_b.}
\]

The weighted inequality is stronger than merely saying some B_a has size at most s_i. It forces a pair of residual blocks with product at most s_i and identifies which defect edges are actually useful for blocking transversals.

## What remains open

- The theorem is conditional on a common vertex x_0 in the tight transversal X and a low-slack color i != c there.
- It does not force such a low-slack color to exist on X.
- It does not yet contradict the possibility that the witnesses for each color are concentrated in a small set of blocks.
- No affine line or Kakeya hypothesis is inferred.

The next target is to combine the block-host bounds across all witness colors, using that every v in X has exactly one designated witness color, or to derive a multicolor contradiction from the weighted blocker constraints.
