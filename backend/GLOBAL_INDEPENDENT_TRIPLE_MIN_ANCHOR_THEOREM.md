# Global Independent-Triple Minimum-Anchor Theorem

Status: **PROVED_ANALYTIC**.

This theorem strictly strengthens `GLOBAL_NEAR_THREE_ANCHOR_H1_THEOREM.md`.  It shows that the exact three-anchor obstruction survives arbitrary excess on two members of an independent triple as long as the third member remains at minimum degree.

---

## 1. Theorem

Let H be a graph on 35 vertices satisfying

- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`.

Suppose H contains three pairwise target-nonadjacent vertices `a,b,c`, and at least one of them, say c, has degree exactly12.

Then

> **`K=sum_v(d_H(v)-12)>=8`.**

Equivalently

> **`e(H)>=214`.**

No bound is assumed on the individual degrees of a and b beyond the global minimum degree.

---

## 2. Reduction to K<=6

Since

`K=2e(H)-420`

is even, it suffices to rule out `K<=6`.

Write

`d(a)=12+e_a`, `d(b)=12+e_b`, `d(c)=12`,

and put

`h=e_a+e_b`.

Under `K<=6`, necessarily `h<=6`.

---

## 3. Signature partition

Every vertex outside `{a,b,c}` is adjacent to at least one of the three anchors, otherwise it would form an independent4 together with them.

Partition the remaining32 vertices into

- exclusive blocks `X_a,X_b,X_c`, where a vertex meets exactly the named anchor;
- connector set C, consisting of vertices meeting at least two anchors.

Let

- `c0=|C|`;
- t be the number of connectors meeting all three anchors;
- `c_a,c_b,c_c` be the numbers of connectors adjacent to the corresponding anchor.

The total anchor degree is

`36+h`.

The exclusive vertices contribute `32-c0` anchor incidences, while connectors contribute `2c0+t`.  Therefore

`36+h=(32-c0)+(2c0+t)=32+c0+t`,

so

> **`c0+t=4+h`.**                                         (IM1)

In particular

> `c0<=4+h`.                                               (IM2)

Also

`c_a+c_b+c_c=2c0+t=c0+4+h`.                              (IM3)

---

## 4. The minimum-degree anchor forces connector incidence

The exclusive set `X_c union {c}` is a clique: two nonadjacent vertices of X_c together with a and b would form an independent4.

Since `omega(H)<=11`,

`|X_c|<=10`.

But c has degree12 and its neighbours are exactly `X_c` plus its incident connectors. Hence

`12=|X_c|+c_c`,

so

> **`c_c>=2`.**                                            (IM4)

Using (IM3),

`c_a+c_b <= c0+h+2 <= 6+2h`.                              (IM5)

Therefore

`|X_a|+|X_b|`
`=(12+e_a-c_a)+(12+e_b-c_b)`
`=24+h-(c_a+c_b)`
`>=18-h`.                                                  (IM6)

---

## 5. At least twelve exact degree-12 vertices in X_a union X_b

The anchors a,b themselves already consume h units of the total excess budget.  Under the contradiction assumption `K<=6`, at most

`6-h`

vertices outside the anchors can have positive excess, because every such vertex contributes at least one unit.

Hence among `X_a union X_b`, the number of degree-12 vertices is at least

`(18-h)-(6-h)=12`.                                        (IM7)

Let `Z_a` and `Z_b` be the degree-12 vertices in `X_a` and `X_b` respectively.

Each Z-set is a clique because each exclusive block is a clique.

If every cross pair in `Z_a x Z_b` were also adjacent, then

`Z_a union Z_b`

would be a clique of size at least12, contradicting `omega(H)<=11`.

Therefore there exist

`x in Z_a`, `y in Z_b`

with `xy` a target nonedge.

By exclusivity, x and y are both nonadjacent to c.  Thus

`{x,y,c}`

is a set of three pairwise nonadjacent degree-12 vertices.

Apply `GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md`:

`K>=8`,

contradicting `K<=6`.

This proves the theorem.

---

## 6. d3 common-missing-triangle consequence

Use the exact transport reduction in `GLOBAL_COMMON_S_NEAR_ANCHOR_DEFICIT_REDUCTION.md`.

For a d3 common missing triangle S at allowance a, every owner repivot core H_y contains S as an independent triple with total degree excess

`h_y<=a-3`.

### a<=5

If `a<=5`, then `h_y<=2`.  Three nonnegative integer excesses summing to at most2 must include at least one zero.  Hence S contains a degree-12 vertex in H_y.

The present theorem gives

`K(H_y)>=8`,

so

> **`q_y<=E-305`.**

Therefore the entire d3 missing-triangle sector for allowances

> **`a=3,4,5`**

lies automatically in the strengthened three-anchor envelope.

This simultaneously subsumes the previous separate a=3 and a=4 anchor arguments.

### a=6

Now `h_y<=3`.

If any of the three transported vertices has degree12, the same theorem again gives `K(H_y)>=8`.

Thus the only possible escape from the three-anchor envelope has all three transported excesses positive.  Since their sum is at most3, the escape is forced to be exactly

> **degree pattern `(13,13,13)`.**                          (IM8)

Moreover equation (NA2) gives equality throughout:

`sum sigma_s=3`,

`sum |D_s intersect D_y|=0`.

Since each transported excess is one, this forces

> **`sigma_s=1` for all three s in S**,                    (IM9)
>
> **`D_s intersect D_y=empty` for all s in S`.**          (IM10)

Hence d3/A6 missing-triangle shallow loss has only one balanced near-anchor equality geometry left.

---

## 7. Research consequence

The historical d3 high-slack hierarchy should no longer be organized by A3/A4/A5 support multiplicity cases.

For a common missing triangle:

- A3--A5 are globally controlled by one independent-triple theorem;
- A6 reduces to the single balanced `(13,13,13)` transported equality.

The natural next graph-theoretic target is therefore the all-degree-13 independent triple, not another shell-support case split.

If that balanced near-anchor equality is shown to require `K>=8`, the d3 missing-triangle sector is fully absorbed into the same `E-305` envelope through allowance6.