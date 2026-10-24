# Partition / Signature Compatibility Route

Status: **first compatibility theorem proved; robust partition contradiction open**.

## 1. Row-signature viewpoint

For each vertex x, record the color row

`sigma_x(z)=color(xz)`, `z!=x`.

If `xy` has color i, then a third vertex z makes triangle xyz rainbow exactly when

`sigma_x(z) != i`,
`sigma_y(z) != i`,
`sigma_x(z) != sigma_y(z)`.

Thus the edgewise bad-extension statistic is the number of coordinates where the two rows either hit the edge color or collide with each other.

The global theorem proves

`average_(xy) b(xy) <= 3(r-1)-3P/(n r^2)`.

Since each row has length `r^2`, adjacent row signatures are therefore almost orthogonal: on average they have only `O(r)` forbidden/collision coordinates among `Theta(r^2)` coordinates.

This statement is genuinely multicolor and has no single-color analogue.

## 2. Connection to near-Turan partitions

The mother architecture already supplies two relevant facts:

1. each color graph has independence number at most r and is measured by a Turan slack `s_i` with exact total
   `sum_i s_i=r^2(r-1)/2`;
2. when a color is close to its Turan minimum, stability places it close to a union of r near-balanced cliques.

Inside an exact clique partition for color i, vertices in the same i-block have row entry i to one another. For another color j, edge-disjointness forces every j-block to intersect an i-block in at most one point. Exact simultaneous clique partitions therefore generate near-orthogonal block incidence matrices.

The new row-signature theorem says something complementary: even before a partition is chosen, most endpoint pairs demand near-disjoint color signatures on almost all third vertices.

The intended synthesis is

`small Turan slack -> near clique partitions`

plus

`few bad extensions -> near orthogonality of those partitions`.

## 3. Exact intersection-matrix target

For two colors i,j with candidate r-block partitions

`P_i={A_1,...,A_r}`, `P_j={B_1,...,B_r}`,

define the intersection matrix

`M^(i,j)_(ab)=|A_a intersect B_b|`.

In the exact edge-disjoint clique-partition regime,

`M^(i,j)_(ab)<=1`.

If both partitions cover `r^2` old vertices in r blocks of size r, every row and column sum is r, so all entries equal 1: the partitions are orthogonal.

Thus an exact pair of Turan-minimal color partitions automatically has the affine-plane-type incidence property needed by the known nonextension argument.

The robust target is to show that total partition error `o(r^2)` together with the `O(r)` bad-extension budget per typical edge forces all but `o(r^2)` entries of `M^(i,j)` to equal 1, with the remaining errors repairable or contradictory.

## 4. New edge compatibility theorem

For an i-colored edge xy,

`b(xy)=d_i(x)+d_i(y)-2-c_i(x,y)+sum_(j!=i)c_j(x,y)`.

Averaging over every edge of the complete graph gives

`average b <= 3(r-1)-3P/(n r^2)`.

Hence for any fixed `K>1`, all but at most a `1/K` fraction of edges satisfy

`b(xy) <= K[3(r-1)-3P/(n r^2)]`

by Markov.

For these typical edges, the total cross-color common-neighbor collision

`sum_(j!=i)c_j(x,y)`

is `O_K(r)` after subtracting the nonnegative same-color union term. This supplies an explicit sparse-collision condition to feed into robust intersection-matrix arguments.

## 5. Equality benchmark

At hereditary equality on a `4r+1` set, the mother branch already proves a stronger exact compatibility fact: every non-target color becomes `K_5 union (r-1)K_4`, and a target clique of target-degree-`r+1` vertices has size at most `floor((r-1)/2)` by counting incidences with the unique 5-blocks.

This shows that exact multicolor partition compatibility is already strong enough to kill a backend boundary. The present workstream seeks the robust/global analogue on `r^2+1` vertices.

## 6. Current blocker

Ordinary single-color stability permits `Theta(r^2)` edits in a typical color, while the total global error is `Theta(r^3)`. The missing theorem must convert the row-signature collision budget into a substantially smaller **simultaneous** partition error, or else show that the errors of different colors cannot occupy disjoint locations.

A sufficient next theorem would be:

> For two colors with slack `O(r^2)`, if their row-signature collision contribution is `O(r^3)` in total, then their near-Turan block partitions can be chosen with only `O(r)` (or `o(r^2)`) non-orthogonal incidences.

Such a theorem would bridge I1 to I2/I3 and could then be combined with the affine-plane nonextension mechanism.
