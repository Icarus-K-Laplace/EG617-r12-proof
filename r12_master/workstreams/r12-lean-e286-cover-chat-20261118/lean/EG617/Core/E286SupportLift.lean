module
public import EG617.Core.E286SupportCounts

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

noncomputable def seedLabelNeighbors (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : V) : Finset (Fin 4) :=
  Finset.univ.filter (fun i => G.Adj v (e i))

theorem seedLabelNeighbors_image (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : V) :
    (seedLabelNeighbors G I e v).image (fun i => (e i : V)) = seedNeighbors G I v := by
  classical
  ext w
  constructor
  · intro hw
    obtain ⟨i, hi, rfl⟩ := Finset.mem_image.mp hw
    exact Finset.mem_filter.mpr ⟨(e i).property, (Finset.mem_filter.mp hi).2⟩
  · intro hw
    obtain ⟨hwI, hvw⟩ := Finset.mem_filter.mp hw
    obtain ⟨i, hi⟩ := e.surjective ⟨w, hwI⟩
    refine Finset.mem_image.mpr ⟨i, Finset.mem_filter.mpr ⟨Finset.mem_univ i, ?_⟩, ?_⟩
    · simpa only [hi] using hvw
    · exact congrArg Subtype.val hi

theorem seedLabelNeighbors_card (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : V) :
    (seedLabelNeighbors G I e v).card = (seedNeighbors G I v).card := by
  have h := congrArg Finset.card (seedLabelNeighbors_image G I e v)
  have hinj : Function.Injective (fun i : Fin 4 => (e i : V)) := by
    intro a b hab
    exact e.injective (Subtype.ext hab)
  rw [Finset.card_image_of_injective _ hinj] at h
  exact h

theorem e286_seed_support_code_exists (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : (seedMultipleSet G I : Set V)) :
    ∃ i : Fin 11, e286SupportType i = seedLabelNeighbors G I e v := by
  have h2 := (Finset.mem_filter.mp v.property).2
  have hl : 2 ≤ (seedLabelNeighbors G I e v).card := by
    rw [seedLabelNeighbors_card]
    exact h2
  exact (e286_support_type_complete _ hl).exists

noncomputable def e286SeedSupportCode (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : (seedMultipleSet G I : Set V)) : Fin 11 :=
  Classical.choose (e286_seed_support_code_exists G I e v)

theorem e286_seed_support_code_spec (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : (seedMultipleSet G I : Set V)) :
    e286SupportType (e286SeedSupportCode G I e v) = seedLabelNeighbors G I e v :=
  Classical.choose_spec (e286_seed_support_code_exists G I e v)

noncomputable def e286GraphSupportCounts (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) : List ℕ :=
  List.ofFn fun i : Fin 11 =>
    (Finset.univ.filter (fun v : (seedMultipleSet G I : Set V) =>
      e286SeedSupportCode G I e v = i)).card

theorem e286_ofFn_get (f : Fin 11 → ℕ) (i : Fin 11) :
    (List.ofFn f)[i.val]! = f i := by fin_cases i <;> rfl

theorem e286_weightedSum_ofFn (f : Fin 11 → ℕ) :
    e286WeightedSum e286SupportWeights (List.ofFn f) =
      ∑ i : Fin 11, ((e286SupportType i).card - 1) * f i := by
  simp [e286WeightedSum, e286SupportWeights, List.ofFn_succ,
    Fin.sum_univ_succ, e286SupportType]

theorem e286_weighted_fiber_count {W : Type u} [Fintype W]
    (code : W → Fin 11) (w : Fin 11 → ℕ) :
    (∑ i : Fin 11, w i * (Finset.univ.filter (fun v => code v = i)).card) =
      ∑ v : W, w (code v) := by
  classical
  simpa only [Finset.sum_const, smul_eq_mul, Nat.mul_comm] using
    Finset.sum_fiberwise' (Finset.univ : Finset W) code w

theorem e286_graph_support_weighted_sum (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hi : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V)) :
    e286WeightedSum e286SupportWeights (e286GraphSupportCounts G I e) = 5 := by
  classical
  unfold e286GraphSupportCounts
  rw [e286_weightedSum_ofFn, e286_weighted_fiber_count]
  have he : (∑ v : (seedMultipleSet G I : Set V),
      ((e286SupportType (e286SeedSupportCode G I e v)).card - 1)) =
      ∑ v : (seedMultipleSet G I : Set V), ((seedNeighbors G I v).card - 1) := by
    apply Finset.sum_congr rfl
    intro v _
    rw [e286_seed_support_code_spec, seedLabelNeighbors_card]
  rw [he]
  exact (Finset.sum_subtype (seedMultipleSet G I) (fun _ => Iff.rfl)
    (fun v => (seedNeighbors G I v).card - 1)).symm.trans
      (e286_seed_surplus_five G hG I hc hi hd)

theorem e286_graph_support_incidence (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (s : Fin 4) :
    e286CountIncidence (e286GraphSupportCounts G I e) s =
      ((seedMultipleSet G I).filter (G.Adj (e s))).card := by
  classical
  simp only [e286CountIncidence, e286GraphSupportCounts, e286_ofFn_get]
  have hf := e286_weighted_fiber_count (e286SeedSupportCode G I e)
    (fun i => if s ∈ e286SupportType i then 1 else 0)
  simp only [ite_mul, one_mul, zero_mul] at hf
  rw [hf]
  have he : (∑ v : (seedMultipleSet G I : Set V),
      if s ∈ e286SupportType (e286SeedSupportCode G I e v) then 1 else 0) =
      ∑ v : (seedMultipleSet G I : Set V), if G.Adj (e s) v then 1 else 0 := by
    apply Finset.sum_congr rfl
    intro v _
    rw [e286_seed_support_code_spec]
    simp only [seedLabelNeighbors, Finset.mem_filter, Finset.mem_univ, true_and,
      G.adj_comm (v : V) (e s)]
  rw [he]
  calc
    _ = ∑ v ∈ seedMultipleSet G I, if G.Adj (e s) v then 1 else 0 :=
      (Finset.sum_subtype (seedMultipleSet G I) (fun _ => Iff.rfl)
        (fun v => if G.Adj (e s) v then 1 else 0)).symm
    _ = _ := by simp

/-- The ten-orbit count classification is applied to the actual graph, after
the regular seeds, partition, surplus and every incidence bound have been
derived from the original five hypotheses. No abstract count vector is assumed. -/
theorem e286_actual_support_orbit (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧
      ∃ e : Fin 4 ≃ (I : Set V), ∃ σ : Equiv.Perm (Fin 4),
        e286RelabelCounts σ (e286GraphSupportCounts G I e) ∈
          e286SupportOrbitRepresentatives := by
  classical
  obtain ⟨I, hc, hi, hd⟩ := e286_exists_regular_independent_four G hG
  let e : Fin 4 ≃ (I : Set V) := Fintype.equivOfCardEq (by
    simp only [Fintype.card_fin, Set.fintypeCard_eq_ncard, Set.ncard_coe_finset, hc])
  have hlen : (e286GraphSupportCounts G I e).length = 11 := by
    simp [e286GraphSupportCounts]
  have hsum := e286_graph_support_weighted_sum G hG I hc hi hd e
  have hinc : ∀ s : Fin 4, 2 ≤ e286CountIncidence (e286GraphSupportCounts G I e) s := by
    intro s
    rw [e286_graph_support_incidence]
    have hk := hG.2.2.2.2 (seedPrivateClique G I (e s))
      (e286_private_class_isClique G hG I hc hi (e s) (e s).property)
    have hp := e286_private_multiple_card G I hi (e s) (e s).property (hd (e s) (e s).property)
    omega
  obtain ⟨σ, hσ⟩ := e286_support_counts_complete _ hlen hsum hinc
  exact ⟨I, hc, hi, hd, e, σ, hσ⟩

end EG617

