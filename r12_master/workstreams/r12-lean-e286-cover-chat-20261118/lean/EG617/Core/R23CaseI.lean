module
public import EG617.Core.C5TypeFibers
public import Mathlib.Algebra.BigOperators.Fin
public import Mathlib.Tactic.FinCases

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem c5_remaining_fiber_sum (n : Fin 5 → ℕ) (a : Fin 5)
    (hs : ∑ i, n i = 23) (ha : n a = 10)
    (hplus : n (a + 2) = 1) (hminus : n (a - 2) = 1) :
    n (a + 1) + n (a - 1) = 11 := by
  have hsub1 : ∀ i : Fin 5, i - 1 = i + 4 := by decide
  have hsub2 : ∀ i : Fin 5, i - 2 = i + 3 := by decide
  simp only [hsub1, hsub2] at hminus ⊢
  fin_cases a <;> norm_num [Fin.sum_univ_succ] at hs ha hplus hminus ⊢ <;> omega

/-- C5(10,A,1,1,B), up to rotation, specified by all actual vertex fibers
and an adjacency equivalence on every vertex pair. No abstract type pattern
is substituted for the graph. -/
def R23CaseIProfile (G : SimpleGraph V) : Prop :=
  ∃ (t : V → Fin 5) (a : Fin 5) (A B : ℕ),
    (∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y)) ∧
    (Finset.univ.filter (fun x => t x = a)).card = 10 ∧
    (Finset.univ.filter (fun x => t x = a + 1)).card = A ∧
    (Finset.univ.filter (fun x => t x = a + 2)).card = 1 ∧
    (Finset.univ.filter (fun x => t x = a - 2)).card = 1 ∧
    (Finset.univ.filter (fun x => t x = a - 1)).card = B ∧
    A + B = 11 ∧ 1 ≤ A ∧ A ≤ 10 ∧ 1 ≤ B ∧ B ≤ 10

/-- Frozen M2a / Case I, with original R23 assumptions and exactly122 edges. -/
theorem r23_122_case_I (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 122) :
    R23CaseIProfile G := by
  classical
  obtain ⟨S, f, t, P, Q, hf, _, hlabels, hpres, hcover, hP, hQ, hcross⟩ :=
    r23_122_complete_type_data G hV ht hI he
  obtain ⟨a, ha, hsingle⟩ := complete_exterior_type_fiber_profile f ht S P Q
    hf hcover hP hQ t hlabels hcross
  let n := fun i : Fin 5 => (Finset.univ.filter (fun x => t x = i)).card
  have hcycle : ∀ i, t (f i) = i := by
    intro i
    have hi := cycleNeighborLabels_cycle_vertex f ht i
    have hc : (cycleNeighborLabels f (f i)).card = 2 := by rw [hi, c5Type_card]
    exact (cycleNeighborLabels_unique_type f ht (f i) hc).unique (hlabels (f i)) hi
  have hpos : ∀ i, 1 ≤ n i := by
    intro i
    apply Finset.card_pos.mpr
    exact ⟨f i, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hcycle i⟩⟩
  have hsum : ∑ i, n i = 23 := by
    have h := Finset.card_eq_sum_card_fiberwise (f := t)
      (s := Finset.univ) (t := Finset.univ) (fun x _ => Finset.mem_univ (t x))
    simpa only [Finset.card_univ, hV] using h.symm
  have hnon : a + 2 ≠ a ∧ ¬ (SimpleGraph.cycleGraph 5).Adj a (a + 2) ∧
      a - 2 ≠ a ∧ ¬ (SimpleGraph.cycleGraph 5).Adj a (a - 2) :=
    (by decide : ∀ i : Fin 5, i + 2 ≠ i ∧
      ¬ (SimpleGraph.cycleGraph 5).Adj i (i + 2) ∧ i - 2 ≠ i ∧
      ¬ (SimpleGraph.cycleGraph 5).Adj i (i - 2)) a
  have hplus : n (a + 2) = 1 := hsingle _ hnon.1 hnon.2.1
  have hminus : n (a - 2) = 1 := hsingle _ hnon.2.2.1 hnon.2.2.2
  have hpair := c5_remaining_fiber_sum n a hsum ha hplus hminus
  have hpa := hpos (a + 1)
  have hpb := hpos (a - 1)
  exact ⟨t, a, n (a + 1), n (a - 1), hpres, ha, rfl, hplus, hminus, rfl,
    hpair, hpa, by omega, hpb, by omega⟩

end EG617
