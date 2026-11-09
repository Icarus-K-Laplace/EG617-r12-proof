module

public import EG617.Frontend.EdgeCounting
public import EG617.Combinatorics.TuranArithmetic

@[expose] public section

set_option autoImplicit false

namespace EG617

/-- On any induced vertex set, the complement of a color graph has no 13-clique.
The only coloring assumption is the original `ValidColoring` predicate. -/
theorem inducedColorGraph_compl_cliqueFree (c : EdgeColoring)
    (hc : ValidColoring c) (i : Color) (S : Finset Vertex) :
    (inducedColorGraph c i S)ᶜ.CliqueFree 13 := by
  classical
  intro t ht
  have hi : (inducedColorGraph c i S).IsNIndepSet 13 t :=
    SimpleGraph.isNClique_compl.mp ht
  have hind : ∀ u ∈ t.image (fun x : S => (x : Vertex)),
      ∀ v ∈ t.image (fun x : S => (x : Vertex)),
        ¬ (colorGraph c i).Adj u v := by
    intro u hu v hv
    obtain ⟨u', hu', rfl⟩ := Finset.mem_image.mp hu
    obtain ⟨v', hv', rfl⟩ := Finset.mem_image.mp hv
    by_cases huv : u' = v'
    · subst v'
      exact (colorGraph c i).loopless.irrefl (u' : Vertex)
    · change ¬ (inducedColorGraph c i S).Adj u' v'
      exact hi.isIndepSet hu' hv' huv
  have hcard : (t.image (fun x : S => (x : Vertex))).card = 13 := by
    rw [Finset.card_image_of_injective t Subtype.val_injective]
    exact hi.card_eq
  have hbound := independent_card_le_twelve c hc
    (t.image (fun x : S => (x : Vertex))) i hind
  rw [hcard] at hbound
  exact (by decide : ¬ (13 ≤ 12)) hbound

/-- The exact Turan-complement lower bound for every finite induced vertex set.
The cutoff needed in `tau12_add_turanNumber` follows from `Vertex = Fin 145`;
no density or terminal conclusion is assumed. -/
theorem tau12_le_colorEdgeCount (c : EdgeColoring) (hc : ValidColoring c)
    (i : Color) (S : Finset Vertex) :
    tau12 S.card ≤ colorEdgeCount c i S := by
  classical
  let G : SimpleGraph S := inducedColorGraph c i S
  have hcf : Gᶜ.CliqueFree (12 + 1) :=
    inducedColorGraph_compl_cliqueFree c hc i S
  have hcomp : Gᶜ.edgeFinset.card ≤ SimpleGraph.turanNumber S.card 12 := by
    simpa only [Fintype.card_coe] using hcf.card_edgeFinset_le
  have hd : Disjoint G.edgeFinset Gᶜ.edgeFinset :=
    SimpleGraph.disjoint_edgeFinset.mpr disjoint_compl_right
  have htotal : G.edgeFinset.card + Gᶜ.edgeFinset.card = Nat.choose S.card 2 := by
    calc
      G.edgeFinset.card + Gᶜ.edgeFinset.card =
          (G.edgeFinset ∪ Gᶜ.edgeFinset).card :=
        (Finset.card_union_of_disjoint hd).symm
      _ = (⊤ : SimpleGraph S).edgeFinset.card := by
        rw [← SimpleGraph.edgeFinset_sup, sup_compl_eq_top]
      _ = Nat.choose S.card 2 := by
        simpa only [Fintype.card_coe] using
          (SimpleGraph.card_edgeFinset_top_eq_card_choose_two (V := S))
  have hsize : S.card ≤ 145 := by
    simpa only [Vertex, Fintype.card_fin] using S.card_le_univ
  have hnum := tau12_add_turanNumber S.card hsize
  have hsum : tau12 S.card + SimpleGraph.turanNumber S.card 12 ≤
      G.edgeFinset.card + SimpleGraph.turanNumber S.card 12 := by
    calc
      tau12 S.card + SimpleGraph.turanNumber S.card 12 = Nat.choose S.card 2 := hnum
      _ = G.edgeFinset.card + Gᶜ.edgeFinset.card := htotal.symm
      _ ≤ G.edgeFinset.card + SimpleGraph.turanNumber S.card 12 :=
        Nat.add_le_add_left hcomp _
  change tau12 S.card ≤ G.edgeFinset.card
  exact (Nat.add_le_add_iff_right).mp hsum

end EG617