# E408 whole-layer exact-color-count closure

Updated: 2026-10-27
Status: **PROVED_CONDITIONAL E408 ENERGY-LAYER CONTRADICTION** under the genuine h13 T61 full-color residual contract, the exact-129 Type-I equality classification, the registered pointwise degree floors, and the cited extremal theorems.

This file records an important dependency simplification: the argument originally written as `Q32_EXACT_COLOR_COUNT_COLLAPSE.md` does not use q=32, the 285-edge core, the seven-block equality system, or any witness-support theorem. It excludes every genuine E408 h13 T61 residual directly.

## 1. Residual color ledger uses only E=408

Let R be a genuine 61-vertex E408 target residual. It has

\[
\binom{61}{2}=1830
\]

pairs, of which 408 have the target color. Hence the eleven non-target colors together use

\[
1830-408=1422
\]

residual edges.

For every non-target color C, the balanced-coloring condition gives

\[
\alpha(C[R])\le12,
\]

while target independence in R gives

\[
\omega(C[R])\le5.
\]

The Brouwer--Kang--Pikhurko second-Turan theorem in complement form gives

\[
e_C(R)\ge129.
\]

Write

\[
e_C(R)=129+s_C,\qquad s_C\ge0.
\]

Then purely from the residual edge partition,

\[
\sum_C s_C=1422-11\cdot129=3.\tag{1}
\]

Therefore the number m of exact-129 non-target colors belongs to

\[
\boxed{m\in\{8,9,10\}}.\tag{2}
\]

No outer seven-block ledger is used in (1) or (2).

## 2. Exact colors and exceptional injectivity

For an exact-129 color the registered Type-I equality classification has one exceptional residual vertex of color-degree nine; all other residual vertices have color-degree at least four.

The exceptional-injectivity degree argument is likewise q-independent. If a residual vertex v is exceptional for n_v exact colors, then exact colors contribute at least

\[
4m+5n_v
\]

degree at v. The target color has degree at least13 because R is h13. For nonexact colors the registered pointwise floors are:

- s=1: degree at least3;
- s>=2 with total excess at most3: degree at least2.

For m=8,9,10 the minimum combined nonexact contribution is respectively 6,3,2? More precisely the only excess partitions are:

- m=8: 1+1+1, floor 3+3+3=9;
- m=9: 1+2, floor 3+2=5;
- m=10: 3, floor at least2.

These stronger values in particular imply n_v<=1 in every case. Thus all m exact exceptional vertices are distinct.

The older `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md` used weaker safe combined floors and reached the same conclusion; no 285-edge core identity entered that proof.

## 3. Nonexact low-degree lemmas

The analytic lemmas from `Q32_EXACT_COLOR_COUNT_COLLAPSE.md` depend only on residual color parameters.

### 3.1 131-edge color

If D has 131 edges and a degree-two vertex v, its 58-point nonneighbourhood N has alpha<=11 and omega<=5, hence at least129 edges by the second-Turan theorem. The two v-edges then exhaust the global edge count and force v's two neighbours to have degree one, contradicting the registered s>=2 degree floor. Therefore

\[
\delta(D)\ge3.\tag{3}
\]

### 3.2 130-edge color

If D has 130 edges and d_D(v)=3, the 57-point nonneighbourhood has at least124 edges. The remaining six degree incidences force v and its three neighbours to form an isolated K4. Thus every degree-three vertex lies in an isolated K4.

Two isolated K4s are impossible: deleting them leaves 53 vertices and118 edges with alpha<=10 and omega<=5, but the second-Turan lower bound is119. Hence

\[
\#\{v:d_D(v)=3\}\le4.\tag{4}
\]

### 3.3 132-edge color

A degree-two vertex in a 132-edge color lies in an isolated K3 by the same 58-point argument. Four isolated K3s are impossible because deleting them leaves a 49-vertex,120-edge graph with alpha<=8, below the elementary Turan floor p_8(49)=126. Hence

\[
\#\{v:d_D(v)=2\}\le9.\tag{5}
\]

## 4. Exclude every exact-color count

### m=10

The unique nonexact color has132 edges. At each of the ten distinct exact exceptional vertices x,

\[
d_D(x)\le60-13-9-9\cdot4=2.
\]

The pointwise floor gives equality. Thus D has at least ten degree-two vertices, contradicting (5).

### m=9

The two nonexact colors have130 and131 edges. At every exact exceptional vertex,

\[
d_{130}(x)+d_{131}(x)\le60-13-9-8\cdot4=6.
\]

By the pointwise floors and (3), both degrees equal3. Thus the 130-edge color has at least nine degree-three vertices, contradicting (4).

### m=8

The three nonexact colors all have130 edges. At each of the eight distinct exact exceptional vertices,

\[
d_1(x)+d_2(x)+d_3(x)\le60-13-(9+7\cdot4)=10.
\]

Each degree is at least3, so at least two are exactly3. Across eight exceptional vertices this demands at least16 degree-three incidences, while (4) gives total capacity at most 3*4=12. Contradiction.

Therefore all possibilities in (2) are impossible.

## 5. Whole-layer theorem

We conclude

\[
\boxed{\text{No genuine E408 h13 T61 residual exists}.}
\]

This conclusion is independent of the regular-pivot maximum charge Q. In particular it simultaneously eliminates the historical Q=31,32,33 subfrontiers.

Consequences:

1. the E408 V9/V11 charge reduction is no longer load-bearing for the root proof;
2. the Q33 31-point/56-witness closure remains valid but is now redundant for full E408 exclusion;
3. the Q32 285-edge support program remains a valid independent audit but is also redundant for whole-layer exclusion;
4. the E408 seven-block equality theorem is not needed by this shortest route.

## 6. Dependency firewall

Load-bearing inputs:

- genuine 61-point h13 T61 residual with E=408;
- balanced-coloring consequence alpha(C[R])<=12 for each non-target color;
- omega(C[R])<=5;
- second-Turan lower bound giving 129 and the stated smaller induced-subgraph bounds;
- exact-129 Type-I equality degree structure;
- the pointwise minimum-degree floors for s=1 and s>=2 residual colors;
- target minimum degree13;
- unique edge ownership / total vertex degree60.

Not used:

- q=32 or q=33;
- e(H)=284 or285;
- support sizes 31,41,44,47;
- seven outer K12 blocks;
- P_C,R_C duplicate budgets;
- V9/V10/V11 charge classification;
- SAT/ILP or graph enumeration.

Thus the correct promotion is an E408 energy-layer theorem, not merely a Q32 terminal theorem.
