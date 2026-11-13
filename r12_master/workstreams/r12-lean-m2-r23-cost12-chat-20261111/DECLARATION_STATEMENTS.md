# Exact Lean declaration statements

Verbatim source signatures. Consult CI_STATUS.json for actual verification.
All definitions and proof bodies are retained in the standard .lean files.

## EG617.colorGraph

Source: EG617/Basic/ColoringLemmas.lean

```lean
def colorGraph (c : EdgeColoring) (i : Color) : SimpleGraph Vertex where
  Adj u v
```

## EG617.colorGraph_adj_iff

Source: EG617/Basic/ColoringLemmas.lean

```lean
theorem colorGraph_adj_iff (c : EdgeColoring) (i : Color)
    (u v : Vertex) (h : u ≠ v) :
    (colorGraph c i).Adj u v ↔ c (edgeOf u v h) = i
```

## EG617.validColoring_iff_colorGraph

Source: EG617/Basic/ColoringLemmas.lean

```lean
theorem validColoring_iff_colorGraph (c : EdgeColoring) :
    ValidColoring c ↔ ∀ S : Finset Vertex, S.card = 13 →
      ∀ i : Color, ∃ u ∈ S, ∃ v ∈ S, (colorGraph c i).Adj u v
```

## EG617.colorGraph_partition

Source: EG617/Basic/ColoringLemmas.lean

```lean
theorem colorGraph_partition (c : EdgeColoring) (u v : Vertex) (h : u ≠ v) :
    ∃! i : Color, (colorGraph c i).Adj u v
```

## EG617.no_independent_thirteen

Source: EG617/Basic/ColoringLemmas.lean

```lean
theorem no_independent_thirteen (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (hS : S.card = 13) (i : Color) :
    ¬ (∀ u ∈ S, ∀ v ∈ S, ¬ (colorGraph c i).Adj u v)
```

## EG617.no_monochromatic_thirteen

Source: EG617/Basic/ColoringLemmas.lean

```lean
theorem no_monochromatic_thirteen (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (hS : S.card = 13) (i : Color) :
    ¬ (∀ u ∈ S, ∀ v ∈ S, ∀ h : u ≠ v, c (edgeOf u v h) = i)
```

## EG617.Vertex

Source: EG617/Basic/Definitions.lean

```lean
abbrev Vertex
```

## EG617.Color

Source: EG617/Basic/Definitions.lean

```lean
abbrev Color
```

## EG617.Edge

Source: EG617/Basic/Definitions.lean

```lean
abbrev Edge
```

## EG617.EdgeColoring

Source: EG617/Basic/Definitions.lean

```lean
abbrev EdgeColoring
```

## EG617.edgeOf

Source: EG617/Basic/Definitions.lean

```lean
def edgeOf (u v : Vertex) (h : u ≠ v) : Edge
```

## EG617.Inside

Source: EG617/Basic/Definitions.lean

```lean
def Inside (e : Edge) (S : Finset Vertex) : Prop
```

## EG617.edgeOf_swap

Source: EG617/Basic/Definitions.lean

```lean
theorem edgeOf_swap (u v : Vertex) (h : u ≠ v) :
    edgeOf u v h = edgeOf v u h.symm
```

## EG617.edgeOf_eq_iff

Source: EG617/Basic/Definitions.lean

```lean
theorem edgeOf_eq_iff
    (u v x y : Vertex) (huv : u ≠ v) (hxy : x ≠ y) :
    edgeOf u v huv = edgeOf x y hxy ↔
      (u = x ∧ v = y) ∨ (u = y ∧ v = x)
```

## EG617.edge_has_endpoints

Source: EG617/Basic/Definitions.lean

```lean
theorem edge_has_endpoints (e : Edge) :
    ∃ u v : Vertex, u ≠ v ∧ e.val = s(u, v)
```

## EG617.edgeOf_surjective

Source: EG617/Basic/Definitions.lean

```lean
theorem edgeOf_surjective (e : Edge) :
    ∃ u v : Vertex, ∃ h : u ≠ v, edgeOf u v h = e
```

## EG617.edgeOf_inside_iff

Source: EG617/Basic/Definitions.lean

```lean
theorem edgeOf_inside_iff
    (u v : Vertex) (h : u ≠ v) (S : Finset Vertex) :
    Inside (edgeOf u v h) S ↔ u ∈ S ∧ v ∈ S
```

## EG617.inside_mono

Source: EG617/Basic/Definitions.lean

```lean
theorem inside_mono {e : Edge} {S T : Finset Vertex}
    (hST : S ⊆ T) (he : Inside e S) : Inside e T
```

## EG617.mem_complete_iff

Source: EG617/Basic/Definitions.lean

```lean
theorem mem_complete_iff (e : Sym2 Vertex) :
    e ∈ (SimpleGraph.completeGraph Vertex).edgeSet ↔ ¬ e.IsDiag
```

## EG617.edgeEquivComplete

Source: EG617/Basic/Definitions.lean

```lean
def edgeEquivComplete :
    Edge ≃ (SimpleGraph.completeGraph Vertex).edgeSet where
  toFun e
```

## EG617.ValidColoring

Source: EG617/Basic/OriginalProblem.lean

```lean
def ValidColoring (c : EdgeColoring) : Prop
```

## EG617.EG617R12Statement

Source: EG617/Basic/OriginalProblem.lean

```lean
def EG617R12Statement : Prop
```

## EG617.validColoring_iff_endpoints

Source: EG617/Basic/OriginalProblem.lean

```lean
theorem validColoring_iff_endpoints (c : EdgeColoring) :
    ValidColoring c ↔
      ∀ S : Finset Vertex, S.card = 13 → ∀ i : Color,
        ∃ u ∈ S, ∃ v ∈ S, ∃ h : u ≠ v, c (edgeOf u v h) = i
```

## EG617.originalProblem_iff_missingColor

Source: EG617/Basic/OriginalProblem.lean

```lean
theorem originalProblem_iff_missingColor :
    EG617R12Statement ↔
      ∀ c : EdgeColoring, ∃ S : Finset Vertex, S.card = 13 ∧
        ∃ i : Color, ∀ e : Edge, Inside e S → c e ≠ i
```

## EG617.tau12

Source: EG617/Combinatorics/TuranArithmetic.lean

```lean
def tau12 (n : ℕ) : ℕ
```

## EG617.tau12_add_turanNumber

Source: EG617/Combinatorics/TuranArithmetic.lean

```lean
theorem tau12_add_turanNumber (n : ℕ) (hn : n ≤ 145) :
    tau12 n + SimpleGraph.turanNumber n 12 = Nat.choose n 2
```

## EG617.CoreIndependenceBound

Source: EG617/Core/Admissibility.lean

```lean
def CoreIndependenceBound (a : ℕ) (G : SimpleGraph V) : Prop
```

## EG617.CoreCliqueBound

Source: EG617/Core/Admissibility.lean

```lean
def CoreCliqueBound (k : ℕ) (G : SimpleGraph V) : Prop
```

## EG617.coreInducedEdgeCount

Source: EG617/Core/Admissibility.lean

```lean
noncomputable def coreInducedEdgeCount (G : SimpleGraph V) (S : Finset V) : ℕ
```

## EG617.CoreAdmissible

Source: EG617/Core/Admissibility.lean

```lean
def CoreAdmissible (a : ℕ) (G : SimpleGraph V) : Prop
```

## EG617.core_induced_edge_count_univ

Source: EG617/Core/Admissibility.lean

```lean
theorem core_induced_edge_count_univ [Fintype V] (G : SimpleGraph V) :
    coreInducedEdgeCount G Finset.univ = G.edgeFinset.card
```

## EG617.core_independenceBound_induce

Source: EG617/Core/Admissibility.lean

```lean
theorem core_independenceBound_induce (G : SimpleGraph V) (a : ℕ)
    (hG : CoreIndependenceBound a G) (S : Finset V) :
    CoreIndependenceBound a (G.induce (S : Set V))
```

## EG617.core_cliqueBound_induce

Source: EG617/Core/Admissibility.lean

```lean
theorem core_cliqueBound_induce (G : SimpleGraph V) (k : ℕ)
    (hG : CoreCliqueBound k G) (S : Finset V) :
    CoreCliqueBound k (G.induce (S : Set V))
```

## EG617.core_independence_nonNeighbors

Source: EG617/Core/Admissibility.lean

```lean
theorem core_independence_nonNeighbors (G : SimpleGraph V) (a : ℕ)
    (hG : CoreIndependenceBound (a + 1) G) (v : V) (S : Finset V)
    (hS : ∀ w ∈ S, w ≠ v ∧ ¬ G.Adj v w) (hind : G.IsIndepSet (S : Set V)) :
    S.card ≤ a
```

## EG617.core_compl_edge_count

Source: EG617/Core/Admissibility.lean

```lean
theorem core_compl_edge_count [Fintype V] (G : SimpleGraph V) :
    G.edgeFinset.card + Gᶜ.edgeFinset.card = (Fintype.card V).choose 2
```

## EG617.core_induced_edge_count_image

Source: EG617/Core/Admissibility.lean

```lean
theorem core_induced_edge_count_image (G : SimpleGraph V) (S : Finset V)
    (T : Finset S) :
    coreInducedEdgeCount (G.induce (S : Set V)) T =
      coreInducedEdgeCount G (T.image fun x : S => (x : V))
```

## EG617.core_admissible_induce

Source: EG617/Core/Admissibility.lean

```lean
theorem core_admissible_induce (G : SimpleGraph V) (a : ℕ)
    (hG : CoreAdmissible a G) (S : Finset V) :
    CoreAdmissible a (G.induce (S : Set V))
```

## EG617.core_admissible_nonNeighbors

Source: EG617/Core/Admissibility.lean

```lean
theorem core_admissible_nonNeighbors (G : SimpleGraph V) (a : ℕ)
    (hG : CoreAdmissible (a + 1) G) (v : V) (S : Finset V)
    (hS : ∀ w ∈ S, w ≠ v ∧ ¬ G.Adj v w) :
    CoreAdmissible a (G.induce (S : Set V))
```

## EG617.Gate47Statement

Source: EG617/Core/Admissibility.lean

```lean
def Gate47Statement : Prop
```

## EG617.two_colorable_partition

Source: EG617/Core/BipartiteExterior.lean

```lean
theorem two_colorable_partition (G : SimpleGraph V) (hb : G.Colorable 2) :
    ∃ A : Finset V, G.IsIndepSet (A : Set V) ∧ G.IsIndepSet ((Aᶜ : Finset V) : Set V)
```

## EG617.bipartition_edge_count

Source: EG617/Core/BipartiteExterior.lean

```lean
theorem bipartition_edge_count (G : SimpleGraph V) (A : Finset V)
    (hA : G.IsIndepSet (A : Set V)) (hB : G.IsIndepSet ((Aᶜ : Finset V) : Set V)) :
    G.edgeFinset.card = adjCount G A Aᶜ
```

## EG617.adjCount_eq_card_product_filter

Source: EG617/Core/BipartiteExterior.lean

```lean
theorem adjCount_eq_card_product_filter (G : SimpleGraph V) (A B : Finset V) :
    adjCount G A B = ((A ×ˢ B).filter (fun xy => G.Adj xy.1 xy.2)).card
```

## EG617.adjCount_add_missing_eq_product

Source: EG617/Core/BipartiteExterior.lean

```lean
theorem adjCount_add_missing_eq_product (G : SimpleGraph V) (A B : Finset V) :
    adjCount G A B + ((A ×ˢ B).filter (fun xy => ¬ G.Adj xy.1 xy.2)).card =
      A.card * B.card
```

## EG617.complete_cross_of_no_missing

Source: EG617/Core/BipartiteExterior.lean

```lean
theorem complete_cross_of_no_missing (G : SimpleGraph V) (A B : Finset V)
    (h : ((A ×ˢ B).filter (fun xy => ¬ G.Adj xy.1 xy.2)).card = 0) :
    ∀ a ∈ A, ∀ b ∈ B, G.Adj a b
```

## EG617.unique_missing_cross_of_card_one

Source: EG617/Core/BipartiteExterior.lean

```lean
theorem unique_missing_cross_of_card_one (G : SimpleGraph V) (A B : Finset V)
    (h : ((A ×ˢ B).filter (fun xy => ¬ G.Adj xy.1 xy.2)).card = 1) :
    ∃ a ∈ A, ∃ b ∈ B, ∀ x ∈ A, ∀ y ∈ B,
      (¬ G.Adj x y ↔ x = a ∧ y = b)
```

## EG617.bipartite_18_dense_classification

Source: EG617/Core/BipartiteExterior.lean

```lean
theorem bipartite_18_dense_classification (G : SimpleGraph V)
    (hV : Fintype.card V = 18) (hb : G.Colorable 2)
    (he : 80 ≤ G.edgeFinset.card) :
    ∃ A : Finset V, G.IsIndepSet (A : Set V) ∧ G.IsIndepSet ((Aᶜ : Finset V) : Set V) ∧
      ((A.card = 9 ∧ Aᶜ.card = 9 ∧ G.edgeFinset.card = 81 ∧
          ∀ a ∈ A, ∀ b ∈ Aᶜ, G.Adj a b) ∨
       (A.card = 8 ∧ Aᶜ.card = 10 ∧ G.edgeFinset.card = 80 ∧
          ∀ a ∈ A, ∀ b ∈ Aᶜ, G.Adj a b) ∨
       (A.card = 9 ∧ Aᶜ.card = 9 ∧ G.edgeFinset.card = 80 ∧
          ∃ a ∈ A, ∃ b ∈ Aᶜ, ∀ x ∈ A, ∀ y ∈ Aᶜ,
            (¬ G.Adj x y ↔ x = a ∧ y = b)))
```

## EG617.adjCount

Source: EG617/Core/EdgePartition.lean

```lean
noncomputable def adjCount (G : SimpleGraph V) (S T : Finset V) : ℕ
```

## EG617.adjCount_eq_sum_filter

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_eq_sum_filter (G : SimpleGraph V) (S T : Finset V) :
    adjCount G S T = ∑ x ∈ S, (T.filter (G.Adj x)).card
```

## EG617.degree_induce_eq_filter

Source: EG617/Core/EdgePartition.lean

```lean
theorem degree_induce_eq_filter (G : SimpleGraph V) (S : Finset V) (x : S) :
    (G.induce (S : Set V)).degree x = (S.filter (G.Adj x)).card
```

## EG617.adjCount_self

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_self (G : SimpleGraph V) (S : Finset V) :
    adjCount G S S = 2 * coreInducedEdgeCount G S
```

## EG617.adjCount_symm

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_symm (G : SimpleGraph V) (S T : Finset V) :
    adjCount G S T = adjCount G T S
```

## EG617.adjCount_union_left

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_union_left (G : SimpleGraph V) (S T U : Finset V)
    (hd : Disjoint S T) : adjCount G (S ∪ T) U = adjCount G S U + adjCount G T U
```

## EG617.adjCount_union_right

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_union_right (G : SimpleGraph V) (S T U : Finset V)
    (hd : Disjoint T U) : adjCount G S (T ∪ U) = adjCount G S T + adjCount G S U
```

## EG617.edge_partition

Source: EG617/Core/EdgePartition.lean

```lean
theorem edge_partition (G : SimpleGraph V) (S : Finset V) :
    G.edgeFinset.card = coreInducedEdgeCount G S + adjCount G S Sᶜ +
      coreInducedEdgeCount G Sᶜ
```

## EG617.adjCount_right_univ

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_right_univ (G : SimpleGraph V) (S : Finset V) :
    adjCount G S Finset.univ = ∑ x ∈ S, G.degree x
```

## EG617.adjCount_le_sum_degrees

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_le_sum_degrees (G : SimpleGraph V) (S T : Finset V) :
    adjCount G S T ≤ ∑ x ∈ S, G.degree x
```

## EG617.adjCount_independent_zero

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_independent_zero (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) : adjCount G I I = 0
```

## EG617.twice_independent_card_le_of_degree_two

Source: EG617/Core/EdgePartition.lean

```lean
theorem twice_independent_card_le_of_degree_two (G : SimpleGraph V)
    (hd : ∀ v, G.degree v = 2) (I : Finset V) (hI : G.IsIndepSet (I : Set V)) :
    2 * I.card ≤ Fintype.card V
```

## EG617.oddCycleBound

Source: EG617/Core/OddCycleArithmetic.lean

```lean
def oddCycleBound (n k : ℕ) : ℕ
```

## EG617.oddCycleBound_23_two

Source: EG617/Core/OddCycleArithmetic.lean

```lean
theorem oddCycleBound_23_two : oddCycleBound 23 2 = 122
```

## EG617.oddCycleBound_23_ge_three

Source: EG617/Core/OddCycleArithmetic.lean

```lean
theorem oddCycleBound_23_ge_three (k : ℕ) (hk : 3 ≤ k)
    (hfit : 2 * k + 1 ≤ 23) : oddCycleBound 23 k ≤ 119
```

## EG617.oddCycleBound_23_three

Source: EG617/Core/OddCycleArithmetic.lean

```lean
theorem oddCycleBound_23_three : oddCycleBound 23 3 = 119
```

## EG617.oddCycleBound_18

Source: EG617/Core/OddCycleArithmetic.lean

```lean
theorem oddCycleBound_18 (k : ℕ) (hk : 2 ≤ k)
    (hfit : 2 * k + 1 ≤ 18) : oddCycleBound 18 k ≤ 73
```

## EG617.oddCycleBound_18_two

Source: EG617/Core/OddCycleArithmetic.lean

```lean
theorem oddCycleBound_18_two : oddCycleBound 18 2 = 73
```

## EG617.cycle_support_card

Source: EG617/Core/OddCycleBound.lean

```lean
theorem cycle_support_card {v : V} (p : G.Walk v v) (hp : p.IsCycle) :
    p.support.toFinset.card = p.length
```

## EG617.chordless_cycle_induced_degree_two

Source: EG617/Core/OddCycleBound.lean

```lean
theorem chordless_cycle_induced_degree_two {v : V} (p : G.Walk v v)
    (hp : p.IsCycle) (hc : p.IsChordless) (x : p.support.toFinset) :
    (G.induce (p.support.toFinset : Set V)).degree x = 2
```

## EG617.chordless_cycle_induced_edges

Source: EG617/Core/OddCycleBound.lean

```lean
theorem chordless_cycle_induced_edges {v : V} (p : G.Walk v v)
    (hp : p.IsCycle) (hc : p.IsChordless) :
    coreInducedEdgeCount G p.support.toFinset = p.length
```

## EG617.twice_subset_independent_card_le_of_induced_degree_two

Source: EG617/Core/OddCycleBound.lean

```lean
theorem twice_subset_independent_card_le_of_induced_degree_two
    (G : SimpleGraph V) (S : Finset V)
    (hd : ∀ v : S, (G.induce (S : Set V)).degree v = 2)
    (I : Finset V) (hIS : I ⊆ S) (hI : G.IsIndepSet (I : Set V)) :
    2 * I.card ≤ S.card
```

## EG617.shortestOddLoop_neighbor_card_le

Source: EG617/Core/OddCycleBound.lean

```lean
theorem shortestOddLoop_neighbor_card_le {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) (ht : G.CliqueFree 3) (k : ℕ)
    (hlen : p.length = 2 * k + 1) (x : V) :
    (p.support.toFinset.filter (G.Adj x)).card ≤ k
```

## EG617.triangleFree_induced_mantel

Source: EG617/Core/OddCycleBound.lean

```lean
theorem triangleFree_induced_mantel (G : SimpleGraph V) (ht : G.CliqueFree 3)
    (S : Finset V) : coreInducedEdgeCount G S ≤ S.card ^ 2 / 4
```

## EG617.shortestOddLoop_edge_bound

Source: EG617/Core/OddCycleBound.lean

```lean
theorem shortestOddLoop_edge_bound (G : SimpleGraph V) (ht : G.CliqueFree 3)
    {v : V} (p : G.Walk v v) (hp : IsShortestOddLoop p) (k : ℕ)
    (hlen : p.length = 2 * k + 1) :
    G.edgeFinset.card ≤ oddCycleBound (Fintype.card V) k
```

## EG617.shortestOddLoop_half_length_ge_two

Source: EG617/Core/OddCycleBound.lean

```lean
theorem shortestOddLoop_half_length_ge_two (G : SimpleGraph V)
    (ht : G.CliqueFree 3) {v : V} (p : G.Walk v v) (hp : IsShortestOddLoop p)
    (k : ℕ) (hlen : p.length = 2 * k + 1) : 2 ≤ k
```

## EG617.triangleFree_nonbipartite_edge_bound

Source: EG617/Core/OddCycleBound.lean

```lean
theorem triangleFree_nonbipartite_edge_bound (G : SimpleGraph V)
    (ht : G.CliqueFree 3) (hb : ¬ G.Colorable 2) :
    ∃ k : ℕ, 2 ≤ k ∧ 2 * k + 1 ≤ Fintype.card V ∧
      G.edgeFinset.card ≤ oddCycleBound (Fintype.card V) k
```

## EG617.triangleFree_nonbipartite_18_edges_le_73

Source: EG617/Core/OddCycleBound.lean

```lean
theorem triangleFree_nonbipartite_18_edges_le_73 (G : SimpleGraph V)
    (hV : Fintype.card V = 18) (ht : G.CliqueFree 3) (hb : ¬ G.Colorable 2) :
    G.edgeFinset.card ≤ 73
```

## EG617.IsShortestOddCycle

Source: EG617/Core/OddCycleBound.lean

```lean
def IsShortestOddCycle {v : V} (p : G.Walk v v) : Prop
```

## EG617.shortestOddCycle_iff_shortestOddLoop

Source: EG617/Core/OddCycleBound.lean

```lean
theorem shortestOddCycle_iff_shortestOddLoop {v : V} (p : G.Walk v v) :
    IsShortestOddCycle p ↔ IsShortestOddLoop p
```

## EG617.shortestOddCycle_edge_bound

Source: EG617/Core/OddCycleBound.lean

```lean
theorem shortestOddCycle_edge_bound (G : SimpleGraph V) (ht : G.CliqueFree 3)
    {v : V} (p : G.Walk v v) (hp : IsShortestOddCycle p) (k : ℕ)
    (hlen : p.length = 2 * k + 1) :
    G.edgeFinset.card ≤ oddCycleBound (Fintype.card V) k
```

## EG617.IsShortestOddLoop

Source: EG617/Core/OddCycleStructure.lean

```lean
def IsShortestOddLoop {v : V} (p : G.Walk v v) : Prop
```

## EG617.bypass_parity_of_short_loops_even

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem bypass_parity_of_short_loops_even (N : ℕ)
    (hN : ∀ v (q : G.Walk v v), q.length < N → Even q.length)
    {a b : V} (p : G.Walk a b) (hp : p.length < N) :
    p.bypass.length % 2 = p.length % 2
```

## EG617.shortestOddLoop_isCycle

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem shortestOddLoop_isCycle {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) : p.IsCycle
```

## EG617.exists_shortestOddLoop

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem exists_shortestOddLoop (hG : ¬ G.Colorable 2) :
    ∃ v, ∃ p : G.Walk v v, IsShortestOddLoop p
```

## EG617.exists_odd_cycle_of_not_two_colorable

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem exists_odd_cycle_of_not_two_colorable (hG : ¬ G.Colorable 2) :
    ∃ v, ∃ p : G.Walk v v, p.IsCycle ∧ IsShortestOddLoop p
```

## EG617.walk_end_edge_mem_of_length_one

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem walk_end_edge_mem_of_length_one {a b : V} (p : G.Walk a b)
    (hp : p.length = 1) : s(a, b) ∈ p.edges
```

## EG617.shortestOddLoop_isChordless

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem shortestOddLoop_isChordless {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) : p.IsChordless
```

## EG617.cycleGraph_twice_independent_card_le

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem cycleGraph_twice_independent_card_le (m : ℕ)
    (S : Finset (Fin (m + 3)))
    (hS : (SimpleGraph.cycleGraph (m + 3)).IsIndepSet (S : Set (Fin (m + 3)))) :
    2 * S.card ≤ m + 3
```

## EG617.cycle_copy_twice_neighbor_card_le

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem cycle_copy_twice_neighbor_card_le (m : ℕ)
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph (m + 3)) G)
    (ht : G.CliqueFree 3) (x : V) :
    2 * ((Finset.univ : Finset (Fin (m + 3))).filter
      (fun i => G.Adj x (f i))).card ≤ m + 3
```

## EG617.core_not_two_colorable_of_card_24

Source: EG617/Core/R224.lean

```lean
theorem core_not_two_colorable_of_card_24 (L : SimpleGraph V)
    (hV : Fintype.card V = 24)
    (hI : CoreIndependenceBound 11 L) : ¬ L.Colorable 2
```

## EG617.core_triangleFree_edges_lt_132_of_card_24

Source: EG617/Core/R224.lean

```lean
theorem core_triangleFree_edges_lt_132_of_card_24 (L : SimpleGraph V)
    (hV : Fintype.card V = 24)
    (ht : L.CliqueFree 3) (hI : CoreIndependenceBound 11 L) :
    L.edgeFinset.card < 132
```

## EG617.core_R224_empty_of_card

Source: EG617/Core/R224.lean

```lean
theorem core_R224_empty_of_card (G : SimpleGraph V)
    (hV : Fintype.card V = 24) : ¬ CoreAdmissible 2 G
```

## EG617.core_not_two_colorable_24

Source: EG617/Core/R224.lean

```lean
theorem core_not_two_colorable_24 (L : SimpleGraph (Fin 24))
    (hI : CoreIndependenceBound 11 L) : ¬ L.Colorable 2
```

## EG617.core_triangleFree24_edges_lt_132

Source: EG617/Core/R224.lean

```lean
theorem core_triangleFree24_edges_lt_132 (L : SimpleGraph (Fin 24))
    (ht : L.CliqueFree 3) (hI : CoreIndependenceBound 11 L) :
    L.edgeFinset.card < 132
```

## EG617.core_R224_empty

Source: EG617/Core/R224.lean

```lean
theorem core_R224_empty (G : SimpleGraph (Fin 24)) : ¬ CoreAdmissible 2 G
```

## EG617.core_R3_card_le_degree_add_24

Source: EG617/Core/R224.lean

```lean
theorem core_R3_card_le_degree_add_24 (G : SimpleGraph V)
    (hG : CoreAdmissible 3 G) (v : V) : Fintype.card V ≤ G.degree v + 24
```

## EG617.core_R335_degree_ge_11

Source: EG617/Core/R224.lean

```lean
theorem core_R335_degree_ge_11 (G : SimpleGraph (Fin 35))
    (hG : CoreAdmissible 3 G) (v : Fin 35) : 11 ≤ G.degree v
```

## EG617.core_R337_empty_of_card

Source: EG617/Core/R224.lean

```lean
theorem core_R337_empty_of_card (G : SimpleGraph V)
    (hV : Fintype.card V = 37) : ¬ CoreAdmissible 3 G
```

## EG617.core_R337_empty

Source: EG617/Core/R224.lean

```lean
theorem core_R337_empty (G : SimpleGraph (Fin 37)) : ¬ CoreAdmissible 3 G
```

## EG617.core_R4_card_le_degree_add_37

Source: EG617/Core/R224.lean

```lean
theorem core_R4_card_le_degree_add_37 (G : SimpleGraph V)
    (hG : CoreAdmissible 4 G) (v : V) : Fintype.card V ≤ G.degree v + 37
```

## EG617.core_R447_degree_ge_10

Source: EG617/Core/R224.lean

```lean
theorem core_R447_degree_ge_10 (G : SimpleGraph (Fin 47))
    (hG : CoreAdmissible 4 G) (v : Fin 47) : 10 ≤ G.degree v
```

## EG617.not_two_colorable_of_independence_bound

Source: EG617/Core/R23Reduction.lean

```lean
theorem not_two_colorable_of_independence_bound (G : SimpleGraph V) (a : ℕ)
    (hI : CoreIndependenceBound a G) (hV : 2 * a < Fintype.card V) :
    ¬ G.Colorable 2
```

## EG617.r23_shortestOddLoop_length_five

Source: EG617/Core/R23Reduction.lean

```lean
theorem r23_shortestOddLoop_length_five (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (he : 121 ≤ G.edgeFinset.card) {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) : p.length = 5
```

## EG617.r23_exists_five_cycle_bipartite_exterior

Source: EG617/Core/R23Reduction.lean

```lean
theorem r23_exists_five_cycle_bipartite_exterior (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ v, ∃ p : G.Walk v v, IsShortestOddLoop p ∧ p.IsCycle ∧
      p.IsChordless ∧ p.length = 5 ∧
      p.support.toFinsetᶜ.card = 18 ∧
      80 ≤ coreInducedEdgeCount G p.support.toFinsetᶜ ∧
      (G.induce ((p.support.toFinsetᶜ : Finset V) : Set V)).Colorable 2
```

## EG617.independent_card_le_twelve

Source: EG617/Frontend/ColoringReduction.lean

```lean
theorem independent_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hind : ∀ u ∈ S, ∀ v ∈ S, ¬ (colorGraph c i).Adj u v) :
    S.card ≤ 12
```

## EG617.monochromatic_card_le_twelve

Source: EG617/Frontend/ColoringReduction.lean

```lean
theorem monochromatic_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hmono : ∀ u ∈ S, ∀ v ∈ S, ∀ h : u ≠ v, c (edgeOf u v h) = i) :
    S.card ≤ 12
```

## EG617.colorGraph_clique_card_le_twelve

Source: EG617/Frontend/ColoringReduction.lean

```lean
theorem colorGraph_clique_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hclique : ∀ u ∈ S, ∀ v ∈ S, u ≠ v → (colorGraph c i).Adj u v) :
    S.card ≤ 12
```

## EG617.inducedColorGraph

Source: EG617/Frontend/EdgeCounting.lean

```lean
def inducedColorGraph (c : EdgeColoring) (i : Color) (S : Finset Vertex) :
    SimpleGraph S
```

## EG617.colorEdgeCount

Source: EG617/Frontend/EdgeCounting.lean

```lean
noncomputable def colorEdgeCount (c : EdgeColoring) (i : Color)
    (S : Finset Vertex) : ℕ
```

## EG617.colorEdgeCount_univ

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem colorEdgeCount_univ (c : EdgeColoring) (i : Color) :
    colorEdgeCount c i Finset.univ = (colorGraph c i).edgeFinset.card
```

## EG617.inducedColorGraph_adj_iff

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem inducedColorGraph_adj_iff (c : EdgeColoring) (i : Color)
    (S : Finset Vertex) (u v : S) :
    (inducedColorGraph c i S).Adj u v ↔
      ∃ h : (u : Vertex) ≠ (v : Vertex), c (edgeOf u v h) = i
```

## EG617.induced_edge_unique_color

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem induced_edge_unique_color (c : EdgeColoring) (S : Finset Vertex)
    (u v : S) (h : u ≠ v) :
    ∃! i : Color, (inducedColorGraph c i S).Adj u v
```

## EG617.induced_color_edges_disjoint

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem induced_color_edges_disjoint (c : EdgeColoring) (S : Finset Vertex) :
    ((Finset.univ : Finset Color) : Set Color).PairwiseDisjoint
      (fun i => (inducedColorGraph c i S).edgeFinset)
```

## EG617.induced_color_edges_union

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem induced_color_edges_union (c : EdgeColoring) (S : Finset Vertex) :
    (Finset.univ.biUnion fun i : Color => (inducedColorGraph c i S).edgeFinset) =
      (⊤ : SimpleGraph S).edgeFinset
```

## EG617.sum_colorEdgeCount

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem sum_colorEdgeCount (c : EdgeColoring) (S : Finset Vertex) :
    ∑ i : Color, colorEdgeCount c i S = S.card.choose 2
```

## EG617.D

Source: EG617/Frontend/HereditaryCaps.lean

```lean
def D (n : ℕ) : ℕ
```

## EG617.colorEdgeCount_add_eleven_tau_le

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem colorEdgeCount_add_eleven_tau_le (c : EdgeColoring)
    (hc : ValidColoring c) (i : Color) (S : Finset Vertex) :
    colorEdgeCount c i S + 11 * tau12 S.card ≤ S.card.choose 2
```

## EG617.hereditary_color_cap

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem hereditary_color_cap (c : EdgeColoring) (hc : ValidColoring c)
    (i : Color) (S : Finset Vertex) : colorEdgeCount c i S ≤ D S.card
```

## EG617.hereditary_cap_subtraction_exact

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem hereditary_cap_subtraction_exact (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) : D S.card + 11 * tau12 S.card = S.card.choose 2
```

## EG617.exists_least_color

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem exists_least_color (c : EdgeColoring) :
    ∃ i : Color, ∀ j : Color,
      colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ
```

## EG617.least_color_edgeCount_le_870

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem least_color_edgeCount_le_870 (c : EdgeColoring) (i : Color)
    (hi : ∀ j : Color,
      colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ) :
    colorEdgeCount c i Finset.univ ≤ 870
```

## EG617.exists_least_color_with_hereditary_cap

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem exists_least_color_with_hereditary_cap (c : EdgeColoring)
    (hc : ValidColoring c) :
    ∃ i : Color,
      (∀ j : Color, colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ) ∧
      colorEdgeCount c i Finset.univ ≤ 870 ∧
      (∀ S : Finset Vertex, colorEdgeCount c i S ≤ D S.card)
```

## EG617.exists_colorGraph_card_edgeFinset_le_870

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem exists_colorGraph_card_edgeFinset_le_870 (c : EdgeColoring) :
    ∃ i : Color, (colorGraph c i).edgeFinset.card ≤ 870
```

## EG617.inducedColorGraph_compl_cliqueFree

Source: EG617/Frontend/TuranBounds.lean

```lean
theorem inducedColorGraph_compl_cliqueFree (c : EdgeColoring)
    (hc : ValidColoring c) (i : Color) (S : Finset Vertex) :
    (inducedColorGraph c i S)ᶜ.CliqueFree 13
```

## EG617.tau12_le_colorEdgeCount

Source: EG617/Frontend/TuranBounds.lean

```lean
theorem tau12_le_colorEdgeCount (c : EdgeColoring) (hc : ValidColoring c)
    (i : Color) (S : Finset Vertex) :
    tau12 S.card ≤ colorEdgeCount c i S
```

