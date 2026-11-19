module
public import EG617.Core.E286SupportLift
public import EG617.Core.E286DisjointPairs

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem e286_support_type_injective : Function.Injective e286SupportType := by
  intro i j hij
  have h2 : 2 ≤ (e286SupportType i).card := by
    fin_cases i <;> norm_num [e286SupportType]
  exact (e286_support_type_complete _ h2).unique rfl hij.symm

theorem seedLabelNeighbors_relabel (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (σ : Equiv.Perm (Fin 4)) (v : V) :
    seedLabelNeighbors G I (σ.symm.trans e) v =
      (seedLabelNeighbors G I e v).image σ := by
  classical
  ext t
  constructor
  · intro ht
    have hn := (Finset.mem_filter.mp ht).2
    exact Finset.mem_image.mpr ⟨σ.symm t,
      Finset.mem_filter.mpr ⟨Finset.mem_univ _, hn⟩, σ.apply_symm_apply t⟩
  · intro ht
    obtain ⟨a, ha, he⟩ := Finset.mem_image.mp ht
    subst t
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_univ _, ?_⟩
    simpa only [Equiv.trans_apply, Equiv.symm_apply_apply] using (Finset.mem_filter.mp ha).2

/-- Relabeling the support count vector is exactly the count vector of the
inverse-reindexed actual seeds. This is a graph identity, not a finite test. -/
theorem e286_graph_support_counts_relabel (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (σ : Equiv.Perm (Fin 4)) :
    e286GraphSupportCounts G I (σ.symm.trans e) =
      e286RelabelCounts σ (e286GraphSupportCounts G I e) := by
  classical
  unfold e286RelabelCounts e286GraphSupportCounts
  simp only [e286_ofFn_get]
  apply congrArg (fun f : Fin 11 → ℕ => List.ofFn f)
  funext j
  have hf := e286_weighted_fiber_count (e286SeedSupportCode G I e)
    (fun i => if (e286SupportType i).image σ = e286SupportType j then 1 else 0)
  simp only [ite_mul, one_mul, zero_mul] at hf
  rw [hf]
  have hp (v : (seedMultipleSet G I : Set V)) :
      e286SeedSupportCode G I (σ.symm.trans e) v = j ↔
        (e286SupportType (e286SeedSupportCode G I e v)).image σ = e286SupportType j := by
    have he : e286SupportType (e286SeedSupportCode G I (σ.symm.trans e) v) =
        (e286SupportType (e286SeedSupportCode G I e v)).image σ := by
      rw [e286_seed_support_code_spec, e286_seed_support_code_spec, seedLabelNeighbors_relabel]
    constructor
    · intro h
      exact he.symm.trans (congrArg e286SupportType h)
    · intro h
      exact e286_support_type_injective (he.trans h)
  simp_rw [← hp]
  simp

/-- All ten representatives occur as distributions relative to actual
reindexed seeds. No abstract relabeling is left for the terminal proofs. -/
theorem e286_actual_oriented_support_orbit (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives := by
  obtain ⟨I, hc, hi, hd, e, σ, hσ⟩ := e286_actual_support_orbit G hG
  refine ⟨I, hc, hi, hd, σ.symm.trans e, ?_⟩
  rw [e286_graph_support_counts_relabel]
  exact hσ

theorem e286_first_support_orbit_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V))
    (hcounts : e286GraphSupportCounts G I e = [1,0,0,0,0,1,0,0,0,0,1]) : False := by
  classical
  have hrow (s : Fin 4) : e286CountIncidence (e286GraphSupportCounts G I e) s = 2 := by
    rw [hcounts]
    fin_cases s <;> norm_num [e286CountIncidence, Fin.sum_univ_succ, e286SupportType]
  have hK (s : Fin 4) : (seedPrivateClique G I (e s)).card = 11 := by
    have hp := e286_private_multiple_card G I hI _ (e s).property (hd _ (e s).property)
    have hr := hrow s
    rw [e286_graph_support_incidence] at hr
    omega
  have hcount (i : Fin 11) :
      (e286GraphSupportCounts G I e)[i.val]! =
        (Finset.univ.filter (fun v : (seedMultipleSet G I : Set V) =>
          e286SeedSupportCode G I e v = i)).card := by
    simp only [e286GraphSupportCounts, e286_ofFn_get]
  have h0 := congrArg (fun xs : List ℕ => xs[(0 : Fin 11).val]!) hcounts
  have h5 := congrArg (fun xs : List ℕ => xs[(5 : Fin 11).val]!) hcounts
  rw [hcount] at h0 h5
  norm_num at h0 h5
  obtain ⟨z, hz⟩ := Finset.card_pos.mp (show 0 <
    (Finset.univ.filter (fun v : (seedMultipleSet G I : Set V) =>
      e286SeedSupportCode G I e v = 0)).card by omega)
  obtain ⟨w, hw⟩ := Finset.card_pos.mp (show 0 <
    (Finset.univ.filter (fun v : (seedMultipleSet G I : Set V) =>
      e286SeedSupportCode G I e v = 5)).card by omega)
  have hzcode := (Finset.mem_filter.mp hz).2
  have hwcode := (Finset.mem_filter.mp hw).2
  have hzlabel : seedLabelNeighbors G I e z = {0, 1} := by
    rw [← e286_seed_support_code_spec G I e z, hzcode]
    rfl
  have hwlabel : seedLabelNeighbors G I e w = {2, 3} := by
    rw [← e286_seed_support_code_spec G I e w, hwcode]
    rfl
  have hzactual := seedLabelNeighbors_image G I e z
  have hwactual := seedLabelNeighbors_image G I e w
  rw [hzlabel] at hzactual
  rw [hwlabel] at hwactual
  apply e286_complementary_k11_pairs_impossible G hG I hc hI e hK z w
  · simpa using hzactual.symm
  · simpa using hwactual.symm

/-- The first frozen orbit is excluded after actual realization; the other
nine remain, so this is not E286 nonexistence. -/
theorem e286_actual_support_nine_remaining (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives.tail := by
  obtain ⟨I, hc, hi, hd, e, he⟩ := e286_actual_oriented_support_orbit G hG
  refine ⟨I, hc, hi, hd, e, ?_⟩
  have he' : e286GraphSupportCounts G I e = [1,0,0,0,0,1,0,0,0,0,1] ∨
      e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives.tail := List.mem_cons.mp he
  rcases he' with he | he
  · exact (e286_first_support_orbit_impossible G hG I hc hi hd e he).elim
  · exact he

end EG617
