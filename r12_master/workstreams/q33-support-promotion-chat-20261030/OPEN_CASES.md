# Q33 support promotion — exact remaining OPEN frontier

Status: **OPEN / NOT_CERTIFIED**.

## Excluded by source-correct variable-core profile screen
- m=8: v=31,32,33,34;
- m=9: v=32,33,34;
- m=10: v=34,35,36,37.

## First profile-feasible cells
- m=8, v=35, h in {6,7,8};
- m=9, v=35, h=9;
- m=10, v=38, h=10.

Every larger support size through47 remains feasible in this necessary relaxation.

## Next structural attack
The tightest cells now have highly constrained selected gadget counts:
- m=8,v=35: six, seven, or eight selected gadget witnesses;
- m=9,v=35: all nine selected exact colors must use a gadget witness;
- m=10,v=38: all ten selected exact colors must use a gadget witness.

Next encode the actual labelled K5 component core subsets, gadget-core subsets, pairwise linear witness intersections, and vertex degree/excess ledger. The profile DP does not yet impose these vertex labels.

## Explicit limitation
The source-verified exact-129 factor theorem gives ten isolated K5s plus an 11-vertex gadget, but does not by itself make every K5 have exactly one shell vertex. The variable-core model allows component core sizes c_i=0,...,4. Do not use the older fixed c_i=4 profile screen as a universal parent reduction.


## 2026-10-30 — updated component-only frontier (supersedes the all-h first-survivor list)

The canonical support family selects seven component K4 witnesses in every exact-129 color, so h=0. The source-correct component-only profile screen now excludes:
- m=8: v=31,...,38;
- m=9: v=32,...,39;
- m=10: v=34,...,40.

The first aggregate profile-feasible cells are:
- m=8, v=39;
- m=9, v=40;
- m=10, v=41.

Every larger support size through47 has at least one aggregate cost-pair survivor. These are necessary-profile survivors only, not labelled graph realizations.

Next attack: impose the actual seven-witness incidence matrix, exact component/gadget vertex partition, cross-color pairwise linearity, the four units of core degree excess, and the seven-block near-Latin duplicate ledger on the remaining support ranges. Q33 remains OPEN / NOT_CERTIFIED.
