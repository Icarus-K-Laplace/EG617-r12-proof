# Residual branch closure for r >= 17

Status: **`PROVED_ANALYTIC`**.

Dependency: `CORE_MINDEG_BOUNDARY_THEOREM.md`.

This file proves that once an induced `4r+1` residual with the expected hereditary constraints is obtained, the entire desired pivot/core contract follows automatically for `r>=17`.

## Theorem 1. 3r exclusion

Let `r>=17`. There is no graph `X` on `3r` vertices satisfying

- `alpha(X)<=3`;
- `omega(X)<=r-1`;
- every induced subgraph inherits the least-color cap `D_r`.

### Proof

Delete any vertex `u`. The graph

`H=X-u`

has `3r-1` vertices and satisfies the hypotheses of the general residual-core minimum-degree theorem. Hence

`delta(H)>=r`.

Fix any vertex `v in X`. First, deleting any other vertex shows `d_X(v)>=r`, so `v` has a neighbor. Now delete a neighbor `u of v`; then

`d_X(v)-1=d_{X-u}(v)>=r`.

Thus

`delta(X)>=r+1`.

The cap at order `3r` is exact:

`p_r(3r)=3r`,

so

`D_r(3r)=C(3r,2)-3r(r-1)=3r(r+1)/2`.

The minimum-degree bound gives the reverse inequality

`e(X)>=3r(r+1)/2`.

Hence equality holds and `X` is `(r+1)`-regular.

Put `L=bar X`. Then

- `|L|=3r`;
- `L` is `(2r-2)`-regular;
- `L` is `K_4`-free because `alpha(X)<=3`;
- `alpha(L)=omega(X)<=r-1`.

For `r>=17`,

`2r-2 > 5(3r)/8`.

The Andrasfai--Erdos--Sos theorem for `K_4`-free graphs forces `L` to be 3-partite. One part then has at least `r` vertices, contradicting `alpha(L)<=r-1`.

Status: `PROVED_ANALYTIC`.

External theorem used: Andrasfai--Erdos--Sos (`K_4`-free minimum-degree threshold `>5n/8` implies 3-partite).

---

## Theorem 2. Automatic minimum degree of a 4r+1 residual

Let `r>=17`. Let `F` be a graph on `4r+1` vertices satisfying

- `alpha(F)<=4`;
- `omega(F)<=r-1`;
- the inherited least-color cap on every induced subgraph.

Then

> `delta(F)>=r+1`.

### Proof

Suppose `d_F(v)<=r`. Then

`A=F-N_F[v]`

has

`|A|=4r-d_F(v)>=3r`.

Since `alpha(F)<=4`, the non-neighborhood `A` has `alpha(A)<=3`: an independent 4-set in `A` together with `v` would give an independent 5-set in `F`.

Choose any induced `3r`-vertex subset `X of A`. It satisfies

- `alpha(X)<=3`;
- `omega(X)<=r-1`;
- the hereditary cap.

This contradicts Theorem 1.

Status: `PROVED_ANALYTIC`.

---

## Theorem 3. A degree-(r+1) pivot exists

Under the hypotheses of Theorem 2,

> `delta(F)=r+1`.

In particular there exists a legal degree-`(r+1)` pivot `p`.

### Proof

The cap at `4r+1` is

`p_r(4r+1)=6r+4`,

hence

`D_r(4r+1)
 =C(4r+1,2)-(r-1)(6r+4)
 =2r^2+4r+4`.

If every vertex had degree at least `r+2`, then

`e(F)>= (4r+1)(r+2)/2`.

The excess over the cap is

`(4r+1)(r+2)/2-(2r^2+4r+4)=(r-6)/2>0`.

Contradiction for `r>=17`. Combined with Theorem 2, `delta(F)=r+1`.

Status: `PROVED_SYMBOLIC` once Theorem 2 is available.

---

# Main residual-branch theorem

Let `r>=17`. Suppose an induced residual `F` has

`|F|=4r+1`,
`alpha(F)<=4`,
`omega(F)<=r-1`,

and inherits the least-color cap from the full counterexample.

Then there exists a vertex `p` with

`d_F(p)=r+1`.

Define

`H=F-N_F[p]`.

Then

- `|H|=3r-1`;
- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- `delta(H)>=r`.

### Proof of the inherited alpha bound

The order identity is immediate. Every vertex of `H` is nonadjacent to `p`. If `H` contained an independent 4-set, adding `p` would produce an independent 5-set in `F`, contradicting `alpha(F)<=4`.

The clique bound and hereditary cap are inherited.

The minimum degree `delta(H)>=r` is exactly the theorem of `CORE_MINDEG_BOUNDARY_THEOREM.md`.

Status: **`PROVED_ANALYTIC` for every `r>=17`**.

## Meaning for the program

The load-bearing residual branch is now closed once the `4r+1` residual itself is extracted. No r=12 recurrence seed is needed for

- `delta(F)>=r+1`;
- existence of the exact degree-`(r+1)` pivot;
- `delta(H)>=r`.

Therefore the remaining front-end problem is sharply upstream:

> force a normalized `4r+1` K_r-free residual, or prove that maximal block extraction stops at a rigid `5r+1` terminal.

That is now the only general-r extraction obstruction.