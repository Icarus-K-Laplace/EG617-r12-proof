# Kang-Pikhurko Equality Classification at `5r+1`, translated to color-graph language

Status: **EXTERNAL_THEOREM_TRANSLATION / VERIFIED_SOURCE**. The classification is Kang–Pikhurko (2005), Theorem 4 + Lemma 5. The deductions below are elementary complements of their construction.

## 1. Equality regime

Let C be a graph on

`n=5r+1`

with

`alpha(C)<=r`, `omega(C)<=5`,

and minimum possible edge count under these two constraints:

`e(C)=p_r(5r+1)+4=10r+9`.

Then J=bar(C) is a non-r-partite `K_(r+1)`-free graph with

`e(J)=t_r(5r+1)-4`,

which is exactly the Brouwer/Kang-Pikhurko equality layer.

Kang–Pikhurko Theorem 4 says every equality graph J is one of their graphs `G(n_1,...,n_r)`. Lemma 5 classifies the optimal part-size sequences.

## 2. The only part-size sequences at n=5r+1

Their sequence has r positive integers

`n_1<=...<=n_r`,

summing to `n-1=5r`, and satisfying

`n_1>=2`, `n_2<=n_1+1`, `n_r<=n_1+2`, `n_r<=n_3+1`.

Since the average is exactly5, these conditions force precisely three possibilities:

> **Type I:** `(5,5,...,5)`;
>
> **Type II:** `(4,5,...,5,6)`;
>
> **Type III:** `(4,4,5,...,5,6,6)`.

Proof: if `n_1>=5`, the average forces all entries to be5. If `n_1=4`, every entry lies in {4,5,6}; the numbers of 4s and6s must agree. Three or more 4s would give `n_3=4`, and then `n_r<=n_3+1=5`, excluding any6. Hence there are one or two 4s. Values `n_1<=3` are incompatible with average5 and the range conditions.

## 3. Complement color-graph gadget

In the KP construction choose the first two nontrivial parts `N_s,N_t`; here these are `N_1,N_2`. Let `A*` be a nonempty proper subset of `N_1`, let `y in N_2`, and let x be the added exceptional vertex.

In the color graph C=bar(J):

- every N_i induces a clique;
- there are no cross edges except:
  - y is joined to every vertex of A*;
  - x is joined to `N_1\A*` and `N_2\{y}`.

Thus all nontriviality is confined to

`N_1 union N_2 union {x}`;

every part `N_i`, i>=3, is an isolated clique component in C.

## 4. Degree distributions

Every vertex has C-degree at least4.

Moreover the total degree excess over4 is always

`sum_v(d_C(v)-4)=2(10r+9)-4(5r+1)=14`.

The three sequence types realize this14-unit excess as follows.

### Type I: all parts size5

Let `a=|A*|`, `1<=a<=4`.

- x has degree `9-a`;
- all five vertices of N1 have degree5;
- four vertices of `N2\{y}` have degree5;
- y has degree `4+a`;
- all `5(r-2)` vertices in parts i>=3 have degree4.

Hence at least `5(r-2)` vertices are ordinary degree4 vertices lying in isolated C-K5 components.

### Type II: sizes `(4,5^(r-2),6)`

Here `1<=a<=3`.

- x has degree `8-a`;
- all four N1 vertices have degree4;
- the four vertices `N2\{y}` have degree5;
- y has degree `4+a`;
- the K6 part contributes six degree5 vertices;
- all vertices in the remaining ordinary K5 parts have degree4.

There are `5(r-3)` ordinary degree4 vertices in isolated K5 components; the only additional degree4 vertices lie in the exceptional N1 gadget.

### Type III: sizes `(4,4,5^(r-4),6,6)`

Here `1<=a<=3`.

- x has degree `7-a`;
- all four N1 vertices have degree4;
- three vertices of `N2\{y}` have degree4;
- y has degree `3+a`;
- the two K6 parts contribute twelve degree5 vertices;
- all `5(r-4)` vertices in ordinary K5 parts have degree4.

Depending on a, x or y may also have degree4. Again every vertex has degree at least4.

## 5. r=12 high-layer consequence

For a 61-point target residual with target edge count E, the total excess of the eleven non-target colors above their constrained minimum129 is

`411-E`.

Therefore:

- E=408: total excess3, so at least8 non-target colors are exact KP equality colors;
- E=407: total excess4, so at least7 are exact;
- E=406: total excess5, so at least6 are exact.

Each exact color has minimum degree4 and at least40 ordinary degree4 vertices lying in isolated K5 components (the Type III worst case for r=12).

For a target vertex v,

`sum_(j!=target)d_j(v)=60-d_F(v)`.

In particular a target degree13 vertex has total non-target degree47, only three above the baseline `11*4=44`. Hence among exact colors it can be exceptional/high in very few of them. Combining this with the ordinary-K5 incidence counts is a promising local route for E407/E408.

## 6. Source

M. Kang and O. Pikhurko, *Maximum K_{r+1}-free graphs which are not r-partite*, Matematychni Studii 24 (2005), 12–20, Theorem 4 and Lemma 5, DOI 10.30970/ms.24.1.12-20.
