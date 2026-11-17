module

public import EG617.Core.R23Reduction

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem two_colorable_partition (G : SimpleGraph V) (hb : G.Colorable 2) :
    ∃ A : Finset V, G.IsIndepSet (A : Set V) ∧ G.IsIndepSet ((Aᶜ : Finset V) : Set V) := by
  classical
  obtain ⟨C⟩ := hb
  let A := (Finset.univ : Finset V).filter (fun v => C v = 0)
  refine ⟨A, ?_, ?_⟩
  · intro x hx y hy _
    exact C.not_adj_of_mem_colorClass (Finset.mem_filter.mp hx).2
      (Finset.mem_filter.mp hy).2
  · intro x hx y hy _
    have h1 : ∀ z ∈ Aᶜ, C z = 1 := by
      intro z hz
      have hnot : C z ≠ 0 := by simpa [A] using hz
      exact ((by decide : ∀ i : Fin 2, i = 0 ∨ i = 1) (C z)).resolve_left hnot
    exact C.not_adj_of_mem_colorClass (h1 x hx) (h1 y hy)

theorem bipartition_edge_count (G : SimpleGraph V) (A : Finset V)
    (hA : G.IsIndepSet (A : Set V)) (hB : G.IsIndepSet ((Aᶜ : Finset V) : Set V)) :
    G.edgeFinset.card = adjCount G A Aᶜ := by
  have ha := adjCount_self G A
  have hb := adjCount_self G Aᶜ
  have hza := adjCount_independent_zero G A hA
  have hzb := adjCount_independent_zero G Aᶜ hB
  have hp := edge_partition G A
  omega

theorem adjCount_eq_card_product_filter (G : SimpleGraph V) (A B : Finset V) :
    adjCount G A B = ((A ×ˢ B).filter (fun xy => G.Adj xy.1 xy.2)).card := by
  classical
  unfold adjCount
  rw [← Finset.sum_product']
  simp

theorem adjCount_add_missing_eq_product (G : SimpleGraph V) (A B : Finset V) :
    adjCount G A B + ((A ×ˢ B).filter (fun xy => ¬ G.Adj xy.1 xy.2)).card =
      A.card * B.card := by
  classical
  rw [adjCount_eq_card_product_filter]
  simpa only [Finset.card_product] using
    (Finset.card_filter_add_card_filter_not (s := A ×ˢ B) (fun xy => G.Adj xy.1 xy.2))

theorem complete_cross_of_no_missing (G : SimpleGraph V) (A B : Finset V)
    (h : ((A ×ˢ B).filter (fun xy => ¬ G.Adj xy.1 xy.2)).card = 0) :
    ∀ a ∈ A, ∀ b ∈ B, G.Adj a b := by
  classical
  intro a ha b hb
  by_contra hn
  have hm : (a, b) ∈ (A ×ˢ B).filter (fun xy => ¬ G.Adj xy.1 xy.2) := by
    simp [ha, hb, hn]
  rw [Finset.card_eq_zero.mp h] at hm
  simpa using hm

theorem unique_missing_cross_of_card_one (G : SimpleGraph V) (A B : Finset V)
    (h : ((A ×ˢ B).filter (fun xy => ¬ G.Adj xy.1 xy.2)).card = 1) :
    ∃ a ∈ A, ∃ b ∈ B, ∀ x ∈ A, ∀ y ∈ B,
      (¬ G.Adj x y ↔ x = a ∧ y = b) := by
  classical
  obtain ⟨⟨a, b⟩, he⟩ := Finset.card_eq_one.mp h
  have hm : (a, b) ∈ (A ×ˢ B).filter (fun xy => ¬ G.Adj xy.1 xy.2) := by
    rw [he]; exact Finset.mem_singleton_self _
  have hab := Finset.mem_product.mp (Finset.mem_filter.mp hm).1
  refine ⟨a, hab.1, b, hab.2, ?_⟩
  intro x hx y hy
  have hh := congrArg (fun s : Finset (V × V) => (x, y) ∈ s) he
  simpa [hx, hy] using hh

/-- The exact three exterior forms, stated without choosing vertex labels.
Independent parts cover all vertices; the final disjunction specifies every
cross edge, including the unique deleted edge when present. -/
theorem bipartite_18_dense_classification (G : SimpleGraph V)
    (hV : Fintype.card V = 18) (hb : G.Colorable 2)
    (he : 80 ≤ G.edgeFinset.card) :
    ∃ A : Finset V, G.IsIndepSet (A : Set V) ∧ G.IsIndepSet ((Aᶜ : Finset V) : Set V) ∧
      ((A.card = 9 ∧ Aᶜ.card = 9 ∧ G.edgeFinset.card = 81 ∧
          ∀ a ∈ A, ∀ b ∈ Aᶜ, G.Adj a b) ∨
       (A.card = 8 ∧ Aᶜ.card = 10 ∧ G.edgeFinset.card = 80 ∧
          ∀ a ∈ A, ∀ b ∈ Aᶜ, G.Adj a b) ∨
       (A.card = 9 ∧ Aᶜ.card = 9 ∧ G.edgeFinset.card = 80 ∧
          ∃ a ∈ A, ∃ b ∈ Aᶜ, ∀ x ∈ A, ∀ y ∈ Aᶜ,
            (¬ G.Adj x y ↔ x = a ∧ y = b))) := by
  classical
  obtain ⟨A, hA, hB⟩ := two_colorable_partition G hb
  have horient : ∃ S : Finset V, G.IsIndepSet (S : Set V) ∧
      G.IsIndepSet ((Sᶜ : Finset V) : Set V) ∧ S.card ≤ Sᶜ.card := by
    by_cases h : A.card ≤ Aᶜ.card
    · exact ⟨A, hA, hB, h⟩
    · refine ⟨Aᶜ, hB, ?_, ?_⟩ <;> simp only [compl_compl]
      · exact hA
      · omega
  obtain ⟨S, hS, hT, hle⟩ := horient
  have hsum : S.card + Sᶜ.card = 18 := by
    simpa [hV] using Finset.card_add_card_compl S
  have hedge := bipartition_edge_count G S hS hT
  have hledger := adjCount_add_missing_eq_product G S Sᶜ
  have hprod : 80 ≤ S.card * Sᶜ.card := by omega
  have hcases : (S.card = 8 ∧ Sᶜ.card = 10) ∨ (S.card = 9 ∧ Sᶜ.card = 9) := by
    have hsmall : S.card ≤ 9 := by omega
    generalize hn : S.card = n at *
    interval_cases n <;> simp_all <;> omega
  refine ⟨S, hS, hT, ?_⟩
  rcases hcases with ⟨h8, h10⟩ | ⟨h9, h9'⟩
  · have hmiss : ((S ×ˢ Sᶜ).filter (fun xy => ¬ G.Adj xy.1 xy.2)).card = 0 := by
      rw [h8, h10] at hledger; omega
    exact Or.inr (Or.inl ⟨h8, h10, by rw [h8, h10] at hledger; omega,
      complete_cross_of_no_missing G S Sᶜ hmiss⟩)
  · rw [h9, h9'] at hledger
    by_cases h81 : G.edgeFinset.card = 81
    · exact Or.inl ⟨h9, h9', h81,
        complete_cross_of_no_missing G S Sᶜ (by omega)⟩
    · exact Or.inr (Or.inr ⟨h9, h9', by omega,
        unique_missing_cross_of_card_one G S Sᶜ (by omega)⟩)

end EG617
