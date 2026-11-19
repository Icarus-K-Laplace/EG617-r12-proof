module
public import EG617.Core.E286SeedLedger
public import EG617.Core.E286CommonNeighbors

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem seed_private_nonadj_other_seed (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s t x : V) (hs : s ∈ I) (ht : t ∈ I)
    (hts : t ≠ s) (hx : x ∈ seedPrivateClique G I s) : ¬ G.Adj x t := by
  rcases Finset.mem_insert.mp hx with he | hx
  · subst x
    exact hI hs ht hts.symm
  · exact seedNeighbors_singleton_nonadj G I s x (Finset.mem_filter.mp hx).2 t ht hts

theorem seed_private_mem_seed (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s x : V)
    (hx : x ∈ seedPrivateClique G I s) (hxI : x ∈ I) : x = s := by
  rcases Finset.mem_insert.mp hx with he | hx
  · exact he
  · exact (seedNeighbors_singleton_outside G I hI s x (Finset.mem_filter.mp hx).2 hxI).elim

/-- Frozen Section3: a pair-support point forces every edge between its two
actual missing sets. No compatibility relation is treated as adjacency. -/
theorem e286_pair_blocker_complete (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (i j z : V) (hi : i ∈ I) (hj : j ∈ I) (hij : i ≠ j)
    (hz : seedNeighbors G I z = {i, j})
    (x y : V) (hx : x ∈ seedPrivateClique G I i)
    (hy : y ∈ seedPrivateClique G I j) (hzx : ¬ G.Adj z x) (hzy : ¬ G.Adj z y) :
    G.Adj x y := by
  classical
  by_contra hxy
  let R := (I.erase i).erase j
  have hR (t : V) (ht : t ∈ R) : t ∈ I ∧ t ≠ i ∧ t ≠ j := by
    obtain ⟨htj, ht'⟩ := Finset.mem_erase.mp ht
    obtain ⟨hti, htI⟩ := Finset.mem_erase.mp ht'
    exact ⟨htI, hti, htj⟩
  have hji : j ∈ I.erase i := Finset.mem_erase.mpr ⟨hij.symm, hj⟩
  have hRc : R.card = 2 := by
    dsimp only [R]
    rw [Finset.card_erase_of_mem hji, Finset.card_erase_of_mem hi, hc]
  have hxR : x ∉ R := by
    intro h
    exact (hR x h).2.1 (seed_private_mem_seed G I hI i x hx (hR x h).1)
  have hyR : y ∉ R := by
    intro h
    exact (hR y h).2.2 (seed_private_mem_seed G I hI j y hy (hR y h).1)
  have hxyne : x ≠ y := by
    intro he
    subst y
    exact Finset.disjoint_left.mp (seed_private_classes_disjoint G I hI i j hi hj hij)
      hx hy
  have hRI : G.IsIndepSet (R : Set V) := fun a ha b hb hab =>
    hI (hR a ha).1 (hR b hb).1 hab
  have hyRI : G.IsIndepSet ((insert y R : Finset V) : Set V) := by
    rw [Finset.coe_insert]
    apply hRI.insert
    intro t ht _
    have hn := seed_private_nonadj_other_seed G I hI j t y hj (hR t ht).1 (hR t ht).2.2 hy
    exact ⟨hn, fun h => hn h.symm⟩
  have hJ : G.IsIndepSet ((insert x (insert y R) : Finset V) : Set V) := by
    rw [Finset.coe_insert]
    apply hyRI.insert
    intro t ht _
    rcases Finset.mem_insert.mp ht with he | ht
    · subst t
      exact ⟨hxy, fun h => hxy h.symm⟩
    · have hn := seed_private_nonadj_other_seed G I hI i t x hi (hR t ht).1 (hR t ht).2.1 hx
      exact ⟨hn, fun h => hn h.symm⟩
  have hzZ : z ∈ seedMultipleSet G I := by
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_univ _, ?_⟩
    rw [hz, Finset.card_pair hij]
  have hzI : z ∉ I := by
    intro hm
    have he := seedNeighbors_empty_of_seed G I hI z hm
    rw [hz] at he
    have hp := congrArg Finset.card he
    simp [hij] at hp
  have hn : ∀ t ∈ insert x (insert y R), t ≠ z ∧ ¬ G.Adj z t := by
    intro t ht
    rcases Finset.mem_insert.mp ht with he | ht
    · subst t
      refine ⟨?_, hzx⟩
      intro he
      subst z
      exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hI i hi)
        hx hzZ
    · rcases Finset.mem_insert.mp ht with he | ht
      · subst t
        refine ⟨?_, hzy⟩
        intro he
        subst z
        exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hI j hj)
          hy hzZ
      · refine ⟨fun he => hzI (he ▸ (hR t ht).1), ?_⟩
        intro hadj
        have hm : t ∈ seedNeighbors G I z := Finset.mem_filter.mpr ⟨(hR t ht).1, hadj⟩
        rw [hz] at hm
        exact (Finset.mem_pair.mp hm).elim (hR t ht).2.1 (hR t ht).2.2
  have hb := core_independence_nonNeighbors G 3 hG.2.2.2.1 z _ hn hJ
  have hx' : x ∉ insert y R := by simp [hxyne, hxR]
  rw [Finset.card_insert_of_notMem hx', Finset.card_insert_of_notMem hyR, hRc] at hb
  omega

/-- Every local charge is bounded by the original global excess8. -/
theorem e286_subset_excess_budget (G : SimpleGraph V) (hG : E286Hypotheses G)
    (S : Finset V) : (∑ v ∈ S, degreeExcess12 G v) ≤ 8 := by
  have h : (∑ v ∈ S, degreeExcess12 G v) ≤ ∑ v : V, degreeExcess12 G v :=
    Finset.sum_le_sum_of_subset (Finset.subset_univ S)
  simpa only [e286_excess_sum G hG] using h

end EG617
