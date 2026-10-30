# Universal multicolor intersection interface

## M1. Pairwise linear factors — PROVED

Distinct exact colors' K5 factors intersect in at most one vertex: two shared vertices would assign their edge to two colors. The same statement holds for their core intersections. This uses unique edge ownership only; it does not identify their special points or their factor labels.

## M2. Common five-point deletion — PROVED from U1

For every valid target core, the SAME five-set Z from U1 makes the union of all eleven non-target core graphs four-partite. Its parts have orders10,10,11,11. In particular every exact factor meets each K_i in at most one vertex, and this holds simultaneously for every color. This is stronger than allowing a different four-partition for each color; the partition comes from H itself.

This records an intermediate interface under the putative core contract. U6 later excludes that contract itself. No independent-set partition from a sibling is used.

## M3. Enlarged outside-set occupancy — PROVED_CONDITIONAL on exact Type I

Let W=O union Z, of order19, and K=H minus Z, of order42. Each K5 factor meets W, since it has at most one point in each of the four K_i. If x lies in W, the twelve factor W-counts sum18 and their total surplus over one per factor is6. If x lies in K, they sum19 and their surplus is7.

Thus each exact color has at least six factor intersections of size4 in K when x is in W, and at least five when x is in K. Each such four-set is a transversal of the four common parts and is monochromatic in that exact color. Across colors these transversals remain pairwise linear by M1.

Do not confuse this enlarged19-point outside set with the original14-point O. Both exceptional positions are retained. This is a new common-part projection of the source system, not a replacement for the full gadget edges.

## M4. Degree conservation on the common partition — PROVED

For v in K_i, let t(v) be its number of target neighbors in the other three K_j. Then the number of non-target neighbors of v in K is42-|K_i|-t(v). A source transversal through v consumes three distinct such edges. Hence the number of selected exact-color transversal factors through v is at most

    floor((42-|K_i|-t(v))/3).

This counts actual edge ownership. It is valid for all m but does not by itself contradict m=8,9,10. A repeated factor label, repeated matching, or repeated special point is not automatically an edge collision.

## Relation to the final proof

The target-core theorem U6 excludes both D and P before any colored extension is imposed. The intersection statements above remain valid necessary deductions for the contradiction argument but are not load-bearing in U6. No simultaneous design classification, linear-program dual certificate or full colored search is claimed or required. All source placements are covered uniformly by excluding their common core projection.
