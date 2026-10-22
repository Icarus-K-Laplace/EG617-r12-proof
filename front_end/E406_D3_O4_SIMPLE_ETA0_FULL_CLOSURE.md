# E406 d=3 Type-A O4: eta=0 simple-four-double branch — FULL CLOSURE

Status: `PROVED EMPTY` for the complete eta=0 O4 multiplicity type consisting of four distinct double-full vertices.

This file is a modern closure index. It uses only proof bodies whose hypotheses have been checked against the modern eta=0 O4 interface.

Modern contract:

- four pairwise anticomplete K3 support rows;
- H has35 vertices;
- `e(H)=152`;
- total H-core excess is4;
- O=4;
- full-row counts `(9,10,10,10)`;
- total partial support incidence R=3;
- the four O-units are carried by four distinct double-full vertices;
- `alpha(C)<=4`, `omega(C)<=11`;
- every pure class is a clique of size at most8;
- every singleton-full partial carrier is complete to its pure class and therefore lies only in a pure class of size at most7.

The historical S30 simple-four-double proofs were written for the weaker excess budget6. Whenever used below, their argument is monotone in the total available excess: the same row-count, pure-clique, pair-overlap, alpha and clique hypotheses hold here, while the modern excess budget is smaller. No historical CLOSED label is imported without its proof body.

## 1. Exhaustive pure-size list

Let P_i be the four pure classes. Four double vertices use four H-vertices. Every remaining non-pure vertex is a singleton partial carrier, and R=3 implies at most three such vertices.

Hence

`sum p_i >= 28`,

with each `p_i<=8`.

The sorted possibilities are exactly

- sum28: `(4,8,8,8)`, `(5,7,8,8)`, `(6,6,8,8)`, `(6,7,7,8)`, `(7,7,7,7)`;
- sum29: `(5,8,8,8)`, `(6,7,8,8)`, `(7,7,7,8)`;
- sum30: `(6,8,8,8)`, `(7,7,8,8)`;
- sum31: `(7,8,8,8)`.

No other partition is possible.

## 2. Modern new closures

The following three profiles are now closed directly in the E406 repository:

### `(4,8,8,8)`

Closed in `E406_D3_TYPEA_O4_MODERN_INTERFACE.md` by row-degree count. Since 8-8 double edges are impossible under the modern four-unit excess budget, all four double edges would have to pass through the 4-row, but the three 8-rows require five or six double incidences depending on which row has full count9. Contradiction.

### `(5,7,8,8)`

Closed in `E406_D3_O4_SIMPLE_5788_ETA0.md` by complete row-orientation analysis, 7-8 near-twin rigidity, Mantel lower bounds on common nonneighbourhoods, and one direct independent5 construction.

### `(6,7,7,8)`

Closed in `E406_D3_O4_SIMPLE_6778_ETA0.md` by complete row-orientation analysis. The key modern input is `eps_x<=2`, forcing every 7-8 overlap to be complete to its 7-class with at most one outside H-neighbour. The remaining 7-7 low-cost forms are eliminated by same-row singleton, common-nonneighbourhood, or independent5 arguments.

## 3. Audited weaker-budget closures that remain valid a fortiori

The following profiles have analytic proof bodies in the audited S30 O4 archive. Each proof uses the same incidence / pure-clique / alpha / clique interface and derives a required excess strictly exceeding the historical budget6, or a structural independent-set/clique contradiction. Therefore they remain valid under the modern budget4.

### All pure classes at least7

`S30_O4_SIMPLE_DOUBLE_AUDIT.md` proves:

- `(7,7,7,7)`;
- `(7,7,7,8)`;
- `(7,7,8,8)`;
- `(7,8,8,8)`.

The proof uses the pair-overlap table, singleton external capacities, and the minimum edge count required in the special-vertex graph to avoid an independent5-set.

### `(6,8,8,8)` and `(6,7,8,8)`

The same audited file proves these profiles impossible by the forced row-pair graph and 8-8 / 7-8 pair costs plus singleton capacity. The historical contradiction already exceeds total excess6.

### `(5,8,8,8)`

The standalone analytic file `PROOF.md` in the audited archive closes this profile. In the modern budget4 setting the proof is even shorter because the forced 8-8 overlap alone has lower cost6>4. Its longer equality-rigidity argument is retained only as provenance.

### `(6,6,8,8)`

The standalone analytic file `PROOF(1).md` proves every row orientation requires at least seven units of disjoint excess. Hence it is impossible under the modern four-unit budget.

## 4. Conclusion

Every sorted pure-size profile in the exhaustive list is impossible.

Therefore

> **ETA0-SIMPLE-O4 CLOSURE. No eta=0 E406 d3 Type-A O4 state exists whose four O-units are carried by four distinct double-full vertices.**

The remaining modern d3-TypeA O4 work is restricted to

- eta=1 simple-four-double states;
- one triple + two doubles;
- two triples.

The four-full + double multiplicity type is already excluded by `E406_D3_NO_FOURFULL.md`.