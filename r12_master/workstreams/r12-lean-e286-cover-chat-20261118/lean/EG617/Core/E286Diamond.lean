module
public import EG617.Core.E286Star

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators
namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem e286_shared_ten_pointwise (G : SimpleGraph V) (L A C : Finset V)
    (r q : V) (hl : L.card = 10) (ha : 0 < A.card) (hc : 0 < C.card) (hL : G.IsClique (L : Set V))
    (hLA : Disjoint L A) (hLC : Disjoint L C) (hAC : Disjoint A C)
    (hrL : r ∉ L) (hqL : q ∉ L) (hrC : r ∉ C) (hqA : q ∉ A)
    (hB : ∀ x ∈ e286Missing G L r, ∀ y ∈ A, G.Adj x y)
    (hD : ∀ x ∈ e286Missing G L q, ∀ y ∈ C, G.Adj x y) (x : V) :
    (x ∈ e286Missing G L r → x ∈ e286Missing G L q →
      A.card + C.card - 3 ≤ degreeExcess12 G x) ∧
    (x ∈ e286Missing G L r → x ∉ e286Missing G L q →
      A.card - 2 ≤ degreeExcess12 G x) ∧
    (x ∈ e286Missing G L q → x ∉ e286Missing G L r →
      C.card - 2 ≤ degreeExcess12 G x) := by
  classical
  have hsingle (v : V) (hx : x ∈ L) (hn : x ∉ e286Missing G L v) : G.Adj x v := by
    by_contra h
    exact hn (Finset.mem_filter.mpr ⟨hx, fun he => h he.symm⟩)
  refine ⟨?_, ?_, ?_⟩
  · intro hb hd
    have h := e286_clique_blocker_vertex_charge G L (A ∪ C) hL
      (Finset.disjoint_union_right.mpr ⟨hLA, hLC⟩) x (Finset.mem_filter.mp hb).1
      (fun y hy => (Finset.mem_union.mp hy).elim (hB x hb y) (hD x hd y))
    rw [hl, Finset.card_union_of_disjoint hAC] at h
    omega
  · intro hb hd
    have hx := (Finset.mem_filter.mp hb).1
    have h := e286_clique_charge_with_extra G L A hL hLA q x hqL hqA hx
      (hsingle q hx hd) (hB x hb)
    rw [hl] at h
    omega
  · intro hd hb
    have hx := (Finset.mem_filter.mp hd).1
    have h := e286_clique_charge_with_extra G L C hL hLC r x hrL hrC hx
      (hsingle r hx hb) (hD x hd)
    rw [hl] at h
    omega

theorem e286_shared_ten_charge (G : SimpleGraph V) (L A C : Finset V)
    (r q : V) (hl : L.card = 10) (ha : 0 < A.card) (hc : 0 < C.card) (hL : G.IsClique (L : Set V))
    (hLA : Disjoint L A) (hLC : Disjoint L C) (hAC : Disjoint A C)
    (hrL : r ∉ L) (hqL : q ∉ L) (hrC : r ∉ C) (hqA : q ∉ A)
    (hB : ∀ x ∈ e286Missing G L r, ∀ y ∈ A, G.Adj x y)
    (hD : ∀ x ∈ e286Missing G L q, ∀ y ∈ C, G.Adj x y) :
    (e286Missing G L r).card * (A.card - 2) + (e286Missing G L q).card * (C.card - 2) ≤
      ∑ x ∈ e286Missing G L r ∪ e286Missing G L q, degreeExcess12 G x := by
  classical
  let B := e286Missing G L r
  let D := e286Missing G L q
  let U := B ∪ D
  have hfilter (S : Finset V) (hs : S ⊆ U) : U.filter (fun x => x ∈ S) = S := by
    ext x
    simp only [Finset.mem_filter]
    exact ⟨And.right, fun hx => ⟨hs hx, hx⟩⟩
  have ledger (S : Finset V) (hs : S ⊆ U) (n : ℕ) :
      (∑ x ∈ U, if x ∈ S then n else 0) = S.card * n := by
    rw [← Finset.sum_filter, hfilter S hs]
    simp
  have hlocal (x : V) (hx : x ∈ U) :
      (if x ∈ B then A.card - 2 else 0) + (if x ∈ D then C.card - 2 else 0) ≤ degreeExcess12 G x := by
    obtain ⟨both, left, right⟩ := e286_shared_ten_pointwise G L A C r q hl ha hc hL
      hLA hLC hAC hrL hqL hrC hqA hB hD x
    by_cases hb : x ∈ B <;> by_cases hd : x ∈ D
    · have h := both hb hd
      simp only [if_pos hb, if_pos hd]
      omega
    · have h := left hb hd
      simp only [if_pos hb, if_neg hd]
      omega
    · have h := right hd hb
      simp only [if_neg hb, if_pos hd]
      omega
    · simp [hb, hd]
  have h := Finset.sum_le_sum hlocal
  rw [Finset.sum_add_distrib, ledger B Finset.subset_union_left,
    ledger D Finset.subset_union_right] at h
  exact h

theorem e286_h5_D_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hi : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V))
    (hcounts : e286GraphSupportCounts G I e = [1,1,1,1,1,0,0,0,0,0,0]) : False := by
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
  let u (i : Fin 4) : Fin 4 := if i.val < 2 then 0 else 1
  let v (i : Fin 4) : Fin 4 := if i.val % 2 = 0 then 2 else 3
  let code (i : Fin 4) : Fin 11 := ⟨i.val+1,by omega⟩
  have wit (i : Fin 4) : ∃ z : (seedMultipleSet G I : Set V), e286SeedSupportCode G I e z = code i := by
    have h : 0 < (e286GraphSupportCounts G I e)[(code i).val]! := by
      rw [hcounts]
      dsimp only [code]
      fin_cases i <;> decide
    simp only [e286GraphSupportCounts,e286_ofFn_get] at h
    obtain ⟨z,hz⟩ := Finset.card_pos.mp h
    exact ⟨z,(Finset.mem_filter.mp hz).2⟩
  choose z hz using wit
  let p (i : Fin 4) : V := z i
  have pinj : Function.Injective p := by
    intro i j h
    have eq : z i = z j := Subtype.ext h
    have hcode := congrArg (e286SeedSupportCode G I e) eq
    rw [hz,hz] at hcode
    exact Fin.ext (by have h := congrArg Fin.val hcode; dsimp [code] at h; omega)
  have hp (i : Fin 4) : seedNeighbors G I (p i) = {(e (u i) : V),(e (v i) : V)} := by
    have h := seedLabelNeighbors_image G I e (z i)
    rw [← e286_seed_support_code_spec G I e (z i),hz] at h
    have ht : e286SupportType (code i) = {u i,v i} := by fin_cases i <;> rfl
    rw [ht] at h
    simpa [p] using h.symm
  have out (i j : Fin 4) : p i ∉ K j := fun h =>
    Finset.disjoint_left.mp (seed_private_multiple_disjoint G I hi _ (e j).property) h (z i).property
  let A (i : Fin 4) := e286Missing G (K (u i)) (p i)
  let B (i : Fin 4) := e286Missing G (K (v i)) (p i)
  have sa (i : Fin 4) : A i ⊆ K (u i) := Finset.filter_subset _ _
  have sb (i : Fin 4) : B i ⊆ K (v i) := Finset.filter_subset _ _
  have uv (i : Fin 4) : u i ≠ v i := by fin_cases i <;> decide
  have k10 (i : Fin 4) : (K (u i)).card = 10 := by fin_cases i <;> apply sizes
  have k11 (i : Fin 4) : (K (v i)).card = 11 := by fin_cases i <;> apply sizes
  have edge (i : Fin 4) : ∀ x ∈ A i, ∀ y ∈ B i, G.Adj x y :=
    e286_actual_pair_edges G hG I hc hi _ _ _ (e (u i)).property (e (v i)).property (ne _ _ (uv i)) (hp i)
  have bp (i : Fin 4) : 0 < (B i).card := Finset.card_pos.mpr
    (e286_eleven_clique_missing_nonempty G hG _ (k11 i) (cl _) _ (out i _))
  let aCost (i : Fin 4) := (A i).card * ((B i).card-2)
  let bCost (i : Fin 4) := (B i).card * ((A i).card-2)
  let cost (i : Fin 4) := degreeExcess12 G (p i) + aCost i + bCost i
  have five (i : Fin 4) (hn : ¬ ∀ x ∈ K (u i), G.Adj (p i) x) : 5 ≤ cost i := by
    have h := e286_f10_11_extra_completer_minimum (A i).card (B i).card
      (Finset.card_pos.mpr (e286_missing_of_incomplete G _ _ hn)) (bp i)
      ((Finset.card_le_card (sa i)).trans (k10 i).le) ((Finset.card_le_card (sb i)).trans (k11 i).le)
    have deg := e286_pair_point_degree_charge G _ _ (sep _ _ (uv i)) (p i)
    change (K (u i)).card + (K (v i)).card ≤ 12 + degreeExcess12 G (p i) + (A i).card + (B i).card at deg
    rw [k10,k11] at deg
    dsimp only [cost,aCost,bCost]
    omega
  have expense (i : Fin 4) : degreeExcess12 G (p i) ≤ cost i := by dsimp only [cost]; omega
  have side (i j : Fin 4) (ij : i ≠ j) (same : u i = u j) : 5 ≤ cost i + cost j := by
    by_cases ci : ∀ x ∈ K (u i), G.Adj (p i) x
    · by_cases cj : ∀ x ∈ K (u j), G.Adj (p j) x
      · have seven := (e286_ten_clique_completers_excess G hG _ (k10 i) (cl _) _ _
          (fun h => ij (pinj h)) (out i _) (out j _) (fun x hx => ⟨ci x hx,cj x (same ▸ hx)⟩)).2
        have h := seven.trans (Nat.add_le_add (expense i) (expense j))
        omega
      · have h := five j cj
        omega
    · have h := five i ci
      omega
  let R (i : Fin 4) := insert (p i) (K i)
  have dis (i j : Fin 4) (h : i ≠ j) : Disjoint (R i) (R j) :=
    Finset.disjoint_insert_left.mpr ⟨fun hm => (Finset.mem_insert.mp hm).elim
      (fun e => h (pinj e)) (out i j), Finset.disjoint_insert_right.mpr ⟨out j i,sep i j h⟩⟩
  have total := e286_subset_excess_budget G hG (Finset.univ.biUnion R)
  rw [Finset.sum_biUnion (fun i _ j _ h => dis i j h)] at total
  have unfoldR (i : Fin 4) : (∑ x ∈ R i, degreeExcess12 G x) =
      degreeExcess12 G (p i) + ∑ x ∈ K i, degreeExcess12 G x := Finset.sum_insert (out i i)
  simp only [unfoldR,Fin.sum_univ_succ] at total
  have ledger0 : aCost 0 + aCost 1 ≤ ∑ x ∈ K 0, degreeExcess12 G x := by
    have raw := e286_shared_ten_charge G (K 0) (B 0) (B 1) (p 0) (p 1) (sizes 0) (bp 0) (bp 1) (cl 0)
      ((sep 0 (v 0) (by decide)).mono_right (sb 0)) ((sep 0 (v 1) (by decide)).mono_right (sb 1))
      ((sep (v 0) (v 1) (by decide)).mono (sb 0) (sb 1))
      (out 0 0) (out 1 0) (fun h => out 0 _ (sb 1 h)) (fun h => out 1 _ (sb 0 h))
      (edge 0) (edge 1)
    exact raw.trans (Finset.sum_le_sum_of_subset (Finset.union_subset (sa 0) (sa 1)))
  have ledger1 : aCost 2 + aCost 3 ≤ ∑ x ∈ K 1, degreeExcess12 G x := by
    have raw := e286_shared_ten_charge G (K 1) (B 2) (B 3) (p 2) (p 3) (sizes 1) (bp 2) (bp 3) (cl 1)
      ((sep 1 (v 2) (by decide)).mono_right (sb 2)) ((sep 1 (v 3) (by decide)).mono_right (sb 3))
      ((sep (v 2) (v 3) (by decide)).mono (sb 2) (sb 3))
      (out 2 1) (out 3 1) (fun h => out 2 _ (sb 3 h)) (fun h => out 3 _ (sb 2 h))
      (edge 2) (edge 3)
    exact raw.trans (Finset.sum_le_sum_of_subset (Finset.union_subset (sa 2) (sa 3)))
  have ledger2 : bCost 0 + bCost 2 ≤ ∑ x ∈ K 2, degreeExcess12 G x := by
    have raw := e286_shared_leaf_pair_charge G (K 2) (A 0) (A 2) (p 0) (p 2) (sizes 2) (cl 2)
      ((sep 2 (u 0) (by decide)).mono_right (sa 0)) ((sep 2 (u 2) (by decide)).mono_right (sa 2))
      ((sep (u 0) (u 2) (by decide)).mono (sa 0) (sa 2))
      (out 0 2) (out 2 2) (fun h => out 0 _ (sa 2 h)) (fun h => out 2 _ (sa 0 h))
      (fun y hy x hx => (edge 0 x hx y hy).symm) (fun y hy x hx => (edge 2 x hx y hy).symm)
    exact raw.trans (Finset.sum_le_sum_of_subset (Finset.union_subset (sb 0) (sb 2)))
  have ledger3 : bCost 1 + bCost 3 ≤ ∑ x ∈ K 3, degreeExcess12 G x := by
    have raw := e286_shared_leaf_pair_charge G (K 3) (A 1) (A 3) (p 1) (p 3) (sizes 3) (cl 3)
      ((sep 3 (u 1) (by decide)).mono_right (sa 1)) ((sep 3 (u 3) (by decide)).mono_right (sa 3))
      ((sep (u 1) (u 3) (by decide)).mono (sa 1) (sa 3))
      (out 1 3) (out 3 3) (fun h => out 1 _ (sa 3 h)) (fun h => out 3 _ (sa 1 h))
      (fun y hy x hx => (edge 1 x hx y hy).symm) (fun y hy x hx => (edge 3 x hx y hy).symm)
    exact raw.trans (Finset.sum_le_sum_of_subset (Finset.union_subset (sb 1) (sb 3)))
  have left := side 0 1 (by decide) rfl
  have right := side 2 3 (by decide) rfl
  dsimp only [cost] at left right
  change (degreeExcess12 G (p 0) + _) + ((degreeExcess12 G (p 1) + _) +
    ((degreeExcess12 G (p 2) + _) + ((degreeExcess12 G (p 3) + _) + 0))) ≤ 8 at total
  omega

theorem e286_actual_support_only_C (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧ (∀ x ∈ I, G.degree x = 12) ∧
      ∃ e : Fin 4 ≃ (I : Set V), e286GraphSupportCounts G I e = [3,0,0,0,0,2,0,0,0,0,0] := by
  obtain ⟨I,hc,hi,hd,e,h | h⟩ := e286_actual_support_D_or_C G hG
  · exact (e286_h5_D_impossible G hG I hc hi hd e h).elim
  · exact ⟨I,hc,hi,hd,e,h⟩

end EG617
