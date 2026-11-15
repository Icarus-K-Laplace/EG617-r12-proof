module
public import EG617.Core.R23EdgeCompletion

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V] {G : SimpleGraph V}

/-- Lift the finite singleton extension to an actual missing cycle edge whose
endpoints have no common neighbor. Every graph/partition hypothesis is explicit. -/
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
      ∀ w, G.Adj u w → ¬ G.Adj (f q) w := by
  classical
  obtain ⟨a, hza, _⟩ := cycleNeighborLabels_unique_type f ht z hz2
  have hex : ∀ x, ∃ i, x ∈ B → cycleNeighborLabels f x = c5Type i := by
    intro x
    by_cases hx : x ∈ B
    · obtain ⟨i, hi, _⟩ := cycleNeighborLabels_unique_type f ht x (hB2 x hx)
      exact ⟨i, fun _ => hi⟩
    · exact ⟨0, fun h => False.elim (hx h)⟩
  choose t hlabels using hex
  have hsub : B.image t ⊆ c5Type a := by
    intro b hb
    obtain ⟨x, hx, rfl⟩ := Finset.mem_image.mp hb
    have hd := adjacent_cycleNeighborLabels_disjoint f ht (hedges z hz x hx)
    rw [hza, hlabels x hx] at hd
    exact (c5_adj_iff_mem_type _ _).mp ((c5Type_disjoint_iff _ _).mp hd).symm
  have hp : ∀ b ∈ B.image t, p ∉ c5Type b := by
    intro b hb hpb
    obtain ⟨x, hx, rfl⟩ := Finset.mem_image.mp hb
    have hd := adjacent_cycleNeighborLabels_disjoint f ht (hedges u hu x hx)
    rw [hsingle, hlabels x hx] at hd
    exact Finset.disjoint_left.mp hd (Finset.mem_singleton_self p) hpb
  obtain ⟨i, hpi, hcompat⟩ := c5_singleton_extension a (B.image t) hsub p hp
  have hsmall : ({p} : Finset (Fin 5)).card < (c5Type i).card := by
    rw [c5Type_card]
    simp
  obtain ⟨q, hq, hqnot⟩ := Finset.exists_mem_notMem_of_card_lt_card hsmall
  have hqp : q ≠ p := by simpa only [Finset.mem_singleton] using hqnot
  have huS : u ∉ S := Finset.mem_compl.mp (hcover ▸ Finset.mem_union_left B hu)
  have hfq : f q ∈ S := hS ▸ Finset.mem_image.mpr ⟨q, Finset.mem_univ q, rfl⟩
  refine ⟨q, (fun h => huS (h.symm ▸ hfq)), ?_, ?_⟩
  · intro huq
    have hm : q ∈ cycleNeighborLabels f u := Finset.mem_filter.mpr ⟨Finset.mem_univ q, huq⟩
    rw [hsingle] at hm
    exact hqp (Finset.mem_singleton.mp hm)
  · intro w huw
    by_cases hwS : w ∈ S
    · have hwp : w = f p := by
        obtain ⟨j, _, rfl⟩ := Finset.mem_image.mp (hS.symm ▸ hwS)
        have hm : j ∈ cycleNeighborLabels f u := Finset.mem_filter.mpr ⟨Finset.mem_univ j, huw⟩
        rw [hsingle] at hm
        exact congrArg f (Finset.mem_singleton.mp hm)
      subst w
      intro hadj
      have hpc5 : (SimpleGraph.cycleGraph 5).Adj p q := by
        apply (c5_adj_iff_mem_type p q).mpr
        rw [← cycleNeighborLabels_cycle_vertex f ht q]
        exact Finset.mem_filter.mpr ⟨Finset.mem_univ p, hadj⟩
      have hn := cycleNeighborLabels_independent f ht (f i) p
        (by rw [cycleNeighborLabels_cycle_vertex f ht i]; exact hpi) q
        (by rw [cycleNeighborLabels_cycle_vertex f ht i]; exact hq)
      exact hn hpc5
    · have hwAB := Finset.mem_union.mp (hcover.symm ▸ Finset.mem_compl.mpr hwS)
      rcases hwAB with hwA | hwB
      · exact False.elim (hA hu hwA huw.ne huw)
      · intro hadj
        have hm : q ∈ cycleNeighborLabels f w :=
          Finset.mem_filter.mpr ⟨Finset.mem_univ q, hadj.symm⟩
        rw [hlabels w hwB] at hm
        exact Finset.disjoint_left.mp (hcompat (t w) (Finset.mem_image.mpr ⟨w, hwB, rfl⟩)) hq hm

end EG617
