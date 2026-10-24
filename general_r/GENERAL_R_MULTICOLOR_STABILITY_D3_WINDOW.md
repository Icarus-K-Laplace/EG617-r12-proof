# General-r Multicolor Stability and the d3 Near-Extremal Window

Status: **PROVED_SYMBOLIC**, conditional on the general residual-core / near-anchor theorem. External input: Furedi's quantitative Turan stability (`r`-partite deletion distance at most the Turan edge deficit).

## 1. Quantitative one-color setup

Let C be one non-target color graph on

`n=4r+1`

vertices. Its complement J is `K_(r+1)`-free. Write

`e(C)=p_r(4r+1)+t`,

so

`e(J)=ex(4r+1,K_(r+1))-t`.

Furedi's quantitative Turan stability implies that one may delete at most

`m<=t`

edges from J to obtain an r-partite graph H.

Fix such a partition with part sizes

`n_i=4+y_i`, `i=1,...,r`.

Since `sum n_i=4r+1`,

`sum y_i=1`.

Let T be the complete r-partite graph on the same parts. Write

- `delta_p=ex(4r+1,K_(r+1))-e(T)>=0` for the partition imbalance deficit;
- `h=e(T)-e(H)>=0` for missing cross edges of H.

Since `J=H union R` with `|R|=m`,

`ex-t=e(J)=e(T)-h+m`,

so

> **`delta_p+h=t+m`.**

The complement of T is a union of r cliques of sizes `4+y_i`, hence

`delta_p=sum_i C(4+y_i,2)-p_r(4r+1)`
`       =(sum_i y_i^2-1)/2`.

Therefore

> **`sum_i y_i^2=2delta_p+1<=4t+1`.**

Let

`P=sum_(y_i>0)y_i`.

As in the exact-equality calculation, integer `y_i^2>=|y_i|` and `sum y_i=1` give

> **`P<=delta_p+1`.**

Also

> **`max_i y_i^+ <= sqrt(4t+1)`.**

## 2. Degree-sum bound on a target clique

Let B be a target-color clique. Hence B is an independent set in C.

For each part i let

`k_i=|B intersect part_i|`.

Inside one part, every pair of B-vertices is an edge of the clique complement of H, but cannot be an edge of C. Therefore all such pairs must belong to the deleted set R. Hence

> **`sum_i C(k_i,2)<=m<=t`.**

For a B-vertex in part i, its C-degree is at most

`(n_i-1)`

from the within-part clique of `bar(H)`, plus any cross-color edge arising from a missing cross edge of H.

Since a cross edge of C has at most one endpoint in B, summing over B gives

`sum_(x in B)d_C(x)`
` <= 3|B| + sum_i k_i y_i + h`.

Discard negative y terms. For k>=1,

`k<=1+C(k,2)`.

Thus

`sum_i k_i y_i^+`
` <=P + (max y_i^+) sum_i C(k_i,2)`
` <=delta_p+1 + m sqrt(4t+1)`.

Using `delta_p+h=t+m`,

`sum_(x in B)(d_C(x)-3)`
` <=1+t+m+m sqrt(4t+1)`
` <=1+2t+t sqrt(4t+1)`.

Therefore:

> **One-color stability incidence bound**
>
> `sum_(x in B)(d_C(x)-3) <= 1+2t+t sqrt(4t+1)`.

For t=0 this specializes to the exact unique-5-block capacity one.

## 3. Multicolor regular-clique bound

Return to the r-coloring and let F be the target residual. Put

`epsilon=D_r(4r+1)-e(F)`.

For the other colors C_j write their excesses as t_j. Edge partition gives

`sum_j t_j=epsilon`.

Assume B is a target clique whose every vertex has target degree `r+1`. Then every x in B has total non-target degree

`3r-1`.

Relative to baseline three in each of the `r-1` non-target colors, the total degree excess over all x in B is exactly

`2|B|`.

Apply the one-color bound and use

`sum t_j=epsilon`,

`sum t_j sqrt(4t_j+1) <= epsilon sqrt(4epsilon+1)`.

This gives

> **`2|B| <= (r-1)+2epsilon+epsilon sqrt(4epsilon+1)`.**

Equivalently

> **`|B| <= [r-1+2epsilon+epsilon sqrt(4epsilon+1)]/2`.**

This is a fixed-deficit multicolor Turan-stability obstruction for regular target cliques.

## 4. Common-S shell consequence

For a d3 common-S family, the regular-clique extraction from

`{p} union (A\S)`

gives a regular target clique of size at least

`r-1-B_shell`,

where `B_shell=e_M(L)+G_L`.

Therefore

`B_shell >= [r-1-2epsilon-epsilon sqrt(4epsilon+1)]/2`.

Assume the general near-anchor theorem `K_r>=8`. At residual edge layer

`e(F)=D_r(4r+1)-epsilon`,

the backend identity gives

> **`q<=3r-1-epsilon`.**

For d3,

`q=3r-6+a+B_shell`,

so necessarily

`B_shell<=5-epsilon`.

The two inequalities are incompatible whenever

> **`r>11+epsilon sqrt(4epsilon+1)`.**

Hence:

> **Fixed-deficit d3 exclusion.** For every fixed epsilon, all sufficiently large r admit no regular d3 shell vertex in the residual edge layer `D_r(4r+1)-epsilon`.

## 5. Asymptotic window

The sufficient condition is asymptotically

`2 epsilon^(3/2) < r`.

Consequently the exclusion holds uniformly whenever

> **`epsilon=o(r^(2/3))`.**

Thus an `o(r^(2/3))`-wide band below the maximum residual edge layer is completely free of scalable d3 support geometry, conditional only on the residual-core extraction and the general near-anchor theorem.

This is the first quantitative large-r width theorem in the general-r programme.

## 6. External input

The quantitative stability input is the theorem commonly attributed to Furedi: a `K_(r+1)`-free graph with `ex(n,K_(r+1))-t` edges can be made r-partite by deleting at most t edges. It is discussed, for example, in the literature on making `K_(r+1)`-free graphs r-partite.
