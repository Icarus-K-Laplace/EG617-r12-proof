module
public import EG617.Core.GateRows

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Frozen M6: minimum degree11 forces at least287 edges. Every row, missing
shell edge, and exterior graph below is constructed from the given graph. -/
theorem core_R447_min_degree_eleven_edges_ge_287 (G : SimpleGraph V)
    (hV : Fintype.card V = 47) (hG : CoreAdmissible 4 G) (v : V)
    (hd : G.degree v = 11) (hmin : ∀ w, 11 ≤ G.degree w) :
    287 ≤ G.edgeFinset.card := by
  classical
  let S := G.neighborFinset v
  let C := Gᶜ.neighborFinset v
  let M := (G.induce (S : Set V))ᶜ
  let r : (S : Set V) → ℕ := fun a => (C.filter (G.Adj a)).card
  have hS : S.card = 11 := by
    simpa only [S, SimpleGraph.card_neighborFinset_eq_degree, ← SimpleGraph.ncard_neighborSet] using hd
  have hC : C.card = 35 := by
    have hc : C.card = Fintype.card V - 1 - G.degree v := G.degree_compl v
    omega
  have ha : CoreAdmissible 3 (G.induce (C : Set V)) :=
    core_admissible_nonNeighbors G 3 hG v C (by
      intro w hw
      have h := (SimpleGraph.mem_neighborFinset Gᶜ v w).mp hw
      exact ⟨h.ne.symm, ((SimpleGraph.compl_adj G v w).mp h).2⟩)
  have heC : 210 ≤ coreInducedEdgeCount G C := by
    have h := core_R335_edges_ge_210 (G.induce (C : Set V))
      (by simpa only [Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using hC) ha
    simpa only [coreInducedEdgeCount, SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] using h
  obtain ⟨x, hx, y, hy, hxy, hnxy⟩ := core_degree_eleven_neighbor_nonedge G hG.2.1 v hd
  have hSC : Disjoint S C := by
    rw [Finset.disjoint_left]
    intro z hz hzC
    exact ((SimpleGraph.compl_adj G v z).mp
      ((SimpleGraph.mem_neighborFinset Gᶜ v z).mp hzC)).2
      ((SimpleGraph.mem_neighborFinset G v z).mp hz)
  have hxC : x ∉ C := fun hxC => Finset.disjoint_left.mp hSC hx hxC
  have hyC : y ∉ C := fun hyC => Finset.disjoint_left.mp hSC hy hyC
  have hrow : ∀ a, M.degree a ≤ r a := fun a => core_shell_row_missing_degree_le G v hd hmin a
  have hpair : 12 ≤ r ⟨x, hx⟩ + r ⟨y, hy⟩ := by
    have hu := core_R4_row_union_ge_twelve G hG C hC x y hxy hnxy hxC hyC
    have hc := Finset.card_union_le (C.filter (G.Adj x)) (C.filter (G.Adj y))
    exact hu.trans hc
  have hrows := core_missing_edge_row_sum M r hrow ⟨x, hx⟩ ⟨y, hy⟩
    (fun he => hxy (congrArg Subtype.val he)) hpair
  have hcross : (∑ a : (S : Set V), r a) = adjCount G S C := by
    rw [adjCount_eq_sum_filter, ← Finset.sum_coe_sort S]
  rw [hcross] at hrows
  have hcomp := core_compl_edge_count (G.induce (S : Set V))
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard,
    Set.ncard_coe_finset, hS] at hcomp
  norm_num only [Nat.choose_two_right] at hcomp
  have he := (core_shell_edge_degree_ledger G v).1
  dsimp only [M] at hrows
  simp only [S, C, SimpleGraph.neighborFinset_def, ← Set.toFinite_toFinset,
    ← SimpleGraph.ncard_neighborSet, coreInducedEdgeCount, SimpleGraph.edgeFinset_card,
    Set.fintypeCard_eq_ncard] at he heC hrows hcomp hd ⊢
  omega

/-- The original frozen GATE47 statement, retaining alpha, omega, ALL induced
D caps and the286-edge premise. This does not assert the EG617 main theorem. -/
theorem gate47_verified : Gate47Statement := by
  classical
  intro G hG hedge
  obtain ⟨v, hv⟩ := G.exists_minimal_degree_vertex
  have hmin : ∀ w, G.degree v ≤ G.degree w := by
    intro w
    rw [← hv]
    exact G.minDegree_le_degree w
  have h10 := core_R447_degree_ge_10 G hG v
  have h12 : 12 ≤ G.degree v := by
    by_contra hn
    have hc : G.degree v = 10 ∨ G.degree v = 11 := by omega
    rcases hc with hd | hd
    · have he := core_R447_min_degree_ten_edges_ge_289 G rfl hG v hd
        (fun w => hd ▸ hmin w)
      omega
    · have he := core_R447_min_degree_eleven_edges_ge_287 G rfl hG v hd
        (fun w => hd ▸ hmin w)
      omega
  intro w
  exact h12.trans (hmin w)

end EG617
