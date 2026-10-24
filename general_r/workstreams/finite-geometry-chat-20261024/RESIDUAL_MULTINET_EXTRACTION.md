# Residual Multinet Extraction from a Tight Compression Transversal

Status: **PROVED as a conditional consequence of J's Case B; no full affine plane or EG617 contradiction is claimed.**

## Exact upstream contract

This note invokes the exact Case B theorem proved on the J branch in

- branch: workstream/general-r-induction-compression-20261024
- file: general_r/workstreams/induction-compression-chat-20261024/ALIGNMENT_FREE_WITNESS_RIGIDITY.md
- source commit: 009a546cf0d66e4060a601bba168674214e7ac6c
- theorem: J.W1 and J.W5.

The hypothesis is a full hypothetical r-counterexample, a fixed color c with no robust shell, and the matching-number-two/tight-transversal case. Set q=r-1, let X be the 2r-point minimum transversal, and let R=V\\X, so |R|=q². For every i != c, alpha(G_i[R])<=q. Define

\[
b_i=e(G_i[R])-m_q,\qquad m_q=q\binom q2.
\]

J proves, without a low-slack neighborhood premise,

\[
b_i\ge0,\qquad \sum_{i\ne c}b_i\le\binom q2.
\]

## Theorem K.RM1 — A residual q-net with at least ceil(q/2) directions

Call i residual-low if b_i<=q-2. Every non-low color has b_i>=q-1, so at most floor(q/2) colors are non-low. There are q colors i != c; hence at least ceil(q/2) are residual-low.

For q>=3, Brouwer's non-q-partite Turan threshold applied to the complement of G_i[R] implies that every residual-low color partitions R into q monochromatic color-i clique blocks. Any two residual-low colors i,j give orthogonal partitions: a j-block is independent in G_i[R], so has at most q points; q such blocks partition q² points, hence each has exactly q points. It intersects each i-block in at most one point, so it intersects every i-block exactly once. The same argument gives size q for every i-block.

Thus R carries a q-net with t>=ceil(q/2) directions: each direction partitions q² points into q blocks of size q, and blocks from different directions intersect in exactly one point.

This theorem uses residual excess on R, not the neighborhood slack s_i(x) from the full r-coloring. It is therefore consistent with J/K's Local Slack Gap Theorem, which rules out s_i(x)<=r-2 on every full-counterexample neighborhood.

## Corollary K.RM2 — MOLS lower bound

Fix any two of the t orthogonal partitions as row and column classes. Each of the remaining t-2 partitions is a Latin square, and pairwise orthogonality of partitions gives pairwise orthogonality of these squares. Therefore the Case B contract implies

\[
N(q)\ge t-2\ge\left\lceil\frac q2\right\rceil-2,
\]

where N(q) denotes the maximum number of mutually orthogonal Latin squares of order q.

### Special audit: q=10, hence r=11

If a hypothetical r=11 counterexample enters Case B, then q=10 and t>=5. The residual 100-point set R would therefore yield at least three mutually orthogonal Latin squares of order 10.

The existence of 3 MOLS(10) remains a documented open problem in the 2026 SAT investigation by Bright, Keita, and Stevens, *Myrvold's Results on Orthogonal Triples of 10 x 10 Latin Squares: A SAT Investigation*, Electronic Journal of Combinatorics 33(1) (2026), P1.30, DOI [10.37236/13960](https://doi.org/10.37236/13960), preprint [arXiv:2503.10504](https://arxiv.org/abs/2503.10504). The investigation resolves restricted cases, not the general existence question.

Therefore this is a conditional reduction of the r=11 Case B branch to a classical open design question, **not** a contradiction. It does not address Case A.

## Theorem K.RM3 — Full-affine-plane subcase

If the omitted color c also satisfies alpha(G_c[R])<=q, then Turan complementarity gives e(G_c[R])>=m_q. But the total edge count on R is (q+1)m_q, while the other q colors contribute q*m_q+sum b_i. Hence

\[
e(G_c[R])=m_q-\sum_{i\ne c}b_i.
\]

It follows that all b_i=0 and e(G_c[R])=m_q. Every one of the q+1 color graphs on R is then a disjoint union of q K_q blocks; the partitions are pairwise orthogonal. Consequently R is an affine plane of order q (equivalently a complete set of q-1 MOLS).

This is only a structural subcase. No theorem here shows that the resulting affine-plane coloring cannot coexist with the 2r outside vertices X, and no line-hitting lower bound is invoked without a proved shell-hitting premise.

## Open gaps

1. Case A (matching number at least three) is not covered by this extraction.
2. In Case B, the q-net may have only ceil(q/2) directions; it need not complete to an affine plane.
3. The net blocks are not automatically all required to lie in a deletion shell, so the bound tq-C(t,2) cannot be applied to |X| without an additional theorem.
4. No contradiction to P(r), no fixed-merge escape, and no implication not-P(r) => not-P(r-1) is proved here.
