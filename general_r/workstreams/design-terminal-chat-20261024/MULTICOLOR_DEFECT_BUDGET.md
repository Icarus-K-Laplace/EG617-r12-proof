# Multicolor defect budget: exact accounting and corrected cylinder audit

Date: 2026-10-24  
Scope: the frozen `(5r+1)` terminal contract.

## 1. Frozen aggregate bounds

Let (W) be the terminal, (Q_0=\bigcup_{j=1}^5K(B_j)) the target ideal partition, and (Q_i=\bigcup_{a=1}^rK(C_{ia})) a non-target ideal partition. Under the existing stability theorem:
[
\sum_{i=0}^{r-1}|E(G_i[W])\triangle E(Q_i)|\le27r+15,
\qquad
\sum_{i=1}^{r-1}s_i\le8r+5.
]
For each non-target color define
[
d_i=\sum_a\bigl(|C_{ia}|-|\{j:C_{ia}\cap B_j\ne\varnothing\}|\bigr),
\qquad
m_{ij}=r-|\{a:C_{ia}\cap B_j\ne\varnothing\}|.
]
Then
[
\boxed{\sum_{j=1}^5m_{ij}=d_i-1.}
]
This is exact incidence bookkeeping.

## 2. Exact per-color ledger

Let
- (\Delta_i=e(Q_i)-p_r(5r+1)\ge0) be ideal block-size imbalance;
- (R_i=|E(Q_i)\setminus E(G_i)|) be deleted ideal edges;
- (A_i=|E(G_i)\setminus E(Q_i)|) be added cross-block edges.

Then
[
\boxed{s_i=\Delta_i-R_i+A_i.}
]
No term may be dropped. The same-group pair count and (d_i) are not interchangeable: a block with three points in one target group contributes (2) to (d_i) but (3) same-group pairs.

## 3. What the cylinder argument proves conditionally

If a repeated-group pair (uv\subset B_j\setminus X) is missing from (G_i), and there is a label (k\ne j) represented by a point of (B_k\setminus X) in **every other** ideal block of (Q_i), then
[
|E(G_i)\triangle E(Q_i)|\ge r-1.
]
The proof selects one ordinary (B_k)-point from each block. All selected points are pairwise target-adjacent, so every choice must contain an (i)-edge from (u) or (v). This is a **conditional** lemma; (d_i\le5) alone does not guarantee the ordinary-label condition because a hub may be the only point of that group in a block.

## 4. Correction: a cheap local cover exists but violates target alpha

The earlier attempted unconditional low-incidence propagation statement is withdrawn. A one-color graph can have (d_i=1), (s_i=4), and edit distance (6), with (\alpha(G_i)\le r), by deleting the repeated pair (uv) and adding a star from (u) to all five vertices of another transversal block, where one star edge is a target-deleted hub edge.

But that star plus the 5-clique block forms a (K_6) in (G_i), hence an independent 6-set in the target graph (G_0). It violates the full terminal condition (\alpha(G_0)\le5). So it is **not** a terminal counterexample; rather, it shows exactly why target alpha must be used in Hub Propagation.

A second previously suggested (d_i=6) pattern is also withdrawn as an (\alpha(G_i)\le r) example: an independent set can double two missing repeated-group pairs and omit the special singleton/4-block cover, so the proposed proof did not control all ((r+1))-sets.

## 5. New exact joint constraint

The target condition (\alpha(G_0)\le5) implies every non-target (G_i) is (K_6)-free. Therefore no vertex can be adjacent to all five vertices of a clean 5-clique ideal block. Any one-block cylinder cover of a missing pair must make the cover block non-clique in the actual color, creating another defect.

This yields a **defect-propagation chain**: every cheap star cover creates a new missing edge whose own independent-transversal obstruction must be covered elsewhere. The current blocker is to prove a lower bound on the total cost of this chain without double-counting edges or assuming affine-plane existence.

## 6. Global cross-pair budget

Let (a_j=|B_j|), (C=\sum_{j<k}a_ja_k), (D) be the number of target-ideal internal edges deleted from the actual target graph, (A) the number of actual target cross edges, and
[
\Delta_0=\sum_j\binom{a_j}{2}-p_5(5r+1),\qquad
S_{\rm non}=\sum_{i>0}s_i.
]
Then the exact identities are
[
s_0=\Delta_0-D+A,
\qquad
\boxed{A=C+D-(r-1)(10r+5)-S_{\rm non}},
]
or equivalently
[
\boxed{A=9r+5-\Delta_0+D-S_{\rm non}.}
]
In particular (s_0\ge r) implies (A\ge r-\Delta_0+D). Cylinder lower bounds for different deleted edges cannot simply be summed: they may reuse a hub star.

**Status:** identities and K6 exclusion are **PROVED_ANALYTIC**; defect-chain budget and Hub Propagation remain **OPEN**.


## 7. Exact two-defect closure and the slack threshold

The block-level gadget in `HUB_PROPAGATION_THEOREM.md` has one 6-block and one 5-block, with exactly two missing ideal edges and nine added cross-block edges:
[
R_i=2,\quad A_i=9,\quad s_i=7,\quad
|E(G_i)\triangle E(Q_i)|=11.
]
It satisfies both (\alpha(G_i)\le r) and (K_6)-freeness. Therefore the local requirements do not imply (s_i\ge9), nor do they force a third defect after two defects interact.

This matters numerically: the inherited aggregate budget is
[
\sum_{i>0}s_i\le8r+5.
]
A hypothetical family with (s_i=7) or (8) in most colors is not excluded by this inequality alone. The total edit bound (27r+15) likewise permits (11(r-1)) edits at the scalar level.

## 8. Target labels create the real obstruction

The two-defect gadget has not been completed into a target-labelled terminal. If a missing edge (wx) in a non-target ideal block is a target cross-star edge (wB_k\), then the point (z_k\in B_k) in any other ideal block has both (wz_k) and (xz_k) target-colored whenever (z_k\notin X). It cannot serve as a (G_i)-neighbor of either endpoint.

Thus the cover must either:
- use a hub (z_k\in X\) in that coordinate;
- use edges involving other selected blocks; or
- exploit a further target-internal deletion.

A fixed blocked coordinate can be covered by a local 9-edge two-coordinate barrier (four neighbors into each of two 5-blocks plus the edge between their two nonneighbors), so merely saying “the cover propagates” does not give a growing lower bound.

**Updated blocker:** prove a target-labelled, pair-ownership-aware lower bound on the *entire* cover system. It must rule out repeating constant-size local gadgets across colors, not merely rule out one gadget in isolation.
