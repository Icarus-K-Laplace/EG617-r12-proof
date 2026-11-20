module
public import EG617.Core.E286TripleCharge

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Frozen Section4 for actual private cliques. Every geometric premise of
the three-clique charge is derived from the actual seed support and alpha4.
No local-budget or ordered-missing-set hypothesis is assumed. -/
theorem e286_private_triple_k11_charge (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (e : Fin 4 ≃ (I : Set V)) (z : V)
    (hz : seedNeighbors G I z = {(e 0 : V), (e 1 : V), (e 2 : V)})
    (hK : ∀ i : Fin 4, i ≠ 3 → (seedPrivateClique G I (e i)).card = 11) :
    3 ≤ ∑ v ∈ insert z (seedPrivateClique G I (e 0) ∪
      seedPrivateClique G I (e 1) ∪ seedPrivateClique G I (e 2)), degreeExcess12 G v := by
  classical
  let K := fun i : Fin 4 => seedPrivateClique G I (e i)
  have heinj : Function.Injective (fun i : Fin 4 => (e i : V)) := by
    intro a b hab
    exact e.injective (Subtype.ext hab)
  have hne (a b : Fin 4) (hab : a ≠ b) : (e a : V) ≠ e b := fun h => hab (heinj h)
  have hcl (i : Fin 4) : G.IsClique (K i : Set V) :=
    e286_private_class_isClique G hG I hc hI _ (e i).property
  have hdis (a b : Fin 4) (hab : a ≠ b) : Disjoint (K a) (K b) :=
    seed_private_classes_disjoint G I hI _ _ (e a).property (e b).property (hne a b hab)
  have hzZ : z ∈ seedMultipleSet G I := by
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_univ _, ?_⟩
    rw [hz, Finset.card_insert_of_notMem (show (e 0 : V) ∉ ({(e 1 : V), (e 2 : V)} : Finset V) by
      simp [hne 0 1 (by decide), hne 0 2 (by decide)]), Finset.card_pair (hne 1 2 (by decide))]
    omega
  have hzout (i : Fin 4) : z ∉ K i := by
    intro hm
    exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hI _ (e i).property) hm hzZ
  have hsout (i : Fin 4) (hi : i ≠ 3) : (e 3 : V) ∉ K i := by
    intro hm
    have he := seed_private_mem_seed G I hI (e i) (e 3) hm (e 3).property
    exact hne 3 i hi.symm he
  have hanti (i : Fin 4) (hi : i ≠ 3) (v : V) (hv : v ∈ K i) : ¬ G.Adj v (e 3) :=
    seed_private_nonadj_other_seed G I hI (e i) (e 3) v (e i).property
      (e 3).property (hne 3 i hi.symm) hv
  have hadj (i : Fin 4) (hi : i = 0 ∨ i = 1 ∨ i = 2) : G.Adj z (e i) := by
    have hm : (e i : V) ∈ seedNeighbors G I z := by
      rw [hz]
      rcases hi with he | he | he <;> subst i <;> simp
    exact (Finset.mem_filter.mp hm).2
  have hzs : z ≠ (e 3 : V) := by
    intro he
    have h := hadj 0 (Or.inl rfl)
    rw [he] at h
    exact hI (e 3).property (e 0).property (hne 3 0 (by decide)) h
  have hnzs : ¬ G.Adj z (e 3) := by
    intro h
    have hm : (e 3 : V) ∈ seedNeighbors G I z := Finset.mem_filter.mpr ⟨(e 3).property, h⟩
    rw [hz] at hm
    simp only [Finset.mem_insert, Finset.mem_singleton] at hm
    rcases hm with he | he | he
    · exact hne 3 0 (by decide) he
    · exact hne 3 1 (by decide) he
    · exact hne 3 2 (by decide) he
  apply e286_three_k11_local_charge G hG (K 0) (K 1) (K 2) (hcl 0) (hcl 1) (hcl 2)
    (hK 0 (by decide)) (hK 1 (by decide)) (hK 2 (by decide))
    (hdis 0 1 (by decide)) (hdis 0 2 (by decide)) (hdis 1 2 (by decide))
    z (e 3) hzs hnzs (hzout 0) (hzout 1) (hzout 2)
    (hsout 0 (by decide)) (hsout 1 (by decide)) (hsout 2 (by decide))
  · intro v hv
    rcases Finset.mem_union.mp hv with hv | hv
    · rcases Finset.mem_union.mp hv with hv | hv
      · exact hanti 0 (by decide) v hv
      · exact hanti 1 (by decide) v hv
    · exact hanti 2 (by decide) v hv
  · exact ⟨e 0, Finset.mem_insert_self _ _, hadj 0 (Or.inl rfl)⟩
  · exact ⟨e 1, Finset.mem_insert_self _ _, hadj 1 (Or.inr (Or.inl rfl))⟩
  · exact ⟨e 2, Finset.mem_insert_self _ _, hadj 2 (Or.inr (Or.inr rfl))⟩

end EG617
