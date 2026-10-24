# E407 Cell-B independent-4 saturation theorem

Status: **PROVED_RELATIVE_TO_BROUWER/KANG-PIKHURKO AND THE CELL-B COLOR-CERTIFICATE BOUND**.

This theorem is independent of the retained-seed status of the V12 Q32 templates.

## Setup

Assume an E407 h13 T61 residual F realizes the |W|=23 sharp Cell-B common-antineighbourhood normal form from `T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD.md`.

Thus:

- W has 23 vertices;
- `bar(F[W])=S(K_11,11)`;
- write A,B for the two 11-point sides and w for the subdivision vertex;
- x in A and y in B are the two endpoints of the subdivided cross edge;
- `e_F(W)=131`;
- `d_F(w)=20` and `d_F(w,O)=0`, where `O=V(F)\W` has 38 vertices;
- every side vertex of A union B has internal target degree11 and hence at least2 target neighbours in O;
- the Cell-B color-certificate inequality gives

  `d_F(o,W)<=3` for every `o in O`.

## 1. O cannot have alpha at most3

Suppose `alpha(F[O])<=3`.

Then `J=bar(F[O])` is K4-free. Also `alpha(J)=omega(F[O])<=11`. Since `|O|=38>3*11`, J cannot be 3-partite.

Brouwer's exact second-Turan theorem for non-3-partite K4-free graphs yields

`e_F(O)>=p_3(38)+floor(38/3)-1`.

Now

`p_3(38)=C(13,2)+C(13,2)+C(12,2)=222`,

so

> `e_F(O)>=233`.

Every one of the 22 side vertices in W has internal target degree11 and total degree at least13, so

> `e_F(W,O)>=44`.

Therefore

`e(F)>=131+233+44=408`,

contradicting E407.

Hence

> **alpha(F[O])=4.**

## 2. Every independent 4-set saturates the W-neighbourhood bound

Fix any target-independent 4-set

`Q={q1,q2,q3,q4} subset O`.

By the Cell-B pointwise certificate,

`|N_F(q_i) intersect W|<=3`.

Therefore

`|N_F(Q) intersect W|<=12`.

Let

`W0=W\N_F(Q)`.

Every point of W0 is target-nonadjacent to all four points of Q.

If W0 contained two target-nonadjacent vertices u,v, then

`Q union {u,v}`

would be a target-independent 6-set, contradicting alpha(F)<=5.

Thus W0 must be a target clique.

Since omega(F[W])<=11,

`|W0|<=11`.

But `|W|=23`, so

`|N_F(Q) intersect W|>=12`.

Combining with the upper bound gives equality throughout:

> `|N_F(Q) intersect W|=12`;
>
> every qi has exactly3 target neighbours in W;
>
> the four 3-point neighbourhoods are pairwise disjoint;
>
> W0 is a target K11.

## 3. Only two orientations are possible

Because `d_F(w,O)=0`, the subdivision vertex w does not lie in `N_F(Q)`. Hence

> `w in W0`.

In the target graph F[W], the only 11-cliques containing w are

- `w union (A\{x})`;
- `w union (B\{y})`.

Indeed, w is target-adjacent to every side vertex except x,y; each side is a target K11; and there are no target cross-edges between A and B except xy.

Therefore every target-independent 4-set Q in O satisfies exactly one of the two orientation identities

> **A-orientation:**
>
> `union_(q in Q) N_F(q,W)=B union {x}`;

or

> **B-orientation:**
>
> `union_(q in Q) N_F(q,W)=A union {y}`.

Moreover the union is partitioned into the four disjoint 3-point neighbourhoods of the members of Q.

## Consequence

Any E407 Cell-B completion is no longer an arbitrary 14-defect extension.

It must satisfy simultaneously:

1. `alpha(F[O])=4`;
2. every independent 4-set of O has W-degree exactly3 at each point;
3. its four W-neighbourhoods are pairwise disjoint;
4. they partition one of the two fixed 12-point sets `B union {x}` or `A union {y}`.

Thus the surviving Cell-B problem is an exact 4x3 transversal-incidence system with only two orientations. This is the appropriate object to intersect with the four 130-edge isolated-K4 colours and with the V12 common-K11 Q32 templates.
