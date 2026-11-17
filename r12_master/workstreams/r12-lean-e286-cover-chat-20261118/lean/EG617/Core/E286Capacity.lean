module
public import EG617.Core.E286Seeds

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- The full excess budget controls every actual induced vertex set, without
assuming a hereditary density cap. -/
theorem e286_induced_degree_budget (G : SimpleGraph V) (hG : E286Hypotheses G)
    (S : Finset V) :
    2 * coreInducedEdgeCount G S ≤ 12 * S.card + 8 := by
  classical
  have hx : (∑ v ∈ S, degreeExcess12 G v) ≤ 8 := by
    calc
      _ ≤ ∑ v : V, degreeExcess12 G v :=
        Finset.sum_le_sum_of_subset (Finset.subset_univ S)
      _ = 8 := e286_excess_sum G hG
  have hs : (∑ v ∈ S, degreeExcess12 G v) + ∑ _v ∈ S, 12 =
      ∑ v ∈ S, G.degree v := by
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro v _
    have hd := hG.2.2.1 v
    simp only [degreeExcess12, ← SimpleGraph.ncard_neighborSet] at hd ⊢
    omega
  simp only [Finset.sum_const, smul_eq_mul] at hs
  have he := adjCount_le_sum_degrees G S S
  rw [adjCount_self] at he
  omega

theorem oddCycleBound_25 (k : ℕ) (hk : 2 ≤ k) (hfit : 2 * k + 1 ≤ 25) :
    oddCycleBound 25 k ≤ 145 := by
  have : k ≤ 12 := by omega
  interval_cases k <;> norm_num [oddCycleBound]

/-- Frozen E286 Section1: the25-point alpha2/omega11 lower bound is abstract;
no inherited D cap or unformalized common-neighborhood result is used. -/
theorem alpha_two_25_edges_ge_155 (G : SimpleGraph V)
    (hV : Fintype.card V = 25) (hI : CoreIndependenceBound 2 G)
    (hK : CoreCliqueBound 11 G) : 155 ≤ G.edgeFinset.card := by
  classical
  have ht : Gᶜ.CliqueFree 3 := by
    intro S hS
    have hi : G.IsNIndepSet 3 S := (SimpleGraph.isNClique_compl G).mp hS
    have hb := hI S hi.isIndepSet
    rw [hi.card_eq] at hb
    omega
  have hi : CoreIndependenceBound 11 Gᶜ := by
    intro S hS
    exact hK S ((SimpleGraph.isIndepSet_compl G).mp hS)
  have hn := not_two_colorable_of_independence_bound Gᶜ 11 hi (by omega)
  obtain ⟨k, hk, hfit, he⟩ := triangleFree_nonbipartite_edge_bound Gᶜ ht hn
  rw [hV] at hfit he
  have hb := he.trans (oddCycleBound_25 k hk hfit)
  have hc := core_compl_edge_count G
  rw [hV] at hc
  norm_num only [Nat.choose_two_right] at hc
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at hc hb ⊢
  omega

theorem e286_no_induced_alpha_two_25 (G : SimpleGraph V) (hG : E286Hypotheses G)
    (S : Finset V) (hS : S.card = 25)
    (hI : CoreIndependenceBound 2 (G.induce (S : Set V))) : False := by
  have hK := core_cliqueBound_induce G 11 hG.2.2.2.2 S
  have hl := alpha_two_25_edges_ge_155 (G.induce (S : Set V))
    (by simpa only [Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using hS) hI hK
  have hu := e286_induced_degree_budget G hG S
  rw [hS] at hu
  simp only [coreInducedEdgeCount, SimpleGraph.edgeFinset_card,
    Set.fintypeCard_eq_ncard] at hu hl
  omega

/-- Independence-only common-antineighborhood inheritance. The existing
CoreAdmissible version also assumes D caps, which E286 does not have. -/
theorem independenceBound_common_nonNeighbors (G : SimpleGraph V) (a : ℕ)
    (hG : CoreIndependenceBound (a + 2) G) (x y : V) (hxy : x ≠ y)
    (hnxy : ¬ G.Adj x y) (S : Finset V)
    (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    CoreIndependenceBound a (G.induce (S : Set V)) := by
  classical
  intro T hT
  let U := T.image (fun z : (S : Set V) => (z : V))
  have hUS : U ⊆ S := by
    intro z hz
    obtain ⟨b, _, rfl⟩ := Finset.mem_image.mp hz
    exact b.property
  have hU : G.IsIndepSet (U : Set V) := by
    intro b hb c hc hbc
    obtain ⟨b', hb', rfl⟩ := Finset.mem_image.mp hb
    obtain ⟨c', hc', rfl⟩ := Finset.mem_image.mp hc
    exact hT hb' hc' (fun he => hbc (congrArg Subtype.val he))
  have hyU : y ∉ U := fun hy => (hS y (hUS hy)).2.1 rfl
  have hi : G.IsIndepSet ((insert y U : Finset V) : Set V) := by
    intro b hb c hc hbc
    by_cases hby : b = y
    · subst b
      have hcU := Finset.mem_of_mem_insert_of_ne hc hbc.symm
      exact (hS c (hUS hcU)).2.2.2
    · have hbU := Finset.mem_of_mem_insert_of_ne hb hby
      by_cases hcy : c = y
      · subst c
        exact fun he => (hS b (hUS hbU)).2.2.2 he.symm
      · exact hU hbU (Finset.mem_of_mem_insert_of_ne hc hcy) hbc
  have hn : ∀ z ∈ insert y U, z ≠ x ∧ ¬ G.Adj x z := by
    intro z hz
    rcases Finset.mem_insert.mp hz with rfl | hz
    · exact ⟨hxy.symm, hnxy⟩
    · exact ⟨(hS z (hUS hz)).1, (hS z (hUS hz)).2.2.1⟩
  have hb := core_independence_nonNeighbors G (a + 1) hG x (insert y U) hn hi
  rw [Finset.card_insert_of_notMem hyU] at hb
  have hcard : U.card = T.card := Finset.card_image_of_injective _ Subtype.val_injective
  omega

theorem e286_common_antineighborhood_card_le_24 (G : SimpleGraph V)
    (hG : E286Hypotheses G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y)
    (S : Finset V)
    (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    S.card ≤ 24 := by
  classical
  by_contra hn
  obtain ⟨T, hTS, hT⟩ := Finset.exists_subset_card_eq (show 25 ≤ S.card by omega)
  have hI := independenceBound_common_nonNeighbors G 2 hG.2.2.2.1 x y hxy hnxy T
    (fun z hz => hS z (hTS hz))
  exact e286_no_induced_alpha_two_25 G hG T hT hI

end EG617

