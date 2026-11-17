# Universal Cost-6 — LEAN VERIFIED

Frozen source: MINIMUM_DEGREE_GATE_SELF_CONTAINED.md, low M3, immutable
c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2. Exact build provenance: CI_STATUS.json.

```lean
theorem r23_cost_six (G : SimpleGraph V) (hV : Fintype.card V = 23)
    (ht : G.CliqueFree 3) (hI : CoreIndependenceBound 11 G)
    (he : 121 ≤ G.edgeFinset.card) : CostSixProperty G
```

Here V is an arbitrary finite type. CostSixProperty G is exactly
forall I : Finset V, G.IsIndepSet (I : Set V) -> exists T : Finset V,
T.card=12 and coreInducedEdgeCount G T + (T intersect I).card <=6.
The induced edge count is the actual unordered edgeFinset cardinality.
No classification or Cost-6 hypothesis is assumed by this parent theorem.

case_I_cost_six proves the three actual fiber-union witnesses cover every
independent set, including empty and nonmaximal sets. Their sizes, induced
edges, and intersections are counted by c5_three_fiber_witness_counts.
exceptional_cost_four proves the stronger universal cost<=4, and
exceptional_cost_six supplies the common interface.

case_I_single_edge_deletion_cost_six treats all independent sets newly created
by deleting one edge. Existing independent sets use graph edge-count monotonicity.
For a new independent set, a deleted endpoint adjacent to the ten-point center
forces its intersection with that center to have size<=1. The standard witness
then has cost<=4. In the remaining singleton-to-singleton case, both other large
class intersections vanish; A+B=11 ensures one alternate witness has cost<=6.
This strengthens the paper's deletion sublemma: it also covers deletions with
alpha>11. The original r23_cost_six still retains alpha<=11 exactly as required.
No original statement is weakened; no diagnostic computation is a Lean premise.

The complete classification r23_complete_classification selects the three cases.
All finite decide calls concern explicit Fin 5 cycle relations; they are reduced
and checked by the Lean kernel. No native_decide or external oracle occurs.

Independent diagnostic attack: all61 class-edge representatives and all351071
independent sets, including alpha>11 cases, had cost<=6; the exceptional graph
had worst cost4. This is testing only; see logs/cost-six-deletion-attack.json.
