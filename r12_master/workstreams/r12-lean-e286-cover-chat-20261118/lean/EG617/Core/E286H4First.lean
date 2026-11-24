module
public import EG617.Core.E286Mixed

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- A multiplicity at least two produces distinct actual vertices, not two
names for a single representative. -/
theorem e286_double_count_actual_witnesses (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (i : Fin 11)
    (hpos : 2 ≤ (e286GraphSupportCounts G I e)[i.val]!) :
    ∃ p q : V, p ≠ q ∧
      seedNeighbors G I p = (e286SupportType i).image (fun j => (e j : V)) ∧
      seedNeighbors G I q = (e286SupportType i).image (fun j => (e j : V)) := by
  classical
  simp only [e286GraphSupportCounts, e286_ofFn_get] at hpos
  obtain ⟨p, hp, q, hq, hpq⟩ := Finset.one_lt_card.mp (show 1 <
    (Finset.univ.filter (fun v : (seedMultipleSet G I : Set V) =>
      e286SeedSupportCode G I e v = i)).card by omega)
  have actual (v : (seedMultipleSet G I : Set V)) (hv : e286SeedSupportCode G I e v = i) :
      seedNeighbors G I v = (e286SupportType i).image (fun j => (e j : V)) := by
    have he := seedLabelNeighbors_image G I e v
    rw [← e286_seed_support_code_spec G I e v, hv] at he
    exact he.symm
  exact ⟨p, q, (fun h => hpq (Subtype.ext h)),
    actual p (Finset.mem_filter.mp hp).2, actual q (Finset.mem_filter.mp hq).2⟩

/-- Frozen Section6, first h4 pattern. The unused triple support need not
be assumed: two distinct 01 points and the 23 point already contradict excess8. -/
theorem e286_doubled_mixed_opposite_pair_impossible (G : SimpleGraph V)
    (hG : E286Hypotheses G) (I : Finset V) (hc : I.card = 4)
    (hI : G.IsIndepSet (I : Set V)) (e : Fin 4 ≃ (I : Set V))
    (hK0 : (seedPrivateClique G I (e 0)).card = 10)
    (hK : ∀ s : Fin 4, s ≠ 0 → (seedPrivateClique G I (e s)).card = 11)
    (p q r : V) (hpq : p ≠ q)
    (hp : seedNeighbors G I p = {(e 0 : V), (e 1 : V)})
    (hq : seedNeighbors G I q = {(e 0 : V), (e 1 : V)})
    (hr : seedNeighbors G I r = {(e 2 : V), (e 3 : V)}) : False := by
  classical
  let K := fun s : Fin 4 => seedPrivateClique G I (e s)
  let A := K 0 ∪ K 1
  let B := insert r (K 2 ∪ K 3)
  have heinj : Function.Injective (fun s : Fin 4 => (e s : V)) := by
    intro a b hab
    exact e.injective (Subtype.ext hab)
  have hne (a b : Fin 4) (hab : a ≠ b) : (e a : V) ≠ e b := fun h => hab (heinj h)
  have hrZ := e286_pair_support_mem_multiple G I _ _ r (hne 2 3 (by decide)) hr
  have hout (v : V) (hv : v ∈ seedMultipleSet G I) (s : Fin 4) : v ∉ K s := by
    intro hm
    exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hI _ (e s).property) hm hv
  have hsep (a b : Fin 4) (hab : a ≠ b) : Disjoint (K a) (K b) :=
    seed_private_classes_disjoint G I hI _ _ (e a).property (e b).property (hne a b hab)
  have hAB : Disjoint A (K 2 ∪ K 3) := by
    dsimp only [A]
    rw [Finset.disjoint_union_left, Finset.disjoint_union_right, Finset.disjoint_union_right]
    exact ⟨⟨hsep 0 2 (by decide), hsep 0 3 (by decide)⟩,
      ⟨hsep 1 2 (by decide), hsep 1 3 (by decide)⟩⟩
  have hrA : r ∉ A := by
    intro hm
    exact (Finset.mem_union.mp hm).elim (hout r hrZ 0) (hout r hrZ 1)
  have hvB (v : V) (hv : seedNeighbors G I v = {(e 0 : V), (e 1 : V)}) : v ∉ B := by
    have hvZ := e286_pair_support_mem_multiple G I _ _ v (hne 0 1 (by decide)) hv
    have hvr : v ≠ r := by
      intro he
      have hm : (e 0 : V) ∈ seedNeighbors G I v := by rw [hv]; simp
      rw [he, hr] at hm
      simp only [Finset.mem_insert, Finset.mem_singleton] at hm
      exact hm.elim (hne 0 2 (by decide)) (hne 0 3 (by decide))
    intro hm
    rcases Finset.mem_insert.mp hm with he | hm
    · exact hvr he
    · exact (Finset.mem_union.mp hm).elim (hout v hvZ 2) (hout v hvZ 3)
  have hr6 : 6 ≤ ∑ v ∈ B, degreeExcess12 G v :=
    e286_private_k11_pair_charge G hG I hc hI _ _ r
      (e 2).property (e 3).property (hne 2 3 (by decide)) hr
      (hK 2 (by decide)) (hK 3 (by decide))
  have complete (v : V) (hv : seedNeighbors G I v = {(e 0 : V), (e 1 : V)}) :
      ∀ x ∈ K 0, G.Adj v x := by
    rcases e286_private_mixed_pair_dichotomy G hG I hc hI _ _ v
      (e 0).property (e 1).property (hne 0 1 (by decide)) hv hK0 (hK 1 (by decide))
      with hcomp | h4
    · exact hcomp
    · have hdis : Disjoint (insert v A) B := by
        rw [Finset.disjoint_left]
        intro x hx hxB
        rcases Finset.mem_insert.mp hx with he | hx
        · subst x
          exact hvB v hv hxB
        · rcases Finset.mem_insert.mp hxB with he | hxB
          · subst x
            exact hrA hx
          · exact Finset.disjoint_left.mp hAB hx hxB
      have h8 := e286_subset_excess_budget G hG (insert v A ∪ B)
      rw [Finset.sum_union hdis] at h8
      change 4 ≤ ∑ x ∈ insert v A, degreeExcess12 G x at h4
      omega
  have hpZ := e286_pair_support_mem_multiple G I _ _ p (hne 0 1 (by decide)) hp
  have hqZ := e286_pair_support_mem_multiple G I _ _ q (hne 0 1 (by decide)) hq
  have h7 := (e286_ten_clique_completers_excess G hG (K 0) hK0
    (e286_private_class_isClique G hG I hc hI _ (e 0).property) p q hpq
    (hout p hpZ 0) (hout q hqZ 0) (fun x hx => ⟨complete p hp x hx, complete q hq x hx⟩)).2
  have hdis : Disjoint ({p, q} : Finset V) B := by
    rw [Finset.disjoint_left]
    intro x hx hxB
    rcases Finset.mem_insert.mp hx with he | hx
    · subst x
      exact hvB p hp hxB
    · have he := Finset.mem_singleton.mp hx
      subst x
      exact hvB q hq hxB
  have h8 := e286_subset_excess_budget G hG (({p, q} : Finset V) ∪ B)
  rw [Finset.sum_union hdis, Finset.sum_pair hpq] at h8
  omega

/-- The third representative is realized on the actual graph; all clique
sizes and multiplicities are derived, including the two distinct 01 vertices. -/
theorem e286_third_support_orbit_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V))
    (hcounts : e286GraphSupportCounts G I e = [2,0,0,0,0,1,0,0,1,0,0]) : False := by
  classical
  have hrow (s : Fin 4) : e286CountIncidence (e286GraphSupportCounts G I e) s =
      if s = 0 then 3 else 2 := by
    rw [hcounts]
    fin_cases s <;> norm_num [e286CountIncidence, Fin.sum_univ_succ, e286SupportType]
  have hK0 : (seedPrivateClique G I (e 0)).card = 10 := by
    have hp := e286_private_multiple_card G I hI _ (e 0).property (hd _ (e 0).property)
    have hr := hrow 0
    rw [e286_graph_support_incidence] at hr
    norm_num at hr
    omega
  have hK (s : Fin 4) (hs : s ≠ 0) : (seedPrivateClique G I (e s)).card = 11 := by
    have hp := e286_private_multiple_card G I hI _ (e s).property (hd _ (e s).property)
    have hr := hrow s
    rw [e286_graph_support_incidence, if_neg hs] at hr
    omega
  obtain ⟨p, q, hpq, hp, hq⟩ := e286_double_count_actual_witnesses G I e 0 (by rw [hcounts]; norm_num)
  obtain ⟨r, hr⟩ := e286_positive_count_actual_witness G I e 5 (by rw [hcounts]; norm_num)
  apply e286_doubled_mixed_opposite_pair_impossible G hG I hc hI e hK0 hK p q r hpq
  · simpa [e286SupportType] using hp
  · simpa [e286SupportType] using hq
  · simpa [e286SupportType] using hr

/-- Both h3 and the first h4 orbit are excluded. The two other h4 and five h5
orbits remain; this theorem is not E286 nonexistence. -/
theorem e286_actual_support_seven_remaining (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives.tail.tail.tail := by
  obtain ⟨I, hc, hi, hd, e, he⟩ := e286_actual_support_eight_remaining G hG
  refine ⟨I, hc, hi, hd, e, ?_⟩
  have he' : e286GraphSupportCounts G I e = [2,0,0,0,0,1,0,0,1,0,0] ∨
      e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives.tail.tail.tail := List.mem_cons.mp he
  rcases he' with he | he
  · exact (e286_third_support_orbit_impossible G hG I hc hi hd e he).elim
  · exact he

end EG617
