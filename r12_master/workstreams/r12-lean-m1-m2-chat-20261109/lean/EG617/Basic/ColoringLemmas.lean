module

public import EG617.Basic.OriginalProblem

@[expose] public section

set_option autoImplicit false

namespace EG617

/-- The graph consisting precisely of the edges assigned color i. -/
def colorGraph (c : EdgeColoring) (i : Color) : SimpleGraph Vertex where
  Adj u v := ∃ h : u ≠ v, c (edgeOf u v h) = i
  symm.symm u v h := by
    obtain ⟨hne, hc⟩ := h
    refine ⟨hne.symm, ?_⟩
    rw [← edgeOf_swap u v hne]
    exact hc
  loopless.irrefl u := by
    rintro ⟨h, _⟩
    exact h rfl

theorem colorGraph_adj_iff (c : EdgeColoring) (i : Color)
    (u v : Vertex) (h : u ≠ v) :
    (colorGraph c i).Adj u v ↔ c (edgeOf u v h) = i := by
  constructor
  · rintro ⟨_, hc⟩
    exact hc
  · intro hc
    exact ⟨h, hc⟩

theorem validColoring_iff_colorGraph (c : EdgeColoring) :
    ValidColoring c ↔ ∀ S : Finset Vertex, S.card = 13 →
      ∀ i : Color, ∃ u ∈ S, ∃ v ∈ S, (colorGraph c i).Adj u v := by
  rw [validColoring_iff_endpoints]
  rfl

theorem colorGraph_partition (c : EdgeColoring) (u v : Vertex) (h : u ≠ v) :
    ∃! i : Color, (colorGraph c i).Adj u v := by
  refine ⟨c (edgeOf u v h), ⟨h, rfl⟩, ?_⟩
  intro i hi
  exact ((colorGraph_adj_iff c i u v h).mp hi).symm

/-- The first exact frontend consequence: no independent 13-set in a color. -/
theorem no_independent_thirteen (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (hS : S.card = 13) (i : Color) :
    ¬ (∀ u ∈ S, ∀ v ∈ S, ¬ (colorGraph c i).Adj u v) := by
  intro hind
  obtain ⟨u, hu, v, hv, huv⟩ :=
    (validColoring_iff_colorGraph c).mp hc S hS i
  exact hind u hu v hv huv

/-- A monochromatic 13-set would omit a distinct color. -/
theorem no_monochromatic_thirteen (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (hS : S.card = 13) (i : Color) :
    ¬ (∀ u ∈ S, ∀ v ∈ S, ∀ h : u ≠ v, c (edgeOf u v h) = i) := by
  intro hmono
  obtain ⟨j, hji⟩ := exists_ne i
  obtain ⟨u, hu, v, hv, h, hj⟩ :=
    (validColoring_iff_endpoints c).mp hc S hS j
  exact hji (hj.symm.trans (hmono u hu v hv h))

end EG617
