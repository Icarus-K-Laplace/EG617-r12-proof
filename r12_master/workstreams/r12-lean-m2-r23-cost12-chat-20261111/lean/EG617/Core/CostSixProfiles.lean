module
public import EG617.Core.CostSixCounts

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Frozen M3 Case I: the three concrete twelve-vertex witnesses cover every
independent set, including nonmaximal and empty independent sets. -/
theorem case_I_cost_six (G : SimpleGraph V) (h : R23CaseIProfile G) :
    CostSixProperty G := by
  classical
  obtain ⟨t, c, A, B, hp, hn0, hn1, hn2, hn3, hn4, hAB, _⟩ := h
  change (c5Fiber t c).card = 10 at hn0
  change (c5Fiber t (c + 1)).card = A at hn1
  change (c5Fiber t (c + 2)).card = 1 at hn2
  change (c5Fiber t (c - 2)).card = 1 at hn3
  change (c5Fiber t (c - 1)).card = B at hn4
  intro I hI
  obtain ⟨hb, hz⟩ := independent_c5_fiber_counts G t hp I hI
  have hcycle : (SimpleGraph.cycleGraph 5).Adj c (c + 1) ∧
      (SimpleGraph.cycleGraph 5).Adj (c + 1) (c + 2) ∧
      (SimpleGraph.cycleGraph 5).Adj (c + 2) (c - 2) ∧
      (SimpleGraph.cycleGraph 5).Adj (c - 2) (c - 1) ∧
      (SimpleGraph.cycleGraph 5).Adj (c - 1) c :=
    (by decide : ∀ c : Fin 5, (SimpleGraph.cycleGraph 5).Adj c (c + 1) ∧
      (SimpleGraph.cycleGraph 5).Adj (c + 1) (c + 2) ∧
      (SimpleGraph.cycleGraph 5).Adj (c + 2) (c - 2) ∧
      (SimpleGraph.cycleGraph 5).Adj (c - 2) (c - 1) ∧
      (SimpleGraph.cycleGraph 5).Adj (c - 1) c) c
  have hw0 := c5_three_fiber_witness_counts G t hp c (c + 2) (c - 2)
    ((by decide : ∀ c : Fin 5, c ≠ c + 2) c)
    ((by decide : ∀ c : Fin 5, c ≠ c - 2) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj c (c + 2)) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj c (c - 2)) c)
    hcycle.2.2.1 I
  have hw1 := c5_three_fiber_witness_counts G t hp (c - 1) (c + 1) (c + 2)
    ((by decide : ∀ c : Fin 5, c - 1 ≠ c + 1) c)
    ((by decide : ∀ c : Fin 5, c - 1 ≠ c + 2) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj (c - 1) (c + 1)) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj (c - 1) (c + 2)) c)
    hcycle.2.1 I
  have hw2 := c5_three_fiber_witness_counts G t hp (c + 1) (c - 1) (c - 2)
    ((by decide : ∀ c : Fin 5, c + 1 ≠ c - 1) c)
    ((by decide : ∀ c : Fin 5, c + 1 ≠ c - 2) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj (c + 1) (c - 1)) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj (c + 1) (c - 2)) c)
    hcycle.2.2.2.1.symm I
  dsimp only at hw0 hw1 hw2
  rw [hn0, hn2, hn3] at hw0
  rw [hn4, hn1, hn2] at hw1
  rw [hn1, hn4, hn3] at hw2
  have h0 := hb c
  have h1 := hb (c + 1)
  have h2 := hb (c + 2)
  have h3 := hb (c - 2)
  have h4 := hb (c - 1)
  rw [hn0] at h0
  rw [hn1] at h1
  rw [hn2] at h2
  rw [hn3] at h3
  rw [hn4] at h4
  have hc := case_I_cost_arithmetic A B _ _ _ _ _ hAB h0 h1 h2 h3 h4
    (hz _ _ hcycle.1) (hz _ _ hcycle.2.1) (hz _ _ hcycle.2.2.1)
    (hz _ _ hcycle.2.2.2.1) (hz _ _ hcycle.2.2.2.2)
  rcases hc with hc | hc | hc
  · exact ⟨c5Fiber t c ∪ c5Fiber t (c + 2) ∪ c5Fiber t (c - 2), by omega, by omega⟩
  · exact ⟨c5Fiber t (c - 1) ∪ c5Fiber t (c + 1) ∪ c5Fiber t (c + 2), by omega, by omega⟩
  · exact ⟨c5Fiber t (c + 1) ∪ c5Fiber t (c - 1) ∪ c5Fiber t (c - 2), by omega, by omega⟩

/-- The exceptional profile has the stronger universal Cost-4 bound. -/
theorem exceptional_cost_four (G : SimpleGraph V) (h : R23ExceptionalProfile G)
    (I : Finset V) (hI : G.IsIndepSet (I : Set V)) :
    ∃ T : Finset V, T.card = 12 ∧ coreInducedEdgeCount G T + (T ∩ I).card ≤ 4 := by
  classical
  obtain ⟨t, c, hp, hn0, hn1, hn2, hn3, hn4⟩ := h
  change (c5Fiber t c).card = 9 at hn0
  change (c5Fiber t (c + 1)).card = 9 at hn1
  change (c5Fiber t (c + 2)).card = 2 at hn2
  change (c5Fiber t (c - 2)).card = 1 at hn3
  change (c5Fiber t (c - 1)).card = 2 at hn4
  obtain ⟨hb, hz⟩ := independent_c5_fiber_counts G t hp I hI
  have hcycle : (SimpleGraph.cycleGraph 5).Adj c (c + 1) ∧
      (SimpleGraph.cycleGraph 5).Adj (c + 1) (c + 2) ∧
      (SimpleGraph.cycleGraph 5).Adj (c + 2) (c - 2) ∧
      (SimpleGraph.cycleGraph 5).Adj (c - 2) (c - 1) ∧
      (SimpleGraph.cycleGraph 5).Adj (c - 1) c :=
    (by decide : ∀ c : Fin 5, (SimpleGraph.cycleGraph 5).Adj c (c + 1) ∧
      (SimpleGraph.cycleGraph 5).Adj (c + 1) (c + 2) ∧
      (SimpleGraph.cycleGraph 5).Adj (c + 2) (c - 2) ∧
      (SimpleGraph.cycleGraph 5).Adj (c - 2) (c - 1) ∧
      (SimpleGraph.cycleGraph 5).Adj (c - 1) c) c
  have hw0 := c5_three_fiber_witness_counts G t hp c (c + 2) (c - 2)
    ((by decide : ∀ c : Fin 5, c ≠ c + 2) c)
    ((by decide : ∀ c : Fin 5, c ≠ c - 2) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj c (c + 2)) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj c (c - 2)) c)
    hcycle.2.2.1 I
  have hw1 := c5_three_fiber_witness_counts G t hp (c + 1) (c - 1) (c - 2)
    ((by decide : ∀ c : Fin 5, c + 1 ≠ c - 1) c)
    ((by decide : ∀ c : Fin 5, c + 1 ≠ c - 2) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj (c + 1) (c - 1)) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj (c + 1) (c - 2)) c)
    hcycle.2.2.2.1.symm I
  dsimp only at hw0 hw1
  rw [hn0, hn2, hn3] at hw0
  rw [hn1, hn4, hn3] at hw1
  have h0 := hb c
  have h1 := hb (c + 1)
  have h2 := hb (c + 2)
  have h3 := hb (c - 2)
  have h4 := hb (c - 1)
  rw [hn0] at h0
  rw [hn1] at h1
  rw [hn2] at h2
  rw [hn3] at h3
  rw [hn4] at h4
  have hc := exceptional_cost_arithmetic _ _ _ _ _ h0 h1 h2 h3 h4
    (hz _ _ hcycle.1) (hz _ _ hcycle.2.1) (hz _ _ hcycle.2.2.1)
    (hz _ _ hcycle.2.2.2.1) (hz _ _ hcycle.2.2.2.2)
  rcases hc with hc | hc
  · exact ⟨c5Fiber t c ∪ c5Fiber t (c + 2) ∪ c5Fiber t (c - 2), by omega, by omega⟩
  · exact ⟨c5Fiber t (c + 1) ∪ c5Fiber t (c - 1) ∪ c5Fiber t (c - 2), by omega, by omega⟩

theorem exceptional_cost_six (G : SimpleGraph V) (h : R23ExceptionalProfile G) :
    CostSixProperty G := by
  intro I hI
  obtain ⟨T, hT, he⟩ := exceptional_cost_four G h I hI
  exact ⟨T, hT, by omega⟩

end EG617
