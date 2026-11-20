# Exact Lean statements

Code 8b06204dcafa34c87fee26c0d3b6befaa74afb93, CI 44675832316. Full proof bodies are in standard .lean files.

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

## EG617.c5_incompatible_endpoint_forces_singleton

Source: EG617/Core/C5MissingEdge.lean

```lean
theorem c5_incompatible_endpoint_forces_singleton (A B : Finset (Fin 5))
    (hA : A.Nonempty) (hB : B.Nonempty) (u v : Fin 5)
    (hAB : ∀ a ∈ A, ∀ b ∈ B, (SimpleGraph.cycleGraph 5).Adj a b)
    (hu : ∀ b ∈ B, (SimpleGraph.cycleGraph 5).Adj u b)
    (hv : ∀ a ∈ A, (SimpleGraph.cycleGraph 5).Adj a v)
    (huv : ¬ (SimpleGraph.cycleGraph 5).Adj u v) : A.card = 1
```

## EG617.c5_missing_edge_type_sets

Source: EG617/Core/C5MissingEdge.lean

```lean
theorem c5_missing_edge_type_sets (A B : Finset (Fin 5))
    (hA : A.Nonempty) (hB : B.Nonempty) (u v : Fin 5)
    (hAB : ∀ a ∈ A, ∀ b ∈ B, (SimpleGraph.cycleGraph 5).Adj a b)
    (hu : ∀ b ∈ B, (SimpleGraph.cycleGraph 5).Adj u b)
    (hv : ∀ a ∈ A, (SimpleGraph.cycleGraph 5).Adj a v)
    (huv : ¬ (SimpleGraph.cycleGraph 5).Adj u v) : A.card = 1 ∧ B.card = 1
```

## EG617.c5_missing_endpoint_orientations

Source: EG617/Core/C5MissingEdge.lean

```lean
theorem c5_missing_endpoint_orientations (a b u v : Fin 5)
    (hab : (SimpleGraph.cycleGraph 5).Adj a b)
    (hub : (SimpleGraph.cycleGraph 5).Adj u b)
    (hav : (SimpleGraph.cycleGraph 5).Adj a v)
    (huv : ¬ (SimpleGraph.cycleGraph 5).Adj u v) :
    (b = a + 1 ∧ u = a + 2 ∧ v = a - 1) ∨
      (b = a - 1 ∧ u = a - 2 ∧ v = a + 1)
```

## EG617.c5_singleton_extension

Source: EG617/Core/C5MissingEdge.lean

```lean
theorem c5_singleton_extension (a : Fin 5) (B : Finset (Fin 5))
    (hB : B ⊆ c5Type a) (p : Fin 5) (hp : ∀ b ∈ B, p ∉ c5Type b) :
    ∃ i : Fin 5, p ∈ c5Type i ∧ ∀ b ∈ B, Disjoint (c5Type i) (c5Type b)
```

## EG617.disjoint_cycle_neighbors_no_common_neighbor

Source: EG617/Core/C5MissingGraphLift.lean

```lean
theorem disjoint_cycle_neighbors_no_common_neighbor
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G)
    (S A B : Finset V) (hS : Finset.univ.image f = S) (hcover : A ∪ B = Sᶜ)
    (hA : G.IsIndepSet (A : Set V)) (hB : G.IsIndepSet (B : Set V))
    (u v : V) (hu : u ∈ A) (hv : v ∈ B)
    (hd : Disjoint (cycleNeighborLabels f u) (cycleNeighborLabels f v)) :
    ∀ w, G.Adj u w → ¬ G.Adj v w
```

## EG617.missing_exterior_type_presentation

Source: EG617/Core/C5MissingGraphLift.lean

```lean
theorem missing_exterior_type_presentation
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S A B : Finset V) (hS : Finset.univ.image f = S) (hcover : A ∪ B = Sᶜ)
    (u v : V) (hA : (A.erase u).Nonempty) (hB : (B.erase v).Nonempty)
    (t : V → Fin 5) (hlabels : ∀ x, cycleNeighborLabels f x = c5Type (t x))
    (hmiss : ∀ x ∈ A, ∀ y ∈ B, (¬ G.Adj x y ↔ x = u ∧ y = v))
    (hincompat : ¬ (SimpleGraph.cycleGraph 5).Adj (t u) (t v)) :
    ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y)
```

## EG617.missing_exterior_type_orientations

Source: EG617/Core/C5MissingTypeFibers.lean

```lean
theorem missing_exterior_type_orientations
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (A B : Finset V) (u v : V) (hu : u ∈ A) (hv : v ∈ B)
    (hA : (A.erase u).Nonempty) (hB : (B.erase v).Nonempty)
    (t : V → Fin 5) (hlabels : ∀ x, cycleNeighborLabels f x = c5Type (t x))
    (hmiss : ∀ x ∈ A, ∀ y ∈ B, (¬ G.Adj x y ↔ x = u ∧ y = v))
    (hincompat : ¬ (SimpleGraph.cycleGraph 5).Adj (t u) (t v)) :
    ∃ a b : Fin 5, (∀ x ∈ A.erase u, t x = a) ∧
      (∀ y ∈ B.erase v, t y = b) ∧
      ((b = a + 1 ∧ t u = a + 2 ∧ t v = a - 1) ∨
       (b = a - 1 ∧ t u = a - 2 ∧ t v = a + 1))
```

## EG617.one_exception_type_fiber_card

Source: EG617/Core/C5MissingTypeFibers.lean

```lean
theorem one_exception_type_fiber_card (C : Finset V) (t : V → Fin 5)
    (u : V) (hu : u ∈ C) (hc : C.card = 9) (a i : Fin 5)
    (hrest : ∀ x ∈ C.erase u, t x = a) :
    (C.filter (fun x => t x = i)).card =
      (if a = i then 8 else 0) + (if t u = i then 1 else 0)
```

## EG617.missing_exterior_type_fiber_formula

Source: EG617/Core/C5MissingTypeFibers.lean

```lean
theorem missing_exterior_type_fiber_formula
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (S A B : Finset V)
    (hS : Finset.univ.image f = S) (hcover : A ∪ B = Sᶜ) (hdis : Disjoint A B)
    (hA : A.card = 9) (hB : B.card = 9) (u v : V) (hu : u ∈ A) (hv : v ∈ B)
    (t : V → Fin 5) (hcycle : ∀ i, t (f i) = i) (a b : Fin 5)
    (hAt : ∀ x ∈ A.erase u, t x = a) (hBt : ∀ y ∈ B.erase v, t y = b) :
    ∀ i : Fin 5, (Finset.univ.filter (fun x => t x = i)).card =
      1 + (if a = i then 8 else 0) + (if b = i then 8 else 0) +
        (if t u = i then 1 else 0) + (if t v = i then 1 else 0)
```

## EG617.c5_missing_fiber_profile

Source: EG617/Core/C5MissingTypeFibers.lean

```lean
theorem c5_missing_fiber_profile (n : Fin 5 → ℕ) (a b u v : Fin 5)
    (hn : ∀ i, n i = 1 + (if a = i then 8 else 0) + (if b = i then 8 else 0) +
      (if u = i then 1 else 0) + (if v = i then 1 else 0))
    (ho : (b = a + 1 ∧ u = a + 2 ∧ v = a - 1) ∨
      (b = a - 1 ∧ u = a - 2 ∧ v = a + 1)) :
    ∃ c : Fin 5, n c = 9 ∧ n (c + 1) = 9 ∧ n (c + 2) = 2 ∧
      n (c - 2) = 1 ∧ n (c - 1) = 2
```

## EG617.singleton_cycle_edge_completion_witness

Source: EG617/Core/C5SingletonGraphLift.lean

```lean
theorem singleton_cycle_edge_completion_witness
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S A B : Finset V) (hS : Finset.univ.image f = S)
    (hcover : A ∪ B = Sᶜ) (hA : G.IsIndepSet (A : Set V))
    (u z : V) (hu : u ∈ A) (hz : z ∈ A) (p : Fin 5)
    (hsingle : cycleNeighborLabels f u = {p})
    (hz2 : (cycleNeighborLabels f z).card = 2)
    (hB2 : ∀ x ∈ B, (cycleNeighborLabels f x).card = 2)
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y) :
    ∃ q : Fin 5, u ≠ f q ∧ ¬ G.Adj u (f q) ∧
      ∀ w, G.Adj u w → ¬ G.Adj (f q) w
```

## EG617.cycle_type_fiber_card

Source: EG617/Core/C5TypeFibers.lean

```lean
theorem cycle_type_fiber_card
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (S : Finset V)
    (hS : Finset.univ.image f = S) (t : V → Fin 5)
    (hcycle : ∀ i, t (f i) = i) (i : Fin 5) :
    (Finset.univ.filter (fun x => t x = i)).card =
      1 + (Sᶜ.filter (fun x => t x = i)).card
```

## EG617.singleton_side_type_fiber_profile

Source: EG617/Core/C5TypeFibers.lean

```lean
theorem singleton_side_type_fiber_profile
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S A B : Finset V) (hS : Finset.univ.image f = S)
    (hcover : A ∪ B = Sᶜ) (hA : A.card = 9)
    (t : V → Fin 5) (hlabels : ∀ x, cycleNeighborLabels f x = c5Type (t x))
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y)
    (hsingle : (A.image t).card = 1) :
    ∃ a : Fin 5, (Finset.univ.filter (fun x => t x = a)).card = 10 ∧
      ∀ i, i ≠ a → ¬ (SimpleGraph.cycleGraph 5).Adj a i →
        (Finset.univ.filter (fun x => t x = i)).card = 1
```

## EG617.complete_exterior_type_fiber_profile

Source: EG617/Core/C5TypeFibers.lean

```lean
theorem complete_exterior_type_fiber_profile
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S A B : Finset V) (hS : Finset.univ.image f = S)
    (hcover : A ∪ B = Sᶜ) (hA : A.card = 9) (hB : B.card = 9)
    (t : V → Fin 5) (hlabels : ∀ x, cycleNeighborLabels f x = c5Type (t x))
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y) :
    ∃ a : Fin 5, (Finset.univ.filter (fun x => t x = a)).card = 10 ∧
      ∀ i, i ≠ a → ¬ (SimpleGraph.cycleGraph 5).Adj a i →
        (Finset.univ.filter (fun x => t x = i)).card = 1
```

## EG617.cycleNeighborLabels_cycle_vertex

Source: EG617/Core/C5TypePresentation.lean

```lean
theorem cycleNeighborLabels_cycle_vertex
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (i : Fin 5) : cycleNeighborLabels f (f i) = c5Type i
```

## EG617.complete_exterior_type_presentation

Source: EG617/Core/C5TypePresentation.lean

```lean
theorem complete_exterior_type_presentation
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S A B : Finset V) (hS : Finset.univ.image f = S)
    (hcover : A ∪ B = Sᶜ) (hA : A.Nonempty) (hB : B.Nonempty)
    (t : V → Fin 5) (hlabels : ∀ x, cycleNeighborLabels f x = c5Type (t x))
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y) :
    ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y)
```

## EG617.exists_cycle_type_assignment

Source: EG617/Core/C5TypePresentation.lean

```lean
theorem exists_cycle_type_assignment
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S : Finset V) (hS : Finset.univ.image f = S)
    (hd : ∀ x ∈ Sᶜ, (S.filter (G.Adj x)).card = 2) :
    ∃ t : V → Fin 5, ∀ x, cycleNeighborLabels f x = c5Type (t x)
```

## EG617.complete_exterior_has_type_presentation

Source: EG617/Core/C5TypePresentation.lean

```lean
theorem complete_exterior_has_type_presentation
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S A B : Finset V) (hS : Finset.univ.image f = S)
    (hcover : A ∪ B = Sᶜ) (hA : A.Nonempty) (hB : B.Nonempty)
    (hd : ∀ x ∈ Sᶜ, (S.filter (G.Adj x)).card = 2)
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y) :
    ∃ t : V → Fin 5, (∀ x, cycleNeighborLabels f x = c5Type (t x)) ∧
      ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y)
```

## EG617.c5Type

Source: EG617/Core/C5Types.lean

```lean
def c5Type (i : Fin 5) : Finset (Fin 5)
```

## EG617.c5Type_card

Source: EG617/Core/C5Types.lean

```lean
theorem c5Type_card (i : Fin 5) : (c5Type i).card = 2
```

## EG617.c5Type_disjoint_iff

Source: EG617/Core/C5Types.lean

```lean
theorem c5Type_disjoint_iff (i j : Fin 5) :
    Disjoint (c5Type i) (c5Type j) ↔ (SimpleGraph.cycleGraph 5).Adj i j
```

## EG617.c5_adj_iff_mem_type

Source: EG617/Core/C5Types.lean

```lean
theorem c5_adj_iff_mem_type (i j : Fin 5) :
    (SimpleGraph.cycleGraph 5).Adj i j ↔ i ∈ c5Type j
```

## EG617.c5_independent_pair_unique_type

Source: EG617/Core/C5Types.lean

```lean
theorem c5_independent_pair_unique_type (S : Finset (Fin 5))
    (hcard : S.card = 2)
    (hI : ∀ i ∈ S, ∀ j ∈ S, ¬ (SimpleGraph.cycleGraph 5).Adj i j) :
    ∃! i : Fin 5, S = c5Type i
```

## EG617.c5_common_neighbors_unique

Source: EG617/Core/C5Types.lean

```lean
theorem c5_common_neighbors_unique (i j k l : Fin 5) (hne : i ≠ j)
    (hik : (SimpleGraph.cycleGraph 5).Adj i k)
    (hjk : (SimpleGraph.cycleGraph 5).Adj j k)
    (hil : (SimpleGraph.cycleGraph 5).Adj i l)
    (hjl : (SimpleGraph.cycleGraph 5).Adj j l) : k = l
```

## EG617.c5_complete_type_sets

Source: EG617/Core/C5Types.lean

```lean
theorem c5_complete_type_sets (A B : Finset (Fin 5))
    (hA : A.Nonempty) (hB : B.Nonempty)
    (hcross : ∀ i ∈ A, ∀ j ∈ B, Disjoint (c5Type i) (c5Type j)) :
    (A.card = 1 ∨ B.card = 1) ∧ A.card ≤ 2 ∧ B.card ≤ 2
```

## EG617.cycleNeighborLabels

Source: EG617/Core/C5Types.lean

```lean
noncomputable def cycleNeighborLabels
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (x : V) : Finset (Fin 5)
```

## EG617.cycleNeighborLabels_independent

Source: EG617/Core/C5Types.lean

```lean
theorem cycleNeighborLabels_independent
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3) (x : V) :
    ∀ i ∈ cycleNeighborLabels f x, ∀ j ∈ cycleNeighborLabels f x,
      ¬ (SimpleGraph.cycleGraph 5).Adj i j
```

## EG617.cycleNeighborLabels_unique_type

Source: EG617/Core/C5Types.lean

```lean
theorem cycleNeighborLabels_unique_type
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3) (x : V)
    (hc : (cycleNeighborLabels f x).card = 2) :
    ∃! i : Fin 5, cycleNeighborLabels f x = c5Type i
```

## EG617.adjacent_cycleNeighborLabels_disjoint

Source: EG617/Core/C5Types.lean

```lean
theorem adjacent_cycleNeighborLabels_disjoint
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    {x y : V} (hxy : G.Adj x y) :
    Disjoint (cycleNeighborLabels f x) (cycleNeighborLabels f y)
```

## EG617.complete_bipartite_type_image

Source: EG617/Core/C5Types.lean

```lean
theorem complete_bipartite_type_image
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (A B : Finset V) (hA : A.Nonempty) (hB : B.Nonempty) (t : V → Fin 5)
    (hlabels : ∀ x, x ∈ A ∨ x ∈ B → cycleNeighborLabels f x = c5Type (t x))
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y) :
    ((A.image t).card = 1 ∨ (B.image t).card = 1) ∧
      (A.image t).card ≤ 2 ∧ (B.image t).card ≤ 2
```

## EG617.CostSixProperty

Source: EG617/Core/CostSixCounts.lean

```lean
def CostSixProperty (G : SimpleGraph V) : Prop
```

## EG617.c5Fiber

Source: EG617/Core/CostSixCounts.lean

```lean
noncomputable def c5Fiber (t : V → Fin 5) (i : Fin 5) : Finset V
```

## EG617.mem_c5Fiber

Source: EG617/Core/CostSixCounts.lean

```lean
@[simp] theorem mem_c5Fiber (t : V → Fin 5) (i : Fin 5) (x : V) :
    x ∈ c5Fiber t i ↔ t x = i
```

## EG617.c5Fiber_disjoint

Source: EG617/Core/CostSixCounts.lean

```lean
theorem c5Fiber_disjoint (t : V → Fin 5) {i j : Fin 5} (hne : i ≠ j) :
    Disjoint (c5Fiber t i) (c5Fiber t j)
```

## EG617.c5Fiber_adjCount

Source: EG617/Core/CostSixCounts.lean

```lean
theorem c5Fiber_adjCount (G : SimpleGraph V) (t : V → Fin 5)
    (hp : ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y)) (i j : Fin 5) :
    adjCount G (c5Fiber t i) (c5Fiber t j) =
      if (SimpleGraph.cycleGraph 5).Adj i j then (c5Fiber t i).card * (c5Fiber t j).card else 0
```

## EG617.c5_three_fiber_witness_counts

Source: EG617/Core/CostSixCounts.lean

```lean
theorem c5_three_fiber_witness_counts (G : SimpleGraph V) (t : V → Fin 5)
    (hp : ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y))
    (i j k : Fin 5) (hij : i ≠ j) (hik : i ≠ k)
    (hnij : ¬ (SimpleGraph.cycleGraph 5).Adj i j)
    (hnik : ¬ (SimpleGraph.cycleGraph 5).Adj i k)
    (hjk : (SimpleGraph.cycleGraph 5).Adj j k) (I : Finset V) :
    let F
```

## EG617.independent_c5_fiber_counts

Source: EG617/Core/CostSixCounts.lean

```lean
theorem independent_c5_fiber_counts (G : SimpleGraph V) (t : V → Fin 5)
    (hp : ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y))
    (I : Finset V) (hI : G.IsIndepSet (I : Set V)) :
    (∀ i, (c5Fiber t i ∩ I).card ≤ (c5Fiber t i).card) ∧
      ∀ i j, (SimpleGraph.cycleGraph 5).Adj i j →
        (c5Fiber t i ∩ I).card = 0 ∨ (c5Fiber t j ∩ I).card = 0
```

## EG617.case_I_cost_arithmetic

Source: EG617/Core/CostSixCounts.lean

```lean
theorem case_I_cost_arithmetic (A B p a s d b : ℕ) (hAB : A + B = 11)
    (hp : p ≤ 10) (ha : a ≤ A) (hs : s ≤ 1) (hd : d ≤ 1) (hb : b ≤ B)
    (hpa : p = 0 ∨ a = 0) (has : a = 0 ∨ s = 0) (hsd : s = 0 ∨ d = 0)
    (hdb : d = 0 ∨ b = 0) (hbp : b = 0 ∨ p = 0) :
    1 + p + s + d ≤ 6 ∨ A + a + b + s ≤ 6 ∨ B + a + b + d ≤ 6
```

## EG617.exceptional_cost_arithmetic

Source: EG617/Core/CostSixCounts.lean

```lean
theorem exceptional_cost_arithmetic (p q c d e : ℕ)
    (hp : p ≤ 9) (hq : q ≤ 9) (hc : c ≤ 2) (hd : d ≤ 1) (he : e ≤ 2)
    (hpq : p = 0 ∨ q = 0) (hqc : q = 0 ∨ c = 0) (hcd : c = 0 ∨ d = 0)
    (hde : d = 0 ∨ e = 0) (hep : e = 0 ∨ p = 0) :
    2 + p + c + d ≤ 4 ∨ 2 + q + d + e ≤ 4
```

## EG617.coreInducedEdgeCount_mono_graph

Source: EG617/Core/CostSixDeletion.lean

```lean
theorem coreInducedEdgeCount_mono_graph (G H : SimpleGraph V) (h : G ≤ H)
    (T : Finset V) : coreInducedEdgeCount G T ≤ coreInducedEdgeCount H T
```

## EG617.independent_sup_edge_or_endpoints

Source: EG617/Core/CostSixDeletion.lean

```lean
theorem independent_sup_edge_or_endpoints (G : SimpleGraph V) (u v : V)
    (I : Finset V) (hI : G.IsIndepSet (I : Set V)) :
    (G ⊔ SimpleGraph.edge u v).IsIndepSet (I : Set V) ∨ (u ∈ I ∧ v ∈ I)
```

## EG617.independent_sup_edge_neighbor_card

Source: EG617/Core/CostSixDeletion.lean

```lean
theorem independent_sup_edge_neighbor_card (G : SimpleGraph V) (u v : V)
    (I S : Finset V) (hI : G.IsIndepSet (I : Set V)) (w : V) (hw : w ∈ I)
    (hS : ∀ x ∈ S, x ∈ I ∧ (G ⊔ SimpleGraph.edge u v).Adj w x) : S.card ≤ 1
```

## EG617.case_I_single_edge_deletion_cost_six

Source: EG617/Core/CostSixDeletion.lean

```lean
theorem case_I_single_edge_deletion_cost_six (G : SimpleGraph V) (u v : V)
    (hne : u ≠ v) (h : R23CaseIProfile (G ⊔ SimpleGraph.edge u v)) :
    CostSixProperty G
```

## EG617.r23_cost_six

Source: EG617/Core/CostSixDeletion.lean

```lean
theorem r23_cost_six (G : SimpleGraph V) (hV : Fintype.card V = 23)
    (ht : G.CliqueFree 3) (hI : CoreIndependenceBound 11 G)
    (he : 121 ≤ G.edgeFinset.card) : CostSixProperty G
```

## EG617.case_I_cost_six

Source: EG617/Core/CostSixProfiles.lean

```lean
theorem case_I_cost_six (G : SimpleGraph V) (h : R23CaseIProfile G) :
    CostSixProperty G
```

## EG617.exceptional_cost_four

Source: EG617/Core/CostSixProfiles.lean

```lean
theorem exceptional_cost_four (G : SimpleGraph V) (h : R23ExceptionalProfile G)
    (I : Finset V) (hI : G.IsIndepSet (I : Set V)) :
    ∃ T : Finset V, T.card = 12 ∧ coreInducedEdgeCount G T + (T ∩ I).card ≤ 4
```

## EG617.exceptional_cost_six

Source: EG617/Core/CostSixProfiles.lean

```lean
theorem exceptional_cost_six (G : SimpleGraph V) (h : R23ExceptionalProfile G) :
    CostSixProperty G
```

## EG617.seed_private_nonadj_other_seed

Source: EG617/Core/E286Blocker.lean

```lean
theorem seed_private_nonadj_other_seed (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s t x : V) (hs : s ∈ I) (ht : t ∈ I)
    (hts : t ≠ s) (hx : x ∈ seedPrivateClique G I s) : ¬ G.Adj x t
```

## EG617.seed_private_mem_seed

Source: EG617/Core/E286Blocker.lean

```lean
theorem seed_private_mem_seed (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s x : V)
    (hx : x ∈ seedPrivateClique G I s) (hxI : x ∈ I) : x = s
```

## EG617.e286_pair_blocker_complete

Source: EG617/Core/E286Blocker.lean

```lean
theorem e286_pair_blocker_complete (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (i j z : V) (hi : i ∈ I) (hj : j ∈ I) (hij : i ≠ j)
    (hz : seedNeighbors G I z = {i, j})
    (x y : V) (hx : x ∈ seedPrivateClique G I i)
    (hy : y ∈ seedPrivateClique G I j) (hzx : ¬ G.Adj z x) (hzy : ¬ G.Adj z y) :
    G.Adj x y
```

## EG617.e286_subset_excess_budget

Source: EG617/Core/E286Blocker.lean

```lean
theorem e286_subset_excess_budget (G : SimpleGraph V) (hG : E286Hypotheses G)
    (S : Finset V) : (∑ v ∈ S, degreeExcess12 G v) ≤ 8
```

## EG617.e286_induced_degree_budget

Source: EG617/Core/E286Capacity.lean

```lean
theorem e286_induced_degree_budget (G : SimpleGraph V) (hG : E286Hypotheses G)
    (S : Finset V) :
    2 * coreInducedEdgeCount G S ≤ 12 * S.card + 8
```

## EG617.oddCycleBound_25

Source: EG617/Core/E286Capacity.lean

```lean
theorem oddCycleBound_25 (k : ℕ) (hk : 2 ≤ k) (hfit : 2 * k + 1 ≤ 25) :
    oddCycleBound 25 k ≤ 145
```

## EG617.alpha_two_25_edges_ge_155

Source: EG617/Core/E286Capacity.lean

```lean
theorem alpha_two_25_edges_ge_155 (G : SimpleGraph V)
    (hV : Fintype.card V = 25) (hI : CoreIndependenceBound 2 G)
    (hK : CoreCliqueBound 11 G) : 155 ≤ G.edgeFinset.card
```

## EG617.e286_no_induced_alpha_two_25

Source: EG617/Core/E286Capacity.lean

```lean
theorem e286_no_induced_alpha_two_25 (G : SimpleGraph V) (hG : E286Hypotheses G)
    (S : Finset V) (hS : S.card = 25)
    (hI : CoreIndependenceBound 2 (G.induce (S : Set V))) : False
```

## EG617.independenceBound_common_nonNeighbors

Source: EG617/Core/E286Capacity.lean

```lean
theorem independenceBound_common_nonNeighbors (G : SimpleGraph V) (a : ℕ)
    (hG : CoreIndependenceBound (a + 2) G) (x y : V) (hxy : x ≠ y)
    (hnxy : ¬ G.Adj x y) (S : Finset V)
    (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    CoreIndependenceBound a (G.induce (S : Set V))
```

## EG617.e286_common_antineighborhood_card_le_24

Source: EG617/Core/E286Capacity.lean

```lean
theorem e286_common_antineighborhood_card_le_24 (G : SimpleGraph V)
    (hG : E286Hypotheses G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y)
    (S : Finset V)
    (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    S.card ≤ 24
```

## EG617.e286_two_disjoint_neighbor_sets

Source: EG617/Core/E286Charges.lean

```lean
theorem e286_two_disjoint_neighbor_sets (G : SimpleGraph V) (v : V) (A B : Finset V)
    (hd : Disjoint A B) (ha : ∀ x ∈ A, G.Adj v x) (hb : ∀ x ∈ B, G.Adj v x) :
    A.card + B.card ≤ G.degree v
```

## EG617.e286_clique_blocker_vertex_charge

Source: EG617/Core/E286Charges.lean

```lean
theorem e286_clique_blocker_vertex_charge (G : SimpleGraph V)
    (K B : Finset V) (hK : G.IsClique (K : Set V)) (hd : Disjoint K B)
    (x : V) (hx : x ∈ K) (hB : ∀ y ∈ B, G.Adj x y) :
    K.card + B.card ≤ 13 + degreeExcess12 G x
```

## EG617.e286_pair_point_degree_charge

Source: EG617/Core/E286Charges.lean

```lean
theorem e286_pair_point_degree_charge (G : SimpleGraph V) (K L : Finset V)
    (hd : Disjoint K L) (z : V) :
    K.card + L.card ≤ 12 + degreeExcess12 G z +
      (K.filter (fun v => ¬ G.Adj z v)).card +
      (L.filter (fun v => ¬ G.Adj z v)).card
```

## EG617.e286_f11_minimum

Source: EG617/Core/E286Charges.lean

```lean
theorem e286_f11_minimum (a b : ℕ) (ha : 1 ≤ a) (hb : 1 ≤ b)
    (ha' : a ≤ 11) (hb' : b ≤ 11) :
    6 ≤ (10 - a - b) + a * (b - 2) + b * (a - 2)
```

## EG617.e286_k11_pair_local_charge

Source: EG617/Core/E286Charges.lean

```lean
theorem e286_k11_pair_local_charge (G : SimpleGraph V) (K L : Finset V)
    (hK : G.IsClique (K : Set V)) (hL : G.IsClique (L : Set V))
    (hcK : K.card = 11) (hcL : L.card = 11) (hd : Disjoint K L)
    (z : V) (hzK : z ∉ K) (hzL : z ∉ L)
    (ha : (K.filter (fun v => ¬ G.Adj z v)).Nonempty)
    (hb : (L.filter (fun v => ¬ G.Adj z v)).Nonempty)
    (he : ∀ x ∈ K, ¬ G.Adj z x → ∀ y ∈ L, ¬ G.Adj z y → G.Adj x y) :
    6 ≤ ∑ v ∈ insert z ((K.filter (fun v => ¬ G.Adj z v)) ∪
      (L.filter (fun v => ¬ G.Adj z v))), degreeExcess12 G v
```

## EG617.e286_common_neighbors_excess_bound

Source: EG617/Core/E286CommonNeighbors.lean

```lean
theorem e286_common_neighbors_excess_bound (G : SimpleGraph V)
    (hG : E286Hypotheses G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y) :
    (G.neighborFinset x ∩ G.neighborFinset y).card ≤
      3 + degreeExcess12 G x + degreeExcess12 G y
```

## EG617.e286_pair_excess_le_eight

Source: EG617/Core/E286CommonNeighbors.lean

```lean
theorem e286_pair_excess_le_eight (G : SimpleGraph V) (hG : E286Hypotheses G)
    (x y : V) (hxy : x ≠ y) :
    degreeExcess12 G x + degreeExcess12 G y ≤ 8
```

## EG617.e286_common_neighbors_le_eleven

Source: EG617/Core/E286CommonNeighbors.lean

```lean
theorem e286_common_neighbors_le_eleven (G : SimpleGraph V)
    (hG : E286Hypotheses G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y) :
    (G.neighborFinset x ∩ G.neighborFinset y).card ≤ 11
```

## EG617.e286_common_set_excess_charge

Source: EG617/Core/E286CommonNeighbors.lean

```lean
theorem e286_common_set_excess_charge (G : SimpleGraph V)
    (hG : E286Hypotheses G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y)
    (K : Finset V) (hK : ∀ z ∈ K, G.Adj x z ∧ G.Adj y z) :
    K.card ≤ 3 + degreeExcess12 G x + degreeExcess12 G y
```

## EG617.e286_ten_clique_completers_excess

Source: EG617/Core/E286CommonNeighbors.lean

```lean
theorem e286_ten_clique_completers_excess (G : SimpleGraph V)
    (hG : E286Hypotheses G) (K : Finset V) (hcard : K.card = 10)
    (hcl : G.IsClique (K : Set V)) (x y : V) (hxy : x ≠ y)
    (hx : x ∉ K) (hy : y ∉ K)
    (hadj : ∀ z ∈ K, G.Adj x z ∧ G.Adj y z) :
    ¬ G.Adj x y ∧ 7 ≤ degreeExcess12 G x + degreeExcess12 G y
```

## EG617.e286_eleven_clique_missing_nonempty

Source: EG617/Core/E286DisjointPairs.lean

```lean
theorem e286_eleven_clique_missing_nonempty (G : SimpleGraph V)
    (hG : E286Hypotheses G) (K : Finset V) (hc : K.card = 11)
    (hK : G.IsClique (K : Set V)) (z : V) (hz : z ∉ K) :
    (K.filter (fun x => ¬ G.Adj z x)).Nonempty
```

## EG617.e286_pair_support_mem_multiple

Source: EG617/Core/E286DisjointPairs.lean

```lean
theorem e286_pair_support_mem_multiple (G : SimpleGraph V) (I : Finset V)
    (i j z : V) (hij : i ≠ j) (hz : seedNeighbors G I z = {i, j}) :
    z ∈ seedMultipleSet G I
```

## EG617.e286_private_k11_pair_charge

Source: EG617/Core/E286DisjointPairs.lean

```lean
theorem e286_private_k11_pair_charge (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (i j z : V) (hi : i ∈ I) (hj : j ∈ I) (hij : i ≠ j)
    (hz : seedNeighbors G I z = {i, j})
    (hci : (seedPrivateClique G I i).card = 11)
    (hcj : (seedPrivateClique G I j).card = 11) :
    6 ≤ ∑ v ∈ insert z (seedPrivateClique G I i ∪ seedPrivateClique G I j),
      degreeExcess12 G v
```

## EG617.e286_complementary_k11_pairs_impossible

Source: EG617/Core/E286DisjointPairs.lean

```lean
theorem e286_complementary_k11_pairs_impossible (G : SimpleGraph V)
    (hG : E286Hypotheses G) (I : Finset V) (hc : I.card = 4)
    (hI : G.IsIndepSet (I : Set V)) (e : Fin 4 ≃ (I : Set V))
    (hK : ∀ s : Fin 4, (seedPrivateClique G I (e s)).card = 11)
    (z w : V) (hz : seedNeighbors G I z = {(e 0 : V), (e 1 : V)})
    (hw : seedNeighbors G I w = {(e 2 : V), (e 3 : V)}) : False
```

## EG617.E286Hypotheses

Source: EG617/Core/E286Excess.lean

```lean
def E286Hypotheses (G : SimpleGraph V) : Prop
```

## EG617.E286Statement

Source: EG617/Core/E286Excess.lean

```lean
def E286Statement : Prop
```

## EG617.degreeExcess12

Source: EG617/Core/E286Excess.lean

```lean
noncomputable def degreeExcess12 (G : SimpleGraph V) (v : V) : ℕ
```

## EG617.excessSupport

Source: EG617/Core/E286Excess.lean

```lean
noncomputable def excessSupport (G : SimpleGraph V) : Finset V
```

## EG617.e286_degree_sum

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_degree_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v : V, G.degree v = 572
```

## EG617.e286_excess_sum

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_excess_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v : V, degreeExcess12 G v = 8
```

## EG617.e286_support_sum

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_support_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v ∈ excessSupport G, degreeExcess12 G v = 8
```

## EG617.e286_support_card_le_eight

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_support_card_le_eight (G : SimpleGraph V) (hG : E286Hypotheses G) :
    (excessSupport G).card ≤ 8
```

## EG617.e286_degree_le_twenty

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_degree_le_twenty (G : SimpleGraph V) (hG : E286Hypotheses G) (v : V) :
    G.degree v ≤ 20
```

## EG617.e286_regular_complement

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_regular_complement (G : SimpleGraph V) (hG : E286Hypotheses G) :
    (excessSupport G)ᶜ = Finset.univ.filter (fun v => G.degree v = 12)
```

## EG617.e286_regular_card_ge_39

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_regular_card_ge_39 (G : SimpleGraph V) (hG : E286Hypotheses G) :
    39 ≤ (Finset.univ.filter (fun v => G.degree v = 12)).card
```

## EG617.e286_support_degree_sum

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_support_degree_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v ∈ excessSupport G, G.degree v = 12 * (excessSupport G).card + 8
```

## EG617.e286_regular_edge_ledger

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_regular_edge_ledger (G : SimpleGraph V) (hG : E286Hypotheses G) :
    coreInducedEdgeCount G (excessSupport G)ᶜ + 12 * (excessSupport G).card + 8 =
      286 + coreInducedEdgeCount G (excessSupport G)
```

## EG617.e286_support_type_injective

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem e286_support_type_injective : Function.Injective e286SupportType
```

## EG617.seedLabelNeighbors_relabel

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem seedLabelNeighbors_relabel (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (σ : Equiv.Perm (Fin 4)) (v : V) :
    seedLabelNeighbors G I (σ.symm.trans e) v =
      (seedLabelNeighbors G I e v).image σ
```

## EG617.e286_graph_support_counts_relabel

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem e286_graph_support_counts_relabel (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (σ : Equiv.Perm (Fin 4)) :
    e286GraphSupportCounts G I (σ.symm.trans e) =
      e286RelabelCounts σ (e286GraphSupportCounts G I e)
```

## EG617.e286_actual_oriented_support_orbit

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem e286_actual_oriented_support_orbit (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives
```

## EG617.e286_first_support_orbit_impossible

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem e286_first_support_orbit_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V))
    (hcounts : e286GraphSupportCounts G I e = [1,0,0,0,0,1,0,0,0,0,1]) : False
```

## EG617.e286_actual_support_nine_remaining

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem e286_actual_support_nine_remaining (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives.tail
```

## EG617.seedNeighbors

Source: EG617/Core/E286PrivateClasses.lean

```lean
noncomputable def seedNeighbors (G : SimpleGraph V) (I : Finset V) (v : V) : Finset V
```

## EG617.seedPrivateClique

Source: EG617/Core/E286PrivateClasses.lean

```lean
noncomputable def seedPrivateClique (G : SimpleGraph V) (I : Finset V) (s : V) : Finset V
```

## EG617.seedMultipleSet

Source: EG617/Core/E286PrivateClasses.lean

```lean
noncomputable def seedMultipleSet (G : SimpleGraph V) (I : Finset V) : Finset V
```

## EG617.seedNeighbors_empty_of_seed

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem seedNeighbors_empty_of_seed (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s : V) (hs : s ∈ I) :
    seedNeighbors G I s = ∅
```

## EG617.seedNeighbors_singleton_outside

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem seedNeighbors_singleton_outside (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s v : V)
    (hv : seedNeighbors G I v = {s}) : v ∉ I
```

## EG617.seedNeighbors_singleton_nonadj

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem seedNeighbors_singleton_nonadj (G : SimpleGraph V) (I : Finset V)
    (s v : V) (hv : seedNeighbors G I v = {s}) (t : V) (ht : t ∈ I)
    (hts : t ≠ s) : ¬ G.Adj v t
```

## EG617.e286_private_class_isClique

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem e286_private_class_isClique (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (s : V) (hs : s ∈ I) :
    G.IsClique (seedPrivateClique G I s : Set V)
```

## EG617.e286_seed_dominates

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem e286_seed_dominates (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (v : V) (hv : v ∉ I) : (seedNeighbors G I v).Nonempty
```

## EG617.e286_private_multiple_card

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem e286_private_multiple_card (G : SimpleGraph V)
    (I : Finset V) (hI : G.IsIndepSet (I : Set V)) (s : V) (hs : s ∈ I)
    (hdeg : G.degree s = 12) :
    (seedPrivateClique G I s).card +
      ((seedMultipleSet G I).filter (G.Adj s)).card = 13
```

## EG617.e286_seed_incidence_sum

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem e286_seed_incidence_sum (G : SimpleGraph V) (I : Finset V)
    (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hdeg : ∀ s ∈ I, G.degree s = 12) :
    ∑ v ∈ Iᶜ, (seedNeighbors G I v).card = 48
```

## EG617.e286_seed_surplus_five

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem e286_seed_surplus_five (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hdeg : ∀ s ∈ I, G.degree s = 12) :
    ∑ v ∈ seedMultipleSet G I, ((seedNeighbors G I v).card - 1) = 5
```

## EG617.e286_seed_support_counts

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem e286_seed_support_counts (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hdeg : ∀ s ∈ I, G.degree s = 12) :
    3 ≤ (seedMultipleSet G I).card ∧ (seedMultipleSet G I).card ≤ 5 ∧
    (∑ s ∈ I, (seedPrivateClique G I s).card) + (seedMultipleSet G I).card = 47
```

## EG617.e286_seed_classes_cover

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem e286_seed_classes_cover (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V)) (v : V) :
    v ∈ seedMultipleSet G I ∨ ∃ s ∈ I, v ∈ seedPrivateClique G I s
```

## EG617.seed_private_classes_disjoint

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem seed_private_classes_disjoint (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s t : V) (hs : s ∈ I) (ht : t ∈ I)
    (hst : s ≠ t) : Disjoint (seedPrivateClique G I s) (seedPrivateClique G I t)
```

## EG617.seed_private_multiple_disjoint

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem seed_private_multiple_disjoint (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s : V) (hs : s ∈ I) :
    Disjoint (seedPrivateClique G I s) (seedMultipleSet G I)
```

## EG617.e286_seed_support_reduction

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem e286_seed_support_reduction (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ s ∈ I, G.degree s = 12) ∧
      3 ≤ (seedMultipleSet G I).card ∧ (seedMultipleSet G I).card ≤ 5 ∧
      (∑ v ∈ seedMultipleSet G I, ((seedNeighbors G I v).card - 1)) = 5 ∧
      (∑ s ∈ I, (seedPrivateClique G I s).card) + (seedMultipleSet G I).card = 47 ∧
      (∀ s ∈ I, G.IsClique (seedPrivateClique G I s : Set V) ∧
        (seedPrivateClique G I s).card ≤ 11 ∧
        (seedPrivateClique G I s).card + ((seedMultipleSet G I).filter (G.Adj s)).card = 13) ∧
      (∀ v, v ∈ seedMultipleSet G I ∨ ∃ s ∈ I, v ∈ seedPrivateClique G I s) ∧
      (∀ s ∈ I, ∀ t ∈ I, s ≠ t →
        Disjoint (seedPrivateClique G I s) (seedPrivateClique G I t)) ∧
      (∀ s ∈ I, Disjoint (seedPrivateClique G I s) (seedMultipleSet G I)) ∧
      ∀ v ∈ seedMultipleSet G I, 2 ≤ (seedNeighbors G I v).card ∧
        (seedNeighbors G I v).card ≤ 4
```

## EG617.e286_exists_regular_independent_four

Source: EG617/Core/E286Seeds.lean

```lean
theorem e286_exists_regular_independent_four (G : SimpleGraph V)
    (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      ∀ v ∈ I, G.degree v = 12
```

## EG617.e286SupportType

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286SupportType (i : Fin 11) : Finset (Fin 4)
```

## EG617.e286SupportWeights

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286SupportWeights : List ℕ
```

## EG617.e286_support_type_complete

Source: EG617/Core/E286SupportCounts.lean

```lean
theorem e286_support_type_complete (S : Finset (Fin 4)) (hS : 2 ≤ S.card) :
    ∃! i : Fin 11, e286SupportType i = S
```

## EG617.e286_support_type_weight

Source: EG617/Core/E286SupportCounts.lean

```lean
theorem e286_support_type_weight (i : Fin 11) :
    (e286SupportType i).card - 1 = e286SupportWeights[i.val]!
```

## EG617.e286WeightedSum

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286WeightedSum : List ℕ → List ℕ → ℕ
  | w :: ws, x :: xs => w * x + e286WeightedSum ws xs
  | _, _ => 0

/-- All nonnegative count vectors with prescribed weighted surplus.
The bound on each first coordinate is proved in the completeness theorem. -/
def e286WeightedProfiles : List ℕ → ℕ → List (List ℕ)
  | [], b => if b = 0 then [[]] else []
  | w :: ws, b => (List.range (b + 1)).flatMap fun x =>
      if w * x ≤ b then (e286WeightedProfiles ws (b - w * x)).map (x :: ·) else []

theorem e286_weighted_profiles_complete (ws xs : List ℕ) (b : ℕ)
    (hpos : ∀ w ∈ ws, 1 ≤ w) (hlen : xs.length = ws.length)
    (hsum : e286WeightedSum ws xs = b) :
    xs ∈ e286WeightedProfiles ws b
```

## EG617.e286WeightedProfiles

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286WeightedProfiles : List ℕ → ℕ → List (List ℕ)
  | [], b => if b = 0 then [[]] else []
  | w :: ws, b => (List.range (b + 1)).flatMap fun x =>
      if w * x ≤ b then (e286WeightedProfiles ws (b - w * x)).map (x :: ·) else []

theorem e286_weighted_profiles_complete (ws xs : List ℕ) (b : ℕ)
    (hpos : ∀ w ∈ ws, 1 ≤ w) (hlen : xs.length = ws.length)
    (hsum : e286WeightedSum ws xs = b) :
    xs ∈ e286WeightedProfiles ws b
```

## EG617.e286_weighted_profiles_complete

Source: EG617/Core/E286SupportCounts.lean

```lean
theorem e286_weighted_profiles_complete (ws xs : List ℕ) (b : ℕ)
    (hpos : ∀ w ∈ ws, 1 ≤ w) (hlen : xs.length = ws.length)
    (hsum : e286WeightedSum ws xs = b) :
    xs ∈ e286WeightedProfiles ws b
```

## EG617.e286CountIncidence

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286CountIncidence (xs : List ℕ) (s : Fin 4) : ℕ
```

## EG617.e286RelabelCounts

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286RelabelCounts (σ : Equiv.Perm (Fin 4)) (xs : List ℕ) : List ℕ
```

## EG617.e286SupportOrbitRepresentatives

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286SupportOrbitRepresentatives : List (List ℕ)
```

## EG617.e286_finite_support_orbit_check

Source: EG617/Core/E286SupportCounts.lean

```lean
theorem e286_finite_support_orbit_check :
    ∀ xs ∈ e286WeightedProfiles e286SupportWeights 5,
      (∀ s : Fin 4, 2 ≤ e286CountIncidence xs s) →
      ∃ σ : Equiv.Perm (Fin 4),
        e286RelabelCounts σ xs ∈ e286SupportOrbitRepresentatives
```

## EG617.e286_support_counts_complete

Source: EG617/Core/E286SupportCounts.lean

```lean
theorem e286_support_counts_complete (xs : List ℕ)
    (hlen : xs.length = 11) (hsum : e286WeightedSum e286SupportWeights xs = 5)
    (hinc : ∀ s : Fin 4, 2 ≤ e286CountIncidence xs s) :
    ∃ σ : Equiv.Perm (Fin 4),
      e286RelabelCounts σ xs ∈ e286SupportOrbitRepresentatives
```

## EG617.seedLabelNeighbors

Source: EG617/Core/E286SupportLift.lean

```lean
noncomputable def seedLabelNeighbors (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : V) : Finset (Fin 4)
```

## EG617.seedLabelNeighbors_image

Source: EG617/Core/E286SupportLift.lean

```lean
theorem seedLabelNeighbors_image (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : V) :
    (seedLabelNeighbors G I e v).image (fun i => (e i : V)) = seedNeighbors G I v
```

## EG617.seedLabelNeighbors_card

Source: EG617/Core/E286SupportLift.lean

```lean
theorem seedLabelNeighbors_card (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : V) :
    (seedLabelNeighbors G I e v).card = (seedNeighbors G I v).card
```

## EG617.e286_seed_support_code_exists

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_seed_support_code_exists (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : (seedMultipleSet G I : Set V)) :
    ∃ i : Fin 11, e286SupportType i = seedLabelNeighbors G I e v
```

## EG617.e286SeedSupportCode

Source: EG617/Core/E286SupportLift.lean

```lean
noncomputable def e286SeedSupportCode (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : (seedMultipleSet G I : Set V)) : Fin 11
```

## EG617.e286_seed_support_code_spec

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_seed_support_code_spec (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : (seedMultipleSet G I : Set V)) :
    e286SupportType (e286SeedSupportCode G I e v) = seedLabelNeighbors G I e v
```

## EG617.e286GraphSupportCounts

Source: EG617/Core/E286SupportLift.lean

```lean
noncomputable def e286GraphSupportCounts (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) : List ℕ
```

## EG617.e286_ofFn_get

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_ofFn_get (f : Fin 11 → ℕ) (i : Fin 11) :
    (List.ofFn f)[i.val]! = f i
```

## EG617.e286_weightedSum_ofFn

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_weightedSum_ofFn (f : Fin 11 → ℕ) :
    e286WeightedSum e286SupportWeights (List.ofFn f) =
      ∑ i : Fin 11, ((e286SupportType i).card - 1) * f i
```

## EG617.e286_weighted_fiber_count

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_weighted_fiber_count {W : Type u} [Fintype W]
    (code : W → Fin 11) (w : Fin 11 → ℕ) :
    (∑ i : Fin 11, w i * (Finset.univ.filter (fun v => code v = i)).card) =
      ∑ v : W, w (code v)
```

## EG617.e286_graph_support_weighted_sum

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_graph_support_weighted_sum (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hi : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V)) :
    e286WeightedSum e286SupportWeights (e286GraphSupportCounts G I e) = 5
```

## EG617.e286_graph_support_incidence

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_graph_support_incidence (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (s : Fin 4) :
    e286CountIncidence (e286GraphSupportCounts G I e) s =
      ((seedMultipleSet G I).filter (G.Adj (e s))).card
```

## EG617.e286_actual_support_orbit

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_actual_support_orbit (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧
      ∃ e : Fin 4 ≃ (I : Set V), ∃ σ : Equiv.Perm (Fin 4),
        e286RelabelCounts σ (e286GraphSupportCounts G I e) ∈
          e286SupportOrbitRepresentatives
```

## EG617.e286_independent_three_forces_edge

Source: EG617/Core/E286Triple.lean

```lean
theorem e286_independent_three_forces_edge (G : SimpleGraph V) (hG : E286Hypotheses G)
    (J : Finset V) (hc : J.card = 3) (hJ : G.IsIndepSet (J : Set V))
    (x y : V) (hxy : x ≠ y) (hx : x ∉ J) (hy : y ∉ J)
    (hxJ : ∀ t ∈ J, ¬ G.Adj x t) (hyJ : ∀ t ∈ J, ¬ G.Adj y t) : G.Adj x y
```

## EG617.e286_ordered_three_cliques_obstruction

Source: EG617/Core/E286Triple.lean

```lean
theorem e286_ordered_three_cliques_obstruction (G : SimpleGraph V) (hG : E286Hypotheses G)
    (K L M : Finset V) (hK : G.IsClique (K : Set V))
    (hL : G.IsClique (L : Set V)) (hM : G.IsClique (M : Set V))
    (hcK : K.card = 11) (hcL : L.card = 11) (hcM : M.card = 11)
    (hKL : Disjoint K L) (hKM : Disjoint K M) (hLM : Disjoint L M)
    (z s : V) (hzs : z ≠ s) (hnzs : ¬ G.Adj z s)
    (hzK : z ∉ K) (hzL : z ∉ L) (hzM : z ∉ M)
    (hsK : s ∉ K) (hsL : s ∉ L) (hsM : s ∉ M)
    (hanti : ∀ v ∈ K ∪ L ∪ M, ¬ G.Adj v s)
    (hbound : ∀ v ∈ K ∪ L ∪ M, degreeExcess12 G v ≤ 2)
    (hA : (K.filter (fun v => ¬ G.Adj z v)).Nonempty)
    (hB : 5 ≤ (L.filter (fun v => ¬ G.Adj z v)).card)
    (hC : 5 ≤ (M.filter (fun v => ¬ G.Adj z v)).card)
    (hBC : 13 ≤ (L.filter (fun v => ¬ G.Adj z v)).card +
      (M.filter (fun v => ¬ G.Adj z v)).card) : False
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

## EG617.core_R447_min_degree_eleven_edges_ge_287

Source: EG617/Core/Gate47.lean

```lean
theorem core_R447_min_degree_eleven_edges_ge_287 (G : SimpleGraph V)
    (hV : Fintype.card V = 47) (hG : CoreAdmissible 4 G) (v : V)
    (hd : G.degree v = 11) (hmin : ∀ w, 11 ≤ G.degree w) :
    287 ≤ G.edgeFinset.card
```

## EG617.gate47_verified

Source: EG617/Core/Gate47.lean

```lean
theorem gate47_verified : Gate47Statement
```

## EG617.core_admissible_common_nonNeighbors

Source: EG617/Core/GateRows.lean

```lean
theorem core_admissible_common_nonNeighbors (G : SimpleGraph V) (a : ℕ)
    (hG : CoreAdmissible (a + 2) G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y)
    (S : Finset V) (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    CoreAdmissible a (G.induce (S : Set V))
```

## EG617.core_R4_common_nonneighbors_card_le_23

Source: EG617/Core/GateRows.lean

```lean
theorem core_R4_common_nonneighbors_card_le_23 (G : SimpleGraph V)
    (hG : CoreAdmissible 4 G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y)
    (S : Finset V) (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    S.card ≤ 23
```

## EG617.core_R4_row_union_ge_twelve

Source: EG617/Core/GateRows.lean

```lean
theorem core_R4_row_union_ge_twelve (G : SimpleGraph V) (hG : CoreAdmissible 4 G)
    (C : Finset V) (hC : C.card = 35) (x y : V) (hxy : x ≠ y)
    (hnxy : ¬ G.Adj x y) (hx : x ∉ C) (hy : y ∉ C) :
    12 ≤ ((C.filter (G.Adj x)) ∪ (C.filter (G.Adj y))).card
```

## EG617.core_two_degrees_le_edges_add_one

Source: EG617/Core/GateRows.lean

```lean
theorem core_two_degrees_le_edges_add_one (G : SimpleGraph V) (x y : V) (hxy : x ≠ y) :
    G.degree x + G.degree y ≤ G.edgeFinset.card + 1
```

## EG617.core_shell_row_missing_degree_le

Source: EG617/Core/GateRows.lean

```lean
theorem core_shell_row_missing_degree_le (G : SimpleGraph V) (v : V)
    (hd : G.degree v = 11) (hmin : ∀ w, 11 ≤ G.degree w)
    (a : (G.neighborFinset v : Set V)) :
    ((G.induce (G.neighborFinset v : Set V))ᶜ).degree a ≤
      ((Gᶜ.neighborFinset v).filter (G.Adj a)).card
```

## EG617.core_missing_edge_row_sum

Source: EG617/Core/GateRows.lean

```lean
theorem core_missing_edge_row_sum (M : SimpleGraph V) (r : V → ℕ)
    (hrow : ∀ a, M.degree a ≤ r a) (a b : V) (hab : a ≠ b)
    (hpair : 12 ≤ r a + r b) :
    M.edgeFinset.card + 11 ≤ ∑ x : V, r x
```

## EG617.core_shell_edge_degree_ledger

Source: EG617/Core/GateShell.lean

```lean
theorem core_shell_edge_degree_ledger (G : SimpleGraph V) (v : V) :
    let S
```

## EG617.core_induced_edges_le_choose

Source: EG617/Core/GateShell.lean

```lean
theorem core_induced_edges_le_choose (G : SimpleGraph V) (S : Finset V) :
    coreInducedEdgeCount G S ≤ S.card.choose 2
```

## EG617.core_R447_min_degree_ten_edges_ge_289

Source: EG617/Core/GateShell.lean

```lean
theorem core_R447_min_degree_ten_edges_ge_289 (G : SimpleGraph V)
    (hV : Fintype.card V = 47) (hG : CoreAdmissible 4 G) (v : V)
    (hd : G.degree v = 10) (hmin : ∀ w, 10 ≤ G.degree w) :
    289 ≤ G.edgeFinset.card
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

## EG617.two_cycle_neighbors_cross_card_le_nine

Source: EG617/Core/R23BalancedExterior.lean

```lean
theorem two_cycle_neighbors_cross_card_le_nine (G : SimpleGraph V)
    (ht : G.CliqueFree 3) (hI : CoreIndependenceBound 11 G)
    (S B : Finset V) (v : V) (hd : (S.filter (G.Adj v)).card = 2)
    (hB : B ⊆ Sᶜ) (hedges : ∀ b ∈ B, G.Adj v b) : B.card ≤ 9
```

## EG617.r23_exists_balanced_exterior

Source: EG617/Core/R23BalancedExterior.lean

```lean
theorem r23_exists_balanced_exterior (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G),
      Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
      ∃ A : Finset ((Sᶜ : Finset V) : Set V),
        let H
```

## EG617.c5_remaining_fiber_sum

Source: EG617/Core/R23CaseI.lean

```lean
theorem c5_remaining_fiber_sum (n : Fin 5 → ℕ) (a : Fin 5)
    (hs : ∑ i, n i = 23) (ha : n a = 10)
    (hplus : n (a + 2) = 1) (hminus : n (a - 2) = 1) :
    n (a + 1) + n (a - 1) = 11
```

## EG617.R23CaseIProfile

Source: EG617/Core/R23CaseI.lean

```lean
def R23CaseIProfile (G : SimpleGraph V) : Prop
```

## EG617.r23_122_case_I

Source: EG617/Core/R23CaseI.lean

```lean
theorem r23_122_case_I (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 122) :
    R23CaseIProfile G
```

## EG617.R23OneEdgeCompletion

Source: EG617/Core/R23CaseII.lean

```lean
def R23OneEdgeCompletion (G : SimpleGraph V) : Prop
```

## EG617.singleton_partition_completes_to_case_I

Source: EG617/Core/R23CaseII.lean

```lean
theorem singleton_partition_completes_to_case_I (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 121)
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (S A B : Finset V)
    (hS : Finset.univ.image f = S) (hcover : A ∪ B = Sᶜ)
    (hA : G.IsIndepSet (A : Set V)) (hB : G.IsIndepSet (B : Set V))
    (hAc : A.card = 9) (hBc : B.card = 9)
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y)
    (hd : ∃ u ∈ Sᶜ, (S.filter (G.Adj u)).card = 1 ∧
      ∀ x ∈ Sᶜ, x ≠ u → (S.filter (G.Adj x)).card = 2) :
    R23OneEdgeCompletion G
```

## EG617.R23MissingEdgeExterior

Source: EG617/Core/R23CaseII.lean

```lean
def R23MissingEdgeExterior (G : SimpleGraph V) : Prop
```

## EG617.r23_121_completion_or_missing_exterior

Source: EG617/Core/R23CaseII.lean

```lean
theorem r23_121_completion_or_missing_exterior (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 121) :
    R23OneEdgeCompletion G ∨ R23MissingEdgeExterior G
```

## EG617.R23ExceptionalProfile

Source: EG617/Core/R23Classification.lean

```lean
def R23ExceptionalProfile (G : SimpleGraph V) : Prop
```

## EG617.missing_exterior_completion_or_exceptional

Source: EG617/Core/R23Classification.lean

```lean
theorem missing_exterior_completion_or_exceptional (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 121)
    (hm : R23MissingEdgeExterior G) :
    R23OneEdgeCompletion G ∨ R23ExceptionalProfile G
```

## EG617.r23_complete_classification

Source: EG617/Core/R23Classification.lean

```lean
theorem r23_complete_classification (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    R23CaseIProfile G ∨ R23OneEdgeCompletion G ∨ R23ExceptionalProfile G
```

## EG617.r23_122_complete_type_data

Source: EG617/Core/R23CompleteExterior.lean

```lean
theorem r23_122_complete_type_data (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 122) :
    ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G)
      (t : V → Fin 5) (P Q : Finset V),
      Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
      (∀ x, cycleNeighborLabels f x = c5Type (t x)) ∧
      (∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y)) ∧
      P ∪ Q = Sᶜ ∧ P.card = 9 ∧ Q.card = 9 ∧
      (∀ x ∈ P, ∀ y ∈ Q, G.Adj x y)
```

## EG617.r23_122_type_presentation

Source: EG617/Core/R23CompleteExterior.lean

```lean
theorem r23_122_type_presentation (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 122) :
    ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G)
      (t : V → Fin 5), Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
      (∀ x, cycleNeighborLabels f x = c5Type (t x)) ∧
      ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y)
```

## EG617.triangleFree_sup_edge_of_no_common_neighbor

Source: EG617/Core/R23EdgeCompletion.lean

```lean
theorem triangleFree_sup_edge_of_no_common_neighbor (G : SimpleGraph V)
    (ht : G.CliqueFree 3) (u v : V) (hne : u ≠ v)
    (hcommon : ∀ w, G.Adj u w → ¬ G.Adj v w) :
    (G ⊔ SimpleGraph.edge u v).CliqueFree 3
```

## EG617.r23_one_edge_completion_case_I

Source: EG617/Core/R23EdgeCompletion.lean

```lean
theorem r23_one_edge_completion_case_I (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 121)
    (u v : V) (hne : u ≠ v) (hn : ¬ G.Adj u v)
    (hcommon : ∀ w, G.Adj u w → ¬ G.Adj v w) :
    let H
```

## EG617.deficit_sum_add

Source: EG617/Core/R23ExactLedger.lean

```lean
theorem deficit_sum_add (T : Finset V) (d : V → ℕ) (hd : ∀ v ∈ T, d v ≤ 2) :
    (∑ v ∈ T, (2 - d v)) + (∑ v ∈ T, d v) = 2 * T.card
```

## EG617.deficit_zero_iff

Source: EG617/Core/R23ExactLedger.lean

```lean
theorem deficit_zero_iff (T : Finset V) (d : V → ℕ) (hd : ∀ v ∈ T, d v ≤ 2) :
    (∑ v ∈ T, (2 - d v)) = 0 ↔ ∀ v ∈ T, d v = 2
```

## EG617.deficit_one_distribution

Source: EG617/Core/R23ExactLedger.lean

```lean
theorem deficit_one_distribution (T : Finset V) (d : V → ℕ)
    (hd : ∀ v ∈ T, d v ≤ 2) (h : (∑ v ∈ T, (2 - d v)) = 1) :
    ∃ v ∈ T, d v = 1 ∧ ∀ w ∈ T, w ≠ v → d w = 2
```

## EG617.ExactC5NeighborLedger

Source: EG617/Core/R23ExactLedger.lean

```lean
def ExactC5NeighborLedger (G : SimpleGraph V) (S : Finset V) : Prop
```

## EG617.r23_exact_neighbor_ledger

Source: EG617/Core/R23ExactLedger.lean

```lean
theorem r23_exact_neighbor_ledger (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ v, ∃ p : G.Walk v v, IsShortestOddLoop p ∧ p.IsCycle ∧ p.length = 5 ∧
      ExactC5NeighborLedger G p.support.toFinset
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

## EG617.five_cycle_copy_same_support

Source: EG617/Core/R23TypeLift.lean

```lean
theorem five_cycle_copy_same_support {v : V} (p : G.Walk v v)
    (hc : p.IsCycle) (h5 : p.length = 5) :
    ∃ f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G,
      Finset.univ.image f = p.support.toFinset
```

## EG617.cycleNeighborLabels_card_eq

Source: EG617/Core/R23TypeLift.lean

```lean
theorem cycleNeighborLabels_card_eq
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (S : Finset V)
    (hS : Finset.univ.image f = S) (x : V) :
    (cycleNeighborLabels f x).card = (S.filter (G.Adj x)).card
```

## EG617.r23_exact_labeled_neighbor_ledger

Source: EG617/Core/R23TypeLift.lean

```lean
theorem r23_exact_labeled_neighbor_ledger (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G),
      Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
      (∀ x, (cycleNeighborLabels f x).card = (S.filter (G.Adj x)).card) ∧
      (∀ x ∈ Sᶜ, (S.filter (G.Adj x)).card = 2 →
        ∃! i : Fin 5, cycleNeighborLabels f x = c5Type i)
```

## EG617.core_degree_eleven_neighbor_nonedge

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_degree_eleven_neighbor_nonedge (G : SimpleGraph V)
    (hG : CoreCliqueBound 11 G) (v : V) (hd : G.degree v = 11) :
    ∃ x ∈ G.neighborFinset v, ∃ y ∈ G.neighborFinset v, x ≠ y ∧ ¬ G.Adj x y
```

## EG617.core_common_nonneighbors_clique

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_common_nonneighbors_clique (G : SimpleGraph V)
    (hG : CoreIndependenceBound 3 G) (x y : V) (hxy : x ≠ y) (hnot : ¬ G.Adj x y)
    (S : Finset V) (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    G.IsClique (S : Set V)
```

## EG617.core_edge_count_union

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_edge_count_union (G : SimpleGraph V) (S T : Finset V) (hd : Disjoint S T) :
    coreInducedEdgeCount G (S ∪ T) = coreInducedEdgeCount G S +
      adjCount G S T + coreInducedEdgeCount G T
```

## EG617.core_pair_cross_lower_bound

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_pair_cross_lower_bound (G : SimpleGraph V) (T : Finset V)
    (x y : V) (hxy : x ≠ y) :
    T.card ≤ adjCount G T {x, y} + (T.filter (fun z => ¬ G.Adj x z ∧ ¬ G.Adj y z)).card
```

## EG617.core_induce_compl

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_induce_compl (G : SimpleGraph V) (T : Finset V) :
    (G.induce (T : Set V))ᶜ = Gᶜ.induce (T : Set V)
```

## EG617.core_induced_compl_edge_count

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_induced_compl_edge_count (G : SimpleGraph V) (T : Finset V) :
    coreInducedEdgeCount G T + coreInducedEdgeCount Gᶜ T = T.card.choose 2
```

## EG617.core_fourteen_cost_obstruction

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_fourteen_cost_obstruction (G : SimpleGraph V)
    (hcap : ∀ U : Finset V, coreInducedEdgeCount G U ≤ D U.card)
    (T : Finset V) (hT : T.card = 12) (x y : V) (hxy : x ≠ y)
    (hx : x ∉ T) (hy : y ∉ T)
    (hcost : coreInducedEdgeCount Gᶜ T +
      (T.filter (fun z => ¬ G.Adj x z ∧ ¬ G.Adj y z)).card ≤ 6) : False
```

## EG617.core_R223_complement_cost_six

Source: EG617/Core/R335Neighborhood.lean

```lean
theorem core_R223_complement_cost_six (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (hG : CoreAdmissible 2 G) :
    CostSixProperty Gᶜ
```

## EG617.core_R335_degree_eleven_nonneighbor_cost_six

Source: EG617/Core/R335Neighborhood.lean

```lean
theorem core_R335_degree_eleven_nonneighbor_cost_six (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G)
    (v : V) (hd : G.degree v = 11) :
    let S
```

## EG617.core_R335_degree_ne_eleven

Source: EG617/Core/R335Sharp.lean

```lean
theorem core_R335_degree_ne_eleven (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G) (v : V) :
    G.degree v ≠ 11
```

## EG617.core_R335_degree_ge_twelve

Source: EG617/Core/R335Sharp.lean

```lean
theorem core_R335_degree_ge_twelve (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G) (v : V) :
    12 ≤ G.degree v
```

## EG617.core_R335_edges_ge_210

Source: EG617/Core/R335Sharp.lean

```lean
theorem core_R335_edges_ge_210 (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G) :
    210 ≤ G.edgeFinset.card
```

## EG617.core_R336_degree_ge_thirteen

Source: EG617/Core/R336Sharp.lean

```lean
theorem core_R336_degree_ge_thirteen (G : SimpleGraph V)
    (hV : Fintype.card V = 36) (hG : CoreAdmissible 3 G) (v : V) :
    13 ≤ G.degree v
```

## EG617.core_R336_edges_ge_234

Source: EG617/Core/R336Sharp.lean

```lean
theorem core_R336_edges_ge_234 (G : SimpleGraph V)
    (hV : Fintype.card V = 36) (hG : CoreAdmissible 3 G) :
    234 ≤ G.edgeFinset.card
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

