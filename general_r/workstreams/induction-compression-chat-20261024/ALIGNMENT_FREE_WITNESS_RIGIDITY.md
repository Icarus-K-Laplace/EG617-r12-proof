# Alignment-Free Witness Rigidity: Residual Budget and Color Dichotomy

Status: **PROVED alignment-free dichotomy; global contradiction remains OPEN.**

This note uses the already-established Case B contract only. It does not assume a low-slack vertex in X.

## Setup

Let H_{-c} have matching number two and transversal number 2r. Let X be the union of a maximum matching, so |X|=2r, and let R=V\X, |R|=(r-1)^2. For each v in X choose a private witness

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

This is an unconditional finite-geometry extraction from Case B for every r>=4. It is not a full affine plane: the number of directions is only guaranteed to be at least ceil((r-1)/2), and no theorem yet completes the net or connects its blocks to a shell-hitting lower bound. The construction does not contradict K's Local Slack Gap Theorem, because b_i is an excess on R=V\\X, not the neighborhood slack on V\\{x}.
