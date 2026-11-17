module
public import EG617.Core.E286Excess

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Frozen E286 Section2. Four actual independent degree12 seeds exist.
The seed set is derived, not an additional assumption of the equality theorem. -/
theorem e286_exists_regular_independent_four (G : SimpleGraph V)
    (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      ∀ v ∈ I, G.degree v = 12 := by
  classical
  by_contra hn
  let S := excessSupport G
  let R := Sᶜ
  have hRreg : ∀ v ∈ R, G.degree v = 12 := by
    intro v hv
    have hr := e286_regular_complement G hG
    change v ∈ (excessSupport G)ᶜ at hv
    rw [hr] at hv
    exact (Finset.mem_filter.mp hv).2
  have hI3 : CoreIndependenceBound 3 (G.induce (R : Set V)) := by
    intro T hT
    by_contra hcard
    obtain ⟨U, hUT, hU⟩ := Finset.exists_subset_card_eq (show 4 ≤ T.card by omega)
    let I : Finset V := U.image (fun x : (R : Set V) => (x : V))
    have hi : I.card = 4 := by
      rw [Finset.card_image_of_injective _ Subtype.val_injective]
      exact hU
    have hind : G.IsIndepSet (I : Set V) := by
      intro x hx y hy hxy
      obtain ⟨x', hx', rfl⟩ := Finset.mem_image.mp hx
      obtain ⟨y', hy', rfl⟩ := Finset.mem_image.mp hy
      exact hT (hUT hx') (hUT hy') (fun he => hxy (congrArg Subtype.val he))
    apply hn
    refine ⟨I, hi, hind, ?_⟩
    intro v hv
    obtain ⟨x, _, rfl⟩ := Finset.mem_image.mp hv
    exact hRreg x x.property
  have hcf : (G.induce (R : Set V))ᶜ.CliqueFree 4 := by
    intro T hT
    have hi : (G.induce (R : Set V)).IsNIndepSet 4 T :=
      (SimpleGraph.isNClique_compl (G.induce (R : Set V))).mp hT
    have hb := hI3 T hi.isIndepSet
    rw [hi.card_eq] at hb
    omega
  have ht : (G.induce (R : Set V))ᶜ.edgeFinset.card ≤
      SimpleGraph.turanNumber R.card 3 := by
    simpa only [Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using
      hcf.card_edgeFinset_le
  have hc := core_compl_edge_count (G.induce (R : Set V))
  have hp := e286_regular_edge_ledger G hG
  have hb := core_induced_edges_le_choose G S
  have hq := e286_support_card_le_eight G hG
  have hcard := Finset.card_add_card_compl S
  simp only [hG.1] at hcard
  have hR : R.card = 47 - S.card := by dsimp only [R]; omega
  rw [SimpleGraph.turanNumber_three, hR] at ht
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard,
    Set.ncard_coe_finset, hR] at hc ht
  simp only [coreInducedEdgeCount, SimpleGraph.edgeFinset_card,
    Set.fintypeCard_eq_ncard] at hp hb
  change S.card ≤ 8 at hq
  change (G.induce (R : Set V)).edgeSet.ncard + 12 * S.card + 8 =
    286 + (G.induce (S : Set V)).edgeSet.ncard at hp
  have hnum : (47 - S.card).choose 2 + 12 * S.card + 8 ≤
      286 + S.card.choose 2 + (47 - S.card) ^ 2 / 3 := by omega
  generalize S.card = q at hnum hq
  interval_cases q <;> norm_num [Nat.choose_two_right] at hnum

end EG617

