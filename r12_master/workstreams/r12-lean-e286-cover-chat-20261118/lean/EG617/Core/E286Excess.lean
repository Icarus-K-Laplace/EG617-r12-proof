module
public import EG617.Core.Gate47

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- The five hypotheses of frozen Theorem E286. In particular, no hereditary
density cap is added to this abstract graph theorem. -/
def E286Hypotheses (G : SimpleGraph V) : Prop :=
  Fintype.card V = 47 ∧ G.edgeFinset.card = 286 ∧
    (∀ v, 12 ≤ G.degree v) ∧ CoreIndependenceBound 4 G ∧ CoreCliqueBound 11 G

/-- The original abstract equality exclusion is a target, not a proved theorem. -/
def E286Statement : Prop :=
  ¬ ∃ G : SimpleGraph (Fin 47), E286Hypotheses G

noncomputable def degreeExcess12 (G : SimpleGraph V) (v : V) : ℕ :=
  G.degree v - 12

noncomputable def excessSupport (G : SimpleGraph V) : Finset V :=
  Finset.univ.filter (fun v => 0 < degreeExcess12 G v)

/-- Exact degree sum, before any support or orbit reduction. -/
theorem e286_degree_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v : V, G.degree v = 572 := by
  have h := G.sum_degrees_eq_twice_card_edges
  have he := hG.2.1
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at h he
  omega

theorem e286_excess_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v : V, degreeExcess12 G v = 8 := by
  classical
  have hid : (∑ v : V, degreeExcess12 G v) + ∑ _v : V, 12 =
      ∑ v : V, G.degree v := by
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro v _
    have hd := hG.2.2.1 v
    simp only [degreeExcess12, ← SimpleGraph.ncard_neighborSet] at hd ⊢
    omega
  have hs := e286_degree_sum G hG
  simp only [Finset.sum_const, Finset.card_univ, smul_eq_mul, hG.1] at hid
  omega

theorem e286_support_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v ∈ excessSupport G, degreeExcess12 G v = 8 := by
  classical
  have he : (∑ v ∈ excessSupport G, degreeExcess12 G v) =
      ∑ v : V, degreeExcess12 G v := by
    apply Finset.sum_subset (Finset.subset_univ _)
    intro v _ hv
    have hn : ¬ 0 < degreeExcess12 G v := by
      simpa only [excessSupport, Finset.mem_filter, Finset.mem_univ, true_and] using hv
    omega
  exact he.trans (e286_excess_sum G hG)

theorem e286_support_card_le_eight (G : SimpleGraph V) (hG : E286Hypotheses G) :
    (excessSupport G).card ≤ 8 := by
  classical
  have h : (excessSupport G).card ≤
      ∑ v ∈ excessSupport G, degreeExcess12 G v := by
    calc
      _ = ∑ _v ∈ excessSupport G, 1 := by simp
      _ ≤ _ := Finset.sum_le_sum (fun v hv => by
        have hp := (Finset.mem_filter.mp hv).2
        omega)
  rw [e286_support_sum G hG] at h
  exact h

theorem e286_degree_le_twenty (G : SimpleGraph V) (hG : E286Hypotheses G) (v : V) :
    G.degree v ≤ 20 := by
  have hle : degreeExcess12 G v ≤ ∑ w : V, degreeExcess12 G w :=
    Finset.single_le_sum (fun w _ => Nat.zero_le _) (Finset.mem_univ v)
  rw [e286_excess_sum G hG] at hle
  simp only [degreeExcess12, ← SimpleGraph.ncard_neighborSet] at hle ⊢
  omega

theorem e286_regular_complement (G : SimpleGraph V) (hG : E286Hypotheses G) :
    (excessSupport G)ᶜ = Finset.univ.filter (fun v => G.degree v = 12) := by
  classical
  ext v
  have hd := hG.2.2.1 v
  simp only [Finset.mem_compl, excessSupport, Finset.mem_filter, Finset.mem_univ,
    true_and, degreeExcess12, ← SimpleGraph.ncard_neighborSet] at hd ⊢
  omega

theorem e286_regular_card_ge_39 (G : SimpleGraph V) (hG : E286Hypotheses G) :
    39 ≤ (Finset.univ.filter (fun v => G.degree v = 12)).card := by
  classical
  have hc := Finset.card_add_card_compl (excessSupport G)
  simp only [Finset.card_univ, hG.1, e286_regular_complement G hG] at hc
  have hs := e286_support_card_le_eight G hG
  omega

/-- The exceptional degree sum is exactly 12q+8, not merely bounded by it. -/
theorem e286_support_degree_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v ∈ excessSupport G, G.degree v = 12 * (excessSupport G).card + 8 := by
  classical
  have hi : (∑ v ∈ excessSupport G, degreeExcess12 G v) +
      ∑ _v ∈ excessSupport G, 12 = ∑ v ∈ excessSupport G, G.degree v := by
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro v _
    have hd := hG.2.2.1 v
    simp only [degreeExcess12, ← SimpleGraph.ncard_neighborSet] at hd ⊢
    omega
  rw [e286_support_sum G hG] at hi
  simp only [Finset.sum_const, smul_eq_mul] at hi
  omega

/-- Exact edge ledger needed to find the four regular independent seeds. -/
theorem e286_regular_edge_ledger (G : SimpleGraph V) (hG : E286Hypotheses G) :
    coreInducedEdgeCount G (excessSupport G)ᶜ + 12 * (excessSupport G).card + 8 =
      286 + coreInducedEdgeCount G (excessSupport G) := by
  classical
  let S := excessSupport G
  have hp := edge_partition G S
  have hs := adjCount_union_right G S S Sᶜ disjoint_compl_right
  rw [Finset.union_compl, adjCount_right_univ, adjCount_self] at hs
  have hd := e286_support_degree_sum G hG
  have he := hG.2.1
  simp only [S, SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at hp hs he
  omega

end EG617

