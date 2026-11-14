module
public import EG617.Core.R23BalancedExterior

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V] {G : SimpleGraph V}

theorem cycleNeighborLabels_cycle_vertex
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (i : Fin 5) : cycleNeighborLabels f (f i) = c5Type i := by
  classical
  symm
  apply Finset.eq_of_subset_of_card_le
  · intro j hj
    apply Finset.mem_filter.mpr
    exact ⟨Finset.mem_univ j,
      f.toHom.map_adj (((c5_adj_iff_mem_type j i).mpr hj).symm)⟩
  · have h := cycle_copy_twice_neighbor_card_le 2 f ht (f i)
    change 2 * (cycleNeighborLabels f (f i)).card ≤ 5 at h
    rw [c5Type_card]
    omega

/-- Actual full cross adjacency, together with exact types, yields all graph
edges. Merely assuming pairwise type compatibility would not suffice. -/
theorem complete_exterior_type_presentation
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S A B : Finset V) (hS : Finset.univ.image f = S)
    (hcover : A ∪ B = Sᶜ) (hA : A.Nonempty) (hB : B.Nonempty)
    (t : V → Fin 5) (hlabels : ∀ x, cycleNeighborLabels f x = c5Type (t x))
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y) :
    ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y) := by
  classical
  have hforward : ∀ {x y}, G.Adj x y →
      (SimpleGraph.cycleGraph 5).Adj (t x) (t y) := by
    intro x y hxy
    have h := adjacent_cycleNeighborLabels_disjoint f ht hxy
    rw [hlabels x, hlabels y] at h
    exact (c5Type_disjoint_iff _ _).mp h
  have hcycle : ∀ i, t (f i) = i := by
    intro i
    have hi := cycleNeighborLabels_cycle_vertex f ht i
    have hc : (cycleNeighborLabels f (f i)).card = 2 := by rw [hi, c5Type_card]
    exact (cycleNeighborLabels_unique_type f ht (f i) hc).unique (hlabels (f i)) hi
  have hfrom_cycle : ∀ x ∈ S, ∀ y,
      (SimpleGraph.cycleGraph 5).Adj (t x) (t y) → G.Adj x y := by
    intro x hx y hxy
    obtain ⟨i, _, rfl⟩ := Finset.mem_image.mp (hS.symm ▸ hx)
    rw [hcycle] at hxy
    have hm : i ∈ cycleNeighborLabels f y := by
      rw [hlabels y]
      exact (c5_adj_iff_mem_type _ _).mp hxy
    exact (Finset.mem_filter.mp hm).2.symm
  have hntriangle : ∀ a b c : Fin 5,
      (SimpleGraph.cycleGraph 5).Adj a c →
      (SimpleGraph.cycleGraph 5).Adj b c →
      ¬ (SimpleGraph.cycleGraph 5).Adj a b := by
    intro a b c hac hbc hab
    exact Finset.disjoint_left.mp ((c5Type_disjoint_iff a b).mpr hab)
      ((c5_adj_iff_mem_type c a).mp hac.symm)
      ((c5_adj_iff_mem_type c b).mp hbc.symm)
  intro x y
  refine ⟨hforward, ?_⟩
  intro hxy
  by_cases hx : x ∈ S
  · exact hfrom_cycle x hx y hxy
  by_cases hy : y ∈ S
  · exact (hfrom_cycle y hy x hxy.symm).symm
  have hxAB : x ∈ A ∨ x ∈ B := Finset.mem_union.mp (hcover.symm ▸ Finset.mem_compl.mpr hx)
  have hyAB : y ∈ A ∨ y ∈ B := Finset.mem_union.mp (hcover.symm ▸ Finset.mem_compl.mpr hy)
  rcases hxAB with hxA | hxB <;> rcases hyAB with hyA | hyB
  · obtain ⟨b, hb⟩ := hB
    exact False.elim (hntriangle (t x) (t y) (t b)
      (hforward (hedges x hxA b hb)) (hforward (hedges y hyA b hb)) hxy)
  · exact hedges x hxA y hyB
  · exact (hedges y hyA x hxB).symm
  · obtain ⟨a, ha⟩ := hA
    exact False.elim (hntriangle (t x) (t y) (t a)
      (hforward (hedges a ha x hxB).symm) (hforward (hedges a ha y hyB).symm) hxy)

/-- The actual types are chosen from neighbor counts; no type assignment is
an assumption of this presentation theorem. -/
theorem complete_exterior_has_type_presentation
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S A B : Finset V) (hS : Finset.univ.image f = S)
    (hcover : A ∪ B = Sᶜ) (hA : A.Nonempty) (hB : B.Nonempty)
    (hd : ∀ x ∈ Sᶜ, (S.filter (G.Adj x)).card = 2)
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y) :
    ∃ t : V → Fin 5, (∀ x, cycleNeighborLabels f x = c5Type (t x)) ∧
      ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y) := by
  classical
  have hc : ∀ x, (cycleNeighborLabels f x).card = 2 := by
    intro x
    by_cases hx : x ∈ S
    · obtain ⟨i, _, rfl⟩ := Finset.mem_image.mp (hS.symm ▸ hx)
      rw [cycleNeighborLabels_cycle_vertex f ht, c5Type_card]
    · exact (cycleNeighborLabels_card_eq f S hS x).trans (hd x (Finset.mem_compl.mpr hx))
  have hex : ∀ x, ∃ i, cycleNeighborLabels f x = c5Type i :=
    fun x => (cycleNeighborLabels_unique_type f ht x (hc x)).exists
  choose t hlabels using hex
  exact ⟨t, hlabels, complete_exterior_type_presentation f ht S A B hS hcover hA hB t hlabels hedges⟩

end EG617
