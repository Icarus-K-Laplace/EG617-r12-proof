# Current minimal proof obligations

Verified checkpoint: 2dba3b9 / Linux CI 43616747074.

1. R23 122-edge branch: derive fiber sizes 10,a,1,1,b up to cycle
   rotation/reflection, a+b=11 and 1<=a,b<=10, from the verified actual
   type presentation and balanced complete exterior. Candidate C5TypeFibers.lean
   splits each fiber into its cycle vertex and exterior vertices. It is not
   promoted before kernel validation.
2. R23 121-edge K9,9 branch: lift the unique singleton extension to an actual
   one-edge supergraph preserving triangle-freeness and alpha<=11.
3. R23 121-edge K9,9-e: retain the exact exceptional endpoints; lift compatible
   completion and all ten incompatible orientations to whole-graph statements,
   proving the latter is C5(9,9,2,1,2).
4. Cost-6 for every independent set and every permitted single-edge deletion.
5. Sharp R335/R336; GATE47 d=10/d=11 exclusions, shell incidence and row-union
   inequality, with every original CoreAdmissible hereditary condition retained.

CLOSED: exact neighbor deficits, same-support type labeling, K8,10 exclusion,
and the 122-edge full adjacency/type equivalence. The last result depends on
actual complete bipartite adjacency, not compatibility alone.

Recent failed CI runs 43615074608, 43615446118, 43615749155, 43616064184,
43616405629 were Lean elaboration/instance failures, now resolved at the named
checkpoint. Logs are preserved. They are not mathematical counterexamples.
No sorry/admit/custom axiom/native_decide or external oracle is permitted.
