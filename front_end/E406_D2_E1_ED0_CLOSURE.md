# E406 d2-e1 terminal: closure of the e_D=0 branch

Status: `PROVED EMPTY` for the `e_D=0` subbranch of the unique d2-e1 terminal. E406 remains `OPEN`.

Dependencies:

- `E406_D2_E1_CLEAN_SUPPORTS.md`;
- near-284 PAIR-13;
- the E406 core floor / minimum-degree theorem.

Assume the d2-e1 terminal and additionally `e_D=0`.

Then the exchanged old-core pair D is a target nonedge of two degree12 vertices. Every clean support `U_t` is target-anticomplete to D and lies in

`X = {core vertices target-nonadjacent to both vertices of D}`.

Because `alpha(C)<=4`,

`alpha(C[X])<=2`: an independent triple in X together with the independent pair D would form an independent5-set in C.

There are at least five clean pivots.

## 1. A stronger support-incidence budget

Let `k_x` be the number of clean supports containing a core vertex x.

The original retained T-block has one decorated missing edge whose two endpoints carry total decoration7. Those two vertices remain in the shell after repivoting any clean t.

If `U_t={a,b}`, then after repivoting t the support vertices a,b enter the shell. Their global degrees give new-shell decorations at least

`epsilon_a+k_a-1`,
`epsilon_b+k_b-1`.

Thus the support pair consumes at least

`epsilon(U_t)+k_a+k_b-2`

additional decoration beyond the retained7 units.

### Type A

A Type-A support is a target nonedge with epsilon=0 and q_t=31. Since q31 has `G<=9`,

`k_a+k_b<=4`.      (A-inc)

### Type B

A Type-B support is a target edge with epsilon=0 and q_t=30. Since q30 has `G<=8`,

`k_a+k_b<=3`.      (B-inc)

### Type C

A Type-C support is a target edge with epsilon=1 and q_t=31. Again `G<=9`, so

`k_a+k_b<=3`.      (C-inc)

In particular Type-B and Type-C support classes cannot repeat.

## 2. Cross-edge bound between distinct clean supports

Let U,V be distinct clean supports and repivot at the shell vertex carrying U.

Every vertex of V remains in the new core. Since both U and V are target-anticomplete to S, retained vertices receive no compensation from the imported S-pair. Minimum degree12 therefore gives

`e_C(U,V) <= epsilon(V)`.

Interchanging U,V gives

`e_C(U,V) <= min(epsilon(U),epsilon(V))`.      (CROSS)

Consequences:

- any pair involving Type A or Type B supports is target-anticomplete when the supports are disjoint;
- two disjoint Type-C supports have at most one cross target edge.

The PAIR-13 overlap analysis from `E406_D2_E1_CLEAN_SUPPORTS.md` also gives:

- a Type-B support has no proper one-point overlap with another distinct support;
- if two Type-C supports overlap, the shared endpoint is regular and their two nonshared endpoints carry the two distinct excess units.

## 3. Type A is impossible

Let U={a,b} be a Type-A support. It is a target nonedge in X.

Since `alpha(X)<=2`, every vertex of every other clean support must be target-adjacent to at least one of a,b. But a support disjoint from U is target-anticomplete to U by CROSS because `epsilon(U)=0`.

Therefore every clean support intersects U.

Counting clean-support incidences on a,b gives

`k_a+k_b >= number of clean pivots >=5`,

contradicting (A-inc).

Hence there are no Type-A clean supports.

## 4. Type B is impossible

There are at least five clean pivots and every Type-B/Type-C class is nonrepeating, so there are at least three distinct support classes.

Suppose U is Type B. By CROSS, U is target-anticomplete to every other distinct support.

Take two other distinct supports V,W.

- if either has zero excess, V and W are target-anticomplete;
- if both are Type C, their cross graph has at most one target edge, so one can choose `v in V`, `w in W` with `vw` a target nonedge.

Choose any `u in U`. Then `{u,v,w}` is an independent triple in X, contradicting `alpha(X)<=2`.

Therefore there are no Type-B clean supports.

## 5. Five or more Type-C supports force an independent transversal

All clean supports are now Type C.

Each distinct Type-C support needs one unit of old-core excess. If two such supports overlap, their shared endpoint is regular and their two nonshared endpoints carry two distinct excess units. Hence distinct Type-C supports consume distinct positive-excess vertices.

The old q30 core has only six total excess units, so there are at most six clean supports; in particular there are five or six distinct Type-C supports.

By (C-inc), for every support edge `{a,b}` the support-incidence degrees satisfy

`k_a+k_b<=3`.

Therefore the graph whose edges are the Type-C supports has components only of the forms

- an isolated edge;
- a two-edge path P3.

With at least five edges, it has a matching of size at least3. Choose three vertex-disjoint Type-C supports U,V,W.

By CROSS, between each pair of supports there is at most one target edge.

There are `2^3=8` choices of one endpoint from each support. A fixed cross edge between one pair forbids exactly two of the eight choices. There are at most three support pairs, so at most six choices are forbidden.

Hence some transversal `{u,v,w}` contains no target edge. It is an independent triple in X, contradicting `alpha(X)<=2`.

## 6. Conclusion

The `e_D=0` branch of the unique d2-e1 terminal is empty.

Therefore every remaining d2-e1 survivor must satisfy

`e_D=1`.

The exchanged old-core pair D is a target edge with total old-core excess exactly1. This is now the sole d2 final-rise subbranch.