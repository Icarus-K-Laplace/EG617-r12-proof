module
public import EG617.Core.R23Classification

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- The original universal Cost-6 target, using actual induced unordered edges. -/
def CostSixProperty (G : SimpleGraph V) : Prop :=
  ∀ I : Finset V, G.IsIndepSet (I : Set V) →
    ∃ T : Finset V, T.card = 12 ∧ coreInducedEdgeCount G T + (T ∩ I).card ≤ 6

noncomputable def c5Fiber (t : V → Fin 5) (i : Fin 5) : Finset V :=
  Finset.univ.filter (fun x => t x = i)

@[simp] theorem mem_c5Fiber (t : V → Fin 5) (i : Fin 5) (x : V) :
    x ∈ c5Fiber t i ↔ t x = i := by
  classical
  simp [c5Fiber]

theorem c5Fiber_disjoint (t : V → Fin 5) {i j : Fin 5} (hne : i ≠ j) :
    Disjoint (c5Fiber t i) (c5Fiber t j) := by
  classical
  rw [Finset.disjoint_left]
  intro x hx hy
  exact hne ((mem_c5Fiber t i x).mp hx |>.symm.trans ((mem_c5Fiber t j x).mp hy))

theorem c5Fiber_adjCount (G : SimpleGraph V) (t : V → Fin 5)
    (hp : ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y)) (i j : Fin 5) :
    adjCount G (c5Fiber t i) (c5Fiber t j) =
      if (SimpleGraph.cycleGraph 5).Adj i j then (c5Fiber t i).card * (c5Fiber t j).card else 0 := by
  classical
  unfold adjCount
  calc
    _ = ∑ x ∈ c5Fiber t i, ∑ y ∈ c5Fiber t j,
        if (SimpleGraph.cycleGraph 5).Adj i j then 1 else 0 := by
      apply Finset.sum_congr rfl
      intro x hx
      apply Finset.sum_congr rfl
      intro y hy
      rw [hp x y, (mem_c5Fiber t i x).mp hx, (mem_c5Fiber t j y).mp hy]
    _ = _ := by
      by_cases h : (SimpleGraph.cycleGraph 5).Adj i j <;> simp [h, Nat.mul_comm]

/-- Exact witness counts when three selected types have just one adjacent pair. -/
theorem c5_three_fiber_witness_counts (G : SimpleGraph V) (t : V → Fin 5)
    (hp : ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y))
    (i j k : Fin 5) (hij : i ≠ j) (hik : i ≠ k)
    (hnij : ¬ (SimpleGraph.cycleGraph 5).Adj i j)
    (hnik : ¬ (SimpleGraph.cycleGraph 5).Adj i k)
    (hjk : (SimpleGraph.cycleGraph 5).Adj j k) (I : Finset V) :
    let F := c5Fiber t
    let T := F i ∪ F j ∪ F k
    T.card = (F i).card + (F j).card + (F k).card ∧
      coreInducedEdgeCount G T = (F j).card * (F k).card ∧
      (T ∩ I).card = (F i ∩ I).card + (F j ∩ I).card + (F k ∩ I).card := by
  classical
  let F := c5Fiber t
  let T := F i ∪ F j ∪ F k
  have hdij : Disjoint (F i) (F j) := c5Fiber_disjoint t hij
  have hdik : Disjoint (F i) (F k) := c5Fiber_disjoint t hik
  have hdjk : Disjoint (F j) (F k) := c5Fiber_disjoint t hjk.ne
  have hdijk : Disjoint (F i ∪ F j) (F k) := Finset.disjoint_union_left.mpr ⟨hdik, hdjk⟩
  refine ⟨?_, ?_, ?_⟩
  · exact (Finset.card_union_of_disjoint hdijk).trans
      (congrArg (fun n => n + (F k).card) (Finset.card_union_of_disjoint hdij))
  · have hL : ∀ U, adjCount G (F i ∪ F j) U = adjCount G (F i) U + adjCount G (F j) U :=
      fun U => adjCount_union_left G (F i) (F j) U hdij
    have hL3 : ∀ U, adjCount G T U = adjCount G (F i ∪ F j) U + adjCount G (F k) U :=
      fun U => adjCount_union_left G (F i ∪ F j) (F k) U hdijk
    have hR : ∀ U, adjCount G U (F i ∪ F j) = adjCount G U (F i) + adjCount G U (F j) :=
      fun U => adjCount_union_right G U (F i) (F j) hdij
    have hR3 : ∀ U, adjCount G U T = adjCount G U (F i ∪ F j) + adjCount G U (F k) :=
      fun U => adjCount_union_right G U (F i ∪ F j) (F k) hdijk
    have hF : ∀ a b, adjCount G (F a) (F b) =
        if (SimpleGraph.cycleGraph 5).Adj a b then (F a).card * (F b).card else 0 :=
      fun a b => c5Fiber_adjCount G t hp a b
    have hnji : ¬ (SimpleGraph.cycleGraph 5).Adj j i := fun h => hnij h.symm
    have hnki : ¬ (SimpleGraph.cycleGraph 5).Adj k i := fun h => hnik h.symm
    have hkj := hjk.symm
    have he := adjCount_self G T
    simp only [hL3, hL, hR3, hR, hF] at he
    simp [hnij, hnik, hnji, hnki, hjk, hkj] at he
    simp only [Nat.mul_comm] at he
    omega
  · have hdi : Disjoint (F i ∩ I) (F j ∩ I) := hdij.mono Finset.inter_subset_left Finset.inter_subset_left
    have hdk : Disjoint (F i ∩ I ∪ F j ∩ I) (F k ∩ I) :=
      Finset.disjoint_union_left.mpr
        ⟨hdik.mono Finset.inter_subset_left Finset.inter_subset_left,
          hdjk.mono Finset.inter_subset_left Finset.inter_subset_left⟩
    change ((F i ∪ F j ∪ F k) ∩ I).card = _
    rw [Finset.union_inter_distrib_right, Finset.union_inter_distrib_right,
      Finset.card_union_of_disjoint hdk, Finset.card_union_of_disjoint hdi]

/-- Independence applies to every actual vertex of I, forcing one of every
adjacent pair of type-intersections to be empty. -/
theorem independent_c5_fiber_counts (G : SimpleGraph V) (t : V → Fin 5)
    (hp : ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y))
    (I : Finset V) (hI : G.IsIndepSet (I : Set V)) :
    (∀ i, (c5Fiber t i ∩ I).card ≤ (c5Fiber t i).card) ∧
      ∀ i j, (SimpleGraph.cycleGraph 5).Adj i j →
        (c5Fiber t i ∩ I).card = 0 ∨ (c5Fiber t j ∩ I).card = 0 := by
  classical
  refine ⟨fun _ => Finset.card_le_card Finset.inter_subset_left, ?_⟩
  intro i j hij
  by_cases hi : (c5Fiber t i ∩ I).card = 0
  · exact Or.inl hi
  right
  by_contra hj
  obtain ⟨x, hx⟩ := Finset.card_pos.mp (Nat.pos_of_ne_zero hi)
  obtain ⟨y, hy⟩ := Finset.card_pos.mp (Nat.pos_of_ne_zero hj)
  have htx := (mem_c5Fiber t i x).mp (Finset.mem_inter.mp hx).1
  have hty := (mem_c5Fiber t j y).mp (Finset.mem_inter.mp hy).1
  have hadj : G.Adj x y := (hp x y).mpr (by rw [htx, hty]; exact hij)
  exact hI (Finset.mem_inter.mp hx).2 (Finset.mem_inter.mp hy).2 hadj.ne hadj

theorem case_I_cost_arithmetic (A B p a s d b : ℕ) (hAB : A + B = 11)
    (hp : p ≤ 10) (ha : a ≤ A) (hs : s ≤ 1) (hd : d ≤ 1) (hb : b ≤ B)
    (hpa : p = 0 ∨ a = 0) (has : a = 0 ∨ s = 0) (hsd : s = 0 ∨ d = 0)
    (hdb : d = 0 ∨ b = 0) (hbp : b = 0 ∨ p = 0) :
    1 + p + s + d ≤ 6 ∨ A + a + b + s ≤ 6 ∨ B + a + b + d ≤ 6 := by
  omega

theorem exceptional_cost_arithmetic (p q c d e : ℕ)
    (hp : p ≤ 9) (hq : q ≤ 9) (hc : c ≤ 2) (hd : d ≤ 1) (he : e ≤ 2)
    (hpq : p = 0 ∨ q = 0) (hqc : q = 0 ∨ c = 0) (hcd : c = 0 ∨ d = 0)
    (hde : d = 0 ∨ e = 0) (hep : e = 0 ∨ p = 0) :
    2 + p + c + d ≤ 4 ∨ 2 + q + d + e ≤ 4 := by
  omega

end EG617
