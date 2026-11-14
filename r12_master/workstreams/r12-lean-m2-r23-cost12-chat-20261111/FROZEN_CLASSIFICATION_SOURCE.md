# Frozen classification source, read 2026-11-14

Exact source commit: c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2.
Exact path: r12_master/workstreams/astra-global-root-integration-chat-20261031/frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md.
The original frozen file was read through the GitHub connector and was not edited.

M2a: 122 edges implies C5(10,a,1,1,b), a+b=11, 1<=a,b<=10.
M2b: 121 edges and K9,9 exterior gives exactly one singleton; adding one cycle
edge extends to a triangle-free M2a graph, preserving alpha<=11.
M2c: K8,10 exterior implies a blow-up with independent set at least12, impossible.
M2d: K9,9 minus uv, with all two-neighbor vertices. Compatible missing endpoints
are completed to M2a. Otherwise the remaining two type sets are singletons,
and all cases are C5(9,9,2,1,2), up to cycle rotation/reversal.

The condition 'K9,9 exterior' alone does not imply all vertices have two cycle
neighbors: M2b is explicitly the singleton exception. This is retained throughout.
The exact edge ledger is independent of any external finite enumeration.

Next lift obligation: construct a labeled C5 copy whose image is the SAME cycle
support used by r23_exact_neighbor_ledger; transfer actual neighbor cardinalities
to cycleNeighborLabels, then apply the verified type lemmas and prove whole-graph
class adjacency/cardinality equivalences for M2a-M2d. No isomorphism is assumed.
