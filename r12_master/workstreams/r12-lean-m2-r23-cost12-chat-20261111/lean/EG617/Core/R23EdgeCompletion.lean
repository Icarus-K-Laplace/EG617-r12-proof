module
public import EG617.Core.R23CaseI

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Adding a genuinely new edge creates no triangle if its endpoints have no
common neighbor. This condition must be proved at each classification branch. -/
theorem triangleFree_sup_edge_of_no_common_neighbor (G : SimpleGraph V)
    (ht : G.CliqueFree 3) (u v : V) (hne : u ≠ v)
    (hcommon : ∀ w, G.Adj u w → ¬ G.Adj v w) :
    (G ⊔ SimpleGraph.edge u v).CliqueFree 3 := by
  classical
  intro S hS
  have hu : u ∈ S := ht.mem_of_sup_edge_isNClique hS
  have hswap : (G ⊔ SimpleGraph.edge v u).IsNClique 3 S := by
    rw [SimpleGraph.edge_comm v u]
    exact hS
  have hv : v ∈ S := ht.mem_of_sup_edge_isNClique hswap
  have hsmall : ({u, v} : Finset V).card < S.card := by
    rw [hS.card_eq]
    simp [hne]
  obtain ⟨w, hw, hwuv⟩ := Finset.exists_mem_notMem_of_card_lt_card hsmall
  have hwne : w ≠ u ∧ w ≠ v := by simpa using hwuv
  have huw := hS.isClique hu hw hwne.1.symm
  have hvw := hS.isClique hv hw hwne.2.symm
  have hGu : G.Adj u w := huw.resolve_right (by simp [SimpleGraph.edge_adj, hwne.1, hwne.2])
  have hGv : G.Adj v w := hvw.resolve_right (by simp [SimpleGraph.edge_adj, hwne.1, hwne.2])
  exact hcommon w hGu hGv

/-- General graph-level completion tool for M2b and the compatible M2d case.
The no-common-neighbor obligation is explicit, not a hidden terminal assumption.
This is not by itself a proof that either branch supplies such an edge. -/
theorem r23_one_edge_completion_case_I (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 121)
    (u v : V) (hne : u ≠ v) (hn : ¬ G.Adj u v)
    (hcommon : ∀ w, G.Adj u w → ¬ G.Adj v w) :
    let H := G ⊔ SimpleGraph.edge u v
    G ≤ H ∧ H.CliqueFree 3 ∧ CoreIndependenceBound 11 H ∧
      H.edgeFinset.card = 122 ∧ R23CaseIProfile H := by
  classical
  let H := G ⊔ SimpleGraph.edge u v
  have hHt : H.CliqueFree 3 := triangleFree_sup_edge_of_no_common_neighbor G ht u v hne hcommon
  have hHI : CoreIndependenceBound 11 H := by
    intro S hS
    apply hI S
    intro x hx y hy hxy hadj
    exact hS hx hy hxy (Or.inl hadj)
  have hHe : H.edgeFinset.card = 122 := by
    rw [SimpleGraph.card_edgeFinset_sup_edge G hn hne, he]
  exact ⟨le_sup_left, hHt, hHI, hHe, r23_122_case_I H hV hHt hHI hHe⟩

end EG617
