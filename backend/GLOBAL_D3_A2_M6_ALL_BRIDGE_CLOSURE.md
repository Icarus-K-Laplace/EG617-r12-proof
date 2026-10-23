# Global d=3 A2 M=6 All-Bridge Closure

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_A2_TWO_BLOCK_INCIDENCE_BUDGET.md`;
- `GLOBAL_ZERO_CHARGE_INCIDENCE_SIGNATURE_THEOREM.md`;
- common-S overlap saturation / row closure at allowance2;
- `GLOBAL_FULLY_DECORATED_TO_ONESPOKE_BRIDGE.md`;
- `GLOBAL_ONESPOKE_CLIQUE_FORCING_THEOREM.md`;
- `alpha(H)<=3`.

Purpose: close every `M=6` maximal-disjoint-pair window in the final q32 fully-decorated nine-owner state, including `b>0`. The proof uses only sparse six-point core classification and zero-charge incidence signatures.

## 1. Setup and numerical reduction

Let D,E be a maximal disjoint pair of 3-supports and put

`C=D union E`, `|C|=6`,
`M=m_D+m_E=6`.

Let b be the total owner multiplicity of bridge supports meeting both D and E.

The two-block budget gives

`12+b+e_H(C)<=17`,

hence

> `b+e_H(C)<=5`.                                             (M1)

Because `alpha(H[C])<=3`, every 6-vertex induced graph has at least three target edges (equivalently its complement is K4-free and has at most12 edges). Thus

> `e_H(C)>=3`.                                                (M2)

Therefore

> `b<=2`, `e_H(C) in {3,4,5}`.                               (M3)

The `b=0` window was already reduced to the unique P3-plus-K3 Type-C geometry and is closed by `GLOBAL_ONESPOKE_CLIQUE_FORCING_THEOREM.md`.

It remains to treat `b>=1`. Then (M1) sharpens to

> `e_H(C)<=4`.                                                (M4)

Thus only 3-edge and 4-edge six-point cores occur.

## 2. The 3-edge core is impossible

A six-vertex graph with three edges and independence number at most3 is necessarily

> `H[C]=3K2`.                                                 (M5)

Indeed the complement has12 edges and is K4-free, so it is the extremal Turan graph `K_(2,2,2)`; taking complements gives three disjoint target edges.

Since both supports D and E contain at least one internal target edge and each has only three vertices, exactly one matching edge lies inside D, exactly one lies inside E, and the third is a D--E cross edge.

Hence

`e_H(D)=e_H(E)=1`.

At allowance2 this forces

`w(D)=w(E)=0`.                                                (M6)

Thus all six C-vertices have zero common-S charge.

Every target edge joining two zero-charge support-union vertices forces equal incidence signatures. Therefore each of the three K2 components of H[C] is an inseparable zero-signature block: any support containing one endpoint contains the other.

### 2.1 b=2

Here `12+2+3=17`, so the two-block budget is saturated. There is one remaining side owner, and its support must meet C in exactly one vertex.

But every C-vertex lies in a two-point zero-signature block, so any distinct support containing that vertex contains its signature mate as well and meets C in at least two points.

Contradiction.

### 2.2 b=1

Now `12+1+3=16`, so the entire induced-cap budget has only one extra C-incidence beyond the lower count used in the two-block inequality.

There are two remaining side owners. Each side support is certified to meet C at least once. By the same zero-signature block argument, each actually meets C at least twice, contributing at least one extra incidence per owner.

This requires at least two extra incidences, but only one is available.

Contradiction.

Therefore

> the 3-edge core is impossible for every `b>=1`.             (M7)

## 3. Classification of the 4-edge core

Now `e_H(C)=4`. Equation (M1) gives

> `b=1`,                                                     (M8)

and the two-block budget is saturated.

A six-vertex four-edge graph with independence number at most3 is, up to isomorphism, exactly one of

1. `P4 disjoint_union K2`;
2. `K3 disjoint_union K2 disjoint_union K1`.                 (M9)

Proof: a connected six-vertex graph needs at least five edges. For a `4+2` component split, the four-vertex three-edge component must be P4 rather than K1,3, since the latter plus K2 has independence4. For a `3+2+1` split, the edge count forces K3+K2+K1. A `3+3` split with four total edges gives two P3 components and independence4; all other component-size splits have independence at least4.

Saturation also gives:

- the unique bridge owner support meets C in exactly two vertices;
- the two remaining side-owner supports meet C in exactly one vertex each;
- there are no omitted extra dense-base--C incidences.

## 4. K3 + K2 + K1 is impossible

Let Q be the K3 component, R the K2 component and z the isolated vertex.

Because D,E partition C into triples and each contains an internal target edge, only two partition types are possible up to exchanging D,E.

### 4.1 One support is Q

Then the other support is `R union {z}`. The pair geometry is exactly a target K3 anticomplete to a one-edge triple.

The generalized M=6 support-to-one-spoke bound still supplies at least14 one-spoke pivots: here `e_H(C)=4<6`, so `alpha(H[C])=3`, and the proof of the one-spoke count is unchanged for b=1.

The Type-A argument from `GLOBAL_D3_A2_M6_PAIR_GEOMETRY_REDUCTION.md` applies verbatim: every one-spoke pivot must hit the isolated vertex of the one-edge support, which has zero charge and core degree12. At least14 distinct core neighbours are impossible.

Hence this partition is empty.

### 4.2 Q is split 2+1

The support containing the single Q-vertex must also contain both vertices of R in order to have an internal edge. The other support consists of the remaining two Q-vertices and z.

Thus both D and E are one-edge supports, so

`w(D)=w(E)=0`.

All C-vertices are zero-charge. Since Q is target-connected, all three Q-vertices have the same incidence signature. The two R-vertices likewise have one common incidence signature.

A bridge support meeting C in exactly two vertices cannot exist:

- if it contains a Q-vertex, equal signature forces all three Q-vertices into the support, already giving three C-incidences;
- if it contains an R-vertex, equal signature forces both R-vertices, both belonging to the same side of the D/E partition; meeting the other side requires a third C-vertex.

Contradiction.

Therefore

> `K3 union K2 union K1` is impossible.                       (M10)

## 5. P4 + K2 is impossible

Write the path as

`v1-v2-v3-v4`

and the isolated edge as

`u1-u2`.

Up to exchanging D,E and reversing the path, the partition into two 3-supports with at least one internal edge each has only two edge-count types.

### 5.1 Both supports are one-edge supports

This is the `(1,1,2)` type: each support contains one internal target edge and there are two D--E cross edges.

Thus `w(D)=w(E)=0`; all six C-vertices are zero-charge.

The four path vertices form one target-connected zero-charge component, hence one incidence-signature class of size4. The two K2 vertices form another signature class of size2.

But the two side-owner supports must each meet C in exactly one vertex. Any support containing a C-vertex must contain its entire zero-signature class, so it meets C in at least two points (and a path vertex would force four).

Contradiction.

### 5.2 One support is one-edge and the other is P3

Up to labels,

`D={u1,u2,v1}`

is the one-edge support and

`E={v2,v3,v4}`

is the P3 support. The unique D--E cross target edge is `v1v2`.

The one-edge support has

`w(D)=0`.

The P3 has defect one, so

`w(E)<=1`.

If `w(E)=0`, then the entire target-connected P4 consists of zero-charge vertices; the edge `v1v2` would force v1 and v2 to have the same incidence signature although v1 belongs to D and v2 belongs to E. Impossible.

Hence

> `w(E)=1`,                                                   (M11)

with exactly one positive-charge vertex among `v2,v3,v4`.

#### Positive vertex v2

Then `v3,v4` are a zero-charge target edge and form a two-point signature block; `u1,u2` form another two-point block; v1 is the only singleton zero signature in C.

A bridge support must meet both D and E in exactly two C-points. It cannot overlap E at the positive vertex v2, because every proper overlap at allowance2 is a zero-charge saturation point. Using v3 or v4 forces both by equal signature, already two E-side points, after which a D-side point would be third.

So no bridge support exists. Contradiction.

#### Positive vertex v4

Then `v1,v2,v3` are target-connected zero-charge vertices and therefore one three-point incidence-signature class spanning D and E.

Any bridge support containing one of them contains all three and meets C in at least three points, contradicting the exact two-incidence bridge requirement.

Contradiction.

#### Positive vertex v3

This is the only scalar equality shape not killed immediately.

The zero-charge signature classes in C are

- `X={v1,v2}`;
- `Y={u1,u2}`;
- `Z={v4}`.

These already exhaust the three zero-charge signature classes allowed by `alpha(H)<=3`.

The bridge support is therefore forced to use exactly the pair X; its private third point must have positive charge, otherwise it would create a fourth zero signature.

Both side-owner supports must meet C in exactly one point. The only permissible singleton zero signature is Z, so both side supports contain v4.

Any private point of either side support must have positive charge; otherwise it creates another zero signature. Two distinct side supports cannot share an additional private point, because every proper-overlap point has zero charge and would again create a fourth signature. Hence their private petal pairs are disjoint.

Each side support has one zero-charge hub v4 and two positive private petals. At allowance2 this forces both private charges to equal1 and the support to be a target K3.

Row closure then gives target-anticompleteness between the two private K2 petal pairs.

Finally every vertex of D has zero charge and lies outside both side supports, so row closure makes D target-anticomplete to all four private petals.

Choose an internal target-nonedge pair from the one-edge support D and one private petal from each of the two side K3s. The two chosen petals are target-nonadjacent to each other and both are target-nonadjacent to D.

These four core vertices form an independent4-set, contradicting `alpha(H)<=3`.

Thus the last P4+K2 equality shape is impossible.

Therefore

> `P4 union K2` is impossible.                                (M12)

## 6. M=6 closure

Sections2--5 exclude every `b>=1` possibility. Together with `GLOBAL_ONESPOKE_CLIQUE_FORCING_THEOREM.md`, which closes the unique `b=0` Type-C terminal after the earlier Type-A/B exclusions, we obtain

> **M=6 all-bridge closure:**
>
> no fully-decorated q32 nine-owner A2 support system can have a maximal disjoint pair carrying six owners.   (M13)

Hence in every remaining fully-decorated N=9 survivor,

> `M<=5`.                                                      (M14)

The next bridge is now a weighted-cover theorem for maximal disjoint pairs with at least four owners outside the pair, not another M=6 case split.