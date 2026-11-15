# R23 classification — Case I and Case III verified; remaining121 cases open

Frozen source: c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2,
r12_master/workstreams/astra-global-root-integration-chat-20261031/frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md.
See FROZEN_CLASSIFICATION_SOURCE.md. The frozen proof was read and not edited.

Original hypotheses: card V=23, CliqueFree3, CoreIndependenceBound11, e>=121.
No terminal type distribution, classification or hereditary cap is added.

- Exact ledger and all three neighbor distributions: r23_exact_neighbor_ledger.
- Case I, e=122: r23_122_case_I proves R23CaseIProfile G, with a map on ALL
  actual vertices, adjacency iff C5 adjacency, and the exact five fiber sizes
  10,A,1,1,B, where A+B=11 and1<=A,B<=10.
- Case III, K8,10: r23_exists_balanced_exterior excludes it using an actual
  independent neighborhood of size12, leaving balanced parts of size9.
- Case II: singleton type extension verified, actual graph completion OPEN.
- Case IV: missing-endpoint type constraints and ten orientations verified,
  actual compatible completion and exceptional blow-up classification OPEN.

The Case I representation is equivalent to a C5 blow-up: fibers partition V;
the iff specifies every present and absent edge; all five fiber sizes are
positive. The five labels a,a+1,a+2,a-2,a-1 range over Fin5 in cyclic order.
It does not merely record an edge count or permitted adjacency. Reflection
is included by swapping A and B. A graph-isomorphism object is not the encoding;
the actual-vertex adjacency/fiber characterization is.

Evidence: c252a45b185c07387e71b3416cde37f46b95b3f1, CI43618192344.
Full source signatures: DECLARATION_STATEMENTS.md; exact #checks in CI logs.
The entire R23 classification and GATE47 must NOT be marked LEAN VERIFIED.
