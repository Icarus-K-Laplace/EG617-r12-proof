module
public import EG617.Core.GateShell

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Common nonneighbors of two nonadjacent vertices lower alpha by two;
the clique bound and every induced D cap are inherited unchanged. -/
theorem core_admissible_common_nonNeighbors (G : SimpleGraph V) (a : ℕ)
    (hG : CoreAdmissible (a + 2) G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y)
    (S : Finset V) (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    CoreAdmissible a (G.induce (S : Set V)) := by
  classical
  refine ⟨?_, (core_admissible_induce G (a + 2) hG S).2⟩
  intro T hT
  let U := T.image (fun z : (S : Set V) => (z : V))
  have hUS : U ⊆ S := by
    intro z hz
    obtain ⟨b, _, rfl⟩ := Finset.mem_image.mp hz
    exact b.property
  have hU : G.IsIndepSet (U : Set V) := by
    intro b hb c hc hbc
    obtain ⟨b', hb', rfl⟩ := Finset.mem_image.mp hb
    obtain ⟨c', hc', rfl⟩ := Finset.mem_image.mp hc
    exact hT hb' hc' (fun he => hbc (congrArg Subtype.val he))
  have hyU : y ∉ U := fun hy => (hS y (hUS hy)).2.1 rfl
  have hi : G.IsIndepSet ((insert y U : Finset V) : Set V) := by
    intro b hb c hc hbc
    by_cases hby : b = y
    · subst b
      have hcU := Finset.mem_of_mem_insert_of_ne hc hbc.symm
      exact (hS c (hUS hcU)).2.2.2
    · have hbU := Finset.mem_of_mem_insert_of_ne hb hby
      by_cases hcy : c = y
      · subst c
        exact fun he => (hS b (hUS hbU)).2.2.2 he.symm
      · exact hU hbU (Finset.mem_of_mem_insert_of_ne hc hcy) hbc
  have hn : ∀ z ∈ insert y U, z ≠ x ∧ ¬ G.Adj x z := by
    intro z hz
    rcases Finset.mem_insert.mp hz with rfl | hz
    · exact ⟨hxy.symm, hnxy⟩
    · exact ⟨(hS z (hUS hz)).1, (hS z (hUS hz)).2.2.1⟩
  have hb := core_independence_nonNeighbors G (a + 1) hG.1 x (insert y U) hn hi
  rw [Finset.card_insert_of_notMem hyU] at hb
  have hcard : U.card = T.card := Finset.card_image_of_injective _ Subtype.val_injective
  omega

theorem core_R4_common_nonneighbors_card_le_23 (G : SimpleGraph V)
    (hG : CoreAdmissible 4 G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y)
    (S : Finset V) (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    S.card ≤ 23 := by
  classical
  by_contra hn
  obtain ⟨T, hTS, hT⟩ := Finset.exists_subset_card_eq (show 24 ≤ S.card by omega)
  have ha := core_admissible_common_nonNeighbors G 2 hG x y hxy hnxy T
    (fun z hz => hS z (hTS hz))
  exact core_R224_empty_of_card (G.induce (T : Set V))
    (by simpa only [Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using hT) ha

/-- Frozen M6 row-union lower bound, with both shell endpoints outside C. -/
theorem core_R4_row_union_ge_twelve (G : SimpleGraph V) (hG : CoreAdmissible 4 G)
    (C : Finset V) (hC : C.card = 35) (x y : V) (hxy : x ≠ y)
    (hnxy : ¬ G.Adj x y) (hx : x ∉ C) (hy : y ∉ C) :
    12 ≤ ((C.filter (G.Adj x)) ∪ (C.filter (G.Adj y))).card := by
  classical
  let R := C.filter (G.Adj x) ∪ C.filter (G.Adj y)
  let N := C \ R
  have hRC : R ⊆ C := Finset.union_subset (Finset.filter_subset _ _) (Finset.filter_subset _ _)
  have hn : ∀ z ∈ N, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z := by
    intro z hz
    obtain ⟨hzC, hzR⟩ := Finset.mem_sdiff.mp hz
    refine ⟨fun he => hx (he ▸ hzC), fun he => hy (he ▸ hzC), ?_, ?_⟩
    · intro hadj
      exact hzR (Finset.mem_union_left _ (Finset.mem_filter.mpr ⟨hzC, hadj⟩))
    · intro hadj
      exact hzR (Finset.mem_union_right _ (Finset.mem_filter.mpr ⟨hzC, hadj⟩))
  have hN := core_R4_common_nonneighbors_card_le_23 G hG x y hxy hnxy N hn
  have hcount : N.card + R.card = C.card := Finset.card_sdiff_add_card_eq_card hRC
  change 12 ≤ R.card
  omega

/-- The two endpoint incidence sets overlap in at most their mutual edge. -/
theorem core_two_degrees_le_edges_add_one (G : SimpleGraph V) (x y : V) (hxy : x ≠ y) :
    G.degree x + G.degree y ≤ G.edgeFinset.card + 1 := by
  classical
  let P : Finset V := {x, y}
  have hp : P.card = 2 := by simp [P, hxy]
  have he := edge_partition G P
  have hs := adjCount_union_right G P P Pᶜ disjoint_compl_right
  simp only [Finset.union_compl, adjCount_right_univ, adjCount_self] at hs
  have hsum : (∑ a ∈ P, G.degree a) = G.degree x + G.degree y := by
    exact Finset.sum_pair hxy
  rw [hsum] at hs
  have hsmall := core_induced_edges_le_choose G P
  rw [hp] at hsmall
  norm_num only [Nat.choose_two_right] at hsmall
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at he ⊢
  omega

/-- A shell vertex's actual degree splits into its edge to v, its shell degree
and its exterior row. Minimum degree11 therefore dominates the missing degree. -/
theorem core_shell_row_missing_degree_le (G : SimpleGraph V) (v : V)
    (hd : G.degree v = 11) (hmin : ∀ w, 11 ≤ G.degree w)
    (a : (G.neighborFinset v : Set V)) :
    ((G.induce (G.neighborFinset v : Set V))ᶜ).degree a ≤
      ((Gᶜ.neighborFinset v).filter (G.Adj a)).card := by
  classical
  let S := G.neighborFinset v
  let C := Gᶜ.neighborFinset v
  have ha : G.Adj v a := (SimpleGraph.mem_neighborFinset G v a).mp a.property
  have hdvS : Disjoint ({v} : Finset V) S := by simp [S]
  have hdSC : Disjoint S C := by
    rw [Finset.disjoint_left]
    intro z hz hzC
    exact ((SimpleGraph.compl_adj G v z).mp
      ((SimpleGraph.mem_neighborFinset Gᶜ v z).mp hzC)).2
      ((SimpleGraph.mem_neighborFinset G v z).mp hz)
  have hdAC : Disjoint (({v} : Finset V) ∪ S) C :=
    Finset.disjoint_union_left.mpr ⟨by simp [C], hdSC⟩
  have hcover : (({v} : Finset V) ∪ S) ∪ C = Finset.univ := by
    ext z
    by_cases hz : z = v
    · subst z
      simp
    · by_cases he : G.Adj v z <;> simp [S, C, hz, he, SimpleGraph.compl_adj, Ne.symm hz]
  have hsplit := adjCount_union_right G {(a : V)} ({v} ∪ S) C hdAC
  rw [hcover, adjCount_right_univ, Finset.sum_singleton,
    adjCount_union_right G {(a : V)} {v} S hdvS] at hsplit
  have hav : adjCount G {(a : V)} {v} = 1 := by
    simp only [adjCount, Finset.sum_singleton, if_pos ha.symm]
  have has : adjCount G {(a : V)} S = (G.induce (S : Set V)).degree a := by
    rw [adjCount_eq_sum_filter, Finset.sum_singleton]
    have hdegree := degree_induce_eq_filter G S a
    simp only [← SimpleGraph.ncard_neighborSet] at hdegree ⊢
    exact hdegree.symm
  have hac : adjCount G {(a : V)} C = (C.filter (G.Adj a)).card := by
    rw [adjCount_eq_sum_filter, Finset.sum_singleton]
  rw [hav, has, hac] at hsplit
  have hcomp := (G.induce (S : Set V)).degree_compl a
  have hcard : Fintype.card (S : Set V) = 11 := by
    simpa only [Set.fintypeCard_eq_ncard, Set.ncard_coe_finset, S,
      SimpleGraph.card_neighborFinset_eq_degree, ← SimpleGraph.ncard_neighborSet] using hd
  rw [hcard] at hcomp
  have hm := hmin a
  change ((G.induce (S : Set V))ᶜ).degree a ≤ (C.filter (G.Adj a)).card
  omega

/-- Sum of all row sizes, using one missing edge's two rows and the lower
bound on every other row. This is the paper's z+sum(g)>=11 in exact row form. -/
theorem core_missing_edge_row_sum (M : SimpleGraph V) (r : V → ℕ)
    (hrow : ∀ a, M.degree a ≤ r a) (a b : V) (hab : a ≠ b)
    (hpair : 12 ≤ r a + r b) :
    M.edgeFinset.card + 11 ≤ ∑ x : V, r x := by
  classical
  let U := (Finset.univ.erase a).erase b
  have ha : a ∈ (Finset.univ : Finset V) := Finset.mem_univ _
  have hb : b ∈ (Finset.univ : Finset V).erase a := Finset.mem_erase.mpr ⟨hab.symm, Finset.mem_univ _⟩
  have hr1 := Finset.sum_erase_add (s := Finset.univ) (f := r) ha
  have hr2 := Finset.sum_erase_add (s := Finset.univ.erase a) (f := r) hb
  have hm1 := Finset.sum_erase_add (s := Finset.univ) (f := fun x => M.degree x) ha
  have hm2 := Finset.sum_erase_add (s := Finset.univ.erase a) (f := fun x => M.degree x) hb
  have hrest : (∑ x ∈ U, M.degree x) ≤ ∑ x ∈ U, r x := Finset.sum_le_sum (fun x _ => hrow x)
  have hinc := core_two_degrees_le_edges_add_one M a b hab
  have he := M.sum_degrees_eq_twice_card_edges
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at he hinc ⊢
  dsimp only [U] at hrest
  omega

end EG617
