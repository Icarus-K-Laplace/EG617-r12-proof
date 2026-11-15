module
public import EG617.Core.R23CaseII

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V] {G : SimpleGraph V}

/-- Compatible missing endpoints have no common neighbor: the cycle case uses
actual label disjointness; the exterior case uses the two independent parts. -/
theorem disjoint_cycle_neighbors_no_common_neighbor
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G)
    (S A B : Finset V) (hS : Finset.univ.image f = S) (hcover : A ∪ B = Sᶜ)
    (hA : G.IsIndepSet (A : Set V)) (hB : G.IsIndepSet (B : Set V))
    (u v : V) (hu : u ∈ A) (hv : v ∈ B)
    (hd : Disjoint (cycleNeighborLabels f u) (cycleNeighborLabels f v)) :
    ∀ w, G.Adj u w → ¬ G.Adj v w := by
  classical
  intro w huw hvw
  by_cases hw : w ∈ S
  · obtain ⟨i, _, rfl⟩ := Finset.mem_image.mp (hS.symm ▸ hw)
    exact Finset.disjoint_left.mp hd
      (Finset.mem_filter.mpr ⟨Finset.mem_univ i, huw⟩)
      (Finset.mem_filter.mpr ⟨Finset.mem_univ i, hvw⟩)
  · rcases Finset.mem_union.mp (hcover.symm ▸ Finset.mem_compl.mpr hw) with hwA | hwB
    · exact hA hu hwA huw.ne huw
    · exact hB hv hwB hvw.ne hvw

/-- Incompatible endpoint types make the one missing cross edge precisely a
forbidden type edge. All other cross edges are actual graph hypotheses. -/
theorem missing_exterior_type_presentation
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (S A B : Finset V) (hS : Finset.univ.image f = S) (hcover : A ∪ B = Sᶜ)
    (u v : V) (hA : (A.erase u).Nonempty) (hB : (B.erase v).Nonempty)
    (t : V → Fin 5) (hlabels : ∀ x, cycleNeighborLabels f x = c5Type (t x))
    (hmiss : ∀ x ∈ A, ∀ y ∈ B, (¬ G.Adj x y ↔ x = u ∧ y = v))
    (hincompat : ¬ (SimpleGraph.cycleGraph 5).Adj (t u) (t v)) :
    ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y) := by
  classical
  have hforward : ∀ {x y}, G.Adj x y → (SimpleGraph.cycleGraph 5).Adj (t x) (t y) := by
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
  have hcross : ∀ x ∈ A, ∀ y ∈ B, x ≠ u ∨ y ≠ v → G.Adj x y := by
    intro x hx y hy hn
    by_contra h
    have he := (hmiss x hx y hy).mp h
    rcases hn with hn | hn
    · exact hn he.1
    · exact hn he.2
  have hntriangle : ∀ a b c : Fin 5,
      (SimpleGraph.cycleGraph 5).Adj a c → (SimpleGraph.cycleGraph 5).Adj b c →
      ¬ (SimpleGraph.cycleGraph 5).Adj a b := by
    intro a b c hac hbc hab
    exact Finset.disjoint_left.mp ((c5Type_disjoint_iff a b).mpr hab)
      ((c5_adj_iff_mem_type c a).mp hac.symm) ((c5_adj_iff_mem_type c b).mp hbc.symm)
  obtain ⟨a, ha⟩ := hA
  obtain ⟨b, hb⟩ := hB
  have haA := (Finset.mem_erase.mp ha).2
  have hau := (Finset.mem_erase.mp ha).1
  have hbB := (Finset.mem_erase.mp hb).2
  have hbv := (Finset.mem_erase.mp hb).1
  intro x y
  refine ⟨hforward, ?_⟩
  intro hxy
  by_cases hx : x ∈ S
  · exact hfrom_cycle x hx y hxy
  by_cases hy : y ∈ S
  · exact (hfrom_cycle y hy x hxy.symm).symm
  have hxAB := Finset.mem_union.mp (hcover.symm ▸ Finset.mem_compl.mpr hx)
  have hyAB := Finset.mem_union.mp (hcover.symm ▸ Finset.mem_compl.mpr hy)
  rcases hxAB with hxA | hxB <;> rcases hyAB with hyA | hyB
  · exact False.elim (hntriangle (t x) (t y) (t b)
      (hforward (hcross x hxA b hbB (Or.inr hbv)))
      (hforward (hcross y hyA b hbB (Or.inr hbv))) hxy)
  · by_contra hn
    obtain ⟨rfl, rfl⟩ := (hmiss x hxA y hyB).mp hn
    exact hincompat hxy
  · by_contra hn
    have hnyx : ¬ G.Adj y x := fun h => hn h.symm
    obtain ⟨rfl, rfl⟩ := (hmiss y hyA x hxB).mp hnyx
    exact hincompat hxy.symm
  · exact False.elim (hntriangle (t x) (t y) (t a)
      (hforward (hcross a haA x hxB (Or.inl hau)).symm)
      (hforward (hcross a haA y hyB (Or.inl hau)).symm) hxy)

end EG617
