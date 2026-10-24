# Equality and near-equality cases

## c=2 branch

The analytic proof leaves only one apparent arithmetic escape before the final contradiction:

- `r=12`;
- `K=7`;
- both triple connectors have excess zero and are nonadjacent;
- all seven positive-excess exclusive vertices have excess exactly one;
- for each connector the exact nonneighbour block sizes are `(2,2,10)`.

The degree-2 transversal-cover lemma then forces the two size-2 exact parts to span a complete `K_{2,2}`. Those four vertices exhaust their entire cross-X degree capacity and have no cross edges to the size-10 part.

Every positive-excess vertex is nonadjacent to both connectors. Pick such a vertex `p` in one of the two small blocks. The opposite size-2 exact set has no edges to `p` or to the size-10 exact set. Therefore the independent-4 prohibition forces `p` to be adjacent to all ten vertices of the large exact set. But `p` has excess one and no connector neighbours, hence cross-X degree exactly three. Contradiction.

Thus the c=2 equality layer is empty.

## Remaining equality program

For `c=3,4`, equality analysis should be organized by connector focus rather than by partitions of the integer 7. A pair connector missing anchor `ak` forces a complete bipartite graph between its nonneighbour sets in the other two exclusive blocks. Because exact exclusive vertices have cross-X capacities `2+d_i`, this gives direct lower bounds on where excess must live.

The target is to show that every low-excess connector has a unique focus block, then classify the finite focus assignment among 3 or 4 connectors. This should replace a raw enumeration of the 15 integer partitions of 7.
