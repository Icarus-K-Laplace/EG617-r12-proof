module

public import Mathlib.Combinatorics.SimpleGraph.Basic

@[expose] public section

set_option autoImplicit false

namespace EG617

abbrev Vertex := Fin 145
abbrev Color := Fin 12

/-- An unordered pair of distinct vertices; the quotient removes orientation. -/
abbrev Edge := {e : Sym2 Vertex // ¬ e.IsDiag}
abbrev EdgeColoring := Edge → Color

def edgeOf (u v : Vertex) (h : u ≠ v) : Edge :=
  ⟨s(u, v), fun hd => h (Sym2.mk_isDiag_iff.mp hd)⟩

/-- Both endpoints belong to the vertex set. -/
def Inside (e : Edge) (S : Finset Vertex) : Prop :=
  ∀ v, v ∈ e.val → v ∈ S

theorem edgeOf_swap (u v : Vertex) (h : u ≠ v) :
    edgeOf u v h = edgeOf v u h.symm :=
  Subtype.ext Sym2.eq_swap

theorem edgeOf_eq_iff
    (u v x y : Vertex) (huv : u ≠ v) (hxy : x ≠ y) :
    edgeOf u v huv = edgeOf x y hxy ↔
      (u = x ∧ v = y) ∨ (u = y ∧ v = x) := by
  constructor
  · intro h
    exact Sym2.eq_iff.mp (congrArg Subtype.val h)
  · intro h
    apply Subtype.ext
    exact Sym2.eq_iff.mpr h

theorem edge_has_endpoints (e : Edge) :
    ∃ u v : Vertex, u ≠ v ∧ e.val = s(u, v) := by
  obtain ⟨uv, huv⟩ := Sym2.mk_surjective e.val
  refine ⟨uv.1, uv.2, ?_, huv.symm⟩
  intro h
  apply e.property
  rw [← huv]
  change (s(uv.1, uv.2)).IsDiag
  exact Sym2.mk_isDiag_iff.mpr h

theorem edgeOf_surjective (e : Edge) :
    ∃ u v : Vertex, ∃ h : u ≠ v, edgeOf u v h = e := by
  obtain ⟨u, v, h, he⟩ := edge_has_endpoints e
  exact ⟨u, v, h, Subtype.ext he.symm⟩

theorem edgeOf_inside_iff
    (u v : Vertex) (h : u ≠ v) (S : Finset Vertex) :
    Inside (edgeOf u v h) S ↔ u ∈ S ∧ v ∈ S := by
  constructor
  · intro hS
    exact ⟨hS u (Sym2.mem_mk_left u v),
      hS v (Sym2.mem_mk_right u v)⟩
  · rintro ⟨hu, hv⟩ w hw
    rcases Sym2.mem_iff.mp hw with rfl | rfl
    · exact hu
    · exact hv

theorem inside_mono {e : Edge} {S T : Finset Vertex}
    (hST : S ⊆ T) (he : Inside e S) : Inside e T :=
  fun v hv => hST (he v hv)

theorem mem_complete_iff (e : Sym2 Vertex) :
    e ∈ (SimpleGraph.completeGraph Vertex).edgeSet ↔ ¬ e.IsDiag :=
  Sym2.inductionOn e (fun _ _ => Iff.rfl)

/-- Identity on unordered pairs, with both inverse laws proved. -/
def edgeEquivComplete :
    Edge ≃ (SimpleGraph.completeGraph Vertex).edgeSet where
  toFun e := ⟨e.val, (mem_complete_iff e.val).mpr e.property⟩
  invFun e := ⟨e.val, (mem_complete_iff e.val).mp e.property⟩
  left_inv _ := Subtype.ext rfl
  right_inv _ := Subtype.ext rfl

end EG617
