module
public import EG617.Core.R23CompleteExterior

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V] {G : SimpleGraph V}

/-- Each type fiber contains its cycle vertex and exactly its exterior fiber. -/
theorem cycle_type_fiber_card
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (S : Finset V)
    (hS : Finset.univ.image f = S) (t : V → Fin 5)
    (hcycle : ∀ i, t (f i) = i) (i : Fin 5) :
    (Finset.univ.filter (fun x => t x = i)).card =
      1 + (Sᶜ.filter (fun x => t x = i)).card := by
  classical
  have hfi : f i ∈ S := hS ▸ Finset.mem_image.mpr ⟨i, Finset.mem_univ i, rfl⟩
  have hset : Finset.univ.filter (fun x => t x = i) =
      insert (f i) (Sᶜ.filter (fun x => t x = i)) := by
    ext x
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_insert]
    constructor
    · intro hx
      by_cases hs : x ∈ S
      · obtain ⟨j, _, rfl⟩ := Finset.mem_image.mp (hS.symm ▸ hs)
        have hji : j = i := (hcycle j).symm.trans hx
        exact Or.inl (congrArg f hji)
      · exact Or.inr ⟨Finset.mem_compl.mpr hs, hx⟩
    · rintro (rfl | ⟨_, hx⟩)
      · exact hcycle i
      · exact hx
  rw [hset, Finset.card_insert_of_notMem]
  · omega
  · intro hx
    exact (Finset.mem_compl.mp (Finset.mem_filter.mp hx).1) hfi

/-- The singleton side of a balanced exterior supplies the class of size ten;
the two nonneighboring types have no exterior vertices. -/
theorem singleton_side_type_fiber_profile
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S A B : Finset V) (hS : Finset.univ.image f = S)
    (hcover : A ∪ B = Sᶜ) (hA : A.card = 9)
    (t : V → Fin 5) (hlabels : ∀ x, cycleNeighborLabels f x = c5Type (t x))
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y)
    (hsingle : (A.image t).card = 1) :
    ∃ a : Fin 5, (Finset.univ.filter (fun x => t x = a)).card = 10 ∧
      ∀ i, i ≠ a → ¬ (SimpleGraph.cycleGraph 5).Adj a i →
        (Finset.univ.filter (fun x => t x = i)).card = 1 := by
  classical
  have hcycle : ∀ i, t (f i) = i := by
    intro i
    have hi := cycleNeighborLabels_cycle_vertex f ht i
    have hc : (cycleNeighborLabels f (f i)).card = 2 := by rw [hi, c5Type_card]
    exact (cycleNeighborLabels_unique_type f ht (f i) hc).unique (hlabels (f i)) hi
  obtain ⟨a, himage⟩ := Finset.card_eq_one.mp hsingle
  have hconst : ∀ x ∈ A, t x = a := by
    intro x hx
    have hm : t x ∈ A.image t := Finset.mem_image.mpr ⟨x, hx, rfl⟩
    rw [himage] at hm
    exact Finset.mem_singleton.mp hm
  obtain ⟨z, hz⟩ := Finset.card_pos.mp (by omega : 0 < A.card)
  have hBtype : ∀ x ∈ B, (SimpleGraph.cycleGraph 5).Adj a (t x) := by
    intro x hx
    have h := adjacent_cycleNeighborLabels_disjoint f ht (hedges z hz x hx)
    rw [hlabels z, hlabels x, hconst z hz] at h
    exact (c5Type_disjoint_iff _ _).mp h
  have hfiber : Sᶜ.filter (fun x => t x = a) = A := by
    ext x
    constructor
    · intro hx
      obtain ⟨hxt, hxa⟩ := Finset.mem_filter.mp hx
      rcases Finset.mem_union.mp (hcover.symm ▸ hxt) with hxA | hxB
      · exact hxA
      · have ha := hBtype x hxB
        rw [hxa] at ha
        exact False.elim (ha.ne rfl)
    · intro hx
      exact Finset.mem_filter.mpr ⟨hcover ▸ Finset.mem_union_left B hx, hconst x hx⟩
  refine ⟨a, ?_, ?_⟩
  · rw [cycle_type_fiber_card f S hS t hcycle a, hfiber, hA]
  · intro i hia hn
    have hempty : Sᶜ.filter (fun x => t x = i) = ∅ := by
      apply Finset.eq_empty_iff_forall_notMem.mpr
      intro x hx
      obtain ⟨hxt, hxi⟩ := Finset.mem_filter.mp hx
      rcases Finset.mem_union.mp (hcover.symm ▸ hxt) with hxA | hxB
      · exact hia (hxi.symm.trans (hconst x hxA))
      · exact hn (hxi ▸ hBtype x hxB)
    rw [cycle_type_fiber_card f S hS t hcycle i, hempty]
    simp

/-- Either singleton-side orientation gives the same rotated fiber profile. -/
theorem complete_exterior_type_fiber_profile
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S A B : Finset V) (hS : Finset.univ.image f = S)
    (hcover : A ∪ B = Sᶜ) (hA : A.card = 9) (hB : B.card = 9)
    (t : V → Fin 5) (hlabels : ∀ x, cycleNeighborLabels f x = c5Type (t x))
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y) :
    ∃ a : Fin 5, (Finset.univ.filter (fun x => t x = a)).card = 10 ∧
      ∀ i, i ≠ a → ¬ (SimpleGraph.cycleGraph 5).Adj a i →
        (Finset.univ.filter (fun x => t x = i)).card = 1 := by
  classical
  have hAn : A.Nonempty := Finset.card_pos.mp (by omega)
  have hBn : B.Nonempty := Finset.card_pos.mp (by omega)
  have hquot := complete_bipartite_type_image f ht A B hAn hBn t
    (fun x _ => hlabels x) hedges
  rcases hquot.1 with h | h
  · exact singleton_side_type_fiber_profile f ht S A B hS hcover hA t hlabels hedges h
  · exact singleton_side_type_fiber_profile f ht S B A hS
      (by rw [Finset.union_comm]; exact hcover) hB t hlabels
      (fun x hx y hy => (hedges y hy x hx).symm) h

end EG617
