# General-r Near-Equality Multicolor Regular-Clique Obstruction

Status: **PROVED_SYMBOLIC for target hereditary deficit epsilon<=2**, using Brouwer's exact Turan stability theorem.

## 1. Setup

Let R have `n=4r+1` vertices inside a hypothetical balanced r-colouring. Fix a target color F and define its hereditary-cap deficit

`epsilon = D_r(4r+1)-e(F) >=0`.

For each of the other `r-1` colors C_j, write

`e(C_j)=p_r(4r+1)+s_j`,

where `s_j>=0`. Since the color classes partition all pairs,

> **`sum_j s_j=epsilon`.**

Assume `epsilon<=2`.

## 2. Brouwer forces clique partitions in every other color

The complement `J_j=bar(C_j)` is `K_(r+1)`-free and

`e(J_j)=ex(4r+1,K_(r+1))-s_j`.

Brouwer's exact stability theorem states that for `n>=2r+1`, every `K_(r+1)`-free graph with at least

`ex(n,K_(r+1))-floor(n/r)+2`

edges is r-partite.

Here `n=4r+1`, so `floor(n/r)=4`. Since `s_j<=epsilon<=2`, every J_j is r-partite.

Therefore every C_j is a disjoint union of r cliques.

Let their sizes be

`4+y_1,...,4+y_r`.

Then

`sum_i y_i=1`.

Moreover

`sum_i C(4+y_i,2)=6r+(7+sum_i y_i^2)/2`.

Since `p_r(4r+1)=6r+4`,

> **`sum_i y_i^2=2s_j+1`.**

Put

`P_j=sum_(y_i>0)y_i`.

Writing `N_j=-sum_(y_i<0)y_i`, one has `P_j-N_j=1`. Since every nonzero integer y satisfies `y^2>=|y|`,

`2s_j+1=sum y_i^2 >= P_j+N_j=2P_j-1`.

Hence

> **`P_j<=s_j+1`.**

This avoids any case classification of the near-balanced clique sizes.

## 3. Regular target clique incidence bound

Let B be a target-color clique all of whose vertices have target degree exactly `r+1` inside F.

Fix `x in B`. Its non-target degree on R is

`4r-(r+1)=3r-1`.

In color C_j, if x lies in a clique block of size `4+y`, then that color contributes exactly `3+y` non-target neighbours of x.

Across the `r-1` non-target colors, the baseline contribution is `3(r-1)=3r-3`. Therefore x must accumulate total assigned y-mass exactly2:

`sum_j y_j(x)=2`.

Summing over x in B gives total required assigned y-mass `2|B|`.

Because B is a target clique, any clique block of a non-target color contains at most one B-vertex. Hence in color j the assigned y-mass over all vertices of B is at most the total positive y-mass `P_j`.

Therefore

`2|B| <= sum_j P_j <= sum_j(s_j+1)`
`       =(r-1)+epsilon`.

Thus:

> **Near-equality regular-clique obstruction**
>
> `|B| <= floor((r-1+epsilon)/2)` for every `epsilon<=2`.

For epsilon=0 this recovers `GENERAL_R_MULTICOLOR_EQUALITY_CLIQUE_OBSTRUCTION.md`.

## 4. Common-S B-floor with deficit epsilon

For a common-S family of support size d, `GENERAL_R_COMMON_S_EQUALITY_B_FLOOR.md` extracts a regular target clique of size at least

`r+2-d-B_shell`,

where

`B_shell=e_M(L)+G_L`.

Therefore, whenever `epsilon<=2`,

> **`B_shell >= r+2-d-floor((r-1+epsilon)/2)`.**

This is the near-equality multicolor version of the shell B-floor.

## 5. d3 exclusion through the top three residual edge layers

Assume the general near-anchor theorem gives the core floor `K_r>=8`.

At residual edge layer

`e(F)=D_r(4r+1)-epsilon`,

with `epsilon=0,1,2`, the symbolic backend identity gives

> `q<=3r-1-epsilon`.

Suppose a regular d3 shell vertex exists. It defines a one-owner common-S family with d=3. Its exact q decomposition is

`q=3(r-2)+a+B_shell`,

with `a>=0`.

The near-equality B-floor gives

`B_shell >= r-1-floor((r-1+epsilon)/2)`.

For every `r>=12` and `epsilon in {0,1,2}`, this lower bound is strictly larger than `5-epsilon`. Therefore

`q >=3r-6+B_shell >3r-1-epsilon`,

contradicting the global q ceiling.

Hence:

> **For every r>=12, the top three residual edge layers**
>
> `D_r(4r+1), D_r(4r+1)-1, D_r(4r+1)-2`
>
> **contain no regular shell vertex of missing degree3.**

For r=12 this simultaneously explains the absence of d3 at residual edge layers 340,339,338 once the near-anchor `K>=8` theorem is available.

## 6. Source

The external ingredient is Brouwer's exact Turan stability theorem: if `n>=2r+1` and a `K_(r+1)`-free graph has at least `ex(n,K_(r+1))-floor(n/r)+2` edges, then it is r-partite. See A. E. Brouwer, *Some lotto numbers from an extension of Turan's theorem* (1981), and later restatements in the Turan-stability literature.
