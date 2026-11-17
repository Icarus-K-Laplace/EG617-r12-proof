module
public import EG617.Core.R335Sharp

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Frozen M5: delete an actual neighbor and invoke the full R335 theorem on
the resulting 35-point induced graph, retaining all hereditary conditions. -/
theorem core_R336_degree_ge_thirteen (G : SimpleGraph V)
    (hV : Fintype.card V = 36) (hG : CoreAdmissible 3 G) (v : V) :
    13 ≤ G.degree v := by
  classical
  have hweak := core_R3_card_le_degree_add_24 G hG v
  have hpos : 0 < (G.neighborFinset v).card := by
    rw [SimpleGraph.card_neighborFinset_eq_degree]
    omega
  obtain ⟨w, hw⟩ := Finset.card_pos.mp hpos
  have hvw : G.Adj v w := (SimpleGraph.mem_neighborFinset G v w).mp hw
  let S : Finset V := ({w} : Finset V)ᶜ
  have hvS : v ∈ S := by simp [S, hvw.ne]
  have hS : S.card = 35 := by simp [S, Finset.card_compl, hV]
  have hcard : Fintype.card (S : Set V) = 35 := by
    simpa only [Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using hS
  have hlocal := core_R335_degree_ge_twelve (G.induce (S : Set V)) hcard
    (core_admissible_induce G 3 hG S) ⟨v, hvS⟩
  rw [degree_induce_eq_filter] at hlocal
  have hf : S.filter (G.Adj v) = (G.neighborFinset v).erase w := by
    ext z
    simp [S, and_comm]
  rw [hf, Finset.card_erase_of_mem hw, SimpleGraph.card_neighborFinset_eq_degree] at hlocal
  omega

theorem core_R336_edges_ge_234 (G : SimpleGraph V)
    (hV : Fintype.card V = 36) (hG : CoreAdmissible 3 G) :
    234 ≤ G.edgeFinset.card := by
  classical
  have hsum : ∑ v : V, 13 ≤ ∑ v : V, G.degree v :=
    Finset.sum_le_sum (fun v _ => core_R336_degree_ge_thirteen G hV hG v)
  have he := G.sum_degrees_eq_twice_card_edges
  simp only [Finset.sum_const, Finset.card_univ, smul_eq_mul, hV] at hsum
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at he ⊢
  omega

end EG617
