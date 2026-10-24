# Counterexample search

Status: **no genuine counterexample found; full c=3/c=4 search still open.**

## Search discipline
A candidate must satisfy all of:

- `|H|=3r-1`;
- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- `delta(H)>=r`;
- three pairwise nonadjacent degree-r anchors;
- `K_r<=7`.

No quotient or degree-feasible skeleton is promoted as a counterexample unless it realizes an actual graph satisfying every condition.

## Analytic elimination already stronger than search for c=2
The full `c=2` family is now analytically impossible for every `r>=12`, so there is nothing left to search in the `(r-2,r-2,r-2)` block geometry.

A useful false skeleton appeared during relaxation work: two triple connectors can each concentrate almost all of their X-neighbours in one block while a sparse cross graph satisfies aggregate degree sums. Such skeletons pass coarse edge-count constraints but fail the independent-4 condition once exact-degree cross-capacity is enforced. This is exactly what motivated the degree-2 tripartite transversal-cover lemma.

## Remaining finite skeletons
Only these geometries remain:

1. `c=3`: deficits `(0,0,1)`, hence one triple connector and two pair connectors;
2. `c=4`: deficits `(0,0,2)`, hence four pair connectors with missing-anchor multiplicities `(2,2,0)`;
3. `c=4`: deficits `(0,1,1)`, hence four pair connectors with missing-anchor multiplicities `(2,1,1)`.

The next search will enumerate only the constant-sized connector incidence/focus skeleton, not all `O(r^2)` edges. Any computational elimination will be accompanied by source, deterministic verifier, completeness contract, and checksum before being marked `COMPUTATION_CERTIFIED`.
