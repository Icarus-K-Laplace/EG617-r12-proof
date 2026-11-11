module

public import EG617.Core.OddCycleArithmetic
public import EG617.Core.OddCycleStructure
public import EG617.Core.EdgePartition
public import Mathlib.Combinatorics.SimpleGraph.Connectivity.Subgraph

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable
open scoped BigOperators

namespace EG617
open SimpleGraph SimpleGraph.Walk
universe u
variable {V : Type u} [Fintype V] {G : SimpleGraph V}

theorem cycle_support_card {v : V} (p : G.Walk v v) (hp : p.IsCycle) :
    p.support.toFinset.card = p.length := by
  classical
  have hv : v ∈ p.support.tail := p.end_mem_tail_support hp.not_nil
  have hs : p.support.toFinset = p.support.tail.toFinset := by
    conv_lhs => rw [← p.cons_tail_support]
    simp only [List.toFinset_cons, Finset.insert_eq_of_mem (List.mem_toFinset.mpr hv)]
  rw [hs, List.toFinset_card_of_nodup hp.support_nodup, List.length_tail, p.length_support]
  omega

theorem chordless_cycle_induced_degree_two {v : V} (p : G.Walk v v)
    (hp : p.IsCycle) (hc : p.IsChordless) (x : p.support.toFinset) :
    (G.induce (p.support.toFinset : Set V)).degree x = 2 := by
  classical
  rw [degree_induce_eq_filter]
  have hx : (x : V) ∈ p.support := List.mem_toFinset.mp x.property
  have he : (↑(p.support.toFinset.filter (G.Adj x)) : Set V) =
      p.toSubgraph.neighborSet x := by
    ext y
    simp only [Finset.mem_coe, Finset.mem_filter, List.mem_toFinset,
      SimpleGraph.Subgraph.mem_neighborSet]
    constructor
    · rintro ⟨hy, ha⟩
      exact adj_toSubgraph_iff_mem_edges.mpr (hc.mem_edges hx hy ha)
    · intro ha
      exact ⟨p.mem_verts_toSubgraph.mp (p.toSubgraph.edge_vert ha.symm),
        p.toSubgraph.adj_sub ha⟩
  have hn := hp.ncard_neighborSet_toSubgraph_eq_two hx
  rw [← he] at hn
  simpa using hn

theorem chordless_cycle_induced_edges {v : V} (p : G.Walk v v)
    (hp : p.IsCycle) (hc : p.IsChordless) :
    coreInducedEdgeCount G p.support.toFinset = p.length := by
  classical
  have hd := (G.induce (p.support.toFinset : Set V)).sum_degrees_eq_twice_card_edges
  simp only [chordless_cycle_induced_degree_two p hp hc, Finset.sum_const,
    Finset.card_univ, smul_eq_mul, Fintype.card_coe, cycle_support_card p hp] at hd
  change _ = 2 * coreInducedEdgeCount G p.support.toFinset at hd
  omega

theorem twice_subset_independent_card_le_of_induced_degree_two
    (G : SimpleGraph V) (S : Finset V)
    (hd : ∀ v : S, (G.induce (S : Set V)).degree v = 2)
    (I : Finset V) (hIS : I ⊆ S) (hI : G.IsIndepSet (I : Set V)) :
    2 * I.card ≤ S.card := by
  classical
  let f : I ↪ S := ⟨fun x => ⟨x.val, hIS x.property⟩, by
    intro x y h
    exact Subtype.ext (congrArg Subtype.val h)⟩
  let J : Finset S := Finset.univ.map f
  have hJ : (G.induce (S : Set V)).IsIndepSet (J : Set S) := by
    intro x hx y hy hxy hadj
    obtain ⟨a, _, rfl⟩ := Finset.mem_map.mp hx
    obtain ⟨b, _, rfl⟩ := Finset.mem_map.mp hy
    exact hI a.property b.property
      (fun h => hxy (Subtype.ext h)) hadj
  have h := twice_independent_card_le_of_degree_two (G.induce (S : Set V)) hd J hJ
  simpa [J] using h

theorem shortestOddLoop_neighbor_card_le {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) (ht : G.CliqueFree 3) (k : ℕ)
    (hlen : p.length = 2 * k + 1) (x : V) :
    (p.support.toFinset.filter (G.Adj x)).card ≤ k := by
  classical
  have hpc := shortestOddLoop_isCycle p hp
  have hch := shortestOddLoop_isChordless p hp
  have hI : G.IsIndepSet (↑(p.support.toFinset.filter (G.Adj x)) : Set V) := by
    intro a ha b hb hab
    exact (G.isIndepSet_neighborSet_of_triangleFree ht x)
      (Finset.mem_filter.mp ha).2 (Finset.mem_filter.mp hb).2 hab
  have h := twice_subset_independent_card_le_of_induced_degree_two G p.support.toFinset
    (chordless_cycle_induced_degree_two p hpc hch) _ (Finset.filter_subset _ _) hI
  rw [cycle_support_card p hpc, hlen] at h
  omega

/-- Mantel on any finite induced vertex set, with standard unordered edge counts. -/
theorem triangleFree_induced_mantel (G : SimpleGraph V) (ht : G.CliqueFree 3)
    (S : Finset V) : coreInducedEdgeCount G S ≤ S.card ^ 2 / 4 := by
  classical
  have hti : (G.induce (S : Set V)).CliqueFree 3 :=
    ht.comap (SimpleGraph.Embedding.induce (G := G) (S : Set V)).isContained
  have h := hti.card_edgeFinset_le
  simpa only [SimpleGraph.turanNumber_two, Fintype.card_coe] using h

/-- The graph bound, not merely the numerical formula: the three edge classes
are counted exactly, and no unproved capacity estimate occurs as a hypothesis. -/
theorem shortestOddLoop_edge_bound (G : SimpleGraph V) (ht : G.CliqueFree 3)
    {v : V} (p : G.Walk v v) (hp : IsShortestOddLoop p) (k : ℕ)
    (hlen : p.length = 2 * k + 1) :
    G.edgeFinset.card ≤ oddCycleBound (Fintype.card V) k := by
  classical
  let S := p.support.toFinset
  have hpc := shortestOddLoop_isCycle p hp
  have hch := shortestOddLoop_isChordless p hp
  have hs : S.card = 2 * k + 1 := (cycle_support_card p hpc).trans hlen
  have hc : coreInducedEdgeCount G S = 2 * k + 1 :=
    (chordless_cycle_induced_edges p hpc hch).trans hlen
  have hsum : S.card + Sᶜ.card = Fintype.card V := by
    simpa using Finset.card_add_card_compl S
  have hx : Sᶜ.card = Fintype.card V - (2 * k + 1) := by omega
  have hcross : adjCount G S Sᶜ ≤ k * Sᶜ.card := by
    rw [adjCount_symm, adjCount_eq_sum_filter]
    calc
      _ ≤ ∑ _x ∈ Sᶜ, k := Finset.sum_le_sum (fun x _ =>
        shortestOddLoop_neighbor_card_le p hp ht k hlen x)
      _ = k * Sᶜ.card := by simp [Nat.mul_comm]
  have hout := triangleFree_induced_mantel G ht Sᶜ
  have hpart := edge_partition G S
  rw [hc] at hpart
  rw [hx] at hcross hout
  unfold oddCycleBound
  omega

end EG617
