# I-version q29 recovery audit

Status: PARTIAL RECOVERY / NOT YET STANDALONE COMPLETE.

## Recovered analytic body

For q=29 under the modern r=12 shell interface:

1. Triangle-free branch:
   - four disjoint missing edges already force q>=32;
   - non-bipartite triangle-free possibilities are reduced by odd-cycle/matching counting;
   - hence M is bipartite with a 3-vertex cover and 10-vertex independent shore;
   - an exact row/decoration dynamic program eliminates the surviving K_{3,10}-type weighted states.

2. Triangle but no K4:
   - fixing a missing triangle T, the outside graph N=M-T satisfies nu(N)<=1;
   - the outside-triangle case is eliminated;
   - positive outside edge states force A=t(T) in {24,25};
   - empty/star attachment states are then eliminated using the r=12 heavy-four cross-colour theorem and exact excess accounting.

Thus every non-K4 q29 shell is eliminated in the recovered I proof body.

## Remaining K4 frontier

For q=29 with K4 subset M, the I-version reduces the shell to four attachment profiles. Three are already eliminated; the main profile (3,10,11,11) has 119 lower-registry states. A row-cover calculation gives a maximum migrated coverage 3297 versus 3630 required transversal coverage, reducing 125 states to six residual terminal states.

However, the I-version itself explicitly says the final r=11 row-cover certificate must be rebuilt from its definitions in r=12 semantics before the six terminals can be declared dead.

Therefore the correct status is:

- non-K4 q29: recovered/closed under stated dependencies;
- K4 q29: reduced to six finite terminal attachment states;
- generic q29 standalone theorem: NOT YET COMPLETE from I alone.

This file supersedes any historical blanket label 'q29 completely eliminated' unless the row-cover migration is independently reconstructed.
