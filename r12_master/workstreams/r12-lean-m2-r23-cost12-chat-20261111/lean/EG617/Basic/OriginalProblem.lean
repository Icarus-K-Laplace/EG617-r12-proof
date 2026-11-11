module

public import EG617.Basic.Definitions

@[expose] public section

set_option autoImplicit false

namespace EG617

/-- Every 13-vertex set contains an edge of every one of the twelve colors. -/
def ValidColoring (c : EdgeColoring) : Prop :=
  ∀ S : Finset Vertex, S.card = 13 →
    ∀ i : Color, ∃ e : Edge, Inside e S ∧ c e = i

/-- The original target proposition. This definition does not prove it. -/
def EG617R12Statement : Prop :=
  ¬ ∃ c : EdgeColoring, ValidColoring c

/-- An independent endpoint formulation of the same coloring condition. -/
theorem validColoring_iff_endpoints (c : EdgeColoring) :
    ValidColoring c ↔
      ∀ S : Finset Vertex, S.card = 13 → ∀ i : Color,
        ∃ u ∈ S, ∃ v ∈ S, ∃ h : u ≠ v, c (edgeOf u v h) = i := by
  constructor
  · intro hc S hS i
    obtain ⟨e, he, hcol⟩ := hc S hS i
    obtain ⟨u, v, h, rfl⟩ := edgeOf_surjective e
    obtain ⟨hu, hv⟩ := (edgeOf_inside_iff u v h S).mp he
    exact ⟨u, hu, v, hv, h, hcol⟩
  · intro hc S hS i
    obtain ⟨u, hu, v, hv, h, hcol⟩ := hc S hS i
    exact ⟨edgeOf u v h, (edgeOf_inside_iff u v h S).mpr ⟨hu, hv⟩, hcol⟩

/-- Equivalent missing-color statement, without claiming either side is proved. -/
theorem originalProblem_iff_missingColor :
    EG617R12Statement ↔
      ∀ c : EdgeColoring, ∃ S : Finset Vertex, S.card = 13 ∧
        ∃ i : Color, ∀ e : Edge, Inside e S → c e ≠ i := by
  classical
  simp only [EG617R12Statement, ValidColoring, not_exists, not_forall,
    not_and, exists_prop]
  
end EG617
