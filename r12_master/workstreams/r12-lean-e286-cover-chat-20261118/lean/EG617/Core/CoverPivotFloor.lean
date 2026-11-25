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

end EG617
