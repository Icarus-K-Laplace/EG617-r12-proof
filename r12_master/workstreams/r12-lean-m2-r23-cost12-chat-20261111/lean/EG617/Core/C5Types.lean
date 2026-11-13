module

public import EG617.Core.BipartiteExterior

@[expose] public section
set_option autoImplicit false

namespace EG617

/-- Exact two-neighbor labels relative to a labeled five-cycle. -/
def c5Type (i : Fin 5) : Finset (Fin 5) := {i - 1, i + 1}

theorem c5Type_card (i : Fin 5) : (c5Type i).card = 2 := by
  exact (by decide : ∀ j : Fin 5, (c5Type j).card = 2) i

theorem c5Type_disjoint_iff (i j : Fin 5) :
    Disjoint (c5Type i) (c5Type j) ↔ (SimpleGraph.cycleGraph 5).Adj i j := by
  exact (by decide : ∀ a b : Fin 5,
    Disjoint (c5Type a) (c5Type b) ↔ (SimpleGraph.cycleGraph 5).Adj a b) i j

theorem c5_adj_iff_mem_type (i j : Fin 5) :
    (SimpleGraph.cycleGraph 5).Adj i j ↔ i ∈ c5Type j := by
  exact (by decide : ∀ a b : Fin 5,
    (SimpleGraph.cycleGraph 5).Adj a b ↔ a ∈ c5Type b) i j

set_option maxRecDepth 100000 in
set_option maxHeartbeats 2000000 in
theorem c5_independent_pair_unique_type (S : Finset (Fin 5))
    (hcard : S.card = 2)
    (hI : ∀ i ∈ S, ∀ j ∈ S, ¬ (SimpleGraph.cycleGraph 5).Adj i j) :
    ∃! i : Fin 5, S = c5Type i := by
  exact (by decide : ∀ T : Finset (Fin 5), T.card = 2 →
    (∀ a ∈ T, ∀ b ∈ T, ¬ (SimpleGraph.cycleGraph 5).Adj a b) →
    ∃! i : Fin 5, T = c5Type i) S hcard hI

theorem c5_common_neighbors_unique (i j k l : Fin 5) (hne : i ≠ j)
    (hik : (SimpleGraph.cycleGraph 5).Adj i k)
    (hjk : (SimpleGraph.cycleGraph 5).Adj j k)
    (hil : (SimpleGraph.cycleGraph 5).Adj i l)
    (hjl : (SimpleGraph.cycleGraph 5).Adj j l) : k = l := by
  exact (by decide : ∀ a b c d : Fin 5, a ≠ b →
    (SimpleGraph.cycleGraph 5).Adj a c → (SimpleGraph.cycleGraph 5).Adj b c →
    (SimpleGraph.cycleGraph 5).Adj a d → (SimpleGraph.cycleGraph 5).Adj b d → c = d)
    i j k l hne hik hjk hil hjl

/-- General structural proof: a complete cross-compatible pair of nonempty
type sets has a singleton side. No list of representatives is assumed. -/
theorem c5_complete_type_sets (A B : Finset (Fin 5))
    (hA : A.Nonempty) (hB : B.Nonempty)
    (hcross : ∀ i ∈ A, ∀ j ∈ B, Disjoint (c5Type i) (c5Type j)) :
    (A.card = 1 ∨ B.card = 1) ∧ A.card ≤ 2 ∧ B.card ≤ 2 := by
  obtain ⟨a, ha⟩ := hA
  obtain ⟨b, hb⟩ := hB
  have hAsub : A ⊆ c5Type b := by
    intro i hi
    exact (c5_adj_iff_mem_type i b).mp ((c5Type_disjoint_iff i b).mp (hcross i hi b hb))
  have hBsub : B ⊆ c5Type a := by
    intro j hj
    exact (c5_adj_iff_mem_type j a).mp
      ((c5Type_disjoint_iff a j).mp (hcross a ha j hj)).symm
  refine ⟨?_, (Finset.card_le_card hAsub).trans_eq (c5Type_card b),
    (Finset.card_le_card hBsub).trans_eq (c5Type_card a)⟩
  by_cases h : A.card = 1
  · exact Or.inl h
  · right
    obtain ⟨i, hi, j, hj, hij⟩ := Finset.one_lt_card.mp (by
      have := Finset.card_pos.mpr ⟨a, ha⟩; omega)
    have heq : B = {b} := by
      ext z
      constructor
      · intro hz
        apply Finset.mem_singleton.mpr
        exact c5_common_neighbors_unique i j z b hij
          ((c5Type_disjoint_iff i z).mp (hcross i hi z hz))
          ((c5Type_disjoint_iff j z).mp (hcross j hj z hz))
          ((c5Type_disjoint_iff i b).mp (hcross i hi b hb))
          ((c5Type_disjoint_iff j b).mp (hcross j hj b hb))
      · intro hz
        have := Finset.mem_singleton.mp hz
        simpa only [this] using hb
    simp [heq]

universe u
variable {V : Type u} {G : SimpleGraph V}

noncomputable def cycleNeighborLabels
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (x : V) : Finset (Fin 5) := by
  classical
  exact Finset.univ.filter (fun i => G.Adj x (f i))

theorem cycleNeighborLabels_independent
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3) (x : V) :
    ∀ i ∈ cycleNeighborLabels f x, ∀ j ∈ cycleNeighborLabels f x,
      ¬ (SimpleGraph.cycleGraph 5).Adj i j := by
  classical
  intro i hi j hj hadj
  have hfi := (Finset.mem_filter.mp hi).2
  have hfj := (Finset.mem_filter.mp hj).2
  exact (G.isIndepSet_neighborSet_of_triangleFree ht x) hfi hfj
    (fun h => hadj.ne (f.injective h)) (f.toHom.map_adj hadj)

/-- The finite domain is justified by the actual five-cycle copy and exact
neighbor set. Every two-neighbor vertex has one and only one of the five types. -/
theorem cycleNeighborLabels_unique_type
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3) (x : V)
    (hc : (cycleNeighborLabels f x).card = 2) :
    ∃! i : Fin 5, cycleNeighborLabels f x = c5Type i :=
  c5_independent_pair_unique_type _ hc (cycleNeighborLabels_independent f ht x)

/-- Necessity only: compatible labels do not imply an edge. -/
theorem adjacent_cycleNeighborLabels_disjoint
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    {x y : V} (hxy : G.Adj x y) :
    Disjoint (cycleNeighborLabels f x) (cycleNeighborLabels f y) := by
  classical
  rw [Finset.disjoint_left]
  intro i hi hj
  have hx := (Finset.mem_filter.mp hi).2
  have hy := (Finset.mem_filter.mp hj).2
  exact (G.isIndepSet_neighborSet_of_triangleFree ht x) hxy hx hy.ne hy

/-- Complete bipartite adjacency supplies every cross-compatibility constraint;
the type quotient therefore has a singleton side and at most two opposite types. -/
theorem complete_bipartite_type_image
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (A B : Finset V) (hA : A.Nonempty) (hB : B.Nonempty) (t : V → Fin 5)
    (hlabels : ∀ x, x ∈ A ∨ x ∈ B → cycleNeighborLabels f x = c5Type (t x))
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y) :
    ((A.image t).card = 1 ∨ (B.image t).card = 1) ∧
      (A.image t).card ≤ 2 ∧ (B.image t).card ≤ 2 := by
  classical
  apply c5_complete_type_sets _ _ (hA.image t) (hB.image t)
  intro i hi j hj
  obtain ⟨x, hx, rfl⟩ := Finset.mem_image.mp hi
  obtain ⟨y, hy, rfl⟩ := Finset.mem_image.mp hj
  have h := adjacent_cycleNeighborLabels_disjoint f ht (hedges x hx y hy)
  rw [hlabels x (Or.inl hx), hlabels y (Or.inr hy)] at h
  exact h

end EG617
