module

public import EG617.Core.C5MissingEdge

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem deficit_sum_add (T : Finset V) (d : V → ℕ) (hd : ∀ v ∈ T, d v ≤ 2) :
    (∑ v ∈ T, (2 - d v)) + (∑ v ∈ T, d v) = 2 * T.card := by
  rw [← Finset.sum_add_distrib]
  calc
    _ = ∑ _v ∈ T, 2 := Finset.sum_congr rfl (fun v hv => Nat.sub_add_cancel (hd v hv))
    _ = _ := by simp [Nat.mul_comm]

theorem deficit_zero_iff (T : Finset V) (d : V → ℕ) (hd : ∀ v ∈ T, d v ≤ 2) :
    (∑ v ∈ T, (2 - d v)) = 0 ↔ ∀ v ∈ T, d v = 2 := by
  constructor
  · intro h v hv
    have hle : 2 - d v ≤ ∑ w ∈ T, (2 - d w) :=
      Finset.single_le_sum (f := fun w => 2 - d w) (fun w _ => Nat.zero_le _) hv
    have := hd v hv
    omega
  · intro h
    apply Finset.sum_eq_zero
    intro v hv
    simp [h v hv]

theorem deficit_one_distribution (T : Finset V) (d : V → ℕ)
    (hd : ∀ v ∈ T, d v ≤ 2) (h : (∑ v ∈ T, (2 - d v)) = 1) :
    ∃ v ∈ T, d v = 1 ∧ ∀ w ∈ T, w ≠ v → d w = 2 := by
  classical
  have hex : ∃ v ∈ T, d v ≠ 2 := by
    by_contra hn
    have hall : ∀ v ∈ T, d v = 2 := by simpa only [not_exists, not_and, not_not] using hn
    have hz := (deficit_zero_iff T d hd).mpr hall
    omega
  obtain ⟨v, hv, hne⟩ := hex
  have hle : 2 - d v ≤ ∑ w ∈ T, (2 - d w) :=
    Finset.single_le_sum (f := fun w => 2 - d w) (fun w _ => Nat.zero_le _) hv
  have hvd := hd v hv
  have h1 : d v = 1 := by omega
  have hs := Finset.sum_erase_add T (fun w => 2 - d w) hv
  have hz : (∑ w ∈ T.erase v, (2 - d w)) = 0 := by omega
  refine ⟨v, hv, h1, ?_⟩
  intro w hw hwv
  have hm : w ∈ T.erase v := Finset.mem_erase.mpr ⟨hwv, hw⟩
  have hb : 2 - d w ≤ ∑ z ∈ T.erase v, (2 - d z) :=
    Finset.single_le_sum (f := fun z => 2 - d z) (fun z _ => Nat.zero_le _) hm
  have := hd w hw
  omega

/-- All fields are conclusions. S is supplied as the support of a shortest C5
in r23_exact_neighbor_ledger, never as an assumed distribution. -/
def ExactC5NeighborLedger (G : SimpleGraph V) (S : Finset V) : Prop :=
  let T := Sᶜ
  let d := fun v => (S.filter (G.Adj v)).card
  let x := adjCount G S T
  let y := coreInducedEdgeCount G T
  S.card = 5 ∧ T.card = 18 ∧ coreInducedEdgeCount G S = 5 ∧
  (∀ v ∈ T, d v ≤ 2) ∧ 80 ≤ y ∧ y ≤ 81 ∧
  121 ≤ G.edgeFinset.card ∧ G.edgeFinset.card ≤ 122 ∧
  G.edgeFinset.card = 5 + x + y ∧ (x = 35 ∨ x = 36) ∧
  (∑ v ∈ T, (2 - d v)) = 36 - x ∧
  ((y = 80 ∧ x = 36 ∧ G.edgeFinset.card = 121 ∧ ∀ v ∈ T, d v = 2) ∨
   (y = 81 ∧ x = 35 ∧ G.edgeFinset.card = 121 ∧
     ∃ v ∈ T, d v = 1 ∧ ∀ w ∈ T, w ≠ v → d w = 2) ∨
   (y = 81 ∧ x = 36 ∧ G.edgeFinset.card = 122 ∧ ∀ v ∈ T, d v = 2)) ∧
  (x = 35 ↔ ∃! v, v ∈ T ∧ d v = 1)

/-- Exact 121/122 edge ledger and all three neighborhood distributions from the
original R23 hypotheses. No terminal classification or saturation assumption. -/
theorem r23_exact_neighbor_ledger (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ v, ∃ p : G.Walk v v, IsShortestOddLoop p ∧ p.IsCycle ∧ p.length = 5 ∧
      ExactC5NeighborLedger G p.support.toFinset := by
  classical
  obtain ⟨v, p, hp, hc, hh, h5, h18, h80, _⟩ :=
    r23_exists_five_cycle_bipartite_exterior G hV ht hI he
  let S := p.support.toFinset
  let T := Sᶜ
  let d := fun x => (S.filter (G.Adj x)).card
  let x := adjCount G S T
  let y := coreInducedEdgeCount G T
  have hS : S.card = 5 := (cycle_support_card p hc).trans h5
  have hT : T.card = 18 := h18
  have hC : coreInducedEdgeCount G S = 5 := (chordless_cycle_induced_edges p hc hh).trans h5
  have hd : ∀ w ∈ T, d w ≤ 2 := fun w _ => shortestOddLoop_neighbor_card_le p hp ht 2 h5 w
  have hsum : (∑ w ∈ T, d w) = x := by
    exact (adjCount_eq_sum_filter G T S).symm.trans (adjCount_symm G T S)
  have hxle : x ≤ 36 := by
    rw [← hsum]
    calc
      _ ≤ ∑ _w ∈ T, 2 := Finset.sum_le_sum hd
      _ = 36 := by simp [hT]
  have hylo : 80 ≤ y := h80
  have hyhi : y ≤ 81 := by
    have hm := triangleFree_induced_mantel G ht T
    norm_num [hT] at hm
    exact hm
  have hpart : G.edgeFinset.card = 5 + x + y := by
    have h := edge_partition G S
    rw [hC] at h
    exact h
  have hehi : G.edgeFinset.card ≤ 122 := by
    have h := shortestOddLoop_edge_bound G ht p hp 2 h5
    simpa only [hV, oddCycleBound_23_two] using h
  have hx : x = 35 ∨ x = 36 := by omega
  have hdef : (∑ w ∈ T, (2 - d w)) = 36 - x := by
    have h := deficit_sum_add T d hd
    rw [hsum, hT] at h
    omega
  have hall : x = 36 → ∀ w ∈ T, d w = 2 := by
    intro hx36
    apply (deficit_zero_iff T d hd).mp
    omega
  have hone : x = 35 → ∃ w ∈ T, d w = 1 ∧ ∀ z ∈ T, z ≠ w → d z = 2 := by
    intro hx35
    apply deficit_one_distribution T d hd
    omega
  refine ⟨v, p, hp, hc, h5, ?_⟩
  change S.card = 5 ∧ T.card = 18 ∧ coreInducedEdgeCount G S = 5 ∧
    (∀ w ∈ T, d w ≤ 2) ∧ 80 ≤ y ∧ y ≤ 81 ∧
    121 ≤ G.edgeFinset.card ∧ G.edgeFinset.card ≤ 122 ∧
    G.edgeFinset.card = 5 + x + y ∧ (x = 35 ∨ x = 36) ∧
    (∑ w ∈ T, (2 - d w)) = 36 - x ∧ _
  refine ⟨hS, hT, hC, hd, hylo, hyhi, he, hehi, hpart, hx, hdef, ?_, ?_⟩
  · by_cases hy80 : y = 80
    · have hx36 : x = 36 := by omega
      exact Or.inl ⟨hy80, hx36, by omega, hall hx36⟩
    · have hy81 : y = 81 := by omega
      rcases hx with hx35 | hx36
      · exact Or.inr (Or.inl ⟨hy81, hx35, by omega, hone hx35⟩)
      · exact Or.inr (Or.inr ⟨hy81, hx36, by omega, hall hx36⟩)
  · constructor
    · intro hx35
      obtain ⟨w, hw, hw1, hrest⟩ := hone hx35
      refine ⟨w, ⟨hw, hw1⟩, ?_⟩
      intro z hz
      by_contra hzw
      have hz1 : d z = 1 := hz.2
      have := hrest z hz.1 hzw
      omega
    · rintro ⟨w, hw, _⟩
      rcases hx with h35 | h36
      · exact h35
      · have hw1 : d w = 1 := hw.2
        have := hall h36 w hw.1
        omega

end EG617
