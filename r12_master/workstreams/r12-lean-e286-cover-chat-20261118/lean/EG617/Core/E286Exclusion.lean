module
public import EG617.Core.E286Diamond

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators
namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- In orbit C the 23 charge leaves only two excess units for all three
01 points. Each completes one of two ten-cliques. Two must complete the same one. -/
theorem e286_h5_C_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hi : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V))
    (counts : e286GraphSupportCounts G I e = [3,0,0,0,0,2,0,0,0,0,0]) : False := by
  classical
  let K := fun i : Fin 4 => seedPrivateClique G I (e i)
  have rowSize (s : Fin 4) (n : ℕ) (h : e286CountIncidence (e286GraphSupportCounts G I e) s = n) :
      (K s).card = 13-n := by
    rw [e286_graph_support_incidence] at h
    have hr := e286_private_multiple_card G I hi _ (e s).property (hd _ (e s).property)
    dsimp only [K]
    omega
  have k0 : (K 0).card = 10 := rowSize 0 3 (by rw [counts]; norm_num [e286CountIncidence,Fin.sum_univ_succ,e286SupportType])
  have k1 : (K 1).card = 10 := rowSize 1 3 (by rw [counts]; norm_num [e286CountIncidence,Fin.sum_univ_succ,e286SupportType])
  have k2 : (K 2).card = 11 := rowSize 2 2 (by rw [counts]; norm_num [e286CountIncidence,Fin.sum_univ_succ,e286SupportType])
  have k3 : (K 3).card = 11 := rowSize 3 2 (by rw [counts]; norm_num [e286CountIncidence,Fin.sum_univ_succ,e286SupportType])
  have threshold : E286PairThreshold (K 0).card (K 1).card 2 := Or.inr (Or.inl ⟨k0,k1,rfl⟩)
  let F := Finset.univ.filter (fun z : (seedMultipleSet G I : Set V) => e286SeedSupportCode G I e z = 0)
  have three : 2 < F.card := by
    have h : 2 < (e286GraphSupportCounts G I e)[(0 : Fin 11).val]! := by rw [counts]; decide
    simpa only [e286GraphSupportCounts,e286_ofFn_get,F] using h
  obtain ⟨p',w',r',pp,ww,rr,pw',pr',wr'⟩ := Finset.two_lt_card_iff.mp three
  let p : V := p'
  let w : V := w'
  let r : V := r'
  have pw : p ≠ w := fun h => pw' (Subtype.ext h)
  have pr : p ≠ r := fun h => pr' (Subtype.ext h)
  have wr : w ≠ r := fun h => wr' (Subtype.ext h)
  have actual (x : (seedMultipleSet G I : Set V)) (hx : x ∈ F) :
      seedNeighbors G I x = {(e 0 : V),(e 1 : V)} := by
    have h := seedLabelNeighbors_image G I e x
    rw [← e286_seed_support_code_spec G I e x, (Finset.mem_filter.mp hx).2] at h
    simpa [e286SupportType] using h.symm
  have hp := actual p' pp
  have hw := actual w' ww
  have hr := actual r' rr
  obtain ⟨q,hq'⟩ := e286_positive_count_actual_witness G I e 5 (by rw [counts]; norm_num)
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
  have or' := out 0 1 (by decide) r hr
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
  have rSide := choiceSide r p pr.symm rQ pQ hr hp
  have noTen (S : Finset V) (hs : S.card = 10) (hS : G.IsClique (S : Set V))
      (u v : V) (uv : u ≠ v) (us : u ∉ S) (vs : v ∉ S) (uQ : u ∉ Q) (vQ : v ∉ Q)
      (adj : ∀ x ∈ S, G.Adj u x ∧ G.Adj v x) : False := by
    have seven := (e286_ten_clique_completers_excess G hG S hs hS u v uv us vs adj).2
    have two := pairBudget u v uv uQ vQ
    omega
  rcases pSide with h | h <;> rcases wSide with j | j <;> rcases rSide with l | l
  all_goals first
    | exact noTen _ k0 (cl 0) p w pw (op 0) (ow 0) pQ wQ (fun x hx => ⟨h x hx,j x hx⟩)
    | exact noTen _ k1 (cl 1) p w pw (op 1) (ow 1) pQ wQ (fun x hx => ⟨h x hx,j x hx⟩)
    | exact noTen _ k0 (cl 0) p r pr (op 0) (or' 0) pQ rQ (fun x hx => ⟨h x hx,l x hx⟩)
    | exact noTen _ k1 (cl 1) p r pr (op 1) (or' 1) pQ rQ (fun x hx => ⟨h x hx,l x hx⟩)
    | exact noTen _ k0 (cl 0) w r wr (ow 0) (or' 0) wQ rQ (fun x hx => ⟨j x hx,l x hx⟩)
    | exact noTen _ k1 (cl 1) w r wr (ow 1) (or' 1) wQ rQ (fun x hx => ⟨j x hx,l x hx⟩)

theorem e286_excluded (G : SimpleGraph V) (hG : E286Hypotheses G) : False := by
  obtain ⟨I,hc,hi,hd,e,h⟩ := e286_actual_support_only_C G hG
  exact e286_h5_C_impossible G hG I hc hi hd e h

theorem E286_verified : E286Statement := by
  rintro ⟨G,hG⟩
  exact e286_excluded G hG

end EG617
