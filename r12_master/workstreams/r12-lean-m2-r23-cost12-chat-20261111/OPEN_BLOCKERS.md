# Current minimal proof obligations

Verified code c252a45 / Linux CI 43618192344.

1. Frozen M2b /121-edge K9,9: use the unique singleton and the verified
   c5_singleton_extension to construct an ACTUAL one-edge supergraph.
   Prove it triangle-free, retain alpha<=11, prove exactly122 edges,
   and apply r23_122_case_I. Type compatibility alone does not add an edge.
2. Frozen M2d /121-edge K9,9-e: compatible endpoint completion; otherwise
   derive the actual vertex fibers and adjacency of C5(9,9,2,1,2) from the
   verified ten endpoint orientations, including all rotations/reflections.
3. Cost-6 for every independent set, including legal deleted-edge graphs.
4. Sharp R335/R336; GATE47 d=10/d=11, shell incidence, row-union inequality
   and287-edge contradiction, retaining every original hereditary D condition.

CLOSED: exact ledger/distribution, same-support labeling, K8,10 exclusion,
and COMPLETE122-edge Case I with fiber sizes10,A,1,1,B and A+B=11.

Failures retained in logs were elaboration/instance issues. The last Case I
failure43617898415 was unreduced Fin5 negative-one notation; explicitly
rewriting cyclic subtraction to positive addition resolved it. No mathematical
counterexample was inferred from tactic failure. No sorry/admit/custom axiom,
native_decide or external oracle is allowed.
