# Global d=3 A2 M=6 Pair-Geometry Reduction

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_A2_TWO_BLOCK_INCIDENCE_BUDGET.md`;
- `GLOBAL_FULLY_DECORATED_TO_ONESPOKE_BRIDGE.md`;
- common-S row closure and zero-charge signature theorem;
- `alpha(H)<=3`.

Purpose: classify and eliminate two of the three possible disjoint-pair equality geometries in the final `M=6,b=0` window.

## 1. Setup

Let D,E be the maximal disjoint pair with

`m_D+m_E=6`, `b=0`.

The two-block budget gives

`e_H(D union E)<=5`.                                        (G1)

Because D,E are disjoint 3-supports and every support has at least one internal target edge, write

`e_D=e_H(D)`, `e_E=e_H(E)`, `c=e_H(D,E)`.

The ambient core has `alpha(H)<=3`.

## 2. Only three pair geometries survive alpha<=3 and e<=5

If one support has one internal edge, its support charge is zero. Row closure then forces c=0.

A one-edge support has independence number2. Hence if the other support also has at most two internal edges, choosing an internal nonedge pair from each gives an independent4-set.

Therefore a one-edge support can coexist only with a target K3, giving

> Type A: `(e_D,e_E,c)=(1,3,0)` up to exchange.              (G2)

Assume now both supports have at least two internal edges.

If both have two edges, each is a P3 with one internal nonedge pair. To avoid the union of those two pairs being an independent4-set, at least one cross target edge is necessary. Budget (G1) allows exactly one:

> Type B: `(2,2,1)`.                                         (G3)

If one support is a P3 and the other a K3, the internal edge count already equals5, so no cross edge is allowed:

> Type C: `(2,3,0)` up to exchange.                           (G4)

Two K3s would contribute six internal edges and violate (G1).

Thus Types A--C exhaust the M=6,b=0 pair geometry.

## 3. Type A is impossible by one-spoke hitting capacity

Let D be the one-edge support and E the K3.

Since D has one internal edge, its support charge is zero. Write its edge as ab and let c_D be its isolated third vertex.

D and E are target-anticomplete.

The fully-decorated support-to-one-spoke bridge gives at least

`k>=14`

legal one-spoke pivots in this M=6,b=0 window.

Take any such one-spoke pivot v. It has common-S charge1, so row closure allows at most one H-neighbour in D and at most one in E.

Suppose v were not target-adjacent to the isolated vertex c_D.

- if v has no neighbour in D, choose either internal nonedge pair involving c_D;
- if its unique D-neighbour is a, choose the nonedge pair `{b,c_D}`;
- if its unique D-neighbour is b, choose `{a,c_D}`.

In every case there is an internal nonedge pair `{x,c_D}` in D consisting of v-nonneighbours.

Since v has at most one neighbour in the K3 E, at least two vertices of E are v-nonneighbours. Choose any one, e.

Because D--E has no target edges,

`{x,c_D,e}`

is an independent triple contained in the anti-neighbourhood Z_v of v.

But every one-spoke anti-neighbourhood satisfies `alpha(H[Z_v])<=2`.

Contradiction.

Hence every one-spoke pivot must be target-adjacent to c_D.

The vertex c_D has common-S charge zero, so `kappa_(c_D)=0` and its H-degree is exactly12.

Therefore it has at most12 H-neighbours in total, whereas at least14 distinct one-spoke vertices would all have to be its neighbours.

Contradiction.

Thus

> Type A is impossible.                                      (G5)

## 4. Type B is impossible by exact one-incidence equality

Now D and E are both P3s and there is exactly one cross target edge.

A P3 has missing-edge defect1 and therefore total support charge at most1.

The unique cross edge is required to destroy the independent4 formed by the two internal P3 nonedge pairs. Consequently it must join one endpoint of the nonedge pair in D to one endpoint of the nonedge pair in E.

Row closure implies both cross-edge endpoints have positive common-S charge. Since each support has total charge at most1, those endpoints carry the entire charge of their respective supports.

Thus, in each P3,

- the cross-edge endpoint has charge1;
- the center and the opposite endpoint have charge0.

The latter two vertices are target-adjacent inside the P3. By the zero-charge signature theorem they therefore have the same support-incidence signature.

The two-block budget is saturated in Type B:

`2M+b+e_H(D union E)=12+0+5=17`.

Hence every one of the remaining three owner rows must contribute exactly one target incidence into C=D union E. Equivalently every remaining support class must meet C in exactly one vertex; there is no room for a second C-incidence.

But a proper support overlap can occur only at a zero-charge vertex.

- the positive cross-edge endpoints cannot be shared;
- either of the two zero vertices in one P3 has exactly the same incidence signature as the other, so any support containing one must contain both.

Therefore no distinct support class can meet D or E in exactly one vertex.

This contradicts the existence of the remaining three owner rows.

Hence

> Type B is impossible.                                      (G6)

## 5. Unique surviving M=6,b=0 geometry

The only pair geometry not excluded by Sections3--4 is

> **Type C:** one P3 support and one target K3 support, with no target cross edge between them.   (G7)

Moreover the two-block incidence budget is saturated:

`e_H(D union E)=5`,

so every remaining owner support meets `D union E` in exactly one core vertex and there are no omitted r--C target edges.

Thus the final M=6,b=0 problem has been reduced from arbitrary two-block attachments to a unique P3-plus-K3 equality geometry.

## 6. Next bridge

Let D be the P3 and E the K3.

Every one-spoke pivot must hit the unique internal nonedge pair of D. Hence all at-least14 one-spoke pivots are target-adjacent to one of two specified D endpoints.

The remaining task is an endpoint-capacity / zero-signature equality analysis of this unique Type-C geometry.

This is a single equality structure, not an E-layer case family.
