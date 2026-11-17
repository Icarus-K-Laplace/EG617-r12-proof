module
public import EG617.Core.C5MissingGraphLift

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V] {G : SimpleGraph V}

/-- Actual missing-edge constraints force constant types on both eight-point
remainders, with every endpoint orientation included. -/
theorem missing_exterior_type_orientations
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (ht : G.CliqueFree 3)
    (A B : Finset V) (u v : V) (hu : u ∈ A) (hv : v ∈ B)
    (hA : (A.erase u).Nonempty) (hB : (B.erase v).Nonempty)
    (t : V → Fin 5) (hlabels : ∀ x, cycleNeighborLabels f x = c5Type (t x))
    (hmiss : ∀ x ∈ A, ∀ y ∈ B, (¬ G.Adj x y ↔ x = u ∧ y = v))
    (hincompat : ¬ (SimpleGraph.cycleGraph 5).Adj (t u) (t v)) :
    ∃ a b : Fin 5, (∀ x ∈ A.erase u, t x = a) ∧
      (∀ y ∈ B.erase v, t y = b) ∧
      ((b = a + 1 ∧ t u = a + 2 ∧ t v = a - 1) ∨
       (b = a - 1 ∧ t u = a - 2 ∧ t v = a + 1)) := by
  classical
  have hforward : ∀ {x y}, G.Adj x y → (SimpleGraph.cycleGraph 5).Adj (t x) (t y) := by
    intro x y hxy
    have h := adjacent_cycleNeighborLabels_disjoint f ht hxy
    rw [hlabels x, hlabels y] at h
    exact (c5Type_disjoint_iff _ _).mp h
  have hcross : ∀ x ∈ A, ∀ y ∈ B, x ≠ u ∨ y ≠ v → G.Adj x y := by
    intro x hx y hy hn
    by_contra h
    have he := (hmiss x hx y hy).mp h
    rcases hn with hn | hn
    · exact hn he.1
    · exact hn he.2
  let X := (A.erase u).image t
  let Y := (B.erase v).image t
  have hXY : ∀ a ∈ X, ∀ b ∈ Y, (SimpleGraph.cycleGraph 5).Adj a b := by
    intro a ha b hb
    obtain ⟨x, hx, rfl⟩ := Finset.mem_image.mp ha
    obtain ⟨y, hy, rfl⟩ := Finset.mem_image.mp hb
    exact hforward (hcross x (Finset.mem_erase.mp hx).2 y (Finset.mem_erase.mp hy).2
      (Or.inl (Finset.mem_erase.mp hx).1))
  have huY : ∀ b ∈ Y, (SimpleGraph.cycleGraph 5).Adj (t u) b := by
    intro b hb
    obtain ⟨y, hy, rfl⟩ := Finset.mem_image.mp hb
    exact hforward (hcross u hu y (Finset.mem_erase.mp hy).2 (Or.inr (Finset.mem_erase.mp hy).1))
  have hXv : ∀ a ∈ X, (SimpleGraph.cycleGraph 5).Adj a (t v) := by
    intro a ha
    obtain ⟨x, hx, rfl⟩ := Finset.mem_image.mp ha
    exact hforward (hcross x (Finset.mem_erase.mp hx).2 v hv (Or.inl (Finset.mem_erase.mp hx).1))
  have hsingle := c5_missing_edge_type_sets X Y (hA.image t) (hB.image t)
    (t u) (t v) hXY huY hXv hincompat
  obtain ⟨a, ha⟩ := Finset.card_eq_one.mp hsingle.1
  obtain ⟨b, hb⟩ := Finset.card_eq_one.mp hsingle.2
  have haX : a ∈ X := by rw [ha]; exact Finset.mem_singleton_self a
  have hbY : b ∈ Y := by rw [hb]; exact Finset.mem_singleton_self b
  refine ⟨a, b, ?_, ?_, c5_missing_endpoint_orientations a b (t u) (t v)
    (hXY a haX b hbY) (huY b hbY) (hXv a haX) hincompat⟩
  · intro x hx
    have hm : t x ∈ X := Finset.mem_image.mpr ⟨x, hx, rfl⟩
    rw [ha] at hm
    exact Finset.mem_singleton.mp hm
  · intro y hy
    have hm : t y ∈ Y := Finset.mem_image.mpr ⟨y, hy, rfl⟩
    rw [hb] at hm
    exact Finset.mem_singleton.mp hm

/-- Exact size of a type fiber on a nine-point part with one exceptional vertex. -/
theorem one_exception_type_fiber_card (C : Finset V) (t : V → Fin 5)
    (u : V) (hu : u ∈ C) (hc : C.card = 9) (a i : Fin 5)
    (hrest : ∀ x ∈ C.erase u, t x = a) :
    (C.filter (fun x => t x = i)).card =
      (if a = i then 8 else 0) + (if t u = i then 1 else 0) := by
  classical
  have hrc : ((C.erase u).filter (fun x => t x = i)).card = (if a = i then 8 else 0) := by
    by_cases hai : a = i
    · have hf : (C.erase u).filter (fun x => t x = i) = C.erase u :=
        Finset.filter_eq_self.mpr (fun x hx => (hrest x hx).trans hai)
      rw [hf, Finset.card_erase_of_mem hu, hc]
      simp [hai]
    · have hf : (C.erase u).filter (fun x => t x = i) = ∅ := by
        apply Finset.eq_empty_iff_forall_notMem.mpr
        intro x hx
        have hm := Finset.mem_filter.mp hx
        exact hai ((hrest x hm.1).symm.trans hm.2)
      simp [hf, hai]
  have hfilter := congrArg (fun D : Finset V => (D.filter (fun x => t x = i)).card)
    (Finset.insert_erase hu)
  have hnot : u ∉ (C.erase u).filter (fun x => t x = i) := by
    intro h
    exact (Finset.mem_erase.mp (Finset.mem_filter.mp h).1).1 rfl
  by_cases hui : t u = i
  · simp only [Finset.filter_insert, hui, if_true, Finset.card_insert_of_notMem hnot, hrc] at hfilter
    simpa only [hui, if_true] using hfilter.symm
  · simp only [Finset.filter_insert, hui, if_false, hrc] at hfilter
    simpa only [hui, if_false, Nat.add_zero] using hfilter.symm

/-- All vertex fibers are counted exactly: one cycle vertex, two eight-point
remainders, and the two exceptional endpoints. -/
theorem missing_exterior_type_fiber_formula
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (S A B : Finset V)
    (hS : Finset.univ.image f = S) (hcover : A ∪ B = Sᶜ) (hdis : Disjoint A B)
    (hA : A.card = 9) (hB : B.card = 9) (u v : V) (hu : u ∈ A) (hv : v ∈ B)
    (t : V → Fin 5) (hcycle : ∀ i, t (f i) = i) (a b : Fin 5)
    (hAt : ∀ x ∈ A.erase u, t x = a) (hBt : ∀ y ∈ B.erase v, t y = b) :
    ∀ i : Fin 5, (Finset.univ.filter (fun x => t x = i)).card =
      1 + (if a = i then 8 else 0) + (if b = i then 8 else 0) +
        (if t u = i then 1 else 0) + (if t v = i then 1 else 0) := by
  classical
  intro i
  have hd : Disjoint (A.filter (fun x => t x = i)) (B.filter (fun x => t x = i)) :=
    hdis.mono (Finset.filter_subset _ _) (Finset.filter_subset _ _)
  rw [cycle_type_fiber_card f S hS t hcycle i, ← hcover,
    Finset.filter_union, Finset.card_union_of_disjoint hd,
    one_exception_type_fiber_card A t u hu hA a i hAt,
    one_exception_type_fiber_card B t v hv hB b i hBt]
  omega

/-- Both orientations of all five cycle rotations yield the exceptional profile. -/
theorem c5_missing_fiber_profile (n : Fin 5 → ℕ) (a b u v : Fin 5)
    (hn : ∀ i, n i = 1 + (if a = i then 8 else 0) + (if b = i then 8 else 0) +
      (if u = i then 1 else 0) + (if v = i then 1 else 0))
    (ho : (b = a + 1 ∧ u = a + 2 ∧ v = a - 1) ∨
      (b = a - 1 ∧ u = a - 2 ∧ v = a + 1)) :
    ∃ c : Fin 5, n c = 9 ∧ n (c + 1) = 9 ∧ n (c + 2) = 2 ∧
      n (c - 2) = 1 ∧ n (c - 1) = 2 := by
  rcases ho with ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩
  · refine ⟨a, ?_, ?_, ?_, ?_, ?_⟩ <;> rw [hn] <;> fin_cases a <;> decide
  · refine ⟨a - 1, ?_, ?_, ?_, ?_, ?_⟩ <;> rw [hn] <;> fin_cases a <;> decide

end EG617
