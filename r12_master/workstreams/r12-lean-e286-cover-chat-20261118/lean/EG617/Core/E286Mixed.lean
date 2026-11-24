module
public import EG617.Core.E286H3Remaining

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Frozen Section3: full finite domain follows from the actual clique cards. -/
theorem e286_f10_11_minimum (a b : ℕ) (ha : 1 ≤ a) (hb : 1 ≤ b)
    (ha' : a ≤ 10) (hb' : b ≤ 11) :
    4 ≤ (9 - a - b) + a * (b - 3) + b * (a - 2) := by
  interval_cases a <;> interval_cases b <;> norm_num

/-- Actual mixed blocker; positive missing sets and all forced edges are explicit. -/
theorem e286_k10_k11_pair_local_charge (G : SimpleGraph V) (K L : Finset V)
    (hK : G.IsClique (K : Set V)) (hL : G.IsClique (L : Set V))
    (hcK : K.card = 10) (hcL : L.card = 11) (hd : Disjoint K L)
    (z : V) (hzK : z ∉ K) (hzL : z ∉ L)
    (ha : (e286Missing G K z).Nonempty) (hb : (e286Missing G L z).Nonempty)
    (he : ∀ x ∈ K, ¬ G.Adj z x → ∀ y ∈ L, ¬ G.Adj z y → G.Adj x y) :
    4 ≤ ∑ v ∈ insert z (e286Missing G K z ∪ e286Missing G L z), degreeExcess12 G v := by
  classical
  let A := e286Missing G K z
  let B := e286Missing G L z
  have hAK : A ⊆ K := Finset.filter_subset _ _
  have hBL : B ⊆ L := Finset.filter_subset _ _
  have hAB : Disjoint A B := hd.mono hAK hBL
  have hax (x : V) (hx : x ∈ A) : B.card - 3 ≤ degreeExcess12 G x := by
    have h := e286_clique_blocker_vertex_charge G K B hK (hd.mono_right hBL) x (hAK hx)
      (fun y hy => he x (hAK hx) (Finset.mem_filter.mp hx).2 y (hBL hy) (Finset.mem_filter.mp hy).2)
    rw [hcK] at h
    omega
  have hby (y : V) (hy : y ∈ B) : A.card - 2 ≤ degreeExcess12 G y := by
    have h := e286_clique_blocker_vertex_charge G L A hL (hd.symm.mono_right hAK) y (hBL hy)
      (fun x hx => (he x (hAK hx) (Finset.mem_filter.mp hx).2 y (hBL hy) (Finset.mem_filter.mp hy).2).symm)
    rw [hcL] at h
    omega
  have hsa : A.card * (B.card - 3) ≤ ∑ v ∈ A, degreeExcess12 G v := by
    simpa only [Finset.sum_const, smul_eq_mul] using Finset.sum_le_sum hax
  have hsb : B.card * (A.card - 2) ≤ ∑ v ∈ B, degreeExcess12 G v := by
    simpa only [Finset.sum_const, smul_eq_mul] using Finset.sum_le_sum hby
  have hz := e286_pair_point_degree_charge G K L hd z
  rw [hcK, hcL] at hz
  change 10 + 11 ≤ 12 + degreeExcess12 G z + A.card + B.card at hz
  have hzlow : 9 - A.card - B.card ≤ degreeExcess12 G z := by omega
  have ha10 : A.card ≤ 10 := hcK ▸ Finset.card_le_card hAK
  have hb11 : B.card ≤ 11 := hcL ▸ Finset.card_le_card hBL
  have hmin := e286_f10_11_minimum A.card B.card
    (Finset.card_pos.mpr ha) (Finset.card_pos.mpr hb) ha10 hb11
  have hzout : z ∉ A ∪ B := by
    intro hm
    exact (Finset.mem_union.mp hm).elim (fun h => hzK (hAK h)) (fun h => hzL (hBL h))
  change 4 ≤ ∑ v ∈ insert z (A ∪ B), degreeExcess12 G v
  rw [Finset.sum_insert hzout, Finset.sum_union hAB]
  omega

/-- Frozen Section6's mixed-pair dichotomy. The K11 missing set and blocker
edges follow from the original E286 hypotheses, not additional assumptions. -/
theorem e286_private_mixed_pair_dichotomy (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (i j z : V) (hi : i ∈ I) (hj : j ∈ I) (hij : i ≠ j)
    (hz : seedNeighbors G I z = {i, j})
    (hci : (seedPrivateClique G I i).card = 10)
    (hcj : (seedPrivateClique G I j).card = 11) :
    (∀ x ∈ seedPrivateClique G I i, G.Adj z x) ∨
      4 ≤ ∑ v ∈ insert z (seedPrivateClique G I i ∪ seedPrivateClique G I j),
        degreeExcess12 G v := by
  classical
  by_cases ha : (e286Missing G (seedPrivateClique G I i) z).Nonempty
  · right
    have hzZ := e286_pair_support_mem_multiple G I i j z hij hz
    have hzout (s : V) (hs : s ∈ I) : z ∉ seedPrivateClique G I s := by
      intro hm
      exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hI s hs) hm hzZ
    have hKi := e286_private_class_isClique G hG I hc hI i hi
    have hKj := e286_private_class_isClique G hG I hc hI j hj
    have hb := e286_k10_k11_pair_local_charge G _ _ hKi hKj hci hcj
      (seed_private_classes_disjoint G I hI i j hi hj hij) z (hzout i hi) (hzout j hj) ha
      (e286_eleven_clique_missing_nonempty G hG _ hcj hKj z (hzout j hj))
      (fun x hx hzx y hy hzy =>
        e286_pair_blocker_complete G hG I hc hI i j z hi hj hij hz x y hx hy hzx hzy)
    apply hb.trans
    apply Finset.sum_le_sum_of_subset
    apply Finset.insert_subset_insert
    exact Finset.union_subset_union (Finset.filter_subset _ _) (Finset.filter_subset _ _)
  · left
    intro x hx
    by_contra hn
    exact ha ⟨x, Finset.mem_filter.mpr ⟨hx, hn⟩⟩

end EG617
