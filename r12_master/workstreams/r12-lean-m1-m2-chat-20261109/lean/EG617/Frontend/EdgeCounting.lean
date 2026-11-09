module

public import EG617.Frontend.ColoringReduction
public import Mathlib.Combinatorics.SimpleGraph.Finite
public import Mathlib.Algebra.BigOperators.Group.Finset.Basic

@[expose] public section

set_option autoImplicit false

open scoped BigOperators

attribute [local instance] Classical.propDecidable

namespace EG617

/-- The original color graph restricted to the actual vertices of `S`. -/
def inducedColorGraph (c : EdgeColoring) (i : Color) (S : Finset Vertex) :
    SimpleGraph S := (colorGraph c i).induce (S : Set Vertex)

/-- Unordered, loopless edges of one color inside `S`, counted once. -/
noncomputable def colorEdgeCount (c : EdgeColoring) (i : Color)
    (S : Finset Vertex) : ℕ := by
  classical
  exact (inducedColorGraph c i S).edgeFinset.card

/-- At the full vertex set this is exactly the edge count of the original color graph. -/
theorem colorEdgeCount_univ (c : EdgeColoring) (i : Color) :
    colorEdgeCount c i Finset.univ = (colorGraph c i).edgeFinset.card := by
  classical
  unfold colorEdgeCount inducedColorGraph
  simpa only [Finset.coe_univ] using
    (SimpleGraph.induceUnivIso (colorGraph c i)).card_edgeFinset_eq

/-- Explicit connection of induced adjacency to the original edge coloring. -/
theorem inducedColorGraph_adj_iff (c : EdgeColoring) (i : Color)
    (S : Finset Vertex) (u v : S) :
    (inducedColorGraph c i S).Adj u v ↔
      ∃ h : (u : Vertex) ≠ (v : Vertex), c (edgeOf u v h) = i := Iff.rfl

/-- Every original edge in an induced vertex set has exactly one color. -/
theorem induced_edge_unique_color (c : EdgeColoring) (S : Finset Vertex)
    (u v : S) (h : u ≠ v) :
    ∃! i : Color, (inducedColorGraph c i S).Adj u v := by
  exact colorGraph_partition c u v (fun huv => h (Subtype.ext huv))

theorem induced_color_edges_disjoint (c : EdgeColoring) (S : Finset Vertex) :
    ((Finset.univ : Finset Color) : Set Color).PairwiseDisjoint
      (fun i => (inducedColorGraph c i S).edgeFinset) := by
  classical
  intro i _ j _ hij
  apply Finset.disjoint_left.mpr
  intro e hei hej
  revert hei hej
  refine Sym2.inductionOn e ?_
  intro u v hei hej
  have hi : (inducedColorGraph c i S).Adj u v := by
    simpa only [SimpleGraph.mem_edgeFinset, SimpleGraph.mem_edgeSet] using hei
  have hj : (inducedColorGraph c j S).Adj u v := by
    simpa only [SimpleGraph.mem_edgeFinset, SimpleGraph.mem_edgeSet] using hej
  obtain ⟨_, hci⟩ := (inducedColorGraph_adj_iff c i S u v).mp hi
  obtain ⟨_, hcj⟩ := (inducedColorGraph_adj_iff c j S u v).mp hj
  exact hij (hci.symm.trans hcj)

theorem induced_color_edges_union (c : EdgeColoring) (S : Finset Vertex) :
    (Finset.univ.biUnion fun i : Color => (inducedColorGraph c i S).edgeFinset) =
      (⊤ : SimpleGraph S).edgeFinset := by
  classical
  ext e
  refine Sym2.inductionOn e ?_
  intro u v
  simp only [Finset.mem_biUnion, Finset.mem_univ, true_and,
    SimpleGraph.mem_edgeFinset, SimpleGraph.mem_edgeSet, SimpleGraph.top_adj]
  constructor
  · rintro ⟨i, hi⟩
    exact hi.ne
  · intro h
    obtain ⟨i, hi, _⟩ := induced_edge_unique_color c S u v h
    exact ⟨i, hi⟩

/-- Exact cross-color edge ledger; validity is not needed for this partition identity. -/
theorem sum_colorEdgeCount (c : EdgeColoring) (S : Finset Vertex) :
    ∑ i : Color, colorEdgeCount c i S = S.card.choose 2 := by
  classical
  unfold colorEdgeCount
  rw [← Finset.card_biUnion (induced_color_edges_disjoint c S),
    induced_color_edges_union, SimpleGraph.card_edgeFinset_top_eq_card_choose_two]
  simp

end EG617
