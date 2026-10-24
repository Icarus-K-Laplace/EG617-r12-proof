# Equality and near-equality cases

The parity lemma removes the entire apparent `K=7` layer: every `K_r` is even, so a counterexample has `K<=6`.

## c=2
No equality layer survives. The previous apparent `r=12,K=7,(2,2,10)` escape is impossible already by parity.

## c=3
For `r>=14`, all focus/nonfocus inequalities are strict enough to force `K>=8`.

At `r=13`, the only mixed-focus arithmetic boundary under `K<=6` is

- one pair connector focused on `X3`;
- the other pair connector `v` nonfocused;
- `v` has excess `6` and connector-degree `0`;
- its nonneighbour rectangle has size `(2,2)` between the zero-deficit block and `X3`;
- every other vertex is exact.

This boundary is impossible because the triple connector would have to be adjacent to all eleven vertices of the opposite zero-deficit block while already adjacent to the three anchors.

## c=4, deficits (0,0,2)
At most two connectors can focus on `X3`, so at least two are nonfocused.

The only boundary layers that reach total budget six are:

- `r=16`: a single nonfocused connector can attain local cost six, but two required nonfocused connectors cannot coexist because different-group charges add and same-group nonadjacent supports are disjoint; adjacency raises local cost above six.
- `r=15`: an adjacent nonfocused connector can stay within budget only with connector excess `k=6`; two such connectors are impossible.
- `r=14`: the only two-connector overlap escape is two adjacent same-group connectors with `k=0` and identical `(a,b)=(10,1)` rectangles. Their common `X3` vertex carries all six excess units and has no remaining connector slot, contradicting the focused pair from the other group.
- `r=13`: a different-group equality pair would require `(k,a,b)=(3,4,2)` for both, exhausting all six units and leaving their `X3` rectangle vertices unavailable to the required focused connectors. Hence the nonfocused pair must be same-group; the other-group focused pair then lowers the effective `X3` capacity from four to two, after which both adjacency and nonadjacency alternatives exceed budget.

Thus no equality case survives.

## c=4, deficits (0,1,1)
No two connectors can focus on the same deficit-1 block.

The boundary layers are:

- `r=16`: both `(0,1)` connectors must focus, leaving two nonfocused type-U connectors; disjoint-support charge is at least twelve.
- `r=15`: the same focus pattern holds; an adjacent type-U connector would need `k=6`, so two are impossible.
- `r=14`: a nonfocused `(0,1)` connector would have the unique boundary `k=6`, connector-degree `0`, rectangle `(3,2)`. It would force each other connector to be complete to the same deficit-1 block, contradicting focus collision. Thus both `(0,1)` connectors focus, and the remaining type-U pair cannot fit budget.
- `r=13`: if either `(0,1)` connector is nonfocused, additive rectangle charges exceed six. Hence both focus. A nonadjacent type-U pair can hit `K=6` only through two `(k,a,b)=(3,3,3)` layers, but then exact rectangle vertices have no slot for the focused connectors. An adjacent type-U pair receives one focused connector neighbour on each side, reducing both effective capacities to two and forcing `k=6` on each connector.

Thus the equality set is empty for every `r>=13`.

## Final equality status

For the parameterized theorem (`r>=13`), there are **no surviving `K=0,2,4,6` configurations** in any of the four anchor geometries.

The only non-parameterized residue is proof-engineering at `r=12`: the parent project already has a complete closure, but this workstream has not yet rewritten that closure into the new focus/rectangle language.
