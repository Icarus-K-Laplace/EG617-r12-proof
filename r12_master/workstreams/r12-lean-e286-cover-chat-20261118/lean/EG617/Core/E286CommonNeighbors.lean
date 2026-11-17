module
public import EG617.Core.E286Capacity

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Frozen E286 (1), with the actual common neighborhood and the original
five hypotheses. The obsolete constant9 is not assumed or used. -/
theorem e286_common_neighbors_excess_bound (G : SimpleGraph V)
    (hG : E286Hypotheses G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y) :
    (G.neighborFinset x ∩ G.neighborFinset y).card ≤
      3 + degreeExcess12 G x + degreeExcess12 G y := by
  classical
  let A := G.neighborFinset x
  let B := G.neighborFinset y
  let P : Finset V := {x, y}
  let U := A ∪ B
  let N := (P ∪ U)ᶜ
  have hN : ∀ z ∈ N, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z := by
    intro z hz
    have hn : z ∉ P ∪ U := Finset.mem_compl.mp hz
    refine ⟨?_, ?_, ?_, ?_⟩
    · intro he
      subst z
      exact hn (Finset.mem_union_left _ (by simp [P]))
    · intro he
      subst z
      exact hn (Finset.mem_union_left _ (by simp [P]))
    · intro hadj
      exact hn (Finset.mem_union_right _ (Finset.mem_union_left _
        ((SimpleGraph.mem_neighborFinset G x z).mpr hadj)))
    · intro hadj
      exact hn (Finset.mem_union_right _ (Finset.mem_union_right _
        ((SimpleGraph.mem_neighborFinset G y z).mpr hadj)))
  have hn := e286_common_antineighborhood_card_le_24 G hG x y hxy hnxy N hN
  have hd : Disjoint P U := by
    rw [Finset.disjoint_left]
    intro z hz hzU
    rcases Finset.mem_insert.mp hz with rfl | hz
    · rcases Finset.mem_union.mp hzU with h | h
      · exact G.loopless.irrefl x ((SimpleGraph.mem_neighborFinset G x x).mp h)
      · exact hnxy ((SimpleGraph.mem_neighborFinset G y x).mp h).symm
    · have he : z = y := Finset.mem_singleton.mp hz
      subst z
      rcases Finset.mem_union.mp hzU with h | h
      · exact hnxy ((SimpleGraph.mem_neighborFinset G x y).mp h)
      · exact G.loopless.irrefl y ((SimpleGraph.mem_neighborFinset G y y).mp h)
  have hp : P.card = 2 := by simp [P, hxy]
  have hcover := Finset.card_add_card_compl (P ∪ U)
  rw [Finset.card_union_of_disjoint hd, hp, hG.1] at hcover
  have hu := Finset.card_union_add_card_inter A B
  have hx := hG.2.2.1 x
  have hy := hG.2.2.1 y
  change N.card ≤ 24 at hn
  change 2 + U.card + N.card = 47 at hcover
  change (A ∩ B).card ≤ 3 + degreeExcess12 G x + degreeExcess12 G y
  simp only [A, B, SimpleGraph.card_neighborFinset_eq_degree,
    ← SimpleGraph.ncard_neighborSet] at hu
  simp only [degreeExcess12, ← SimpleGraph.ncard_neighborSet] at hx hy ⊢
  change U.card + (A ∩ B).card = (G.neighborSet x).ncard + (G.neighborSet y).ncard at hu
  omega

theorem e286_pair_excess_le_eight (G : SimpleGraph V) (hG : E286Hypotheses G)
    (x y : V) (hxy : x ≠ y) :
    degreeExcess12 G x + degreeExcess12 G y ≤ 8 := by
  classical
  have h : (∑ v ∈ ({x, y} : Finset V), degreeExcess12 G v) ≤
      ∑ v : V, degreeExcess12 G v :=
    Finset.sum_le_sum_of_subset (Finset.subset_univ _)
  rw [Finset.sum_pair hxy, e286_excess_sum G hG] at h
  exact h

theorem e286_common_neighbors_le_eleven (G : SimpleGraph V)
    (hG : E286Hypotheses G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y) :
    (G.neighborFinset x ∩ G.neighborFinset y).card ≤ 11 := by
  have hc := e286_common_neighbors_excess_bound G hG x y hxy hnxy
  have he := e286_pair_excess_le_eight G hG x y hxy
  omega

/-- Any specified common-neighbor set yields a local excess charge. -/
theorem e286_common_set_excess_charge (G : SimpleGraph V)
    (hG : E286Hypotheses G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y)
    (K : Finset V) (hK : ∀ z ∈ K, G.Adj x z ∧ G.Adj y z) :
    K.card ≤ 3 + degreeExcess12 G x + degreeExcess12 G y := by
  have hsub : K ⊆ G.neighborFinset x ∩ G.neighborFinset y := by
    intro z hz
    exact Finset.mem_inter.mpr ⟨(SimpleGraph.mem_neighborFinset G x z).mpr (hK z hz).1,
      (SimpleGraph.mem_neighborFinset G y z).mpr (hK z hz).2⟩
  exact (Finset.card_le_card hsub).trans
    (e286_common_neighbors_excess_bound G hG x y hxy hnxy)

/-- Two exterior completers of an actual K10 cannot be adjacent; their
combined excess is at least7. All disjointness conditions are explicit. -/
theorem e286_ten_clique_completers_excess (G : SimpleGraph V)
    (hG : E286Hypotheses G) (K : Finset V) (hcard : K.card = 10)
    (hcl : G.IsClique (K : Set V)) (x y : V) (hxy : x ≠ y)
    (hx : x ∉ K) (hy : y ∉ K)
    (hadj : ∀ z ∈ K, G.Adj x z ∧ G.Adj y z) :
    ¬ G.Adj x y ∧ 7 ≤ degreeExcess12 G x + degreeExcess12 G y := by
  classical
  have hn : ¬ G.Adj x y := by
    intro hxyadj
    have hKy : G.IsClique ((insert y K : Finset V) : Set V) := by
      rw [Finset.coe_insert]
      exact hcl.insert (fun z hz _ => (hadj z hz).2)
    have hKxy : G.IsClique ((insert x (insert y K) : Finset V) : Set V) := by
      rw [Finset.coe_insert]
      apply hKy.insert
      intro z hz _
      rcases Finset.mem_insert.mp hz with rfl | hz
      · exact hxyadj
      · exact (hadj z hz).1
    have hb := hG.2.2.2.2 (insert x (insert y K)) hKxy
    have hx' : x ∉ insert y K := by simp [hxy, hx]
    rw [Finset.card_insert_of_notMem hx', Finset.card_insert_of_notMem hy, hcard] at hb
    omega
  refine ⟨hn, ?_⟩
  have hc := e286_common_set_excess_charge G hG x y hxy hn K hadj
  rw [hcard] at hc
  omega

end EG617

