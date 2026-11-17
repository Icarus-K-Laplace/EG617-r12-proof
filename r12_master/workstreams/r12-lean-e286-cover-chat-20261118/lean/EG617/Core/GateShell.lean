module
public import EG617.Core.R336Sharp

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Exact frozen M6 shell ledger, with no assumption that the shell is a clique. -/
theorem core_shell_edge_degree_ledger (G : SimpleGraph V) (v : V) :
    let S := G.neighborFinset v
    let C := Gᶜ.neighborFinset v
    G.edgeFinset.card = coreInducedEdgeCount G C + G.degree v +
      coreInducedEdgeCount G S + adjCount G S C ∧
    (∑ a ∈ S, G.degree a) = G.degree v + 2 * coreInducedEdgeCount G S + adjCount G S C := by
  classical
  let S := G.neighborFinset v
  let C := Gᶜ.neighborFinset v
  have hvS : v ∉ S := by simp [S]
  have hvC : v ∉ C := by simp [C]
  have hdvS : Disjoint ({v} : Finset V) S := by simpa using hvS
  have hdSC : Disjoint S C := by
    rw [Finset.disjoint_left]
    intro a ha hb
    have hna := (SimpleGraph.compl_adj G v a).mp ((SimpleGraph.mem_neighborFinset Gᶜ v a).mp hb)
    exact hna.2 ((SimpleGraph.mem_neighborFinset G v a).mp ha)
  have hdAC : Disjoint (({v} : Finset V) ∪ S) C :=
    Finset.disjoint_union_left.mpr ⟨by simpa using hvC, hdSC⟩
  have hcover : (({v} : Finset V) ∪ S) ∪ C = Finset.univ := by
    ext a
    by_cases hav : a = v
    · subst a
      simp
    · by_cases ha : G.Adj v a <;> simp [S, C, hav, ha, SimpleGraph.compl_adj, Ne.symm hav]
  have hvs : adjCount G {v} S = G.degree v := by
    have h : ∀ a ∈ S, G.Adj v a := fun a ha => (SimpleGraph.mem_neighborFinset G v a).mp ha
    rw [adjCount_eq_sum_filter, Finset.sum_singleton, Finset.filter_eq_self.mpr h]
    simp only [S, SimpleGraph.card_neighborFinset_eq_degree, ← SimpleGraph.ncard_neighborSet]
  have hvc : adjCount G {v} C = 0 := by
    have h : ∀ a ∈ C, ¬ G.Adj v a := fun a ha =>
      ((SimpleGraph.compl_adj G v a).mp ((SimpleGraph.mem_neighborFinset Gᶜ v a).mp ha)).2
    rw [adjCount_eq_sum_filter, Finset.sum_singleton]
    apply Finset.card_eq_zero.mpr
    apply Finset.eq_empty_iff_forall_notMem.mpr
    intro a ha
    exact h a (Finset.mem_filter.mp ha).1 (Finset.mem_filter.mp ha).2
  have hvv : coreInducedEdgeCount G {v} = 0 := by
    have hc := adjCount_self G ({v} : Finset V)
    have hz : adjCount G ({v} : Finset V) {v} = 0 := by simp [adjCount]
    rw [hz] at hc
    simp only [coreInducedEdgeCount, SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at hc ⊢
    omega
  have hA := core_edge_count_union G {v} S hdvS
  rw [hvs, hvv, zero_add] at hA
  have hAC := core_edge_count_union G ({v} ∪ S) C hdAC
  rw [hcover, core_induced_edge_count_univ, hA,
    adjCount_union_left G {v} S C hdvS, hvc, zero_add] at hAC
  have hdeg := adjCount_union_right G S ({v} ∪ S) C hdAC
  rw [hcover, adjCount_right_univ,
    adjCount_union_right G S {v} S hdvS,
    adjCount_symm G S {v}, hvs, adjCount_self G S] at hdeg
  simp only [S, C, SimpleGraph.neighborFinset_def, ← Set.toFinite_toFinset,
    ← SimpleGraph.ncard_neighborSet, SimpleGraph.edgeFinset_card,
    Set.fintypeCard_eq_ncard] at hAC hdeg ⊢
  exact ⟨by omega, hdeg⟩

theorem core_induced_edges_le_choose (G : SimpleGraph V) (S : Finset V) :
    coreInducedEdgeCount G S ≤ S.card.choose 2 := by
  classical
  have h := (G.induce (S : Set V)).card_edgeFinset_le_card_choose_two
  simpa only [coreInducedEdgeCount, SimpleGraph.edgeFinset_card,
    Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using h

/-- Frozen M6 d=10 exclusion with the original full admissibility contract. -/
theorem core_R447_min_degree_ten_edges_ge_289 (G : SimpleGraph V)
    (hV : Fintype.card V = 47) (hG : CoreAdmissible 4 G) (v : V)
    (hd : G.degree v = 10) (hmin : ∀ w, 10 ≤ G.degree w) :
    289 ≤ G.edgeFinset.card := by
  classical
  let S := G.neighborFinset v
  let C := Gᶜ.neighborFinset v
  have hS : S.card = 10 := by
    simpa only [S, SimpleGraph.card_neighborFinset_eq_degree, ← SimpleGraph.ncard_neighborSet] using hd
  have hC : C.card = 36 := by
    have hc : C.card = Fintype.card V - 1 - G.degree v := G.degree_compl v
    omega
  have ha : CoreAdmissible 3 (G.induce (C : Set V)) :=
    core_admissible_nonNeighbors G 3 hG v C (by
      intro w hw
      have h := (SimpleGraph.mem_neighborFinset Gᶜ v w).mp hw
      exact ⟨h.ne.symm, ((SimpleGraph.compl_adj G v w).mp h).2⟩)
  have heC := core_R336_edges_ge_234 (G.induce (C : Set V))
    (by simpa only [Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using hC) ha
  change 234 ≤ coreInducedEdgeCount G C at heC
  obtain ⟨he, hs⟩ := core_shell_edge_degree_ledger G v
  have hsum : ∑ a ∈ S, 10 ≤ ∑ a ∈ S, G.degree a := Finset.sum_le_sum (fun a _ => hmin a)
  simp only [Finset.sum_const, smul_eq_mul, hS] at hsum
  have hsmall := core_induced_edges_le_choose G S
  rw [hS] at hsmall
  norm_num only [Nat.choose_two_right] at hsmall
  simp only [S, C, SimpleGraph.neighborFinset_def, ← Set.toFinite_toFinset,
    ← SimpleGraph.ncard_neighborSet, SimpleGraph.edgeFinset_card,
    Set.fintypeCard_eq_ncard] at he hs heC hsum hsmall hd ⊢
  omega

end EG617
