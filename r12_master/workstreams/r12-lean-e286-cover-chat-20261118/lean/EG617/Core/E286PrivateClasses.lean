module
public import EG617.Core.E286Seeds

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

noncomputable def seedNeighbors (G : SimpleGraph V) (I : Finset V) (v : V) : Finset V :=
  I.filter (G.Adj v)

noncomputable def seedPrivateClique (G : SimpleGraph V) (I : Finset V) (s : V) : Finset V :=
  insert s (Finset.univ.filter (fun v => seedNeighbors G I v = {s}))

noncomputable def seedMultipleSet (G : SimpleGraph V) (I : Finset V) : Finset V :=
  Finset.univ.filter (fun v => 2 ≤ (seedNeighbors G I v).card)

theorem seedNeighbors_empty_of_seed (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s : V) (hs : s ∈ I) :
    seedNeighbors G I s = ∅ := by
  classical
  apply Finset.eq_empty_iff_forall_notMem.mpr
  intro t ht
  obtain ⟨htI, hadj⟩ := Finset.mem_filter.mp ht
  by_cases hst : s = t
  · subst t
    exact G.loopless.irrefl s hadj
  · exact hI hs htI hst hadj

theorem seedNeighbors_singleton_outside (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s v : V)
    (hv : seedNeighbors G I v = {s}) : v ∉ I := by
  intro hvI
  have he := seedNeighbors_empty_of_seed G I hI v hvI
  rw [hv] at he
  have hc := congrArg Finset.card he
  simp at hc

theorem seedNeighbors_singleton_nonadj (G : SimpleGraph V) (I : Finset V)
    (s v : V) (hv : seedNeighbors G I v = {s}) (t : V) (ht : t ∈ I)
    (hts : t ≠ s) : ¬ G.Adj v t := by
  intro hadj
  have hm : t ∈ seedNeighbors G I v := Finset.mem_filter.mpr ⟨ht, hadj⟩
  rw [hv] at hm
  exact hts (Finset.mem_singleton.mp hm)

/-- Actual private classes are cliques, by the original alpha4 bound. -/
theorem e286_private_class_isClique (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (s : V) (hs : s ∈ I) :
    G.IsClique (seedPrivateClique G I s : Set V) := by
  classical
  have hadj (v : V) (hv : seedNeighbors G I v = {s}) : G.Adj s v := by
    have hm : s ∈ seedNeighbors G I v := by rw [hv]; simp
    exact (Finset.mem_filter.mp hm).2.symm
  intro x hx y hy hxy
  rcases Finset.mem_insert.mp hx with rfl | hx
  · rcases Finset.mem_insert.mp hy with rfl | hy
    · exact (hxy rfl).elim
    · exact hadj y (Finset.mem_filter.mp hy).2
  · have hxP := (Finset.mem_filter.mp hx).2
    rcases Finset.mem_insert.mp hy with rfl | hy
    · exact (hadj x hxP).symm
    · have hyP := (Finset.mem_filter.mp hy).2
      by_contra hnxy
      have hxI := seedNeighbors_singleton_outside G I hI s x hxP
      have hyI := seedNeighbors_singleton_outside G I hI s y hyP
      let J := insert y (I.erase s)
      have hJ : G.IsIndepSet (J : Set V) := by
        intro a ha b hb hab
        rcases Finset.mem_insert.mp ha with he | ha
        · subst a
          have hb' := Finset.mem_of_mem_insert_of_ne hb hab.symm
          exact seedNeighbors_singleton_nonadj G I s y hyP b
            (Finset.mem_erase.mp hb').2 (Finset.mem_erase.mp hb').1
        · rcases Finset.mem_insert.mp hb with he | hb
          · subst b
            intro he
            exact seedNeighbors_singleton_nonadj G I s y hyP a
              (Finset.mem_erase.mp ha).2 (Finset.mem_erase.mp ha).1 he.symm
          · exact hI (Finset.mem_erase.mp ha).2 (Finset.mem_erase.mp hb).2 hab
      have hn : ∀ z ∈ J, z ≠ x ∧ ¬ G.Adj x z := by
        intro z hz
        rcases Finset.mem_insert.mp hz with he | hz
        · subst z
          exact ⟨hxy.symm, hnxy⟩
        · exact ⟨fun he => hxI (he ▸ (Finset.mem_erase.mp hz).2),
            seedNeighbors_singleton_nonadj G I s x hxP z
              (Finset.mem_erase.mp hz).2 (Finset.mem_erase.mp hz).1⟩
      have hb := core_independence_nonNeighbors G 3 hG.2.2.2.1 x J hn hJ
      have hyErase : y ∉ I.erase s := fun h => hyI (Finset.mem_erase.mp h).2
      have hJcard : J.card = 4 := by
        dsimp only [J]
        rw [Finset.card_insert_of_notMem hyErase, Finset.card_erase_of_mem hs, hcard]
      omega

/-- Every nonseed sees a seed; the four-set is derived in the parent theorem. -/
theorem e286_seed_dominates (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (v : V) (hv : v ∉ I) : (seedNeighbors G I v).Nonempty := by
  classical
  by_contra hn
  have he : seedNeighbors G I v = ∅ := Finset.not_nonempty_iff_eq_empty.mp hn
  have hnon : ∀ z ∈ I, z ≠ v ∧ ¬ G.Adj v z := by
    intro z hz
    refine ⟨fun h => hv (h ▸ hz), ?_⟩
    intro hadj
    have hm : z ∈ seedNeighbors G I v := Finset.mem_filter.mpr ⟨hz, hadj⟩
    rw [he] at hm
    exact Finset.notMem_empty z hm
  have hb := core_independence_nonNeighbors G 3 hG.2.2.2.1 v I hnon hI
  omega

/-- Private clique plus multiple-support neighbors accounts for the actual
twelve neighbors and the seed itself. -/
theorem e286_private_multiple_card (G : SimpleGraph V)
    (I : Finset V) (hI : G.IsIndepSet (I : Set V)) (s : V) (hs : s ∈ I)
    (hdeg : G.degree s = 12) :
    (seedPrivateClique G I s).card +
      ((seedMultipleSet G I).filter (G.Adj s)).card = 13 := by
  classical
  let P := Finset.univ.filter (fun v => seedNeighbors G I v = {s})
  let Z := (seedMultipleSet G I).filter (G.Adj s)
  have hsP : s ∉ P := by
    intro hm
    exact seedNeighbors_singleton_outside G I hI s s (Finset.mem_filter.mp hm).2 hs
  have hu : P ∪ Z = G.neighborFinset s := by
    ext v
    constructor
    · intro hv
      rcases Finset.mem_union.mp hv with hv | hv
      · have he := (Finset.mem_filter.mp hv).2
        have hm : s ∈ seedNeighbors G I v := by rw [he]; simp
        exact (SimpleGraph.mem_neighborFinset G s v).mpr (Finset.mem_filter.mp hm).2.symm
      · exact (SimpleGraph.mem_neighborFinset G s v).mpr (Finset.mem_filter.mp hv).2
    · intro hv
      have hadj := (SimpleGraph.mem_neighborFinset G s v).mp hv
      have hm : s ∈ seedNeighbors G I v := Finset.mem_filter.mpr ⟨hs, hadj.symm⟩
      by_cases h2 : 2 ≤ (seedNeighbors G I v).card
      · exact Finset.mem_union_right _ (Finset.mem_filter.mpr
          ⟨Finset.mem_filter.mpr ⟨Finset.mem_univ v, h2⟩, hadj⟩)
      · have h1 : (seedNeighbors G I v).card = 1 := by
          have hp := Finset.card_pos.mpr ⟨s, hm⟩
          omega
        obtain ⟨t, ht⟩ := Finset.card_eq_one.mp h1
        have hst : s = t := by rw [ht] at hm; exact Finset.mem_singleton.mp hm
        have he : seedNeighbors G I v = {s} := by simpa only [hst] using ht
        exact Finset.mem_union_left _ (Finset.mem_filter.mpr ⟨Finset.mem_univ v, he⟩)
  have hd : Disjoint P Z := by
    rw [Finset.disjoint_left]
    intro v hvP hvZ
    have he := (Finset.mem_filter.mp hvP).2
    have h2 := (Finset.mem_filter.mp (Finset.mem_filter.mp hvZ).1).2
    rw [he] at h2
    simp at h2
  have hc := congrArg Finset.card hu
  rw [Finset.card_union_of_disjoint hd, SimpleGraph.card_neighborFinset_eq_degree] at hc
  change (insert s P).card + Z.card = 13
  rw [Finset.card_insert_of_notMem hsP]
  simp only [← SimpleGraph.ncard_neighborSet] at hc hdeg
  omega

end EG617

