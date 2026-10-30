# M10 residual graph and light-component classification

Date: 2026-10-30  
Status: PROVED necessary-condition catalog; full Q32 compatibility remains OPEN.

## 1. Seven-vertex residual slack

Let R be the seven-vertex set outside the ten pivot blocks Q_1,...,Q_10. Let X,Y,Z be the pivot slack variables (renamed to avoid collision with the source special point x_C). The registered ledger is

    X+Y+Z=32
    2X+Y>=50
    8<=Y+2Z<=14.

Consequently

    0<=Z<=7
    X>=18+Z
    max(0,8-2Z)<=Y<=14-2Z.

For r in R put b_r=sum_i(|N_H(r) intersect Q_i|-1). Then

    sum_r b_r=Y
    d_R(r)+b_r>=2
    B_min(R):=sum_r max(0,2-d_R(r)) <= Y.

The core contract gives alpha(R)<=4.

## 2. Why clique-cover number at most four is a theorem, not an input assumption

For each pivot block Q_i, define

    B_i={r in R: |N_H(r) intersect Q_i|>=2}.

Then |B_i|<=y_i, where y_i=sum_r(|N(r) intersect Q_i|-1). On R minus B_i, each residual vertex has a unique neighbor in Q_i. The independent-pair incidence lemma forces the fibers of this unique-neighbor map to be cliques in R. Equivalently,

    chi(complement(R-B_i))<=4,
    chi(complement(R))<=4+|B_i|<=4+y_i.

Summing over the ten blocks gives

    Y>=10(chi(complement(R))-4)

whenever the right side is positive.

- If chi(complement(R))>=6, then Y>=20, contradicting Y<=14.
- If chi(complement(R))=5, the complement is K5-free and 5-chromatic on seven vertices. A 5-critical subgraph must use all seven vertices and has minimum degree at least four, so Delta(R)<=2. The seven-vertex maximum-degree-two classification together with alpha(R)<=4 leaves exactly R=C5 dot-union 2K1. Thus e(R)=5, Z=2, and B_min(R)=4.
- In this exceptional graph, Y<=14-2Z=10. The degree floor at the two isolated residual vertices requires at least two extra Q-incidences at each. The incidence proof in V47_RESIDUAL_INCIDENCE_COVER.md, Section 7, shows that no block's unique extra incidence can be placed at an isolated residual vertex. Since the total budget is exactly Y=10, each of the ten blocks has exactly one extra incidence, and the two isolated vertices cannot receive the required four incidences. Contradiction.

Therefore every original full-support m=10 candidate satisfies

    chi(complement(R))<=4,

or equivalently R has a partition into at most four cliques. This conclusion is source-correct and does not assume y_i=0 for all ten blocks.

The excluded 5-chromatic residual is exactly one isomorphism type, graph6 code FLo??, with 252 labelled copies. It passes the scalar B_min budget; it is excluded by the incidence argument above, not by the scalar degree filter.

## 3. Exhaustive residual-graph relaxation

All seven-vertex simple graphs with 3 through 10 edges were considered. For each Z, the filters were applied in this order:
1. alpha(R)<=4;
2. clique-cover-number(R)<=4, justified by Section 2;
3. B_min(R)<=14-2Z.

The non-isomorphic survivors are represented by graph6 codes in M10_RESIDUAL_GRAPH_CATALOG.csv. The catalog has 371 pairwise non-isomorphic representatives. Their orbit-stabilizer sum is exactly 797,072, the independently enumerated labelled survivor count.

| Z | e(R) | Y upper bound | Non-isomorphic types | Connected R types | Ordered four-clique-fiber maps |
|---:|---:|---:|---:|---:|---:|
| 0 | 3 | 14 | 1 | 0 | 24 |
| 1 | 4 | 12 | 3 | 0 | 96 |
| 2 | 5 | 10 | 10 | 0 | 528 |
| 3 | 6 | 8 | 30 | 6 | 2,160 |
| 4 | 7 | 6 | 56 | 28 | 6,576 |
| 5 | 8 | 4 | 91 | 63 | 16,800 |
| 6 | 9 | 2 | 118 | 101 | 35,460 |
| 7 | 10 | 0 | 62 | 62 | 31,476 |
| Total | — | — | 371 | 260 | 93,120 |

For a particular graph in the CSV, the allowed Y values start at max(0,8-2Z,B_min) and end at 14-2Z. The CSV records Z, graph6 representative, B_min, and the exact number of ordered maps f:R->[4] whose fibers are cliques. Empty fibers are allowed.

For each graph type, a second partition G is an independent copy of the same four-clique-fiber assignment space before the cross-map and outer-track conditions are imposed. The raw number of ordered (F,G) pairs across the catalog is 34,794,144. This is a candidate-pair count, not a count of globally compatible Q32 assignments.

## 4. Labelled enumeration counts

The independent labelled enumeration covered every graph on seven labelled vertices with e=3,...,10, a total of 1,048,344 graphs.

| Stage | Count |
|---|---:|
| All labelled graphs with 3..10 edges | 1,048,344 |
| alpha(R)<=4 | 1,014,289 |
| alpha(R)<=4 and clique-cover(R)<=4 | 1,014,037 |
| Further rejected by B_min budget | 216,965 |
| Final labelled residual graphs | 797,072 |
| The excluded C5 dot-union 2K1 labelled copies | 252 |

The 252 exceptional graphs all have Z=2, e(R)=5, B_min=4 and are precisely the labelled copies of C5 dot-union 2K1. They are excluded by Section 2's incidence contradiction.

There are 260 connected and 111 disconnected isomorphism types. This is connectivity of R, not connectivity of the ten-block light graph L.

## 5. Fiber assignment enumeration

For every one of the 371 graph6 representatives, enumerate all 4^7 maps from the seven residual vertices to four labelled fiber names and retain exactly those maps whose fibers are cliques. The verified counts are:
- 93,120 ordered single-fiber maps;
- 34,794,144 ordered pairs of maps (F,G), before requiring the two partitions to agree, before matching compatibility, and before any outer weighted-heavy graph is attached.

The verifier can emit all 93,120 maps with --dump-fibers and all 797,072 labelled residual graph masks with --dump-labelled-graphs.

## 6. Scope firewall

This is a necessary-condition catalog, not a full 47-vertex Q32 enumeration. It does not impose:
- the block-indexed incidence vectors a_ri;
- the compatibility of two fiber maps F,G;
- all ten-block weighted-heavy graphs;
- all pairwise matching permutations and extra-edge endpoints;
- every source gadget edge placement from M10_SOURCE_PROFILE_CATALOG.md;
- the global edge-disjointness of the ten exact colors plus the remaining nonexact color;
- the target clique cap on the entire 47-core after all blocks are attached.

The 3+7 branch has its own stronger source-derived contract and is conditionally excluded by the Astra theorem. The 371-type catalog does not close any of the other light-component profiles.

## 7. Component-specific residual budget refinements

The generic B_min<=14-2z catalog can be sharpened inside 4+6:
- K4 small side: B_min<=10-2z, z=0,...,5, leaving 79 types / 121,782 labelled graphs / 9,600 fiber maps.
- K4-e small side: B_min<=8-2z; after the already-closed z=4 slice, z=1,2,3 leaves 15 types / 11,662 labelled graphs / 1,176 fiber maps.

The filtered graph6 representatives and exact fiber-profile counts are recorded in M10_4PLUS6_TIGHT_RESIDUAL_FILTER.csv. These remain necessary residual relaxations, not complete 47-core configurations.
