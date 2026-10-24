# Symbolic Front Recurrence

Status: **PROVED AS AN ABSTRACT TERMINATING RECURRENCE; quantitative seed dominance open**.

## 1. General-r contextual state

Fix `r>3` and a least-edge color graph G from a hypothetical counterexample on `r^2+1` vertices. On every vertex set W, define the inherited cap

`D_r(|W|)=C(|W|,2)-(r-1)p_r(|W|)`,

where `p_a(n)` is the Turan-complement lower bound for an n-vertex graph with independence number at most a.

After maximal target-`K_r` block packing, the residual contextual classes have clique number at most `r-1`. Define

`C_r(a,n)={ induced J<=G : |J|=n, alpha(J)<=a, omega(J)<=r-1, all inherited D_r caps hold }`.

Let `B_r(a,n)` be any certified lower edge floor for this class, and

`M_r(a)=max{n : C_r(a,n) is not certified empty}`.

For the extraction reductio, additionally impose contextual emptiness `C_r(4,n)=empty` for `n>=4r+1`.

## 2. Symbolic local recurrence

Take `J in C_r(a,n)` and a minimum-degree pivot p of degree h. Put

`A=N_J(p)`, `C=J-N[p]`, `m=n-h-1`, `M=bar(J[A])`.

Then

`alpha(C)<=a-1`, `alpha(M)<=r-2`.

For `v in A`, set

`g_v=d_J(v)-h>=0`, `t_v=|N_C(v)|`, `z=e(M)`, `q=z+sum_A g_v`.

The exact identities are

`t_v=d_M(v)+g_v`,
`e(J)=C(h+1,2)+q+e(C)`.

The common shell floor is

`Z_r(h)=max(p_(r-2)(h), C(h+1,2)-D_r(h+1), C(h,2)-D_r(h))`.

Thus `q>=Z_r(h)`.

### Pair/matching layer

If `h>=r-1`, M contains an edge. Define

`beta=max(0,m-M_r(a-2))`.

Then any M-edge has core-row union at least beta, giving `q>=beta-1`; if

`B_r(a-1,m)+beta>D_r(m+2)`,

that h-row is impossible.

A maximum matching in M leaves an independent set of size at most `r-2`, hence

`k_0(r,h)=ceil((h-r+2)/2)`

matching edges are guaranteed. Any stronger shell-cap theorem may replace `k_0` by a certified `k_r(h)>=k_0`; this isolates the r=12 shell-size upgrades from the recurrence architecture.

For `1<=t<=k_r(h)`,

`q>=t beta-C(2t,2)+p_a(2t)`.

### Triangle layer

If M is triangle-free, for the same t,

`q>=t beta-t^2`.

If M has a triangle and `a>=3`, define

`gamma=max(0,m-M_r(a-3))`.

The triangle alternative gives `q>=gamma-3`, provided

`B_r(a-1,m)+gamma<=D_r(m+3)`.

If this density condition fails, the triangle alternative is discarded. For `a=2`, only the triangle-free alternative survives.

Let `Q_r(a,n,h)` be the minimum of the surviving triangle-free/triangle alternatives after taking the maximum with all common q-floors.

### Row and node update

For every surviving h-row,

`L_h=max(ceil(nh/2), B_r(a-1,m)+C(h+1,2)+Q_r(a,n,h))`.

Define

`DEL_r(a,n)=ceil(n B_r(a,n-1)/(n-2))` for `n>2`.

Given any finite external seed floor `S_r(a,n)`, set

`B_r(a,n)=max(p_a(n), DEL_r(a,n), S_r(a,n), min_h L_h)`.

If there is no surviving h-row or the resulting floor exceeds `D_r(n)`, certify `C_r(a,n)=empty`.

## 3. Conditional symbolic termination theorem

> **Theorem (front recurrence termination).** Fix `r>3`, a finite order limit N, the cap `D_r`, and any finite seed/cutoff package whose entries refer only to already declared base states. Evaluating the recurrence in increasing a and, within each a, increasing n terminates after finitely many states and yields a sound contextual lower-floor/emptiness certificate on all `(a,n)` with `a<=r`, `n<=N`.

Proof: every recurrence dependency is either `(a,n-1)` or has strictly smaller a. Pair and triangle coverage query only `M_r(a-2)` and `M_r(a-3)`, which are determined before row a is processed. All remaining operations are finite maxima/minima of integers. Hence the dependency graph is acyclic.

This proves H2 in the requested conditional sense for every `r>3`; it does **not** supply the quantitative seeds required to eliminate the outer states.

## 4. Symbolic outer budget

Let

`mu_r=r(r^2+1)/2`

be the least-color edge upper bound. For an anchor of degree d and an inclusion-maximal packing of j target `K_r` blocks in its nonneighborhood, the residual has

`a=r-1-j`,
`n=r^2-d-jr`.

The exact anchor ledger implies the universal upper budget

`U_r(d,j)=mu_r-C(d+1,2)-j C(r,2)`,

with further embedding charges only decreasing the actual residual edge count.

For every `r>3`, the anchor minimum degree satisfies `d<=r-1`: average degree is at most r; if `d=r`, the least-color graph is r-regular. Brooks' theorem gives an r-coloring of every component (the forbidden `K_(r+1)` exception cannot occur, and r>3 excludes the odd-cycle exception), producing an independent set of size at least `ceil((r^2+1)/r)=r+1`, contradiction.

At the terminal anchor degree `d=r-1`,

- `j=r-5` gives `(a,n)=(4,4r+1)`;
- `j=r-6` gives `(a,n)=(5,5r+1)`.

## 5. Conditional extraction theorem

Assume the contextual exclusion of `(4,4r+1)` and assume the recurrence closure of a seed package satisfies

`B_r(r-1-j, r^2-d-jr) > U_r(d,j)`

for every admissible outer pair `(d,j)` except `(d,j)=(r-1,r-6)` and the excluded extraction coordinate `(r-1,r-5)`.

Then every hypothetical counterexample forces exactly the dichotomy

`(4r+1) residual  OR  (5r+1) design-like terminal`.

Thus H4 has been reduced to a finite family of symbolic budget inequalities. The open problem is to prove those inequalities uniformly in r from a small seed envelope.

## 6. Structurally sufficient seed interface

The r=12 certificate uses only the following low-a numerical information beyond automatic bases:

- maximum order at `a=2`: `2r-1` when r=12;
- maximum order at `a=3`: `3r` when r=12;
- contextual maximum order at `a=4`: `4r` under no extraction;
- five edge floors at `(2,2r-1)`, `(3,3r-1)`, `(3,3r)`, `(4,4r-1)`, `(4,4r)`.

At r=12 these are exactly 131,210,234,284,308.

This five-floor/two-cutoff interface is a **structurally sufficient template**, not yet proved minimal among all possible general-r seed packages. Finding asymptotic formulas strong enough for its entries is the unique quantitative blocker to H3/H4.
