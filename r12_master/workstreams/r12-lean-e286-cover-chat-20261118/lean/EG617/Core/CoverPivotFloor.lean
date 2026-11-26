module
public import EG617.Core.Core47Floor
import Mathlib.Tactic.Ring

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
      (f := fun _ => 12) (g := fun w => G.degree w) (fun w _ => core_R335_degree_ge_twelve G hv ha w)
    simp [hv] at rest
    have total := Finset.sum_erase_add (Finset.univ : Finset V) (fun w => G.degree w) (Finset.mem_univ v)
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
  obtain ⟨_,_,_,_,_,ledger⟩ := r23_exact_neighbor_ledger Gᶜ hv cf bound (by
    simpa only [SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard] using high)
  have upper := ledger.2.2.2.2.2.2.2.1
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
  have low := Finset.sum_le_sum (s := U) (f := fun _ => 12) (g := fun z => G.degree z) (fun z _ => hd z)
  simp only [Finset.sum_const,smul_eq_mul,cu] at low
  have small := core_induced_edges_le_choose G U
  rw [cu] at small
  norm_num [Nat.choose_two_right] at small
  simp only [SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard] at he part
  omega

/-- Equality case of the 288-core gate: a 12-vertex union of the two rows
forces a 14-set over its hereditary cap. -/
theorem cover_211_pair_union_ne_twelve (G : SimpleGraph V) (ha : CoreAdmissible 4 G)
    (C : Finset V) (cc : C.card = 35) (hc : CoreAdmissible 3 (G.induce (C : Set V)))
    (ec : coreInducedEdgeCount G C = 211) (x y : V) (ne : x ≠ y) (hn : ¬G.Adj x y)
    (hx : x ∉ C) (hy : y ∉ C) :
    ((C.filter (G.Adj x)) ∪ (C.filter (G.Adj y))).card ≠ 12 := by
  classical
  let U := C.filter (G.Adj x) ∪ C.filter (G.Adj y)
  let W := C \ U
  intro cu
  change U.card = 12 at cu
  have sub : U ⊆ C := Finset.union_subset (Finset.filter_subset _ _) (Finset.filter_subset _ _)
  have decomp : U ∪ W = C := Finset.union_sdiff_of_subset sub
  have dj : Disjoint U W := Finset.disjoint_sdiff
  have cw : W.card = 23 := by
    have := Finset.card_sdiff_add_card_eq_card sub
    change (C \ U).card = 23
    omega
  have adm := core_admissible_common_nonNeighbors G 2 ha x y ne hn W (by
    intro z hz
    obtain ⟨hz,out⟩ := Finset.mem_sdiff.mp hz
    exact ⟨fun e => hx (e ▸ hz),fun e => hy (e ▸ hz),
      fun e => out (Finset.mem_union_left _ (Finset.mem_filter.mpr ⟨hz,e⟩)),
      fun e => out (Finset.mem_union_right _ (Finset.mem_filter.mpr ⟨hz,e⟩))⟩)
  have ew := cover_R223_edges_ge_131 _ (by change Fintype.card W = 23; rwa [Fintype.card_coe]) adm
  change 131 ≤ coreInducedEdgeCount G W at ew
  have sum : 144 ≤ adjCount G U C := by
    rw [adjCount_eq_sum_filter]
    have point (z : V) (hz : z ∈ U) : 12 ≤ (C.filter (G.Adj z)).card := by
      have low := core_R335_degree_ge_twelve _ (by change Fintype.card C = 35; rwa [Fintype.card_coe]) hc ⟨z,sub hz⟩
      have eqn := degree_induce_eq_filter G C ⟨z,sub hz⟩
      simp only [← SimpleGraph.ncard_neighborSet] at low eqn
      rw [eqn] at low
      convert low using 1 <;> congr 1 <;> ext w <;> simp
    have sum := Finset.sum_le_sum point
    simpa only [Finset.sum_const,smul_eq_mul,cu] using sum
  have cross := adjCount_union_right G U U W dj
  rw [decomp,adjCount_self] at cross
  have edges := core_edge_count_union G U W dj
  rw [decomp] at edges
  have dense : 64 ≤ coreInducedEdgeCount G U := by omega
  have anti : U.filter (fun z => ¬G.Adj x z ∧ ¬G.Adj y z) = ∅ := by
    apply Finset.eq_empty_iff_forall_notMem.mpr
    intro z hz
    obtain ⟨hz,h1,h2⟩ := Finset.mem_filter.mp hz
    rcases Finset.mem_union.mp hz with hz | hz
    · exact h1 (Finset.mem_filter.mp hz).2
    · exact h2 (Finset.mem_filter.mp hz).2
  apply core_fourteen_cost_obstruction G ha.2.2 U cu x y ne (fun h => hx (sub h)) (fun h => hy (sub h))
  have comp := core_induced_compl_edge_count G U
  rw [cu] at comp
  norm_num [Nat.choose_two_right] at comp
  rw [anti,Finset.card_empty]
  omega

theorem cover_pair_row_charge (M : SimpleGraph V) (r : V → ℕ)
    (hrow : ∀ a, M.degree a ≤ r a) (a b : V) (hab : a ≠ b)
    : M.edgeFinset.card + r a + r b ≤ (∑ x : V, r x) + 1 := by
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


theorem cover_degree_eleven_edges_ge_289 (G : SimpleGraph V)
    (hV : Fintype.card V = 47) (hG : CoreAdmissible 4 G) (v : V)
    (hd : G.degree v = 11) (hmin : ∀ w, 11 ≤ G.degree w) :
    289 ≤ G.edgeFinset.card := by
  classical
  by_contra! small
  let S := G.neighborFinset v
  let C := Gᶜ.neighborFinset v
  let M := (G.induce (S : Set V))ᶜ
  let r : ↥(S : Set V) → ℕ := fun a => (C.filter (G.Adj a)).card
  have hS : S.card = 11 := by
    simpa only [S, SimpleGraph.card_neighborFinset_eq_degree, ← SimpleGraph.ncard_neighborSet] using hd
  have hC : C.card = 35 := by
    have hc : C.card = Fintype.card V - 1 - G.degree v := G.degree_compl v
    omega
  have ha : CoreAdmissible 3 (G.induce (C : Set V)) :=
    core_admissible_nonNeighbors G 3 hG v C (by
      intro w hw
      have h := (SimpleGraph.mem_neighborFinset Gᶜ v w).mp hw
      exact ⟨h.ne.symm, ((SimpleGraph.compl_adj G v w).mp h).2⟩)
  have heC : 211 ≤ coreInducedEdgeCount G C := by
    have h := cover_R335_edges_ge_211 (G.induce (C : Set V))
      (by simpa only [Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using hC) ha
    simpa only [coreInducedEdgeCount, SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] using h
  obtain ⟨x, hx, y, hy, hxy, hnxy⟩ := core_degree_eleven_neighbor_nonedge G hG.2.1 v hd
  have hSC : Disjoint S C := by
    rw [Finset.disjoint_left]
    intro z hz hzC
    exact ((SimpleGraph.compl_adj G v z).mp
      ((SimpleGraph.mem_neighborFinset Gᶜ v z).mp hzC)).2
      ((SimpleGraph.mem_neighborFinset G v z).mp hz)
  have hxC : x ∉ C := fun hxC => Finset.disjoint_left.mp hSC hx hxC
  have hyC : y ∉ C := fun hyC => Finset.disjoint_left.mp hSC hy hyC
  have hrow : ∀ a, M.degree a ≤ r a := fun a => core_shell_row_missing_degree_le G v hd hmin a
  have hpair : 12 ≤ r ⟨x, hx⟩ + r ⟨y, hy⟩ := by
    have hu := core_R4_row_union_ge_twelve G hG C hC x y hxy hnxy hxC hyC
    have hc := Finset.card_union_le (C.filter (G.Adj x)) (C.filter (G.Adj y))
    exact hu.trans hc
  have hrows := cover_pair_row_charge M r (by
    intro a
    simpa only [← SimpleGraph.ncard_neighborSet] using hrow a) ⟨x, hx⟩ ⟨y, hy⟩
    (fun he => hxy (congrArg Subtype.val he))
  have hcross : (∑ a : (S : Set V), r a) = adjCount G S C := by
    rw [adjCount_eq_sum_filter, ← Finset.sum_coe_sort S]
    rfl
  rw [hcross] at hrows
  have hcomp := core_compl_edge_count (G.induce (S : Set V))
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard,
    Set.ncard_coe_finset, hS] at hcomp
  norm_num only [Nat.choose_two_right] at hcomp
  have he := (core_shell_edge_degree_ledger G v).1
  dsimp only [M] at hrows
  have over : 212 ≤ coreInducedEdgeCount G C ∨ 13 ≤ r ⟨x,hx⟩ + r ⟨y,hy⟩ := by
    by_cases big : 212 ≤ coreInducedEdgeCount G C
    · exact Or.inl big
    · right
      have eqn : coreInducedEdgeCount G C = 211 := by omega
      have not12 := cover_211_pair_union_ne_twelve G hG C hC ha eqn x y hxy hnxy hxC hyC
      have lower := core_R4_row_union_ge_twelve G hG C hC x y hxy hnxy hxC hyC
      have upper := Finset.card_union_le (C.filter (G.Adj x)) (C.filter (G.Adj y))
      change 13 ≤ (C.filter (G.Adj x)).card + (C.filter (G.Adj y)).card
      omega
  simp only [coreInducedEdgeCount, SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard]
    at he heC hrows hcomp over small
  simp only [S,C,SimpleGraph.neighborFinset_def,← Set.toFinite_toFinset,
    ← SimpleGraph.ncard_neighborSet] at he heC hrows hcomp hd over hpair
  omega

theorem cover_h13_core_288_min_degree (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (p : V) (hp : G.degree p = 13)
    (he : coreInducedEdgeCount G (Gᶜ.neighborFinset p) ≤ 288)
    (z : (Gᶜ.neighborFinset p : Set V)) :
    12 ≤ (G.induce (Gᶜ.neighborFinset p : Set V)).degree z := by
  classical
  let C := Gᶜ.neighborFinset p
  let H := G.induce (C : Set V)
  have cc : C.card = 47 := by
    change (Gᶜ.neighborFinset p).card = 47
    rw [SimpleGraph.card_neighborFinset_eq_degree,G.degree_compl,hv,hp]
  have adm := core_admissible_nonNeighbors G 4 ha p C (by
    intro w hw
    have h := (SimpleGraph.compl_adj G p w).mp ((SimpleGraph.mem_neighborFinset Gᶜ p w).mp hw)
    exact ⟨h.1.symm,h.2⟩)
  have md (w : (C : Set V)) : 11 ≤ H.degree w := cover_h13_core_min_degree G hv ha p hp w
  change 12 ≤ H.degree z
  by_contra! low
  have dz : H.degree z = 11 := by have := md z; omega
  have big := cover_degree_eleven_edges_ge_289 H (by change Fintype.card C = 47; rwa [Fintype.card_coe]) adm z dz md
  change coreInducedEdgeCount G C ≤ 288 at he
  simp only [coreInducedEdgeCount,SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard] at he
  dsimp only [H] at big
  simp only [SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard] at big
  omega

/-- EDGE13 for every missing-shell edge of an actual regular-pivot core in
the licensed at-most-288 edge range. -/
theorem cover_h13_EDGE13 (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (p : V) (hp : G.degree p = 13)
    (he : coreInducedEdgeCount G (Gᶜ.neighborFinset p) ≤ 288)
    (x y : V) (ne : x ≠ y) (hn : ¬G.Adj x y)
    (hx : x ∉ Gᶜ.neighborFinset p) (hy : y ∉ Gᶜ.neighborFinset p) :
    let C := Gᶜ.neighborFinset p
    13 ≤ ((C.filter (G.Adj x)) ∪ (C.filter (G.Adj y))).card := by
  classical
  let C := Gᶜ.neighborFinset p
  let R := C.filter (G.Adj x) ∪ C.filter (G.Adj y)
  have cc : C.card = 47 := by
    change (Gᶜ.neighborFinset p).card = 47
    rw [SimpleGraph.card_neighborFinset_eq_degree,G.degree_compl,hv,hp]
  have sub : R ⊆ C := Finset.union_subset (Finset.filter_subset _ _) (Finset.filter_subset _ _)
  change 13 ≤ R.card
  by_contra! small
  have card := Finset.card_sdiff_add_card_eq_card sub
  obtain ⟨W,hw,cw⟩ := Finset.exists_subset_card_eq (show 35 ≤ (C \ R).card by omega)
  have wc : W ⊆ C := fun z hz => (Finset.mem_sdiff.mp (hw hz)).1
  let X := C \ W
  have cx : X.card = 12 := by
    have := Finset.card_sdiff_add_card_eq_card wc
    change (C \ W).card = 12
    omega
  have adm := core_admissible_common_nonNeighbors G 3 ha x y ne hn W (by
    intro z hz
    obtain ⟨hz,out⟩ := Finset.mem_sdiff.mp (hw hz)
    exact ⟨fun e => hx (e ▸ hz),fun e => hy (e ▸ hz),
      fun e => out (Finset.mem_union_left _ (Finset.mem_filter.mpr ⟨hz,e⟩)),
      fun e => out (Finset.mem_union_right _ (Finset.mem_filter.mpr ⟨hz,e⟩))⟩)
  have ew := cover_R335_edges_ge_211 _ (by change Fintype.card W = 35; rwa [Fintype.card_coe]) adm
  change 211 ≤ coreInducedEdgeCount G W at ew
  have deg (z : V) (hz : z ∈ X) : 12 ≤ (C.filter (G.Adj z)).card := by
    have mem := (Finset.mem_sdiff.mp hz).1
    have low := cover_h13_core_288_min_degree G hv ha p hp he ⟨z,mem⟩
    have eqn := degree_induce_eq_filter G C ⟨z,mem⟩
    simp only [← SimpleGraph.ncard_neighborSet] at low eqn
    rw [eqn] at low
    convert low using 1 <;> congr 1 <;> ext w <;> simp
  have sum := Finset.sum_le_sum deg
  rw [← adjCount_eq_sum_filter] at sum
  simp only [Finset.sum_const,smul_eq_mul,cx] at sum
  have dj : Disjoint W X := Finset.disjoint_sdiff
  have decomp : W ∪ X = C := Finset.union_sdiff_of_subset wc
  have incid := adjCount_union_right G X W X dj
  rw [decomp,adjCount_self,adjCount_symm G X W] at incid
  have edges := core_edge_count_union G W X dj
  rw [decomp] at edges
  have cap := core_induced_edges_le_choose G X
  rw [cx] at cap
  norm_num [Nat.choose_two_right] at cap
  change coreInducedEdgeCount G C ≤ 288 at he
  omega

theorem cover_middle_degree_promotes (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ z, 13 ≤ G.degree z) (p y : V)
    (py : G.Adj p y) (hp : G.degree p = 13) (hy : G.degree y = 13)
    (he : coreInducedEdgeCount G (Gᶜ.neighborFinset p) ≤ 288) :
    let C := Gᶜ.neighborFinset p
    let S := Gᶜ.neighborFinset y \ C
    let qy := (G.induce (G.neighborFinset y : Set V))ᶜ.edgeFinset.card +
      ∑ z ∈ G.neighborFinset y, (G.degree z - 13)
    (3 ≤ S.card ∧ S.card ≤ 10 → 30 ≤ qy) ∧
      (4 ≤ S.card ∧ S.card ≤ 9 → 36 ≤ qy) := by
  classical
  let C := Gᶜ.neighborFinset p
  let Y := Gᶜ.neighborFinset y
  let R := C \ Y
  let S := Y \ C
  have point (z : V) (hz : z ∈ R) : 12 ≤ (C.filter (G.Adj z)).card := by
    have mem := (Finset.mem_sdiff.mp hz).1
    have low := cover_h13_core_288_min_degree G hv ha p hp he ⟨z,mem⟩
    have eqn := degree_induce_eq_filter G C ⟨z,mem⟩
    simp only [← SimpleGraph.ncard_neighborSet] at low eqn
    rw [eqn] at low
    convert low using 1 <;> congr 1 <;> ext w <;> simp
  have sum := Finset.sum_le_sum point
  rw [← adjCount_eq_sum_filter] at sum
  simp only [Finset.sum_const,smul_eq_mul] at sum
  have same : S.card = R.card := cover_repivot_equal_exchange G p y (hp.trans hy.symm)
  rw [← same] at sum
  have charge := cover_repivot_exact_row_charge G hv ha hd p y py hp hy
  dsimp only at charge ⊢
  dsimp only [S,R,Y,C] at sum
  have arith (d : ℕ) : (3 ≤ d ∧ d ≤ 10 → 30 + 2*d.choose 2 ≤ d*12) ∧
      (4 ≤ d ∧ d ≤ 9 → 36 + 2*d.choose 2 ≤ d*12) := by
    constructor <;> rintro ⟨h1,h2⟩ <;> interval_cases d <;> decide
  constructor
  · intro h
    have := (arith _).1 h
    omega
  · intro h
    have := (arith _).2 h
    omega

theorem cover_shell_missing_edges_ge_22 (G : SimpleGraph V) (ha : CoreAdmissible 5 G)
    (p : V) (hp : G.degree p = 13) : 22 ≤ coreInducedEdgeCount Gᶜ (G.neighborFinset p) := by
  classical
  let A := G.neighborFinset p
  have cp : p ∉ A := by simp [A]
  have ca : A.card = 13 := (SimpleGraph.card_neighborFinset_eq_degree G p).trans hp
  have dj : Disjoint ({p} : Finset V) A := Finset.disjoint_singleton_left.mpr cp
  have cap := ha.2.2 ({p} ∪ A)
  rw [Finset.card_union_of_disjoint dj,Finset.card_singleton,ca] at cap
  have d14 : D (1+13) = 69 := by decide
  rw [d14] at cap
  have edges := core_edge_count_union G {p} A dj
  have row : adjCount G {p} A = 13 := by
    rw [adjCount_eq_sum_filter,Finset.sum_singleton,Finset.filter_eq_self.mpr
      (fun z hz => (SimpleGraph.mem_neighborFinset G p z).mp hz),ca]
  have comp := core_induced_compl_edge_count G A
  rw [ca] at comp
  norm_num [Nat.choose_two_right] at comp
  change 22 ≤ coreInducedEdgeCount Gᶜ A
  omega

theorem cover_shell_target_clique_cap (G : SimpleGraph V) (ha : CoreAdmissible 5 G)
    (p : V) (I : Finset V) (sub : I ⊆ G.neighborFinset p) (cl : G.IsClique (I : Set V)) :
    I.card ≤ 10 := by
  classical
  have extCl : G.IsClique (insert p (I : Set V)) :=
    cl.insert (fun w hw _ => (SimpleGraph.mem_neighborFinset G p w).mp (sub hw))
  have bound := ha.2.1 (insert p I) (by simpa only [Finset.coe_insert] using extCl)
  have outside : p ∉ I := fun hp => ((SimpleGraph.mem_neighborFinset G p p).mp (sub hp)).ne rfl
  rw [Finset.card_insert_of_notMem outside] at bound
  omega

/-- At energy 408, an extreme middle degree of 3 or 10 saturates the old
core inequality and forces all four nonnegative corrections individually. -/
theorem cover_408_repivot_equality (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ z, 13 ≤ G.degree z) (p y : V)
    (py : G.Adj p y) (hp : G.degree p = 13) (hy : G.degree y = 13)
    (energy : G.edgeFinset.card = 408)
    (he : coreInducedEdgeCount G (Gᶜ.neighborFinset p) ≤ 288) :
    let A := G.neighborFinset p
    let C := Gᶜ.neighborFinset p
    let Y := Gᶜ.neighborFinset y
    let S := Y \ C
    let R := C \ Y
    let B := A \ S
    let qy := (G.induce (G.neighborFinset y : Set V))ᶜ.edgeFinset.card +
      ∑ z ∈ G.neighborFinset y, (G.degree z - 13)
    S.card = 3 ∨ S.card = 10 →
      qy = 30 ∧ coreInducedEdgeCount Gᶜ B = 0 ∧ (∑ z ∈ B, (G.degree z - 13)) = 0 ∧
      adjCount G R C = 12 * S.card ∧ coreInducedEdgeCount Gᶜ R = 0 ∧ adjCount G S R = 0 ∧
      coreInducedEdgeCount G Y = 287 := by
  classical
  let C := Gᶜ.neighborFinset p
  let Y := Gᶜ.neighborFinset y
  let R := C \ Y
  let S := Y \ C
  have point (z : V) (hz : z ∈ R) : 12 ≤ (C.filter (G.Adj z)).card := by
    have mem := (Finset.mem_sdiff.mp hz).1
    have low := cover_h13_core_288_min_degree G hv ha p hp he ⟨z,mem⟩
    have eqn := degree_induce_eq_filter G C ⟨z,mem⟩
    simp only [← SimpleGraph.ncard_neighborSet] at low eqn
    rw [eqn] at low
    convert low using 1 <;> congr 1 <;> ext w <;> simp
  have sum := Finset.sum_le_sum point
  rw [← adjCount_eq_sum_filter] at sum
  simp only [Finset.sum_const,smul_eq_mul] at sum
  have same : S.card = R.card := cover_repivot_equal_exchange G p y (hp.trans hy.symm)
  rw [← same] at sum
  dsimp only [R,S,C,Y] at sum
  have charge := cover_repivot_exact_row_charge G hv ha hd p y py hp hy
  obtain ⟨_,newFloor,newLedger⟩ := cover_h13_pivot_floor_ledger G hv ha hd y hy
  dsimp only at charge ⊢
  intro cs
  have scalar (d : ℕ) (hc : d = 3 ∨ d = 10) : 30 + 2 * d.choose 2 = d * 12 := by
    rcases hc with rfl | rfl <;> decide
  have val := scalar _ cs
  have upper := (cover_h13_pivot_charge_upper G hv ha hd y hy).2 energy
  simp only [SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard] at energy newLedger upper charge ⊢
  omega

/-- The inserted vertices in the energy-408 equality channel are a target
clique. Minimum degree 12 is obtained anew on the repivoted 287-edge core. -/
theorem cover_408_inserted_missing_zero (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ z, 13 ≤ G.degree z) (p y : V)
    (py : G.Adj p y) (hp : G.degree p = 13) (hy : G.degree y = 13)
    (energy : G.edgeFinset.card = 408)
    (he : coreInducedEdgeCount G (Gᶜ.neighborFinset p) ≤ 288) :
    let C := Gᶜ.neighborFinset p
    let Y := Gᶜ.neighborFinset y
    let S := Y \ C
    S.card = 3 ∨ S.card = 10 → coreInducedEdgeCount Gᶜ S = 0 := by
  classical
  let C := Gᶜ.neighborFinset p
  let Y := Gᶜ.neighborFinset y
  let S := Y \ C
  dsimp only
  intro h
  obtain ⟨qy,_,_,removed,kappa,_,newSize⟩ := cover_408_repivot_equality G hv ha hd p y py hp hy energy he h
  have point (z : V) (hz : z ∈ S) : 12 ≤ (Y.filter (G.Adj z)).card := by
    have mem := (Finset.mem_sdiff.mp hz).1
    have low := cover_h13_core_288_min_degree G hv ha y hy (by omega) ⟨z,mem⟩
    have eqn := degree_induce_eq_filter G Y ⟨z,mem⟩
    simp only [← SimpleGraph.ncard_neighborSet] at low eqn
    rw [eqn] at low
    convert low using 1 <;> congr 1 <;> ext w <;> simp
  have sum := Finset.sum_le_sum point
  rw [← adjCount_eq_sum_filter] at sum
  simp only [Finset.sum_const,smul_eq_mul] at sum
  have cap := (cover_h13_pivot_charge_upper G hv ha hd p hp).2 energy
  have balance := cover_repivot_charge_identity G hv ha hd p y hp hy
  dsimp only [S,C,Y] at sum
  dsimp only at balance ⊢
  omega

/-- Matching bound for a triangle-free set of endpoints in the actual shell.
The matching is supplied as two injective lists of disjoint endpoints. -/
theorem cover_shell_matching_charge (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ z, 13 ≤ G.degree z) (p : V) (hp : G.degree p = 13)
    (k : ℕ) (l r : Fin k ↪ V)
    (hl : ∀ i, l i ∈ G.neighborFinset p) (hr : ∀ i, r i ∈ G.neighborFinset p)
    (dis : ∀ i j, l i ≠ r j) (miss : ∀ i, ¬G.Adj (l i) (r i)) :
    let I := Finset.univ.map l ∪ Finset.univ.map r
    let q := coreInducedEdgeCount Gᶜ (G.neighborFinset p) +
      ∑ z ∈ G.neighborFinset p, (G.degree z - 13)
    (Gᶜ.induce (I : Set V)).CliqueFree 3 → 12*k ≤ q + k*k := by
  classical
  let L := Finset.univ.map l
  let R := Finset.univ.map r
  let I := L ∪ R
  let C := Gᶜ.neighborFinset p
  have dj : Disjoint L R := Finset.disjoint_left.mpr (by
    intro z hz hw
    obtain ⟨i,_,rfl⟩ := Finset.mem_map.mp hz
    obtain ⟨j,_,e⟩ := Finset.mem_map.mp hw
    exact dis i j e.symm)
  have sub : I ⊆ G.neighborFinset p := by
    intro z hz
    rcases Finset.mem_union.mp hz with h | h
    · obtain ⟨i,_,rfl⟩ := Finset.mem_map.mp h
      exact hl i
    · obtain ⟨i,_,rfl⟩ := Finset.mem_map.mp h
      exact hr i
  have out (z : V) (hz : z ∈ G.neighborFinset p) : z ∉ C := fun hc =>
    ((SimpleGraph.compl_adj G p z).mp ((SimpleGraph.mem_neighborFinset Gᶜ p z).mp hc)).2
      ((SimpleGraph.mem_neighborFinset G p z).mp hz)
  have cc : C.card = 47 := by
    change (Gᶜ.neighborFinset p).card = 47
    rw [SimpleGraph.card_neighborFinset_eq_degree,G.degree_compl,hv,hp]
  have pair (i : Fin k) : 12 ≤ (C.filter (G.Adj (l i))).card + (C.filter (G.Adj (r i))).card :=
    (cover_h13_missing_edge_row_union G hv ha C cc _ _ (dis i i) (miss i) (out _ (hl i))
      (out _ (hr i))).trans (Finset.card_union_le _ _)
  have low := Finset.sum_le_sum (s := Finset.univ) (fun i _ => pair i)
  simp only [Finset.sum_const,Finset.card_univ,Fintype.card_fin,smul_eq_mul,Finset.sum_add_distrib] at low
  have eqn : adjCount G I C = (∑ i, (C.filter (G.Adj (l i))).card) +
      ∑ i, (C.filter (G.Adj (r i))).card := by
    rw [adjCount_eq_sum_filter,Finset.sum_union dj]
    simp [L,R,Finset.sum_map]
  have ci : I.card = k+k := by rw [Finset.card_union_of_disjoint dj]; simp [L,R]
  dsimp only
  intro cf
  have m : coreInducedEdgeCount Gᶜ I ≤ k*k := by
    change (Gᶜ.induce (I : Set V)).CliqueFree 3 at cf
    have h := cf.card_edgeFinset_le
    rw [SimpleGraph.turanNumber_two] at h
    simp only [SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard,Set.ncard_coe_finset,ci] at h
    have ar : (k+k)^2 = (k*k)*4 := by ring
    rw [ar,Nat.mul_div_cancel _ (by decide : 0 < 4)] at h
    simpa only [coreInducedEdgeCount,SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard] using h
  have ledger := cover_shell_subset_charge G p hp hd I sub
  dsimp only at ledger ⊢
  change coreInducedEdgeCount Gᶜ (G.neighborFinset p) + _ + coreInducedEdgeCount Gᶜ I =
    adjCount G I C + coreInducedEdgeCount Gᶜ _ + _ at ledger
  rw [eqn] at ledger
  rw [Nat.mul_comm 12 k]
  omega

/-- Any subset of a shell below charge 30 obeys the sharp K4-free Turan
cap. The four-clique obstruction is derived on the original parent. -/
theorem cover_low_charge_shell_turan (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ z, 13 ≤ G.degree z) (p : V) (hp : G.degree p = 13)
    (hq : coreInducedEdgeCount Gᶜ (G.neighborFinset p) +
      (∑ z ∈ G.neighborFinset p, (G.degree z - 13)) ≤ 29)
    (T : Finset V) (sub : T ⊆ G.neighborFinset p) :
    coreInducedEdgeCount Gᶜ T ≤ T.card^2 / 3 := by
  classical
  have cf : (Gᶜ.induce (T : Set V)).CliqueFree 4 := by
    intro S hs
    let I := S.image (fun z : (T : Set V) => z.val)
    have ci : I.card = 4 := (Finset.card_image_of_injective _ Subtype.val_injective).trans hs.card_eq
    have incl : I ⊆ G.neighborFinset p := by
      intro z hz
      obtain ⟨w,_,rfl⟩ := Finset.mem_image.mp hz
      exact sub w.property
    have ind : G.IsIndepSet (I : Set V) := by
      intro x hx y hy ne
      obtain ⟨u,hu,rfl⟩ := Finset.mem_image.mp hx
      obtain ⟨v,hv',rfl⟩ := Finset.mem_image.mp hy
      have edge := hs.isClique hu hv' (fun h => ne (congrArg Subtype.val h))
      exact ((SimpleGraph.compl_adj G u.val v.val).mp edge).2
    have cap := cover_K4_charge_floor G hv ha hd p hp I incl ind ci
    omega
  have cap := cf.card_edgeFinset_le
  rw [SimpleGraph.turanNumber_three] at cap
  simpa only [coreInducedEdgeCount,SimpleGraph.edgeFinset_card,Set.fintypeCard_eq_ncard,
    Set.ncard_coe_finset] using cap

/-- Three shell rows of size at least eleven already force charge thirty. -/
theorem cover_three_heavy_rows (G : SimpleGraph V) (hd : ∀ z, 13 ≤ G.degree z)
    (p : V) (hp : G.degree p = 13)
    (hq : coreInducedEdgeCount Gᶜ (G.neighborFinset p) +
      (∑ z ∈ G.neighborFinset p, (G.degree z - 13)) ≤ 29) :
    ((G.neighborFinset p).filter (fun z => 11 ≤ ((Gᶜ.neighborFinset p).filter (G.Adj z)).card)).card ≤ 2 := by
  classical
  let C := Gᶜ.neighborFinset p
  let X := (G.neighborFinset p).filter (fun z => 11 ≤ (C.filter (G.Adj z)).card)
  change X.card ≤ 2
  by_contra! big
  obtain ⟨T,sub,ct⟩ := Finset.exists_subset_card_eq (show 3 ≤ X.card by omega)
  have low := Finset.sum_le_sum (s := T) (f := fun _ => 11) (g := fun z => (C.filter (G.Adj z)).card)
    (fun z hz => (Finset.mem_filter.mp (sub hz)).2)
  rw [← adjCount_eq_sum_filter] at low
  simp only [Finset.sum_const,smul_eq_mul,ct] at low
  have ledger := cover_shell_subset_charge G p hp hd T
    (fun z hz => (Finset.mem_filter.mp (sub hz)).1)
  have cap := core_induced_edges_le_choose Gᶜ T
  rw [ct] at cap
  norm_num [Nat.choose_two_right] at cap
  dsimp only at ledger
  dsimp only [C] at low
  omega

/-- On a low-charge pivot whose core has at most 288 edges, two distinct
heavy rows force an outside missing edge. EDGE13 and the five-edge Turan
bound on those four endpoints contradict the subset charge identity. -/
theorem cover_low_charge_heavy_rows_unique (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ z, 13 ≤ G.degree z) (p : V) (hp : G.degree p = 13)
    (he : coreInducedEdgeCount G (Gᶜ.neighborFinset p) ≤ 288)
    (hq : coreInducedEdgeCount Gᶜ (G.neighborFinset p) +
      (∑ z ∈ G.neighborFinset p, (G.degree z - 13)) ≤ 29)
    (x y : V) (hx : x ∈ G.neighborFinset p) (hy : y ∈ G.neighborFinset p)
    (wx : 11 ≤ ((Gᶜ.neighborFinset p).filter (G.Adj x)).card)
    (wy : 11 ≤ ((Gᶜ.neighborFinset p).filter (G.Adj y)).card) : x = y := by
  classical
  by_contra ne
  let A := G.neighborFinset p
  let C := Gᶜ.neighborFinset p
  let B := (A.erase x).erase y
  have ymem : y ∈ A.erase x := Finset.mem_erase.mpr ⟨ne.symm,hy⟩
  have cb : B.card = 11 := by
    change ((A.erase x).erase y).card = 11
    rw [Finset.card_erase_of_mem ymem,Finset.card_erase_of_mem hx]
    change (G.neighborFinset p).card - 1 - 1 = 11
    rw [SimpleGraph.card_neighborFinset_eq_degree,hp]
  have ba : B ⊆ A := (Finset.erase_subset _ _).trans (Finset.erase_subset _ _)
  obtain ⟨a,ham,b,hbm,ab,miss⟩ : ∃ a ∈ B, ∃ b ∈ B, a ≠ b ∧ ¬G.Adj a b := by
    by_contra no
    have cl : G.IsClique (B : Set V) := by
      intro a ham b hbm ab
      by_contra miss
      exact no ⟨a,ham,b,hbm,ab,miss⟩
    have bound := cover_shell_target_clique_cap G ha p B ba cl
    omega
  let I := ({x,y} : Finset V) ∪ {a,b}
  have inner (w : V) (hw : w ∈ B) : w ≠ x ∧ w ≠ y := by
    obtain ⟨hwy,hw⟩ := Finset.mem_erase.mp hw
    exact ⟨(Finset.mem_erase.mp hw).1,hwy⟩
  obtain ⟨ax,ay⟩ := inner a ham
  obtain ⟨bx,by'⟩ := inner b hbm
  have dj : Disjoint ({x,y} : Finset V) {a,b} := by
    simp [Finset.disjoint_left,ax,ay,bx,by',Ne.symm ax,Ne.symm ay,Ne.symm bx,Ne.symm by']
  have size : I.card = 4 := by
    rw [Finset.card_union_of_disjoint dj,Finset.card_pair ne,Finset.card_pair ab]
  have sub : I ⊆ A := by
    intro w hw
    rcases Finset.mem_union.mp hw with h|h
    · simp only [Finset.mem_insert,Finset.mem_singleton] at h
      rcases h with rfl|rfl <;> assumption
    · simp only [Finset.mem_insert,Finset.mem_singleton] at h
      rcases h with rfl|rfl
      · exact ba ham
      · exact ba hbm
  have outside (w : V) (hw : w ∈ A) : w ∉ C := fun hc =>
    ((SimpleGraph.compl_adj G p w).mp ((SimpleGraph.mem_neighborFinset Gᶜ p w).mp hc)).2
      ((SimpleGraph.mem_neighborFinset G p w).mp hw)
  have edge := cover_h13_EDGE13 G hv ha p hp he a b ab miss (outside _ (ba ham)) (outside _ (ba hbm))
  have pair := Finset.card_union_le (C.filter (G.Adj a)) (C.filter (G.Adj b))
  change 13 ≤ ((C.filter (G.Adj a)) ∪ (C.filter (G.Adj b))).card at edge
  have cap := cover_low_charge_shell_turan G hv ha hd p hp hq I sub
  rw [size] at cap
  norm_num at cap
  have led := cover_shell_subset_charge G p hp hd I sub
  dsimp only at led
  rw [adjCount_eq_sum_filter,Finset.sum_union dj,Finset.sum_pair ne,Finset.sum_pair ab] at led
  dsimp only [C] at edge pair
  omega

/-- A set left after deleting one shell vertex contains a missing triangle
or two disjoint missing edges: every further one-vertex deletion still
leaves eleven points and hence contains a missing edge. -/
theorem cover_twelve_triangle_or_matching (G : SimpleGraph V) (ha : CoreAdmissible 5 G)
    (p : V) (B : Finset V) (cb : B.card = 12) (sub : B ⊆ G.neighborFinset p) :
    (∃ a ∈ B, ∃ b ∈ B, ∃ c ∈ B, a ≠ b ∧ b ≠ c ∧ a ≠ c ∧
       ¬G.Adj a b ∧ ¬G.Adj b c ∧ ¬G.Adj a c) ∨
    ∃ a ∈ B, ∃ b ∈ B, ∃ c ∈ B, ∃ d ∈ B, a ≠ b ∧ c ≠ d ∧
       Disjoint ({a,b} : Finset V) {c,d} ∧ ¬G.Adj a b ∧ ¬G.Adj c d := by
  classical
  have edge (T : Finset V) (ts : T ⊆ B) (ct : 11 ≤ T.card) :
      ∃ a ∈ T, ∃ b ∈ T, a ≠ b ∧ ¬G.Adj a b := by
    by_contra no
    have cap := cover_shell_target_clique_cap G ha p T (ts.trans sub) (by
      intro a ha b hb ab
      by_contra miss
      exact no ⟨a,ha,b,hb,ab,miss⟩)
    omega
  have erased (u : V) (hu : u ∈ B) := edge (B.erase u) (Finset.erase_subset _ _)
    (by rw [Finset.card_erase_of_mem hu,cb]; decide)
  obtain ⟨a,aa,b,bb,ab,mab⟩ := edge B (fun _ h => h) (by omega)
  by_cases matching : ∃ u ∈ B, ∃ v ∈ B, ∃ w ∈ B, ∃ t ∈ B, u ≠ v ∧ w ≠ t ∧
       Disjoint ({u,v} : Finset V) {w,t} ∧ ¬G.Adj u v ∧ ¬G.Adj w t
  · exact Or.inr matching
  left
  have meet (u v w t : V) (hu : u ∈ B) (hv : v ∈ B) (hw : w ∈ B) (ht : t ∈ B)
      (uv : u ≠ v) (wt : w ≠ t) (m1 : ¬G.Adj u v) (m2 : ¬G.Adj w t) :
      u = w ∨ u = t ∨ v = w ∨ v = t := by
    by_contra! h
    exact matching ⟨u,hu,v,hv,w,hw,t,ht,uv,wt,by
      simp [Finset.disjoint_left,h.1,h.2.1,h.2.2.1,h.2.2.2,
        Ne.symm h.1,Ne.symm h.2.1,Ne.symm h.2.2.1,Ne.symm h.2.2.2],m1,m2⟩
  have other (u v : V) (hu : u ∈ B) (hv : v ∈ B) (uv : u ≠ v) (muv : ¬G.Adj u v) :
      ∃ w ∈ B, w ≠ u ∧ w ≠ v ∧ ¬G.Adj v w := by
    obtain ⟨s,hs,t,ht,st,mst⟩ := erased u hu
    obtain ⟨su,hs⟩ := Finset.mem_erase.mp hs
    obtain ⟨tu,ht⟩ := Finset.mem_erase.mp ht
    rcases meet u v s t hu hv hs ht uv st muv mst with eq|eq|eq|eq
    · exact (su eq.symm).elim
    · exact (tu eq.symm).elim
    · subst s; exact ⟨t,ht,tu,st.symm,mst⟩
    · subst t; exact ⟨s,hs,su,st,fun e => mst e.symm⟩
  obtain ⟨s,hs,sa,sb,mbs⟩ := other a b aa bb ab mab
  obtain ⟨t,ht,tb,ta,mat⟩ := other b a bb aa ab.symm (fun e => mab e.symm)
  have st : s = t := by
    rcases meet b s a t bb hs aa ht sb.symm ta.symm mbs mat with eq|eq|eq|eq
    · exact (ab eq.symm).elim
    · exact (tb eq.symm).elim
    · exact (sa eq).elim
    · exact eq
  subst t
  exact ⟨a,aa,b,bb,s,hs,ab,sb.symm,sa.symm,mab,mbs,mat⟩

/-- Add a separate hub to a group of shell rows and charge their exact
incidences against the K4-free capacity of the resulting set. -/
theorem cover_hub_row_budget (G : SimpleGraph V) (hv : Fintype.card V = 61)
    (ha : CoreAdmissible 5 G) (hd : ∀ z, 13 ≤ G.degree z) (p : V) (hp : G.degree p = 13)
    (hq : coreInducedEdgeCount Gᶜ (G.neighborFinset p) +
      (∑ z ∈ G.neighborFinset p, (G.degree z - 13)) ≤ 29)
    (x : V) (hx : x ∈ G.neighborFinset p) (T : Finset V) (xt : x ∉ T)
    (sub : T ⊆ G.neighborFinset p) :
    ((Gᶜ.neighborFinset p).filter (G.Adj x)).card + adjCount G T (Gᶜ.neighborFinset p) ≤
      29 + (T.card + 1)^2 / 3 := by
  classical
  have incl : insert x T ⊆ G.neighborFinset p := Finset.insert_subset hx sub
  have cap := cover_low_charge_shell_turan G hv ha hd p hp hq _ incl
  rw [Finset.card_insert_of_notMem xt] at cap
  have led := cover_shell_subset_charge G p hp hd _ incl
  dsimp only at led
  rw [adjCount_eq_sum_filter,Finset.sum_insert xt] at led
  rw [adjCount_eq_sum_filter]
  omega

end EG617
