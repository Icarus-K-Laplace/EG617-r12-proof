# Global Independent-Triple h<=3 Theorem

Status: **PROVED_ANALYTIC**.

This theorem closes the balanced `(13,13,13)` near-anchor equality left by `GLOBAL_INDEPENDENT_TRIPLE_MIN_ANCHOR_THEOREM.md` and yields a uniform obstruction for every independent triple of total local excess at most three.

---

## 1. Theorem

Let H be a graph on 35 vertices satisfying

- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`.

Suppose H contains three pairwise target-nonadjacent vertices whose total degree excess above12 is at most three.

Then

> **`K=sum_v(d_H(v)-12)>=8`.**

Equivalently

> **`e(H)>=214`.**

If at least one member of the triple has degree12, this is already `GLOBAL_INDEPENDENT_TRIPLE_MIN_ANCHOR_THEOREM.md`.  Hence only the exact degree pattern

> `(13,13,13)`

requires proof.

---

## 2. Assume a balanced near-anchor triple and K<=6

Let `a1,a2,a3` be pairwise nonadjacent degree-13 vertices.

Assume for contradiction

`K<=6`.

The anchors consume exactly three units of excess, so outside them at most three vertices can have positive excess.

Partition the other32 vertices by their nonempty anchor-neighbourhood signatures:

- exclusive clique blocks `X1,X2,X3`;
- connector set C, `c=|C|`;
- t triple-connectors adjacent to all three anchors.

The anchor-degree sum is39, so

`39=(32-c)+(2c+t)=32+c+t`,

hence

> **`c+t=7`.**                                             (H3-1)

Since `0<=t<=c`,

> **`4<=c<=7`.**                                           (H3-2)

Every `Xi union {ai}` is a clique, so `|Xi|<=10`.  Also every connector-incidence count is at most c, hence `|Xi|>=13-c`.

Finally

> `|X1|+|X2|+|X3|=32-c`.                                  (H3-3)

---

## 3. Degree-12 subsets and transversal cover

Let

`Zi={x in Xi:d_H(x)=12}`.

Since at most three vertices outside the anchors have positive excess,

> `|Z1|+|Z2|+|Z3| >= (32-c)-3 =29-c >=22`.                (H3-4)

Suppose there is no independent transversal `z_i in Z_i`.

Then every triple in `Z1 x Z2 x Z3` contains a target cross-edge.  If `z1>=z2>=z3` denote the three Z-sizes in decreasing order, the standard transversal-cover counting gives

> **`E_cross >= z2*z3`,**                                  (H3-5)

where `E_cross` is the total number of target edges between distinct exclusive blocks.

Indeed an edge between the two largest Z-parts covers at most `z3` triples, etc.; equivalently the general bound is `E_cross>=ceil(z1z2z3/max z_i)=z2z3`.

---

## 4. Global upper bound on cross-block edges

Put `x_i=|Xi|` and let `K_X` be the excess on the exclusive blocks.  For `x in Xi`, its base clique `Xi union {ai}` already supplies exactly `x_i` target neighbours.  Therefore

`d_cross(x)+d_C(x)=12+kappa_x-x_i`.

Summing over all exclusive vertices gives the exact identity

> `2E_cross+E_(X,C)=sum_i x_i(12-x_i)+K_X`.               (H3-6)

Because the three anchors already consume three excess units and `K<=6`,

`K_X<=3`.                                                  (H3-7)

We also need a lower bound on exclusive--connector edges.

A pair-connector has two anchor neighbours and at most `c-1` connector neighbours, so degree at least12 forces at least

`11-c`

exclusive neighbours.

A triple-connector similarly needs at least

`10-c`

exclusive neighbours.

There are `c-t` pair-connectors and t triple-connectors.  Hence

`E_(X,C)>=(c-t)(11-c)+t(10-c)`
`=c(11-c)-t`.

Using `t=7-c`,

> **`E_(X,C)>=12c-c^2-7`.**                               (H3-8)

Combining (H3-6)--(H3-8):

> **`E_cross <= [sum_i x_i(12-x_i)+10-12c+c^2]/2`.**     (H3-9)

---

## 5. Exhaustive block-size arithmetic

The conditions

- `x1+x2+x3=32-c`;
- `13-c<=x_i<=10`;
- `4<=c<=7`

leave only the following unordered block-size triples.

For each row, the third column is the upper bound (H3-9).  The fourth column is the smallest possible transversal-cover lower bound `z2z3` after placing all three available positive-excess vertices so as to minimize that product.

|c|block sizes|max E_cross|min z2 z3|
|---:|---|---:|---:|
|4|(10,9,9)|26|54|
|5|(10,9,8)|27|45|
|5|(9,9,9)|28|54|
|6|(10,9,7)|28|36|
|6|(10,8,8)|29|40|
|6|(9,9,8)|30|45|
|7|(10,8,7)|31|32|
|7|(9,9,7)|32|36|
|7|(9,8,8)|33|40|

Every listed row contradicts (H3-5).

The only arithmetic cell not eliminated is

> `c=7`, block sizes `(10,9,6)`,                       (H3-10)

where minimizing the cover bound requires all three non-anchor excess units to lie in the size-six block.  Hence necessarily

- `K=6`;
- all seven connectors have excess zero;
- X1 and X2 are entirely degree12;
- X3 has exactly three degree12 and three positive-excess vertices;
- after ordering,

  `(|Z1|,|Z2|,|Z3|)=(10,9,3)`.

We now eliminate this final equality geometry directly.

---

## 6. Final (10,9,6) equality contradiction

Take any `x in Z1`.

Because `|X1|=10`, x already has ten target neighbours in its base clique `X1 union {a1}`.  Since x has degree12, it has at most two target neighbours outside that base.

Therefore

- x has at least seven target nonneighbours in Z2 (which has size9);
- x has at least one target nonneighbour `z in Z3` (which has size3).

Now z is degree12 and belongs to the size-six exclusive block X3.  Its base clique `X3 union {a3}` supplies six target neighbours, so z has at most six target neighbours outside that base.

If z were adjacent to all seven Z2-vertices which are nonadjacent to x, then z would already have at least seven external neighbours, impossible.

Hence some `y in Z2` is nonadjacent to both x and z.

By construction x and y lie in different exclusive blocks, z lies in the third, and all three have degree12.  Thus

`{x,y,z}`

is a set of three pairwise target-nonadjacent degree-12 vertices.

Apply `GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md`:

`K>=8`,

contradicting `K<=6`.

Thus the balanced `(13,13,13)` independent triple cannot occur at total core excess at most six.

---

## 7. Uniform h<=3 conclusion

Combining this theorem with `GLOBAL_INDEPENDENT_TRIPLE_MIN_ANCHOR_THEOREM.md`:

> **Any independent triple whose total degree excess above12 is at most3 forces global core excess `K>=8`.**

This is a graph-theoretic theorem with no shell/support labels.

---

## 8. d3 common-missing-triangle consequence

For a d3 common missing triangle S with ambient allowance a, `GLOBAL_COMMON_S_NEAR_ANCHOR_DEFICIT_REDUCTION.md` gives, in every owner repivot core,

`h_y=sum_(s in S)(d_(H_y)(s)-12)<=a-3`.

Therefore for

> **`a<=6`**

we have `h_y<=3`, and the present theorem yields

`K(H_y)>=8`,

hence

> **`q_y<=E-305`.**

Thus the entire d3 common-missing-triangle hierarchy

> **A3, A4, A5 and A6**

is absorbed into the same strengthened backend envelope.  No support multiplicity casework remains in this sector.

This substantially shrinks the shallow-loss Bridge B: a d3 higher-slack state can only escape this theorem when its common missing triple is not internally complete in the missing graph, or when allowance exceeds six.