# Core minimum-degree boundary theorem

Workstream: `general-r-residual-core-extraction-20261024`

Primary status: `PROVED_ANALYTIC`.

External inputs used:

1. Andrasfai--Erdos--Sos for triangle-free graphs: if a triangle-free `n`-vertex graph has minimum degree `>2n/5`, then it is bipartite.
2. Classical Erdos extremal theorem for non-bipartite triangle-free graphs: an `n`-vertex triangle-free non-bipartite graph has at most `floor((n-1)^2/4)+1` edges.

No r=12 Ramsey seed is used.

## Contract

Let `r>=6`. Let `H` be a graph on `3r-1` vertices satisfying

- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- every induced subgraph `X` inherits the least-color cap
  `e(X)<=D_r(|X|)=C(|X|,2)-(r-1)p_r(|X|)`.

The last condition is exactly the hereditary cap supplied by an ambient balanced-coloring counterexample.

## Lemma 1: exact cap values around 2r

For `r<=n<2r`, balanced `r`-part clique-union minimization gives

`p_r(n)=n-r`.

Hence

`D_r(n)=C(n,2)-(r-1)(n-r)`.

In particular

- `D_r(2r)=r^2`;
- `D_r(2r-1)=r(r-1)`.

Status: `PROVED_SYMBOLIC`.

## Lemma 2: 2r exclusion

There is no induced/cap-inheriting graph `X` on `2r` vertices satisfying

- `alpha(X)<=2`;
- `omega(X)<=r-1`.

### Proof

Put `J=bar X`. Then

- `J` is triangle-free because `alpha(X)<=2`;
- `alpha(J)=omega(X)<=r-1`.

From the cap,

`e(X)<=D_r(2r)=r^2`,

so

`e(J)>=C(2r,2)-r^2=r(r-1)`.

Because `J` is triangle-free, every neighborhood in `J` is independent. Since `alpha(J)<=r-1`,

`Delta(J)<=r-1`.

Thus

`e(J)<=2r(r-1)/2=r(r-1)`.

Equality holds. Therefore `J` is `(r-1)`-regular.

For `r>=6`,

`r-1 > 2(2r)/5`.

By Andrasfai--Erdos--Sos, `J` is bipartite. One part of a bipartition of a `2r`-vertex graph has size at least `r`, producing an independent set of size `r` in `J`, contrary to `alpha(J)<=r-1`.

Contradiction.

Status: `PROVED_ANALYTIC`.

## Theorem 3: one-degree-away core minimum degree

Under the contract,

> `delta(H)>=r-1`.

### Proof

Suppose `v in H` has `d_H(v)<=r-2`. Set

`A=H-N_H[v]`.

Then

`|A|=(3r-1)-1-d_H(v)>=2r`.

If `A` contained an independent triple, together with `v` it would form an independent 4-set in `H`; hence `alpha(H[A])<=2`.

Choose any `2r` vertices of `A` and call the induced graph `X`. Then

- `alpha(X)<=2`;
- `omega(X)<=omega(H)<=r-1`;
- `X` inherits the hereditary cap.

This contradicts Lemma 2.

Therefore `delta(H)>=r-1`.

Status: `PROVED_ANALYTIC`.

## Theorem 4: exact near-Mantel compression of the only bad degree

Assume the contract and suppose `v in H` satisfies

`d_H(v)=r-1`.

Set

`A=H-N_H[v]`, so `|A|=2r-1`, and put

`J=bar{H[A]}`.

Then:

1. `J` is triangle-free;
2. `alpha(J)<=r-1`;
3. `J` is non-bipartite;
4. its edge count has only two possibilities:

   `e(J) in {(r-1)^2, (r-1)^2+1}`.

Equivalently,

`e(H[A]) in {r(r-1), r(r-1)-1}`.

### Proof

Triangle-freeness and the independence bound follow exactly as above.

If `J` were bipartite, one bipartition class would have size at least `r` because `|J|=2r-1`, contradicting `alpha(J)<=r-1`. Hence `J` is non-bipartite.

The hereditary cap at `2r-1` gives

`e(H[A])<=D_r(2r-1)=r(r-1)`.

Thus

`e(J)>=C(2r-1,2)-r(r-1)=(r-1)^2`.

The classical Erdos bound for non-bipartite triangle-free graphs gives

`e(J)<=floor((2r-2)^2/4)+1=(r-1)^2+1`.

The conclusion follows.

Status: `PROVED_ANALYTIC`.

## Corollary 5: symbolic defect ledger for a boundary blocker

Retain `d_H(v)=r-1`. Put

- `B=N_H(v)`, so `|B|=r-1`;
- `K=bar H`;
- `epsilon in {0,1}` by `e_K(A)=(r-1)^2+epsilon`;
- for each `b in B`, let `m_b` be the number of **H-edges** from `b` to `A`, equivalently
  `m_b=|A\N_K(b)|`;
- `M=sum_{b in B} m_b`;
- `s=e_K(B)`.

Then:

### (i) Global defect budget

`M-s <= 2r-1+epsilon`.

Proof: `p_r(3r-1)=3r-2`, so the whole-core cap is equivalent to

`e_K(H)>=(r-1)(3r-2)=3r^2-5r+2`.

But exact decomposition gives

`e_K(H)=3r^2-3r+1+epsilon-M+s`.

Rearrange.

### (ii) Per-row bound

For every `b in B`,

`m_b<=r+epsilon`.

Proof: apply the hereditary cap to `A union {b}`, which has `2r` vertices. In complement language its edge count is at least `r(r-1)`. Thus

`e_K(A)+(2r-1-m_b)>=r(r-1)`.

Substitute `e_K(A)=(r-1)^2+epsilon`.

### (iii) Pair obstruction on complement edges inside B

For every `bb' in E(K[B])`,

`m_b+m_{b'}>=r`.

Proof: common `K[A]`-neighbors of `b,b'` have size at least

`(2r-1)-m_b-m_{b'}`.

Because `K` is `K_4`-free (`alpha(H)<=3`), the common `A`-neighborhood of an edge `bb'` is independent in `K[A]`; its size is at most `alpha(K[A])<=r-1`. Rearranging gives the claim.

### (iv) B is not independent in K

`alpha(K[B])<=r-2`, hence `s>=1`.

Proof: `v` is nonadjacent in `K` to every vertex of `B`. An independent `(r-1)`-set in `K[B]` together with `v` would be an independent `r`-set in `K`, equivalently an `r`-clique in `H`, contradicting `omega(H)<=r-1`.

Status of (i)--(iv): `PROVED_SYMBOLIC`.

## Residual-core consequence

The general residual-core minimum-degree problem has therefore been reduced from an arbitrary low-degree obstruction to one exact boundary class:

> For `r>=6`, failure of `delta(H)>=r` forces a vertex of degree exactly `r-1`; its `2r-1` non-neighbors support a non-bipartite triangle-free complement lying within **one edge** of the sharp non-bipartite Mantel ceiling, together with the exact defect ledger above.

This is strictly stronger than the previous state `OPEN: delta(H)>=r`, but it does **not** yet prove `delta(H)>=r`.

## Next target

Eliminate the boundary blocker using the fact that `H` is not an arbitrary capped graph: it is the pivot core of a `4r+1` residual with a degree-`(r+1)` pivot. The shell interface yields additional row constraints recorded in `OPEN_GAPS.md`.