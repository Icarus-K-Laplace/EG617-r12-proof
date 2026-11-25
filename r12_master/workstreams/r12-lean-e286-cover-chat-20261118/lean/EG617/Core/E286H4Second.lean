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

/-- Frozen Section 6, second h4 orbit. Each incidence and each support point
is obtained from the specified count vector on the actual graph. -/
theorem e286_h4_second_orbit_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V))
    (hcounts : e286GraphSupportCounts G I e = [1,0,1,0,0,1,1,0,0,0,0]) : False := by
  classical
  let K := fun i : Fin 4 => seedPrivateClique G I (e i)
  have row (s : Fin 4) : e286CountIncidence (e286GraphSupportCounts G I e) s =
      if s = 0 then 3 else 2 := by
    rw [hcounts]
    fin_cases s <;> norm_num [e286CountIncidence, Fin.sum_univ_succ, e286SupportType]
  have card0 : (K 0).card = 10 := by
    have h := e286_private_multiple_card G I hI _ (e 0).property (hd _ (e 0).property)
    have hr := row 0
    rw [e286_graph_support_incidence] at hr
    norm_num at hr
    dsimp only [K]
    omega
  have card11 (s : Fin 4) (hs : s ≠ 0) : (K s).card = 11 := by
    have h := e286_private_multiple_card G I hI _ (e s).property (hd _ (e s).property)
    have hr := row s
    rw [e286_graph_support_incidence, if_neg hs] at hr
    dsimp only [K]
    omega
  have cl (i : Fin 4) : G.IsClique ((K i : Finset V) : Set V) :=
    e286_private_class_isClique G hG I hc hI _ (e i).property
  obtain ⟨p, hp'⟩ := e286_positive_count_actual_witness G I e 0 (by rw [hcounts]; norm_num)
  obtain ⟨r, hr'⟩ := e286_positive_count_actual_witness G I e 2 (by rw [hcounts]; norm_num)
  obtain ⟨q, hq'⟩ := e286_positive_count_actual_witness G I e 5 (by rw [hcounts]; norm_num)
  have hp : seedNeighbors G I p = {(e 0 : V), (e 1 : V)} := by simpa [e286SupportType] using hp'
  have hr : seedNeighbors G I r = {(e 0 : V), (e 3 : V)} := by simpa [e286SupportType] using hr'
  have hq : seedNeighbors G I q = {(e 2 : V), (e 3 : V)} := by simpa [e286SupportType] using hq'
  have hne (a b : Fin 4) (h : a ≠ b) : (e a : V) ≠ e b :=
    fun he => h (e.injective (Subtype.ext he))
  have sep (a b : Fin 4) (h : a ≠ b) : Disjoint (K a) (K b) :=
    seed_private_classes_disjoint G I hI _ _ (e a).property (e b).property (hne a b h)
  have outside (v : V) (hv : v ∈ seedMultipleSet G I) (s : Fin 4) : v ∉ K s := by
    intro hm
    exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hI _ (e s).property) hm hv
  have outP := outside p (e286_pair_support_mem_multiple G I _ _ p (hne 0 1 (by decide)) hp)
  have outR := outside r (e286_pair_support_mem_multiple G I _ _ r (hne 0 3 (by decide)) hr)
  have outQ := outside q (e286_pair_support_mem_multiple G I _ _ q (hne 2 3 (by decide)) hq)
  have pr : p ≠ r := by
    intro he
    have hm : (e 1 : V) ∈ seedNeighbors G I p := by rw [hp]; simp
    rw [he, hr] at hm
    simpa [hne 1 0 (by decide), hne 1 3 (by decide)] using hm
  have pq : p ≠ q := by
    intro he
    have hm : (e 0 : V) ∈ seedNeighbors G I p := by rw [hp]; simp
    rw [he, hq] at hm
    simpa [hne 0 2 (by decide), hne 0 3 (by decide)] using hm
  have rq : r ≠ q := by
    intro he
    have hm : (e 0 : V) ∈ seedNeighbors G I r := by rw [hr]; simp
    rw [he, hq] at hm
    simpa [hne 0 2 (by decide), hne 0 3 (by decide)] using hm
  let Q := insert q (K 2 ∪ K 3)
  have q6 : 6 ≤ ∑ v ∈ Q, degreeExcess12 G v :=
    e286_private_k11_pair_charge G hG I hc hI _ _ q (e 2).property (e 3).property
      (hne 2 3 (by decide)) hq (card11 2 (by decide)) (card11 3 (by decide))
  have pOutQ : p ∉ Q := by simp [Q, pq, outP]
  have rOutQ : r ∉ Q := by simp [Q, rq, outR]
  have small (S : Finset V) (hs : Disjoint S Q) : (∑ x ∈ S, degreeExcess12 G x) ≤ 2 := by
    have h := e286_subset_excess_budget G hG (S ∪ Q)
    rw [Finset.sum_union hs] at h
    omega
  have pComplete : ∀ x ∈ K 0, G.Adj p x := by
    rcases e286_private_mixed_pair_dichotomy G hG I hc hI _ _ p (e 0).property (e 1).property
      (hne 0 1 (by decide)) hp card0 (card11 1 (by decide)) with h | h
    · exact h
    · have pairs : Disjoint (K 0 ∪ K 1) (K 2 ∪ K 3) := by
        rw [Finset.disjoint_union_left, Finset.disjoint_union_right, Finset.disjoint_union_right]
        exact ⟨⟨sep 0 2 (by decide), sep 0 3 (by decide)⟩,
          ⟨sep 1 2 (by decide), sep 1 3 (by decide)⟩⟩
      have hs := small (insert p (K 0 ∪ K 1)) (Finset.disjoint_insert_left.mpr
        ⟨pOutQ, Finset.disjoint_insert_right.mpr ⟨by simp [outQ], pairs⟩⟩)
      change 4 ≤ ∑ x ∈ insert p (K 0 ∪ K 1), degreeExcess12 G x at h
      omega
  let A := e286Missing G (K 0) r
  let B := e286Missing G (K 3) r
  let C := e286Missing G (K 2) q
  let D := e286Missing G (K 3) q
  by_cases ha : A.Nonempty
  · have sa : A ⊆ K 0 := Finset.filter_subset _ _
    have sb : B ⊆ K 3 := Finset.filter_subset _ _
    have sc : C ⊆ K 2 := Finset.filter_subset _ _
    have sd : D ⊆ K 3 := Finset.filter_subset _ _
    have hb : B.Nonempty := e286_eleven_clique_missing_nonempty G hG _ (card11 3 (by decide)) (cl 3) r (outR 3)
    have hc' : C.Nonempty := e286_eleven_clique_missing_nonempty G hG _ (card11 2 (by decide)) (cl 2) q (outQ 2)
    have hd' : D.Nonempty := e286_eleven_clique_missing_nonempty G hG _ (card11 3 (by decide)) (cl 3) q (outQ 3)
    have edgeAB (x : V) (hx : x ∈ A) (y : V) (hy : y ∈ B) : G.Adj x y :=
      e286_pair_blocker_complete G hG I hc hI _ _ r (e 0).property (e 3).property
        (hne 0 3 (by decide)) hr x y (sa hx) (sb hy)
        (Finset.mem_filter.mp hx).2 (Finset.mem_filter.mp hy).2
    have edgeCD (x : V) (hx : x ∈ C) (y : V) (hy : y ∈ D) : G.Adj x y :=
      e286_pair_blocker_complete G hG I hc hI _ _ q (e 2).property (e 3).property
        (hne 2 3 (by decide)) hq x y (sc hx) (sd hy)
        (Finset.mem_filter.mp hx).2 (Finset.mem_filter.mp hy).2
    have five : 5 ≤ degreeExcess12 G r + (∑ x ∈ A, degreeExcess12 G x) + B.card * (A.card - 2) :=
      e286_extra_completer_split G _ _ card0 (card11 3 (by decide)) (cl 0) (sep 0 3 (by decide))
        r p (outP 0) (outP 3) pComplete ha hb edgeAB
    have six : 6 ≤ degreeExcess12 G q + (∑ x ∈ C, degreeExcess12 G x) + D.card * (C.card - 2) := by
      apply e286_split_pair_charge G (K 2) (K 3) q (sep 2 3 (by decide)) 11 11 6
        (card11 2 (by decide)) (card11 3 (by decide))
      · exact e286_f11_minimum C.card D.card (Finset.card_pos.mpr hc') (Finset.card_pos.mpr hd')
          (le_trans (Finset.card_le_card sc) (card11 2 (by decide)).le)
          (le_trans (Finset.card_le_card sd) (card11 3 (by decide)).le)
      · intro x hx
        have h := e286_clique_blocker_vertex_charge G (K 2) D (cl 2)
          ((sep 2 3 (by decide)).mono_right sd) x (sc hx) (edgeCD x hx)
        rw [card11 2 (by decide)] at h
        change D.card - 2 ≤ degreeExcess12 G x
        omega
    have leaf : B.card * (A.card - 2) + D.card * (C.card - 2) ≤
        ∑ x ∈ B ∪ D, degreeExcess12 G x :=
      e286_shared_leaf_pair_charge G (K 3) A C r q (card11 3 (by decide)) (cl 3)
        ((sep 3 0 (by decide)).mono_right sa) ((sep 3 2 (by decide)).mono_right sc)
        ((sep 0 2 (by decide)).mono sa sc) (outR 3) (outQ 3)
        (fun hm => outR 2 (sc hm)) (fun hm => outQ 0 (sa hm))
        (fun y hy x hx => (edgeAB x hx y hy).symm) (fun y hy x hx => (edgeCD x hx y hy).symm)
    have su : B ∪ D ⊆ K 3 := Finset.union_subset sb sd
    have haC := (sep 0 2 (by decide)).mono sa sc
    have dis : Disjoint (A ∪ C) (B ∪ D) := Finset.disjoint_union_left.mpr
      ⟨(sep 0 3 (by decide)).mono sa su, (sep 2 3 (by decide)).mono sc su⟩
    have extOut (v : V) (hv : ∀ i : Fin 4, v ∉ K i) : v ∉ (A ∪ C) ∪ (B ∪ D) := by
      intro hm
      rcases Finset.mem_union.mp hm with h | h
      · exact (Finset.mem_union.mp h).elim (fun h => hv 0 (sa h)) (fun h => hv 2 (sc h))
      · exact hv 3 (su h)
    have qOut := extOut q outQ
    have rOut : r ∉ insert q ((A ∪ C) ∪ (B ∪ D)) := by
      intro hm
      exact (Finset.mem_insert.mp hm).elim rq (extOut r outR)
    have budget := e286_subset_excess_budget G hG (insert r (insert q ((A ∪ C) ∪ (B ∪ D))))
    rw [Finset.sum_insert rOut, Finset.sum_insert qOut, Finset.sum_union dis, Finset.sum_union haC] at budget
    omega
  · have rComplete (x : V) (hx : x ∈ K 0) : G.Adj r x := by
      by_contra hn
      exact ha ⟨x, Finset.mem_filter.mpr ⟨hx, hn⟩⟩
    have seven := (e286_ten_clique_completers_excess G hG (K 0) card0 (cl 0) p r pr
      (outP 0) (outR 0) (fun x hx => ⟨pComplete x hx, rComplete x hx⟩)).2
    have hs := small ({p,r} : Finset V) (Finset.disjoint_insert_left.mpr
      ⟨pOutQ, Finset.disjoint_singleton_left.mpr rOutQ⟩)
    rw [Finset.sum_pair pr] at hs
    omega

theorem e286_actual_support_six_remaining (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives.tail.tail.tail.tail := by
  obtain ⟨I, hc, hi, hd, e, he⟩ := e286_actual_support_seven_remaining G hG
  refine ⟨I, hc, hi, hd, e, ?_⟩
  rcases List.mem_cons.mp he with horbit | htail
  · exact (e286_h4_second_orbit_impossible G hG I hc hi hd e horbit).elim
  · exact htail

end EG617
