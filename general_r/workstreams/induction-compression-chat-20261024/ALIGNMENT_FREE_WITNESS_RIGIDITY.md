# Alignment-Free Witness Rigidity: Residual Budget and Color Dichotomy

Status: **PROVED alignment-free dichotomy; global contradiction remains OPEN.**

This note uses the already-established Case B contract only. It does not assume a low-slack vertex in X.

## Setup

Let H_{-c} have matching number two and transversal number 2r. Let X be the union of a maximum matching, so |X|=2r, and let R=V minus X, |R|=(r-1)^2. For each v in X choose a private witness

\[
T_v=\{v\}\cup Q_v,\qquad |Q_v|=r-1,\qquad Q_v\subset R,
\]

independent in its designated color i_v != c. Put

\[
C_i=\{v\in X:i_v=i\},\quad n_i=|C_i|,\quad
S=\{i\ne c:n_i>0\}.
\]

(Equivalently, C_i is the set of roots whose chosen private witness has color i.) Thus \(\sum_{i\ne c}n_i=2r\) and \(|S|\le r-1\).

Write

\[
m_{r-1}=(r-1)\binom{r-1}{2}
=\frac{(r-1)^2(r-2)}2,
\qquad
b_i=e(G_i[R])-m_{r-1}\quad(i\ne c).
\]

## Theorem J.W1 — Residual edge budget

For every i != c, b_i is a nonnegative integer, and

\[
\boxed{\sum_{i\ne c}b_i\le\binom{r-1}{2}.}
\]

### Proof

Because X hits every independent r-set in every color i != c, the graph G_i[R] has independence number at most r-1. Turan complementarity therefore gives \(e(G_i[R])\ge m_{r-1}\), so \(b_i\ge0\).

The total number of edges in R is

\[
\binom{(r-1)^2}{2}=r\,m_{r-1}.
\]

The full counterexample condition gives \(\alpha(G_c[R])\le r\). The Turan lower bound for this color is

\[
e(G_c[R])\ge
\binom{(r-1)^2}{2}-t_r((r-1)^2)
=\frac{(r-1)(r-2)^2}{2}.
\]

Subtracting the \(r-1\) floors \(m_{r-1}\) from the total edge count leaves

\[
\sum_{i\ne c}b_i
=m_{r-1}-e(G_c[R])
\le \frac{(r-1)(r-2)}2
=\binom{r-1}{2}.
\]

## Theorem J.W2 — Alignment-free color-concentration / residual-partition dichotomy

At least one of the following holds:

**(A) Repeated low-excess witness color.** There is a color i != c with \(n_i\ge2\) and

\[
\boxed{b_i\le r-3.}
\]

For this color, R has a partition into q=r-1 nonempty color-i clique blocks \(P_1,\ldots,P_q\), and every residual witness \(Q_v\) with \(v\in C_i\) is a transversal of these q blocks.

**(B) Quantitative color concentration.** There is a color i != c with

\[
\boxed{n_i\ge4.}
\]

Every pair of its residual witnesses has the same-color perfect-matching rigidity described in Theorem J.W3 below, and their overlap graph has at least two edges.

### Proof

Suppose (A) fails. Let t be the number of colors with \(n_i\ge2\). Every such color then has \(b_i\ge r-2\), so Theorem J.W1 implies

\[
t(r-2)\le\binom{r-1}{2},
\qquad t\le\frac{r-1}{2}.
\]

If every \(n_i\le3\), the t repeated color classes contribute at most \(3t\), and each other nonempty color class contributes one. Therefore

\[
2r=\sum_i n_i\le |S|+2t
\le (r-1)+(r-1)=2r-2,
\]

a contradiction. Hence some \(n_i\ge4\), proving (B).

Now suppose (A) holds. Put q=r-1. We have \(\alpha(G_i[R])\le q\) and \(e(G_i[R])=q\binom q2+b_i\), with \(b_i\le q-2\). For r>=4, Brouwer's non-q-partite Turan threshold applied to \(\overline{G_i[R]}\) makes that complement q-partite. Hence \(G_i[R]\) partitions into q cliques \(P_a\). The clique sizes \(p_a=|P_a|\) satisfy

\[
b_i=\frac12\sum_{a=1}^q(p_a-q)^2+e_\times,
\]

where \(e_\times\) is the number of color-i edges between different blocks. Since \(b_i\le q-2\), no block is empty; also \(p_a\le r=q+1\) by the global clique bound. Each \(Q_v\) for \(v\in C_i\) is an independent q-set in \(G_i[R]\), so it has at most one point in each clique block. With q nonempty blocks and |Q_v|=q, it has exactly one point in every block.

For r=3, the budget gives \(b_i=0\) for a repeated low-excess color. Equality in Turan's theorem makes \(G_i[R]\) a matching on four vertices, i.e. two K_2 blocks, and each two-point \(Q_v\) is a transversal. This handles the small case excluded by Brouwer's \(n\ge2q+1\) hypothesis.

## Theorem J.W3 — Same-color residual witnesses have perfect difference matchings

Let u != v have the same witness color i, and put

\[
h_{uv}=|Q_u\cap Q_v|,\quad
A=Q_u\setminus Q_v,\quad B=Q_v\setminus Q_u.
\]

Then the color-i bipartite graph between A and B contains a perfect matching of size

\[
\boxed{|A|=|B|=r-1-h_{uv}.}
\]

The full witness difference graph between \(T_u\setminus T_v\) and \(T_v\setminus T_u\) likewise contains a perfect matching of size \(r-h_{uv}\).

### Proof

Both \(Q_u,Q_v\) are independent sets of size r-1 in \(G_i[R]\), and \(\alpha(G_i[R])\le r-1\). Their intersection has no color-i edges to either difference set, and each difference set is internally independent. Thus the only color-i edges in \(G_i[Q_u\cup Q_v]\) run between A and B. Its independence number is at most r-1, so the bipartite graph on A union B has independence number at most \(r-1-h_{uv}\). Since it has \(2(r-1-h_{uv})\) vertices, its vertex-cover number is at least \(r-1-h_{uv}\). By König's theorem its matching number is at least that value, hence it has a perfect matching.

The same argument on \(T_u\cup T_v\), using \(\alpha(G_i)\le r\), gives a perfect matching of size r-h_uv between the full symmetric differences.

Consequences:
- If \(Q_u=Q_v\), then the sole possible full-difference matching is the edge uv, so uv must have color i.
- If \(|Q_u\cap Q_v|=r-2\), the two unique residual difference vertices must be joined by a color-i edge. If uv is not color i, the full-difference matching additionally requires both crossed root-to-residual edges to have color i.

## Theorem J.W4 — Edge-ownership inequality without duplicate charging

For a fixed color i, define

\[
\mu_i(x)=|\{v\in C_i:x\in T_v\}|,\qquad
\rho_i(z)=|\{v\in C_i:z\in Q_v\}|\quad(z\in R).
\]

For every color-i edge xy, no witness \(T_v\) contains both endpoints. Hence the edge can occur in selected perfect matchings for at most \(\mu_i(x)\mu_i(y)\) same-color witness pairs. Choosing one perfect matching for every pair gives the exact safe accounting inequality

\[
\boxed{
\sum_{\{u,v\}\subset C_i}(r-h_{uv})
\le \sum_{xy\in E(G_i)}\mu_i(x)\mu_i(y).
}
\]

Using only the residual perfect matchings also gives

\[
\boxed{
\sum_{\{u,v\}\subset C_i}(r-1-h_{uv})
\le \sum_{xy\in E(G_i[R])}\rho_i(x)\rho_i(y).
}
\]

These inequalities explicitly allow one physical edge to serve several witness pairs, with its multiplicity bounded by endpoint incidence. They do **not** yet exceed the available color-edge budget.

## Exact remaining gap

The dichotomy is unconditional in Case B and bypasses the former requirement to find a low-slack vertex in X. It does not yet exclude either branch:

- Branch A gives at least two same-color residual transversals of a near-balanced clique partition of R, with at most r-3 excess edges.
- Branch B gives at least four same-color maximum independent sets in R, a dense overlap graph, and perfect matchings on every pairwise symmetric difference.

A further theorem must exclude one of these graph-level kernels or combine it with the matching pair S_1,S_2 defining X. No full contradiction and no \(\neg P(r)\Rightarrow\neg P(r-1)\) theorem is claimed.


## Theorem J.W5 — Alignment-free residual multinet extraction

Let q=r-1 and retain the Case B setup. There are exactly q colors i!=c. From Theorem J.W1,

\[
\sum_{i\ne c}b_i\le\binom q2,\qquad b_i\ge0.
\]

Call a color residual-low if \(b_i\le q-2\). Every color that is not residual-low has \(b_i\ge q-1\), so there are at most

\[
\left\lfloor\frac{\binom q2}{q-1}\right\rfloor
=\left\lfloor\frac q2\right\rfloor
\]

such colors. Therefore at least \(\lceil q/2\rceil\) colors are residual-low.

For q>=3, each residual-low color i has, by the complement-Turan/Brouwer argument, a partition of R into q nonempty color-i clique blocks. If i and j are two distinct residual-low colors, every j-block is independent in G_i[R] and has size at most q; because q such blocks cover q² points, each has size exactly q. The same applies to i-blocks. A j-block meets each i-block in at most one point and has q points across q i-blocks, so it meets every i-block exactly once.

Hence the residual-low colors define a **q-net with at least ceil(q/2) directions**: R is a q²-point set, and each residual-low color supplies a partition into q blocks of size q, with any two blocks from different partitions intersecting in exactly one point.

This is an unconditional finite-geometry extraction from Case B for every r>=4. It is not a full affine plane: the number of directions is only guaranteed to be at least ceil((r-1)/2), and no theorem yet completes the net or connects its blocks to a shell-hitting lower bound. The construction does not contradict K's Local Slack Gap Theorem, because b_i is an excess on R=V minus X, not the neighborhood slack on V minus {x}.


## Theorem J.W6 — Threshold high-excess interface

In the second branch of J.W2, the repeated witness color i satisfies b_i>=r-2=q-1. If equality b_i=q-1 holds, the exact K-line normal form K.RM4 applies; see K branch commit b20a3dde117facb37e78c2311160a149e578b27c, file general_r/workstreams/finite-geometry-chat-20261024/RESIDUAL_MULTINET_EXTRACTION.md.

Precisely, either G_i[R] is a q-clique partition plus q-1 cross-block color-i edges, or deleting one exceptional residual point leaves q clique blocks (sizes q except one q-1) plus a nonempty star of color-i cross-block edges. In the latter case the exceptional point's residual color-i degree is 2q-2-a for some 1<=a<=q-1.

This imports the exact extremal theorem without copying its proof. It refines the high-color branch to a finite incidence kernel at equality, but does not exclude the kernel. If b_i>=q, this extremal equality classification does not directly apply.


## Theorem J.W7 — Exact r=7 Case B interface

The K branch has closed the residual edge-budget profile when q=r-1=6; see commit eb238d01b9aebf98a7614dba00e2696a2f3d05cf, file general_r/workstreams/finite-geometry-chat-20261024/RESIDUAL_MULTINET_EXTRACTION.md, Theorem K.RM5.

Under Case B at r=7:
- exactly three colors i!=c have b_i=0 and form three pairwise orthogonal 6-clique partitions of R;
- exactly three colors have b_i=5 and are non-6-partite, each at the Kang–Pikhurko exceptional-star threshold;
- G_c[R] is the union of seven c-cliques of sizes 6,5,5,5,5,5,5;
- the 6-clique is a transversal of all three directions, and the six 5-cliques are pairwise disjoint near-transversals.

The witness-color dichotomy then gives either repeated witnesses in a zero-excess direction, or at least four witnesses in one of the three high colors. This is a precise finite kernel for the r=7 Case B, but it remains OPEN whether the one-transversal/six-near-transversal partition can occur together with the three exceptional-star color graphs. This does not close Case A or prove the all-r induction.


## r=7 audit correction — design subkernel is realizable

The K branch has an explicit Latin-square incidence realization of the 3-net plus one-transversal/six-near-transversal partition forced in the r=7 Case B (K commit 825c48ae4e5cc47e7feb6abab6337de62db6fd6c, file Q6_NEAR_TRANSVERSAL_OBSTRUCTION_AUDIT.md). Thus this partition cannot be ruled out by Euler–Tarry alone. It is only an abstract design-level realization, not a full EG617 graph counterexample: the three exceptional-star high-color graphs, root colors, and cross-edges remain to be realized simultaneously or shown impossible.


## Theorem J.W8 — Full-contract contradiction at residual Turan equality

Assume Case B and q=r-1>=4. If

\[
\sum_{i\ne c}b_i=\binom q2,
\]

then, since \(e(G_c[R])=m_q-\sum_{i\ne c}b_i\), the omitted color satisfies

\[
e(G_c[R])=m_q-\binom q2=\frac{q(q-1)^2}{2}.
\]

This is the Turan minimum for a graph on q² vertices with independence number at most q+1. Equality forces G_c[R] to be a disjoint union of q+1 c-cliques with sizes

\[
q,\underbrace{q-1,\ldots,q-1}_{q\text{ blocks}}.
\]

Let these blocks be \(B_0,B_1,\ldots,B_q\), with |B_0|=q and |B_j|=q-1 for j>=1.

### Root-block coverage

For every root x in X, its color-c neighborhood in R contains an entire block B_j. Otherwise choose one non-neighbor of x from every block; the chosen q+1 points form a c-independent set Q, and Q union {x} has r+1=q+2 points but no c-edge, contradiction.

### Capacity of each block

- At most one root can be c-adjacent to every point of B_0. Two such roots x,y make B_0 union {x,y} an (r+1)-set with either only color c (if xy has color c, violating omega(G_c)<=r) or at most two colors (if xy has another color).
- At most two roots can be c-adjacent to every point of any B_j, j>=1. Three such roots x,y,z make B_j union {x,y,z} an (r+1)-set. All edges except the three root-root edges have color c, so at most four colors occur. Since r=q+1>=5, this violates the counterexample condition.

Assign each root one block fully contained in its color-c neighborhood. The block capacities give

\[
|X|\le1+2q<2q+2=|X|,
\]

a contradiction.

Therefore, for every full hypothetical counterexample in Case B and every r>=5,

\[
\boxed{\sum_{i\ne c}b_i\le\binom{r-1}{2}-1.}
\]

This is a graph-level contradiction to the equality case, independent of witness-color alignment and independent of the MOLS classification.

## Corollary J.W9 — Strictly stronger residual-net bound

For q=r-1>=4, every non-q-partite complement \(\overline{G_i[R]}\) costs b_i>=q-1 by Brouwer's threshold. The strict budget in J.W8 therefore implies that at most floor((q-1)/2) of the q residual colors are non-q-partite. Consequently at least

\[
\boxed{\left\lceil\frac{q+1}{2}\right\rceil}
\]

colors give pairwise orthogonal q-clique partitions of R. Equivalently,

\[
N(q)\ge\left\lceil\frac{q+1}{2}\right\rceil-2.
\]

This improves J.W5 by one direction when q is even.

## Corollary J.W10 — Case B is impossible at r=7

For r=7, q=6, J.W9 forces at least four pairwise orthogonal partitions of a 36-point set into six 6-cliques. Four directions yield two mutually orthogonal Latin squares of order 6, which are ruled out by Euler–Tarry. Hence the matching-number-two/tight-transversal Case B cannot occur at r=7.

This does not eliminate Case A (matching number at least three) and therefore does not prove the full r=7 compression implication.


## Audit correction — J.W11 withdrawn

The attempted quantitative extension in commit 5466f79333f0e8b1694c181c2ece4ae907086a37 is **invalid and withdrawn**. The random-transversal step sampled one vertex from each entire clique block, but the required choice must be a color-c nonneighbor of a fixed root in every block. These candidate subsets can be singletons, so the claimed probability bound by \(d/(q-k)^2\) is not justified. A single cross-block c-edge can block all allowed root-nonneighbor transversals when the two candidate sets are its endpoints.

Accordingly, do **not** use the claimed bound \(d\ge \binom{k+1}{2}\), its numerical thresholds, or the implied stronger MOLS count. The valid theorem remains J.W8: only the endpoint \(d=0\) is excluded by the exact Turan-partition/root-capacity argument, giving \(d\ge1\). A stronger quantitative bound requires a separate blocker argument that accounts for the root-dependent candidate sets.
