# Three-Anchor K=6 / Two-Connector Full Closure

Status: **PROVED_ANALYTIC**.

This theorem eliminates all three normal forms from `GLOBAL_THREE_ANCHOR_K6_C2_NORMAL_FORM.md` by one transversal-cover counting argument.

Dependencies:

- `GLOBAL_THREE_ANCHOR_K6_C2_NORMAL_FORM.md`;
- `alpha(H)<=3`;
- exact degree12 of every block vertex in the K=6 c=2 normal forms.

No solver and no E-layer label are used.

---

## 1. Common setup

In every K=6 c=2 normal form there are three clique blocks

`X1,X2,X3`,

all of size10, and two connectors z,w.

Every block vertex has degree exactly12.

For a fixed connector z define

`M_i={x in X_i : zx is a target nonedge}`,

`m_i=|M_i|`.

Let

`e_ij=e_H(M_i,M_j)`.

---

## 2. Every M1 x M2 x M3 transversal must contain a cross edge

Take arbitrary

`x_i in M_i`, `i=1,2,3`.

All three vertices are nonadjacent to z.

If `x1,x2,x3` were pairwise target-nonadjacent, then

`{z,x1,x2,x3}`

would be an independent4, contradicting `alpha(H)<=3`.

Therefore every triple in

`M_1 x M_2 x M_3`

contains at least one target edge joining two different blocks.

An edge between M1 and M2 covers exactly `m_3` such triples; similarly for the other pairs. Hence the union bound gives the necessary transversal-cover inequality

> `m_3 e_12 + m_2 e_13 + m_1 e_23 >= m_1 m_2 m_3`.   (T1)

In particular, if `E_cross` is the **total** number of target edges between distinct X-blocks, then

> `E_cross * max(m_1,m_2,m_3) >= m_1m_2m_3`.          (T2)

Thus

> `E_cross >= ceil(m_1m_2m_3 / max m_i)`.              (T3)

This bound uses only independence number3 and one connector's block-nonneighbour profile.

---

## 3. Exact global cross-edge count

Let `r_x` be the number of the two connectors {z,w} which are nonadjacent to a block vertex x.

Every x in X_i already has exactly ten target neighbours inside

`X_i union {a_i}`.

It has exactly `2-r_x` target neighbours among the two connectors.

Because `d_H(x)=12`, its number of target neighbours in the other two X-blocks is therefore exactly

`12-10-(2-r_x)=r_x`.                                       (T4)

Summing (T4) over all thirty block vertices, the total number of cross-block edge stubs is

`sum_x r_x = m(z)+m(w)`,                                    (T5)

where m(z),m(w) are the total block-nonneighbour counts of the two connectors.

Every cross-block target edge contributes two stubs, so

> **`E_cross=(m(z)+m(w))/2`.**                              (T6)

This is exact in every K=6 c=2 normal form.

---

# 4. Type A contradiction

Type A has

- z,w adjacent;
- both connector profiles `(7,6,6)`;
- hence `m(z)=m(w)=19`.

Equation (T6) gives

`E_cross=19`.

Apply (T3) to either connector:

`E_cross >= ceil(7*6*6/7)=36`.

Thus

`19>=36`, contradiction.

So Type A is impossible.

---

# 5. Type B contradiction

Type B has connector profiles

`(7,6,6)` and `(9,4,4)`,

with total block-nonneighbour counts19 and17.

Hence by (T6)

`E_cross=18`.

Apply (T3) to the `(7,6,6)` connector:

`E_cross>=36`.

Contradiction.

Thus Type B is impossible.

---

# 6. Type C contradiction

Type C has both profiles

`(8,5,5)`,

so `m(z)=m(w)=18` and

`E_cross=18`.

For either connector, (T3) gives

`E_cross >= ceil(8*5*5/8)=25`.

Contradiction.

Thus Type C is impossible.

---

# 7. Conclusion

All three K=6 two-connector normal forms are impossible.

Therefore

> **there is no three-anchor K=6 core with connector count c=2.**   (T7)

The first surviving three-anchor equality layer, if it exists at all, must lie in the c=3 or c=4 regimes.

---

# 8. Reusable transversal-cover lemma

The proof isolates a general device worth retaining independently:

> Let z be a vertex nonadjacent to three vertex blocks M1,M2,M3.  If `alpha(H)<=3`, then the cross edges among the three blocks must cover every transversal, so
>
> `|M3|e(M1,M2)+|M2|e(M1,M3)+|M1|e(M2,M3) >= |M1||M2||M3|`.

Whenever degree equalities globally upper-bound the available cross-edge count, this gives an immediate contradiction.

This mechanism is not specific to K=6 and may be reusable in later equality geometries.