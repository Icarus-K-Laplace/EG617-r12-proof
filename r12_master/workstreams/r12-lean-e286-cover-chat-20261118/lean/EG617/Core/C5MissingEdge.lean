module

public import EG617.Core.C5Types
public import Mathlib.Data.Fintype.Powerset

@[expose] public section
set_option autoImplicit false

namespace EG617

/-- If one extra vertex is compatible with every type on a side, it is the
unique common neighbor whenever the opposite side has two distinct types. -/
theorem c5_incompatible_endpoint_forces_singleton (A B : Finset (Fin 5))
    (hA : A.Nonempty) (hB : B.Nonempty) (u v : Fin 5)
    (hAB : ∀ a ∈ A, ∀ b ∈ B, (SimpleGraph.cycleGraph 5).Adj a b)
    (hu : ∀ b ∈ B, (SimpleGraph.cycleGraph 5).Adj u b)
    (hv : ∀ a ∈ A, (SimpleGraph.cycleGraph 5).Adj a v)
    (huv : ¬ (SimpleGraph.cycleGraph 5).Adj u v) : A.card = 1 := by
  obtain ⟨b, hb⟩ := hB
  by_contra hnot
  have hpos := Finset.card_pos.mpr hA
  obtain ⟨i, hi, j, hj, hij⟩ := Finset.one_lt_card.mp (by omega : 1 < A.card)
  have heq := c5_common_neighbors_unique i j b v hij
    (hAB i hi b hb) (hAB j hj b hb) (hv i hi) (hv j hj)
  exact huv (heq ▸ hu b hb)

/-- Complete removal of the missing endpoints leaves singleton type sets on
both sides; the conclusion is derived from all actual cross constraints. -/
theorem c5_missing_edge_type_sets (A B : Finset (Fin 5))
    (hA : A.Nonempty) (hB : B.Nonempty) (u v : Fin 5)
    (hAB : ∀ a ∈ A, ∀ b ∈ B, (SimpleGraph.cycleGraph 5).Adj a b)
    (hu : ∀ b ∈ B, (SimpleGraph.cycleGraph 5).Adj u b)
    (hv : ∀ a ∈ A, (SimpleGraph.cycleGraph 5).Adj a v)
    (huv : ¬ (SimpleGraph.cycleGraph 5).Adj u v) : A.card = 1 ∧ B.card = 1 := by
  refine ⟨c5_incompatible_endpoint_forces_singleton A B hA hB u v hAB hu hv huv, ?_⟩
  apply c5_incompatible_endpoint_forces_singleton B A hB hA v u
  · intro b hb a ha; exact (hAB a ha b hb).symm
  · intro a ha; exact (hv a ha).symm
  · intro b hb; exact (hu b hb).symm
  · intro h; exact huv h.symm

set_option maxRecDepth 100000 in
set_option maxHeartbeats 2000000 in
/-- All incompatible endpoint configurations, parametrized by five rotations
and two orientations. This ranges over all four Fin 5 labels, not selected examples. -/
theorem c5_missing_endpoint_orientations (a b u v : Fin 5)
    (hab : (SimpleGraph.cycleGraph 5).Adj a b)
    (hub : (SimpleGraph.cycleGraph 5).Adj u b)
    (hav : (SimpleGraph.cycleGraph 5).Adj a v)
    (huv : ¬ (SimpleGraph.cycleGraph 5).Adj u v) :
    (b = a + 1 ∧ u = a + 2 ∧ v = a - 1) ∨
      (b = a - 1 ∧ u = a - 2 ∧ v = a + 1) := by
  exact (by decide : ∀ a b u v : Fin 5,
    (SimpleGraph.cycleGraph 5).Adj a b → (SimpleGraph.cycleGraph 5).Adj u b →
    (SimpleGraph.cycleGraph 5).Adj a v → ¬ (SimpleGraph.cycleGraph 5).Adj u v →
    (b = a + 1 ∧ u = a + 2 ∧ v = a - 1) ∨
      (b = a - 1 ∧ u = a - 2 ∧ v = a + 1)) a b u v hab hub hav huv

set_option maxRecDepth 100000 in
set_option maxHeartbeats 2000000 in
/-- A singleton cycle-neighbor extends to a two-neighbor type compatible with
the entire opposite-side type set, not merely with one selected vertex. -/
theorem c5_singleton_extension (a : Fin 5) (B : Finset (Fin 5))
    (hB : B ⊆ c5Type a) (p : Fin 5) (hp : ∀ b ∈ B, p ∉ c5Type b) :
    ∃ i : Fin 5, p ∈ c5Type i ∧ ∀ b ∈ B, Disjoint (c5Type i) (c5Type b) := by
  exact (by decide : ∀ a : Fin 5, ∀ B : Finset (Fin 5), B ⊆ c5Type a →
    ∀ p : Fin 5, (∀ b ∈ B, p ∉ c5Type b) →
    ∃ i : Fin 5, p ∈ c5Type i ∧ ∀ b ∈ B, Disjoint (c5Type i) (c5Type b)) a B hB p hp

end EG617
