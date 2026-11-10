module

public import EG617.Frontend.HereditaryCaps

@[expose] public section

set_option autoImplicit false
attribute [local instance] Classical.propDecidable

universe u
namespace EG617
variable {V : Type u}

/-- Exact finite-set form of the paper's independence-number bound. -/
def CoreIndependenceBound (a : ℕ) (G : SimpleGraph V) : Prop :=
  ∀ S : Finset V, G.IsIndepSet (S : Set V) → S.card ≤ a

/-- Exact finite-set form of the paper's clique-number bound. -/
def CoreCliqueBound (k : ℕ) (G : SimpleGraph V) : Prop :=
  ∀ S : Finset V, G.IsClique (S : Set V) → S.card ≤ k

noncomputable def coreInducedEdgeCount (G : SimpleGraph V) (S : Finset V) : ℕ := by
  classical
  exact (G.induce (S : Set V)).edgeFinset.card

/-- The frozen R(a,n) contract includes the cap on EVERY induced vertex set. -/
def CoreAdmissible (a : ℕ) (G : SimpleGraph V) : Prop :=
  CoreIndependenceBound a G ∧ CoreCliqueBound 11 G ∧
    ∀ S : Finset V, coreInducedEdgeCount G S ≤ D S.card

theorem core_induced_edge_count_univ [Fintype V] (G : SimpleGraph V) :
    coreInducedEdgeCount G Finset.univ = G.edgeFinset.card := by
  classical
  let e : G.induce (↑(Finset.univ : Finset V)) ≃g G :=
    { toEquiv :=
        { toFun := fun v => v.val
          invFun := fun v => ⟨v, Finset.mem_univ v⟩
          left_inv := fun _ => Subtype.ext rfl
          right_inv := fun _ => rfl }
      map_rel_iff' := by intro x y; rfl }
  exact e.card_edgeFinset_eq

theorem core_independenceBound_induce (G : SimpleGraph V) (a : ℕ)
    (hG : CoreIndependenceBound a G) (S : Finset V) :
    CoreIndependenceBound a (G.induce (S : Set V)) := by
  classical
  intro T hT
  have hI : G.IsIndepSet (↑(T.image fun x : S => (x : V))) := by
    intro x hx y hy hxy
    obtain ⟨x', hx', rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨y', hy', rfl⟩ := Finset.mem_image.mp hy
    exact hT hx' hy' (fun h => hxy (congrArg Subtype.val h))
  have h := hG (T.image fun x : S => (x : V)) hI
  have he : Function.Injective (fun x : S => (x : V)) := Subtype.val_injective
  rw [Finset.card_image_of_injective T he] at h
  exact h

theorem core_cliqueBound_induce (G : SimpleGraph V) (k : ℕ)
    (hG : CoreCliqueBound k G) (S : Finset V) :
    CoreCliqueBound k (G.induce (S : Set V)) := by
  classical
  intro T hT
  have hI : G.IsClique (↑(T.image fun x : S => (x : V))) := by
    intro x hx y hy hxy
    obtain ⟨x', hx', rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨y', hy', rfl⟩ := Finset.mem_image.mp hy
    exact hT hx' hy' (fun h => hxy (congrArg Subtype.val h))
  have h := hG (T.image fun x : S => (x : V)) hI
  have he : Function.Injective (fun x : S => (x : V)) := Subtype.val_injective
  rw [Finset.card_image_of_injective T he] at h
  exact h

/-- A nonneighborhood reduces the allowed independence size by one.
No degree, edge-floor or terminal theorem is assumed. -/
theorem core_independence_nonNeighbors (G : SimpleGraph V) (a : ℕ)
    (hG : CoreIndependenceBound (a + 1) G) (v : V) (S : Finset V)
    (hS : ∀ w ∈ S, w ≠ v ∧ ¬ G.Adj v w) (hind : G.IsIndepSet (S : Set V)) :
    S.card ≤ a := by
  classical
  have hv : v ∉ S := fun h => (hS v h).1 rfl
  have hi : G.IsIndepSet (↑(insert v S)) := by
    intro x hx y hy hxy
    by_cases hxv : x = v
    · subst x
      have hyv : y ≠ v := Ne.symm hxy
      exact (hS y (Finset.mem_of_mem_insert_of_ne hy hyv)).2
    · have hxS : x ∈ S := Finset.mem_of_mem_insert_of_ne hx hxv
      by_cases hyv : y = v
      · subst y
        exact fun h => (hS x hxS).2 h.symm
      · exact hind hxS (Finset.mem_of_mem_insert_of_ne hy hyv) hxy
  have hb := hG (insert v S) hi
  rw [Finset.card_insert_of_notMem hv] at hb
  omega

theorem core_compl_edge_count [Fintype V] (G : SimpleGraph V) :
    G.edgeFinset.card + Gᶜ.edgeFinset.card = (Fintype.card V).choose 2 := by
  classical
  have hd : Disjoint G.edgeFinset Gᶜ.edgeFinset :=
    SimpleGraph.disjoint_edgeFinset.mpr disjoint_compl_right
  have hu : G.edgeFinset ∪ Gᶜ.edgeFinset = (⊤ : SimpleGraph V).edgeFinset := by
    ext e
    refine Sym2.inductionOn e ?_
    intro x y
    simp only [Finset.mem_union, SimpleGraph.mem_edgeFinset,
      SimpleGraph.mem_edgeSet, SimpleGraph.compl_adj, SimpleGraph.top_adj]
    constructor
    · rintro (h | h)
      · exact h.ne
      · exact h.1
    · intro h
      by_cases ha : G.Adj x y
      · exact Or.inl ha
      · exact Or.inr ⟨h, ha⟩
  rw [← Finset.card_union_of_disjoint hd, hu,
    SimpleGraph.card_edgeFinset_top_eq_card_choose_two]

/-- Nested induced sets have exactly the same edges as their image in the parent. -/
theorem core_induced_edge_count_image (G : SimpleGraph V) (S : Finset V)
    (T : Finset S) :
    coreInducedEdgeCount (G.induce (S : Set V)) T =
      coreInducedEdgeCount G (T.image fun x : S => (x : V)) := by
  classical
  let U := T.image fun x : S => (x : V)
  let f : T → U := fun x => ⟨x.val.val, Finset.mem_image.mpr ⟨x.val, x.property, rfl⟩⟩
  have hf : Function.Bijective f := by
    constructor
    · intro x y h
      apply Subtype.ext
      apply Subtype.ext
      exact congrArg (fun z : U => (z : V)) h
    · intro y
      obtain ⟨x, hx, he⟩ := Finset.mem_image.mp y.property
      exact ⟨⟨x, hx⟩, Subtype.ext he⟩
  let e : (G.induce (S : Set V)).induce (T : Set S) ≃g G.induce (U : Set V) :=
    { toEquiv := Equiv.ofBijective f hf
      map_rel_iff' := by intro x y; rfl }
  exact e.card_edgeFinset_eq

/-- All three frozen R(a,n) conditions are hereditary, including every cap. -/
theorem core_admissible_induce (G : SimpleGraph V) (a : ℕ)
    (hG : CoreAdmissible a G) (S : Finset V) :
    CoreAdmissible a (G.induce (S : Set V)) := by
  classical
  refine ⟨core_independenceBound_induce G a hG.1 S,
    core_cliqueBound_induce G 11 hG.2.1 S, ?_⟩
  intro T
  rw [core_induced_edge_count_image]
  have h := hG.2.2 (T.image fun x : S => (x : V))
  have he : Function.Injective (fun x : S => (x : V)) := Subtype.val_injective
  rw [Finset.card_image_of_injective T he] at h
  exact h

/-- A target definition, NOT a proof of the GATE47 theorem. -/
def Gate47Statement : Prop :=
  ∀ G : SimpleGraph (Fin 47), CoreAdmissible 4 G → G.edgeFinset.card ≤ 286 →
    ∀ v : Fin 47, 12 ≤ G.degree v

end EG617
