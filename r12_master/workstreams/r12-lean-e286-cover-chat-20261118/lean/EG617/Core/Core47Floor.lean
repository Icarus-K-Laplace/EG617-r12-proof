module
public import EG617.Core.E286Exclusion

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators
namespace EG617

/-- In the low-edge range there is a missing edge with fewer than ten common
neighbors. This supplies a one-edge extension preserving the clique bound. -/
theorem core47_sparse_nonedge (G : SimpleGraph (Fin 47)) (he : G.edgeFinset.card ≤ 285)
    (hd : ∀ x, 12 ≤ G.degree x) :
    ∃ x y, x ≠ y ∧ ¬G.Adj x y ∧ ((G.neighborFinset x).filter (G.Adj y)).card ≤ 9 := by
  classical
  have hsum : (∑ x, G.degree x) ≤ 570 := by
    have h := G.sum_degrees_eq_twice_card_edges
    simp only [SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard] at h he
    omega
  obtain ⟨x,hx⟩ : ∃ x, G.degree x = 12 := by
    by_contra! h
    have too := Finset.sum_le_sum (s := (Finset.univ : Finset (Fin 47)))
      (f := fun _ => 13) (g := fun x => G.degree x)
      (fun x _ => show 13 ≤ G.degree x by have := hd x; have := h x; omega)
    norm_num at too
    omega
  let N := G.neighborFinset x
  have nc : N.card = 12 := (SimpleGraph.card_neighborFinset_eq_degree G x).trans hx
  have tc : Nᶜ.card = 35 := by rw [Finset.card_compl,nc]; decide
  by_contra! no
  have low (y : Fin 47) (hy : y ∈ Nᶜ) : 10 ≤ (N.filter (G.Adj y)).card := by
    by_cases eq : y = x
    · subst y
      have same : N.filter (G.Adj x) = N := by
        ext t
        simp only [Finset.mem_filter]
        exact ⟨And.left,fun ht => ⟨ht,(SimpleGraph.mem_neighborFinset G x t).mp ht⟩⟩
      rw [same,nc]
      decide
    · exact no x y eq.symm (fun h => Finset.mem_compl.mp hy ((SimpleGraph.mem_neighborFinset G x y).mpr h))
  have many := Finset.sum_le_sum low
  simp only [Finset.sum_const,smul_eq_mul,tc] at many
  have bound := adjCount_le_sum_degrees G N Nᶜ
  rw [adjCount_symm,adjCount_eq_sum_filter] at bound
  have rest := Finset.sum_le_sum (s := Nᶜ) (f := fun _ => 12) (g := fun y => G.degree y) (fun y _ => hd y)
  simp only [Finset.sum_const,smul_eq_mul,tc] at rest
  have partition := Finset.sum_add_sum_compl N (fun y => G.degree y)
  omega

theorem core47_add_sparse_edge_clique (G : SimpleGraph (Fin 47)) (bound : CoreCliqueBound 11 G)
    (x y : Fin 47) (xy : x ≠ y)
    (small : ((G.neighborFinset x).filter (G.Adj y)).card ≤ 9) :
    CoreCliqueBound 11 (G ⊔ SimpleGraph.edge x y) := by
  classical
  intro S hS
  have old (a b : Fin 47) (ha : a ∈ S) (hb : b ∈ S) (ab : a ≠ b)
      (h : ¬ (a = x ∧ b = y ∨ a = y ∧ b = x)) : G.Adj a b := by
    rcases hS ha hb ab with e | e
    · exact e
    · exact (h ((SimpleGraph.edge_adj _ _ _ _).mp e).1).elim
  by_cases hx : x ∈ S <;> by_cases hy : y ∈ S
  · have yerase : y ∈ S.erase x := Finset.mem_erase.mpr ⟨xy.symm,hy⟩
    have sub : (S.erase x).erase y ⊆ (G.neighborFinset x).filter (G.Adj y) := by
      intro z hz
      obtain ⟨zy,hz⟩ := Finset.mem_erase.mp hz
      obtain ⟨zx,hs⟩ := Finset.mem_erase.mp hz
      exact Finset.mem_filter.mpr ⟨(SimpleGraph.mem_neighborFinset G x z).mpr
        (old x z hx hs zx.symm (by simp [zy,zx,xy])),old y z hy hs zy.symm (by simp [zy,zx,xy.symm])⟩
    have h := Finset.card_le_card sub
    rw [Finset.card_erase_of_mem yerase, Finset.card_erase_of_mem hx] at h
    omega
  all_goals
    apply bound S
    intro a ha b hb ab
    apply old a b ha hb ab
    rintro (⟨rfl,rfl⟩ | ⟨rfl,rfl⟩) <;> contradiction

/-- The extension uses only the abstract E286 bounds after the original
hereditary hypotheses have supplied the minimum-degree gate. -/
theorem core47_low_edges_impossible (G : SimpleGraph (Fin 47)) (he : G.edgeFinset.card ≤ 286)
    (hd : ∀ x, 12 ≤ G.degree x) (ha : CoreIndependenceBound 4 G) (hc : CoreCliqueBound 11 G) :
    False := by
  classical
  generalize hgap : 286 - G.edgeFinset.card = k
  induction k generalizing G with
  | zero =>
    exact e286_excluded G ⟨by decide,by omega,hd,ha,hc⟩
  | succ k ih =>
    obtain ⟨x,y,hxy,hn,hs⟩ := core47_sparse_nonedge G (by omega) hd
    let H := G ⊔ SimpleGraph.edge x y
    have plus : H.edgeFinset.card = G.edgeFinset.card + 1 := G.card_edgeFinset_sup_edge x y hn hxy
    have leGH : G ≤ H := le_sup_left
    apply ih H (by omega) (fun v => (hd v).trans (SimpleGraph.degree_le_of_le leGH))
    · intro S hS
      exact ha S (fun a ha' b hb' hab e => hS ha' hb' hab (leGH e))
    · exact core47_add_sparse_edge_clique G hc x y hxy hs
    · omega

theorem core47_edge_floor_287 (G : SimpleGraph (Fin 47)) (hG : CoreAdmissible 4 G) :
    287 ≤ G.edgeFinset.card := by
  by_contra! he
  have low : G.edgeFinset.card ≤ 286 := by omega
  exact core47_low_edges_impossible G low (gate47_verified G hG low) hG.1 hG.2.1

end EG617
