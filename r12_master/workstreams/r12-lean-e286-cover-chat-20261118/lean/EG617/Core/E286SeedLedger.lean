module
public import EG617.Core.E286PrivateClasses

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem e286_seed_incidence_sum (G : SimpleGraph V) (I : Finset V)
    (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hdeg : ∀ s ∈ I, G.degree s = 12) :
    ∑ v ∈ Iᶜ, (seedNeighbors G I v).card = 48 := by
  classical
  have ht : adjCount G Finset.univ I = 48 := by
    rw [adjCount_symm, adjCount_right_univ]
    calc
      _ = ∑ _s ∈ I, 12 := Finset.sum_congr rfl (fun s hs => hdeg s hs)
      _ = 48 := by simp [hcard]
  have hs := adjCount_union_left G I Iᶜ I disjoint_compl_right
  rw [Finset.union_compl, adjCount_independent_zero G I hI, zero_add, ht] at hs
  simpa only [adjCount_eq_sum_filter, seedNeighbors] using hs.symm

theorem e286_seed_surplus_five (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hdeg : ∀ s ∈ I, G.degree s = 12) :
    ∑ v ∈ seedMultipleSet G I, ((seedNeighbors G I v).card - 1) = 5 := by
  classical
  have hpos : ∀ v ∈ Iᶜ, 1 ≤ (seedNeighbors G I v).card := by
    intro v hv
    exact Finset.card_pos.mpr (e286_seed_dominates G hG I hcard hI v
      (Finset.mem_compl.mp hv))
  have hplus : (∑ v ∈ Iᶜ, ((seedNeighbors G I v).card - 1)) + ∑ _v ∈ Iᶜ, 1 = 48 := by
    rw [← Finset.sum_add_distrib]
    calc
      _ = ∑ v ∈ Iᶜ, (seedNeighbors G I v).card := by
        apply Finset.sum_congr rfl
        intro v hv
        exact Nat.sub_add_cancel (hpos v hv)
      _ = 48 := e286_seed_incidence_sum G I hcard hI hdeg
  have hc := Finset.card_add_card_compl I
  rw [hcard, hG.1] at hc
  simp only [Finset.sum_const, smul_eq_mul, mul_one] at hplus
  have hz : seedMultipleSet G I ⊆ Iᶜ := by
    intro v hv
    apply Finset.mem_compl.mpr
    intro hvI
    have hp := (Finset.mem_filter.mp hv).2
    rw [seedNeighbors_empty_of_seed G I hI v hvI] at hp
    simp at hp
  have he : (∑ v ∈ seedMultipleSet G I, ((seedNeighbors G I v).card - 1)) =
      ∑ v ∈ Iᶜ, ((seedNeighbors G I v).card - 1) := by
    apply Finset.sum_subset hz
    intro v _ hv
    have hn : ¬ 2 ≤ (seedNeighbors G I v).card := by
      simpa only [seedMultipleSet, Finset.mem_filter, Finset.mem_univ, true_and] using hv
    omega
  omega

theorem e286_seed_support_counts (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hdeg : ∀ s ∈ I, G.degree s = 12) :
    3 ≤ (seedMultipleSet G I).card ∧ (seedMultipleSet G I).card ≤ 5 ∧
    (∑ s ∈ I, (seedPrivateClique G I s).card) + (seedMultipleSet G I).card = 47 := by
  classical
  let Z := seedMultipleSet G I
  have hs := e286_seed_surplus_five G hG I hcard hI hdeg
  have hpos : ∀ v ∈ Z, 2 ≤ (seedNeighbors G I v).card :=
    fun v hv => (Finset.mem_filter.mp hv).2
  have hle : Z.card ≤ 5 := by
    have hl : Z.card ≤ ∑ v ∈ Z, ((seedNeighbors G I v).card - 1) := by
      calc
        _ = ∑ _v ∈ Z, 1 := by simp
        _ ≤ _ := Finset.sum_le_sum (fun v hv => by have := hpos v hv; omega)
    omega
  have hsum : (∑ v ∈ Z, (seedNeighbors G I v).card) = Z.card + 5 := by
    have he : (∑ v ∈ Z, ((seedNeighbors G I v).card - 1)) + ∑ _v ∈ Z, 1 =
        ∑ v ∈ Z, (seedNeighbors G I v).card := by
      rw [← Finset.sum_add_distrib]
      exact Finset.sum_congr rfl (fun v hv => Nat.sub_add_cancel (by have := hpos v hv; omega))
    simp only [Finset.sum_const, smul_eq_mul, mul_one] at he
    omega
  have hrows : (∑ s ∈ I, (Z.filter (G.Adj s)).card) =
      ∑ v ∈ Z, (seedNeighbors G I v).card := by
    rw [← adjCount_eq_sum_filter, adjCount_symm, adjCount_eq_sum_filter]
    rfl
  have hrow : ∀ s ∈ I, 2 ≤ (Z.filter (G.Adj s)).card := by
    intro s hsI
    have hk := hG.2.2.2.2 (seedPrivateClique G I s)
      (e286_private_class_isClique G hG I hcard hI s hsI)
    have he := e286_private_multiple_card G I hI s hsI (hdeg s hsI)
    omega
  have h8 : 8 ≤ ∑ s ∈ I, (Z.filter (G.Adj s)).card := by
    calc
      8 = ∑ _s ∈ I, 2 := by simp [hcard]
      _ ≤ _ := Finset.sum_le_sum hrow
  have htotal : (∑ s ∈ I, (seedPrivateClique G I s).card) +
      (∑ s ∈ I, (Z.filter (G.Adj s)).card) = 52 := by
    rw [← Finset.sum_add_distrib]
    calc
      _ = ∑ _s ∈ I, 13 := Finset.sum_congr rfl
        (fun s hsI => e286_private_multiple_card G I hI s hsI (hdeg s hsI))
      _ = 52 := by simp [hcard]
  change 3 ≤ Z.card ∧ Z.card ≤ 5 ∧ _
  constructor
  · omega
  constructor
  · exact hle
  · omega

theorem e286_seed_classes_cover (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V)) (v : V) :
    v ∈ seedMultipleSet G I ∨ ∃ s ∈ I, v ∈ seedPrivateClique G I s := by
  classical
  by_cases hvI : v ∈ I
  · exact Or.inr ⟨v, hvI, Finset.mem_insert_self _ _⟩
  · by_cases h2 : 2 ≤ (seedNeighbors G I v).card
    · exact Or.inl (Finset.mem_filter.mpr ⟨Finset.mem_univ v, h2⟩)
    · have hp := Finset.card_pos.mpr (e286_seed_dominates G hG I hcard hI v hvI)
      obtain ⟨s, hs⟩ := Finset.card_eq_one.mp (show (seedNeighbors G I v).card = 1 by omega)
      have hm : s ∈ seedNeighbors G I v := by rw [hs]; simp
      exact Or.inr ⟨s, (Finset.mem_filter.mp hm).1,
        Finset.mem_insert_of_mem (Finset.mem_filter.mpr ⟨Finset.mem_univ v, hs⟩)⟩

theorem seed_private_classes_disjoint (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s t : V) (hs : s ∈ I) (ht : t ∈ I)
    (hst : s ≠ t) : Disjoint (seedPrivateClique G I s) (seedPrivateClique G I t) := by
  classical
  rw [Finset.disjoint_left]
  intro v hvS hvT
  rcases Finset.mem_insert.mp hvS with he | hvS
  · subst v
    rcases Finset.mem_insert.mp hvT with he | hvT
    · exact hst he
    · exact seedNeighbors_singleton_outside G I hI t s (Finset.mem_filter.mp hvT).2 hs
  · have hvPs := (Finset.mem_filter.mp hvS).2
    rcases Finset.mem_insert.mp hvT with he | hvT
    · subst v
      exact seedNeighbors_singleton_outside G I hI s t hvPs ht
    · have hvPt := (Finset.mem_filter.mp hvT).2
      have he : ({s} : Finset V) = {t} := hvPs.symm.trans hvPt
      exact hst (Finset.singleton_injective he)

theorem seed_private_multiple_disjoint (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s : V) (hs : s ∈ I) :
    Disjoint (seedPrivateClique G I s) (seedMultipleSet G I) := by
  classical
  rw [Finset.disjoint_left]
  intro v hv hvZ
  have h2 := (Finset.mem_filter.mp hvZ).2
  rcases Finset.mem_insert.mp hv with he | hv
  · subst v
    rw [seedNeighbors_empty_of_seed G I hI s hs] at h2
    simp at h2
  · rw [(Finset.mem_filter.mp hv).2] at h2
    simp at h2

/-- Complete graph-to-support domain reduction. This is not yet the ten-orbit
classification: it constructs the actual partition and proves its finite bounds. -/
theorem e286_seed_support_reduction (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ s ∈ I, G.degree s = 12) ∧
      3 ≤ (seedMultipleSet G I).card ∧ (seedMultipleSet G I).card ≤ 5 ∧
      (∑ v ∈ seedMultipleSet G I, ((seedNeighbors G I v).card - 1)) = 5 ∧
      (∑ s ∈ I, (seedPrivateClique G I s).card) + (seedMultipleSet G I).card = 47 ∧
      (∀ s ∈ I, G.IsClique (seedPrivateClique G I s : Set V) ∧
        (seedPrivateClique G I s).card ≤ 11 ∧
        (seedPrivateClique G I s).card + ((seedMultipleSet G I).filter (G.Adj s)).card = 13) ∧
      (∀ v, v ∈ seedMultipleSet G I ∨ ∃ s ∈ I, v ∈ seedPrivateClique G I s) ∧
      (∀ s ∈ I, ∀ t ∈ I, s ≠ t →
        Disjoint (seedPrivateClique G I s) (seedPrivateClique G I t)) ∧
      (∀ s ∈ I, Disjoint (seedPrivateClique G I s) (seedMultipleSet G I)) ∧
      ∀ v ∈ seedMultipleSet G I, 2 ≤ (seedNeighbors G I v).card ∧
        (seedNeighbors G I v).card ≤ 4 := by
  obtain ⟨I, hc, hi, hd⟩ := e286_exists_regular_independent_four G hG
  obtain ⟨h3, h5, htotal⟩ := e286_seed_support_counts G hG I hc hi hd
  refine ⟨I, hc, hi, hd, h3, h5, e286_seed_surplus_five G hG I hc hi hd, htotal,
    ?_, e286_seed_classes_cover G hG I hc hi, ?_, ?_, ?_⟩
  · intro s hs
    have hk := e286_private_class_isClique G hG I hc hi s hs
    exact ⟨hk, hG.2.2.2.2 _ hk, e286_private_multiple_card G I hi s hs (hd s hs)⟩
  · intro s hs t ht hst
    exact seed_private_classes_disjoint G I hi s t hs ht hst
  · intro s hs
    exact seed_private_multiple_disjoint G I hi s hs
  · intro v hv
    refine ⟨(Finset.mem_filter.mp hv).2, ?_⟩
    have hle := Finset.card_le_card (Finset.filter_subset (G.Adj v) I)
    simpa only [seedNeighbors, hc] using hle

end EG617

