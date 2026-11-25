module
public import EG617.Core.E286DoublePair

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem e286_doubled_mixed_charge_five (G : SimpleGraph V) (hG : E286Hypotheses G)
    (K L : Finset V) (p w : V) (hpw : p ≠ w)
    (hk : K.card = 10) (hl : L.card = 11) (hK : G.IsClique (K : Set V))
    (hL : G.IsClique (L : Set V)) (dis : Disjoint K L)
    (pK : p ∉ K) (pL : p ∉ L) (wK : w ∉ K) (wL : w ∉ L)
    (ep : ∀ x ∈ e286Missing G K p, ∀ y ∈ e286Missing G L p, G.Adj x y)
    (ew : ∀ x ∈ e286Missing G K w, ∀ y ∈ e286Missing G L w, G.Adj x y) :
    5 ≤ ∑ x ∈ insert p (insert w (K ∪ L)), degreeExcess12 G x := by
  classical
  by_contra! hn
  have budget : (∑ x ∈ insert p (insert w (K ∪ L)), degreeExcess12 G x) ≤ 4 := by omega
  have reverse : (∑ x ∈ insert w (insert p (K ∪ L)), degreeExcess12 G x) ≤ 4 := by
    rwa [Finset.insert_comm]
  have shape : E286PairThreshold K.card L.card 4 := Or.inr (Or.inr ⟨hk,hl,rfl⟩)
  have onlyK (z : V) (hz : z ∉ L) (h : (∀ x ∈ K, G.Adj z x) ∨ (∀ y ∈ L, G.Adj z y)) :
      ∀ x ∈ K, G.Adj z x := by
    rcases h with h | h
    · exact h
    · obtain ⟨y,hy⟩ := e286_eleven_clique_missing_nonempty G hG L hl hL z hz
      exact ((Finset.mem_filter.mp hy).2 (h y (Finset.mem_filter.mp hy).1)).elim
  have cp := onlyK p pL (e286_doubled_pair_completion G K L p w 4 shape hK hL dis hpw pK pL wK wL ep ew budget)
  have cw := onlyK w wL (e286_doubled_pair_completion G K L w p 4 shape hK hL dis hpw.symm wK wL pK pL ew ep reverse)
  have h7 := (e286_ten_clique_completers_excess G hG K hk hK p w hpw pK wK
    (fun x hx => ⟨cp x hx,cw x hx⟩)).2
  rw [Finset.sum_insert (show p ∉ insert w (K ∪ L) by simp [hpw,pK,pL]),
    Finset.sum_insert (show w ∉ K ∪ L by simp [wK,wL])] at budget
  omega

theorem e286_actual_pair_edges (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hi : G.IsIndepSet (I : Set V))
    (i j z : V) (ii : i ∈ I) (jj : j ∈ I) (ij : i ≠ j) (hz : seedNeighbors G I z = {i,j}) :
    ∀ x ∈ e286Missing G (seedPrivateClique G I i) z,
      ∀ y ∈ e286Missing G (seedPrivateClique G I j) z, G.Adj x y := by
  intro x hx y hy
  exact e286_pair_blocker_complete G hG I hc hi i j z ii jj ij hz x y
    (Finset.mem_filter.mp hx).1 (Finset.mem_filter.mp hy).1
    (Finset.mem_filter.mp hx).2 (Finset.mem_filter.mp hy).2

theorem e286_h5_P_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hi : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V))
    (hcounts : e286GraphSupportCounts G I e = [1,2,0,0,2,0,0,0,0,0,0]) : False := by
  classical
  let K := fun i : Fin 4 => seedPrivateClique G I (e i)
  have sizes (i : Fin 4) : (K i).card = if i.val < 2 then 10 else 11 := by
    have row : e286CountIncidence (e286GraphSupportCounts G I e) i = if i.val < 2 then 3 else 2 := by
      rw [hcounts]
      fin_cases i <;> norm_num [e286CountIncidence, Fin.sum_univ_succ, e286SupportType]
    rw [e286_graph_support_incidence] at row
    have h := e286_private_multiple_card G I hi _ (e i).property (hd _ (e i).property)
    dsimp only [K]
    split at row <;> split <;> omega
  have ne (i j : Fin 4) (h : i ≠ j) : (e i : V) ≠ e j := fun he => h (e.injective (Subtype.ext he))
  have sep (i j : Fin 4) (h : i ≠ j) : Disjoint (K i) (K j) :=
    seed_private_classes_disjoint G I hi _ _ (e i).property (e j).property (ne i j h)
  have cl (i : Fin 4) : G.IsClique ((K i : Finset V) : Set V) :=
    e286_private_class_isClique G hG I hc hi _ (e i).property
  obtain ⟨p,w,pw,hp',hw'⟩ := e286_double_count_actual_witnesses G I e 1 (by rw [hcounts]; norm_num)
  obtain ⟨q,t,qt,hq',ht'⟩ := e286_double_count_actual_witnesses G I e 4 (by rw [hcounts]; norm_num)
  have hp : seedNeighbors G I p = {(e 0 : V), (e 2 : V)} := by simpa [e286SupportType] using hp'
  have hw : seedNeighbors G I w = {(e 0 : V), (e 2 : V)} := by simpa [e286SupportType] using hw'
  have hq : seedNeighbors G I q = {(e 1 : V), (e 3 : V)} := by simpa [e286SupportType] using hq'
  have ht : seedNeighbors G I t = {(e 1 : V), (e 3 : V)} := by simpa [e286SupportType] using ht'
  have outside (i j : Fin 4) (ij : i ≠ j) (v : V)
      (hv : seedNeighbors G I v = {(e i : V), (e j : V)}) (s : Fin 4) : v ∉ K s := by
    intro hm
    exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hi _ (e s).property) hm
      (e286_pair_support_mem_multiple G I _ _ v (ne i j ij) hv)
  have charge (i j : Fin 4) (ij : i ≠ j) (ki : (K i).card = 10) (kj : (K j).card = 11)
      (u v : V) (uv : u ≠ v) (hu : seedNeighbors G I u = {(e i : V),(e j : V)})
      (hv : seedNeighbors G I v = {(e i : V),(e j : V)}) :
      5 ≤ ∑ x ∈ insert u (insert v (K i ∪ K j)), degreeExcess12 G x :=
    e286_doubled_mixed_charge_five G hG _ _ u v uv ki kj (cl i) (cl j) (sep i j ij)
      (outside i j ij u hu i) (outside i j ij u hu j) (outside i j ij v hv i) (outside i j ij v hv j)
      (e286_actual_pair_edges G hG I hc hi _ _ u (e i).property (e j).property (ne i j ij) hu)
      (e286_actual_pair_edges G hG I hc hi _ _ v (e i).property (e j).property (ne i j ij) hv)
  have left := charge 0 2 (by decide) (sizes 0) (sizes 2) p w pw hp hw
  have right := charge 1 3 (by decide) (sizes 1) (sizes 3) q t qt hq ht
  have different (u v : V) (hu : seedNeighbors G I u = {(e 0 : V), (e 2 : V)})
      (hv : seedNeighbors G I v = {(e 1 : V), (e 3 : V)}) : u ≠ v := by
    intro huv
    have hm : (e 0 : V) ∈ seedNeighbors G I u := by rw [hu]; simp
    rw [huv,hv] at hm
    simpa [ne 0 1 (by decide), ne 0 3 (by decide)] using hm
  have disK : Disjoint (K 0 ∪ K 2) (K 1 ∪ K 3) := by
    rw [Finset.disjoint_union_left, Finset.disjoint_union_right, Finset.disjoint_union_right]
    exact ⟨⟨sep 0 1 (by decide),sep 0 3 (by decide)⟩,⟨sep 2 1 (by decide),sep 2 3 (by decide)⟩⟩
  have dis : Disjoint (insert p (insert w (K 0 ∪ K 2))) (insert q (insert t (K 1 ∪ K 3))) := by
    simp only [Finset.disjoint_insert_left, Finset.disjoint_insert_right, Finset.mem_insert, Finset.mem_union]
    have op := outside 0 2 (by decide) p hp
    have ow := outside 0 2 (by decide) w hw
    have oq := outside 1 3 (by decide) q hq
    have ot := outside 1 3 (by decide) t ht
    simp [different p q hp hq,different p t hp ht,different w q hw hq,different w t hw ht,op,ow,oq,ot,disK]
  have eight := e286_subset_excess_budget G hG
    (insert p (insert w (K 0 ∪ K 2)) ∪ insert q (insert t (K 1 ∪ K 3)))
  rw [Finset.sum_union dis] at eight
  omega

/-- Delete P from the six actual representatives, retaining the order in the frozen table. -/
def e286AfterP : List (List ℕ) :=
  (e286SupportOrbitRepresentatives.drop 4).take 2 ++ e286SupportOrbitRepresentatives.drop 7

theorem e286_actual_support_after_P (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e ∈ e286AfterP := by
  obtain ⟨I,hc,hi,hd,e,he⟩ := e286_actual_support_six_remaining G hG
  refine ⟨I,hc,hi,hd,e,?_⟩
  have noP := e286_h5_P_impossible G hG I hc hi hd e
  simp only [e286SupportOrbitRepresentatives, List.tail_cons, List.mem_cons, List.not_mem_nil,
    or_false] at he
  change e286GraphSupportCounts G I e ∈ [_,_,_,_,_] 
  simp only [List.mem_cons, List.not_mem_nil, or_false]
  rcases he with h | h | h | h | h | h
  · exact Or.inl h
  · exact Or.inr (Or.inl h)
  · exact (noP h).elim
  · exact Or.inr (Or.inr (Or.inl h))
  · exact Or.inr (Or.inr (Or.inr (Or.inl h)))
  · exact Or.inr (Or.inr (Or.inr (Or.inr h)))

end EG617
