module

public import EG617.Basic.ColoringLemmas
public import Mathlib.Data.Finset.Card

@[expose] public section

set_option autoImplicit false

namespace EG617

/-- Every finite independent vertex set in each color graph has at most 12 vertices. -/
theorem independent_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hind : ∀ u ∈ S, ∀ v ∈ S, ¬ (colorGraph c i).Adj u v) :
    S.card ≤ 12 := by
  classical
  by_contra hlarge
  have h13 : 13 ≤ S.card := Nat.succ_le_of_lt (Nat.lt_of_not_ge hlarge)
  obtain ⟨T, hTS, hT⟩ := Finset.exists_subset_card_eq h13
  apply no_independent_thirteen c hc T hT i
  intro u hu v hv
  exact hind u (hTS hu) v (hTS hv)

/-- Every monochromatic finite vertex set has at most 12 vertices. -/
theorem monochromatic_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hmono : ∀ u ∈ S, ∀ v ∈ S, ∀ h : u ≠ v, c (edgeOf u v h) = i) :
    S.card ≤ 12 := by
  classical
  by_contra hlarge
  have h13 : 13 ≤ S.card := Nat.succ_le_of_lt (Nat.lt_of_not_ge hlarge)
  obtain ⟨T, hTS, hT⟩ := Finset.exists_subset_card_eq h13
  apply no_monochromatic_thirteen c hc T hT i
  intro u hu v hv hne
  exact hmono u (hTS hu) v (hTS hv) hne

/-- The same clique bound expressed directly with the color graph's adjacency relation. -/
theorem colorGraph_clique_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hclique : ∀ u ∈ S, ∀ v ∈ S, u ≠ v → (colorGraph c i).Adj u v) :
    S.card ≤ 12 := by
  apply monochromatic_card_le_twelve c hc S i
  intro u hu v hv hne
  exact (colorGraph_adj_iff c i u v hne).mp (hclique u hu v hv hne)

end EG617
