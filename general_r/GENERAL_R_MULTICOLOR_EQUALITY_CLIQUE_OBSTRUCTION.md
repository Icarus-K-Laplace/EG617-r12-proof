# General-r Multicolor Equality / Regular-Clique Obstruction

Status: **PROVED_SYMBOLIC under the original balanced-colouring contract.**

This theorem is independent of the common-S support geometry. It uses only the hereditary extremal equality at order `4r+1` and the fact that the `r` color classes partition the edges of the complete graph.

## 1. Extremal equality in the other colors

Let `R` be a set of `4r+1` vertices inside a hypothetical Problem-617 counterexample. Fix one target color and let `F` be its graph on R.

For every color graph C on R we have `alpha(C)<=r`. Hence, by Turan in the complement,

`e(C)>=p_r(4r+1)=6r+4`.

Equivalently the target color satisfies the hereditary cap

`e(F)<=D_r(4r+1)=C(4r+1,2)-(r-1)(6r+4)`.

Assume equality:

`e(F)=D_r(4r+1)`.

Then the total number of non-target edges is exactly `(r-1)(6r+4)`. Since each of the other `r-1` colors contains at least `6r+4` edges, every one contains exactly that many.

Equality in Turan is unique. Therefore every non-target color graph is the complement of the balanced Turan graph `T_r(4r+1)`, hence is exactly

> `K_5 disjoint_union (r-1) K_4`.

Thus each non-target color partitions R into one 5-block and `r-1` 4-blocks.

## 2. A regular target clique cannot be large

Let B be a target-color clique whose every vertex has target degree exactly `r+1` inside F.

Fix `x in B`. Its non-target degree in R is

`(4r+1-1)-(r+1)=3r-1`.

For each of the other `r-1` colors, x lies in exactly one clique block. It gets three neighbours from that color when it lies in a 4-block and four neighbours when it lies in the unique 5-block.

Let `m_x` be the number of non-target colors whose 5-block contains x. Since color edge sets are disjoint and exhaust all non-target edges incident to x,

`3(r-1)+m_x=3r-1`,

so

> **`m_x=2`.**

Therefore the vertices of B require exactly `2|B|` incidences with the unique 5-blocks of the non-target colors.

But a non-target 5-block contains at most one vertex of B: two vertices of B are joined by a target edge, whereas two points in the same non-target block would have their edge in that non-target color.

There are only `r-1` non-target colors and hence only `r-1` such 5-blocks. Consequently

> **`2|B|<=r-1`.**

Equivalently:

> **Regular-clique obstruction:** `|B|<=floor((r-1)/2)`.

## 3. d3 top-boundary corollary

Assume the strengthened near-anchor envelope `q<=3r-1` and a d3 common-S family.

For d=3,

`q=3(r-2)+a+B`,

where `B=e_M(L)+G_L>=0`.

The only Bridge-B boundary beyond the transported-pair low-charge windows is

`b=e_M(S)=1, a=5`.

If it occurs, then

`q=3r-1+B`.

The global ceiling forces

`q=3r-1` and `B=0`.

The symbolic backend identity together with the strengthened core floor then forces the residual edge layer to equal the hereditary maximum `D_r(4r+1)`, so Section 1 applies.

Now `B=0` means:

- every leftover shell vertex is regular;
- the leftover set L is a target clique;
- every common-S owner is regular and target-adjacent to every shell point outside S;
- the owners are mutually target-adjacent.

Therefore

`B0={p} union (A\S)`

is a target clique of size

`1+(r+1-3)=r-1`,

and every vertex of B0 has target degree exactly `r+1`.

The regular-clique obstruction gives

`r-1 <= floor((r-1)/2)`,

impossible for every `r>=2`.

Hence:

> **The d3 boundary `b=1,a=5` is impossible.**

## 4. Strict d3 allowance consequence

Conditional on the general exact/near-anchor theorem (which supplies `q<=3r-1`), every d3 common-S family satisfies

> **`a<=4`.**

Indeed if `q<=3r-2`, this follows immediately from `q=3(r-2)+a+B`. If `q=3r-1`, then `a+B<=5`; the sole `a=5` possibility has `B=0` and is excluded above.

Thus the apparent all-r d3 higher-slack frontier collapses completely below allowance five.

## 5. Generalization

The counting proof actually shows more: at hereditary equality on `4r+1`, any target clique consisting of target-degree-`r+1` vertices has size at most `floor((r-1)/2)`.

This is a multicolor compatibility theorem. It is strictly stronger than applying one-color Turan stability independently to each color and is a concrete instance of the multicolor rigidity sought by the general-r programme.
