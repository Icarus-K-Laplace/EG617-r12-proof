module

public import EG617.Core.R224
public import Mathlib.Algebra.BigOperators.Ring.Finset

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Ordered incidences from S to T; internal edges are counted twice. -/
noncomputable def adjCount (G : SimpleGraph V) (S T : Finset V) : ℕ :=
  ∑ x ∈ S, ∑ y ∈ T, if G.Adj x y then 1 else 0

theorem adjCount_eq_sum_filter (G : SimpleGraph V) (S T : Finset V) :
    adjCount G S T = ∑ x ∈ S, (T.filter (G.Adj x)).card := by
  classical
  simp [adjCount]

theorem degree_induce_eq_filter (G : SimpleGraph V) (S : Finset V) (x : S) :
    (G.induce (S : Set V)).degree x = (S.filter (G.Adj x)).card := by
  classical
  have h := congrArg Finset.card
    (SimpleGraph.map_neighborFinset_induce (G := G) (s := (S : Set V)) x)
  have he : G.neighborFinset x ∩ S = S.filter (G.Adj x) := by
    ext y
    simp [and_comm]
  simpa only [Finset.card_map, SimpleGraph.card_neighborFinset_eq_degree,
    Set.toFinset_coe, he] using h

theorem adjCount_self (G : SimpleGraph V) (S : Finset V) :
    adjCount G S S = 2 * coreInducedEdgeCount G S := by
  classical
  rw [adjCount_eq_sum_filter, ← Finset.sum_coe_sort S]
  calc
    _ = ∑ x : S, (G.induce (S : Set V)).degree x := by
      apply Finset.sum_congr rfl
      intro x _
      exact (degree_induce_eq_filter G S x).symm
    _ = 2 * coreInducedEdgeCount G S :=
      (G.induce (S : Set V)).sum_degrees_eq_twice_card_edges

theorem adjCount_symm (G : SimpleGraph V) (S T : Finset V) :
    adjCount G S T = adjCount G T S := by
  classical
  unfold adjCount
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro y _
  apply Finset.sum_congr rfl
  intro x _
  by_cases h : G.Adj x y <;> simp [h, G.adj_comm]

theorem adjCount_union_left (G : SimpleGraph V) (S T U : Finset V)
    (hd : Disjoint S T) : adjCount G (S ∪ T) U = adjCount G S U + adjCount G T U := by
  classical
  exact Finset.sum_union hd

theorem adjCount_union_right (G : SimpleGraph V) (S T U : Finset V)
    (hd : Disjoint T U) : adjCount G S (T ∪ U) = adjCount G S T + adjCount G S U := by
  classical
  simp only [adjCount, Finset.sum_union hd, Finset.sum_add_distrib]

/-- Exact unordered edge ledger: inside S, across the cut, inside its complement. -/
theorem edge_partition (G : SimpleGraph V) (S : Finset V) :
    G.edgeFinset.card = coreInducedEdgeCount G S + adjCount G S Sᶜ +
      coreInducedEdgeCount G Sᶜ := by
  classical
  have h := adjCount_union_left G S Sᶜ Finset.univ disjoint_compl_right
  have hS := adjCount_union_right G S S Sᶜ disjoint_compl_right
  have hT := adjCount_union_right G Sᶜ S Sᶜ disjoint_compl_right
  simp only [Finset.union_compl] at h hS hT
  rw [adjCount_symm G Sᶜ S] at hT
  have hs := adjCount_self G S
  have ht := adjCount_self G Sᶜ
  have hu := adjCount_self G Finset.univ
  rw [core_induced_edge_count_univ] at hu
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at hu ⊢
  omega

theorem adjCount_right_univ (G : SimpleGraph V) (S : Finset V) :
    adjCount G S Finset.univ = ∑ x ∈ S, G.degree x := by
  classical
  rw [adjCount_eq_sum_filter]
  apply Finset.sum_congr rfl
  intro x _
  have he : (Finset.univ.filter (G.Adj x)) = G.neighborFinset x := by
    ext y
    simp
  rw [he, SimpleGraph.card_neighborFinset_eq_degree]

theorem adjCount_le_sum_degrees (G : SimpleGraph V) (S T : Finset V) :
    adjCount G S T ≤ ∑ x ∈ S, G.degree x := by
  classical
  rw [adjCount_eq_sum_filter]
  apply Finset.sum_le_sum
  intro x _
  rw [← SimpleGraph.card_neighborFinset_eq_degree]
  apply Finset.card_le_card
  intro y hy
  exact (SimpleGraph.mem_neighborFinset G x y).mpr (Finset.mem_filter.mp hy).2

theorem adjCount_independent_zero (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) : adjCount G I I = 0 := by
  classical
  apply Finset.sum_eq_zero
  intro x hx
  apply Finset.sum_eq_zero
  intro y hy
  have hn : ¬ G.Adj x y := by
    by_cases hxy : x = y
    · subst y; exact G.loopless.irrefl x
    · exact hI hx hy hxy
  simp [hn]

/-- The independence bound of any finite two-regular graph. -/
theorem twice_independent_card_le_of_degree_two (G : SimpleGraph V)
    (hd : ∀ v, G.degree v = 2) (I : Finset V) (hI : G.IsIndepSet (I : Set V)) :
    2 * I.card ≤ Fintype.card V := by
  classical
  have hsplit := adjCount_union_right G I I Iᶜ disjoint_compl_right
  simp only [Finset.union_compl, adjCount_independent_zero G I hI, zero_add] at hsplit
  have hIall := adjCount_right_univ G I
  have hother := adjCount_le_sum_degrees G Iᶜ I
  simp only [hd, Finset.sum_const, smul_eq_mul] at hIall hother
  rw [adjCount_symm G Iᶜ I] at hother
  have hcard : I.card + Iᶜ.card = Fintype.card V := by
    simpa only [Finset.card_univ] using Finset.card_add_card_compl I
  omega

end EG617
