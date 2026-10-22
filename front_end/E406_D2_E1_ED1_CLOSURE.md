# E406 d2-e1 terminal: closure of the e_D=1 branch

Status: `PROVED EMPTY` for the `e_D=1` subbranch. Together with `E406_D2_E1_ED0_CLOSURE.md` and `E406_D2_EGE2_CLOSURE.md`, this closes the entire E406 distance-2 final-rise class.

Assume the unique d2-e1 terminal from `E406_D2_E1_CLEAN_SUPPORTS.md` and now `e_D=1`.

Thus D={d0,d1} is a target edge with total old-core excess1. Relabel so

- d0 has old-core excess0;
- d1 has old-core excess1.

The terminal bounds give

- `A=e(S,T)<=1`;
- `B=e(D,T)<=1`.

Among the eight undecorated T-isolates, at most one is incident with an S-T edge and at most one with a D-T edge. Therefore there are at least

`8-1-1=6`

clean pivots.

For each clean pivot t let `U_t={a,b}` be its 2-row.

## 1. Every clean support lies in a set of independence number at most3

Every clean t is target-anticomplete to S and D.

Repivoting t replaces U_t by S in the 47-core. Since d0 has old-core degree12, is retained, and gains no neighbour from S, minimum degree12 in the new core forces

`e_R(d0,U_t)=0`.

Hence every clean support lies in

`X={x in C: xd0 is a target nonedge}`.

If X contained an independent4-set, adding d0 would give an independent5-set in the old 47-core, contradicting `alpha(C)<=4`. Thus

`alpha(C[X])<=3`.      (X3)

## 2. Support-incidence budgets

Let `k_x` be the number of clean supports containing x.

The retained decorated T-edge carries total decoration7 and remains in the shell after every clean repivot. If `U_t={a,b}`, the two inserted support vertices contribute at least

`epsilon(U_t)+k_a+k_b-2`

additional decoration.

Therefore:

- Type A (target nonedge, epsilon0, q=31): `k_a+k_b<=4`;
- Type B (target edge, epsilon0, q=30): `k_a+k_b<=3`;
- Type C (target edge, epsilon1, q=31): `k_a+k_b<=3`.

In particular Type-B and Type-C support classes cannot repeat; a Type-A class has multiplicity at most2.

For distinct supports U,V, because both are target-anticomplete to S, repivoting one support gives the retained other support no compensation. Minimum degree12 yields

`e_C(U,V)<=min(epsilon(U),epsilon(V))`.      (CROSS)

Thus any pair involving a Type-A or Type-B support is cross-anticomplete when disjoint; two Type-C supports have at most one cross edge.

The PAIR-13 overlap analysis gives additionally:

- a Type-B support cannot properly overlap another distinct support;
- two overlapping Type-C supports share a regular endpoint and their two nonshared endpoints carry distinct excess units.

## 3. Type A is impossible

Let U={a,b} be a Type-A support. Then ab is a target nonedge and both vertices lie in X.

The support instance U itself contributes2 to `k_a+k_b`. Every other clean support intersecting U contributes at least1. Since `k_a+k_b<=4`, at most two other clean support instances can intersect U.

There are at least six clean pivots, so at least three other support instances are disjoint from U.

Among these three disjoint instances their support union must contain a target nonedge pair:

- if one is Type A, use its internal nonedge;
- if one is Type B and another is distinct, CROSS gives a cross nonedge;
- if all three are Type C, three distinct Type-C supports cannot lie in one support-incidence component because every Type-C edge satisfies endpoint support-degree sum at most3; hence two lie in different components, and regular representatives from distinct components are target-nonadjacent.

Choose such a nonedge pair v,w. Since U has zero defect and is disjoint from their supports, CROSS makes both a,b target-nonadjacent to v,w. Thus

`{a,b,v,w}`

is an independent4-set in X, contradicting (X3).

Therefore no clean support is Type A.

## 4. The B/C support-incidence graph

All clean supports are now Type B or Type C and are distinct.

Make a graph F whose vertices are core vertices used by clean supports and whose edges are the support pairs. The incidence budget `k_a+k_b<=3` on every support edge implies every component of F is either

- an isolated edge, or
- a two-edge path P3.

Indeed any three-edge connected component contains an edge whose endpoint degrees sum at least4.

Type-B supports are isolated components because proper overlaps are impossible. A P3 component consists of two Type-C supports sharing their common regular endpoint.

For each component choose a **regular representative**:

- for an isolated Type-B edge, choose either endpoint;
- for an isolated Type-C edge, choose its regular endpoint;
- for a Type-C P3, choose the shared regular centre.

Regular representatives from distinct components are pairwise target-nonadjacent. This follows from CROSS and the vertexwise minimum-degree condition: every cross edge between Type-C supports must join their excess endpoints, while Type-B supports are cross-anticomplete to every distinct support.

## 5. Four components give an independent6-set

Suppose F has at least four components.

Choose regular representatives r1,r2,r3 from three components, and choose a clean pivot t whose support lies in a fourth component. Pick any s in S.

Then the six vertices

`{s,d0,r1,r2,r3,t}`

are pairwise target-nonadjacent:

- s is anticomplete to D and to every clean support;
- d0 is anticomplete to every clean support by Section1;
- r1,r2,r3 are pairwise nonadjacent by the component choice;
- t is clean, so t is nonadjacent to s,d0;
- t has core neighbours only in its own 2-row, hence it is nonadjacent to representatives from the other three components.

This is an independent6-set in the T61 parent, contradiction.

Hence F has at most three components.

## 6. Three components force too much core excess

There are at least six distinct clean support edges, while every component contains at most two edges. Therefore F has exactly three components and exactly six support edges, with every component a P3.

Hence all six supports are Type C.

In a Type-C P3 the shared centre is regular and the two nonshared endpoints carry two distinct positive excess units. Therefore six Type-C supports in three P3 components consume six distinct units of old-core excess.

But D already contains the separate excess1 vertex d1, and clean supports are disjoint from D. Thus the old q30 core would have at least

`6+1=7`

units of excess above degree12.

Its exact total excess is only6. Contradiction.

## 7. Conclusion

The `e_D=1` branch of the d2-e1 terminal is empty.

Together with the previously proved `e_D=0` closure and the `e>=2` retained-star closure:

> **D2-CLOSURE. No E406 q30->q31 final-rise edge of distance2 exists.**
