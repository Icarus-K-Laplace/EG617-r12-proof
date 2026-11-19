module
public import EG617.Core.E286Charges

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem e286_eleven_clique_missing_nonempty (G : SimpleGraph V)
    (hG : E286Hypotheses G) (K : Finset V) (hc : K.card = 11)
    (hK : G.IsClique (K : Set V)) (z : V) (hz : z ∉ K) :
    (K.filter (fun x => ¬ G.Adj z x)).Nonempty := by
  classical
  by_contra hn
  have he := Finset.not_nonempty_iff_eq_empty.mp hn
  have ha (x : V) (hx : x ∈ K) : G.Adj z x := by
    by_contra hnx
    have hm : x ∈ K.filter (fun x => ¬ G.Adj z x) := Finset.mem_filter.mpr ⟨hx, hnx⟩
    rw [he] at hm
    exact Finset.notMem_empty x hm
  have hcl : G.IsClique ((insert z K : Finset V) : Set V) := by
    rw [Finset.coe_insert]
    exact hK.insert (fun x hx _ => ha x hx)
  have hb := hG.2.2.2.2 _ hcl
  rw [Finset.card_insert_of_notMem hz, hc] at hb
  omega

theorem e286_pair_support_mem_multiple (G : SimpleGraph V) (I : Finset V)
    (i j z : V) (hij : i ≠ j) (hz : seedNeighbors G I z = {i, j}) :
    z ∈ seedMultipleSet G I := by
  apply Finset.mem_filter.mpr
  refine ⟨Finset.mem_univ _, ?_⟩
  rw [hz, Finset.card_pair hij]

/-- Frozen Section3, now for actual private K11s with every blocker premise
discharged from alpha4 and omega11. -/
theorem e286_private_k11_pair_charge (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (i j z : V) (hi : i ∈ I) (hj : j ∈ I) (hij : i ≠ j)
    (hz : seedNeighbors G I z = {i, j})
    (hci : (seedPrivateClique G I i).card = 11)
    (hcj : (seedPrivateClique G I j).card = 11) :
    6 ≤ ∑ v ∈ insert z (seedPrivateClique G I i ∪ seedPrivateClique G I j),
      degreeExcess12 G v := by
  classical
  have hzZ := e286_pair_support_mem_multiple G I i j z hij hz
  have hzout (s : V) (hs : s ∈ I) : z ∉ seedPrivateClique G I s := by
    intro hm
    exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hI s hs) hm hzZ
  have hKi := e286_private_class_isClique G hG I hc hI i hi
  have hKj := e286_private_class_isClique G hG I hc hI j hj
  have hb := e286_k11_pair_local_charge G _ _ hKi hKj hci hcj
    (seed_private_classes_disjoint G I hI i j hi hj hij) z (hzout i hi) (hzout j hj)
    (e286_eleven_clique_missing_nonempty G hG _ hci hKi z (hzout i hi))
    (e286_eleven_clique_missing_nonempty G hG _ hcj hKj z (hzout j hj))
    (fun x hx hzx y hy hzy => e286_pair_blocker_complete G hG I hc hI i j z hi hj hij hz x y hx hy hzx hzy)
  apply hb.trans
  apply Finset.sum_le_sum_of_subset
  apply Finset.insert_subset_insert
  exact Finset.union_subset_union (Finset.filter_subset _ _) (Finset.filter_subset _ _)

/-- Frozen Section5, first h3 orbit: the two complementary pair supports on
four private K11s force disjoint charges6+6, exceeding the total excess8.
No claim is made about the other nine support orbits. -/
theorem e286_complementary_k11_pairs_impossible (G : SimpleGraph V)
    (hG : E286Hypotheses G) (I : Finset V) (hc : I.card = 4)
    (hI : G.IsIndepSet (I : Set V)) (e : Fin 4 ≃ (I : Set V))
    (hK : ∀ s : Fin 4, (seedPrivateClique G I (e s)).card = 11)
    (z w : V) (hz : seedNeighbors G I z = {(e 0 : V), (e 1 : V)})
    (hw : seedNeighbors G I w = {(e 2 : V), (e 3 : V)}) : False := by
  classical
  have heinj : Function.Injective (fun s : Fin 4 => (e s : V)) := by
    intro a b hab
    exact e.injective (Subtype.ext hab)
  have hne (a b : Fin 4) (hab : a ≠ b) : (e a : V) ≠ e b := fun h => hab (heinj h)
  have hzZ := e286_pair_support_mem_multiple G I _ _ z (hne 0 1 (by decide)) hz
  have hwZ := e286_pair_support_mem_multiple G I _ _ w (hne 2 3 (by decide)) hw
  have hzw : z ≠ w := by
    intro he
    have hm : (e 0 : V) ∈ seedNeighbors G I z := by rw [hz]; simp
    rw [he, hw] at hm
    have hm' : (e 0 : V) = e 2 ∨ (e 0 : V) = e 3 := by
      simpa only [Finset.mem_insert, Finset.mem_singleton] using hm
    exact hm'.elim (hne 0 2 (by decide)) (hne 0 3 (by decide))
  let A := seedPrivateClique G I (e 0) ∪ seedPrivateClique G I (e 1)
  let B := seedPrivateClique G I (e 2) ∪ seedPrivateClique G I (e 3)
  have hsep (a b : Fin 4) (hab : a ≠ b) :
      Disjoint (seedPrivateClique G I (e a)) (seedPrivateClique G I (e b)) :=
    seed_private_classes_disjoint G I hI _ _ (e a).property (e b).property (hne a b hab)
  have hAB : Disjoint A B := by
    dsimp only [A, B]
    rw [Finset.disjoint_union_left, Finset.disjoint_union_right, Finset.disjoint_union_right]
    exact ⟨⟨hsep 0 2 (by decide), hsep 0 3 (by decide)⟩,
      ⟨hsep 1 2 (by decide), hsep 1 3 (by decide)⟩⟩
  have hout (v : V) (hv : v ∈ seedMultipleSet G I) (s : Fin 4) :
      v ∉ seedPrivateClique G I (e s) := by
    intro hm
    exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hI _ (e s).property) hm hv
  have hzB : z ∉ B := by
    intro hm
    exact (Finset.mem_union.mp hm).elim (hout z hzZ 2) (hout z hzZ 3)
  have hwA : w ∉ A := by
    intro hm
    exact (Finset.mem_union.mp hm).elim (hout w hwZ 0) (hout w hwZ 1)
  have hdis : Disjoint (insert z A) (insert w B) := by
    rw [Finset.disjoint_left]
    intro v hvA hvB
    rcases Finset.mem_insert.mp hvA with he | hvA
    · subst v
      exact (Finset.mem_insert.mp hvB).elim hzw hzB
    · rcases Finset.mem_insert.mp hvB with he | hvB
      · subst v
        exact hwA hvA
      · exact Finset.disjoint_left.mp hAB hvA hvB
  have hz6 := e286_private_k11_pair_charge G hG I hc hI _ _ z
    (e 0).property (e 1).property (hne 0 1 (by decide)) hz (hK 0) (hK 1)
  have hw6 := e286_private_k11_pair_charge G hG I hc hI _ _ w
    (e 2).property (e 3).property (hne 2 3 (by decide)) hw (hK 2) (hK 3)
  have h8 := e286_subset_excess_budget G hG (insert z A ∪ insert w B)
  rw [Finset.sum_union hdis] at h8
  change 6 ≤ ∑ v ∈ insert z A, degreeExcess12 G v at hz6
  change 6 ≤ ∑ v ∈ insert w B, degreeExcess12 G v at hw6
  omega

end EG617
