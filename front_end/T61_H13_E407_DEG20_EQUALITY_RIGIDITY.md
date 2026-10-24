# T61 h13 E407 degree-20 equality rigidity

Status: **PROVED_RELATIVE_TO_BROUWER/KANG-PIKHURKO EXTREMAL THEOREMS**.

This file strengthens the E407 equality discussion in `T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD.md`.

## 1. A 131-edge non-target color cannot have degree 2

Let C be a non-target color graph on the 61-point T61 residual with

`alpha(C)<=12`, `omega(C)<=5`, `e(C)=131`.

Assume a vertex v has degree2. Let

- `U=N_C(v)`, so `|U|=2`;
- `N` be the 58 non-neighbours of v.

Since v is anticomplete to N, an independent12-set in C[N] would extend with v to an independent13-set. Hence

`alpha(C[N])<=11`.

Also `omega(C[N])<=5`.

Because 58>55=11*5, the complement of C[N] is K12-free and non-11-partite. Brouwer's second-Turan theorem gives

`e(C[N])>=p_11(58)+4=125+4=129`.

Now

`e(C)=e(C[N])+d_C(v)+e_C(U,N)+e_C(U)`.

Since the left side is131 and the first two terms are at least129+2, equality is forced:

- `e(C[N])=129`;
- `e_C(U,N)=0`;
- `e_C(U)=0`.

Thus the two vertices of U are independent and anticomplete to N.

To keep `alpha(C)<=12`, we would need `alpha(C[N])<=10`, since any independent set of size11 in N could be enlarged by both vertices of U to size13.

But a 58-point graph with independence number at most10 has at least

`p_10(58)=140`

edges, contradicting `e(C[N])=129`.

Therefore:

> **Every 131-edge non-target color has minimum degree at least3.**

## 2. A 130-edge color at a degree-3 vertex has an isolated K4

Let `e(C)=130` and suppose `d_C(v)=3`. Put

`U=N_C(v)`, `|U|=3`,

and let N be the 57 non-neighbours of v.

As above,

`alpha(C[N])<=11`, `omega(C[N])<=5`.

Brouwer gives

`e(C[N])>=p_11(57)+4=120+4=124`.

Hence

`e_C(U)+e_C(U,N) <= 130-3-124=3`.      (1)

We claim U must be a triangle.

Suppose not. Then U contains two nonadjacent vertices x,y.

- If `e_C(U)=2`, then U is a path and (1) gives `e_C(U,N)<=1`; choose the two path endpoints. Their combined N-neighbourhood has size at most1.
- If `e_C(U)=1`, choose the isolated U-vertex together with a suitable endpoint of the unique U-edge. If the combined N-neighbourhood has size2, then necessarily `e_C(U,N)=2` and `e(C[N])=124`; otherwise it has size at most1.
- If `e_C(U)=0`, since at most3 U-N edges exist, two U-vertices have combined N-neighbourhood at most2. If that union has size2, then `e(C[N])=124`; for smaller unions the argument is stronger.

Delete that combined N-neighbourhood X. In all cases `|X|<=2`, and the remaining graph has at least55 vertices. If `|X|<=1`, then

`e(C[N\X])<=126 < p_10(56)=130`.

If `|X|=2`, the equality bookkeeping above gives

`e(C[N\X])<=124 < p_10(55)=125`.

Hence `C[N\X]` contains an independent11-set I. Since x,y are nonadjacent and have no neighbours in I,

`I union {x,y}`

is an independent13-set in C, contradiction.

Therefore U is a triangle.

Then (1) forces

- `e_C(U)=3`;
- `e_C(U,N)=0`;
- `e(C[N])=124`.

Thus:

> **If a 130-edge non-target color has a degree-3 vertex v, then `C[{v} union U]` is an isolated K4 component.**

The remaining57 vertices form the exact constrained second-Turan equality graph for parameters `(alpha<=11, omega<=5)`.

## 3. Consequence for an E407 target-degree20 vertex

In E407 the total non-target excess above129 is4.

Let v have target degree20. Then its total non-target degree is40.

Use the pointwise floors:

- a 129-edge exact color has degree at least4;
- a 130-edge color has degree at least3;
- a 131-edge color now also has degree at least3 by Section1;
- any higher cell has degree at least2.

Checking all partitions of total excess4, the only way the eleven non-target degrees can sum to40 is

> **`1+1+1+1`.**

Hence globally the eleven non-target edge counts are, up to order,

> **`129^7,130^4`.**

At v:

- v has degree4 in every one of the seven 129-edge exact colors;
- v has degree3 in every one of the four 130-edge colors.

By Section2, in each 130-edge color the three neighbours of v form a triangle and together with v form an isolated K4 component.

## 4. Consequence for E407 Cell B

Assume additionally that a near-anchor common anti-neighbourhood W has the sharp 23-point Cell B normal form

`bar(F[W])=S(K_11,11)`

with subdivision vertex w.

Then `d_(F[W])(w)=20`. Since E407 has `Delta(F)<=20`,

> **`d_F(w)=20` and `d_F(w,V\W)=0`.**

Thus w is target-antocomplete to all 38 vertices outside W.

In the unique Cell-B special non-target color, w has two W-neighbours which are the two endpoints of the P3. Those endpoints are nonadjacent in that color.

Therefore that special color cannot be one of the four 130-edge colors: Section2 would require all three colour-neighbours of w to form a triangle.

Hence:

> **the Cell-B special color is one of the seven exact129 colors.**

Consequently the ten ordinary Cell-B colors consist of

- six exact129 colors;
- four 130-edge colors.

For each of the four 130-edge ordinary colors, w has no W-neighbour, so its degree3 neighbourhood lies entirely in `O=V\W` and forms a triangle. Since an edge `wo` has only one color, these four triples are pairwise disjoint.

Therefore O contains four disjoint triples

`T_1,T_2,T_3,T_4`

such that for four distinct non-target colors `c_i`,

> **`F_(c_i)[{w} union T_i]=K4`**
>
> and this K4 is a component of color `c_i`.

These four triples occupy exactly12 of the 38 outside vertices.

The remaining color-degree partition at w is exact:

- special exact color: degree4 total, with two W-neighbours and two O-neighbours;
- six ordinary exact colors: degree4 each, all four neighbours in O;
- four 130-edge colors: degree3 each, all three neighbours in O.

The O-neighbour counts sum

`2+6*4+4*3=38`,

so they partition all outside vertices by the color of their edge to w.

## 5. Current E407 Cell-B normal form

Any E407 Cell-B completion must simultaneously satisfy:

1. target degree of w exactly20 and no target edge from w to O;
2. global non-target edge-count multiset `129^7,130^4`;
3. the special Cell-B color is exact129;
4. four ordinary 130-colors create four disjoint isolated K4 components through w;
5. the six remaining ordinary exact colors and the special exact color partition the other26 w-O edges in blocks `4,4,4,4,4,4,2`;
6. outside the unavoidable 7 units of target excess at w, the whole target residual has only14 excess units left.

This is a substantially narrower extension problem than the original E407 Q32 shell classification.

It should be intersected with the V12 five common-K11 templates and the 284-edge core rather than enumerated independently.