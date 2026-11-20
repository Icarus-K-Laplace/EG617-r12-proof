module
public import EG617.Core.E286TriplePrivate

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

noncomputable def e286Missing (G : SimpleGraph V) (K : Finset V) (z : V) : Finset V :=
  K.filter (fun v => ¬ G.Adj z v)

def e286K11Cost (a b : ℕ) : ℕ := (10 - a - b) + a * (b - 2) + b * (a - 2)

theorem e286_k11_pair_scalar_charge (G : SimpleGraph V) (K L : Finset V)
    (hK : G.IsClique (K : Set V)) (hL : G.IsClique (L : Set V))
    (hcK : K.card = 11) (hcL : L.card = 11) (hd : Disjoint K L)
    (z : V) (hzK : z ∉ K) (hzL : z ∉ L)
    (he : ∀ x ∈ K, ¬ G.Adj z x → ∀ y ∈ L, ¬ G.Adj z y → G.Adj x y) :
    e286K11Cost (e286Missing G K z).card (e286Missing G L z).card ≤
      ∑ v ∈ insert z (e286Missing G K z ∪ e286Missing G L z), degreeExcess12 G v := by
  classical
  let A := e286Missing G K z
  let B := e286Missing G L z
  have hAK : A ⊆ K := Finset.filter_subset _ _
  have hBL : B ⊆ L := Finset.filter_subset _ _
  have hAB : Disjoint A B := hd.mono hAK hBL
  have hax (x : V) (hx : x ∈ A) : B.card - 2 ≤ degreeExcess12 G x := by
    have h := e286_clique_blocker_vertex_charge G K B hK (hd.mono_right hBL) x (hAK hx)
      (fun y hy => he x (hAK hx) (Finset.mem_filter.mp hx).2 y (hBL hy) (Finset.mem_filter.mp hy).2)
    rw [hcK] at h
    omega
  have hby (y : V) (hy : y ∈ B) : A.card - 2 ≤ degreeExcess12 G y := by
    have h := e286_clique_blocker_vertex_charge G L A hL (hd.symm.mono_right hAK) y (hBL hy)
      (fun x hx => (he x (hAK hx) (Finset.mem_filter.mp hx).2 y (hBL hy) (Finset.mem_filter.mp hy).2).symm)
    rw [hcL] at h
    omega
  have hsa : A.card * (B.card - 2) ≤ ∑ v ∈ A, degreeExcess12 G v := by
    simpa only [Finset.sum_const, smul_eq_mul] using Finset.sum_le_sum hax
  have hsb : B.card * (A.card - 2) ≤ ∑ v ∈ B, degreeExcess12 G v := by
    simpa only [Finset.sum_const, smul_eq_mul] using Finset.sum_le_sum hby
  have hz := e286_pair_point_degree_charge G K L hd z
  rw [hcK, hcL] at hz
  change 11 + 11 ≤ 12 + degreeExcess12 G z + A.card + B.card at hz
  have hzlow : 10 - A.card - B.card ≤ degreeExcess12 G z := by omega
  have hzout : z ∉ A ∪ B := by
    intro hm
    exact (Finset.mem_union.mp hm).elim (fun h => hzK (hAK h)) (fun h => hzL (hBL h))
  change e286K11Cost A.card B.card ≤ ∑ v ∈ insert z (A ∪ B), degreeExcess12 G v
  rw [Finset.sum_insert hzout, Finset.sum_union hAB]
  unfold e286K11Cost
  omega

/-- Frozen equation2, with its small-side orientation and budget conditions. -/
theorem e286_f11_concentrated_minimum (a b : ℕ) (ha : 1 ≤ a) (hb : 1 ≤ b)
    (ha' : a ≤ 11) (hb' : b ≤ 11) (hab : a ≤ b) (hcost : e286K11Cost a b ≤ 8) :
    6 ≤ (10 - a - b) + a * (b - 2) := by
  unfold e286K11Cost at hcost
  interval_cases a <;> interval_cases b <;> norm_num at *

/-- The actual pair point plus the clique with the smaller missing set already
costs6. The scalar budget is derived from global excess8, not assumed. -/
theorem e286_private_pair_concentrated_charge (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (i j z : V) (hi : i ∈ I) (hj : j ∈ I) (hij : i ≠ j)
    (hz : seedNeighbors G I z = {i, j})
    (hci : (seedPrivateClique G I i).card = 11)
    (hcj : (seedPrivateClique G I j).card = 11)
    (hsmall : (e286Missing G (seedPrivateClique G I i) z).card ≤
      (e286Missing G (seedPrivateClique G I j) z).card) :
    6 ≤ ∑ v ∈ insert z (seedPrivateClique G I i), degreeExcess12 G v := by
  classical
  let K := seedPrivateClique G I i
  let L := seedPrivateClique G I j
  let A := e286Missing G K z
  let B := e286Missing G L z
  have hAK : A ⊆ K := Finset.filter_subset _ _
  have hBL : B ⊆ L := Finset.filter_subset _ _
  have hzZ := e286_pair_support_mem_multiple G I i j z hij hz
  have hzout (s : V) (hs : s ∈ I) : z ∉ seedPrivateClique G I s := by
    intro hm
    exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hI s hs) hm hzZ
  have hKi := e286_private_class_isClique G hG I hc hI i hi
  have hKj := e286_private_class_isClique G hG I hc hI j hj
  have hd := seed_private_classes_disjoint G I hI i j hi hj hij
  have hedge := e286_pair_blocker_complete G hG I hc hI i j z hi hj hij hz
  have hsc := e286_k11_pair_scalar_charge G K L hKi hKj hci hcj hd z (hzout i hi) (hzout j hj)
    (fun x hx hzx y hy hzy => hedge x y hx hy hzx hzy)
  have hbgt := e286_subset_excess_budget G hG (insert z (A ∪ B))
  have hcost : e286K11Cost A.card B.card ≤ 8 := hsc.trans hbgt
  have hap := e286_eleven_clique_missing_nonempty G hG K hci hKi z (hzout i hi)
  have hbp := e286_eleven_clique_missing_nonempty G hG L hcj hKj z (hzout j hj)
  have ha11 : A.card ≤ 11 := hci ▸ Finset.card_le_card hAK
  have hb11 : B.card ≤ 11 := hcj ▸ Finset.card_le_card hBL
  have h6 := e286_f11_concentrated_minimum A.card B.card
    (Finset.card_pos.mpr hap) (Finset.card_pos.mpr hbp) ha11 hb11 hsmall hcost
  have hax (x : V) (hx : x ∈ A) : B.card - 2 ≤ degreeExcess12 G x := by
    have h := e286_clique_blocker_vertex_charge G K B hKi (hd.mono_right hBL) x (hAK hx)
      (fun y hy => hedge x y (hAK hx) (hBL hy) (Finset.mem_filter.mp hx).2 (Finset.mem_filter.mp hy).2)
    rw [hci] at h
    omega
  have hsa : A.card * (B.card - 2) ≤ ∑ v ∈ A, degreeExcess12 G v := by
    simpa only [Finset.sum_const, smul_eq_mul] using Finset.sum_le_sum hax
  have hsub : (∑ v ∈ A, degreeExcess12 G v) ≤ ∑ v ∈ K, degreeExcess12 G v :=
    Finset.sum_le_sum_of_subset hAK
  have hzdeg := e286_pair_point_degree_charge G K L hd z
  rw [hci, hcj] at hzdeg
  change 11 + 11 ≤ 12 + degreeExcess12 G z + A.card + B.card at hzdeg
  have hzlow : 10 - A.card - B.card ≤ degreeExcess12 G z := by omega
  change 6 ≤ ∑ v ∈ insert z K, degreeExcess12 G v
  rw [Finset.sum_insert (hzout i hi)]
  omega

end EG617
