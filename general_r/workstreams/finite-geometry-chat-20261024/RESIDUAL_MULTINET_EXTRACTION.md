# Residual Multinet Extraction from a Tight Compression Transversal

Status: **PROVED as a conditional consequence of J's Case B; no full affine plane or EG617 contradiction is claimed.**

## Exact upstream contract

This note invokes the exact Case B theorem proved on the J branch in

- branch: workstream/general-r-induction-compression-20261024
- file: general_r/workstreams/induction-compression-chat-20261024/ALIGNMENT_FREE_WITNESS_RIGIDITY.md
- source commit: 009a546cf0d66e4060a601bba168674214e7ac6c
- theorem: J.W1 and J.W5.

The hypothesis is a full hypothetical r-counterexample, a fixed color c with no robust shell, and the matching-number-two/tight-transversal case. Set q=r-1, let X be the 2r-point minimum transversal, and let R=V minus X, so |R|=q². For every i != c, alpha(G_i[R])<=q. Define

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


## Small-order and non-prime-power audit

The direction bound is t>=ceil(q/2), but it only invokes Brouwer's partition theorem for q>=3. The first values are:

| q=r-1 | Guaranteed directions t | MOLS forced in Case B | Status of the design implication |
|---:|---:|---:|---|
| 2 (r=3) | at least 1 residual-low color; no two-direction net from this count | none | small case not covered by Brouwer |
| 3 (r=4) | at least 2 | 0 | orthogonal partitions only |
| 4 (r=5) | at least 3 | 1 Latin square | strengthened by J.W9 |
| 5 (r=6) | at least 3 | 1 Latin square | no obstruction from count alone |
| 6 (r=7) | at least 4 | 2 MOLS(6) | impossible; Case B is closed by J.W8/J.W9 |
| 7 (r=8) | at least 4 | 2 MOLS(7) | available for prime-power order |
| 8 (r=9) | at least 5 | 3 MOLS(8) | available for prime-power order |
| 9 (r=10) | at least 5 | 3 MOLS(9) | available for prime-power order |
| 10 (r=11) | at least 6 | 4 MOLS(10) | stronger than the known open 3-MOLS threshold; not excluded here |
| 14 (r=15) | at least 8 | 6 MOLS(14) | stronger than the reported open 5-MOLS threshold; not excluded here |

For q=10, a projective plane of order 10 is known not to exist; for q=14, Bruck–Ryser rules out a projective plane of order 14. Hence the full-affine-plane subcase K.RM3 is unavailable at q=10 and q=14. The strict-budget theorem J.W9 strengthens the partial-net requirements to at least 4 MOLS(10) and 6 MOLS(14), respectively. The cited literature only establishes that the weaker 3-MOLS(10) and 5-MOLS(14) thresholds remain open; these stronger implications are not excluded here.

Sources for the two open MOLS thresholds:
- Three MOLS(10): Bright, Keita, Stevens, EJC 33(1) (2026), P1.30, DOI [10.37236/13960](https://doi.org/10.37236/13960), [arXiv:2503.10504](https://arxiv.org/abs/2503.10504).
- Five MOLS(14): Todorov constructed four MOLS(14), DOI [10.1002/jcd.21298](https://doi.org/10.1002/jcd.21298); the existence of a fifth is reported open in the literature on MOLS/difference covering arrays.


## Theorem K.RM4 — Exact first-high-excess normal form at b_i=q-1

Assume q>=3 and fix i!=c with b_i=q-1. Let H_i be the complement of G_i[R]. Then H_i is K_{q+1}-free and

\[
e(H_i)=t_q(q^2)-q+1.
\]

There are two exact cases.

**Case 1: H_i is q-partite.** Its q parts have size at most q because alpha(G_i[R])<=q; since they cover q² vertices, all parts have size q. The graph G_i[R] is therefore a union of q K_q blocks plus exactly q-1 color-i cross-block edges.

**Case 2: H_i is not q-partite.** By the exact extremal classification of Kang–Pikhurko, H_i is a maximum-edge non-q-partite K_{q+1}-free graph and has an exceptional vertex y such that H_i-y is q-partite, with the extremal construction's only missing cross-part pairs forming a nonempty star. Equivalently, R minus {y} has q clique blocks under color i, with sizes q except for one block of size q-1, plus a nonempty star of color-i cross-block edges with a leaves, where 1<=a<=q-1. Since

\[
e(G_i[R\setminus\{y\}])=m_q-(q-1)+a,\qquad e(G_i[R])=m_q+q-1,
\]

the exceptional point has exact residual color-i degree

\[
\boxed{d_i^{R}(y)=2q-2-a.}
\]

The external theorem used is M. Kang and O. Pikhurko, “Maximum K_{r+1}-free graphs which are not r-partite,” *Matematychni Studii* 24(1) (2005), 12–20, DOI [10.30970/ms.24.1.12-20](https://doi.org/10.30970/ms.24.1.12-20), Theorem 4 and Lemma 5. Its assumptions hold because q²>=2q+1 for q>=3.

### Witness interface

If this color i is the repeated witness color from J's Case B dichotomy, each residual witness Q_v is an independent q-set in G_i[R]. In Case 1 it is a transversal of the q blocks avoiding the q-1 defect edges. In Case 2 it either avoids the exceptional vertex and is a transversal avoiding the defect star, or contains the exceptional vertex and has one point in each of q-1 blocks, avoiding both the star and the exceptional vertex's color-i neighborhood.

This is an exact finite incidence kernel at the first high-excess threshold. It is not yet excluded; if b_i>=q, the Kang–Pikhurko extremal equality classification no longer applies directly.


## Theorem K.RM5 — Exact residual profile at q=6 (r=7), Case B

Assume the tight-transversal Case B with q=6, so R has 36 vertices and six residual colors i!=c. The total residual excess satisfies

\[
\sum_{i\ne c}b_i\le\binom62=15.
\]

Let H_i be the complement of G_i[R]. Every q-partite H_i supplies a direction in a net, and these partitions are pairwise orthogonal. Four directions would give two mutually orthogonal Latin squares of order 6, which do not exist by Euler–Tarry (see Betten, *A direct proof of the non-existence of a MOL(6)*, Journal of Geometry 114 (2023), DOI [10.1007/s00022-023-00669-3](https://doi.org/10.1007/s00022-023-00669-3)). Therefore at most three H_i are 6-partite, and at least three are non-6-partite.

By Brouwer's threshold, every non-6-partite H_i has b_i>=5. The budget then forces equality throughout:

\[
\boxed{\begin{aligned}
&\text{exactly three colors have }b_i=5\text{ and non-6-partite }H_i,\\
&\text{the other three colors have }b_i=0\text{ and give three orthogonal directions},\\
&\sum_{i\ne c}b_i=15.
\end{aligned}}
\]

Each of the three high colors is at the exact K.RM4 threshold, so each has the exceptional-star normal form. The three zero-excess colors partition R into three pairwise orthogonal families of six K_6 blocks: a 3-net, equivalently a Latin square of order 6.

The omitted color c is also forced into an exact extremal profile. Since

\[
\binom{36}{2}=630,\qquad m_6=6\binom62=90,
\]

the six other colors use \(6\cdot90+15=555\) edges in R, so \(e(G_c[R])=75\). The full contract gives alpha(G_c[R])<=7, and 75 is exactly the Turan minimum for independence number at most 7. Hence G_c[R] is a union of seven monochromatic-c cliques of sizes

\[
\boxed{6,5,5,5,5,5,5.}
\]

The 6-clique is a full transversal of the three 6-by-6 directions; each of the six 5-cliques is a near-transversal of all three directions. These seven blocks partition all 36 points.

Finally, J's witness-color dichotomy sharpens in this profile. Either at least one zero-excess color has two or more private witnesses, whose residual Q_v are transversals of that direction; or all three zero-excess colors occur at most once among the 14 witness roots, so at least 11 roots use the three high colors and one high color has at least four witnesses. That high color has the exceptional-star form above.

This is a finite incidence kernel for the r=7 Case B, not a contradiction. The one-transversal-plus-six-near-transversal decomposition is not itself an orthogonal mate, so Euler–Tarry cannot be applied to exclude it. Case A is not covered.


### K.RM5 audit boundary

The 3-net plus one-transversal/six-near-transversal subkernel is realizable as a Latin-square incidence structure; see Q6_NEAR_TRANSVERSAL_OBSTRUCTION_AUDIT.md, commit 825c48ae4e5cc47e7feb6abab6337de62db6fd6c. Therefore it cannot be excluded by Euler–Tarry alone. The full EG617 kernel still additionally requires the three exceptional-star high-color graphs and the 14-root witness incidence.


## Theorem K.RM6 — Strict residual budget and r=7 closure

J branch commit c0c31e82b2bd8b4c3c5a7ab6092b660d16bd686b proves the full-contract root-block capacity theorem J.W8: for q=r-1>=4, equality sum b_i=C(q,2) is impossible. Therefore

\[
\sum_{i\ne c}b_i\le\binom q2-1,
\]

and at most floor((q-1)/2) residual complements are non-q-partite. At least ceil((q+1)/2) colors therefore give pairwise orthogonal q-clique partitions, strengthening the earlier bound by one direction for even q.

For q=6 this forces at least four directions, hence two mutually orthogonal Latin squares of order 6, impossible by Euler–Tarry. Thus **Case B is impossible at r=7**. The explicit Latin-square example in Q6_NEAR_TRANSVERSAL_OBSTRUCTION_AUDIT.md realizes only the abstract 3-net plus one-transversal/six-near-transversal subkernel; the root-block coverage constraint prevents extending it to the full EG617 Case B contract.


## Theorem K.RM6 — Strict residual excess budget

**Source:** J branch workstream/general-r-induction-compression-20261024, commit c0c31e82b2bd8b4c3c5a7ab6092b660d16bd686b, file ALIGNMENT_FREE_WITNESS_RIGIDITY.md, Theorem J.W8.

Under the full hypothetical-counterexample contract and Case B, for q=r-1>=4,

\[
\boxed{\sum_{i\ne c}b_i\le \binom q2-1.}
\]

Proof audit: if equality held in the earlier bound, the omitted color c would attain the Turan minimum for alpha(G_c[R])<=q+1. Its graph would be exactly q+1 disjoint cliques of sizes q,q-1,...,q-1. For every x in X, the color-c neighborhood of x must contain an entire block; otherwise choose one c-nonneighbor from each block to get a c-independent (q+1)-set in R which remains c-independent with x, contradicting the full counterexample property. A q-block can be fully contained in at most one root's c-neighborhood; a (q-1)-block can be fully contained in at most two, since three roots plus that block form a (q+2)-set using at most four colors, fewer than r=q+1 for q>=4. Therefore |X|<=1+2q, contradicting |X|=2q+2.

Consequently at most floor((q-1)/2) residual colors are non-q-partite, because each such color costs b_i>=q-1. Thus at least

\[
\boxed{\left\lceil\frac{q+1}{2}\right\rceil}
\]

colors give pairwise orthogonal q-clique partitions of R.

### Corollary K.RM7 — Case B impossible for r=7

For r=7, q=6, the strict bound forces at least four orthogonal 6-clique partitions on the 36-point set R. Taking two as row/column partitions, the other two yield a pair of mutually orthogonal Latin squares of order 6, ruled out by Euler–Tarry. Hence Case B is impossible at r=7.

Boundary: this does not eliminate Case A (matching number at least three), and it does not prove the full r=7 theorem or an all-r induction.


## Audit correction — K.RM8 withdrawn

The quantitative root-block extension imported from J commit 5466f79333f0e8b1694c181c2ece4ae907086a37 is **invalid and withdrawn**. Its random transversal was sampled from full clique blocks, but a contradiction for a root requires selecting only from that root's nonneighbor subset in each block. Those subsets can be singletons; the probability bound used in the attempted proof therefore fails.

Do not use the claimed \(d\ge \binom{k+1}{2}\) bound, its numerical thresholds, or the corresponding stronger net direction count. The independently audited J.W8 strict endpoint bound \(d\ge1\) remains valid, and it is enough to close the q=6 / r=7 Case B using the Euler–Tarry obstruction. Any stronger excess bound must explicitly handle root-dependent transversal blockers.


## Theorem K.RM9 — Root-dependent weighted blocker inequality

Exact source: J branch workstream/general-r-induction-compression-20261024, commit eb5aaee4e2957b8f18d1c62c886dab8d6d23337e, file ALIGNMENT_FREE_WITNESS_RIGIDITY.md, Theorem J.W12.

Assume \(H_c=\overline{G_c[R]}\) is \((q+1)\)-partite with blocks \(B_j\), and let E be the set of cross-block color-c edges in G_c[R]. For a root x that does not fully c-cover any block, set \(A_j(x)=\{v\in B_j: xv\text{ is not color }c\}\), with \(a_j(x)=|A_j(x)|\ge1\). A uniformly random transversal selecting one vertex from each A_j has expected number of cross-block c-edges

\[
W_x=\sum_{\substack{uv\in E\\u\in B_i,\ v\in B_j}}\frac1{a_i(x)a_j(x)}.
\]

If W_x<1, a c-independent transversal exists and adjoining x gives a forbidden c-independent (r+1)-set. Thus every root that fully covers no block must satisfy W_x>=1.

This is the correct blocker-weight condition: choices must be sampled from the root's nonneighbor sets, not the full blocks. It is a necessary structural inequality, not a quantitative lower bound on |E| by itself. The attempted stronger bound in the withdrawn K.RM8 is invalid and must not be reused.
