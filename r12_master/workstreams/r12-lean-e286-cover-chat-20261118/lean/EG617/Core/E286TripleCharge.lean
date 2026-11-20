module
public import EG617.Core.E286Triple

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem e286_missing_card_le_ten (G : SimpleGraph V) (K : Finset V)
    (hc : K.card = 11) (z t : V) (ht : t ∈ K) (hzt : G.Adj z t) :
    (K.filter (fun v => ¬ G.Adj z v)).card ≤ 10 := by
  classical
  have hs : K.filter (fun v => ¬ G.Adj z v) ⊆ K.erase t := by
    intro v hv
    obtain ⟨hvK, hnv⟩ := Finset.mem_filter.mp hv
    refine Finset.mem_erase.mpr ⟨?_, hvK⟩
    intro he
    subst v
    exact hnv hzt
  have h := Finset.card_le_card hs
  rw [Finset.card_erase_of_mem ht, hc] at h
  exact h

/-- Frozen Section4 without an ordering assumption: every ordering is covered
by choosing a smallest missing set. The local excess bound is the conclusion,
not a premise supplied to a parent theorem. -/
theorem e286_three_k11_local_charge (G : SimpleGraph V) (hG : E286Hypotheses G)
    (K L M : Finset V) (hK : G.IsClique (K : Set V))
    (hL : G.IsClique (L : Set V)) (hM : G.IsClique (M : Set V))
    (hcK : K.card = 11) (hcL : L.card = 11) (hcM : M.card = 11)
    (hKL : Disjoint K L) (hKM : Disjoint K M) (hLM : Disjoint L M)
    (z s : V) (hzs : z ≠ s) (hnzs : ¬ G.Adj z s)
    (hzK : z ∉ K) (hzL : z ∉ L) (hzM : z ∉ M)
    (hsK : s ∉ K) (hsL : s ∉ L) (hsM : s ∉ M)
    (hanti : ∀ v ∈ K ∪ L ∪ M, ¬ G.Adj v s)
    (hadjK : ∃ t ∈ K, G.Adj z t) (hadjL : ∃ t ∈ L, G.Adj z t)
    (hadjM : ∃ t ∈ M, G.Adj z t) :
    3 ≤ ∑ v ∈ insert z (K ∪ L ∪ M), degreeExcess12 G v := by
  classical
  by_contra hn
  have hsmall : (∑ v ∈ insert z (K ∪ L ∪ M), degreeExcess12 G v) ≤ 2 := by omega
  have hp (v : V) (hv : v ∈ insert z (K ∪ L ∪ M)) : degreeExcess12 G v ≤ 2 := by
    have h : degreeExcess12 G v ≤ ∑ w ∈ insert z (K ∪ L ∪ M), degreeExcess12 G w :=
      Finset.single_le_sum (fun _ _ => Nat.zero_le _) hv
    omega
  have hz2 := hp z (Finset.mem_insert_self _ _)
  have hbound : ∀ v ∈ K ∪ L ∪ M, degreeExcess12 G v ≤ 2 :=
    fun v hv => hp v (Finset.mem_insert_of_mem hv)
  let A := K.filter (fun v => ¬ G.Adj z v)
  let B := L.filter (fun v => ¬ G.Adj z v)
  let C := M.filter (fun v => ¬ G.Adj z v)
  obtain ⟨a, ha, hza⟩ := hadjK
  obtain ⟨b, hb, hzb⟩ := hadjL
  obtain ⟨c, hc, hzc⟩ := hadjM
  have ha10 := e286_missing_card_le_ten G K hcK z a ha hza
  have hb10 := e286_missing_card_le_ten G L hcL z b hb hzb
  have hc10 := e286_missing_card_le_ten G M hcM z c hc hzc
  change A.card ≤ 10 at ha10
  change B.card ≤ 10 at hb10
  change C.card ≤ 10 at hc10
  have hAB : Disjoint A B := hKL.mono (Finset.filter_subset _ _) (Finset.filter_subset _ _)
  have ht := e286_pair_point_degree_charge G (K ∪ L) M
    (Finset.disjoint_union_left.mpr ⟨hKM, hLM⟩) z
  rw [Finset.card_union_of_disjoint hKL, hcK, hcL, hcM, Finset.filter_union,
    Finset.card_union_of_disjoint hAB] at ht
  change 11 + 11 + 11 ≤ 12 + degreeExcess12 G z + (A.card + B.card) + C.card at ht
  have htotal : 19 ≤ A.card + B.card + C.card := by omega
  have haPos := e286_eleven_clique_missing_nonempty G hG K hcK hK z hzK
  have hbPos := e286_eleven_clique_missing_nonempty G hG L hcL hL z hzL
  have hcPos := e286_eleven_clique_missing_nonempty G hG M hcM hM z hzM
  have hpermB : L ∪ K ∪ M = K ∪ L ∪ M := by rw [Finset.union_comm L K]
  have hpermC : M ∪ K ∪ L = K ∪ L ∪ M := by
    rw [Finset.union_assoc, Finset.union_comm M (K ∪ L)]
  have hcaseC (hca : C.card ≤ A.card) (hcb : C.card ≤ B.card) : False := by
    apply e286_ordered_three_cliques_obstruction G hG M K L hM hK hL hcM hcK hcL
      hKM.symm hLM.symm hKL z s hzs hnzs hzM hzK hzL hsM hsK hsL
      (by rw [hpermC]; exact hanti) (by rw [hpermC]; exact hbound) hcPos
    · change 5 ≤ A.card
      omega
    · change 5 ≤ B.card
      omega
    · change 13 ≤ A.card + B.card
      omega
  by_cases hab : A.card ≤ B.card
  · by_cases hac : A.card ≤ C.card
    · apply e286_ordered_three_cliques_obstruction G hG K L M hK hL hM hcK hcL hcM
        hKL hKM hLM z s hzs hnzs hzK hzL hzM hsK hsL hsM hanti hbound haPos
      · change 5 ≤ B.card
        omega
      · change 5 ≤ C.card
        omega
      · change 13 ≤ B.card + C.card
        omega
    · exact hcaseC (by omega) (by omega)
  · by_cases hbc : B.card ≤ C.card
    · apply e286_ordered_three_cliques_obstruction G hG L K M hL hK hM hcL hcK hcM
        hKL.symm hLM hKM z s hzs hnzs hzL hzK hzM hsL hsK hsM
        (by rw [hpermB]; exact hanti) (by rw [hpermB]; exact hbound) hbPos
      · change 5 ≤ A.card
        omega
      · change 5 ≤ C.card
        omega
      · change 13 ≤ A.card + C.card
        omega
    · exact hcaseC (by omega) (by omega)

end EG617
