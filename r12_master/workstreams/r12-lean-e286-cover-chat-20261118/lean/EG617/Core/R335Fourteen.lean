module
public import EG617.Core.R335Neighborhood

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
universe u
variable {V : Type u} [Fintype V]

/-- Frozen M4: a degree-eleven neighborhood cannot be a clique under omega<=11. -/
theorem core_degree_eleven_neighbor_nonedge (G : SimpleGraph V)
    (hG : CoreCliqueBound 11 G) (v : V) (hd : G.degree v = 11) :
    ∃ x ∈ G.neighborFinset v, ∃ y ∈ G.neighborFinset v, x ≠ y ∧ ¬ G.Adj x y := by
  classical
  by_contra hn
  have hR : G.IsClique (G.neighborFinset v : Set V) := by
    intro x hx y hy hxy
    by_contra hnot
    exact hn ⟨x, hx, y, hy, hxy, hnot⟩
  have hi : G.IsClique (insert v (G.neighborFinset v : Set V)) :=
    hR.insert (fun w hw _ => (SimpleGraph.mem_neighborFinset G v w).mp hw)
  have hb := hG (insert v (G.neighborFinset v)) (by
    simpa only [Finset.coe_insert] using hi)
  have hv : v ∉ G.neighborFinset v := by simp
  rw [Finset.card_insert_of_notMem hv, SimpleGraph.card_neighborFinset_eq_degree, hd] at hb
  omega

/-- Two nonadjacent vertices in an alpha<=3 graph have a clique as their common
nonneighborhood. Both endpoints are explicitly excluded from the vertex set. -/
theorem core_common_nonneighbors_clique (G : SimpleGraph V)
    (hG : CoreIndependenceBound 3 G) (x y : V) (hxy : x ≠ y) (hnot : ¬ G.Adj x y)
    (S : Finset V) (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    G.IsClique (S : Set V) := by
  classical
  intro a ha b hb hab
  by_contra hnab
  obtain ⟨hax, hay, hxa, hya⟩ := hS a ha
  obtain ⟨hbx, hby, hxb, hyb⟩ := hS b hb
  have hi : G.IsIndepSet (({x, y, a, b} : Finset V) : Set V) := by
    intro u hu w hw huw
    simp only [Finset.mem_coe, Finset.mem_insert, Finset.mem_singleton] at hu hw
    rcases hu with rfl | rfl | rfl | rfl <;>
      rcases hw with rfl | rfl | rfl | rfl <;> simp_all [G.adj_comm]
  have hc := hG {x, y, a, b} hi
  have hcard : ({x, y, a, b} : Finset V).card = 4 := by
    simp [hxy, hax, hay, hbx, hby, hab, Ne.symm hax, Ne.symm hay,
      Ne.symm hbx, Ne.symm hby]
  rw [hcard] at hc
  omega

/-- Exact edge ledger for two arbitrary disjoint finite vertex sets. -/
theorem core_edge_count_union (G : SimpleGraph V) (S T : Finset V) (hd : Disjoint S T) :
    coreInducedEdgeCount G (S ∪ T) = coreInducedEdgeCount G S +
      adjCount G S T + coreInducedEdgeCount G T := by
  classical
  have h := adjCount_union_left G S T (S ∪ T) hd
  rw [adjCount_union_right G S S T hd, adjCount_union_right G T S T hd,
    adjCount_symm G T S, adjCount_self G S, adjCount_self G T,
    adjCount_self G (S ∪ T)] at h
  simp only [coreInducedEdgeCount, SimpleGraph.edgeFinset_card,
    Set.fintypeCard_eq_ncard] at h ⊢
  omega

/-- A vertex outside the common nonneighborhood contributes at least one edge
to the two distinct endpoints. This counts actual cross edges once each. -/
theorem core_pair_cross_lower_bound (G : SimpleGraph V) (T : Finset V)
    (x y : V) (hxy : x ≠ y) :
    T.card ≤ adjCount G T {x, y} + (T.filter (fun z => ¬ G.Adj x z ∧ ¬ G.Adj y z)).card := by
  classical
  have hpoint : ∀ z ∈ T, 1 ≤ (if G.Adj z x then 1 else 0) +
      (if G.Adj z y then 1 else 0) +
      (if ¬ G.Adj x z ∧ ¬ G.Adj y z then 1 else 0) := by
    intro z _
    by_cases hx : G.Adj x z <;> by_cases hy : G.Adj y z <;>
      simp [G.adj_comm, hx, hy]
  have hsum := Finset.sum_le_sum hpoint
  have hpair : adjCount G T {x, y} =
      (∑ z ∈ T, if G.Adj z x then 1 else 0) +
      (∑ z ∈ T, if G.Adj z y then 1 else 0) := by
    simp only [adjCount, Finset.sum_pair hxy, Finset.sum_add_distrib]
  rw [hpair]
  simpa [Finset.sum_add_distrib] using hsum

theorem core_induce_compl (G : SimpleGraph V) (T : Finset V) :
    (G.induce (T : Set V))ᶜ = Gᶜ.induce (T : Set V) := by
  ext a b
  change (a ≠ b ∧ ¬ G.Adj a b) ↔ ((a : V) ≠ (b : V) ∧ ¬ G.Adj a b)
  rw [Subtype.val_injective.ne_iff]

theorem core_induced_compl_edge_count (G : SimpleGraph V) (T : Finset V) :
    coreInducedEdgeCount G T + coreInducedEdgeCount Gᶜ T = T.card.choose 2 := by
  classical
  have h := core_compl_edge_count (G.induce (T : Set V))
  simp only [SimpleGraph.edgeFinset_card, Set.fintypeCard_eq_ncard] at h
  rw [core_induce_compl] at h
  simpa only [coreInducedEdgeCount, SimpleGraph.edgeFinset_card,
    Set.fintypeCard_eq_ncard, Set.ncard_coe_finset] using h

/-- Frozen M4's actual fourteen-point counting contradiction. The low-cost
premise is explicit here; the R335 parent must derive it from certified M3. -/
theorem core_fourteen_cost_obstruction (G : SimpleGraph V)
    (hcap : ∀ U : Finset V, coreInducedEdgeCount G U ≤ D U.card)
    (T : Finset V) (hT : T.card = 12) (x y : V) (hxy : x ≠ y)
    (hx : x ∉ T) (hy : y ∉ T)
    (hcost : coreInducedEdgeCount Gᶜ T +
      (T.filter (fun z => ¬ G.Adj x z ∧ ¬ G.Adj y z)).card ≤ 6) : False := by
  classical
  have hdis : Disjoint T ({x, y} : Finset V) := by
    rw [Finset.disjoint_left]
    intro z hz hzxy
    rcases Finset.mem_insert.mp hzxy with rfl | hzxy
    · exact hx hz
    · have : z = y := Finset.mem_singleton.mp hzxy
      subst z
      exact hy hz
  have hp : ({x, y} : Finset V).card = 2 := by simp [hxy]
  have h14 : (T ∪ {x, y}).card = 14 := by
    rw [Finset.card_union_of_disjoint hdis, hT, hp]
  have hc := hcap (T ∪ {x, y})
  rw [h14] at hc
  have hD : D 14 = 69 := by norm_num [D, tau12, Nat.choose_two_right]
  rw [hD] at hc
  have he := core_edge_count_union G T {x, y} hdis
  have hcompl := core_induced_compl_edge_count G T
  rw [hT] at hcompl
  norm_num only [Nat.choose_two_right] at hcompl
  have hcross := core_pair_cross_lower_bound G T x y hxy
  rw [hT] at hcross
  omega

end EG617
