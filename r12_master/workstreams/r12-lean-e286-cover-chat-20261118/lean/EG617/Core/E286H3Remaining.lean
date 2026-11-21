module
public import EG617.Core.E286Concentrated
public import EG617.Core.E286OrbitRealization

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem e286_pair_triple_small_side_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (e : Fin 4 ≃ (I : Set V)) (hK : ∀ i : Fin 4, (seedPrivateClique G I (e i)).card = 11)
    (p t : V) (hp : seedNeighbors G I p = {(e 0 : V), (e 1 : V)})
    (ht : seedNeighbors G I t = {(e 1 : V), (e 2 : V), (e 3 : V)})
    (hsmall : (e286Missing G (seedPrivateClique G I (e 0)) p).card ≤
      (e286Missing G (seedPrivateClique G I (e 1)) p).card) : False := by
  classical
  let K := fun i : Fin 4 => seedPrivateClique G I (e i)
  have heinj : Function.Injective (fun i : Fin 4 => (e i : V)) := by
    intro a b hab
    exact e.injective (Subtype.ext hab)
  have hne (a b : Fin 4) (hab : a ≠ b) : (e a : V) ≠ e b := fun h => hab (heinj h)
  have hpZ := e286_pair_support_mem_multiple G I _ _ p (hne 0 1 (by decide)) hp
  have htZ : t ∈ seedMultipleSet G I := by
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_univ _, ?_⟩
    rw [ht, Finset.card_insert_of_notMem (show (e 1 : V) ∉ ({(e 2 : V), (e 3 : V)} : Finset V) by
      simp [hne 1 2 (by decide), hne 1 3 (by decide)]), Finset.card_pair (hne 2 3 (by decide))]
    omega
  have hpt : p ≠ t := by
    intro he
    have hm : (e 3 : V) ∈ seedNeighbors G I t := by rw [ht]; simp
    rw [← he, hp] at hm
    simp only [Finset.mem_insert, Finset.mem_singleton] at hm
    exact hm.elim (hne 3 0 (by decide)) (hne 3 1 (by decide))
  have hp6 := e286_private_pair_concentrated_charge G hG I hc hI _ _ p
    (e 0).property (e 1).property (hne 0 1 (by decide)) hp (hK 0) (hK 1) hsmall
  let e' : Fin 4 ≃ (I : Set V) := (Equiv.swap (0 : Fin 4) 3).trans e
  have ht' : seedNeighbors G I t = {(e' 0 : V), (e' 1 : V), (e' 2 : V)} := by
    rw [ht]
    ext v
    simp [e', Equiv.swap_apply_def, or_comm, or_left_comm, or_assoc]
  have hK' (i : Fin 4) (_hi : i ≠ 3) : (seedPrivateClique G I (e' i)).card = 11 :=
    hK ((Equiv.swap (0 : Fin 4) 3) i)
  have ht3 := e286_private_triple_k11_charge G hG I hc hI e' t ht' hK'
  have ht3' : 3 ≤ ∑ v ∈ insert t (K 1 ∪ K 2 ∪ K 3), degreeExcess12 G v := by
    simpa [e', K, Equiv.swap_apply_def, Finset.union_assoc, Finset.union_comm,
      Finset.union_left_comm] using ht3
  have hdis (a b : Fin 4) (hab : a ≠ b) : Disjoint (K a) (K b) :=
    seed_private_classes_disjoint G I hI _ _ (e a).property (e b).property (hne a b hab)
  have hKB : Disjoint (K 0) (K 1 ∪ K 2 ∪ K 3) := by
    simp only [Finset.disjoint_union_right]
    exact ⟨⟨hdis 0 1 (by decide), hdis 0 2 (by decide)⟩, hdis 0 3 (by decide)⟩
  have hout (v : V) (hv : v ∈ seedMultipleSet G I) (i : Fin 4) : v ∉ K i := by
    intro hm
    exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hI _ (e i).property) hm hv
  have hpB : p ∉ K 1 ∪ K 2 ∪ K 3 := by
    intro hm
    rcases Finset.mem_union.mp hm with hm | hm
    · exact (Finset.mem_union.mp hm).elim (hout p hpZ 1) (hout p hpZ 2)
    · exact hout p hpZ 3 hm
  have hsets : Disjoint (insert p (K 0)) (insert t (K 1 ∪ K 2 ∪ K 3)) := by
    rw [Finset.disjoint_left]
    intro v hvP hvT
    rcases Finset.mem_insert.mp hvP with he | hvP
    · subst v
      exact (Finset.mem_insert.mp hvT).elim hpt hpB
    · rcases Finset.mem_insert.mp hvT with he | hvT
      · subst v
        exact hout t htZ 0 hvP
      · exact Finset.disjoint_left.mp hKB hvP hvT
  have h8 := e286_subset_excess_budget G hG
    (insert p (K 0) ∪ insert t (K 1 ∪ K 2 ∪ K 3))
  rw [Finset.sum_union hsets] at h8
  change 6 ≤ ∑ v ∈ insert p (K 0), degreeExcess12 G v at hp6
  omega

/-- Frozen Section5's second h3 configuration, with both possible small-side
orientations covered by an actual seed permutation. -/
theorem e286_second_support_configuration_impossible (G : SimpleGraph V)
    (hG : E286Hypotheses G) (I : Finset V) (hc : I.card = 4)
    (hI : G.IsIndepSet (I : Set V)) (e : Fin 4 ≃ (I : Set V))
    (hK : ∀ i : Fin 4, (seedPrivateClique G I (e i)).card = 11)
    (p q r : V) (hp : seedNeighbors G I p = {(e 0 : V), (e 1 : V)})
    (hq : seedNeighbors G I q = {(e 0 : V), (e 2 : V), (e 3 : V)})
    (hr : seedNeighbors G I r = {(e 1 : V), (e 2 : V), (e 3 : V)}) : False := by
  classical
  by_cases hsmall : (e286Missing G (seedPrivateClique G I (e 0)) p).card ≤
      (e286Missing G (seedPrivateClique G I (e 1)) p).card
  · exact e286_pair_triple_small_side_impossible G hG I hc hI e hK p r hp hr hsmall
  · let e' : Fin 4 ≃ (I : Set V) := (Equiv.swap (0 : Fin 4) 1).trans e
    have hK' (i : Fin 4) : (seedPrivateClique G I (e' i)).card = 11 :=
      hK ((Equiv.swap (0 : Fin 4) 1) i)
    have hp' : seedNeighbors G I p = {(e' 0 : V), (e' 1 : V)} := by
      simpa [e', Equiv.swap_apply_def, Finset.pair_comm] using hp
    have hq' : seedNeighbors G I q = {(e' 1 : V), (e' 2 : V), (e' 3 : V)} := by
      simpa [e', Equiv.swap_apply_def] using hq
    have hsmall' : (e286Missing G (seedPrivateClique G I (e' 0)) p).card ≤
        (e286Missing G (seedPrivateClique G I (e' 1)) p).card := by
      simp only [e', Equiv.trans_apply, Equiv.swap_apply_left, Equiv.swap_apply_right]
      omega
    exact e286_pair_triple_small_side_impossible G hG I hc hI e' hK' p q hp' hq' hsmall'

theorem e286_positive_count_actual_witness (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (i : Fin 11)
    (hpos : 0 < (e286GraphSupportCounts G I e)[i.val]!) :
    ∃ v : V, seedNeighbors G I v = (e286SupportType i).image (fun j => (e j : V)) := by
  classical
  simp only [e286GraphSupportCounts, e286_ofFn_get] at hpos
  obtain ⟨v, hv⟩ := Finset.card_pos.mp hpos
  have hcode := (Finset.mem_filter.mp hv).2
  have he := seedLabelNeighbors_image G I e v
  rw [← e286_seed_support_code_spec G I e v, hcode] at he
  exact ⟨v, he.symm⟩

theorem e286_second_support_orbit_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V))
    (hcounts : e286GraphSupportCounts G I e = [1,0,0,0,0,0,0,0,1,1,0]) : False := by
  classical
  have hrow (s : Fin 4) : e286CountIncidence (e286GraphSupportCounts G I e) s = 2 := by
    rw [hcounts]
    fin_cases s <;> norm_num [e286CountIncidence, Fin.sum_univ_succ, e286SupportType]
  have hK (s : Fin 4) : (seedPrivateClique G I (e s)).card = 11 := by
    have hp := e286_private_multiple_card G I hI _ (e s).property (hd _ (e s).property)
    have hr := hrow s
    rw [e286_graph_support_incidence] at hr
    omega
  obtain ⟨p, hp⟩ := e286_positive_count_actual_witness G I e 0 (by rw [hcounts]; norm_num)
  obtain ⟨q, hq⟩ := e286_positive_count_actual_witness G I e 8 (by rw [hcounts]; norm_num)
  obtain ⟨r, hr⟩ := e286_positive_count_actual_witness G I e 9 (by rw [hcounts]; norm_num)
  apply e286_second_support_configuration_impossible G hG I hc hI e hK p q r
  · simpa [e286SupportType] using hp
  · simpa [e286SupportType] using hq
  · simpa [e286SupportType] using hr

/-- Both h3 orbits are excluded from the exhaustive ten-orbit classification.
The three h4 and five h5 representatives remain; E286 itself is still open. -/
theorem e286_actual_support_eight_remaining (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives.tail.tail := by
  obtain ⟨I, hc, hi, hd, e, he⟩ := e286_actual_support_nine_remaining G hG
  refine ⟨I, hc, hi, hd, e, ?_⟩
  have he' : e286GraphSupportCounts G I e = [1,0,0,0,0,0,0,0,1,1,0] ∨
      e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives.tail.tail := List.mem_cons.mp he
  rcases he' with he | he
  · exact (e286_second_support_orbit_impossible G hG I hc hi hd e he).elim
  · exact he

end EG617
