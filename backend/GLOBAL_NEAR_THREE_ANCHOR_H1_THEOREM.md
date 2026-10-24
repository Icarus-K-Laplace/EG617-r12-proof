# Global Near-Three-Anchor h<=1 Theorem

Status: **PROVED_ANALYTIC**.

This theorem extends the exact three-anchor obstruction to the first near-anchor layer and closes the d3/A4 missing-triangle transport sector without support-multiplicity casework.

---

## 1. Theorem

Let H be a graph on 35 vertices satisfying

- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`.

Suppose H contains three pairwise target-nonadjacent vertices whose total degree excess above12 is at most one.

Then

> **`K=sum_v(d_H(v)-12)>=8`.**

Equivalently

> **`e(H)>=214`.**

The h=0 case is exactly `GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md`.  It remains only to prove the degree pattern `(13,12,12)`.

---

## 2. Signature partition for a (13,12,12) independent triple

Let the independent triple be `a,b,c`, with

- `d(a)=13`;
- `d(b)=d(c)=12`.

Every other vertex is adjacent to at least one of `{a,b,c}`, otherwise together with the independent triple it would form an independent4.

Partition the other 32 vertices by their nonempty anchor-neighbourhood signature.

Let

- `X_a,X_b,X_c` be the exclusive blocks, adjacent to exactly one anchor;
- C be the connector set, adjacent to at least two anchors;
- `c0=|C|`;
- t be the number of connectors adjacent to all three anchors.

The number of anchor--nonanchor incidences is

`d(a)+d(b)+d(c)=37`.

The exclusive vertices contribute one incidence each, and the connector set contributes `2c0+t`.  Since

`|X_a|+|X_b|+|X_c|=32-c0`,

we obtain

`37=(32-c0)+(2c0+t)=32+c0+t`.

Hence

> **`c0+t=5`.**                                           (H1-1)

In particular

> **`c0<=5`.**                                             (H1-2)

---

## 3. The large exclusive block of the degree-13 anchor

The degree-13 anchor a has neighbours exactly

- all vertices of `X_a`;
- those connectors whose signature contains a.

Therefore

`13=|X_a|+|C_a|`

with `|C_a|<=c0<=5`.  Hence

> **`|X_a|>=8`.**                                          (H1-3)

Also `X_a union {a}` is a clique: if two vertices `x,x' in X_a` were nonadjacent, then

`{x,x',b,c}`

would be an independent4.

The clique fact is not needed for the numerical lower bound, but records the same partition geometry as the exact three-anchor theorem.

---

## 4. Dichotomy

### Case A: X_a contains a degree-12 vertex

Let `x in X_a` have degree12.

By definition of the exclusive block, x is nonadjacent to b and c.  Since b and c are also nonadjacent, the triple

`{x,b,c}`

consists of three pairwise nonadjacent degree-12 vertices.

Apply `GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md`:

> `K>=8`.

### Case B: every vertex of X_a has degree at least13

Then every vertex of X_a contributes at least one unit of excess.  The anchor a itself contributes one unit.  Therefore

`K>=1+|X_a|>=9`.

Since `K=2e(H)-420` is even, this case actually gives `K>=10`.

In particular `K>=8`.

Combining the two cases proves the theorem.

---

## 5. d3/A4 missing-triangle corollary

Use the notation of `GLOBAL_COMMON_S_NEAR_ANCHOR_DEFICIT_REDUCTION.md`.

For a d3 common missing triangle S at allowance `a=4`, every owner repivot core H_y contains S as an independent triple with total degree excess

`h_y<=a-3=1`.

The present theorem therefore gives

`K(H_y)>=8`,

so

`e(H_y)>=214`.

Using the backend identity

`E=91+q_y+e(H_y)`,

we obtain

> **`q_y<=E-305`.**

Thus the entire d3/A4 common-missing-triangle shallow-loss sector is automatically in the strengthened three-anchor envelope.  No A4 support-multiplicity classification is needed for this sector.

---

## 6. Structural interpretation

The theorem reveals a useful monotonicity mechanism.

A single excess unit on one of three independent near-anchors does not destroy the three-anchor obstruction, because the high anchor must either

1. have a minimum-degree exclusive neighbour, which regenerates an exact three-anchor triple; or
2. force at least eight exclusive neighbours to carry positive excess, which is more expensive than the desired global bound.

This is a reusable replacement principle rather than an equality-case enumeration.

---

## 7. Next layer

The next graph-theoretic frontier is total anchor excess h=2, with local patterns

- `(14,12,12)`;
- `(13,13,12)`.

The first pattern admits the same exclusive-block replacement argument almost verbatim.  The second requires a two-block compatibility theorem for the two degree-13 anchors.

Closing h=2 would immediately absorb the d3/A5 missing-triangle sector into the same backend envelope.