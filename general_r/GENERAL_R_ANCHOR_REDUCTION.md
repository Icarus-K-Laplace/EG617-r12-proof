# General-r Anchor Partition and Near-Anchor Reduction

Status: **PROVED_SYMBOLIC for the partition/reduction statements below, conditional on the general residual-core contract. The exact three-anchor excess bound K_r>=8 remains OPEN for general r.**

Assume throughout

- `r>=12`;
- `|H|=3r-1`;
- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- `delta(H)>=r`;
- `K_r=sum_v(d_H(v)-r)`.

## 1. Exact degree-r three-anchor partition

Let `a1,a2,a3` be pairwise nonadjacent vertices of degree exactly r.

Every other vertex meets at least one anchor. Let C be the set of vertices meeting at least two anchors and let t be the number meeting all three. Anchor-incidence counting gives

`|C|+t=4`.

The exclusive set Xi together with ai is a clique, so `|Xi|<=r-2`. Hence `|C|>=2`.

Therefore

> **`|C| in {2,3,4}`.**

Writing `d_i=(r-2)-|X_i|>=0`, one obtains

`d_1+d_2+d_3=|C|-2`.

Thus the complete block-size list is independent of r:

- c=2: `(r-2,r-2,r-2)`;
- c=3: `(r-2,r-2,r-3)`;
- c=4: `(r-2,r-2,r-4)` or `(r-2,r-3,r-3)`.

The r=12 partitions `(10,10,10)`, `(10,10,9)`, `(10,10,8)`, `(10,9,9)` are exactly these formulas.

## 2. Independent triple containing a minimum-degree anchor

Suppose `a,b,c` are pairwise nonadjacent and `d(c)=r`. Assume for contradiction `K_r<=6`.

Write

`d(a)=r+e_a`, `d(b)=r+e_b`, `h=e_a+e_b`.

Then `h<=6`.

The same signature partition gives

`c_0+t=4+h`,

where c_0 is the connector count.

Because `X_c union {c}` is a clique and `omega(H)<=r-1`,

`|X_c|<=r-2`,

so c has at least two connector neighbours.

Exactly as in the r=12 argument,

`|X_a|+|X_b|>=2r-6-h`.

Outside the anchors, at most `6-h` vertices can have positive excess. Therefore `X_a union X_b` contains at least

> **`2r-12`**

degree-r vertices.

For r>=12 this is at least r vertices.

If every degree-r vertex of X_a were adjacent to every degree-r vertex of X_b, their union would be a clique of size at least r, contradicting `omega(H)<=r-1`.

Hence there exist degree-r vertices `x in X_a`, `y in X_b` with xy a nonedge. By exclusivity both are nonadjacent to c.

Thus:

> **Minimum-anchor reduction.** Under `K_r<=6`, any independent triple containing one degree-r anchor produces an independent triple of three exact degree-r anchors.

Consequently, any general theorem excluding exact degree-r three-anchor cores at K_r<=6 automatically excludes every independent triple containing a minimum-degree vertex.

## 3. Balanced `(r+1,r+1,r+1)` near-anchor triple

Now suppose three pairwise nonadjacent anchors all have degree r+1 and assume `K_r<=6`.

The anchors consume three excess units, so at most three other vertices have positive excess.

Anchor-incidence counting gives

`c+t=7`,

hence

`4<=c<=7`.

Let `d_i=(r-2)-|X_i|`. Then again

`d_1+d_2+d_3=c-2`,

with `0<=d_i<=c-3`.

Thus the possible deficit patterns are finite and independent of r:

- c=4: `(0,1,1)`;
- c=5: `(0,1,2)`, `(1,1,1)`;
- c=6: `(0,1,3)`, `(0,2,2)`, `(1,1,2)`;
- c=7: `(0,1,4)`, `(0,2,3)`, `(1,1,3)`, `(1,2,2)`.

Let Zi be the degree-r vertices in Xi. If there is an independent transversal `z_i in Z_i`, then one has produced an exact degree-r independent triple and enters the exact-anchor branch.

Assume no such transversal exists. Cross-block edges must cover all triples in `Z_1 x Z_2 x Z_3`, so if `z_1>=z_2>=z_3`,

`E_cross>=z_2 z_3`.

The three anchors have already consumed three of the at most six excess units. Hence at most three exclusive-block vertices have positive excess. To minimize `z_2z_3`, all three may be deleted from the smallest block.

On the other hand, degree counting and the connector minimum-degree requirement give

`E_cross <= [sum_i x_i(r-x_i)+10-cr+c^2]/2`.

For the ten deficit patterns above, the lower-minus-upper differences are:

|c|deficits|lower-upper|
|---:|---|---|
|4|(0,1,1)|`r^2-11r+16`|
|5|(0,1,2)|`r^2-12r+18`|
|5|(1,1,1)|`r^2-11r+14`|
|6|(0,1,3)|`r^2-13r+20`|
|6|(0,2,2)|`r^2-13r+23`|
|6|(1,1,2)|`r^2-12r+15`|
|7|(0,1,4)|`r^2-14r+22`|
|7|(0,2,3)|`r^2-14r+25`|
|7|(1,1,3)|`r^2-13r+16`|
|7|(1,2,2)|`r^2-13r+19`|

Every row is strictly positive for every r>=13. Hence:

> **Balanced near-anchor reduction for r>=13.** If `K_r<=6`, an independent triple of three degree-(r+1) vertices must produce an independent triple of exact degree-r vertices.

At r=12 exactly one arithmetic cell escapes this coarse cover bound, namely the historical `(10,9,6)` cell, which the r=12 repository closes by an additional degree-capacity argument.

## 4. Consequence for total anchor excess <=3

If an independent triple has total excess at most3, then either

1. one member has degree r, and Section2 reduces to exact anchors; or
2. all three have positive integer excess, hence all three have degree r+1, and Section3 reduces to exact anchors for r>=13 (with r=12 separately proved in the existing repository).

Therefore the general low-excess anchor theorem has been reduced to one single unresolved symbolic statement:

> **Exact Three-Anchor Excess Conjecture.** Under the residual-core contract, three pairwise nonadjacent degree-r vertices force `K_r>=8` for every r>=12.

Proving this one theorem would immediately generalize the r=12 near-anchor obstruction through total anchor excess three.
