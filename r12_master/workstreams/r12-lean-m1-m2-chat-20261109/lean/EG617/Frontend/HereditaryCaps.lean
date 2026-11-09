module

public import EG617.Frontend.TuranBounds
public import Mathlib.Order.Bounds.Basic
public import Mathlib.Data.Finset.Max
public import Mathlib.Algebra.Order.BigOperators.Group.Finset

@[expose] public section

set_option autoImplicit false

open scoped BigOperators

attribute [local instance] Classical.propDecidable

namespace EG617

/-- The paper's hereditary cap. The stronger additive inequality below certifies
the subtraction on every vertex set arising from a valid coloring. -/
def D (n : ℕ) : ℕ := n.choose 2 - 11 * tau12 n

/-- The eleven other colors consume at least eleven copies of the Turan floor. -/
theorem colorEdgeCount_add_eleven_tau_le (c : EdgeColoring)
    (hc : ValidColoring c) (i : Color) (S : Finset Vertex) :
    colorEdgeCount c i S + 11 * tau12 S.card ≤ S.card.choose 2 := by
  classical
  have hrest : 11 * tau12 S.card ≤
      ∑ j ∈ (Finset.univ : Finset Color).erase i, colorEdgeCount c j S := by
    calc
      11 * tau12 S.card =
          ∑ _j ∈ (Finset.univ : Finset Color).erase i, tau12 S.card := by
        simp [Color]
      _ ≤ ∑ j ∈ (Finset.univ : Finset Color).erase i, colorEdgeCount c j S := by
        exact Finset.sum_le_sum (fun j _ => tau12_le_colorEdgeCount c hc j S)
  have htotal :
      (∑ j ∈ (Finset.univ : Finset Color).erase i, colorEdgeCount c j S) +
        colorEdgeCount c i S = S.card.choose 2 := by
    rw [Finset.sum_erase_add _ _ (Finset.mem_univ i), sum_colorEdgeCount]
  omega

/-- The paper's cap holds for every color and every actual induced vertex set. -/
theorem hereditary_color_cap (c : EdgeColoring) (hc : ValidColoring c)
    (i : Color) (S : Finset Vertex) : colorEdgeCount c i S ≤ D S.card := by
  have h := colorEdgeCount_add_eleven_tau_le c hc i S
  unfold D
  omega

/-- On every actual vertex set, `D` is the paper's exact difference, not a bound
made weaker by truncated natural-number subtraction. -/
theorem hereditary_cap_subtraction_exact (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) : D S.card + 11 * tau12 S.card = S.card.choose 2 := by
  have h := colorEdgeCount_add_eleven_tau_le c hc (0 : Color) S
  unfold D
  omega

/-- A least color exists for every original coloring, without a validity premise. -/
theorem exists_least_color (c : EdgeColoring) :
    ∃ i : Color, ∀ j : Color,
      colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ := by
  classical
  obtain ⟨i, _, hi⟩ := (Finset.univ : Finset Color).exists_min_image
    (fun j => colorEdgeCount c j Finset.univ) Finset.univ_nonempty
  exact ⟨i, fun j => hi j (Finset.mem_univ j)⟩

/-- The exact K145 edge ledger yields the 870-edge bound for any least color. -/
theorem least_color_edgeCount_le_870 (c : EdgeColoring) (i : Color)
    (hi : ∀ j : Color,
      colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ) :
    colorEdgeCount c i Finset.univ ≤ 870 := by
  classical
  have htotal : ∑ j : Color, colorEdgeCount c j Finset.univ = 10440 := by
    simpa [Vertex] using sum_colorEdgeCount c Finset.univ
  have hsum : 12 * colorEdgeCount c i Finset.univ ≤ 10440 := by
    calc
      12 * colorEdgeCount c i Finset.univ =
          ∑ _j : Color, colorEdgeCount c i Finset.univ := by simp [Color]
      _ ≤ ∑ j : Color, colorEdgeCount c j Finset.univ :=
        Finset.sum_le_sum (fun j _ => hi j)
      _ = 10440 := htotal
  omega

/-- The least-color edge conclusions of the frozen paper's hereditary-caps lemma.
The only graph-theoretic premise is the complete original coloring condition. -/
theorem exists_least_color_with_hereditary_cap (c : EdgeColoring)
    (hc : ValidColoring c) :
    ∃ i : Color,
      (∀ j : Color, colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ) ∧
      colorEdgeCount c i Finset.univ ≤ 870 ∧
      (∀ S : Finset Vertex, colorEdgeCount c i S ≤ D S.card) := by
  obtain ⟨i, hi⟩ := exists_least_color c
  exact ⟨i, hi, least_color_edgeCount_le_870 c i hi, hereditary_color_cap c hc i⟩

/-- The same 870-edge conclusion expressed in the original `colorGraph` API. -/
theorem exists_colorGraph_card_edgeFinset_le_870 (c : EdgeColoring) :
    ∃ i : Color, (colorGraph c i).edgeFinset.card ≤ 870 := by
  obtain ⟨i, hi⟩ := exists_least_color c
  exact ⟨i, (colorEdgeCount_univ c i) ▸ least_color_edgeCount_le_870 c i hi⟩

end EG617
