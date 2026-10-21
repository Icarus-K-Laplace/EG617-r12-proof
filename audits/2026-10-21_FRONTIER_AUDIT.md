# Frontier audit — 2026-10-21

This file records the current reconstructed research state after merging the latest frontier audit with the earlier integration documents.

## S30 `(5,7,8,8)` row-labelled branch

Status: `PROVED` under the explicit singleton-adjacency hypotheses of that branch.

Key reduction: with `t=X_BC` and missing-neighbour counts `a,b` into the two relevant classes, the non-overcounted necessary condition is

`(9-a-b)_+ + a(b-2)_+ + b(a-2)_+ <= 5`.

Together with `b>=1`, only

`(a,b)=(0,4),(0,5),(0,6),(0,7),(0,8),(2,2)`

remain; these are analytically excluded by independent-set constructions / degree saturation.

Boundary: the two cross-singleton adjacencies to the C-row singleton remain explicit inputs. Therefore the full `(5,7,8,8)` macro profile is still `OPEN`.

## Eight-block bridge strengthening

Historical eight-block model uses

`e(F)=m-528-x-y`.

The earlier high-cross branch `alpha(F)>=5` can be analytically eliminated under the genuine eight-K12 hypothesis. Consequently, once eight genuine blocks exist, the 49-point residual satisfies

`alpha(F)<=4`.

This is stronger than the older threshold statement `x<=195 => alpha(F)<=4`, but it still does NOT prove the eight blocks exist.

## S31 strict descent

Status: `PROVED` under its explicit parent contract.

For a 61-point graph with `e=406`, `delta>=13`, `alpha<=5`, `omega<=11`, plus the stated hereditary density caps, there exists a degree-13 pivot with

`q_p<=30`.

This is a descent theorem inside the parent class and does not prove the front-end bridge from K145.

## Architectural consequence

The modern proof no longer needs an exact `e(F)=325` bridge. The front-end should aim only to produce a legitimate `F in R(4,49)`; the backend handles edge layers.

Current global status remains `NOT_CERTIFIED`.
