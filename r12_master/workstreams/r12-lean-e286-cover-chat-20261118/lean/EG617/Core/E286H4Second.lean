module
public import EG617.Core.E286H4First

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem e286_f10_11_extra_completer_minimum (a b : ℕ) (ha : 1 ≤ a) (hb : 1 ≤ b)
    (ha' : a ≤ 10) (hb' : b ≤ 11) :
    5 ≤ (9 - a - b) + a * (b - 2) + b * (a - 2) := by
  interval_cases a <;> interval_cases b <;> norm_num

/-- Adding the exterior completer to the forced neighbors recovers one unit
at each missing vertex of the ten-clique. -/
theorem e286_clique_charge_with_extra (G : SimpleGraph V) (K S : Finset V)
    (hK : G.IsClique (K : Set V)) (hd : Disjoint K S) (p x : V)
    (hpK : p ∉ K) (hpS : p ∉ S) (hx : x ∈ K) (hxp : G.Adj x p)
    (hxs : ∀ y ∈ S, G.Adj x y) :
    K.card + S.card + 1 ≤ 13 + degreeExcess12 G x := by
  classical
  have hd' : Disjoint K (insert p S) := by
    rw [Finset.disjoint_left]
    intro y hy hm
    rcases Finset.mem_insert.mp hm with rfl | h
    · exact hpK hy
    · exact Finset.disjoint_left.mp hd hy h
  have h := e286_clique_blocker_vertex_charge G K (insert p S) hK hd' x hx
    (fun y hy => (Finset.mem_insert.mp hy).elim (fun he => he ▸ hxp) (hxs y))
  rw [Finset.card_insert_of_notMem hpS] at h
  omega

/-- Split the scalar cost into the point, the first side's actual excess,
and a fixed charge per missing vertex on the leaf. -/
theorem e286_split_pair_charge (G : SimpleGraph V) (K L : Finset V) (z : V)
    (hd : Disjoint K L) (s t m : ℕ) (hk : K.card = s) (hl : L.card = t)
    (hscalar : m ≤ (s + t - 12 - (e286Missing G K z).card - (e286Missing G L z).card) +
      (e286Missing G K z).card * ((e286Missing G L z).card - 2) +
      (e286Missing G L z).card * ((e286Missing G K z).card - 2))
    (hfirst : ∀ x ∈ e286Missing G K z, (e286Missing G L z).card - 2 ≤ degreeExcess12 G x) :
    m ≤ degreeExcess12 G z + (∑ x ∈ e286Missing G K z, degreeExcess12 G x) +
      (e286Missing G L z).card * ((e286Missing G K z).card - 2) := by
  classical
  have hz := e286_pair_point_degree_charge G K L hd z
  change K.card + L.card ≤ 12 + degreeExcess12 G z + (e286Missing G K z).card +
    (e286Missing G L z).card at hz
  rw [hk, hl] at hz
  have hsum := Finset.sum_le_sum hfirst
  simp only [Finset.sum_const, smul_eq_mul] at hsum
  omega

theorem e286_extra_completer_split (G : SimpleGraph V) (K L : Finset V)
    (hk : K.card = 10) (hl : L.card = 11) (hK : G.IsClique (K : Set V))
    (hd : Disjoint K L) (z p : V) (hpK : p ∉ K) (hpL : p ∉ L)
    (hcomp : ∀ x ∈ K, G.Adj p x)
    (ha : (e286Missing G K z).Nonempty) (hb : (e286Missing G L z).Nonempty)
    (hedge : ∀ x ∈ e286Missing G K z, ∀ y ∈ e286Missing G L z, G.Adj x y) :
    5 ≤ degreeExcess12 G z + (∑ x ∈ e286Missing G K z, degreeExcess12 G x) +
      (e286Missing G L z).card * ((e286Missing G K z).card - 2) := by
  classical
  have hAK : e286Missing G K z ⊆ K := Finset.filter_subset _ _
  have hBL : e286Missing G L z ⊆ L := Finset.filter_subset _ _
  apply e286_split_pair_charge G K L z hd 10 11 5 hk hl
  · exact e286_f10_11_extra_completer_minimum _ _ (Finset.card_pos.mpr ha)
      (Finset.card_pos.mpr hb) (hk ▸ Finset.card_le_card hAK) (hl ▸ Finset.card_le_card hBL)
  · intro x hx
    have h := e286_clique_charge_with_extra G K _ hK (hd.mono_right hBL) p x hpK
      (fun hm => hpL (hBL hm)) (hAK hx) (hcomp x (hAK hx)).symm (hedge x hx)
    rw [hk] at h
    omega

theorem e286_k10_k11_extra_completer_charge (G : SimpleGraph V) (K L : Finset V)
    (hk : K.card = 10) (hl : L.card = 11) (hK : G.IsClique (K : Set V))
    (hL : G.IsClique (L : Set V)) (hd : Disjoint K L)
    (z p : V) (hzK : z ∉ K) (hzL : z ∉ L) (hpK : p ∉ K) (hpL : p ∉ L)
    (hcomp : ∀ x ∈ K, G.Adj p x)
    (ha : (e286Missing G K z).Nonempty) (hb : (e286Missing G L z).Nonempty)
    (hedge : ∀ x ∈ e286Missing G K z, ∀ y ∈ e286Missing G L z, G.Adj x y) :
    5 ≤ ∑ x ∈ insert z (e286Missing G K z ∪ e286Missing G L z), degreeExcess12 G x := by
  classical
  have hAK : e286Missing G K z ⊆ K := Finset.filter_subset _ _
  have hBL : e286Missing G L z ⊆ L := Finset.filter_subset _ _
  have hsplit := e286_extra_completer_split G K L hk hl hK hd z p hpK hpL hcomp ha hb hedge
  have hleaf (y : V) (hy : y ∈ e286Missing G L z) :
      (e286Missing G K z).card - 2 ≤ degreeExcess12 G y := by
    have h := e286_clique_blocker_vertex_charge G L _ hL (hd.symm.mono_right hAK) y
      (hBL hy) (fun x hx => (hedge x hx y hy).symm)
    rw [hl] at h
    omega
  have hs := Finset.sum_le_sum hleaf
  simp only [Finset.sum_const, smul_eq_mul] at hs
  have hout : z ∉ e286Missing G K z ∪ e286Missing G L z := by
    intro hm
    exact (Finset.mem_union.mp hm).elim (fun h => hzK (hAK h)) (fun h => hzL (hBL h))
  rw [Finset.sum_insert hout, Finset.sum_union (hd.mono hAK hBL)]
  omega

/-- The three estimates use the union of forced neighbor sets on a double
miss and the other exterior point on a single miss. -/
theorem e286_shared_leaf_pointwise (G : SimpleGraph V) (L A C : Finset V)
    (r q : V) (hl : L.card = 11) (hL : G.IsClique (L : Set V))
    (hLA : Disjoint L A) (hLC : Disjoint L C) (hAC : Disjoint A C)
    (hrL : r ∉ L) (hqL : q ∉ L) (hrC : r ∉ C) (hqA : q ∉ A)
    (hB : ∀ x ∈ e286Missing G L r, ∀ y ∈ A, G.Adj x y)
    (hD : ∀ x ∈ e286Missing G L q, ∀ y ∈ C, G.Adj x y) (x : V) :
    (x ∈ e286Missing G L r → x ∈ e286Missing G L q →
      A.card + C.card - 2 ≤ degreeExcess12 G x) ∧
    (x ∈ e286Missing G L r → x ∉ e286Missing G L q →
      A.card - 1 ≤ degreeExcess12 G x) ∧
    (x ∈ e286Missing G L q → x ∉ e286Missing G L r →
      C.card - 1 ≤ degreeExcess12 G x) := by
  classical
  have hsingle (v : V) (hx : x ∈ L) (hn : x ∉ e286Missing G L v) : G.Adj x v := by
    by_contra h
    exact hn (Finset.mem_filter.mpr ⟨hx, fun he => h he.symm⟩)
  refine ⟨?_, ?_, ?_⟩
  · intro hb hd
    have h := e286_clique_blocker_vertex_charge G L (A ∪ C) hL
      (Finset.disjoint_union_right.mpr ⟨hLA, hLC⟩) x (Finset.mem_filter.mp hb).1
      (fun y hy => (Finset.mem_union.mp hy).elim (hB x hb y) (hD x hd y))
    rw [hl, Finset.card_union_of_disjoint hAC] at h
    omega
  · intro hb hd
    have hx := (Finset.mem_filter.mp hb).1
    have h := e286_clique_charge_with_extra G L A hL hLA q x hqL hqA hx
      (hsingle q hx hd) (hB x hb)
    rw [hl] at h
    omega
  · intro hd hb
    have hx := (Finset.mem_filter.mp hd).1
    have h := e286_clique_charge_with_extra G L C hL hLC r x hrL hrC hx
      (hsingle r hx hb) (hD x hd)
    rw [hl] at h
    omega

theorem e286_shared_leaf_pair_charge (G : SimpleGraph V) (L A C : Finset V)
    (r q : V) (hl : L.card = 11) (hL : G.IsClique (L : Set V))
    (hLA : Disjoint L A) (hLC : Disjoint L C) (hAC : Disjoint A C)
    (hrL : r ∉ L) (hqL : q ∉ L) (hrC : r ∉ C) (hqA : q ∉ A)
    (hB : ∀ x ∈ e286Missing G L r, ∀ y ∈ A, G.Adj x y)
    (hD : ∀ x ∈ e286Missing G L q, ∀ y ∈ C, G.Adj x y) :
    (e286Missing G L r).card * (A.card - 2) + (e286Missing G L q).card * (C.card - 2) ≤
      ∑ x ∈ e286Missing G L r ∪ e286Missing G L q, degreeExcess12 G x := by
  classical
  let B := e286Missing G L r
  let D := e286Missing G L q
  let U := B ∪ D
  have hfilter (S : Finset V) (hs : S ⊆ U) : U.filter (fun x => x ∈ S) = S := by
    ext x
    simp only [Finset.mem_filter]
    exact ⟨And.right, fun hx => ⟨hs hx, hx⟩⟩
  have ledger (S : Finset V) (hs : S ⊆ U) (n : ℕ) :
      (∑ x ∈ U, if x ∈ S then n else 0) = S.card * n := by
    rw [← Finset.sum_filter, hfilter S hs]
    simp
  have hlocal (x : V) (hx : x ∈ U) :
      (if x ∈ B then A.card - 2 else 0) + (if x ∈ D then C.card - 2 else 0) ≤ degreeExcess12 G x := by
    obtain ⟨both, left, right⟩ := e286_shared_leaf_pointwise G L A C r q hl hL
      hLA hLC hAC hrL hqL hrC hqA hB hD x
    by_cases hb : x ∈ B <;> by_cases hd : x ∈ D
    · have h := both hb hd
      simp only [if_pos hb, if_pos hd]
      omega
    · have h := left hb hd
      simp only [if_pos hb, if_neg hd]
      omega
    · have h := right hd hb
      simp only [if_neg hb, if_pos hd]
      omega
    · simp [hb, hd]
  have h := Finset.sum_le_sum hlocal
  rw [Finset.sum_add_distrib, ledger B Finset.subset_union_left,
    ledger D Finset.subset_union_right] at h
  exact h

end EG617
