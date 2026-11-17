module

public import EG617.Core.R23ExactLedger

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V] {G : SimpleGraph V}

/-- A labeled copy on precisely the given cycle support, not an unrelated C5. -/
theorem five_cycle_copy_same_support {v : V} (p : G.Walk v v)
    (hc : p.IsCycle) (h5 : p.length = 5) :
    ∃ f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G,
      Finset.univ.image f = p.support.toFinset := by
  classical
  let S := p.support.toFinset
  have hw : ∀ x ∈ p.support, x ∈ (S : Set V) := by
    intro x hx
    exact List.mem_toFinset.mpr hx
  let q := p.induce (S : Set V) hw
  have hmap : q.map (SimpleGraph.Embedding.induce (S : Set V)).toHom = p := by
    exact SimpleGraph.Walk.map_induce p hw
  have hq : q.IsCycle := SimpleGraph.Walk.IsCycle.of_map (hmap.symm ▸ hc)
  have hql : q.length = 5 := by
    have hs : q.support.length = p.support.length := by
      simp only [q, SimpleGraph.Walk.support_induce, List.length_attachWith]
    have hqLen := q.length_support
    have hpLen := p.length_support
    omega
  obtain ⟨g⟩ := (SimpleGraph.cycleGraph_isContained_iff (by decide : 2 < 5)).mpr
    ⟨_, q, hq, hql⟩
  let f := (SimpleGraph.Embedding.induce (S : Set V)).toCopy.comp g
  refine ⟨f, Finset.eq_of_subset_of_card_le ?_ ?_⟩
  · intro x hx
    obtain ⟨i, _, rfl⟩ := Finset.mem_image.mp hx
    exact (g i).property
  · rw [Finset.card_image_of_injective _ (show Function.Injective f from f.injective)]
    simp only [Finset.card_univ, Fintype.card_fin]
    exact le_of_eq ((cycle_support_card p hc).trans h5)

/-- Exact transfer of neighbor counts along the labeled cycle bijection. -/
theorem cycleNeighborLabels_card_eq
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (S : Finset V)
    (hS : Finset.univ.image f = S) (x : V) :
    (cycleNeighborLabels f x).card = (S.filter (G.Adj x)).card := by
  classical
  have himage : (cycleNeighborLabels f x).image f = S.filter (G.Adj x) := by
    ext y
    simp only [cycleNeighborLabels, Finset.mem_image, Finset.mem_filter,
      Finset.mem_univ, true_and]
    constructor
    · rintro ⟨i, hi, rfl⟩
      exact ⟨hS ▸ Finset.mem_image.mpr ⟨i, Finset.mem_univ i, rfl⟩, hi⟩
    · rintro ⟨hy, hxy⟩
      obtain ⟨i, _, rfl⟩ := Finset.mem_image.mp (hS.symm ▸ hy)
      exact ⟨i, hxy, rfl⟩
  rw [← himage, Finset.card_image_of_injective _ (show Function.Injective f from f.injective)]

/-- The ledger and every two-neighbor type are realized on one common C5 copy.
All hypotheses are the original dense R23 contract. -/
theorem r23_exact_labeled_neighbor_ledger (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G),
      Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
      (∀ x, (cycleNeighborLabels f x).card = (S.filter (G.Adj x)).card) ∧
      (∀ x ∈ Sᶜ, (S.filter (G.Adj x)).card = 2 →
        ∃! i : Fin 5, cycleNeighborLabels f x = c5Type i) := by
  classical
  obtain ⟨v, p, _, hc, h5, hledger⟩ := r23_exact_neighbor_ledger G hV ht hI he
  obtain ⟨f, hf⟩ := five_cycle_copy_same_support p hc h5
  refine ⟨p.support.toFinset, f, hf, hledger, cycleNeighborLabels_card_eq f _ hf, ?_⟩
  intro x _ hx
  exact cycleNeighborLabels_unique_type f ht x ((cycleNeighborLabels_card_eq f _ hf x).trans hx)

end EG617
