module
public import EG617.Core.E286OrbitP

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem e286_one_completer_scalar_three (s a b : ℕ) (hs : s = 9 ∨ s = 10)
    (ha : 0 < a) (hb : 0 < b) (has : a ≤ s) (hbl : b ≤ 11) :
    3 ≤ s+11-12-a-b + a*(s+b+1-13) + b*(a-2) := by
  rcases hs with rfl | rfl <;> interval_cases a <;> interval_cases b <;> norm_num

/-- With one exterior completer a non-completing 9/11 or 10/11 pair charges
at least three, with its shared-leaf term left in scalar form. -/
theorem e286_one_completer_mixed_split (G : SimpleGraph V) (K L : Finset V) (z p : V)
    (hk : K.card = 9 ∨ K.card = 10) (hl : L.card = 11) (cl : G.IsClique (K : Set V))
    (dis : Disjoint K L) (pk : p ∉ K) (pl : p ∉ L) (comp : ∀ x ∈ K, G.Adj p x)
    (ha : (e286Missing G K z).Nonempty) (hb : (e286Missing G L z).Nonempty)
    (edge : ∀ x ∈ e286Missing G K z, ∀ y ∈ e286Missing G L z, G.Adj x y) :
    3 ≤ degreeExcess12 G z + (∑ x ∈ e286Missing G K z, degreeExcess12 G x) +
      (e286Missing G L z).card * ((e286Missing G K z).card-2) := by
  classical
  let A := e286Missing G K z
  let B := e286Missing G L z
  have sa : A ⊆ K := Finset.filter_subset _ _
  have sb : B ⊆ L := Finset.filter_subset _ _
  have bound := e286_one_completer_scalar_three K.card A.card B.card hk
    (Finset.card_pos.mpr ha) (Finset.card_pos.mpr hb) (Finset.card_le_card sa)
    ((Finset.card_le_card sb).trans hl.le)
  have each (x : V) (hx : x ∈ A) : K.card+B.card+1-13 ≤ degreeExcess12 G x := by
    have h := e286_clique_charge_with_extra G K B cl (dis.mono_right sb) p x pk
      (fun h => pl (sb h)) (sa hx) (comp x (sa hx)).symm (edge x hx)
    omega
  have hs := Finset.sum_le_sum each
  simp only [Finset.sum_const, smul_eq_mul] at hs
  have hp := e286_pair_point_degree_charge G K L dis z
  change K.card + L.card ≤ 12 + degreeExcess12 G z + A.card + B.card at hp
  rw [hl] at hp
  change 3 ≤ degreeExcess12 G z + (∑ x ∈ A, degreeExcess12 G x) + B.card*(A.card-2)
  omega

/-- A disjoint K11/K11 pair costs six. Sharing its leaf leaves too little
budget for a second mixed non-completer, even with a nine-clique as center. -/
theorem e286_shared_leaf_forces_completion (G : SimpleGraph V) (hG : E286Hypotheses G)
    (K : Fin 4 → Finset V) (sizeX : (K 0).card = 9 ∨ (K 0).card = 10)
    (kL : (K 2).card = 11) (kY : (K 3).card = 11) (cl : ∀ i, G.IsClique ((K i : Finset V) : Set V))
    (sep : ∀ i j, i ≠ j → Disjoint (K i) (K j)) (p r q : V) (rq : r ≠ q)
    (outP : ∀ i, p ∉ K i) (outR : ∀ i, r ∉ K i) (outQ : ∀ i, q ∉ K i)
    (complete : ∀ x ∈ K 0, G.Adj p x)
    (edgeAB : ∀ x ∈ e286Missing G (K 0) r, ∀ y ∈ e286Missing G (K 2) r, G.Adj x y)
    (edgeCD : ∀ x ∈ e286Missing G (K 3) q, ∀ y ∈ e286Missing G (K 2) q, G.Adj x y) :
    ∀ x ∈ K 0, G.Adj r x := by
  classical
  let A := e286Missing G (K 0) r
  let B := e286Missing G (K 2) r
  let C := e286Missing G (K 3) q
  let D := e286Missing G (K 2) q
  by_cases ha : A.Nonempty
  · exfalso
    have sa : A ⊆ K 0 := Finset.filter_subset _ _
    have sb : B ⊆ K 2 := Finset.filter_subset _ _
    have sc : C ⊆ K 3 := Finset.filter_subset _ _
    have sd : D ⊆ K 2 := Finset.filter_subset _ _
    have hb : B.Nonempty := e286_eleven_clique_missing_nonempty G hG _ kL (cl 2) r (outR 2)
    have hc' : C.Nonempty := e286_eleven_clique_missing_nonempty G hG _ kY (cl 3) q (outQ 3)
    have hd' : D.Nonempty := e286_eleven_clique_missing_nonempty G hG _ kL (cl 2) q (outQ 2)
    have three : 3 ≤ degreeExcess12 G r + (∑ x ∈ A, degreeExcess12 G x) + B.card * (A.card - 2) :=
      e286_one_completer_mixed_split G (K 0) (K 2) r p sizeX kL (cl 0) (sep 0 2 (by decide))
        (outP 0) (outP 2) complete ha hb edgeAB
    have six : 6 ≤ degreeExcess12 G q + (∑ x ∈ C, degreeExcess12 G x) + D.card * (C.card - 2) := by
      apply e286_split_pair_charge G (K 3) (K 2) q (sep 3 2 (by decide)) 11 11 6
        kY kL
      · exact e286_f11_minimum C.card D.card (Finset.card_pos.mpr hc') (Finset.card_pos.mpr hd')
          (le_trans (Finset.card_le_card sc) kY.le)
          (le_trans (Finset.card_le_card sd) kL.le)
      · intro x hx
        have h := e286_clique_blocker_vertex_charge G (K 3) D (cl 3)
          ((sep 3 2 (by decide)).mono_right sd) x (sc hx) (edgeCD x hx)
        rw [kY] at h
        change D.card - 2 ≤ degreeExcess12 G x
        omega
    have leaf : B.card * (A.card - 2) + D.card * (C.card - 2) ≤
        ∑ x ∈ B ∪ D, degreeExcess12 G x :=
      e286_shared_leaf_pair_charge G (K 2) A C r q kL (cl 2)
        ((sep 2 0 (by decide)).mono_right sa) ((sep 2 3 (by decide)).mono_right sc)
        ((sep 0 3 (by decide)).mono sa sc) (outR 2) (outQ 2)
        (fun hm => outR 3 (sc hm)) (fun hm => outQ 0 (sa hm))
        (fun y hy x hx => (edgeAB x hx y hy).symm) (fun y hy x hx => (edgeCD x hx y hy).symm)
    have su : B ∪ D ⊆ K 2 := Finset.union_subset sb sd
    have haC := (sep 0 3 (by decide)).mono sa sc
    have dis : Disjoint (A ∪ C) (B ∪ D) := Finset.disjoint_union_left.mpr
      ⟨(sep 0 2 (by decide)).mono sa su, (sep 3 2 (by decide)).mono sc su⟩
    have extOut (v : V) (hv : ∀ i : Fin 4, v ∉ K i) : v ∉ (A ∪ C) ∪ (B ∪ D) := by
      intro hm
      rcases Finset.mem_union.mp hm with h | h
      · exact (Finset.mem_union.mp h).elim (fun h => hv 0 (sa h)) (fun h => hv 3 (sc h))
      · exact hv 2 (su h)
    have qOut := extOut q outQ
    have rOut : r ∉ insert q ((A ∪ C) ∪ (B ∪ D)) := by
      intro hm
      exact (Finset.mem_insert.mp hm).elim rq (extOut r outR)
    have budget := e286_subset_excess_budget G hG (insert r (insert q ((A ∪ C) ∪ (B ∪ D))))
    rw [Finset.sum_insert rOut, Finset.sum_insert qOut, Finset.sum_union dis, Finset.sum_union haC] at budget
    omega
  · intro x hx
    by_contra hn
    exact ha ⟨x, Finset.mem_filter.mpr ⟨hx,hn⟩⟩

/-- Frozen Sections 8 and 10 share the same four actual pair points.
In the nine-clique case an extra adjacent completer enlarges the clique to ten. -/
theorem e286_h5_nine_or_B_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hi : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V))
    (profiles : e286GraphSupportCounts G I e = [2,1,1,0,0,1,0,0,0,0,0] ∨
      e286GraphSupportCounts G I e = [2,1,0,0,1,1,0,0,0,0,0]) : False := by
  classical
  let K := fun i : Fin 4 => seedPrivateClique G I (e i)
  have rowSize (s : Fin 4) (n : ℕ) (h : e286CountIncidence (e286GraphSupportCounts G I e) s = n) :
      (K s).card = 13-n := by
    rw [e286_graph_support_incidence] at h
    have hr := e286_private_multiple_card G I hi _ (e s).property (hd _ (e s).property)
    dsimp only [K]
    omega
  have sizes : ((K 0).card = 9 ∧ (K 1).card = 11 ∨ (K 0).card = 10 ∧ (K 1).card = 10) ∧
      (K 2).card = 11 ∧ (K 3).card = 11 := by
    rcases profiles with h | h
    · refine ⟨Or.inl ⟨rowSize 0 4 ?_,rowSize 1 2 ?_⟩,rowSize 2 2 ?_,rowSize 3 2 ?_⟩ <;>
        rw [h] <;> norm_num [e286CountIncidence, Fin.sum_univ_succ, e286SupportType]
    · refine ⟨Or.inr ⟨rowSize 0 3 ?_,rowSize 1 3 ?_⟩,rowSize 2 2 ?_,rowSize 3 2 ?_⟩ <;>
        rw [h] <;> norm_num [e286CountIncidence, Fin.sum_univ_succ, e286SupportType]
  obtain ⟨shape,k2,k3⟩ := sizes
  have threshold : E286PairThreshold (K 0).card (K 1).card 2 := by
    rcases shape with ⟨x,y⟩ | ⟨x,y⟩
    · exact Or.inl ⟨x,y,rfl⟩
    · exact Or.inr (Or.inl ⟨x,y,rfl⟩)
  obtain ⟨p,w,pw,hp',hw'⟩ := e286_double_count_actual_witnesses G I e 0
    (by rcases profiles with h | h <;> rw [h] <;> norm_num)
  obtain ⟨r,hr'⟩ := e286_positive_count_actual_witness G I e 1
    (by rcases profiles with h | h <;> rw [h] <;> norm_num)
  obtain ⟨q,hq'⟩ := e286_positive_count_actual_witness G I e 5
    (by rcases profiles with h | h <;> rw [h] <;> norm_num)
  have hp : seedNeighbors G I p = {(e 0 : V),(e 1 : V)} := by simpa [e286SupportType] using hp'
  have hw : seedNeighbors G I w = {(e 0 : V),(e 1 : V)} := by simpa [e286SupportType] using hw'
  have hr : seedNeighbors G I r = {(e 0 : V),(e 2 : V)} := by simpa [e286SupportType] using hr'
  have hq : seedNeighbors G I q = {(e 2 : V),(e 3 : V)} := by simpa [e286SupportType] using hq'
  have ne (i j : Fin 4) (h : i ≠ j) : (e i : V) ≠ e j := fun he => h (e.injective (Subtype.ext he))
  have cl (i : Fin 4) : G.IsClique ((K i : Finset V) : Set V) := e286_private_class_isClique G hG I hc hi _ (e i).property
  have sep (i j : Fin 4) (h : i ≠ j) : Disjoint (K i) (K j) :=
    seed_private_classes_disjoint G I hi _ _ (e i).property (e j).property (ne i j h)
  have out (i j : Fin 4) (ij : i ≠ j) (z : V) (hz : seedNeighbors G I z = {(e i : V),(e j : V)})
      (s : Fin 4) : z ∉ K s := by
    intro hm
    exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hi _ (e s).property) hm
      (e286_pair_support_mem_multiple G I _ _ z (ne i j ij) hz)
  have op := out 0 1 (by decide) p hp
  have ow := out 0 1 (by decide) w hw
  have or' := out 0 2 (by decide) r hr
  have oq := out 2 3 (by decide) q hq
  have diff (u v a b c d : V) (hu : seedNeighbors G I u = {a,b})
      (hv : seedNeighbors G I v = {c,d}) (ac : a ≠ c) (ad : a ≠ d) : u ≠ v := by
    intro he
    have hm : a ∈ seedNeighbors G I u := by rw [hu]; simp
    rw [he,hv] at hm
    simpa [ac,ad] using hm
  have pq := diff p q _ _ _ _ hp hq (ne 0 2 (by decide)) (ne 0 3 (by decide))
  have wq := diff w q _ _ _ _ hw hq (ne 0 2 (by decide)) (ne 0 3 (by decide))
  have rq := diff r q _ _ _ _ hr hq (ne 0 2 (by decide)) (ne 0 3 (by decide))
  have pr := diff p r _ _ _ _ (hp.trans (Finset.pair_comm _ _)) hr (ne 1 0 (by decide)) (ne 1 2 (by decide))
  have wr := diff w r _ _ _ _ (hw.trans (Finset.pair_comm _ _)) hr (ne 1 0 (by decide)) (ne 1 2 (by decide))
  let Q := insert q (K 2 ∪ K 3)
  have q6 : 6 ≤ ∑ v ∈ Q, degreeExcess12 G v := e286_private_k11_pair_charge G hG I hc hi _ _ q
    (e 2).property (e 3).property (ne 2 3 (by decide)) hq k2 k3
  have small (S : Finset V) (hs : Disjoint S Q) : (∑ x ∈ S, degreeExcess12 G x) ≤ 2 := by
    have h := e286_subset_excess_budget G hG (S ∪ Q)
    rw [Finset.sum_union hs] at h
    omega
  have pQ : p ∉ Q := by simp [Q,pq,op]
  have wQ : w ∉ Q := by simp [Q,wq,ow]
  have rQ : r ∉ Q := by simp [Q,rq,or']
  have sepU : Disjoint (K 0 ∪ K 1) Q := by
    apply Finset.disjoint_insert_right.mpr
    refine ⟨by simp [oq],?_⟩
    rw [Finset.disjoint_union_left, Finset.disjoint_union_right, Finset.disjoint_union_right]
    exact ⟨⟨sep 0 2 (by decide),sep 0 3 (by decide)⟩,⟨sep 1 2 (by decide),sep 1 3 (by decide)⟩⟩
  have pairBudget (u v : V) (uv : u ≠ v) (uQ : u ∉ Q) (vQ : v ∉ Q) :
      degreeExcess12 G u + degreeExcess12 G v ≤ 2 := by
    have h := small ({u,v} : Finset V) (Finset.disjoint_insert_left.mpr
      ⟨uQ, Finset.disjoint_singleton_left.mpr vQ⟩)
    rwa [Finset.sum_pair uv] at h
  have choiceSide (u v : V) (uv : u ≠ v) (uQ : u ∉ Q) (vQ : v ∉ Q)
      (hu : seedNeighbors G I u = {(e 0 : V),(e 1 : V)})
      (hv : seedNeighbors G I v = {(e 0 : V),(e 1 : V)}) :
      (∀ x ∈ K 0, G.Adj u x) ∨ (∀ x ∈ K 1, G.Adj u x) :=
    e286_doubled_pair_completion G _ _ u v 2 threshold (cl 0) (cl 1) (sep 0 1 (by decide))
      uv (out 0 1 (by decide) u hu 0) (out 0 1 (by decide) u hu 1)
      (out 0 1 (by decide) v hv 0) (out 0 1 (by decide) v hv 1)
      (e286_actual_pair_edges G hG I hc hi _ _ u (e 0).property (e 1).property (ne 0 1 (by decide)) hu)
      (e286_actual_pair_edges G hG I hc hi _ _ v (e 0).property (e 1).property (ne 0 1 (by decide)) hv)
      (small _ (Finset.disjoint_insert_left.mpr ⟨uQ,Finset.disjoint_insert_left.mpr ⟨vQ,sepU⟩⟩))
  have pSide := choiceSide p w pw pQ wQ hp hw
  have wSide := choiceSide w p pw.symm wQ pQ hw hp
  have cr (u : V) (ou : ∀ i, u ∉ K i) (cu : ∀ x ∈ K 0, G.Adj u x) : ∀ x ∈ K 0, G.Adj r x :=
    e286_shared_leaf_forces_completion G hG K (shape.elim (fun h => Or.inl h.1) (fun h => Or.inr h.1))
      k2 k3 cl sep u r q rq ou or' oq cu
      (e286_actual_pair_edges G hG I hc hi _ _ r (e 0).property (e 2).property (ne 0 2 (by decide)) hr)
      (e286_actual_pair_edges G hG I hc hi _ _ q (e 3).property (e 2).property (ne 3 2 (by decide))
        (hq.trans (Finset.pair_comm _ _)))
  have noTen (S : Finset V) (hs : S.card = 10) (hS : G.IsClique (S : Set V))
      (u v : V) (uv : u ≠ v) (us : u ∉ S) (vs : v ∉ S) (uQ : u ∉ Q) (vQ : v ∉ Q)
      (adj : ∀ x ∈ S, G.Adj u x ∧ G.Adj v x) : False := by
    have seven := (e286_ten_clique_completers_excess G hG S hs hS u v uv us vs adj).2
    have two := pairBudget u v uv uQ vQ
    omega
  rcases shape with ⟨k9,k11⟩ | ⟨k0,k1⟩
  · have notOne (u : V) (ou : u ∉ K 1) : ¬ ∀ x ∈ K 1, G.Adj u x := by
      obtain ⟨x,hx⟩ := e286_eleven_clique_missing_nonempty G hG _ k11 (cl 1) u ou
      intro h
      exact (Finset.mem_filter.mp hx).2 (h x (Finset.mem_filter.mp hx).1)
    have cp := pSide.resolve_right (notOne p (op 1))
    have cw := wSide.resolve_right (notOne w (ow 1))
    have rr := cr p op cp
    have adjP (v : V) (pv : p ≠ v) (vQ : v ∉ Q) (cv : ∀ x ∈ K 0, G.Adj v x) : G.Adj p v := by
      by_contra hn
      have h := e286_common_set_excess_charge G hG p v pv hn (K 0) (fun x hx => ⟨cp x hx,cv x hx⟩)
      rw [k9] at h
      have h2 := pairBudget p v pv pQ vQ
      omega
    have apw := adjP w pw wQ cw
    have apr := adjP r pr rQ rr
    have ext : G.IsClique ((insert p (K 0) : Finset V) : Set V) := by
      rw [Finset.coe_insert]
      exact (cl 0).insert (fun x hx _ => cp x hx)
    apply noTen (insert p (K 0)) (by rw [Finset.card_insert_of_notMem (op 0),k9]) ext
      w r wr (by simp [pw.symm,ow]) (by simp [pr.symm,or']) wQ rQ
    intro x hx
    rcases Finset.mem_insert.mp hx with rfl | h
    · exact ⟨apw.symm,apr.symm⟩
    · exact ⟨cw x h,rr x h⟩
  · have deny (u : V) (ur : u ≠ r) (ou : ∀ i, u ∉ K i) (uQ : u ∉ Q)
        (cu : ∀ x ∈ K 0, G.Adj u x) : False :=
      noTen (K 0) k0 (cl 0) u r ur (ou 0) (or' 0) uQ rQ
        (fun x hx => ⟨cu x hx, cr u ou cu x hx⟩)
    have cp := pSide.resolve_left (deny p pr op pQ)
    have cw := wSide.resolve_left (deny w wr ow wQ)
    exact noTen (K 1) k1 (cl 1) p w pw (op 1) (ow 1) pQ wQ (fun x hx => ⟨cp x hx,cw x hx⟩)

/-- Only the h4 star, D and C remain after the doubled-pair and shared-leaf exclusions. -/
def e286StarDC : List (List ℕ) :=
  [e286SupportOrbitRepresentatives[4]!, e286SupportOrbitRepresentatives[7]!, e286SupportOrbitRepresentatives[9]!]

theorem e286_actual_support_star_D_C (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e ∈ e286StarDC := by
  obtain ⟨I,hc,hi,hd,e,he⟩ := e286_actual_support_after_P G hG
  refine ⟨I,hc,hi,hd,e,?_⟩
  change e286GraphSupportCounts G I e ∈ [_,_,_,_,_] at he
  change e286GraphSupportCounts G I e ∈ [_,_,_]
  simp only [List.mem_cons,List.not_mem_nil,or_false] at he ⊢
  rcases he with h | h | h | h | h
  · exact Or.inl h
  · exact (e286_h5_nine_or_B_impossible G hG I hc hi hd e (Or.inl h)).elim
  · exact Or.inr (Or.inl h)
  · exact (e286_h5_nine_or_B_impossible G hG I hc hi hd e (Or.inr h)).elim
  · exact Or.inr (Or.inr h)

end EG617
