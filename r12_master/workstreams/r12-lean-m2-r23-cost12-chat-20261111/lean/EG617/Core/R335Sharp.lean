module
public import EG617.Core.R335Fourteen

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Frozen M4: the degree-eleven case is impossible in the original full
R(3,35) class. The Cost-6 witness and the fourteen-set are both derived here. -/
theorem core_R335_degree_ne_eleven (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G) (v : V) :
    G.degree v ≠ 11 := by
  classical
  intro hd
  obtain ⟨x, hx, y, hy, hxy, hnxy⟩ := core_degree_eleven_neighbor_nonedge G hG.2.1 v hd
  let S := Gᶜ.neighborFinset v
  have houtside (w : V) (hw : w ∈ G.neighborFinset v) : w ∉ S := by
    intro hs
    have hcomp := (SimpleGraph.compl_adj G v w).mp
      ((SimpleGraph.mem_neighborFinset Gᶜ v w).mp hs)
    exact hcomp.2 ((SimpleGraph.mem_neighborFinset G v w).mp hw)
  have hxS := houtside x hx
  have hyS := houtside y hy
  let J := S.filter (fun z => ¬ G.Adj x z ∧ ¬ G.Adj y z)
  have hJ : G.IsClique (J : Set V) := by
    apply core_common_nonneighbors_clique G hG.1 x y hxy hnxy J
    intro z hz
    obtain ⟨hzS, hzx, hzy⟩ := Finset.mem_filter.mp hz
    exact ⟨fun he => hxS (he ▸ hzS), fun he => hyS (he ▸ hzS), hzx, hzy⟩
  let I : Finset (S : Set V) := Finset.univ.filter
    (fun z => ¬ G.Adj x z ∧ ¬ G.Adj y z)
  have hI : (G.induce (S : Set V))ᶜ.IsIndepSet (I : Set (S : Set V)) := by
    intro a ha b hb hab hadj
    have haJ : (a : V) ∈ J := Finset.mem_filter.mpr ⟨a.property, (Finset.mem_filter.mp ha).2⟩
    have hbJ : (b : V) ∈ J := Finset.mem_filter.mpr ⟨b.property, (Finset.mem_filter.mp hb).2⟩
    have hGadj := hJ haJ hbJ (fun he => hab (Subtype.ext he))
    exact ((SimpleGraph.compl_adj (G.induce (S : Set V)) a b).mp hadj).2 hGadj
  obtain ⟨T, hT, hcost⟩ := core_R335_degree_eleven_nonneighbor_cost_six G hV hG v hd I hI
  let U : Finset V := T.image (fun z : (S : Set V) => (z : V))
  have hU : U.card = 12 := by
    rw [Finset.card_image_of_injective _ Subtype.val_injective]
    exact hT
  have hUS : U ⊆ S := by
    intro z hz
    obtain ⟨a, _, rfl⟩ := Finset.mem_image.mp hz
    exact a.property
  have hxU : x ∉ U := fun hxU => hxS (hUS hxU)
  have hyU : y ∉ U := fun hyU => hyS (hUS hyU)
  have hf : (T ∩ I).image (fun z : (S : Set V) => (z : V)) =
      U.filter (fun z => ¬ G.Adj x z ∧ ¬ G.Adj y z) := by
    ext z
    simp only [U, I, Finset.mem_image, Finset.mem_inter, Finset.mem_filter,
      Finset.mem_univ, true_and]
    constructor
    · rintro ⟨a, ⟨ha, hP⟩, rfl⟩
      exact ⟨⟨a, ha, rfl⟩, hP⟩
    · rintro ⟨⟨a, ha, rfl⟩, hP⟩
      exact ⟨a, ⟨ha, hP⟩, rfl⟩
  have hfc := congrArg Finset.card hf
  rw [Finset.card_image_of_injective _ Subtype.val_injective] at hfc
  have hinst : @Inter.inter (Finset (S : Set V))
      (@Finset.instInter (S : Set V) (fun a b => Classical.propDecidable (a = b))) T I = T ∩ I := by
    ext z
    simp only [Finset.mem_inter]
  rw [hinst] at hcost
  change coreInducedEdgeCount ((G.induce (S : Set V))ᶜ) T + (T ∩ I).card ≤ 6 at hcost
  rw [core_induce_compl, core_induced_edge_count_image, hfc] at hcost
  exact core_fourteen_cost_obstruction G hG.2.2 U hU x y hxy hxU hyU hcost

theorem core_R335_degree_ge_twelve (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G) (v : V) :
    12 ≤ G.degree v := by
  have hbound := core_R3_card_le_degree_add_24 G hG v
  have hne := core_R335_degree_ne_eleven G hV hG v
  omega

theorem core_R335_edges_ge_210 (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G) :
    210 ≤ G.edgeFinset.card := by
  classical
  have hsum : ∑ v : V, 12 ≤ ∑ v : V, G.degree v :=
    Finset.sum_le_sum (fun v _ => core_R335_degree_ge_twelve G hV hG v)
  have he := G.sum_degrees_eq_twice_card_edges
  simp only [Finset.sum_const, Finset.card_univ, smul_eq_mul, hV] at hsum
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at he ⊢
  omega

end EG617
