module
public import EG617.Core.Core47Floor

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators
namespace EG617
universe u v
variable {V : Type u} {W : Type v} [Fintype V] [Fintype W]

/-- Relabel all three hereditary conditions, including the edge count on each subset. -/
theorem core_admissible_pull_iso {G : SimpleGraph V} {H : SimpleGraph W}
    (f : G ≃g H) (a : ℕ) (hH : CoreAdmissible a H) : CoreAdmissible a G := by
  classical
  constructor
  · intro S hi
    have h := hH.1 (S.image f) (by
      intro x hx y hy hxy hadj
      obtain ⟨s,hs,rfl⟩ := Finset.mem_image.mp hx
      obtain ⟨t,ht,rfl⟩ := Finset.mem_image.mp hy
      exact hi hs ht (fun he => hxy (congrArg f he)) (f.map_rel_iff.mp hadj))
    rwa [Finset.card_image_of_injective _ f.injective] at h
  constructor
  · intro S hc
    have h := hH.2.1 (S.image f) (by
      intro x hx y hy hxy
      obtain ⟨s,hs,rfl⟩ := Finset.mem_image.mp hx
      obtain ⟨t,ht,rfl⟩ := Finset.mem_image.mp hy
      exact f.map_rel_iff.mpr (hc hs ht (fun he => hxy (congrArg f he))))
    rwa [Finset.card_image_of_injective _ f.injective] at h
  · intro S
    let T := S.image f
    let g : S → T := fun s => ⟨f s.val, Finset.mem_image.mpr ⟨_,s.property,rfl⟩⟩
    have bij : Function.Bijective g := by
      constructor
      · intro s t h
        exact Subtype.ext (f.injective (congrArg Subtype.val h))
      · intro t
        obtain ⟨s,hs,h⟩ := Finset.mem_image.mp t.property
        exact ⟨⟨s,hs⟩,Subtype.ext h⟩
    let iso : G.induce (S : Set V) ≃g H.induce (T : Set W) :=
      { toEquiv := Equiv.ofBijective g bij
        map_rel_iff' := by intro x y; exact f.map_rel_iff }
    have count : coreInducedEdgeCount G S = coreInducedEdgeCount H T := iso.card_edgeFinset_eq
    have h := hH.2.2 T
    have card : T.card = S.card := Finset.card_image_of_injective _ f.injective
    rwa [count,← card]

theorem core47_floor_of_card (G : SimpleGraph V) (hn : Fintype.card V = 47)
    (h : CoreAdmissible 4 G) : 287 ≤ G.edgeFinset.card := by
  let iso := G.overFinIso hn
  have bound := core47_edge_floor_287 _ (core_admissible_pull_iso iso.symm 4 h)
  exact iso.card_edgeFinset_eq.symm ▸ bound

/-- Frozen COVER Section 1, every regular pivot has a 47-core of at least
287 edges and satisfies the exact shell charge identity. -/
theorem cover_h13_pivot_floor_ledger (G : SimpleGraph V) (hn : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ x, 13 ≤ G.degree x) (p : V) (hp : G.degree p = 13) :
    let A := G.neighborFinset p
    let C := Gᶜ.neighborFinset p
    let q := (G.induce (A : Set V))ᶜ.edgeFinset.card + ∑ x ∈ A, (G.degree x - 13)
    C.card = 47 ∧ 287 ≤ coreInducedEdgeCount G C ∧
      G.edgeFinset.card = 91 + q + coreInducedEdgeCount G C := by
  classical
  let A := G.neighborFinset p
  let C := Gᶜ.neighborFinset p
  have ca : A.card = 13 := (SimpleGraph.card_neighborFinset_eq_degree G p).trans hp
  have cc : C.card = 47 := by
    change (Gᶜ.neighborFinset p).card = 47
    rw [SimpleGraph.card_neighborFinset_eq_degree, G.degree_compl,hn,hp]
  have adm := core_admissible_nonNeighbors G 4 ha p C (by
    intro w hw
    have hm := (SimpleGraph.mem_neighborFinset Gᶜ p w).mp hw
    exact ⟨hm.ne.symm,((SimpleGraph.compl_adj G p w).mp hm).2⟩)
  have floor : 287 ≤ coreInducedEdgeCount G C :=
    core47_floor_of_card _ (by change Fintype.card C = 47; rwa [Fintype.card_coe]) adm
  have split := core_shell_edge_degree_ledger G p
  obtain ⟨allEdges,allDegrees⟩ := split
  change G.edgeFinset.card = coreInducedEdgeCount G C + G.degree p + coreInducedEdgeCount G A + adjCount G A C at allEdges
  change (∑ x ∈ A, G.degree x) = G.degree p + 2 * coreInducedEdgeCount G A + adjCount G A C at allDegrees
  have deficit : (∑ x ∈ A, (G.degree x-13)) + ∑ _x ∈ A, 13 = ∑ x ∈ A, G.degree x := by
    rw [← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl (fun x _ => Nat.sub_add_cancel (hd x))
  simp only [Finset.sum_const,smul_eq_mul,ca] at deficit
  have shell := core_compl_edge_count (G.induce (A : Set V))
  change coreInducedEdgeCount G A + _ = (Fintype.card A).choose 2 at shell
  rw [Fintype.card_coe,ca] at shell
  norm_num [Nat.choose_two_right] at shell
  refine ⟨cc,floor,?_⟩
  change G.edgeFinset.card = 91 + ((G.induce (A : Set V))ᶜ.edgeFinset.card +
    ∑ x ∈ A, (G.degree x - 13)) + coreInducedEdgeCount G C
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at shell allEdges ⊢
  omega

/-- Frozen COVER upper bound at both energies, for every regular pivot. -/
theorem cover_h13_pivot_charge_upper (G : SimpleGraph V) (hn : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ x, 13 ≤ G.degree x) (p : V) (hp : G.degree p = 13) :
    let A := G.neighborFinset p
    let q := (G.induce (A : Set V))ᶜ.edgeFinset.card + ∑ x ∈ A, (G.degree x - 13)
    (G.edgeFinset.card = 407 → q ≤ 29) ∧ (G.edgeFinset.card = 408 → q ≤ 30) := by
  obtain ⟨_,floor,ledger⟩ := cover_h13_pivot_floor_ledger G hn ha hd p hp
  dsimp only
  constructor <;> intro he <;> omega

/-- A hereditary 24-set contains three independent vertices, expressed in the
ambient vertex type so it can be combined with an independent set outside. -/
theorem cover_independent_three (G : SimpleGraph V) (ha : CoreAdmissible 5 G)
    (S : Finset V) (hs : 24 ≤ S.card) :
    ∃ I : Finset V, I ⊆ S ∧ I.card = 3 ∧ G.IsIndepSet (I : Set V) := by
  classical
  obtain ⟨T,ht,ct⟩ := Finset.exists_subset_card_eq hs
  let H := G.induce (T : Set V)
  have hn : ¬ CoreIndependenceBound 2 H := by
    intro h
    exact core_R224_empty_of_card H
      (by change Fintype.card T = 24; rwa [Fintype.card_coe])
      ⟨h,(core_admissible_induce G 5 ha T).2⟩
  unfold CoreIndependenceBound at hn
  push_neg at hn
  obtain ⟨J,hJ,cJ⟩ := hn
  obtain ⟨K,hK,cK⟩ := Finset.exists_subset_card_eq (show 3 ≤ J.card by omega)
  refine ⟨K.image Subtype.val,?_,?_,?_⟩
  · intro x hx
    obtain ⟨z,_,rfl⟩ := Finset.mem_image.mp hx
    exact ht z.property
  · rwa [Finset.card_image_of_injective _ Subtype.val_injective]
  · intro x hx y hy hxy
    obtain ⟨z,hz,rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨w,hw,rfl⟩ := Finset.mem_image.mp hy
    exact hJ (hK hz) (hK hw) (fun h => hxy (congrArg Subtype.val h))

theorem cover_no_embedded_R336 (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (S : Finset V) (hs : S.card = 36) :
    ¬ CoreAdmissible 3 (G.induce (S : Set V)) := by
  classical
  intro h
  have floor := core_R336_edges_ge_234 _ (by change Fintype.card S = 36; rwa [Fintype.card_coe]) h
  have eS : 234 ≤ coreInducedEdgeCount G S := by
    simpa only [coreInducedEdgeCount, SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] using floor
  have row (v : V) (hn : v ∉ S) : (S.filter (G.Adj v)).card ≤ 3 := by
    have dj : Disjoint ({v} : Finset V) S := Finset.disjoint_singleton_left.mpr hn
    have eqn := core_edge_count_union G {v} S dj
    have cap := ha.2.2 ({v} ∪ S)
    rw [Finset.card_union_of_disjoint dj,Finset.card_singleton,hs] at cap
    have val : D (1+36) = 237 := by decide
    rw [val] at cap
    rw [adjCount_eq_sum_filter] at eqn
    simp only [Finset.sum_singleton] at eqn
    omega
  have outside : 24 ≤ Sᶜ.card := by rw [Finset.card_compl,hs,hv]; decide
  obtain ⟨I,hi,ci,indI⟩ := cover_independent_three G ha Sᶜ outside
  let R := I.biUnion (fun v => S.filter (G.Adj v))
  have cr : R.card ≤ 9 := by
    have cr := Finset.card_biUnion_le (s := I) (t := fun v => S.filter (G.Adj v))
    have sum := Finset.sum_le_sum (s := I) (g := fun _ => 3)
      (fun v hv => row v (Finset.mem_compl.mp (hi hv)))
    simp only [Finset.sum_const,smul_eq_mul,ci] at sum
    exact cr.trans sum
  have sub : R ⊆ S := by
    intro z hz
    obtain ⟨v,_,hz⟩ := Finset.mem_biUnion.mp hz
    exact (Finset.mem_filter.mp hz).1
  have remain : 24 ≤ (S \ R).card := by
    have := Finset.card_sdiff_add_card_eq_card sub
    omega
  obtain ⟨J,hj,cj,indJ⟩ := cover_independent_three G ha _ remain
  have cross (x) (hx : x ∈ I) (y) (hy : y ∈ J) : ¬ G.Adj x y := by
    intro adj
    have mem := Finset.mem_sdiff.mp (hj hy)
    exact mem.2 (Finset.mem_biUnion.mpr ⟨x,hx,Finset.mem_filter.mpr ⟨mem.1,adj⟩⟩)
  have dj : Disjoint I J := Finset.disjoint_left.mpr (fun x hx hy =>
    Finset.mem_compl.mp (hi hx) (Finset.mem_sdiff.mp (hj hy)).1)
  have total := ha.1 (I ∪ J) (by
    intro x hx y hy ne
    rcases Finset.mem_union.mp hx with hx|hx <;> rcases Finset.mem_union.mp hy with hy|hy
    · exact indI hx hy ne
    · exact cross _ hx _ hy
    · exact fun adj => cross _ hy _ hx adj.symm
    · exact indJ hx hy ne)
  rw [Finset.card_union_of_disjoint dj,ci,cj] at total
  omega

theorem cover_common_nonNeighbors_le_35 (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (x y : V) (ne : x ≠ y) (hn : ¬G.Adj x y)
    (U : Finset V) (hu : ∀ z ∈ U, z ≠ x ∧ z ≠ y ∧ ¬G.Adj x z ∧ ¬G.Adj y z) :
    U.card ≤ 35 := by
  classical
  by_contra! h
  obtain ⟨S,sub,cs⟩ := Finset.exists_subset_card_eq (show 36 ≤ U.card by omega)
  exact cover_no_embedded_R336 G hv ha S cs
    (core_admissible_common_nonNeighbors G 3 ha x y ne hn S (fun z hz => hu z (sub hz)))

theorem cover_h13_missing_edge_row_union (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (C : Finset V) (hc : C.card = 47)
    (x y : V) (ne : x ≠ y) (hn : ¬G.Adj x y) (hx : x ∉ C) (hy : y ∉ C) :
    12 ≤ ((C.filter (G.Adj x)) ∪ (C.filter (G.Adj y))).card := by
  classical
  let R := C.filter (G.Adj x) ∪ C.filter (G.Adj y)
  have sub : R ⊆ C := Finset.union_subset (Finset.filter_subset _ _) (Finset.filter_subset _ _)
  have cap := cover_common_nonNeighbors_le_35 G hv ha x y ne hn (C \ R) (by
    intro z hz
    obtain ⟨hz,hr⟩ := Finset.mem_sdiff.mp hz
    exact ⟨fun e => hx (e ▸ hz),fun e => hy (e ▸ hz),
      fun e => hr (Finset.mem_union_left _ (Finset.mem_filter.mpr ⟨hz,e⟩)),
      fun e => hr (Finset.mem_union_right _ (Finset.mem_filter.mpr ⟨hz,e⟩))⟩)
  have := Finset.card_sdiff_add_card_eq_card sub
  change 12 ≤ R.card
  omega

theorem cover_h13_core_min_degree (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (p : V) (hp : G.degree p = 13)
    (v : (Gᶜ.neighborFinset p : Set V)) :
    11 ≤ (G.induce (Gᶜ.neighborFinset p : Set V)).degree v := by
  classical
  let C := Gᶜ.neighborFinset p
  have cc : C.card = 47 := by
    change (Gᶜ.neighborFinset p).card = 47
    rw [SimpleGraph.card_neighborFinset_eq_degree,G.degree_compl,hv,hp]
  have avoid (z : V) (hz : z ∈ C) : p ≠ z ∧ ¬G.Adj p z :=
    (SimpleGraph.compl_adj G p z).mp ((SimpleGraph.mem_neighborFinset Gᶜ p z).mp hz)
  let R := C.filter (G.Adj v.val)
  have sub : R ⊆ C := Finset.filter_subset _ _
  have inside : v.val ∈ C \ R := Finset.mem_sdiff.mpr ⟨v.property,fun h =>
    G.loopless v.val (Finset.mem_filter.mp h).2⟩
  have cap := cover_common_nonNeighbors_le_35 G hv ha p v.val (avoid _ v.property).1
    (avoid _ v.property).2 ((C \ R).erase v.val) (by
      intro z hz
      obtain ⟨hne,hz⟩ := Finset.mem_erase.mp hz
      obtain ⟨hz,hr⟩ := Finset.mem_sdiff.mp hz
      exact ⟨(avoid _ hz).1.symm,hne,(avoid _ hz).2,fun h => hr (Finset.mem_filter.mpr ⟨hz,h⟩)⟩)
  rw [Finset.card_erase_of_mem inside] at cap
  have eqn := degree_induce_eq_filter G C v
  simp only [← SimpleGraph.ncard_neighborSet] at eqn ⊢
  rw [eqn]
  change 11 ≤ R.card
  have := Finset.card_sdiff_add_card_eq_card sub
  omega

theorem cover_core_degree_eleven_clique (G : SimpleGraph V) (hv : Fintype.card V = 47)
    (ha : CoreAdmissible 4 G) : G.IsClique {x | G.degree x = 11} := by
  classical
  intro x hx y hy ne
  change G.degree x = 11 at hx
  change G.degree y = 11 at hy
  by_contra hn
  let S := Gᶜ.neighborFinset x
  have cs : S.card = 35 := by
    change (Gᶜ.neighborFinset x).card = 35
    rw [SimpleGraph.card_neighborFinset_eq_degree,G.degree_compl,hv,hx]
  have mem : y ∈ S := (SimpleGraph.mem_neighborFinset Gᶜ x y).mpr
    ((SimpleGraph.compl_adj G x y).mpr ⟨ne,hn⟩)
  have adm := core_admissible_nonNeighbors G 3 ha x S (by
    intro z hz
    have h := (SimpleGraph.compl_adj G x z).mp ((SimpleGraph.mem_neighborFinset Gᶜ x z).mp hz)
    exact ⟨h.1.symm,h.2⟩)
  have low := core_R335_degree_ge_twelve _ (by change Fintype.card S = 35; rwa [Fintype.card_coe]) adm ⟨y,mem⟩
  have eqn := degree_induce_eq_filter G S ⟨y,mem⟩
  simp only [← SimpleGraph.ncard_neighborSet] at eqn low
  rw [eqn] at low
  have sub : S.filter (G.Adj y) ⊆ G.neighborFinset y := fun z hz =>
    (SimpleGraph.mem_neighborFinset G y z).mpr (Finset.mem_filter.mp hz).2
  have size := Finset.card_le_card sub
  rw [SimpleGraph.card_neighborFinset_eq_degree,hy] at size
  omega

end EG617
