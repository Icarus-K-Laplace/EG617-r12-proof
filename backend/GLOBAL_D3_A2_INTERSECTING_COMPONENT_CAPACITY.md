# Global d=3 A2 Intersecting-Component Capacity Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_Q32_NINE_OWNER_FULLY_DECORATED_TRANSVERSAL_REDUCTION.md`;
- `GLOBAL_ZERO_CHARGE_INCIDENCE_SIGNATURE_THEOREM.md`;
- common-S row closure and the d3 overlap-saturation inequality;
- the K11 base from the nine-owner fully-decorated q32 state;
- inherited caps `D(14)=69`, `D(15)=72`, `D(16)=76`, `D(17)=81`, `D(18)=87`;
- `alpha(H)<=3`.

Purpose: classify and bound any pairwise-intersecting support subfamily in the final fully-decorated allowance-two equality layer. The conclusion is owner-count capacity, not an E-layer case split.

## 1. Setup

Work in a common-S d3 support family with row defect

`Delta(D)=w(D)+mu(D)<=2`

for every support class D.

Assume the distinct support classes in the family are pairwise intersecting.

Whenever distinct D,E intersect properly, the d3 overlap cost is2. Hence

`Delta(D)=Delta(E)=2`,

and every shared support vertex has zero common-S charge.

Thus every vertex lying in at least two distinct support classes is a zero-charge incidence-signature vertex.

By the global zero-charge incidence-signature theorem, at most three distinct zero-charge signatures occur.

Let M denote the total owner multiplicity carried by the pairwise-intersecting family.

The ambient nine-owner fully-decorated state supplies the canonical dense base

`B={p} union Y union {r}=K11`.

All owner-support incidences of the present family are target edges from B into its support union.

## 2. Global common pair

Suppose all support classes contain one common two-point set

`C={x,y}`.

Distinct supports have the form

`D_i=C union {z_i}`

with distinct private petals z_i.

If there are at least two support classes, the pair xy must be a target edge.

Indeed, if xy were a target nonedge, any support requires its petal z_i to have positive charge and to be target-adjacent to both x and y in order to satisfy `Delta<=2`. Row closure against a second support would then see two target neighbours in that support but allow at most the petal charge, which is one; contradiction. A zero-charge petal cannot repair this because zero vertices of different incidence signatures are target-nonadjacent to x and y, leaving the support with no internal edge.

Hence xy is a target edge.

For each support D_i, exact defect arithmetic gives

`w_(z_i)=e_H(z_i,C)`

in `{0,1,2}`.

Row closure against another support shows that the already present z_i--C target edges consume the entire allowance of z_i, so

> private petals of distinct supports are pairwise target-nonadjacent.   (P1)

Therefore `alpha(H)<=3` gives at most three distinct support classes.

For k distinct common-pair supports, the support union has size `2+k` and contains at least the common target edge xy. Hereditary packing with the K11 base gives

`55+3M+1 <= D(13+k)`.

For k=1,2,3 this yields respectively

- `M<=4`;
- `M<=5`;
- `M<=6`.

Thus

> every global-common-pair intersecting family has owner count `M<=6`.   (P2)

## 3. Global common hub

Suppose all supports contain one common zero-charge hub x but there is no common pair.

Write

`D_i={x,u_i,v_i}`.

A support has only two possible nondegenerate forms.

### H-type

Both petals have positive charge. Since their total support defect is at most2, both charges equal1, the support has zero missing internal edges, and

`D_i=K3`.

### Z-type

Exactly one petal, say u_i, has zero charge with a non-global incidence signature. Then x and u_i have different zero signatures and are target-nonadjacent. The other petal v_i must have charge1 and be target-adjacent to both x and u_i. Thus the support is a two-edge path centered at v_i.

There cannot be a second distinct support with the same secondary zero signature u_i: such two supports would share the target-nonedge pair {x,u_i}, while each positive private center sees both points of that pair; row closure against the other support would require two target edges from a charge-one vertex. Hence each secondary zero signature contributes at most one Z-type support class.

There are at most two secondary zero signatures besides the global hub signature.

Now take private-petal sets

`P_i=D_i\{x}`.

For any two distinct supports, every point of P_i is target-nonadjacent to every point of P_j.

- for a positive unit-charge petal, its target edge to x already consumes its row-closure allowance against the other support;
- for a zero petal, zero-charge row closure gives anticompleteness directly.

Therefore the P_i are pairwise target-anticomplete.

Choosing one petal from each distinct support class gives an independent set, so

> at most three distinct support classes occur.               (H1)

Every support contains at least two internal target edges: H-type has3, Z-type has2.

For k distinct common-hub supports, the support union has size `1+2k` and contains at least `2k` target edges. K11 hereditary packing gives

`55+3M+2k <= D(12+2k)`.

For k=1,2,3 this yields

- `M<=4`;
- `M<=5`;
- `M<=8`.

Thus

> every global-common-hub intersecting family has owner count `M<=8`.   (H2)

## 4. No global zero core

Assume now the pairwise-intersecting family has no zero-charge signature contained in every support.

Represent each zero-charge signature class by the set of support classes containing it. Since there are at most three signature classes, every support receives a nonempty membership code in subsets of `{1,2,3}`.

Pairwise intersection of supports means every two support codes intersect.

If a support had code `{1,2,3}`, it would contain representatives of all three distinct zero signatures. Those three zero vertices are pairwise target-nonadjacent, so a 3-point support consisting of them would have no internal target edge, contradicting `Delta<=2`.

Hence code `{1,2,3}` cannot occur.

A pairwise-intersecting family of proper nonempty subsets of `{1,2,3}` with empty total intersection has, up to relabelling, only the three codes

`{1,2}`, `{1,3}`, `{2,3}`.

Moreover each code can occur for at most one support class. If two distinct supports had the same two-signature zero core, they would form a nontrivial common-pair pattern whose common pair consists of two different zero signatures and is therefore a target nonedge, contradicting Section2.

Consequently

> there are exactly at most three support classes.             (T1)

The possible zero-signature class sizes give only two nondegenerate geometries.

### Triangle type (1,1,1)

The three supports have the form

`D_12={a,b,u}`, `D_13={a,c,v}`, `D_23={b,c,w}`,

where a,b,c are distinct zero signatures.

They are pairwise target-nonadjacent. Exact defect arithmetic forces each private vertex to have charge1 and to be adjacent to the two zero vertices in its support. Row closure makes the three private vertices pairwise target-nonadjacent.

Thus the six-point support union has exactly six target edges.

K11 packing on17 points gives

`55+3M+6<=81`,

hence

`M<=6`.                                                       (T2)

### Triangle type (2,1,1)

One zero signature class, say Z_1, has size2, while the other two have size1. The two supports involving Z_1 consist entirely of shared zero vertices and have as their unique internal target edge the edge inside Z_1. The third support contains the two singleton zero signatures plus one charge-one private center adjacent to both.

The support union has five vertices and exactly three target edges.

K11 packing on16 points gives

`55+3M+3<=76`,

so again

`M<=6`.                                                       (T3)

Therefore

> every pairwise-intersecting family with no global zero core has owner count `M<=6`.   (T4)

## 5. Intersecting-family capacity

Combining Sections2--4:

> **d3 A2 intersecting-component capacity theorem.**
> Any pairwise-intersecting family of distinct d3 support classes in the fully-decorated allowance-two equality layer carries at most
>
> `M<=8`
>
> owner rows.                                                 (I1)

The only family reaching the coarse bound8 is a three-class global-common-hub geometry. Common-pair and no-global-core geometries have owner capacity at most6.

## 6. Consequence for the nine-owner escape

The nine-owner fully-decorated residual has total owner count9.

Therefore its support hypergraph cannot be pairwise intersecting.

The preceding fully-decorated transversal theorem already proves that no three support classes are pairwise disjoint.

Hence its matching number is exactly

> `nu(F)=2`.                                                   (I2)

Thus the final nine-owner support hypergraph is genuinely a two-block system: it has a disjoint support pair, but every third support meets at least one member of every maximal disjoint pair.

This identifies the unique remaining structural regime before full closure.

## 7. Generalization

The classification uses only support size3, the overlap cost2, zero-charge signature capacity from `alpha(H)<=3`, and a dense hereditary base. For larger independence bound r, the same signature-code method yields a finite intersecting-component taxonomy controlled by at most r zero signatures.
