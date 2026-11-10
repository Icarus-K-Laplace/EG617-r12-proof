module

public import EG617.Core.Admissibility
public import Mathlib.Combinatorics.SimpleGraph.FiveWheelLike
public import Mathlib.Combinatorics.SimpleGraph.DegreeSum

@[expose] public section

set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617

/-- Two independent color classes of size at most eleven cannot cover 24 vertices. -/
theorem core_not_two_colorable_24 (L : SimpleGraph (Fin 24))
    (hI : CoreIndependenceBound 11 L) : ¬ L.Colorable 2 := by
  classical
  rintro ⟨C⟩
  let A := (Finset.univ : Finset (Fin 24)).filter (fun v => C v = 0)
  let B := (Finset.univ : Finset (Fin 24)).filter (fun v => C v = 1)
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
      24 = (Finset.univ : Finset (Fin 24)).card := by simp
      _ = (A ∪ B).card := congrArg Finset.card hu.symm
      _ ≤ A.card + B.card := Finset.card_union_le A B
  omega

/-- A strengthened low-order parent, using the already formalized AES theorem.
Every hypothesis is a graph condition; no unproved classification is assumed. -/
theorem core_triangleFree24_edges_lt_132 (L : SimpleGraph (Fin 24))
    (ht : L.CliqueFree 3) (hI : CoreIndependenceBound 11 L) :
    L.edgeFinset.card < 132 := by
  classical
  by_contra hnot
  have he : 132 ≤ L.edgeFinset.card := by omega
  have hdeg : ∀ v : Fin 24, L.degree v ≤ 11 := by
    intro v
    have h := hI (L.neighborFinset v) (by
      simpa only [SimpleGraph.coe_neighborFinset] using
        L.isIndepSet_neighborSet_of_triangleFree ht v)
    simpa only [SimpleGraph.card_neighborFinset_eq_degree] using h
  have hmin : ∀ v : Fin 24, 11 ≤ L.degree v := by
    intro v
    have hrest : ∑ w ∈ (Finset.univ : Finset (Fin 24)).erase v, L.degree w ≤ 253 := by
      calc
        _ ≤ ∑ _w ∈ (Finset.univ : Finset (Fin 24)).erase v, 11 :=
          Finset.sum_le_sum (fun w _ => hdeg w)
        _ = 253 := by simp
    have htotal :
        (∑ w ∈ (Finset.univ : Finset (Fin 24)).erase v, L.degree w) + L.degree v =
          2 * L.edgeFinset.card := by
      rw [Finset.sum_erase_add _ _ (Finset.mem_univ v), L.sum_degrees_eq_twice_card_edges]
    omega
  have hmd : 11 ≤ L.minDegree := L.le_minDegree_of_forall_le_degree 11 hmin
  have hcol : L.Colorable 2 :=
    SimpleGraph.colorable_of_cliqueFree_lt_minDegree (G := L) (r := 2) ht (by
      norm_num
      omega)
  exact core_not_two_colorable_24 L hI hcol

/-- Frozen GATE47 parent M1: R(2,24) is empty, with the full hereditary cap
explicit in `CoreAdmissible`. The proof uses only its 24-vertex cap. -/
theorem core_R224_empty (G : SimpleGraph (Fin 24)) : ¬ CoreAdmissible 2 G := by
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
  have hcap := hG.2.2 (Finset.univ : Finset (Fin 24))
  rw [core_induced_edge_count_univ] at hcap
  norm_num [D, tau12, Nat.choose_two_right] at hcap
  have htotal := core_compl_edge_count G
  norm_num [Nat.choose_two_right] at htotal
  have hhigh := core_triangleFree24_edges_lt_132 Gᶜ ht hI
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at hcap htotal hhigh
  omega

end EG617
