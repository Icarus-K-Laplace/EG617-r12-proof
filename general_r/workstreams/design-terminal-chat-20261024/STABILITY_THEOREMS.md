# Stability theorems for a `(5r+1)` terminal

## S1. Exact local multicolor slack identity

Status: **PROVED_SYMBOLIC**.

Let `W` have `5r+1` vertices in a terminal. Let color 0 be the target color, so `alpha(G_0[W])<=5`; every other color satisfies `alpha(G_i[W])<=r`.

The Turan-complement minima are

`p_5(5r+1)=C(r+1,2)+4C(r,2)=(5r^2-3r)/2`,

`p_r(5r+1)=C(6,2)+(r-1)C(5,2)=10r+5`.

Define

`s_0=e(G_0[W])-p_5(5r+1)>=0`,

`s_i=e(G_i[W])-(10r+5)>=0` for `1<=i<=r-1`.

Because the `r` color classes partition `E(K_(5r+1))`,

> `sum_i s_i = C(5r+1,2)-p_5(5r+1)-(r-1)p_r(5r+1)=9r+5`.

This is the fundamental local multicolor budget.

## S2. Strict target Brouwer gap

Status: **PROVED_ANALYTIC**, using Brouwer's non-partite Turan bound and the Kang--Pikhurko equality classification.

Let `J_0=overline(G_0[W])`. Then `J_0` is `K_6`-free. It cannot be 5-partite: five parts on `5r+1` points contain a part of size at least `r+1`, but

`alpha(J_0)=omega(G_0[W])<=r-1`.

Brouwer therefore gives

`s_0=t_5(5r+1)-e(J_0)>=r-1`.

If equality held, Kang--Pikhurko's complete extremal classification writes the equality graph from five base independent parts whose sizes sum `5r`. One base part has size at least `r`, so `alpha(J_0)>=r`, contradicting the terminal clique cap. Hence

> `s_0>=r`.

Combining with S1:

> `S_non:=sum_(i=1)^(r-1) s_i <=8r+5`.

In particular, for `r>=15` at least one non-target color has `s_i<=8`.

### Low-defect equality families for a non-target color

For `J_i=overline(G_i[W])`, Brouwer with `p=r,n=5r+1` says a non-r-partite `J_i` has Turan deficit at least 4.

Therefore:

- if `s_i<=3`, `J_i` is exactly r-partite and `G_i[W]` is exactly a union of `r` clique blocks;
- if `s_i=0`, equality in Turan forces the exact block sizes `6,5,...,5`;
- at `s_i=4`, either one has an r-partite imbalance or a Kang--Pikhurko extremal non-r-partite equality object.

Status: **PROVED_ANALYTIC**.

## S3. Simultaneous Furedi stability

Status: **PROVED_ANALYTIC**.

Furedi's quantitative stability corollary says that a `K_(p+1)`-free graph with Turan deficit `t` differs in at most `3t` edges from a complete p-partite graph on the same vertex set.

Apply it to every complement `J_i`. Complementing back gives clique-union ideal graphs `Q_i` such that

`|E(G_i[W]) Delta E(Q_i)|<=3s_i`.

Therefore

> `sum_i |E(G_i[W]) Delta E(Q_i)| <= 3(9r+5)=27r+15`.  (EDIT)

Here `Q_0` is a union of 5 clique blocks and every `Q_i`, `i>0`, is a union of `r` clique blocks.

## S4. Partition-size energy

Status: **PROVED_ANALYTIC**.

Write target ideal block sizes as `a_(0j)=r+b_j`, `sum b_j=1`. From (EDIT),

`e(Q_0)-p_5(5r+1)<=4s_0`,

while exactly

`e(Q_0)-p_5(5r+1)=(sum_j b_j^2-1)/2`.

Hence

> `sum_(j=1)^5 (a_(0j)-r)^2 <=1+8s_0 <=72r+41`.

For a non-target ideal partition, write its `r` block sizes as `a_(ij)=5+b_(ij)`, with `sum_j b_(ij)=1`. Then

> `sum_j (a_(ij)-5)^2 <=1+8s_i`.

Summing over non-target colors and using S2,

> `sum_(i=1)^(r-1) sum_j (a_(ij)-5)^2 <=65r+39`.  (ENERGY)

Thus at most `65r+39` non-target ideal blocks have size different from 5.

## S5. Approximate edge-partition theorem

Status: **PROVED_ANALYTIC**.

For every pair `e` of vertices define its ideal multiplicity

`m(e)=#{i:e in E(Q_i)}`.

The actual color graphs have multiplicity exactly 1 on every pair. Pairwise comparison with (EDIT) gives

> `sum_e |m(e)-1| <=27r+15`.  (MULT)

Thus all but at most `27r+15` vertex pairs are covered exactly once by the ideal clique systems.

This is a genuinely multicolor statement; it does not follow by treating the color stabilities independently.

## S6. Partial resolvable transversal-design theorem

Status: **PROVED_ANALYTIC**.

Let the five blocks of `Q_0` be the target groups `B_1,...,B_5`.

A size-5 non-target ideal block which is not an exact transversal of the five target groups contains a pair from one `B_j`; that pair is simultaneously in `Q_0` and the non-target `Q_i`, so it consumes at least one unit of the overlap excess in (MULT).

Likewise, if two clean transversal blocks from different colors share two vertices, their shared pair consumes an overlap-excess unit. Deleting one offending block per excess unit removes all such repetitions.

Using (ENERGY) and (MULT), after deleting at most

> `(65r+39)+(27r+15)=92r+54`

non-target ideal blocks in total, the remaining family consists of size-5 exact transversals of `B_1,...,B_5`, any two sharing at most one point. Within each color the retained blocks remain disjoint, hence form a partial parallel class.

Therefore a terminal contains an idealized partial resolvable 5-group transversal design with at least

> `r(r-1)-92r-54 = r^2-93r-54`

clean blocks.

For `r>=94` this lower bound is positive and asymptotically it is `r^2-O(r)`.

Since each clean block covers 10 distinct cross-group pairs and the total number of cross-group pairs of five groups summing to `5r+1` is at most `10r^2+4r`, at most

> `934r+540`

cross-group pairs lie outside this retained linear design.

### Interpretation

This is the precise finite-geometric statement currently justified:

> the general terminal is `O(r)` block-defect away from a resolvable `TD(5,r)` / transversal 5-GDD geometry.

It is **not** yet proved to be an affine plane, a Latin-square system, or an exact TD.

## S7. One-defect-per-color principle

Status: **PROVED_SYMBOLIC**.

Every non-target ideal partition has `r` blocks covering `5r+1` points. It is impossible for all `r` blocks to be size-5 transversals of the five target groups, because those would cover only `5r` points. Thus each non-target ideal color necessarily carries at least one block defect (size or transversality defect).

This is the local shadow of the single extra point and is a natural incidence vector to classify next.
