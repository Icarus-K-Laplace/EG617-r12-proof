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
    (Finset.mem_filter.mp h).2.ne rfl⟩
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
  have same : 12 ≤ (S.filter (G.Adj y)).card := by
    convert low using 1 <;> congr 1 <;> ext z <;> simp
  omega

/-- Vertices inserted into the new core are exactly old shell vertices
missing the repivot. The removed vertices form its old exterior row. -/
theorem cover_repivot_sets (G : SimpleGraph V) (p y : V) (py : G.Adj p y) :
    let C := Gᶜ.neighborFinset p
    let Y := Gᶜ.neighborFinset y
    Y \ C = (G.neighborFinset p).filter (Gᶜ.Adj y) ∧
      C \ Y = C.filter (G.Adj y) := by
  classical
  dsimp only
  constructor <;> ext z <;>
    simp only [Finset.mem_sdiff,Finset.mem_filter,SimpleGraph.mem_neighborFinset,
      SimpleGraph.compl_adj]
  · by_cases h : p = z
    · subst z; simp [py.symm]
    · simp [h] <;> tauto
  · by_cases h : y = z
    · subst z; simp [py]
    · simp [h]

theorem cover_repivot_equal_exchange (G : SimpleGraph V) (p y : V)
    (hp : G.degree p = G.degree y) :
    ((Gᶜ.neighborFinset y) \ (Gᶜ.neighborFinset p)).card =
      ((Gᶜ.neighborFinset p) \ (Gᶜ.neighborFinset y)).card := by
  classical
  have eqn : (Gᶜ.neighborFinset p).card = (Gᶜ.neighborFinset y).card := by
    simp only [SimpleGraph.card_neighborFinset_eq_degree,SimpleGraph.degree_compl,hp]
  rw [Finset.card_sdiff,Finset.card_sdiff,Finset.inter_comm]
  omega

/-- The exact inserted-degree ledger counts the retained and removed parts
of the old exterior separately. It uses no degree threshold. -/
theorem cover_inserted_degree_ledger (G : SimpleGraph V) (C Y : Finset V) :
    let S := Y \ C
    let Drow := C \ Y
    adjCount G S Y + adjCount G S Drow + 2 * coreInducedEdgeCount Gᶜ S =
      adjCount G S C + 2 * S.card.choose 2 := by
  classical
  let S := Y \ C
  let T := C ∩ Y
  let Drow := C \ Y
  have cy : T ∪ S = Y := by ext z; simp [T,S]; tauto
  have cc : T ∪ Drow = C := by ext z; simp [T,Drow]; tauto
  have dy : Disjoint T S := Finset.disjoint_left.mpr (fun z ht hs =>
    (Finset.mem_sdiff.mp hs).2 (Finset.mem_inter.mp ht).1)
  have dc : Disjoint T Drow := Finset.disjoint_left.mpr (fun z ht hs =>
    (Finset.mem_sdiff.mp hs).2 (Finset.mem_inter.mp ht).2)
  have newSum := adjCount_union_right G S T S dy
  have oldSum := adjCount_union_right G S T Drow dc
  rw [cy,adjCount_self] at newSum
  rw [cc] at oldSum
  have missing := core_induced_compl_edge_count G S
  change adjCount G S Y + adjCount G S Drow + 2 * coreInducedEdgeCount Gᶜ S =
    adjCount G S C + 2 * S.card.choose 2
  omega

/-- INS11 in additive form, retaining the nonnegative removed-row charge.
The degree bound belongs to the actual new core of the regular pivot y. -/
theorem cover_repivot_INS11 (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (p y : V) (py : G.Adj p y)
    (hp : G.degree p = 13) (hy : G.degree y = 13) :
    let C := Gᶜ.neighborFinset p
    let S := (G.neighborFinset p).filter (Gᶜ.Adj y)
    let Drow := C.filter (G.Adj y)
    11 * S.card + adjCount G S Drow + 2 * coreInducedEdgeCount Gᶜ S ≤
      adjCount G S C + 2 * S.card.choose 2 := by
  classical
  let C := Gᶜ.neighborFinset p
  let Y := Gᶜ.neighborFinset y
  let S := Y \ C
  have point (z : V) (hz : z ∈ S) : 11 ≤ (Y.filter (G.Adj z)).card := by
    have mem := (Finset.mem_sdiff.mp hz).1
    have low := cover_h13_core_min_degree G hv ha y hy ⟨z,mem⟩
    have eqn := degree_induce_eq_filter G Y ⟨z,mem⟩
    simp only [← SimpleGraph.ncard_neighborSet] at low eqn
    rw [eqn] at low
    convert low using 1 <;> congr 1 <;> ext w <;> simp
  have total := Finset.sum_le_sum point
  rw [← adjCount_eq_sum_filter] at total
  simp only [Finset.sum_const,smul_eq_mul] at total
  have ledger := cover_inserted_degree_ledger G C Y
  obtain ⟨hs,hr⟩ := cover_repivot_sets G p y py
  dsimp only
  rw [← hs,← hr]
  change 11 * S.card + adjCount G S (C \ Y) + 2 * coreInducedEdgeCount Gᶜ S ≤
    adjCount G S C + 2 * S.card.choose 2
  change adjCount G S Y + adjCount G S (C \ Y) + 2 * coreInducedEdgeCount Gᶜ S =
    adjCount G S C + 2 * S.card.choose 2 at ledger
  rw [Nat.mul_comm S.card 11] at total
  omega

/-- Exact exchange identity for two equally large cores. All incidence counts
use the graph induced on the corresponding old or new vertex set. -/
theorem cover_equal_exchange_identity (G : SimpleGraph V) (C Y : Finset V)
    (sizes : (Y \ C).card = (C \ Y).card) :
    let S := Y \ C
    let R := C \ Y
    coreInducedEdgeCount G C + adjCount G S Y + coreInducedEdgeCount Gᶜ S =
      coreInducedEdgeCount G Y + adjCount G R C + coreInducedEdgeCount Gᶜ R := by
  classical
  let S := Y \ C
  let R := C \ Y
  let T := C ∩ Y
  have cy : T ∪ S = Y := by ext z; simp [T,S]; tauto
  have cc : T ∪ R = C := by ext z; simp [T,R]; tauto
  have dy : Disjoint T S := Finset.disjoint_left.mpr (fun z ht hs =>
    (Finset.mem_sdiff.mp hs).2 (Finset.mem_inter.mp ht).1)
  have dc : Disjoint T R := Finset.disjoint_left.mpr (fun z ht hs =>
    (Finset.mem_sdiff.mp hs).2 (Finset.mem_inter.mp ht).2)
  have ey := core_edge_count_union G T S dy
  have ec := core_edge_count_union G T R dc
  have sy := adjCount_union_right G S T S dy
  have rc := adjCount_union_right G R T R dc
  rw [cy] at ey
  rw [cc] at ec
  rw [cy,adjCount_self,adjCount_symm G S T] at sy
  rw [cc,adjCount_self,adjCount_symm G R T] at rc
  have ms := core_induced_compl_edge_count G S
  have mr := core_induced_compl_edge_count G R
  change S.card = R.card at sizes
  rw [sizes] at ms
  change coreInducedEdgeCount G C + adjCount G S Y + coreInducedEdgeCount Gᶜ S =
    coreInducedEdgeCount G Y + adjCount G R C + coreInducedEdgeCount Gᶜ R
  omega

/-- Frozen Section 3 signed charge difference in balance form. Subtracting
the same beta times the exchange size on both sides yields the excess version. -/
theorem cover_repivot_charge_identity (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ z, 13 ≤ G.degree z) (p y : V)
    (hp : G.degree p = 13) (hy : G.degree y = 13) :
    let C := Gᶜ.neighborFinset p
    let Y := Gᶜ.neighborFinset y
    let S := Y \ C
    let R := C \ Y
    let q := fun z : V => (G.induce (G.neighborFinset z : Set V))ᶜ.edgeFinset.card +
      ∑ w ∈ G.neighborFinset z, (G.degree w - 13)
    q y + adjCount G S Y + coreInducedEdgeCount Gᶜ S =
      q p + adjCount G R C + coreInducedEdgeCount Gᶜ R := by
  obtain ⟨_,_,oldLedger⟩ := cover_h13_pivot_floor_ledger G hv ha hd p hp
  obtain ⟨_,_,newLedger⟩ := cover_h13_pivot_floor_ledger G hv ha hd y hy
  have exchange := cover_equal_exchange_identity G _ _ (cover_repivot_equal_exchange G p y (hp.trans hy.symm))
  dsimp only at exchange ⊢
  omega

/-- Independent choices from the uncovered core can be appended to the
independent shell set without introducing a cross edge. -/
theorem cover_uncovered_independent_budget (G : SimpleGraph V) (ha : CoreAdmissible 5 G)
    (I C : Finset V) (dis : Disjoint I C) (hi : G.IsIndepSet (I : Set V))
    (J : Finset V) (hj : J ⊆ C \ I.biUnion (fun x => C.filter (G.Adj x)))
    (ind : G.IsIndepSet (J : Set V)) : I.card + J.card ≤ 5 := by
  classical
  have dj := dis.mono_right (show J ⊆ C from fun z hz => (Finset.mem_sdiff.mp (hj hz)).1)
  have cross (x) (hx : x ∈ I) (z) (hz : z ∈ J) : ¬G.Adj x z := by
    intro h
    obtain ⟨inC,out⟩ := Finset.mem_sdiff.mp (hj hz)
    exact out (Finset.mem_biUnion.mpr ⟨x,hx,Finset.mem_filter.mpr ⟨inC,h⟩⟩)
  have bound := ha.1 (I ∪ J) (by
    intro x hx y hy ne
    rcases Finset.mem_union.mp hx with hx|hx <;> rcases Finset.mem_union.mp hy with hy|hy
    · exact hi hx hy ne
    · exact cross _ hx _ hy
    · exact fun e => cross _ hy _ hx e.symm
    · exact ind hx hy ne)
  rwa [Finset.card_union_of_disjoint dj] at bound

theorem cover_triangle_row_union (G : SimpleGraph V) (ha : CoreAdmissible 5 G)
    (I C : Finset V) (dis : Disjoint I C) (hi : G.IsIndepSet (I : Set V))
    (ci : I.card = 3) (cc : C.card = 47) :
    24 ≤ (I.biUnion (fun x => C.filter (G.Adj x))).card := by
  classical
  let R := I.biUnion (fun x => C.filter (G.Adj x))
  have sub : R ⊆ C := by
    intro z hz
    obtain ⟨_,_,h⟩ := Finset.mem_biUnion.mp hz
    exact (Finset.mem_filter.mp h).1
  have eqn := Finset.card_sdiff_add_card_eq_card sub
  change 24 ≤ R.card
  by_contra! small
  obtain ⟨J,hj,cj,ind⟩ := cover_independent_three G ha (C \ R) (by omega)
  have cap := cover_uncovered_independent_budget G ha I C dis hi J hj ind
  omega

theorem cover_K4_row_union (G : SimpleGraph V) (ha : CoreAdmissible 5 G)
    (I C : Finset V) (dis : Disjoint I C) (hi : G.IsIndepSet (I : Set V))
    (ci : I.card = 4) (cc : C.card = 47) :
    36 ≤ (I.biUnion (fun x => C.filter (G.Adj x))).card := by
  classical
  let R := I.biUnion (fun x => C.filter (G.Adj x))
  have clique : G.IsClique ((C \ R : Finset V) : Set V) := by
    intro x hx y hy ne
    by_contra h
    let J : Finset V := {x,y}
    have sub : J ⊆ C \ R := by
      intro z hz
      rcases Finset.mem_insert.mp hz with rfl | hz
      · exact hx
      · obtain rfl := Finset.mem_singleton.mp hz
        exact hy
    have ind : G.IsIndepSet (J : Set V) := by
      intro u hu v hv uv
      simp only [J,Finset.mem_coe,Finset.mem_insert,Finset.mem_singleton] at hu hv
      rcases hu with rfl|rfl <;> rcases hv with rfl|rfl <;> first | contradiction | exact h | exact fun e => h e.symm
    have cap := cover_uncovered_independent_budget G ha I C dis hi J sub ind
    have cj : J.card = 2 := Finset.card_pair ne
    omega
  have cap := ha.2.1 (C \ R) clique
  have sub : R ⊆ C := by
    intro z hz
    obtain ⟨_,_,h⟩ := Finset.mem_biUnion.mp hz
    exact (Finset.mem_filter.mp h).1
  have eqn := Finset.card_sdiff_add_card_eq_card sub
  change 36 ≤ R.card
  omega

theorem cover_shell_row_identity (G : SimpleGraph V) (p y : V) (py : G.Adj p y)
    (hp : G.degree p = 13) (hy : 13 ≤ G.degree y) :
    ((Gᶜ.neighborFinset p).filter (G.Adj y)).card =
      ((G.neighborFinset p).filter (Gᶜ.Adj y)).card + (G.degree y - 13) := by
  classical
  obtain ⟨ins,rem⟩ := cover_repivot_sets G p y py
  rw [← ins,← rem,Finset.card_sdiff,Finset.card_sdiff,Finset.inter_comm]
  have bound := Finset.card_le_card (Finset.inter_subset_left
    (s₂ := Gᶜ.neighborFinset p) (s₁ := Gᶜ.neighborFinset y))
  have ltY := G.degree_lt_card_verts y
  have ltP := G.degree_lt_card_verts p
  rw [Finset.inter_comm] at bound
  simp only [SimpleGraph.card_neighborFinset_eq_degree,SimpleGraph.degree_compl] at bound ⊢
  omega

/-- Frozen COVER (1), in additive form on arbitrary subsets of the actual shell. -/
theorem cover_shell_subset_charge (G : SimpleGraph V) (p : V) (hp : G.degree p = 13)
    (hd : ∀ y, 13 ≤ G.degree y) (I : Finset V) (sub : I ⊆ G.neighborFinset p) :
    let A := G.neighborFinset p
    let C := Gᶜ.neighborFinset p
    let B := A \ I
    let g := fun y => G.degree y - 13
    coreInducedEdgeCount Gᶜ A + (∑ y ∈ A, g y) + coreInducedEdgeCount Gᶜ I =
      adjCount G I C + coreInducedEdgeCount Gᶜ B + ∑ y ∈ B, g y := by
  classical
  let A := G.neighborFinset p
  let C := Gᶜ.neighborFinset p
  let B := A \ I
  let g := fun y => G.degree y - 13
  have dj : Disjoint I B := Finset.disjoint_sdiff
  have decomp : I ∪ B = A := Finset.union_sdiff_of_subset sub
  have row : adjCount G I C = adjCount Gᶜ I A + ∑ y ∈ I, g y := by
    rw [adjCount_eq_sum_filter,adjCount_eq_sum_filter,← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro y hy
    have eqn := cover_shell_row_identity G p y
      ((SimpleGraph.mem_neighborFinset G p y).mp (sub hy)) hp (hd y)
    dsimp only [A,C,g]
    convert eqn using 2 <;> congr 1 <;> ext z <;> simp
  have edges := core_edge_count_union Gᶜ I B dj
  have adj := adjCount_union_right Gᶜ I I B dj
  have sums := Finset.sum_union (f := g) dj
  rw [decomp] at edges sums
  rw [decomp,adjCount_self] at adj
  change coreInducedEdgeCount Gᶜ A + (∑ y ∈ A, g y) + coreInducedEdgeCount Gᶜ I =
    adjCount G I C + coreInducedEdgeCount Gᶜ B + ∑ y ∈ B, g y
  omega

/-- A missing four-clique in a regular shell forces charge at least 30. -/
theorem cover_K4_charge_floor (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ z, 13 ≤ G.degree z) (p : V) (hp : G.degree p = 13)
    (I : Finset V) (sub : I ⊆ G.neighborFinset p) (hi : G.IsIndepSet (I : Set V))
    (ci : I.card = 4) :
    30 ≤ coreInducedEdgeCount Gᶜ (G.neighborFinset p) +
      ∑ z ∈ G.neighborFinset p, (G.degree z - 13) := by
  classical
  let C := Gᶜ.neighborFinset p
  have cc : C.card = 47 := by
    change (Gᶜ.neighborFinset p).card = 47
    rw [SimpleGraph.card_neighborFinset_eq_degree,G.degree_compl,hv,hp]
  have dj : Disjoint I C := Finset.disjoint_left.mpr (by
    intro z hz hc
    exact ((SimpleGraph.compl_adj G p z).mp ((SimpleGraph.mem_neighborFinset Gᶜ p z).mp hc)).2
      ((SimpleGraph.mem_neighborFinset G p z).mp (sub hz)))
  have cap := cover_K4_row_union G ha I C dj hi ci cc
  have total := Finset.card_biUnion_le (s := I) (t := fun z => C.filter (G.Adj z))
  rw [← adjCount_eq_sum_filter] at total
  have small := core_induced_edges_le_choose Gᶜ I
  rw [ci] at small
  norm_num [Nat.choose_two_right] at small
  have led := cover_shell_subset_charge G p hp hd I sub
  dsimp only at led
  change 36 ≤ _ at cap
  dsimp only [C] at total cap
  omega

/-- Section 3 equation (3) before subtracting a degree threshold. This
natural-number identity also applies when the removed degrees have deficits. -/
theorem cover_repivot_exact_row_charge (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ z, 13 ≤ G.degree z) (p y : V)
    (py : G.Adj p y) (hp : G.degree p = 13) (hy : G.degree y = 13) :
    let A := G.neighborFinset p
    let C := Gᶜ.neighborFinset p
    let Y := Gᶜ.neighborFinset y
    let S := Y \ C
    let R := C \ Y
    let B := A \ S
    let qy := (G.induce (G.neighborFinset y : Set V))ᶜ.edgeFinset.card +
      ∑ z ∈ G.neighborFinset y, (G.degree z - 13)
    qy + 2 * S.card.choose 2 =
      coreInducedEdgeCount Gᶜ B + (∑ z ∈ B, (G.degree z - 13)) +
      adjCount G R C + coreInducedEdgeCount Gᶜ R + adjCount G S R := by
  classical
  let A := G.neighborFinset p
  let C := Gᶜ.neighborFinset p
  let Y := Gᶜ.neighborFinset y
  let S := Y \ C
  have sub : S ⊆ A := by
    change Y \ C ⊆ A
    rw [(cover_repivot_sets G p y py).1]
    exact Finset.filter_subset _ _
  have shell := cover_shell_subset_charge G p hp hd S sub
  have balance := cover_repivot_charge_identity G hv ha hd p y hp hy
  have insertLedger := cover_inserted_degree_ledger G C Y
  have oldMissing : (G.induce (A : Set V))ᶜ.edgeFinset.card = coreInducedEdgeCount Gᶜ A := by
    simp only [coreInducedEdgeCount,SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard,
      core_induce_compl]
  dsimp only at shell balance insertLedger ⊢
  dsimp only [S,Y,C,A] at oldMissing shell insertLedger
  rw [oldMissing] at balance
  omega

/-- Frozen COVER Section 8 strict 211-edge floor, via the kernel-checked
Andrasfai--Erdos--Sos theorem applied to the complement. -/
theorem cover_R335_edges_ge_211 (G : SimpleGraph V) (hv : Fintype.card V = 35)
    (ha : CoreAdmissible 3 G) : 211 ≤ G.edgeFinset.card := by
  classical
  by_contra! he
  have md (v : V) : G.degree v ≤ 12 := by
    have rest := Finset.sum_le_sum (s := (Finset.univ : Finset V).erase v)
      (f := fun _ => 12) (g := G.degree) (fun w _ => core_R335_degree_ge_twelve G hv ha w)
    simp [hv] at rest
    have total := Finset.sum_erase_add (Finset.univ : Finset V) G.degree (Finset.mem_univ v)
    rw [G.sum_degrees_eq_twice_card_edges] at total
    simp only [SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard] at total he
    omega
  have cf : Gᶜ.CliqueFree 4 := by
    intro S hS
    have i := (SimpleGraph.isNClique_compl G).mp hS
    have cap := ha.1 S i.isIndepSet
    rw [i.card_eq] at cap
    omega
  haveI : Nonempty V := Fintype.card_pos_iff.mp (by omega)
  have lower : 22 ≤ Gᶜ.minDegree := Gᶜ.le_minDegree_of_forall_le_degree 22 (by
    intro v
    rw [G.degree_compl,hv]
    have := md v
    omega)
  obtain ⟨col⟩ := SimpleGraph.colorable_of_cliqueFree_lt_minDegree (G := Gᶜ) (r := 3) cf
    (by norm_num [hv]; omega)
  let fiber := fun i : Fin 3 => Finset.univ.filter (fun z : V => col z = i)
  have cap (i : Fin 3) : (fiber i).card ≤ 11 := by
    apply ha.2.1
    apply (SimpleGraph.isIndepSet_compl G).mp
    intro x hx y hy _
    exact col.not_adj_of_mem_colorClass (Finset.mem_filter.mp hx).2 (Finset.mem_filter.mp hy).2
  have total : (∑ i, (fiber i).card) = 35 := by
    simpa only [fiber,Finset.sum_const,smul_eq_mul,mul_one,Finset.card_univ,hv] using
      Finset.sum_fiberwise' (Finset.univ : Finset V) (fun z => col z) (fun _ => (1 : ℕ))
  have upper := Finset.sum_le_sum (s := (Finset.univ : Finset (Fin 3)))
    (fun i _ => cap i)
  norm_num at upper
  omega

theorem cover_R223_edges_ge_131 (G : SimpleGraph V) (hv : Fintype.card V = 23)
    (ha : CoreAdmissible 2 G) : 131 ≤ G.edgeFinset.card := by
  classical
  have total := core_compl_edge_count G
  norm_num [Nat.choose_two_right,hv] at total
  by_contra! he
  have high : 121 ≤ Gᶜ.edgeFinset.card := by
    simp only [SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard] at total he ⊢
    omega
  have cf : Gᶜ.CliqueFree 3 := by
    intro S hS
    have h := (SimpleGraph.isNClique_compl G).mp hS
    have cap := ha.1 S h.isIndepSet
    rw [h.card_eq] at cap
    omega
  have bound : CoreIndependenceBound 11 Gᶜ := fun S h => ha.2.1 S ((SimpleGraph.isIndepSet_compl G).mp h)
  obtain ⟨_,_,_,_,_,ledger⟩ := r23_exact_neighbor_ledger Gᶜ hv cf bound high
  have upper : Gᶜ.edgeFinset.card ≤ 122 := ledger.2.2.2.2.2.2.2.1
  simp only [SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard] at total upper he
  omega

/-- Removing twelve vertices of degree at least twelve from a 288-edge
graph leaves at most 210 edges, with every edge inside the removed set
counted exactly twice in the degree sum. -/
theorem cover_delete_twelve_cap (G : SimpleGraph V) (he : G.edgeFinset.card ≤ 288)
    (hd : ∀ z, 12 ≤ G.degree z) (U : Finset V) (cu : U.card = 12) :
    coreInducedEdgeCount G Uᶜ ≤ 210 := by
  classical
  have part := edge_partition G U
  have degree := adjCount_union_right G U U Uᶜ disjoint_compl_right
  rw [Finset.union_compl,adjCount_right_univ,adjCount_self] at degree
  have low := Finset.sum_le_sum (s := U) (f := fun _ => 12) (g := G.degree) (fun z _ => hd z)
  simp only [Finset.sum_const,smul_eq_mul,cu] at low
  have small := core_induced_edges_le_choose G U
  rw [cu] at small
  norm_num [Nat.choose_two_right] at small
  simp only [SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard] at he part
  omega

end EG617
