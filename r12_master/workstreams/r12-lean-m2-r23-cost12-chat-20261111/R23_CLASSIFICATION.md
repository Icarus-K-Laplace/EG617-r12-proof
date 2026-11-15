# R23 complete classification — LEAN VERIFIED

Code0d2985dbfe109fab301c157f687b3b38478c8bb6; Linux CI43680628810.
Full build, precise types, complete axiom allowlist, dependency pins and hashes PASS.

The kernel-checked parent is EG617.r23_complete_classification in
lean/EG617/Core/R23Classification.lean:

```lean
theorem r23_complete_classification (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    R23CaseIProfile G ∨ R23OneEdgeCompletion G ∨ R23ExceptionalProfile G
```

Here V is an arbitrary finite type. The exact elaborated type (including its
universe/Fintype parameters) is printed in the successful CI log.

Frozen source: c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2,
r12_master/workstreams/astra-global-root-integration-chat-20261031/frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md.
The original source was read and was not edited.

| Paper branch | Actual graph theorem |
|---|---|
| M2a /122 edges | r23_122_case_I |
| M2b /121 edges, complete9+9 exterior | r23_121_completion_or_missing_exterior |
| M2c /8+10 exterior impossible | r23_exists_balanced_exterior |
| M2d /compatible missing endpoints | missing_exterior_completion_or_exceptional, completion alternative |
| M2d /incompatible missing endpoints | missing_exterior_completion_or_exceptional, exceptional alternative |
| Exhaustive combination | r23_complete_classification |

R23CaseIProfile supplies a map on ALL actual vertices, adjacency iff C5 adjacency,
and cyclic fiber sizes10,A,1,1,B with A+B=11 and1<=A,B<=10.
R23OneEdgeCompletion supplies actual distinct nonadjacent endpoints, the graph
G sup edge(u,v), its triangle-freeness, alpha<=11, exactly122 edges and Case I
profile. Thus G differs from that graph by exactly one edge.
R23ExceptionalProfile supplies actual adjacency iff and fiber sizes9,9,2,1,2.

These encode precisely the usual C5 blow-ups: fibers partition V, all five
fibers are nonempty, and the iff specifies every edge and nonedge. Labels
c,c+1,c+2,c-2,c-1 exhaust Fin5 in cyclic order. Rotations and both orientations
are accounted for by the proved endpoint theorem and exact fiber arithmetic.
An explicit graph-isomorphism object is not used as the representation;
the actual-vertex adjacency/fiber characterization is the formal encoding.

No type compatibility is interpreted as an existing edge. Complete or unique
missing cross adjacency is derived first and used in every reverse implication.
Every neighborhood-distribution hypothesis of a helper is derived internally
from the original assumptions before invoking that helper.

This closes frozen M2 only. Cost-6, GATE47 and original EG617 are NOT proved.
