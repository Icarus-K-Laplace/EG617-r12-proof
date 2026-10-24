# Weighted Independent-Transversal Blocker Lemma

Status: **PROVED; elementary probabilistic obstruction bound**.

## Theorem K.B1

Let B_1,...,B_q be pairwise disjoint nonempty finite sets, with b_a=|B_a|. Let F be a simple graph whose edges always join vertices in different parts. Suppose F has no independent transversal, meaning every choice of one vertex from each B_a contains at least one edge of F.

Then

\[
\boxed{\sum_{uv\in E(F)}\frac{1}{b_{a(u)}b_{a(v)}}\ge1,}
\]

where a(u) is the index of the part containing u.

### Proof

Choose a random transversal by choosing one vertex uniformly and independently from each B_a. For an edge uv between B_a and B_b, the probability that both endpoints are selected is exactly 1/(b_a b_b). Since F has no independent transversal, the union of the edge-selection events has probability 1. The union bound therefore implies

\[
1\le\sum_{uv\in E(F)}\Pr(u,v\text{ both selected})
=\sum_{uv\in E(F)}\frac{1}{b_a b_b}.
\]

## Corollaries

Let p=min_{a<b} b_a b_b. Every summand is at most 1/p, so

\[
|E(F)|\ge p=\min_{a<b}b_a b_b.
\]

If every part has size at least k, then |E(F)|>=k^2. Thus a blocker with at most q-2 edges must have a pair of parts whose size product is at most q-2.

The weighted form is more informative than the unweighted corollary: it shows that edges between large residual parts consume little of the obstruction budget, so any small-slack blocker must place its effective defect edges around sufficiently small parts.

## Application to EG617 low-slack restrictions

Let W=V minus {x} have q^2 vertices, and suppose color i has low slack 1<=s_i<=q-2. Its graph partitions into q color-i cliques P_1,...,P_q and s_i cross-block defect edges. Let Y be any set that hits every independent r-set of color i in W, and define B_a=P_a minus Y.

If every B_a is nonempty, the graph F_i consisting only of defect edges with both endpoints in the B_a parts has no independent transversal: an independent transversal would be an independent r-set avoiding Y. Hence

\[
\sum_{uv\in E(F_i)}\frac{1}{|B_{a(u)}||B_{a(v)}|}\ge1,
\qquad
s_i\ge\min_{a<b}|B_a||B_b|.
\]

If some B_a is empty, Y contains a full color-i clique block, which trivially hits all transversals; the weighted lemma is not needed.

## Limitation

This lemma is a necessary condition, not a full characterization of independent-transversal obstructions. It does not by itself imply a contradiction for two orthogonal partitions, nor does it create line-like blocks in three directions. Its value is quantitative: it localizes where the small number of defect edges must lie.
