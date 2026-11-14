module
public import EG617.Core.R23TypeLift

@[expose] public section
set_option autoImplicit false
attribute [local instance 2000] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Two cycle neighbors leave room for at most nine disjoint exterior neighbors. -/
theorem two_cycle_neighbors_cross_card_le_nine (G : SimpleGraph V)
    (ht : G.CliqueFree 3) (hI : CoreIndependenceBound 11 G)
    (S B : Finset V) (v : V) (hd : (S.filter (G.Adj v)).card = 2)
    (hB : B ⊆ Sᶜ) (hedges : ∀ b ∈ B, G.Adj v b) : B.card ≤ 9 := by
  classical
  let N := S.filter (G.Adj v)
  have hdis : Disjoint B N := by
    rw [Finset.disjoint_left]
    intro x hx hn
    exact (Finset.mem_compl.mp (hB hx)) (Finset.mem_filter.mp hn).1
  have hi : G.IsIndepSet ((B ∪ N : Finset V) : Set V) := by
    apply (G.isIndepSet_neighborSet_of_triangleFree ht v).mono
    intro x hx
    rcases Finset.mem_union.mp hx with hx | hx
    · exact hedges x hx
    · exact (Finset.mem_filter.mp hx).2
  have hb := hI (B ∪ N) hi
  rw [Finset.card_union_of_disjoint hdis] at hb
  change B.card + (S.filter (G.Adj v)).card ≤ 11 at hb
  omega

/-- From the original R23 contract, the exterior always has balanced parts.
This excludes the K8,10 branch by its actual neighbors, without assuming types. -/
theorem r23_exists_balanced_exterior (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G),
      Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
      ∃ A : Finset ((Sᶜ : Finset V) : Set V),
        let H := G.induce ((Sᶜ : Finset V) : Set V)
        H.IsIndepSet (A : Set _) ∧ H.IsIndepSet ((Aᶜ : Finset _) : Set _) ∧
        A.card = 9 ∧ Aᶜ.card = 9 ∧
        ((H.edgeFinset.card = 81 ∧ ∀ a ∈ A, ∀ b ∈ Aᶜ, H.Adj a b) ∨
         (H.edgeFinset.card = 80 ∧ ∃ a ∈ A, ∃ b ∈ Aᶜ,
           ∀ x ∈ A, ∀ y ∈ Aᶜ, (¬ H.Adj x y ↔ x = a ∧ y = b))) := by
  classical
  obtain ⟨v, p, _, hp, h5, hl⟩ := r23_exact_neighbor_ledger G hV ht hI he
  obtain ⟨f, hf⟩ := five_cycle_copy_same_support p hp h5
  let S := p.support.toFinset
  let T := Sᶜ
  let H := G.induce (T : Set V)
  have h18 : T.card = 18 := hl.2.1
  have h80 : 80 ≤ coreInducedEdgeCount G T := hl.2.2.2.2.1
  have hHV : Fintype.card (T : Set V) = 18 := by
    simpa only [Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using h18
  have hHt : H.CliqueFree 3 :=
    ht.comap (SimpleGraph.Embedding.induce (G := G) (T : Set V)).isContained
  have hHe : 80 ≤ H.edgeFinset.card := h80
  have hb : H.Colorable 2 := by
    by_contra hn
    have hsmall := triangleFree_nonbipartite_18_edges_le_73 H hHV hHt hn
    have hsmall' : coreInducedEdgeCount G T ≤ 73 := by
      simpa only [coreInducedEdgeCount, H, SimpleGraph.edgeFinset_card,
        Set.fintypeCard_eq_ncard] using hsmall
    omega
  obtain ⟨A, hA, hB, hcases⟩ := bipartite_18_dense_classification H hHV hb hHe
  refine ⟨S, f, hf, hl, A, hA, hB, ?_⟩
  rcases hcases with ⟨ha, hb, he, hc⟩ | ⟨ha, hb, he, hc⟩ | ⟨ha, hb, he, hc⟩
  · exact ⟨ha, hb, Or.inl ⟨he, hc⟩⟩
  · have hd : ∀ x ∈ T, (S.filter (G.Adj x)).card = 2 := by
      have hdist := hl.2.2.2.2.2.2.2.2.2.2.2.1
      rcases hdist with h | h | h
      · exact h.2.2.2
      · have hy : coreInducedEdgeCount G T = 81 := h.1
        have he' : coreInducedEdgeCount G T = 80 := by
          simpa only [coreInducedEdgeCount, H, SimpleGraph.edgeFinset_card,
            Set.fintypeCard_eq_ncard] using he
        omega
      · have hy : coreInducedEdgeCount G T = 81 := h.1
        have he' : coreInducedEdgeCount G T = 80 := by
          simpa only [coreInducedEdgeCount, H, SimpleGraph.edgeFinset_card,
            Set.fintypeCard_eq_ncard] using he
        omega
    obtain ⟨a, ham⟩ := Finset.card_pos.mp (by omega : 0 < A.card)
    let B : Finset V := (Aᶜ : Finset (T : Set V)).image (fun b => (b : V))
    have hBT : B ⊆ T := by
      intro b hb
      obtain ⟨b, _, rfl⟩ := Finset.mem_image.mp hb
      exact b.property
    have hcross : ∀ b ∈ B, G.Adj a.val b := by
      intro b hb
      obtain ⟨b, hbm, rfl⟩ := Finset.mem_image.mp hb
      exact hc a ham b (by simpa only [Finset.mem_compl] using hbm)
    have hle := two_cycle_neighbors_cross_card_le_nine G ht hI S B a.val
      (hd a.val a.property) hBT hcross
    have hcard : B.card = 10 := by
      rw [Finset.card_image_of_injective _ Subtype.val_injective]
      simpa only [Finset.card_compl, Set.fintypeCard_eq_ncard] using hb
    omega
  · exact ⟨ha, hb, Or.inr ⟨he, hc⟩⟩

end EG617
