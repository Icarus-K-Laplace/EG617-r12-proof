module
public import EG617.Core.C5TypePresentation

@[expose] public section
set_option autoImplicit false
attribute [local instance 2000] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- The 122-edge branch is an actual C5 type presentation, with both directions
of adjacency derived from the original graph assumptions. Class sizes remain
a separate classification obligation. -/
theorem r23_122_type_presentation (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 122) :
    ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G)
      (t : V → Fin 5), Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
      (∀ x, cycleNeighborLabels f x = c5Type (t x)) ∧
      ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y) := by
  classical
  obtain ⟨S, f, hf, hl, A, hA, hB, h9, h9', hcases⟩ :=
    r23_exists_balanced_exterior G hV ht hI (by omega)
  let T := Sᶜ
  let H := G.induce (T : Set V)
  have hdist : coreInducedEdgeCount G T = 81 ∧
      ∀ x ∈ T, (S.filter (G.Adj x)).card = 2 := by
    have hh := hl.2.2.2.2.2.2.2.2.2.2.2.1
    rcases hh with h | h | h
    · have := h.2.2.1
      omega
    · have := h.2.2.1
      omega
    · exact ⟨h.1, h.2.2.2⟩
  have hfull : ∀ a ∈ A, ∀ b ∈ Aᶜ, H.Adj a b := by
    rcases hcases with ⟨_, hc⟩ | ⟨he80, _⟩
    · intro a ha b hb
      exact hc a ha b (by simpa only [Finset.mem_compl] using hb)
    · have he80' : coreInducedEdgeCount G T = 80 := by
        simpa only [coreInducedEdgeCount, H, SimpleGraph.edgeFinset_card,
          Set.fintypeCard_eq_ncard] using he80
      omega
  let P : Finset V := A.image (fun a : (T : Set V) => (a : V))
  let Q : Finset V := (Aᶜ : Finset (T : Set V)).image (fun b : (T : Set V) => (b : V))
  have hP : P.Nonempty := (Finset.card_pos.mp (by omega : 0 < A.card)).image _
  have hQ : Q.Nonempty := by
    have hcard : (Aᶜ : Finset (T : Set V)).card = 9 := by
      simpa only [Finset.card_compl, Set.fintypeCard_eq_ncard] using h9'
    exact (Finset.card_pos.mp (by omega : 0 < (Aᶜ : Finset (T : Set V)).card)).image _
  have hcover : P ∪ Q = Sᶜ := by
    ext x
    rw [Finset.mem_union]
    constructor
    · rintro (hx | hx)
      · obtain ⟨a, _, rfl⟩ := Finset.mem_image.mp hx
        exact a.property
      · obtain ⟨b, _, rfl⟩ := Finset.mem_image.mp hx
        exact b.property
    · intro hx
      let z : (T : Set V) := ⟨x, hx⟩
      by_cases hz : z ∈ A
      · exact Or.inl (Finset.mem_image.mpr ⟨z, hz, rfl⟩)
      · exact Or.inr (Finset.mem_image.mpr ⟨z, Finset.mem_compl.mpr hz, rfl⟩)
  have hcross : ∀ x ∈ P, ∀ y ∈ Q, G.Adj x y := by
    intro x hx y hy
    obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hy
    exact hfull a ha b (by simpa only [Finset.mem_compl] using hb)
  obtain ⟨t, htlabels, hpres⟩ := complete_exterior_has_type_presentation
    f ht S P Q hf hcover hP hQ hdist.2 hcross
  exact ⟨S, f, t, hf, hl, htlabels, hpres⟩

end EG617
