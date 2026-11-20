module
public import EG617.Core.E286DisjointPairs

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Alpha4 forces an edge between two distinct vertices anticomplete to an
actual independent three-set. -/
theorem e286_independent_three_forces_edge (G : SimpleGraph V) (hG : E286Hypotheses G)
    (J : Finset V) (hc : J.card = 3) (hJ : G.IsIndepSet (J : Set V))
    (x y : V) (hxy : x ≠ y) (hx : x ∉ J) (hy : y ∉ J)
    (hxJ : ∀ t ∈ J, ¬ G.Adj x t) (hyJ : ∀ t ∈ J, ¬ G.Adj y t) : G.Adj x y := by
  classical
  by_contra hn
  have hI : G.IsIndepSet ((insert x J : Finset V) : Set V) := by
    rw [Finset.coe_insert]
    exact hJ.insert (fun t ht _ => ⟨hxJ t ht, fun h => hxJ t ht h.symm⟩)
  have ha : ∀ t ∈ insert x J, t ≠ y ∧ ¬ G.Adj y t := by
    intro t ht
    rcases Finset.mem_insert.mp ht with he | ht
    · subst t
      exact ⟨hxy, fun h => hn h.symm⟩
    · exact ⟨fun he => hy (he ▸ ht), hyJ t ht⟩
  have hb := core_independence_nonNeighbors G 3 hG.2.2.2.1 y _ ha hI
  rw [Finset.card_insert_of_notMem hx, hc] at hb
  omega

/-- The analytic core of frozen Section4. After choosing a vertex in one
missing set, the two other missing sets have size>=5 and total size>=13.
Deleting at most four neighbors leaves complete cross sets of total size>=9,
contradicting the same four-external-neighbor capacity at their vertices. -/
theorem e286_ordered_three_cliques_obstruction (G : SimpleGraph V) (hG : E286Hypotheses G)
    (K L M : Finset V) (hK : G.IsClique (K : Set V))
    (hL : G.IsClique (L : Set V)) (hM : G.IsClique (M : Set V))
    (hcK : K.card = 11) (hcL : L.card = 11) (hcM : M.card = 11)
    (hKL : Disjoint K L) (hKM : Disjoint K M) (hLM : Disjoint L M)
    (z s : V) (hzs : z ≠ s) (hnzs : ¬ G.Adj z s)
    (hzK : z ∉ K) (hzL : z ∉ L) (hzM : z ∉ M)
    (hsK : s ∉ K) (hsL : s ∉ L) (hsM : s ∉ M)
    (hanti : ∀ v ∈ K ∪ L ∪ M, ¬ G.Adj v s)
    (hbound : ∀ v ∈ K ∪ L ∪ M, degreeExcess12 G v ≤ 2)
    (hA : (K.filter (fun v => ¬ G.Adj z v)).Nonempty)
    (hB : 5 ≤ (L.filter (fun v => ¬ G.Adj z v)).card)
    (hC : 5 ≤ (M.filter (fun v => ¬ G.Adj z v)).card)
    (hBC : 13 ≤ (L.filter (fun v => ¬ G.Adj z v)).card +
      (M.filter (fun v => ¬ G.Adj z v)).card) : False := by
  classical
  let B := L.filter (fun v => ¬ G.Adj z v)
  let C := M.filter (fun v => ¬ G.Adj z v)
  have hBL : B ⊆ L := Finset.filter_subset _ _
  have hCM : C ⊆ M := Finset.filter_subset _ _
  have hBCall : Disjoint B C := hLM.mono hBL hCM
  obtain ⟨x, hx⟩ := hA
  have hxK := (Finset.mem_filter.mp hx).1
  have hzx := (Finset.mem_filter.mp hx).2
  have hxU : x ∈ K ∪ L ∪ M := Finset.mem_union_left _ (Finset.mem_union_left _ hxK)
  have hxs := hanti x hxU
  have hxbound := hbound x hxU
  have hKN : Disjoint K ((B ∪ C).filter (G.Adj x)) := by
    apply (Finset.disjoint_union_right.mpr ⟨hKL.mono_right hBL, hKM.mono_right hCM⟩).mono_right
    exact Finset.filter_subset _ _
  have hcap := e286_clique_blocker_vertex_charge G K _ hK hKN x hxK
    (fun _ hv => (Finset.mem_filter.mp hv).2)
  rw [hcK, Finset.filter_union,
    Finset.card_union_of_disjoint (hBCall.mono (Finset.filter_subset _ _) (Finset.filter_subset _ _))] at hcap
  let B' := B.filter (fun v => ¬ G.Adj x v)
  let C' := C.filter (fun v => ¬ G.Adj x v)
  have hbpart := Finset.card_filter_add_card_filter_not (s := B) (G.Adj x)
  have hcpart := Finset.card_filter_add_card_filter_not (s := C) (G.Adj x)
  change 5 ≤ B.card at hB
  change 5 ≤ C.card at hC
  change 13 ≤ B.card + C.card at hBC
  change (B.filter (G.Adj x)).card + B'.card = B.card at hbpart
  change (C.filter (G.Adj x)).card + C'.card = C.card at hcpart
  have hbpos : 0 < B'.card := by omega
  have hcpos : 0 < C'.card := by omega
  have hsum : 9 ≤ B'.card + C'.card := by omega
  let J : Finset V := insert x {z, s}
  have hxpair : x ∉ ({z, s} : Finset V) := by
    simp only [Finset.mem_insert, Finset.mem_singleton, not_or]
    exact ⟨fun he => hzK (he ▸ hxK), fun he => hsK (he ▸ hxK)⟩
  have hJcard : J.card = 3 := by
    dsimp only [J]
    rw [Finset.card_insert_of_notMem hxpair, Finset.card_pair hzs]
  have hpair : G.IsIndepSet (({z, s} : Finset V) : Set V) := by
    simpa only [Finset.coe_insert, Finset.coe_singleton] using
      (Set.pairwise_pair.mpr (fun _ => ⟨hnzs, fun h => hnzs h.symm⟩) :
        G.IsIndepSet ({z, s} : Set V))
  have hJ : G.IsIndepSet (J : Set V) := by
    change G.IsIndepSet ((insert x {z, s} : Finset V) : Set V)
    rw [Finset.coe_insert]
    apply hpair.insert
    intro t ht _
    rcases Finset.mem_insert.mp ht with he | ht
    · subst t
      exact ⟨fun h => hzx h.symm, hzx⟩
    · have he := Finset.mem_singleton.mp ht
      subst t
      exact ⟨hxs, fun h => hxs h.symm⟩
  have haway (P : Finset V) (hKP : Disjoint K P) (hzP : z ∉ P) (hsP : s ∉ P)
      (v : V) (hvP : v ∈ P) (hvs : ¬ G.Adj v s)
      (hxv : ¬ G.Adj x v) (hzv : ¬ G.Adj z v) :
      v ∉ J ∧ ∀ t ∈ J, ¬ G.Adj v t := by
    constructor
    · intro hvJ
      rcases Finset.mem_insert.mp hvJ with he | hvJ
      · subst v
        exact Finset.disjoint_left.mp hKP hxK hvP
      · rcases Finset.mem_insert.mp hvJ with he | hvJ
        · subst v
          exact hzP hvP
        · have he := Finset.mem_singleton.mp hvJ
          subst v
          exact hsP hvP
    · intro t ht
      rcases Finset.mem_insert.mp ht with he | ht
      · subst t
        exact fun h => hxv h.symm
      · rcases Finset.mem_insert.mp ht with he | ht
        · subst t
          exact fun h => hzv h.symm
        · have he := Finset.mem_singleton.mp ht
          subst t
          exact hvs
  have hB'L : B' ⊆ L := (Finset.filter_subset _ _).trans hBL
  have hC'M : C' ⊆ M := (Finset.filter_subset _ _).trans hCM
  have hedge (y : V) (hy : y ∈ B') (w : V) (hw : w ∈ C') : G.Adj y w := by
    have hyL := hB'L hy
    have hwM := hC'M hw
    have hyU : y ∈ K ∪ L ∪ M := Finset.mem_union_left _ (Finset.mem_union_right _ hyL)
    have hwU : w ∈ K ∪ L ∪ M := Finset.mem_union_right _ hwM
    have hay := haway L hKL hzL hsL y hyL (hanti y hyU)
      (Finset.mem_filter.mp hy).2 (Finset.mem_filter.mp (Finset.mem_filter.mp hy).1).2
    have haw := haway M hKM hzM hsM w hwM (hanti w hwU)
      (Finset.mem_filter.mp hw).2 (Finset.mem_filter.mp (Finset.mem_filter.mp hw).1).2
    have hyw : y ≠ w := by
      intro he
      subst w
      exact Finset.disjoint_left.mp hLM hyL hwM
    exact e286_independent_three_forces_edge G hG J hJcard hJ y w hyw hay.1 haw.1 hay.2 haw.2
  obtain ⟨y, hy⟩ := Finset.card_pos.mp hbpos
  obtain ⟨w, hw⟩ := Finset.card_pos.mp hcpos
  have hycap := e286_clique_blocker_vertex_charge G L C' hL (hLM.mono_right hC'M)
    y (hB'L hy) (hedge y hy)
  have hwcap := e286_clique_blocker_vertex_charge G M B' hM (hLM.symm.mono_right hB'L)
    w (hC'M hw) (fun v hv => (hedge v hv w hw).symm)
  have hybound := hbound y (Finset.mem_union_left _ (Finset.mem_union_right _ (hB'L hy)))
  have hwbound := hbound w (Finset.mem_union_right _ (hC'M hw))
  rw [hcL] at hycap
  rw [hcM] at hwcap
  omega

end EG617
