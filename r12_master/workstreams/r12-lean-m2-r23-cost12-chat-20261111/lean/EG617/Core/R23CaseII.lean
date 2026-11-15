module
public import EG617.Core.C5SingletonGraphLift

@[expose] public section
set_option autoImplicit false
attribute [local instance 2000] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- An actual single missing edge is added; all graph properties of the
resulting Case I graph are explicit. -/
def R23OneEdgeCompletion (G : SimpleGraph V) : Prop :=
  ∃ u v : V, u ≠ v ∧ ¬ G.Adj u v ∧
    let H := G ⊔ SimpleGraph.edge u v
    G ≤ H ∧ H.CliqueFree 3 ∧ CoreIndependenceBound 11 H ∧
      H.edgeFinset.card = 122 ∧ R23CaseIProfile H

/-- Structural graph-level version of the singleton completion. Its neighborhood
distribution will be supplied by the exact R23 ledger, not assumed by the parent. -/
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
    R23OneEdgeCompletion G := by
  classical
  obtain ⟨u, huT, hu1, hrest⟩ := hd
  have huLabels : (cycleNeighborLabels f u).card = 1 :=
    (cycleNeighborLabels_card_eq f S hS u).trans hu1
  obtain ⟨p, hp⟩ := Finset.card_eq_one.mp huLabels
  have hgo : ∀ C D : Finset V, C ∪ D = Sᶜ →
      G.IsIndepSet (C : Set V) → C.card = 9 →
      (∀ x ∈ C, ∀ y ∈ D, G.Adj x y) → u ∈ C → R23OneEdgeCompletion G := by
    intro C D hCD hC hCc hcross huC
    have hsmall : ({u} : Finset V).card < C.card := by simp [hCc]
    obtain ⟨z, hz, hzu⟩ := Finset.exists_mem_notMem_of_card_lt_card hsmall
    have hzne : z ≠ u := by simpa only [Finset.mem_singleton] using hzu
    have hzT : z ∈ Sᶜ := hCD ▸ Finset.mem_union_left D hz
    have hz2 : (cycleNeighborLabels f z).card = 2 :=
      (cycleNeighborLabels_card_eq f S hS z).trans (hrest z hzT hzne)
    have hD2 : ∀ x ∈ D, (cycleNeighborLabels f x).card = 2 := by
      intro x hx
      have hxne : x ≠ u := by
        intro hx_eq
        subst x
        exact (hcross u huC u hx).ne rfl
      exact (cycleNeighborLabels_card_eq f S hS x).trans
        (hrest x (hCD ▸ Finset.mem_union_right C hx) hxne)
    obtain ⟨q, hne, hn, hcommon⟩ := singleton_cycle_edge_completion_witness
      f ht S C D hS hCD hC u z huC hz p hp hz2 hD2 hcross
    exact ⟨u, f q, hne, hn, r23_one_edge_completion_case_I G hV ht hI he u (f q) hne hn hcommon⟩
  rcases Finset.mem_union.mp (hcover.symm ▸ huT) with huA | huB
  · exact hgo A B hcover hA hAc hedges huA
  · exact hgo B A (by rw [Finset.union_comm]; exact hcover) hB hBc
      (fun x hx y hy => (hedges y hy x hx).symm) huB

/-- The unresolved Case IV exterior, with its actual unique missing cross edge
and the same C5 ledger retained for subsequent endpoint lifting. -/
def R23MissingEdgeExterior (G : SimpleGraph V) : Prop :=
  ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G),
    Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
    ∃ A : Finset ((Sᶜ : Finset V) : Set V),
      let H := G.induce ((Sᶜ : Finset V) : Set V)
      H.IsIndepSet (A : Set _) ∧ H.IsIndepSet ((Aᶜ : Finset _) : Set _) ∧
      A.card = 9 ∧ Aᶜ.card = 9 ∧ coreInducedEdgeCount G Sᶜ = 80 ∧
      ∃ a ∈ A, ∃ b ∈ Aᶜ, ∀ x ∈ A, ∀ y ∈ Aᶜ,
        (¬ H.Adj x y ↔ x = a ∧ y = b)

/-- Original R23 assumptions with121 edges: the complete exterior case is
actually completed to Case I; only the exact one-missing-edge exterior remains.
No neighborhood distribution or terminal type pattern is a hypothesis. -/
theorem r23_121_completion_or_missing_exterior (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 121) :
    R23OneEdgeCompletion G ∨ R23MissingEdgeExterior G := by
  classical
  obtain ⟨S, f, hf, hl, A, hA, hB, h9, h9', hcases⟩ :=
    r23_exists_balanced_exterior G hV ht hI (by omega)
  let T := Sᶜ
  let H := G.induce (T : Set V)
  rcases hcases with ⟨h81, hfull⟩ | ⟨h80, hmiss⟩
  · left
    have hy : coreInducedEdgeCount G T = 81 := by
      simpa only [coreInducedEdgeCount, H, SimpleGraph.edgeFinset_card,
        Set.fintypeCard_eq_ncard] using h81
    have hd : ∃ u ∈ T, (S.filter (G.Adj u)).card = 1 ∧
        ∀ x ∈ T, x ≠ u → (S.filter (G.Adj x)).card = 2 := by
      have hdist := hl.2.2.2.2.2.2.2.2.2.2.2.1
      rcases hdist with h | h | h
      · have hh : coreInducedEdgeCount G T = 80 := h.1
        omega
      · exact h.2.2.2
      · have hh := h.2.2.1
        omega
    let P : Finset V := A.image (fun a : (T : Set V) => (a : V))
    let Q : Finset V := (Aᶜ : Finset (T : Set V)).image (fun b : (T : Set V) => (b : V))
    have hP : P.card = 9 := by
      rw [Finset.card_image_of_injective _ Subtype.val_injective]
      exact h9
    have hQ : Q.card = 9 := by
      rw [Finset.card_image_of_injective _ Subtype.val_injective]
      simpa only [Finset.card_compl, Set.fintypeCard_eq_ncard] using h9'
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
    have hPi : G.IsIndepSet (P : Set V) := by
      intro x hx y hy hxy
      obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp hx
      obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hy
      exact hA ha hb (fun h => hxy (congrArg Subtype.val h))
    have hQi : G.IsIndepSet (Q : Set V) := by
      intro x hx y hy hxy
      obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp hx
      obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hy
      exact hB (by simpa only [Finset.mem_coe, Finset.mem_compl] using ha)
        (by simpa only [Finset.mem_coe, Finset.mem_compl] using hb) (fun h => hxy (congrArg Subtype.val h))
    have hcross : ∀ x ∈ P, ∀ y ∈ Q, G.Adj x y := by
      intro x hx y hy
      obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp hx
      obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hy
      exact hfull a ha b (by simpa only [Finset.mem_compl] using hb)
    exact singleton_partition_completes_to_case_I G hV ht hI he f S P Q hf hcover hPi hQi hP hQ hcross hd
  · right
    refine ⟨S, f, hf, hl, A, hA, hB, h9, h9', ?_, hmiss⟩
    simpa only [coreInducedEdgeCount, H, SimpleGraph.edgeFinset_card,
      Set.fintypeCard_eq_ncard] using h80

end EG617
