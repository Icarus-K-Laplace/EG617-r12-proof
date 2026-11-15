module
public import EG617.Core.C5MissingTypeFibers

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Actual-vertex adjacency and all cyclic fiber sizes for C5(9,9,2,1,2). -/
def R23ExceptionalProfile (G : SimpleGraph V) : Prop :=
  ∃ (t : V → Fin 5) (c : Fin 5),
    (∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y)) ∧
    (Finset.univ.filter (fun x => t x = c)).card = 9 ∧
    (Finset.univ.filter (fun x => t x = c + 1)).card = 9 ∧
    (Finset.univ.filter (fun x => t x = c + 2)).card = 2 ∧
    (Finset.univ.filter (fun x => t x = c - 2)).card = 1 ∧
    (Finset.univ.filter (fun x => t x = c - 1)).card = 2

/-- Frozen M2d: complete the compatible missing edge, or identify every actual
vertex and adjacency with the exceptional C5 blow-up. -/
theorem missing_exterior_completion_or_exceptional (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 121)
    (hm : R23MissingEdgeExterior G) :
    R23OneEdgeCompletion G ∨ R23ExceptionalProfile G := by
  classical
  obtain ⟨S, f, hf, hl, A, hA, hB, h9, h9', h80, u, hu, v, hv, hmiss⟩ := hm
  let T := Sᶜ
  let P : Finset V := A.image (fun a : (T : Set V) => (a : V))
  let Q : Finset V := (Aᶜ : Finset (T : Set V)).image (fun b : (T : Set V) => (b : V))
  have hP : P.card = 9 := by
    rw [Finset.card_image_of_injective _ Subtype.val_injective]
    exact h9
  have hQ : Q.card = 9 := by
    rw [Finset.card_image_of_injective _ Subtype.val_injective]
    simpa only [Finset.card_compl, Set.fintypeCard_eq_ncard] using h9'
  have hcover : P ∪ Q = Sᶜ := by
    ext x
    rw [Finset.mem_union]
    constructor
    · rintro (hx | hx)
      · obtain ⟨a, _, rfl⟩ := Finset.mem_image.mp hx
        exact a.property
      · obtain ⟨b, _, rfl⟩ := Finset.mem_image.mp hx
        exact b.property
    · intro hx
      let z : (T : Set V) := ⟨x, hx⟩
      by_cases hz : z ∈ A
      · exact Or.inl (Finset.mem_image.mpr ⟨z, hz, rfl⟩)
      · exact Or.inr (Finset.mem_image.mpr ⟨z, Finset.mem_compl.mpr hz, rfl⟩)
  have hdis : Disjoint P Q := by
    rw [Finset.disjoint_left]
    intro x hx hy
    obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨b, hb, hba⟩ := Finset.mem_image.mp hy
    have hba' : b = a := Subtype.ext hba
    subst b
    exact Finset.mem_compl.mp hb ha
  have hPi : G.IsIndepSet (P : Set V) := by
    intro x hx y hy hxy
    obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hy
    exact hA ha hb (fun h => hxy (congrArg Subtype.val h))
  have hQi : G.IsIndepSet (Q : Set V) := by
    intro x hx y hy hxy
    obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hy
    exact hB (by simpa only [Finset.mem_coe, Finset.mem_compl] using ha)
      (by simpa only [Finset.mem_coe, Finset.mem_compl] using hb) (fun h => hxy (congrArg Subtype.val h))
  have huP : u.val ∈ P := Finset.mem_image.mpr ⟨u, hu, rfl⟩
  have hvQ : v.val ∈ Q := Finset.mem_image.mpr ⟨v, by simpa only [Finset.mem_compl] using hv, rfl⟩
  have hcross : ∀ x ∈ P, ∀ y ∈ Q, (¬ G.Adj x y ↔ x = u.val ∧ y = v.val) := by
    intro x hx y hy
    obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hy
    have hh := hmiss a ha b (by simpa only [Finset.mem_compl] using hb)
    constructor
    · intro hn
      have h := hh.mp hn
      exact ⟨congrArg Subtype.val h.1, congrArg Subtype.val h.2⟩
    · rintro ⟨h1, h2⟩
      exact hh.mpr ⟨Subtype.ext h1, Subtype.ext h2⟩
  have hne : u.val ≠ v.val := by
    intro h
    exact Finset.disjoint_left.mp hdis huP (h.symm ▸ hvQ)
  have hn : ¬ G.Adj u.val v.val := (hcross u.val huP v.val hvQ).mpr ⟨rfl, rfl⟩
  have hd : ∀ x ∈ Sᶜ, (S.filter (G.Adj x)).card = 2 := by
    have hdist := hl.2.2.2.2.2.2.2.2.2.2.2.1
    rcases hdist with h | h | h
    · exact h.2.2.2
    · have hh : coreInducedEdgeCount G Sᶜ = 81 := h.1
      omega
    · have hh : coreInducedEdgeCount G Sᶜ = 81 := h.1
      omega
  obtain ⟨t, hlabels⟩ := exists_cycle_type_assignment f ht S hf hd
  by_cases hc : (SimpleGraph.cycleGraph 5).Adj (t u.val) (t v.val)
  · left
    have hlabelsDisjoint : Disjoint (cycleNeighborLabels f u.val) (cycleNeighborLabels f v.val) := by
      rw [hlabels u.val, hlabels v.val]
      exact (c5Type_disjoint_iff _ _).mpr hc
    have hcommon := disjoint_cycle_neighbors_no_common_neighbor f S P Q hf hcover
      hPi hQi u.val v.val huP hvQ hlabelsDisjoint
    exact ⟨u.val, v.val, hne, hn,
      r23_one_edge_completion_case_I G hV ht hI he u.val v.val hne hn hcommon⟩
  · right
    have hPe : (P.erase u.val).Nonempty := by
      apply Finset.card_pos.mp
      rw [Finset.card_erase_of_mem huP, hP]
      decide
    have hQe : (Q.erase v.val).Nonempty := by
      apply Finset.card_pos.mp
      rw [Finset.card_erase_of_mem hvQ, hQ]
      decide
    obtain ⟨a, b, hAt, hBt, ho⟩ := missing_exterior_type_orientations
      f ht P Q u.val v.val huP hvQ hPe hQe t hlabels hcross hc
    have hcycle : ∀ i, t (f i) = i := by
      intro i
      have hi := cycleNeighborLabels_cycle_vertex f ht i
      have hcard : (cycleNeighborLabels f (f i)).card = 2 := by rw [hi, c5Type_card]
      exact (cycleNeighborLabels_unique_type f ht (f i) hcard).unique (hlabels (f i)) hi
    have hformula := missing_exterior_type_fiber_formula f S P Q hf hcover hdis hP hQ
      u.val v.val huP hvQ t hcycle a b hAt hBt
    obtain ⟨c, hcs⟩ := c5_missing_fiber_profile
      (fun i => (Finset.univ.filter (fun x => t x = i)).card) a b (t u.val) (t v.val) hformula ho
    exact ⟨t, c, missing_exterior_type_presentation f ht S P Q hf hcover u.val v.val
      hPe hQe t hlabels hcross hc, hcs⟩

/-- Complete frozen M2 classification from the original dense R23 contract.
Every graph is Case I, a single-edge deletion of a Case I graph, or the
exceptional C5(9,9,2,1,2). No classification/ledger/type hypothesis is assumed. -/
theorem r23_complete_classification (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    R23CaseIProfile G ∨ R23OneEdgeCompletion G ∨ R23ExceptionalProfile G := by
  classical
  obtain ⟨v, p, _, _, _, hl⟩ := r23_exact_neighbor_ledger G hV ht hI he
  have hupper : G.edgeFinset.card ≤ 122 := hl.2.2.2.2.2.2.2.1
  have hcases : G.edgeFinset.card = 121 ∨ G.edgeFinset.card = 122 := by omega
  rcases hcases with h121 | h122
  · rcases r23_121_completion_or_missing_exterior G hV ht hI h121 with hcomp | hmiss
    · exact Or.inr (Or.inl hcomp)
    · exact Or.inr (missing_exterior_completion_or_exceptional G hV ht hI h121 hmiss)
  · exact Or.inl (r23_122_case_I G hV ht hI h122)

end EG617
