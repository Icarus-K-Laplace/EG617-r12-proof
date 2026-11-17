module

public import EG617.Core.OddCycleBound

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
open SimpleGraph SimpleGraph.Walk
universe u
variable {V : Type u} [Fintype V]

theorem not_two_colorable_of_independence_bound (G : SimpleGraph V) (a : ℕ)
    (hI : CoreIndependenceBound a G) (hV : 2 * a < Fintype.card V) :
    ¬ G.Colorable 2 := by
  classical
  rintro ⟨C⟩
  let A := (Finset.univ : Finset V).filter (fun v => C v = 0)
  let B := (Finset.univ : Finset V).filter (fun v => C v = 1)
  have hA : A.card ≤ a := by
    apply hI A
    intro x hx y hy _
    exact C.not_adj_of_mem_colorClass (Finset.mem_filter.mp hx).2
      (Finset.mem_filter.mp hy).2
  have hB : B.card ≤ a := by
    apply hI B
    intro x hx y hy _
    exact C.not_adj_of_mem_colorClass (Finset.mem_filter.mp hx).2
      (Finset.mem_filter.mp hy).2
  have hu : A ∪ B = Finset.univ := by
    ext v
    simp only [A, B, Finset.mem_union, Finset.mem_filter,
      Finset.mem_univ, true_and, iff_true]
    exact (by decide : ∀ i : Fin 2, i = 0 ∨ i = 1) (C v)
  have hcard := Finset.card_union_le A B
  rw [hu, Finset.card_univ] at hcard
  omega

theorem r23_shortestOddLoop_length_five (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (he : 121 ≤ G.edgeFinset.card) {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) : p.length = 5 := by
  classical
  obtain ⟨k, hk⟩ := hp.1
  have hlen : p.length = 2 * k + 1 := by omega
  have hk2 := shortestOddLoop_half_length_ge_two G ht p hp k hlen
  have hfit := Finset.card_le_univ p.support.toFinset
  rw [cycle_support_card p (shortestOddLoop_isCycle p hp), hlen, hV] at hfit
  have hb := shortestOddLoop_edge_bound G ht p hp k hlen
  rw [hV] at hb
  have hknot : ¬ 3 ≤ k := by
    intro hk3
    have hmax := oddCycleBound_23_ge_three k hk3 hfit
    omega
  omega

/-- The first structural reduction of the 23-point classification. This does
not yet assert the complete bipartite exterior's three near-extremal forms. -/
theorem r23_exists_five_cycle_bipartite_exterior (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ v, ∃ p : G.Walk v v, IsShortestOddLoop p ∧ p.IsCycle ∧
      p.IsChordless ∧ p.length = 5 ∧
      p.support.toFinsetᶜ.card = 18 ∧
      80 ≤ coreInducedEdgeCount G p.support.toFinsetᶜ ∧
      (G.induce ((p.support.toFinsetᶜ : Finset V) : Set V)).Colorable 2 := by
  classical
  have hn := not_two_colorable_of_independence_bound G 11 hI (by omega)
  obtain ⟨v, p, hp⟩ := exists_shortestOddLoop hn
  have hc := shortestOddLoop_isCycle p hp
  have hh := shortestOddLoop_isChordless p hp
  have h5 := r23_shortestOddLoop_length_five G hV ht he p hp
  let S := p.support.toFinset
  have hs : S.card = 5 := (cycle_support_card p hc).trans h5
  have hsum : S.card + Sᶜ.card = Fintype.card V := by
    simpa using Finset.card_add_card_compl S
  have hx : Sᶜ.card = 18 := by omega
  have hcross : adjCount G S Sᶜ ≤ 36 := by
    rw [adjCount_symm, adjCount_eq_sum_filter]
    calc
      _ ≤ ∑ _x ∈ Sᶜ, 2 := Finset.sum_le_sum (fun x _ =>
        shortestOddLoop_neighbor_card_le p hp ht 2 h5 x)
      _ = 36 := by simp [hx]
  have hedge : coreInducedEdgeCount G S = 5 :=
    (chordless_cycle_induced_edges p hc hh).trans h5
  have hpart := edge_partition G S
  have hout : 80 ≤ coreInducedEdgeCount G Sᶜ := by omega
  refine ⟨v, p, hp, hc, hh, h5, hx, hout, ?_⟩
  by_contra hb
  have hti : (G.induce ((Sᶜ : Finset V) : Set V)).CliqueFree 3 :=
    ht.comap (SimpleGraph.Embedding.induce (G := G) ((Sᶜ : Finset V) : Set V)).isContained
  have hsmall := triangleFree_nonbipartite_18_edges_le_73
    (G.induce ((Sᶜ : Finset V) : Set V))
    (by simpa only [Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using hx) hti hb
  have hhsmall : coreInducedEdgeCount G Sᶜ ≤ 73 := by
    simpa only [coreInducedEdgeCount, SimpleGraph.edgeFinset_card,
      Set.fintypeCard_eq_ncard] using hsmall
  omega

end EG617
