module
public import EG617.Core.CostSixDeletion

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Frozen M4's application of M3: the full R(2,23) contract supplies all
four original R23 hypotheses for the complement, including its 121-edge floor. -/
theorem core_R223_complement_cost_six (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (hG : CoreAdmissible 2 G) :
    CostSixProperty Gᶜ := by
  classical
  have ht : Gᶜ.CliqueFree 3 := by
    intro S hS
    have hi : G.IsNIndepSet 3 S := (SimpleGraph.isNClique_compl G).mp hS
    have hb := hG.1 S hi.isIndepSet
    rw [hi.card_eq] at hb
    omega
  have hI : CoreIndependenceBound 11 Gᶜ := by
    intro S hS
    exact hG.2.1 S ((SimpleGraph.isIndepSet_compl G).mp hS)
  have hcap := hG.2.2 (Finset.univ : Finset V)
  rw [core_induced_edge_count_univ] at hcap
  norm_num [D, tau12, Nat.choose_two_right, hV] at hcap
  have htotal := core_compl_edge_count G
  norm_num [Nat.choose_two_right, hV] at htotal
  apply r23_cost_six Gᶜ hV ht hI
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at hcap htotal ⊢
  omega

/-- At a degree-eleven vertex in the original full R(3,35) graph class,
the actual 23-point nonneighborhood complement satisfies universal Cost-6.
This is M4's input reduction, not yet its fourteen-point cap contradiction. -/
theorem core_R335_degree_eleven_nonneighbor_cost_six (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G)
    (v : V) (hd : G.degree v = 11) :
    let S := Gᶜ.neighborFinset v
    CostSixProperty (G.induce (S : Set V))ᶜ := by
  classical
  let S := Gᶜ.neighborFinset v
  have hS : S.card = 23 := by
    have hc : S.card = Fintype.card V - 1 - G.degree v := G.degree_compl v
    omega
  have ha : CoreAdmissible 2 (G.induce (S : Set V)) :=
    core_admissible_nonNeighbors G 2 hG v S (by
      intro w hw
      have hadj : Gᶜ.Adj v w := (SimpleGraph.mem_neighborFinset Gᶜ v w).mp hw
      exact ⟨hadj.ne.symm, (SimpleGraph.compl_adj G v w).mp hadj |>.2⟩)
  exact core_R223_complement_cost_six (G.induce (S : Set V))
    (by simpa only [Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using hS) ha

end EG617
