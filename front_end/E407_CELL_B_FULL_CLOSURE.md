# E407 |W|=23 Cell-B full closure

Status: **PROVED_RELATIVE_TO_BROUWER/KANG-PIKHURKO EXTREMAL INPUTS AND THE CELL-B COLOR-CERTIFICATE LEMMA**.

This theorem is independent of the retained lower-order seeds in V12.

It combines:

- `T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD.md`;
- `E407_CELL_B_INDEPENDENT4_SATURATION.md`;
- `E407_CELL_B_COLOR_DEGREE_NORMAL_FORM.md`.

## 1. Accepted Cell-B structure

Assume for contradiction that an E407 h13 T61 residual F admits an independent near-anchor triple whose common target anti-neighbourhood W has size23 and lies in Cell B.

Write

- A,B for the two 11-point sides;
- w for the subdivision vertex;
- x in A, y in B for the endpoints of the subdivided cross edge;
- O=V(F)\W, |O|=38.

The previous theorems give:

1. `d_F(w)=20` and `d_F(w,O)=0`;
2. `alpha(F[O])=4`;
3. for every independent 4-set Q in O, every q in Q satisfies `d_F(q,W)=3`;
4. the four 3-point W-neighbourhoods are pairwise disjoint and partition exactly one of

   `B union {x}`

   or

   `A union {y}`;

5. the eleven non-target colors consist of seven 129-edge colors and four 130-edge colors;
6. the unique special Cell-B P3 color is one of the exact129 colors.

We show that (3)--(6) are incompatible.

## 2. Maximum-independent-set certificates in the W color factors

### Ordinary colors

For each of the ten ordinary Cell-B colors, the induced graph on W is

`11 K2 union {w}`.

Its independence number is12, and every maximum independent12-set contains w and one endpoint from each matching edge.

Therefore, for an outside vertex q:

- if `qw` has this ordinary color, the edge qw alone hits every maximum independent12-set and is a one-edge certificate;
- if `qw` has a different color, then to prevent q from extending a maximum independent12-set to an independent13-set, q must be joined in this ordinary color to both endpoints of at least one matching edge.

Thus every ordinary color different from the color of qw costs at least two q--W incidences.

### Special color

The special color on W is

`10 K2 union P3(x-w-y)`.

Its maximum independent12-sets contain both x and y and one endpoint from each of the ten matching edges; w is not in any maximum independent12-set of the P3 component.

Hence:

- the edge qw, even if special-colored, does not by itself certify the special color;
- the cheapest special-color certificate is one edge from q to x or y;
- alternatively one may use both endpoints of one of the ten special matching edges, at cost two.

## 3. A saturated q cannot have special-colored qw

Fix an independent4-set Q in O and q in Q.

By the saturation theorem,

`d_F(q,W)=3`.

Thus exactly20 of the 23 q--W edges are non-target.

Suppose qw has the special color.

Then all ten ordinary colors are different from the color of qw, so each requires at least two q--W incidences. This already costs20 ordinary incidences. The special color still needs, besides qw, at least one further certificate edge to x or y.

Hence q has at least22 non-target q--W incidences, so

`d_F(q,W)<=1`,

contradicting `d_F(q,W)=3`.

Therefore:

> **for every q in every independent4-set Q, the edge qw has an ordinary Cell-B color.**

## 4. Equality forces a 9-factor rainbow matching

Let the ordinary color of qw be M_j0.

There are nine other ordinary colors. Each must contribute both endpoints of one of its matching edges. Therefore these nine colors use at least

`9*2=18`

q--W incidences.

The own ordinary color M_j0 uses the one edge qw.

The special color needs at least one certificate edge, so the total non-target count is at least

`18+1+1=20`.

But saturation gives exactly20 non-target q--W edges. Hence equality holds in every step:

1. the own ordinary color contributes only qw;
2. each of the other nine ordinary colors contributes exactly one full matching edge;
3. the special color contributes exactly one edge, necessarily qx or qy;
4. no other q--W edge is non-target.

Because every q--W edge has a unique color, the nine selected ordinary matching edges are pairwise vertex-disjoint.

Each ordinary factor edge joins one A-vertex to one B-vertex. Thus the nine selected edges cover exactly

`9 vertices of A and 9 vertices of B`.

If the special one-edge certificate is qx, then one further A-vertex is non-target. Hence among the 22 side vertices the three target neighbours of q consist of

> **1 vertex in A and 2 vertices in B.**

If the special certificate is qy, the target-neighbourhood type is

> **2 vertices in A and 1 vertex in B.**

Therefore every saturated target 3-neighbourhood N_F(q,W) contains at least one A-vertex and at least one B-vertex.

## 5. Contradiction with the independent4 orientation theorem

Take any independent4-set

`Q={q1,q2,q3,q4} subset O`.

The saturation theorem says the four pairwise disjoint target 3-neighbourhoods partition either

`B union {x}`

or

`A union {y}`.

But each of the four 3-neighbourhoods contains at least one A-vertex and at least one B-vertex.

Therefore their union contains at least four A-vertices and at least four B-vertices.

This is impossible because

- `B union {x}` contains only one A-vertex;
- `A union {y}` contains only one B-vertex.

Contradiction.

Hence:

> **E407 admits no |W|=23 Cell-B completion.**

## 6. High-frontier consequence

`T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD.md` already excludes E408 Cell B because E408 has global target maximum degree19 while the Cell-B subdivision vertex has target degree20 inside W.

Together the two statements give:

> **For both E407 and E408, the sharp |W|=23 Cell-B normal form is empty.**

This removes the canonical subdivided-K11,11 design from the current h13 T61 frontier independently of the retained-seed Q32/Q33 machinery.
