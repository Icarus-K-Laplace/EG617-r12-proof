# General residual-core minimum-degree theorem

Workstream: `general-r-residual-core-extraction-20261024`

Primary status: **`PROVED_ANALYTIC`**.

Headline result:

> For every `r>=17`, the hereditary least-color cap together with
> `|H|=3r-1`, `alpha(H)<=3`, and `omega(H)<=r-1` already forces
> **`delta(H)>=r`**.

This proves the load-bearing minimum-degree clause of the general residual-core contract for all `r>=17`. It uses no r=12 Ramsey seed and no backend d2/d3/support machinery.

External inputs used:

1. Andrasfai--Erdos--Sos for triangle-free graphs: if a triangle-free `n`-vertex graph has minimum degree `>2n/5`, then it is bipartite.
2. Classical Erdos non-bipartite Mantel refinement: if a triangle-free `n`-vertex graph is non-bipartite, then
   `e<=floor((n-1)^2/4)+1`.

## Contract

Let `H` be a graph on `3r-1` vertices satisfying

- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- every induced subgraph `X` inherits the least-color cap

  `e_H(X)<=D_r(|X|)=C(|X|,2)-(r-1)p_r(|X|)`.

Equivalently, with `K=bar H`, every induced `X` satisfies

`e_K(X)>=(r-1)p_r(|X|)`.

The contract is exactly what an induced pivot core inherits from a full balanced-coloring counterexample, except that no minimum-degree hypothesis is assumed.

---

## Lemma 1. Exact cap below 2r

For `r<=n<2r`,

`p_r(n)=n-r`,

hence

`D_r(n)=C(n,2)-(r-1)(n-r)`.

In complement form:

> every `n`-vertex induced subgraph of `K` with `r<=n<2r` has at least
> `(r-1)(n-r)` edges.

In particular

- `D_r(2r)=r^2`;
- `D_r(2r-1)=r(r-1)`.

Status: `PROVED_SYMBOLIC`.

---

## Lemma 2. The 2r exclusion

For `r>=6`, there is no cap-inheriting graph `X` on `2r` vertices with

- `alpha(X)<=2`;
- `omega(X)<=r-1`.

### Proof

Put `J=bar X`. Then `J` is triangle-free and `alpha(J)<=r-1`.

The cap gives

`e(J)>=C(2r,2)-D_r(2r)=r(r-1)`.

Every neighborhood in a triangle-free graph is independent, so

`Delta(J)<=alpha(J)<=r-1`,

and therefore

`e(J)<=r(r-1)`.

Thus equality holds and `J` is `(r-1)`-regular. For `r>=6`,

`r-1>2(2r)/5`.

Andrasfai--Erdos--Sos forces `J` to be bipartite. One bipartition class has at least `r` vertices, contradicting `alpha(J)<=r-1`.

Status: `PROVED_ANALYTIC`.

---

## Lemma 3. First minimum-degree lift

For `r>=6`, the core contract forces

> `delta(H)>=r-1`.

### Proof

If `d_H(v)<=r-2`, then

`A:=H-N_H[v]`

has at least `2r` vertices. Since `alpha(H)<=3`, one has `alpha(H[A])<=2`: an independent triple in `A` together with `v` would be an independent 4-set.

Any induced `2r`-subset of `A` therefore violates Lemma 2.

Status: `PROVED_ANALYTIC`.

Thus the only possible failure of the target `delta(H)>=r` is the exact boundary

`d_H(v)=r-1`.

---

## Lemma 4. Near-Mantel boundary compression

Assume `d_H(v)=r-1`. Put

- `A=H-N_H[v]`, so `|A|=2r-1`;
- `J=bar{H[A]}`.

Then

1. `J` is triangle-free;
2. `alpha(J)<=r-1`;
3. `J` is non-bipartite;
4. for some `epsilon in {0,1}`,

   `e(J)=(r-1)^2+epsilon`.

### Proof

Triangle-freeness follows from `alpha(H)<=3`; the independence bound is `omega(H[A])<=r-1`.

If `J` were bipartite, a bipartition class would have at least `r` vertices because `|A|=2r-1`, contradicting `alpha(J)<=r-1`.

The cap on `A` gives

`e(H[A])<=D_r(2r-1)=r(r-1)`,

so

`e(J)>=(r-1)^2`.

The Erdos non-bipartite triangle-free bound gives

`e(J)<=floor((2r-2)^2/4)+1=(r-1)^2+1`.

Status: `PROVED_ANALYTIC`.

---

## Lemma 5. Exact C5 + near-complete-bipartite structure

Let `r>=6`, write `m=r-3`, and retain the boundary setup of Lemma 4.

Let `C` be a shortest odd cycle of `J`. Then:

> `C` is a 5-cycle.

Put `U=A\V(C)`, so `|U|=2m=2r-6`. Every vertex of `U` has at most two neighbors on `C`. Define

- `c := 2|U|-e_J(C,U) >=0`;
- `t := m^2-e_J(U) >=0`.

Then the exact identity

> `c+t=1-epsilon`

holds.

Consequently the boundary graph has only the following three structural forms.

### Type I: epsilon=1

- `c=t=0`;
- `J[U]=K_{m,m}`;
- every vertex of `U` has exactly two neighbors on `C`.

### Type II: epsilon=0, c=1, t=0

- `J[U]=K_{m,m}`;
- exactly one unit of the possible `2|U|` incidences from `U` to `C` is missing; equivalently exactly one vertex has one `C`-neighbor and every other vertex has two.

### Type III: epsilon=0, c=0, t=1

- every vertex of `U` has exactly two neighbors on `C`;
- `e(J[U])=m^2-1`;
- `J[U]` is bipartite and is either
  - `K_{m,m}` minus one edge, or
  - `K_{m-1,m+1}`.

### Proof

Let the shortest odd cycle have length `ell>=5`. It is induced. A vertex outside a shortest odd cycle has at most two neighbors on it: three neighbors would give either a triangle or a shorter odd cycle.

Thus, with `q=|A|-ell`,

`e(J)<=ell+2q+floor(q^2/4)`.

If `ell=2k+1>=7`, then `q=2r-2k-2` and

`(r-1)^2-[ell+2q+q^2/4]
 =2r(k-2)-k^2+3>0`

whenever the cycle fits. This contradicts `e(J)>=(r-1)^2`. Hence `ell=5`.

Now `|U|=2m`. Mantel gives `e(J[U])<=m^2`, while the shortest-cycle argument gives `e(C,U)<=2|U|`. Therefore

`e(J)<=5+4m+m^2=(r-1)^2+1`.

Comparing with `e(J)=(r-1)^2+epsilon` gives exactly

`c+t=1-epsilon`.

If `t=0`, equality in Mantel gives `J[U]=K_{m,m}`.

If `t=1`, then `e(J[U])=m^2-1`. A non-bipartite triangle-free graph on `2m` vertices has at most `m^2-m+1` edges by the same Erdos theorem; for `m>=3`, this is strictly below `m^2-1`. Hence `J[U]` is bipartite. If its parts have sizes `x,2m-x`, then

`x(2m-x)>=m^2-1`,

so `|x-m|<=1`. Equality of the actual edge count yields exactly the two listed possibilities.

Status: `PROVED_ANALYTIC`.

This is the finite-width structure that replaces an uncontrolled near-Mantel obstruction.

---

## Lemma 6. Constant row-defect bound

Let

`B=N_H(v)`, so `|B|=r-1`,

and continue to write `K=bar H`. For `b in B`, define the A-row defect

`m_b := |A\N_K(b)|`,

i.e. the number of H-edges from `b` into `A`.

For `r>=9`, the unbalanced Type-III subcase `J[U]=K_{m-1,m+1}` is impossible.

In every remaining Type-I/II/III subcase,

> `m_b<=8` for every `b in B`.

### Proof: excluding K_{m-1,m+1}

Let the larger side be `Q`, so `|Q|=m+1=r-2`. Every vertex of `Q` has exactly two neighbors on `C`, and `Q` is independent. Hence

`e_K(C union Q)=5+2(r-2)=2r+1`.

For any `b in B`, the induced set

`S=C union Q union {b}`

has size `r+4<2r` for `r>=9`; the hereditary cap in complement form requires

`e_K(S)>=4(r-1)=4r-4`.

But even if `b` is adjacent to every vertex of `C union Q`,

`e_K(S)<=2r+1+(r+3)=3r+4<4r-4`

for `r>=9`, contradiction.

### Proof: balanced cases

Let `P,Q` be the two balanced sides, each of size `m=r-3`.

For each side `P`, the set `C union P` has `r+2` vertices and

`e_K(C union P)>=2r-2`;

indeed it has `2r-1` edges unless it contains the unique one-incidence-defect vertex of Type II, in which case it has `2r-2`.

Now add `b`. The set

`S=C union P union {b}`

has size `r+3`, so the hereditary cap requires

`e_K(S)>=3(r-1)=3r-3`.

Thus `b` misses at most four vertices of `C union P` (at most three in the one-defect side). The same holds with `Q`.

If `c_b,p_b,q_b` are the numbers of K-nonneighbors of `b` in `C,P,Q`, then

`c_b+p_b<=4`,
`c_b+q_b<=4`.

Therefore

`m_b=c_b+p_b+q_b<=8-c_b<=8`.

Status: `PROVED_ANALYTIC`.

---

## Lemma 7. Every complement edge in B demands r row defects

For every edge `bb' in E(K[B])`,

> `m_b+m_{b'}>=r`.

### Proof

The two vertices have at least

`|A|-m_b-m_{b'}=2r-1-m_b-m_{b'}`

common K-neighbors in `A`.

Because `K` is `K_4`-free (`alpha(H)<=3`), the common A-neighborhood of the K-edge `bb'` must be independent in `K[A]=J`. Since

`alpha(J)=omega(H[A])<=r-1`,

we get

`2r-1-m_b-m_{b'}<=r-1`,

hence the claim.

Status: `PROVED_SYMBOLIC`.

---

## Lemma 8. B must contain a complement edge

`E(K[B])` is nonempty.

### Proof

The vertex `v` is K-nonadjacent to every vertex of `B`. If `B` were independent in `K`, then `{v} union B` would be an independent set of size `r` in `K`, equivalently an `r`-clique in `H`, contradicting `omega(H)<=r-1`.

Status: `PROVED_SYMBOLIC`.

---

# Main theorem: delta(H) >= r for r >= 17

## Statement

Let `r>=17`. If `H` has `3r-1` vertices and satisfies

- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- the inherited least-color cap on every induced subgraph,

then

> **`delta(H)>=r`.**

Status: **`PROVED_ANALYTIC`**.

## Proof

Lemma 3 gives `delta(H)>=r-1`.

Suppose equality occurs at `v`. Lemmas 4--6 give the exact boundary decomposition and the uniform bound

`m_b<=8` for every `b in B=N_H(v)`.

Lemma 8 supplies an edge `bb' in K[B]`. Lemma 7 then requires

`r<=m_b+m_{b'}<=16`,

contradicting `r>=17`.

Therefore the boundary degree `r-1` cannot occur and `delta(H)>=r`.

---

## Strength and scope

- independent of r=12 arithmetic: **yes**;
- requires `r>=17`: **yes**;
- external theorems: AES triangle-free minimum-degree theorem and Erdos non-bipartite Mantel refinement;
- requires a `4r+1` residual or a shell hypothesis: **no**;
- requires backend support/d2/d3 machinery: **no**;
- uses full inherited multicolor hereditary cap: **yes**.

This is stronger than the originally requested local target: once a `3r-1` pivot core with the two clique/independence constraints is extracted from the full coloring, its missing minimum-degree clause is automatic for every `r>=17`.

## Remaining range

The proof leaves `6<=r<=16` unresolved at the exact boundary. That finite range is irrelevant to an “all sufficiently large r” residual-core theorem, but can be audited separately if an all-r statement is later required.