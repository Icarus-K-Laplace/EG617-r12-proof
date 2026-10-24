# General-r Cell A high-layer full exclusion for r>=25

Status: **PROVED_RELATIVE_TO ERDOS NON-BIPARTITE TRIANGLE-FREE EXTREMALITY + BROUWER SECOND-TURAN**, conditional on the contextual `5r+1` high-layer terminal contract and the `|W|=2r-1` Cell-A normal form.

## 1. Cell-A setup

Let F be a contextual target-color terminal on `5r+1` vertices with

- `alpha(F)<=5`;
- `omega(F)<=r-1`;
- `delta(F)=r+1`;
- `e(F)<=U_(5,r)=(5r^2+7r+18)/2`.

Assume a direct near-anchor triple has common target anti-neighbourhood W with

`|W|=2r-1`

in Cell A.

Then every non-target color on W is a minimum `(r-1)`-edge graph with independence number r, hence a matching of size `r-1` plus one isolated vertex.

Let

`J=bar(F[W])`.

Then

- J is triangle-free;
- J is non-bipartite because `alpha(J)=omega(F[W])<=r-1`, whereas a bipartite graph on `2r-1` vertices has an independent side of size at least r;
- `e(J)=(r-1)^2`, one below the Erdős non-bipartite triangle-free maximum `(r-1)^2+1`;
- the `r-1` non-target matching colors form a proper edge-coloring of J;
- if `z_v` is the number of non-target matching colors in which v is the isolated point, then

  `d_J(v)=r-1-z_v`,

  `sum_v z_v=r-1`.

We prove that at most five vertices have `z_v>0`.

## 2. Shortest odd cycle is C5 and the deficit is one-dimensional

Let C be a shortest odd cycle of J, of length `2k+1`.

Every vertex outside C has at most k neighbours on C, and the outside graph is triangle-free. Therefore

`e(J)<= (2k+1)+k(2r-2k-2)+floor((2r-2k-2)^2/4)`.

For k>=3 this is at most `(r-1)^2-2`, below `e(J)=(r-1)^2`.

Hence k=2 and C is a 5-cycle.

Put R=V(J)\C, so `|R|=2r-6=2(r-3)`. The standard C5 bound is

`e(J)<=5+2|R|+floor(|R|^2/4)=(r-1)^2+1`.

Since J has exactly one fewer edge, the two nonnegative deficits

`d_cross=2|R|-e(C,R)`,

`d_R=(r-3)^2-e(R)`

satisfy

> `d_cross+d_R=1`.

Thus exactly one of the following occurs.

### Type A

`R=K_(r-3,r-3)` and `e(C,R)=2|R|-1`.

All but one R-vertex have two C-neighbours; one exceptional R-vertex has one C-neighbour.

### Type B

`e(C,R)=2|R|` and R has `(r-3)^2-1` edges.

The outside graph R is necessarily bipartite. The only bipartite possibilities at this edge count are

- `K_(r-3,r-3)-e`;
- `K_(r-4,r-2)`.

The second is impossible because every R-vertex has two C-neighbours, and vertices in the smaller side would then have J-degree

`(r-2)+2=r>r-1=Delta(J)`.

Therefore

> `R=K_(r-3,r-3)-e`.

## 3. The five C5 two-neighbour patterns form a C5 disjointness graph

A two-element neighbour set on C must be independent on C, so there are exactly five possible two-neighbour patterns.

Make an auxiliary graph D whose five vertices are these patterns, joining two patterns when they are disjoint.

Directly, D is itself a 5-cycle.

Whenever xy is an edge of R, the C-neighbour patterns of x and y must be disjoint, otherwise their common C-neighbour forms a triangle with xy. Thus the pattern supports used on the two sides of R form a complete bipartite subgraph of D, apart from the unique missing R-edge in Type B.

The only complete bipartite subgraphs of a 5-cycle have one side of size1 and the other of size at most2.

This tiny pattern fact forces at least two vertices of C to receive the maximum possible `r-3` neighbours from R in both Type A and Type B.

For completeness:

- in Type A, if one side uses two pattern-types, the other side uses their unique common D-neighbour, so the two C-coordinates of that common pattern are saturated; if both sides use one pattern-type, the same conclusion is immediate, and the single one-neighbour exceptional point can destroy saturation in at most one of the otherwise forced coordinates;
- in Type B, after deleting the endpoints of the unique missing R-edge, the two pattern supports again form such a complete bipartite subgraph of D. If one side uses two types, the opposite missing-edge endpoint is forced into the unique common type, giving two saturated C-coordinates. If both sides use one type, the two exceptional endpoint-types can only move to the alternate D-neighbours, in which case the two middle C-coordinates remain saturated.

Hence:

> **at least two vertices of the C5 have J-degree r-1.**

Therefore at most three C5 vertices have positive degree deficit `r-1-d_J(v)`.

In Type A there is only one deficient R-vertex, so at most four vertices of W have positive deficit.

In Type B the two endpoints of the missing R-edge are deficient, so at most five vertices of W have positive deficit.

Thus in all cases

> **the isolate-support `{v:z_v>0}` has size at most5.**

## 4. Pointwise target-degree bound from the isolate support

Let S0 be the set of W-vertices that are isolated in at least one non-target matching color. We have `|S0|<=5`.

Fix any outside vertex o in `O=V(F)\W`.

For a non-target matching color j on W:

- if the edge from o to the isolated vertex z_j has color j, that single edge is a certificate hitting every maximum independent r-set of the matching-plus-isolate graph;
- otherwise o must be joined in color j to both endpoints of one matching edge.

Because one o--W edge has only one color, at most `|S0|<=5` colors can use the cheap one-edge isolate certificate.

Therefore the number of non-target o--W incidences is at least

`1*5+2*((r-1)-5)=2r-7`

(with an even stronger bound if fewer than five cheap colors are available).

Since `|W|=2r-1`,

> **`d_F(o,W)<=6` for every o in O.**

## 5. Alpha(O)<=3 for r>=25

Suppose Q is a target-independent 4-set in O.

Its target neighbourhood union in W has size at most

`4*6=24`.

Hence at least

`|W|-24=2r-25`

W-vertices are target-nonadjacent to every point of Q.

For r>=25,

`2r-25>r-1>=omega(F[W])`.

Therefore these remaining W-points contain a target-nonedge uv. Then

`Q union {u,v}`

is a target-independent 6-set, contradiction.

Thus

> **`alpha(F[O])<=3` for r>=25.**

## 6. Edge lower bound and contradiction

Now `|O|=3r+2`, `alpha(F[O])<=3`, and `omega(F[O])<=r-1`.

As in the Cell-B theorem, Brouwer's second-Turan result gives

`e_F(O)>=p_3(3r+2)+(r-1)=(3r^2+3r-2)/2`.

Next bound the cross edges. A W-vertex v has internal target degree

`d_(F[W])(v)=r-1+z_v`.

To reach the terminal minimum degree r+1, it needs at least

`max(0,2-z_v)`

target neighbours in O.

Since the isolate support has size at most5, at least `2r-6` W-vertices have z_v=0. Therefore

`e_F(W,O)>=2(2r-6)=4r-12`.

Finally Cell A has

`e_F(W)=r(r-1)`.

Hence

`e(F)>=r(r-1)+(4r-12)+(3r^2+3r-2)/2`

`=(5r^2+9r-26)/2`.

The contextual cap is

`e(F)<=(5r^2+7r+18)/2`.

The lower bound exceeds the upper bound by

`r-22`.

Thus for every r>=25 Cell A is impossible.

## 7. Consequence

Together with `GENERAL_R_CELL_B_HIGH_LAYER_FULL_EXCLUSION_R16.md`:

> **For every r>=25, the entire high-layer `|W|=2r-1` near-anchor cell is empty.**

Therefore in the all-large-r high-minimum-degree 5r+1 terminal the common target anti-neighbourhood can be sharpened from

`|W|<=2r-1`

to

> **`|W|<=2r-2` for r>=25.**
