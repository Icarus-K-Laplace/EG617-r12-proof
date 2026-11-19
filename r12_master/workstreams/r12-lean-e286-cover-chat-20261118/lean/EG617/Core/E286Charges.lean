module
public import EG617.Core.E286Blocker

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem e286_two_disjoint_neighbor_sets (G : SimpleGraph V) (v : V) (A B : Finset V)
    (hd : Disjoint A B) (ha : ∀ x ∈ A, G.Adj v x) (hb : ∀ x ∈ B, G.Adj v x) :
    A.card + B.card ≤ G.degree v := by
  classical
  have hs : A ∪ B ⊆ G.neighborFinset v := by
    intro x hx
    exact (SimpleGraph.mem_neighborFinset G v x).mpr
      ((Finset.mem_union.mp hx).elim (ha x) (hb x))
  have h := Finset.card_le_card hs
  rw [Finset.card_union_of_disjoint hd, SimpleGraph.card_neighborFinset_eq_degree] at h
  exact h

/-- Internal clique neighbors and a disjoint forced blocker give a pointwise
charge; all underlying graph sets are explicit. -/
theorem e286_clique_blocker_vertex_charge (G : SimpleGraph V)
    (K B : Finset V) (hK : G.IsClique (K : Set V)) (hd : Disjoint K B)
    (x : V) (hx : x ∈ K) (hB : ∀ y ∈ B, G.Adj x y) :
    K.card + B.card ≤ 13 + degreeExcess12 G x := by
  classical
  have hd' : Disjoint (K.erase x) B := hd.mono_left (Finset.erase_subset x K)
  have h := e286_two_disjoint_neighbor_sets G x (K.erase x) B hd'
    (fun y hy => hK hx (Finset.mem_erase.mp hy).2 (Finset.mem_erase.mp hy).1.symm) hB
  rw [Finset.card_erase_of_mem hx] at h
  have hp := Finset.card_pos.mpr ⟨x, hx⟩
  simp only [degreeExcess12, ← SimpleGraph.ncard_neighborSet] at h ⊢
  omega

theorem e286_pair_point_degree_charge (G : SimpleGraph V) (K L : Finset V)
    (hd : Disjoint K L) (z : V) :
    K.card + L.card ≤ 12 + degreeExcess12 G z +
      (K.filter (fun v => ¬ G.Adj z v)).card +
      (L.filter (fun v => ¬ G.Adj z v)).card := by
  classical
  have hd' : Disjoint (K.filter (G.Adj z)) (L.filter (G.Adj z)) :=
    hd.mono (Finset.filter_subset _ _) (Finset.filter_subset _ _)
  have h := e286_two_disjoint_neighbor_sets G z _ _ hd'
    (fun _ h => (Finset.mem_filter.mp h).2) (fun _ h => (Finset.mem_filter.mp h).2)
  have hk := Finset.card_filter_add_card_filter_not (s := K) (G.Adj z)
  have hl := Finset.card_filter_add_card_filter_not (s := L) (G.Adj z)
  simp only [degreeExcess12, ← SimpleGraph.ncard_neighborSet] at h ⊢
  omega

/-- Scalar part of frozen Section3 on the complete domain containing every
missing subset of a clique of size11. This is reduced by the Lean kernel. -/
theorem e286_f11_minimum (a b : ℕ) (ha : 1 ≤ a) (hb : 1 ≤ b)
    (ha' : a ≤ 11) (hb' : b ≤ 11) :
    6 ≤ (10 - a - b) + a * (b - 2) + b * (a - 2) := by
  interval_cases a <;> interval_cases b <;> norm_num

/-- The actual three disjoint charged sets in a K11/K11 blocker cost at least6.
The forced edges will be supplied by e286_pair_blocker_complete. -/
theorem e286_k11_pair_local_charge (G : SimpleGraph V) (K L : Finset V)
    (hK : G.IsClique (K : Set V)) (hL : G.IsClique (L : Set V))
    (hcK : K.card = 11) (hcL : L.card = 11) (hd : Disjoint K L)
    (z : V) (hzK : z ∉ K) (hzL : z ∉ L)
    (ha : (K.filter (fun v => ¬ G.Adj z v)).Nonempty)
    (hb : (L.filter (fun v => ¬ G.Adj z v)).Nonempty)
    (he : ∀ x ∈ K, ¬ G.Adj z x → ∀ y ∈ L, ¬ G.Adj z y → G.Adj x y) :
    6 ≤ ∑ v ∈ insert z ((K.filter (fun v => ¬ G.Adj z v)) ∪
      (L.filter (fun v => ¬ G.Adj z v))), degreeExcess12 G v := by
  classical
  let A := K.filter (fun v => ¬ G.Adj z v)
  let B := L.filter (fun v => ¬ G.Adj z v)
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
  have ha' : A.card ≤ 11 := hcK ▸ Finset.card_le_card hAK
  have hb' : B.card ≤ 11 := hcL ▸ Finset.card_le_card hBL
  have hmin := e286_f11_minimum A.card B.card (Finset.card_pos.mpr ha) (Finset.card_pos.mpr hb) ha' hb'
  have hzout : z ∉ A ∪ B := by
    intro hm
    exact (Finset.mem_union.mp hm).elim (fun h => hzK (hAK h)) (fun h => hzL (hBL h))
  change 6 ≤ ∑ v ∈ insert z (A ∪ B), degreeExcess12 G v
  rw [Finset.sum_insert hzout, Finset.sum_union hAB]
  omega

end EG617
