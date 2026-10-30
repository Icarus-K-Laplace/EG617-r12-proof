# M10 residual graph and light-component classification

Status: PROVED necessary-condition catalog; full Q32 compatibility remains OPEN.

## 1. Seven-vertex residual slack

Let R=H\\(Q_1 union ... union Q_10), |R|=7. Let X,Y,Z be the pivot slack variables (renamed here to avoid collision with the source special point x_C). The registered ledger is

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
    B_min(R):=sum_r max(0,2-d_R(r))<=Y.

The residual-incidence cover theorem gives alpha(R)<=4 and clique-cover-number(R)<=4. The latter is equivalent to four-colorability of the complement of R. These are necessary conditions; they do not encode all ten block-neighborhood maps.

## 2. Exhaustive residual-graph relaxation

All seven-vertex simple graphs with 3 through 10 edges were considered. For each Z, the filters were applied in this order:
1. alpha(R)<=4;
2. clique-cover-number(R)<=4;
3. B_min(R)<=14-2Z.

The non-isomorphic survivors are represented by graph6 codes in M10_RESIDUAL_GRAPH_CATALOG.csv. The pure-Python verifier checks the representatives, computes their automorphism groups, and proves catalog completeness by orbit-stabilizer: the sum of labelled orbit sizes is exactly 797,072, the independently enumerated labelled survivor count.

| Z | e(R) | Y interval before B_min | Non-isomorphic types | Connected R types | Ordered four-fiber maps |
|---:|---:|---:|---:|---:|---:|
| 0 | 3 | 8..14 | 1 | 0 | 24 |
| 1 | 4 | 6..12 | 3 | 0 | 96 |
| 2 | 5 | 4..10 | 10 | 0 | 528 |
| 3 | 6 | 2..8 | 30 | 6 | 2,160 |
| 4 | 7 | 0..6 | 56 | 28 | 6,576 |
| 5 | 8 | 0..4 | 91 | 63 | 16,800 |
| 6 | 9 | 0..2 | 118 | 101 | 35,460 |
| 7 | 10 | 0 | 62 | 62 | 31,476 |
| Total | — | — | 371 | 260 | 93,120 |

For a particular graph in the CSV, the allowed Y values start at max(0,8-2Z,B_min) and end at 14-2Z. The CSV records Z, graph6 representative, B_min, and the exact number of ordered maps f:R->[4] whose fibers are cliques. Empty fibers are allowed.

For each graph type, a second partition G is an independent copy of the same four-clique-fiber assignment space before the cross-map and outer-track conditions are imposed. The raw number of ordered (F,G) pairs across the catalog is 34,794,144. This is a candidate-pair count, not a count of globally compatible Q32 assignments.

## 3. Labelled enumeration counts

The independent labelled enumeration covered every graph on seven labelled vertices with e=3,...,10, a total of 1,048,344 graphs.

| Z | Raw | alpha<=4 | alpha<=4 and clique cover<=4 | Rejected by B_min budget | Final labelled survivors |
|---:|---:|---:|---:|---:|---:|
| 0 | 1,330 | 105 | 105 | 0 | 105 |
| 1 | 5,985 | 1,785 | 1,785 | 0 | 1,785 |
| 2 | 20,349 | 12,432 | 12,180 | 0 | 12,180 |
| 3 | 54,264 | 45,227 | 45,227 | 0 | 45,227 |
| 4 | 116,280 | 109,455 | 109,455 | 0 | 109,455 |
| 5 | 203,490 | 200,025 | 200,025 | 0 | 200,025 |
| 6 | 293,930 | 292,775 | 292,775 | 11,900 | 280,875 |
| 7 | 352,716 | 352,485 | 352,485 | 205,065 | 147,420 |
| Total | 1,048,344 | 1,014,289 | 1,014,037 | 216,965 | 797,072 |

The catalogue also distinguishes connected and disconnected residual graphs. There are 260 connected and 111 disconnected isomorphism types. This is connectivity of R, not connectivity of the ten-block light graph L.

## 4. Fiber assignment enumeration

For every one of the 371 graph6 representatives, the verifier enumerates all 4^7 maps from the seven residual vertices to four labelled fiber names and retains exactly those maps whose fibers are cliques. It counts:
- 93,120 ordered single-fiber maps;
- 34,794,144 ordered pairs of maps (F,G), before requiring the two partitions to agree, before matching compatibility, and before any outer weighted-heavy graph is attached.

The verifier can emit all 93,120 maps with --dump-fibers and all 797,072 labelled residual graph masks with --dump-labelled-graphs. This makes the catalogue reproducible without requiring NetworkX or an external solver.

## 5. Scope firewall

This enumeration is broader than the old maximum-degree-two path/cycle catalog, because it permits residual degree above two whenever the global Y slack can pay for it. It is still only a necessary-condition relaxation. It does not impose:
- the ten block-by-block incidence vectors a_{ri};
- the weighted-heavy graph on the ten pivot blocks;
- all pairwise matching/permutation constraints;
- the Type-I source endpoint placements from the previous file;
- the global edge-disjointness of the eleven non-target colors;
- the target clique cap on the entire 47-core after all blocks are attached.

The 3+7 branch has its own stronger source-derived contract and is conditionally closed by the Astra theorem. The 371-type catalog is not a substitute for that theorem and does not close any of the other light-component profiles.
