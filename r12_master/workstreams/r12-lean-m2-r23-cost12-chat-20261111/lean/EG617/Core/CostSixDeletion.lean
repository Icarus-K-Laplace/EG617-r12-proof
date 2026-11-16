module
public import EG617.Core.CostSixProfiles

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
universe u
variable {V : Type u} [Fintype V]

theorem coreInducedEdgeCount_mono_graph (G H : SimpleGraph V) (h : G ≤ H)
    (T : Finset V) : coreInducedEdgeCount G T ≤ coreInducedEdgeCount H T := by
  classical
  unfold coreInducedEdgeCount
  apply Finset.card_le_card
  apply SimpleGraph.edgeFinset_mono
  intro x y hxy
  exact h hxy

/-- An independent set gains an edge only if it contains both added endpoints. -/
theorem independent_sup_edge_or_endpoints (G : SimpleGraph V) (u v : V)
    (I : Finset V) (hI : G.IsIndepSet (I : Set V)) :
    (G ⊔ SimpleGraph.edge u v).IsIndepSet (I : Set V) ∨ (u ∈ I ∧ v ∈ I) := by
  classical
  by_cases hu : u ∈ I
  · by_cases hv : v ∈ I
    · exact Or.inr ⟨hu, hv⟩
    left
    intro x hx y hy hxy he
    rcases he with he | he
    · exact hI hx hy hxy he
    · rcases ((SimpleGraph.edge_adj _ _).mp he).1 with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩
      · exact hv hy
      · exact hv hx
  · left
    intro x hx y hy hxy he
    rcases he with he | he
    · exact hI hx hy hxy he
    · rcases ((SimpleGraph.edge_adj _ _).mp he).1 with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩
      · exact hu hx
      · exact hu hy

/-- In an originally independent set, every neighbor of a fixed vertex after
one edge addition must be the other endpoint; there is at most one. -/
theorem independent_sup_edge_neighbor_card (G : SimpleGraph V) (u v : V)
    (I S : Finset V) (hI : G.IsIndepSet (I : Set V)) (w : V) (hw : w ∈ I)
    (hS : ∀ x ∈ S, x ∈ I ∧ (G ⊔ SimpleGraph.edge u v).Adj w x) : S.card ≤ 1 := by
  classical
  apply Finset.card_le_one.mpr
  intro x hx y hy
  obtain ⟨hxI, hxH⟩ := hS x hx
  obtain ⟨hyI, hyH⟩ := hS y hy
  have hxE : (SimpleGraph.edge u v).Adj w x := hxH.resolve_left (hI hw hxI hxH.ne)
  have hyE : (SimpleGraph.edge u v).Adj w y := hyH.resolve_left (hI hw hyI hyH.ne)
  have hneuv : u ≠ v := by
    rintro rfl
    simpa [SimpleGraph.edge_adj] using hxE
  rcases ((SimpleGraph.edge_adj _ _).mp hxE).1 with ⟨hwu, hxv⟩ | ⟨hwv, hxu⟩
  · rcases ((SimpleGraph.edge_adj _ _).mp hyE).1 with ⟨_, hyv⟩ | ⟨hwv, _⟩
    · exact hxv.trans hyv.symm
    · exact False.elim (hneuv (hwu.symm.trans hwv))
  · rcases ((SimpleGraph.edge_adj _ _).mp hyE).1 with ⟨hwu, _⟩ | ⟨_, hyu⟩
    · exact False.elim (hneuv (hwu.symm.trans hwv))
    · exact hxu.trans hyu.symm

/-- Case I admits Cost-6 after any single edge deletion. The proof also covers
the singleton-to-singleton deletion, without needing an independence cap. -/
theorem case_I_single_edge_deletion_cost_six (G : SimpleGraph V) (u v : V)
    (hne : u ≠ v) (h : R23CaseIProfile (G ⊔ SimpleGraph.edge u v)) :
    CostSixProperty G := by
  classical
  let H := G ⊔ SimpleGraph.edge u v
  have hle : G ≤ H := le_sup_left
  intro I hI
  rcases independent_sup_edge_or_endpoints G u v I hI with hHI | ⟨huI, hvI⟩
  · obtain ⟨T, hT, he⟩ := case_I_cost_six H h I hHI
    exact ⟨T, hT, le_trans (Nat.add_le_add_right
      (coreInducedEdgeCount_mono_graph G H hle T) _) he⟩
  obtain ⟨t, c, A, B, hp, hn0, hn1, hn2, hn3, hn4, hAB, _⟩ := h
  change (c5Fiber t c).card = 10 at hn0
  change (c5Fiber t (c + 1)).card = A at hn1
  change (c5Fiber t (c + 2)).card = 1 at hn2
  change (c5Fiber t (c - 2)).card = 1 at hn3
  change (c5Fiber t (c - 1)).card = B at hn4
  have hw0 := c5_three_fiber_witness_counts H t hp c (c + 2) (c - 2)
    ((by decide : ∀ c : Fin 5, c ≠ c + 2) c)
    ((by decide : ∀ c : Fin 5, c ≠ c - 2) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj c (c + 2)) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj c (c - 2)) c)
    ((by decide : ∀ c : Fin 5, (SimpleGraph.cycleGraph 5).Adj (c + 2) (c - 2)) c) I
  have hw1 := c5_three_fiber_witness_counts H t hp (c - 1) (c + 1) (c + 2)
    ((by decide : ∀ c : Fin 5, c - 1 ≠ c + 1) c)
    ((by decide : ∀ c : Fin 5, c - 1 ≠ c + 2) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj (c - 1) (c + 1)) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj (c - 1) (c + 2)) c)
    ((by decide : ∀ c : Fin 5, (SimpleGraph.cycleGraph 5).Adj (c + 1) (c + 2)) c) I
  have hw2 := c5_three_fiber_witness_counts H t hp (c + 1) (c - 1) (c - 2)
    ((by decide : ∀ c : Fin 5, c + 1 ≠ c - 1) c)
    ((by decide : ∀ c : Fin 5, c + 1 ≠ c - 2) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj (c + 1) (c - 1)) c)
    ((by decide : ∀ c : Fin 5, ¬ (SimpleGraph.cycleGraph 5).Adj (c + 1) (c - 2)) c)
    ((by decide : ∀ c : Fin 5, (SimpleGraph.cycleGraph 5).Adj (c - 1) (c - 2)) c) I
  dsimp only at hw0 hw1 hw2
  rw [hn0, hn2, hn3] at hw0
  rw [hn4, hn1, hn2] at hw1
  rw [hn1, hn4, hn3] at hw2
  have hs : (c5Fiber t (c + 2) ∩ I).card ≤ 1 :=
    (Finset.card_le_card Finset.inter_subset_left).trans_eq hn2
  have hd : (c5Fiber t (c - 2) ∩ I).card ≤ 1 :=
    (Finset.card_le_card Finset.inter_subset_left).trans_eq hn3
  have hm0 := coreInducedEdgeCount_mono_graph G H hle
    (c5Fiber t c ∪ c5Fiber t (c + 2) ∪ c5Fiber t (c - 2))
  have hm1 := coreInducedEdgeCount_mono_graph G H hle
    (c5Fiber t (c - 1) ∪ c5Fiber t (c + 1) ∪ c5Fiber t (c + 2))
  have hm2 := coreInducedEdgeCount_mono_graph G H hle
    (c5Fiber t (c + 1) ∪ c5Fiber t (c - 1) ∪ c5Fiber t (c - 2))
  have hcsmall (w : V) (hw : w ∈ I) (hwc : (SimpleGraph.cycleGraph 5).Adj (t w) c) :
      (c5Fiber t c ∩ I).card ≤ 1 := by
    apply independent_sup_edge_neighbor_card G u v I _ hI w hw
    intro x hx
    obtain ⟨hxc, hxI⟩ := Finset.mem_inter.mp hx
    refine ⟨hxI, (hp w x).mpr ?_⟩
    rw [(mem_c5Fiber t c x).mp hxc]
    exact hwc
  have hz (j : Fin 5) (hju : j ≠ t u) (hjv : j ≠ t v)
      (hAdj : (SimpleGraph.cycleGraph 5).Adj (t u) j ∨
        (SimpleGraph.cycleGraph 5).Adj (t v) j) : (c5Fiber t j ∩ I).card = 0 := by
    apply Finset.card_eq_zero.mpr
    apply Finset.eq_empty_iff_forall_notMem.mpr
    intro x hx
    obtain ⟨hxj, hxI⟩ := Finset.mem_inter.mp hx
    have htx := (mem_c5Fiber t j x).mp hxj
    rcases hAdj with hAdj | hAdj
    · have he : H.Adj u x := (hp u x).mpr (by rw [htx]; exact hAdj)
      have hE := he.resolve_left (hI huI hxI he.ne)
      rcases ((SimpleGraph.edge_adj _ _).mp hE).1 with ⟨_, hxv⟩ | ⟨_, hxu⟩
      · exact hjv (htx.symm.trans (congrArg t hxv))
      · exact hju (htx.symm.trans (congrArg t hxu))
    · have he : H.Adj v x := (hp v x).mpr (by rw [htx]; exact hAdj)
      have hE := he.resolve_left (hI hvI hxI he.ne)
      rcases ((SimpleGraph.edge_adj _ _).mp hE).1 with ⟨_, hxv⟩ | ⟨_, hxu⟩
      · exact hjv (htx.symm.trans (congrArg t hxv))
      · exact hju (htx.symm.trans (congrArg t hxu))
  have huv : (SimpleGraph.cycleGraph 5).Adj (t u) (t v) :=
    (hp u v).mp (Or.inr ((SimpleGraph.edge_adj _ _).mpr ⟨Or.inl ⟨rfl, rfl⟩, hne⟩))
  have hsplit : (SimpleGraph.cycleGraph 5).Adj (t u) c ∨
      (SimpleGraph.cycleGraph 5).Adj (t v) c ∨
      ((c + 1 ≠ t u ∧ c + 1 ≠ t v ∧
        ((SimpleGraph.cycleGraph 5).Adj (t u) (c + 1) ∨
          (SimpleGraph.cycleGraph 5).Adj (t v) (c + 1))) ∧
      (c - 1 ≠ t u ∧ c - 1 ≠ t v ∧
        ((SimpleGraph.cycleGraph 5).Adj (t u) (c - 1) ∨
          (SimpleGraph.cycleGraph 5).Adj (t v) (c - 1)))) :=
    (by decide : ∀ c a b : Fin 5, (SimpleGraph.cycleGraph 5).Adj a b →
      (SimpleGraph.cycleGraph 5).Adj a c ∨ (SimpleGraph.cycleGraph 5).Adj b c ∨
      ((c + 1 ≠ a ∧ c + 1 ≠ b ∧
        ((SimpleGraph.cycleGraph 5).Adj a (c + 1) ∨ (SimpleGraph.cycleGraph 5).Adj b (c + 1))) ∧
      (c - 1 ≠ a ∧ c - 1 ≠ b ∧
        ((SimpleGraph.cycleGraph 5).Adj a (c - 1) ∨ (SimpleGraph.cycleGraph 5).Adj b (c - 1))))) c (t u) (t v) huv
  rcases hsplit with hc | hc | ⟨ha, hb⟩
  · have hsmall := hcsmall u huI hc
    exact ⟨c5Fiber t c ∪ c5Fiber t (c + 2) ∪ c5Fiber t (c - 2), by omega, by omega⟩
  · have hsmall := hcsmall v hvI hc
    exact ⟨c5Fiber t c ∪ c5Fiber t (c + 2) ∪ c5Fiber t (c - 2), by omega, by omega⟩
  · have hza := hz (c + 1) ha.1 ha.2.1 ha.2.2
    have hzb := hz (c - 1) hb.1 hb.2.1 hb.2.2
    by_cases hA : A ≤ 5
    · exact ⟨c5Fiber t (c - 1) ∪ c5Fiber t (c + 1) ∪ c5Fiber t (c + 2), by omega, by omega⟩
    · exact ⟨c5Fiber t (c + 1) ∪ c5Fiber t (c - 1) ∪ c5Fiber t (c - 2), by omega, by omega⟩

/-- Frozen M3 with precisely the original R23 assumptions; every classified
graph and every independent set is covered by the structural proofs above. -/
theorem r23_cost_six (G : SimpleGraph V) (hV : Fintype.card V = 23)
    (ht : G.CliqueFree 3) (hI : CoreIndependenceBound 11 G)
    (he : 121 ≤ G.edgeFinset.card) : CostSixProperty G := by
  rcases r23_complete_classification G hV ht hI he with h | h | h
  · exact case_I_cost_six G h
  · obtain ⟨u, v, hne, _, _, _, _, _, hp⟩ := h
    exact case_I_single_edge_deletion_cost_six G u v hne hp
  · exact exceptional_cost_six G h

end EG617
