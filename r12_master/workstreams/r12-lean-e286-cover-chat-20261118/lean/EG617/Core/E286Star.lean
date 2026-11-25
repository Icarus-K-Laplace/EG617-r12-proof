module
public import EG617.Core.E286LowBudget

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- At x an incident pair point provides its own singleton neighbor when
adjacent and the opposite missing set otherwise. Distinct lanes lie in
disjoint exterior regions. -/
theorem e286_center_lane_bound {ι : Type*} [Fintype ι] (G : SimpleGraph V) (K : Finset V)
    (cl : G.IsClique (K : Set V)) (p : ι → V) (B : ι → Finset V)
    (outside : ∀ i, Disjoint K (insert (p i) (B i)))
    (sep : ∀ i j, i ≠ j → Disjoint (insert (p i) (B i)) (insert (p j) (B j)))
    (force : ∀ i x, x ∈ e286Missing G K (p i) → ∀ y ∈ B i, G.Adj x y)
    (x : V) (hx : x ∈ K) :
    K.card + (∑ i, if G.Adj (p i) x then 1 else (B i).card) ≤ 13 + degreeExcess12 G x := by
  classical
  let lane (i : ι) : Finset V := if G.Adj (p i) x then {p i} else B i
  have sub (i : ι) : lane i ⊆ insert (p i) (B i) := by
    unfold lane
    split
    · exact Finset.singleton_subset_iff.mpr (Finset.mem_insert_self _ _)
    · exact Finset.subset_insert _ _
  have ds : ((Finset.univ : Finset ι) : Set ι).PairwiseDisjoint lane :=
    fun i _ j _ hij => (sep i j hij).mono (sub i) (sub j)
  have hd : Disjoint K (Finset.univ.biUnion lane) := by
    rw [Finset.disjoint_left]
    intro v hv hm
    obtain ⟨i,_,hl⟩ := Finset.mem_biUnion.mp hm
    exact Finset.disjoint_left.mp (outside i) hv (sub i hl)
  have h := e286_clique_blocker_vertex_charge G K (Finset.univ.biUnion lane) cl hd x hx (by
    intro y hy
    obtain ⟨i,_,hl⟩ := Finset.mem_biUnion.mp hy
    by_cases adj : G.Adj (p i) x
    · have eq : y = p i := by simpa [lane,adj] using hl
      exact eq.symm ▸ adj.symm
    · exact force i x (Finset.mem_filter.mpr ⟨hx,adj⟩) y (by simpa [lane,adj] using hl))
  rw [Finset.card_biUnion ds] at h
  have cards (i : ι) : (lane i).card = if G.Adj (p i) x then 1 else (B i).card := by
    by_cases h : G.Adj (p i) x <;> simp [lane,h]
  simpa only [cards] using h

theorem e286_star_scalar (a b : ℕ) (ha : 0 < a) (hb : 0 < b) (h1 : a ≤ 10) (h2 : b ≤ 11) :
    6 ≤ (9-a-b) + a*(b-1) + b*(a-2) := by
  interval_cases a <;> interval_cases b <;> norm_num

/-- Frozen Section 6, star geometry. The three pair points and three leaves
are specified on the actual graph. Charges at their shared center sum over
one set of vertices. -/
theorem e286_three_leaf_star_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (K : Finset V) (L : Fin 3 → Finset V) (p : Fin 3 → V)
    (hk : K.card = 10) (hl : ∀ i, (L i).card = 11) (cl : G.IsClique (K : Set V))
    (cls : ∀ i, G.IsClique ((L i : Finset V) : Set V))
    (pinj : Function.Injective p) (kp : ∀ i, p i ∉ K) (lp : ∀ i j, p i ∉ L j)
    (kl : ∀ i, Disjoint K (L i)) (ll : ∀ i j, i ≠ j → Disjoint (L i) (L j))
    (force : ∀ i x, x ∈ e286Missing G K (p i) → ∀ y ∈ e286Missing G (L i) (p i), G.Adj x y) : False := by
  classical
  let A (i : Fin 3) := e286Missing G K (p i)
  let B (i : Fin 3) := e286Missing G (L i) (p i)
  let R (i : Fin 3) := insert (p i) (L i)
  have sa (i : Fin 3) : A i ⊆ K := Finset.filter_subset _ _
  have sb (i : Fin 3) : B i ⊆ L i := Finset.filter_subset _ _
  have sub (i : Fin 3) : insert (p i) (B i) ⊆ R i := Finset.insert_subset_insert _ (sb i)
  have sep (i j : Fin 3) (h : i ≠ j) : Disjoint (R i) (R j) := by
    apply Finset.disjoint_insert_left.mpr
    exact ⟨fun hm => (Finset.mem_insert.mp hm).elim (fun he => h (pinj he)) (lp i j),
      Finset.disjoint_insert_right.mpr ⟨lp j i,ll i j h⟩⟩
  have out (i : Fin 3) : Disjoint K (R i) := Finset.disjoint_insert_right.mpr ⟨kp i,kl i⟩
  have bp (i : Fin 3) : 0 < (B i).card := Finset.card_pos.mpr
    (e286_eleven_clique_missing_nonempty G hG _ (hl i) (cls i) (p i) (lp i i))
  let weight (x : V) (i : Fin 3) := if x ∈ A i then (B i).card - 1 else 0
  have one (x : V) (hx : x ∈ K) (i : Fin 3) :
      (if G.Adj (p i) x then 1 else (B i).card) = weight x i + 1 := by
    by_cases h : G.Adj (p i) x
    · simp [weight,A,e286Missing,h]
    · have hm : x ∈ A i := Finset.mem_filter.mpr ⟨hx,h⟩
      simp only [if_neg h,weight,if_pos hm]
      have hp := bp i
      omega
  have pointwise (x : V) (hx : x ∈ K) : (∑ i, weight x i) ≤ degreeExcess12 G x := by
    have h := e286_center_lane_bound G K cl p B (fun i => (out i).mono_right (sub i))
      (fun i j hij => (sep i j hij).mono (sub i) (sub j)) force x hx
    simp only [one x hx,Finset.sum_add_distrib,hk] at h
    norm_num at h
    omega
  have column (i : Fin 3) : (∑ x ∈ K, weight x i) = (A i).card * ((B i).card-1) := by
    unfold weight
    rw [← Finset.sum_filter]
    have he : K.filter (fun x => x ∈ A i) = A i := by
      ext x
      simp only [Finset.mem_filter]
      exact ⟨And.right,fun hx => ⟨sa i hx,hx⟩⟩
    simp [he]
  have center := Finset.sum_le_sum pointwise
  rw [Finset.sum_comm] at center
  simp only [column] at center
  let cost (i : Fin 3) := (∑ x ∈ R i, degreeExcess12 G x) + (A i).card*((B i).card-1)
  have total : (∑ i, cost i) ≤ 8 := by
    have d : Disjoint K (Finset.univ.biUnion R) := by
      rw [Finset.disjoint_left]
      intro x hx hm
      obtain ⟨i,_,hi⟩ := Finset.mem_biUnion.mp hm
      exact Finset.disjoint_left.mp (out i) hx hi
    have eight := e286_subset_excess_budget G hG (K ∪ Finset.univ.biUnion R)
    rw [Finset.sum_union d,Finset.sum_biUnion (fun i _ j _ hij => sep i j hij)] at eight
    simp only [cost,Finset.sum_add_distrib]
    omega
  have noncomplete (i : Fin 3) (h : ¬ ∀ x ∈ K, G.Adj (p i) x) : 6 ≤ cost i := by
    have h6 := e286_star_scalar (A i).card (B i).card
      (Finset.card_pos.mpr (e286_missing_of_incomplete G K (p i) h)) (bp i)
      ((Finset.card_le_card (sa i)).trans hk.le) ((Finset.card_le_card (sb i)).trans (hl i).le)
    have hpt := e286_pair_point_degree_charge G K (L i) (kl i) (p i)
    change K.card + (L i).card ≤ 12 + degreeExcess12 G (p i) + (A i).card + (B i).card at hpt
    rw [hk,hl i] at hpt
    have each (x : V) (hx : x ∈ B i) : (A i).card-2 ≤ degreeExcess12 G x := by
      have h := e286_clique_blocker_vertex_charge G (L i) (A i) (cls i) ((kl i).symm.mono_right (sa i))
        x (sb i hx) (fun y hy => (force i y hy x hx).symm)
      rw [hl i] at h
      omega
    have hs := Finset.sum_le_sum each
    simp only [Finset.sum_const,smul_eq_mul] at hs
    have incl : (∑ x ∈ B i, degreeExcess12 G x) ≤ ∑ x ∈ L i, degreeExcess12 G x :=
      Finset.sum_le_sum_of_subset (sb i)
    simp only [cost,R,Finset.sum_insert (lp i i)]
    omega
  have charged (i : Fin 3) : degreeExcess12 G (p i) ≤ cost i := by
    simp only [cost,R,Finset.sum_insert (lp i i)]
    omega
  have pair (i j : Fin 3) (ij : i ≠ j) (ci : ∀ x ∈ K, G.Adj (p i) x)
      (cj : ∀ x ∈ K, G.Adj (p j) x) : 7 ≤ cost i + cost j := by
    have h := (e286_ten_clique_completers_excess G hG K hk cl _ _ (fun e => ij (pinj e))
      (kp i) (kp j) (fun x hx => ⟨ci x hx,cj x hx⟩)).2
    exact h.trans (Nat.add_le_add (charged i) (charged j))
  have sum3 : cost 0 + cost 1 + cost 2 ≤ 8 := by
    simpa [Fin.sum_univ_succ, Nat.add_assoc] using total
  by_cases c0 : ∀ x ∈ K, G.Adj (p 0) x <;>
    by_cases c1 : ∀ x ∈ K, G.Adj (p 1) x <;>
    by_cases c2 : ∀ x ∈ K, G.Adj (p 2) x
  all_goals
    try have h0 := noncomplete 0 c0
    try have h1 := noncomplete 1 c1
    try have h2 := noncomplete 2 c2
    try have h01 := pair 0 1 (by decide) c0 c1
    try have h12 := pair 1 2 (by decide) c1 c2
    try have h02 := pair 0 2 (by decide) c0 c2
    omega

theorem e286_h4_star_orbit_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hi : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V))
    (counts : e286GraphSupportCounts G I e = [1,1,1,0,0,0,0,0,0,1,0]) : False := by
  classical
  let K := fun i : Fin 4 => seedPrivateClique G I (e i)
  have row (s : Fin 4) : e286CountIncidence (e286GraphSupportCounts G I e) s = if s = 0 then 3 else 2 := by
    rw [counts]
    fin_cases s <;> norm_num [e286CountIncidence,Fin.sum_univ_succ,e286SupportType]
  have sizes (s : Fin 4) : (K s).card = if s = 0 then 10 else 11 := by
    have hr := row s
    rw [e286_graph_support_incidence] at hr
    have h := e286_private_multiple_card G I hi _ (e s).property (hd _ (e s).property)
    dsimp only [K]
    split at hr <;> split <;> omega
  have cl (i : Fin 4) : G.IsClique ((K i : Finset V) : Set V) := e286_private_class_isClique G hG I hc hi _ (e i).property
  have ne (i j : Fin 4) (h : i ≠ j) : (e i : V) ≠ e j := fun he => h (e.injective (Subtype.ext he))
  have sep (i j : Fin 4) (h : i ≠ j) : Disjoint (K i) (K j) :=
    seed_private_classes_disjoint G I hi _ _ (e i).property (e j).property (ne i j h)
  have wit (i : Fin 3) : ∃ z, seedNeighbors G I z = {(e 0 : V),(e i.succ : V)} := by
    let t : Fin 11 := ⟨i.val, by omega⟩
    obtain ⟨v,hv⟩ := e286_positive_count_actual_witness G I e t (by
      rw [counts]
      dsimp only [t]
      fin_cases i <;> decide)
    refine ⟨v,?_⟩
    have ht : e286SupportType t = {0,i.succ} := by
      dsimp only [t]
      fin_cases i <;> decide
    rw [ht] at hv
    simpa using hv
  choose p hp using wit
  have pinj : Function.Injective p := by
    intro i j hij
    have hm : (e i.succ : V) ∈ seedNeighbors G I (p i) := by rw [hp]; simp
    rw [hij,hp] at hm
    rcases Finset.mem_insert.mp hm with h | h
    · exact ((ne _ _ (Fin.succ_ne_zero i)) h).elim
    · exact Fin.succ_inj.mp (e.injective (Subtype.ext (Finset.mem_singleton.mp h)))
  have out (i : Fin 3) (s : Fin 4) : p i ∉ K s := by
    intro hm
    exact Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hi _ (e s).property) hm
      (e286_pair_support_mem_multiple G I _ _ (p i) (ne _ _ (Fin.succ_ne_zero i).symm) (hp i))
  exact e286_three_leaf_star_impossible G hG (K 0) (fun i => K i.succ) p
    (by simpa using sizes 0) (fun i => by simpa [Fin.succ_ne_zero] using sizes i.succ) (cl 0)
    (fun i => cl i.succ) pinj (fun i => out i 0) (fun i j => out i j.succ)
    (fun i => sep _ _ (Fin.succ_ne_zero i).symm)
    (fun i j h => sep _ _ (fun he => h (Fin.succ_inj.mp he)))
    (fun i => e286_actual_pair_edges G hG I hc hi _ _ (p i) (e 0).property
      (e i.succ).property (ne _ _ (Fin.succ_ne_zero i).symm) (hp i))

theorem e286_actual_support_D_or_C (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e = [1,1,1,1,1,0,0,0,0,0,0] ∨
        e286GraphSupportCounts G I e = [3,0,0,0,0,2,0,0,0,0,0] := by
  obtain ⟨I,hc,hi,hd,e,he⟩ := e286_actual_support_star_D_C G hG
  refine ⟨I,hc,hi,hd,e,?_⟩
  change e286GraphSupportCounts G I e ∈ [_,_,_] at he
  simp only [List.mem_cons,List.not_mem_nil,or_false] at he
  rcases he with h | h | h
  · exact (e286_h4_star_orbit_impossible G hG I hc hi hd e h).elim
  · exact Or.inl h
  · exact Or.inr h

end EG617
