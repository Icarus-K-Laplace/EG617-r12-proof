# Global d=3 A2 Connected Type-I Full Closure

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_A2_CONNECTED_SIGNATURE_CODE_REDUCTION.md`;
- `GLOBAL_D3_A2_CONNECTED_TYPEII_FULL_CLOSURE.md`;
- `GLOBAL_D3_A2_TWO_COMPONENT_FULL_CLOSURE.md`;
- `GLOBAL_D3_A2_LOW_CHARGE_COMPONENT_CAPACITY.md`;
- `GLOBAL_FULLY_DECORATED_TO_ONESPOKE_BRIDGE.md`;
- zero-charge incidence signatures and allowance-two overlap saturation;
- common-S row closure;
- inherited r=12 caps `D(17)=81`, `D(18)=87`;
- `alpha(H)<=3`, `omega(H)<=11`, and the fully-decorated q32 bound `W<=36`.

Purpose: close the final connected Type-I signature-code regime without owner-weight enumeration. Together with the preceding Type-II and two-component closures this eliminates the entire nine-owner fully-decorated allowance-two support escape.

## 1. Type-I code setup

By the connected signature-code reduction, Type I has two singleton zero-signature groups, labelled `1,2`, no singleton group `3`, and doubleton bridge codes among `12,13,23`.

Let `Z_i` be the full zero-signature class `i`, with size `z_i>=1` whenever the signature occurs. Let `k_i` be the number of distinct singleton-code support classes of code `{i}` for `i=1,2`.

Each doubleton code `ij` occurs for at most one distinct support class. The bridge-code graph Gamma on the represented signatures is connected.

Every proper overlap is allowance-two saturated, so all overlap vertices are zero-charge. Consequently every support-union vertex outside the represented zero-signature classes is positive-charge and private to its support class.

For a singleton-code support of code `{i}`, the number of positive private vertices is exactly

`3-z_i`.

For a doubleton bridge support of code `{i,j}`, the number is exactly

`3-z_i-z_j`.

Because a support has size3, every bridge edge `ij` satisfies

`z_i+z_j<=3`.                                                (I1)

The low-charge intersecting-component theorem gives the following class-count facts:

- a singleton code with `z_i=1` cannot have three distinct support classes, because that would be the forbidden three-class common-hub geometry; hence `k_i<=2`;
- a singleton code with `z_i=2` has at most three distinct classes;
- if `k_i>=2`, then `z_i<=2`.

## 2. One-spoke hit signatures

Let v be a legal one-spoke pivot produced by the fully-decorated support-to-one-spoke bridge. Then its common-S charge is

`w_v=1`.

Define the hit-signature set

`R(v)={i : v has a target neighbour in Z_i}`.

If `ij` is a bridge edge of Gamma, the bridge support contains the whole zero cores `Z_i union Z_j`. Row closure gives

`e_H(v,D_ij)<=1`.

Therefore v cannot hit both zero signatures i and j. Thus

> `R(v)` is an independent set of the bridge graph Gamma.    (I2)

We use the following elementary clique-forcing device repeatedly.

Suppose v,w both miss a zero signature k and there is a support D whose code does not contain k. Each of v,w has at most one target neighbour in the 3-support D, so their sets of target nonneighbours in D each have size at least2 and therefore intersect. Choose a common target-nonneighbour d in D. Any `z in Z_k` has zero charge and lies outside D, so row closure gives `zd` a target nonedge. Hence if `vw` were a target nonedge,

`{v,w,z,d}`

would be an independent4-set. Therefore

> whenever such k,D exist, `vw` is a target edge.            (I3)

## 3. Three-signature Type I forces at least fifteen one-spoke pivots

Assume all three zero signatures `1,2,3` occur. Since the bridge graph is connected, it has at least a spanning tree. By (I1), all `z_i` are 1 or2, and two size-2 signatures cannot be adjacent.

Let P be the number of positive private support-union vertices and put

`Z=z_1+z_2+z_3`.

Because positive private vertices of distinct support classes are disjoint,

`|U|=Z+P`, `W_U>=P`,                                        (I4)

where U is the full support union.

The three zero signatures have pairwise target-nonadjacent representatives, so

`alpha(H[U])=3`.                                             (I5)

We claim

> `2Z+P<=17`.                                                 (I6)

This is a short structural count.

### 3.1 Zero-size pattern 1,1,1

Here each singleton group has at most two distinct classes, so its private contribution is at most4. Every bridge support contributes one private point, and there are at most three bridge codes. Hence

`P<=4+4+3=11`, `Z=3`,

so `2Z+P<=17`.

### 3.2 Zero-size pattern 2,1,1

If the size-2 signature is one of the singleton groups, the singleton private contributions are at most `3+4=7`. The only bridge support with a positive private point is the possible edge joining the two size-1 signatures, so bridge-private contribution is at most1. Thus `P<=8`, `Z=4`, and `2Z+P<=16`.

If instead the size-2 signature is signature3, both singleton signatures have size1 and contribute at most8 private points total. Again only the edge between the two size-1 signatures can contribute a private bridge point, so `P<=9`, `Z=4`, and `2Z+P<=17`.

### 3.3 Zero-size pattern 2,2,1

The two size-2 signatures cannot be adjacent. Hence the size-1 signature is the center of the unique connected bridge path, and both bridge supports have no private point.

If both singleton signatures have size2, singleton private contribution is at most `3+3=6`, so `2Z+P<=16`.

If one singleton signature has size1 and the other size2, the private contribution is at most `4+3=7`, so `2Z+P<=17`.

This proves (I6).

The support-to-one-spoke theorem now gives

`k >= 32-2|U|+W_U`
`   >= 32-2(Z+P)+P`
`   =32-(2Z+P)`
`   >=15`.                                                    (I7)

So at least fifteen legal one-spoke pivots exist.

## 4. Triangle bridge graph: all one-spokes form a clique

Assume Gamma is the triangle `12,13,23`.

By (I2), every one-spoke hits at most one zero signature. For two one-spokes v,w, their hit-signature union has size at most2. Choose a signature k missed by both, and let `ij` be the opposite bridge edge.

Apply (I3) with the bridge support D_ij. Then `vw` is a target edge.

Thus all at least15 one-spoke pivots form a target K15, contradicting `omega(H)<=11`.

Hence the triangle bridge graph is impossible.

## 5. Path bridge graph: all one-spokes again form a clique

Assume Gamma is a path with center c and leaves a,b. The bridge supports are `D_ca,D_cb`.

At least one leaf is one of the singleton signatures 1,2, and therefore has a singleton-code support.

Take two one-spokes v,w.

### 5.1 Both miss the center

Choose `z in Z_c`. Let ell be a leaf that has a singleton-code support D_ell. Both v,w have at most one target neighbour in D_ell, so they have a common target-nonneighbour d in D_ell. Since z is zero-charge and lies outside D_ell, `zd` is a target nonedge. By (I3), `vw` is a target edge.

### 5.2 Both hit the center

By (I2), both miss both leaf signatures. Choose representatives `z_a in Z_a`, `z_b in Z_b`. Distinct zero signatures are target-nonadjacent. Hence if `vw` were a target nonedge, `{v,w,z_a,z_b}` would be independent4. Thus `vw` is a target edge.

### 5.3 One hits the center and the other misses it

Let v hit the center and w miss it.

If w misses at least one leaf, say a, then v also misses a by (I2). Use the opposite bridge support D_cb in (I3): both miss `Z_a`, so `vw` is a target edge.

It remains only to consider the extreme pattern in which w hits both leaves a,b.

#### 5.3.1 Center zero class has size2

Then each bridge support already contains the two points of Z_c plus one leaf zero point, so both leaf zero classes have size1 and the bridge supports have no private point.

The pivot v can hit at most one point of Z_c, while w hits a leaf and therefore misses all of Z_c in the corresponding bridge support. Hence there is a point `z' in Z_c` missed by both.

Choose a singleton support D_ell on a leaf ell. Its zero core has size1, so it has two positive private vertices. Since w hits the leaf zero core, it misses both private vertices; v has at most one target neighbour in D_ell and misses the leaf zero core, so v and w have a common private target-nonneighbour d. The zero vertex z' lies outside D_ell and is target-anticomplete to it. Thus `z'd` is a target nonedge, and `vw` must be a target edge.

#### 5.3.2 Center zero class has size1

For each leaf ell consider D_cell.

If `z_ell=2`, then D_cell consists of the center zero point and the two leaf-zero points. Since v hits the center and w hits at most one leaf-zero point, the other leaf-zero point is a common target-nonneighbour; call it d_ell.

If `z_ell=1`, then D_cell has one private point t_ell. The bridge supports D_ca,D_cb properly overlap in the one-point zero core Z_c, so allowance-two overlap saturation gives exact defect2. The two zero representatives in D_cell are target-nonadjacent. The private point cannot have zero charge, because that would create a fourth zero incidence signature. Therefore exact defect2 forces

- `w_(t_ell)=1`;
- `t_ell` target-adjacent to both zero representatives.

Because v hits the center and w hits the leaf, both miss t_ell. Put `d_ell=t_ell`.

We now have common target-nonneighbours d_a in D_ca and d_b in D_cb. They are target-nonadjacent:

- if both are leaf-zero points, they have distinct zero signatures;
- if one is a leaf-zero point and the other is a private point t, then t already sees the common center zero point and has charge1, so row closure against the opposite bridge support forbids the cross edge;
- if both are private points, each has charge1 and already sees the center zero point, so row closure against the opposite bridge support again forbids their edge.

Hence if `vw` were a target nonedge, `{v,w,d_a,d_b}` would be independent4. Therefore `vw` is a target edge.

All cases give `vw` a target edge. Thus the at least15 one-spoke pivots form a target K15, contradicting `omega(H)<=11`.

Therefore every three-signature Type-I regime is impossible.

## 6. Pure direct two-signature Type I

It remains to consider the case where only zero signatures 1 and2 occur. Connectedness forces the direct bridge code12, and there are no codes13 or23.

Thus all supports have code `1`, `2`, or `12`.

### 6.1 If the support union has independence number3

Let P be the positive private support-union count and `Z=z_1+z_2`.

The bridge support gives `z_1+z_2<=3`. As above, a size-1 singleton zero core supports at most two distinct support classes in the low-charge channel, while a size-2 core supports at most three.

If `(z_1,z_2)=(1,1)`, singleton private contribution is at most `4+4`, while the bridge has one private point. Hence `P<=9`, `Z=2`.

If `(z_1,z_2)=(2,1)` or `(1,2)`, singleton private contribution is at most `3+4`, while the bridge has no private point. Hence `P<=7`, `Z=3`.

Therefore in all cases

> `2Z+P<=13`.                                                 (I8)

If `alpha(H[U])=3`, the support-to-one-spoke theorem gives

> `k>=32-(2Z+P)>=19`.                                        (I9)

We claim all these one-spokes are pairwise target-adjacent.

For any one-spoke v, row closure against the bridge support D_12 gives at most one target edge into `Z_1 union Z_2`; hence v cannot hit both zero signatures.

Take v,w.

If they have a common missed zero signature i, choose a singleton support D_j of the other signature `j!=i`. They have a common target-nonneighbour d in D_j, while any `z in Z_i` is zero-charge and target-anticomplete to D_j. Thus `vw` must be a target edge.

The only remaining case is that v hits signature1 and w hits signature2.

If, say, `z_1=2`, then v hits at most one point of Z_1 and w, having hit Z_2, misses all of Z_1 in D_12. Hence there is `z' in Z_1` missed by both. Since `z_2=1`, a singleton support D_2 has two private vertices. The pivot w hits z_2 and misses both private vertices; v has at most one target edge into D_2 and misses z_2, so v,w have a common private target-nonneighbour d. The zero point z' is target-anticomplete to D_2, hence `z'd` is a nonedge and `vw` must be an edge. The case `z_2=2` is symmetric.

If `z_1=z_2=1`, the bridge support D_12 has a private point t. It properly overlaps both singleton groups at a one-point zero core, so exact allowance-two saturation and positivity of t force

- `w_t=1`;
- t target-adjacent to both zero representatives.

The pivots v,w both miss t. Choose a singleton support D_1. Since v hits z_1 it misses both private vertices of D_1; w misses z_1 and can hit at most one private vertex, so there is a common private target-nonneighbour d. The charge-one vertex t already sees z_1, so row closure against D_1 makes `td` a target nonedge. Thus `vw` must again be a target edge.

Hence all at least19 one-spokes form a target clique, contradicting `omega(H)<=11`.

### 6.2 If the support union has independence number at most2

We show first that each singleton group has exactly one distinct support class.

If, say, code1 had two distinct support classes, their common-core intersecting geometry supplies private vertices p,q from the two classes which are target-nonadjacent: for a size-1 common hub the private blocks are cross-anticomplete; for a size-2 common pair, exact row closure likewise makes the private petals cross-nonadjacent.

Any representative `z_2 in Z_2` is zero-charge and lies outside both code1 supports, so it is target-anticomplete to p and q. Hence `{z_2,p,q}` is an independent triple in U, contradiction.

Thus `k_1=k_2=1`.

The support union is then the union of exactly three support classes: one code1 support, one code2 support and the bridge support D_12. Positive private vertices are unique to their classes. Therefore

`|U| = (z_1+z_2) + (3-z_1)+(3-z_2)+(3-z_1-z_2)`
`    = 9-(z_1+z_2)`.

Since `z_1+z_2` is 2 or3,

> `|U| in {6,7}`.                                             (I10)

The canonical dense owner base is the target K11

`B={p} union Y union {r}`.

The nine owners contribute exactly27 distinct target edges from B into their 3-point core supports in U. Hence

`e_H(B union U) >=55+27+e_H(U)`.                             (I11)

Because `alpha(H[U])<=2`, the complement of H[U] is triangle-free, so Mantel gives

- for `|U|=6`, `e_H(U)>=6`;
- for `|U|=7`, `e_H(U)>=9`.

If `|U|=6`, the 17-point set B union U has at least

`55+27+6=88`

target edges, exceeding `D(17)=81`.

If `|U|=7`, the 18-point set B union U has at least

`55+27+9=91`

target edges, exceeding `D(18)=87`.

Both are impossible.

Therefore the pure direct two-signature Type-I regime is impossible as well.

## 7. Type-I full closure

Sections3--5 exclude every three-signature Type-I connected code system. Section6 excludes the pure direct two-signature system.

Hence:

> **Connected Type-I full closure.**
> No final fully-decorated q32 nine-owner allowance-two support system can realize the Type-I signature-code regime.   (I12)

Combined with

- the two-component full closure;
- the connected Type-II full closure;
- the connected signature-code dichotomy;

this eliminates every nine-owner fully-decorated support escape.

Consequently, together with the earlier non-full-decoration theorem:

> **q32 d3 nine-owner full closure:** no simultaneous nine-owner q32 d3 system exists in the retained CORE211 channel.

Together with the ten-owner closure, the simultaneous q32 d3 owner capacity is therefore at most eight.

## 8. Generalization

The proof exposes a reusable signature-code mechanism:

1. zero-charge incidence signatures compress the overlap graph to a small code graph;
2. bridge supports make one-spoke hit-signature sets independent in that graph;
3. a small positive-private footprint forces many one-spoke pivots;
4. code-graph connectivity then converts those pivots into an oversized target clique;
5. if the support union is too dense to generate one-spokes, the dense owner base plus a Mantel lower bound violates a hereditary cap directly.

This mechanism is parameterized by the zero-signature capacity and hereditary cap and is not intrinsically tied to the E334 label.
