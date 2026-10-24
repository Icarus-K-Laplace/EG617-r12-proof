# Exact Classification of One- and Two-Edge Transversal Blockers

Status: **PROVED**.

## Setup

Let B_1,...,B_q be nonempty parts. Let F be a simple graph whose edges run between distinct parts. An independent transversal is a choice of one vertex from each part with no selected edge.

## Theorem K.B2 — One relevant edge

If F has at most one edge and no independent transversal, then it has exactly one edge, and both endpoint parts are singletons. That edge joins the two singleton vertices.

Proof: one edge can block every transversal only if every transversal selects both endpoints, which requires each endpoint part to have size one.

## Theorem K.B3 — At most two relevant edges

Suppose F has at most two edges and no independent transversal. Then at least one of the following holds:

1. F contains an edge between two singleton parts. This edge alone blocks every transversal; any other edge is irrelevant to the obstruction.
2. F has exactly two edges, and both are between a singleton part and a size-two part. The two edges share the size-two part and use its two different vertices. The singleton endpoints may lie in the same singleton part or in two different singleton parts.

### Proof

Choose a uniformly random transversal. For an edge e between parts B_a,B_b, let A_e be the event that both endpoints are selected. Then P(A_e)=1/(|B_a||B_b|). If no independent transversal exists, these edge events cover the entire product space.

If an edge joins two singleton parts, case 1 holds. Otherwise every event has probability at most 1/2. One edge cannot cover the space. With two edges, the union bound gives

\[
1\le P(A_{e_1})+P(A_{e_2})\le1.
\]

Equality forces both probabilities to equal 1/2 and the events to be disjoint. Thus each edge joins a singleton part to a size-two part. The events can be disjoint only when the edges use different vertices of the same size-two part: if they used different size-two parts, there would be a transversal selecting both edges simultaneously. This proves case 2.

## Corollary K.B4 — The EG617 shell budget removes the three-part pattern

Suppose q>=4, |Y|=2q-1, and B_a=P_a minus Y for q blocks P_a of size q. If a blocker with at most two defect edges has no independent transversal on the nonempty B_a parts, then its obstruction is supported on at most two parts.

Indeed, the only possible three-part form in K.B3 has part sizes 1,1,2. To realize these residual sizes, Y must contain at least

\[
(q-1)+(q-1)+(q-2)=3q-4>2q-1
\]

vertices, impossible. Therefore the two-singleton-edge or singleton-to-size-two obstruction is supported on two parts.

Consequently, if a private color-i witness is an independent transversal with one base vertex in a block P_a and one residual vertex in every other block, its base block must lie in the at-most-two-part obstruction support. Otherwise the witness would have to select a forbidden edge inside the support.

## Application

In the J/K tight-transversal bridge, if a low-slack color has s_i=1 or 2, the defect-edge blocker on residual parts has at most two relevant edges. For q>=4 (and for s_i=1 also at q=3), all private witnesses of that color are based in at most two clique blocks. This sharpens the general bound floor((2q-1)/(q-s_i)) in the small-slack cases.

## Limitation

The classification is exact only for at most two relevant defect edges. It does not classify blockers with three or more edges and does not itself yield a contradiction.

## Round 2 contract audit — classification is conditional/vacuous locally

The exact one-/two-edge classifications above remain valid abstract blocker lemmas. However, when combined with the full EG617 counterexample contract, the low-slack block structure plus the q+1-set `{x} union A_a` condition yields `s_i(x)>=q-1`; see `HIGH_SLACK_COMPATIBILITY.md`. Therefore the cases `s_i(x)=1` or `2` cannot actually occur at a vertex of a full hypothetical counterexample (for q>=3). Do not present the classification as an exhibited or potentially realized local counterexample pattern. Its independent-transversal statement remains correct and can still be used in other contracts.
