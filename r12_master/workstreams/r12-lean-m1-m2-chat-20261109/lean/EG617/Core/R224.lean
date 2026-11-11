module

public import EG617.Core.Admissibility
public import Mathlib.Combinatorics.SimpleGraph.FiveWheelLike
public import Mathlib.Combinatorics.SimpleGraph.DegreeSum

@[expose] public section

set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617

universe u
variable {V : Type u} [Fintype V]

/-- Two independent color classes of size at most eleven cannot cover 24 vertices. -/
theorem core_not_two_colorable_of_card_24 (L : SimpleGraph V)
    (hV : Fintype.card V = 24)
    (hI : CoreIndependenceBound 11 L) : ¬ L.Colorable 2 := by
  classical
  rintro ⟨C⟩
  let A := (Finset.univ : Finset V).filter (fun v => C v = 0)
  let B := (Finset.univ : Finset V).filter (fun v => C v = 1)
  have hA : A.card ≤ 11 := by
    apply hI A
    intro x hx y hy _
    exact C.not_adj_of_mem_colorClass (Finset.mem_filter.mp hx).2
      (Finset.mem_filter.mp hy).2
  have hB : B.card ≤ 11 := by
    apply hI B
    intro x hx y hy _
    exact C.not_adj_of_mem_colorClass (Finset.mem_filter.mp hx).2
      (Finset.mem_filter.mp hy).2
  have hu : A ∪ B = Finset.univ := by
    ext v
    simp only [A, B, Finset.mem_union, Finset.mem_filter,
      Finset.mem_univ, true_and, iff_true]
    exact (by decide : ∀ i : Fin 2, i = 0 ∨ i = 1) (C v)
  have hcard : 24 ≤ A.card + B.card := by
    calc
      24 = (Finset.univ : Finset V).card := by simp [hV]
      _ = (A ∪ B).card := congrArg Finset.card hu.symm
      _ ≤ A.card + B.card := Finset.card_union_le A B
  omega

/-- A strengthened low-order parent, using the already formalized AES theorem.
Every hypothesis is a graph condition; no unproved classification is assumed. -/
theorem core_triangleFree_edges_lt_132_of_card_24 (L : SimpleGraph V)
    (hV : Fintype.card V = 24)
    (ht : L.CliqueFree 3) (hI : CoreIndependenceBound 11 L) :
    L.edgeFinset.card < 132 := by
  classical
  by_contra hnot
  have he : 132 ≤ L.edgeFinset.card := by omega
  have hdeg : ∀ v : V, L.degree v ≤ 11 := by
    intro v
    have h := hI (L.neighborFinset v) (by
      simpa only [SimpleGraph.coe_neighborFinset] using
        L.isIndepSet_neighborSet_of_triangleFree ht v)
    simpa only [SimpleGraph.card_neighborFinset_eq_degree] using h
  have hmin : ∀ v : V, 11 ≤ L.degree v := by
    intro v
    have hrest : ∑ w ∈ (Finset.univ : Finset V).erase v, L.degree w ≤ 253 := by
      calc
        _ ≤ ∑ _w ∈ (Finset.univ : Finset V).erase v, 11 :=
          Finset.sum_le_sum (fun w _ => hdeg w)
        _ = 253 := by simp [hV]
    have htotal :
        (∑ w ∈ (Finset.univ : Finset V).erase v, L.degree w) + L.degree v =
          2 * L.edgeFinset.card := by
      rw [Finset.sum_erase_add _ _ (Finset.mem_univ v), L.sum_degrees_eq_twice_card_edges]
    omega
  haveI : Nonempty V := Fintype.card_pos_iff.mp (by omega)
  have hmd : 11 ≤ L.minDegree := L.le_minDegree_of_forall_le_degree 11 hmin
  have hcol : L.Colorable 2 :=
    SimpleGraph.colorable_of_cliqueFree_lt_minDegree (G := L) (r := 2) ht (by
      norm_num [hV]
      omega)
  exact core_not_two_colorable_of_card_24 L hV hI hcol

/-- Frozen GATE47 parent M1: R(2,24) is empty, with the full hereditary cap
explicit in `CoreAdmissible`. The proof uses only its 24-vertex cap. -/
theorem core_R224_empty_of_card (G : SimpleGraph V)
    (hV : Fintype.card V = 24) : ¬ CoreAdmissible 2 G := by
  classical
  intro hG
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
  have hhigh := core_triangleFree_edges_lt_132_of_card_24 Gᶜ hV ht hI
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at hcap htotal hhigh
  omega

/-- Original Fin 24 interface, preserved as a specialization. -/
theorem core_not_two_colorable_24 (L : SimpleGraph (Fin 24))
    (hI : CoreIndependenceBound 11 L) : ¬ L.Colorable 2 :=
  core_not_two_colorable_of_card_24 L rfl hI

theorem core_triangleFree24_edges_lt_132 (L : SimpleGraph (Fin 24))
    (ht : L.CliqueFree 3) (hI : CoreIndependenceBound 11 L) :
    L.edgeFinset.card < 132 :=
  core_triangleFree_edges_lt_132_of_card_24 L rfl ht hI

theorem core_R224_empty (G : SimpleGraph (Fin 24)) : ¬ CoreAdmissible 2 G :=
  core_R224_empty_of_card G rfl

/-- Frozen M4/M5 first step: every nonneighborhood has at most 23 vertices. -/
theorem core_R3_card_le_degree_add_24 (G : SimpleGraph V)
    (hG : CoreAdmissible 3 G) (v : V) : Fintype.card V ≤ G.degree v + 24 := by
  classical
  by_contra hnot
  let S := Gᶜ.neighborFinset v
  have hcard : S.card = Fintype.card V - 1 - G.degree v := by
    exact G.degree_compl v
  have hbig : 24 ≤ S.card := by omega
  obtain ⟨T, hTS, hT⟩ := Finset.exists_subset_card_eq hbig
  have ha : CoreAdmissible 2 (G.induce (T : Set V)) :=
    core_admissible_nonNeighbors G 2 hG v T (by
      intro w hw
      have hadj : Gᶜ.Adj v w := (SimpleGraph.mem_neighborFinset Gᶜ v w).mp (hTS hw)
      exact ⟨hadj.ne.symm, (SimpleGraph.compl_adj G v w).mp hadj |>.2⟩)
  have hn : Fintype.card T = 24 := by simpa only [Fintype.card_coe] using hT
  exact core_R224_empty_of_card (G.induce (T : Set V)) hn ha

/-- The weak degree bound needed before the remaining 23-point classification. -/
theorem core_R335_degree_ge_11 (G : SimpleGraph (Fin 35))
    (hG : CoreAdmissible 3 G) (v : Fin 35) : 11 ≤ G.degree v := by
  have h := core_R3_card_le_degree_add_24 G hG v
  norm_num at h
  omega

/-- Frozen low M5: the 37-point class is empty, directly from R224. -/
theorem core_R337_empty_of_card (G : SimpleGraph V)
    (hV : Fintype.card V = 37) : ¬ CoreAdmissible 3 G := by
  classical
  intro hG
  have hd : ∀ v : V, 13 ≤ G.degree v := by
    intro v
    have h := core_R3_card_le_degree_add_24 G hG v
    rw [hV] at h
    omega
  have hsum : 481 ≤ 2 * G.edgeFinset.card := by
    calc
      481 = ∑ _v : V, 13 := by simp [hV]
      _ ≤ ∑ v : V, G.degree v := Finset.sum_le_sum (fun v _ => hd v)
      _ = 2 * G.edgeFinset.card := G.sum_degrees_eq_twice_card_edges
  have hcap := hG.2.2 (Finset.univ : Finset V)
  rw [core_induced_edge_count_univ] at hcap
  norm_num [D, tau12, Nat.choose_two_right, hV] at hcap
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at hsum hcap
  omega

theorem core_R337_empty (G : SimpleGraph (Fin 37)) : ¬ CoreAdmissible 3 G :=
  core_R337_empty_of_card G rfl

/-- Frozen low M6 first case: R337 excludes a nonneighborhood of size37. -/
theorem core_R4_card_le_degree_add_37 (G : SimpleGraph V)
    (hG : CoreAdmissible 4 G) (v : V) : Fintype.card V ≤ G.degree v + 37 := by
  classical
  by_contra hnot
  let S := Gᶜ.neighborFinset v
  have hcard : S.card = Fintype.card V - 1 - G.degree v := by
    exact G.degree_compl v
  have hbig : 37 ≤ S.card := by omega
  obtain ⟨T, hTS, hT⟩ := Finset.exists_subset_card_eq hbig
  have ha : CoreAdmissible 3 (G.induce (T : Set V)) :=
    core_admissible_nonNeighbors G 3 hG v T (by
      intro w hw
      have hadj : Gᶜ.Adj v w := (SimpleGraph.mem_neighborFinset Gᶜ v w).mp (hTS hw)
      exact ⟨hadj.ne.symm, (SimpleGraph.compl_adj G v w).mp hadj |>.2⟩)
  have hn : Fintype.card T = 37 := by simpa only [Fintype.card_coe] using hT
  exact core_R337_empty_of_card (G.induce (T : Set V)) hn ha

/-- A proved proper subcase of GATE47, not the target bound12. -/
theorem core_R447_degree_ge_10 (G : SimpleGraph (Fin 47))
    (hG : CoreAdmissible 4 G) (v : Fin 47) : 10 ≤ G.degree v := by
  have h := core_R4_card_le_degree_add_37 G hG v
  norm_num at h
  omega

end EG617
