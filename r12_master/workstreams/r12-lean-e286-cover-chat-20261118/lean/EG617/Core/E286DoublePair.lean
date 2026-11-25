module
public import EG617.Core.E286H4Second

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- The three equality thresholds used in frozen Sections 7 and 9. -/
def E286PairThreshold (s t m : ℕ) : Prop :=
  (s = 9 ∧ t = 11 ∧ m = 2) ∨ (s = 10 ∧ t = 10 ∧ m = 2) ∨
  (s = 10 ∧ t = 11 ∧ m = 4)

theorem e286_threshold_scalar_rigidity (s t m a b : ℕ) (shape : E286PairThreshold s t m)
    (ha : 0 < a) (hb : 0 < b) (has : a ≤ s) (hbt : b ≤ t)
    (budget : (s+t-12-a-b) + a*(s+b-13) + b*(t+a-13) ≤ m) :
    s+b = 13 ∧ t+a = 13 ∧ s+t-12-a-b = m := by
  rcases shape with ⟨rfl,rfl,rfl⟩ | ⟨rfl,rfl,rfl⟩ | ⟨rfl,rfl,rfl⟩ <;>
    interval_cases a <;> interval_cases b <;> norm_num at *

theorem e286_missing_of_incomplete (G : SimpleGraph V) (K : Finset V) (z : V)
    (h : ¬ ∀ x ∈ K, G.Adj z x) : (e286Missing G K z).Nonempty := by
  classical
  push_neg at h
  obtain ⟨x,hx,hn⟩ := h
  exact ⟨x, Finset.mem_filter.mpr ⟨hx,hn⟩⟩

/-- At the threshold, a point missing both actual cliques consumes the
entire local budget, and the two missing sizes saturate the internal degree bound. -/
theorem e286_pair_threshold_rigidity (G : SimpleGraph V) (K L : Finset V) (z : V)
    (m : ℕ) (shape : E286PairThreshold K.card L.card m)
    (hK : G.IsClique (K : Set V)) (hL : G.IsClique (L : Set V)) (dis : Disjoint K L)
    (zK : z ∉ K) (zL : z ∉ L)
    (ha : (e286Missing G K z).Nonempty) (hb : (e286Missing G L z).Nonempty)
    (edge : ∀ x ∈ e286Missing G K z, ∀ y ∈ e286Missing G L z, G.Adj x y)
    (budget : (∑ x ∈ insert z (K ∪ L), degreeExcess12 G x) ≤ m) :
    K.card + (e286Missing G L z).card = 13 ∧
    L.card + (e286Missing G K z).card = 13 ∧ m ≤ degreeExcess12 G z := by
  classical
  let A := e286Missing G K z
  let B := e286Missing G L z
  have sa : A ⊆ K := Finset.filter_subset _ _
  have sb : B ⊆ L := Finset.filter_subset _ _
  have first (x : V) (hx : x ∈ A) : K.card + B.card - 13 ≤ degreeExcess12 G x := by
    have h := e286_clique_blocker_vertex_charge G K B hK (dis.mono_right sb) x (sa hx) (edge x hx)
    omega
  have second (y : V) (hy : y ∈ B) : L.card + A.card - 13 ≤ degreeExcess12 G y := by
    have h := e286_clique_blocker_vertex_charge G L A hL (dis.symm.mono_right sa) y (sb hy)
      (fun x hx => (edge x hx y hy).symm)
    omega
  have fa := Finset.sum_le_sum first
  have fb := Finset.sum_le_sum second
  simp only [Finset.sum_const, smul_eq_mul] at fa fb
  have subA : (∑ x ∈ A, degreeExcess12 G x) ≤ ∑ x ∈ K, degreeExcess12 G x :=
    Finset.sum_le_sum_of_subset sa
  have subB : (∑ x ∈ B, degreeExcess12 G x) ≤ ∑ x ∈ L, degreeExcess12 G x :=
    Finset.sum_le_sum_of_subset sb
  have point := e286_pair_point_degree_charge G K L dis z
  change K.card + L.card ≤ 12 + degreeExcess12 G z + A.card + B.card at point
  rw [Finset.sum_insert (show z ∉ K ∪ L by simp [zK,zL]), Finset.sum_union dis] at budget
  obtain ⟨ea,eb,ez⟩ := e286_threshold_scalar_rigidity K.card L.card m A.card B.card shape
    (Finset.card_pos.mpr ha) (Finset.card_pos.mpr hb) (Finset.card_le_card sa) (Finset.card_le_card sb)
    (by omega)
  exact ⟨ea,eb,by omega⟩

/-- Each point of a doubled pair under its threshold must complete a side.
The scalar rigidity applies in both orders to the same two actual cliques. -/
theorem e286_doubled_pair_completion (G : SimpleGraph V) (K L : Finset V)
    (z w : V) (m : ℕ) (shape : E286PairThreshold K.card L.card m)
    (hK : G.IsClique (K : Set V)) (hL : G.IsClique (L : Set V)) (dis : Disjoint K L)
    (hne : z ≠ w) (zK : z ∉ K) (zL : z ∉ L) (wK : w ∉ K) (wL : w ∉ L)
    (ez : ∀ x ∈ e286Missing G K z, ∀ y ∈ e286Missing G L z, G.Adj x y)
    (ew : ∀ x ∈ e286Missing G K w, ∀ y ∈ e286Missing G L w, G.Adj x y)
    (budget : (∑ x ∈ insert z (insert w (K ∪ L)), degreeExcess12 G x) ≤ m) :
    (∀ x ∈ K, G.Adj z x) ∨ (∀ y ∈ L, G.Adj z y) := by
  classical
  by_cases zk : ∀ x ∈ K, G.Adj z x
  · exact Or.inl zk
  by_cases zl : ∀ y ∈ L, G.Adj z y
  · exact Or.inr zl
  exfalso
  let A := e286Missing G K z
  let B := e286Missing G L z
  have sa : A ⊆ K := Finset.filter_subset _ _
  have sb : B ⊆ L := Finset.filter_subset _ _
  have ha : A.Nonempty := e286_missing_of_incomplete G K z zk
  have hb : B.Nonempty := e286_missing_of_incomplete G L z zl
  have boundZ : (∑ x ∈ insert z (K ∪ L), degreeExcess12 G x) ≤ m :=
    (Finset.sum_le_sum_of_subset (Finset.insert_subset_insert z (Finset.subset_insert w _))).trans budget
  have boundW : (∑ x ∈ insert w (K ∪ L), degreeExcess12 G x) ≤ m :=
    (Finset.sum_le_sum_of_subset (Finset.subset_insert z _)).trans budget
  obtain ⟨sizeK,sizeL,expZ⟩ := e286_pair_threshold_rigidity G K L z m shape hK hL dis zK zL ha hb ez boundZ
  change K.card + B.card = 13 at sizeK
  change L.card + A.card = 13 at sizeL
  rw [Finset.sum_insert (show z ∉ insert w (K ∪ L) by simp [hne,zK,zL]),
    Finset.sum_insert (show w ∉ K ∪ L by simp [wK,wL])] at budget
  have zero (x : V) (hx : x ∈ K ∪ L) : degreeExcess12 G x = 0 := by
    have h : (∑ v ∈ ({x} : Finset V), degreeExcess12 G v) ≤ ∑ v ∈ K ∪ L, degreeExcess12 G v :=
      Finset.sum_le_sum_of_subset (Finset.singleton_subset_iff.mpr hx)
    rw [Finset.sum_singleton] at h
    omega
  by_cases wk : ∀ x ∈ K, G.Adj w x
  · obtain ⟨x,hx⟩ := ha
    have h := e286_clique_charge_with_extra G K B hK (dis.mono_right sb) w x wK
      (fun hm => wL (sb hm)) (sa hx) (wk x (sa hx)).symm (ez x hx)
    have h0 := zero x (Finset.mem_union_left L (sa hx))
    omega
  by_cases wl : ∀ y ∈ L, G.Adj w y
  · obtain ⟨y,hy⟩ := hb
    have h := e286_clique_charge_with_extra G L A hL (dis.symm.mono_right sa) w y wL
      (fun hm => wK (sa hm)) (sb hy) (wl y (sb hy)).symm (fun x hx => (ez x hx y hy).symm)
    have h0 := zero y (Finset.mem_union_right K (sb hy))
    omega
  have expW := (e286_pair_threshold_rigidity G K L w m shape hK hL dis wK wL
    (e286_missing_of_incomplete G K w wk) (e286_missing_of_incomplete G L w wl) ew boundW).2.2
  have pos : 0 < m := by rcases shape with h | h | h <;> omega
  omega

end EG617
