module

public import EG617.Core.R224
public import Mathlib.Combinatorics.SimpleGraph.Coloring.Constructions
public import Mathlib.Combinatorics.SimpleGraph.Walk.Chord

@[expose] public section
set_option autoImplicit false
attribute [local instance] Classical.propDecidable

namespace EG617
open SimpleGraph SimpleGraph.Walk
universe u
variable {V : Type u} {G : SimpleGraph V}

/-- Minimality is over all odd closed walks; below it is proved to yield a simple cycle. -/
def IsShortestOddLoop {v : V} (p : G.Walk v v) : Prop :=
  Odd p.length ∧ ∀ w (q : G.Walk w w), Odd q.length → p.length ≤ q.length

/-- Removing repeated vertices preserves parity when no shorter odd loop exists. -/
theorem bypass_parity_of_short_loops_even (N : ℕ)
    (hN : ∀ v (q : G.Walk v v), q.length < N → Even q.length)
    {a b : V} (p : G.Walk a b) (hp : p.length < N) :
    p.bypass.length % 2 = p.length % 2 := by
  classical
  induction p with
  | nil => simp [bypass]
  | @cons a b c hab p ih =>
    have hp0 : p.length + 1 < N := by simpa only [length_cons] using hp
    have hp' : p.length < N := by omega
    have hi := ih hp'
    have hle := p.length_bypass_le_length
    simp only [bypass]
    split_ifs with hs
    · have ht := p.bypass.length_takeUntil_le_length hs
      have he := hN a ((p.bypass.takeUntil a hs).cons hab) (by
        simp only [length_cons]
        simp only [length_cons] at hp
        omega)
      have hsum := congrArg Walk.length (p.bypass.take_spec hs)
      simp only [length_append] at hsum
      rw [Nat.even_iff] at he
      simp only [length_cons] at he ⊢
      omega
    · simp only [length_cons]
      omega

theorem shortestOddLoop_isCycle {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) : p.IsCycle := by
  classical
  have hno : ∀ w (q : G.Walk w w), q.length < p.length → Even q.length := by
    intro w q hq
    apply Nat.not_odd_iff_even.mp
    intro ho
    have := hp.2 w q ho
    omega
  cases p with
  | nil => exfalso; simpa using hp.1
  | cons hvw p =>
    have hpar := bypass_parity_of_short_loops_even (p.length + 1) hno p (by omega)
    have ho : Odd (p.bypass.cons hvw).length := by
      have hodd := hp.1
      rw [Nat.odd_iff] at hodd
      rw [Nat.odd_iff]
      simp only [length_cons] at *
      omega
    have hmin := hp.2 v (p.bypass.cons hvw) ho
    have heq : p.bypass = p := p.length_le_bypass_length_iff.mp (by
      simp only [length_cons] at hmin
      omega)
    have hpath : p.IsPath := heq ▸ p.bypass_isPath
    apply (cons_isCycle_iff p hvw).mpr
    refine ⟨hpath, ?_⟩
    intro hedge
    have hlen : p.length = 1 := hpath.length_eq_one_of_mem_edges (by
      simpa only [Sym2.eq_swap] using hedge)
    have := hp.1
    norm_num [length_cons, hlen, Nat.odd_iff] at this

theorem exists_shortestOddLoop (hG : ¬ G.Colorable 2) :
    ∃ v, ∃ p : G.Walk v v, IsShortestOddLoop p := by
  classical
  have hex : ∃ n : ℕ, ∃ v, ∃ p : G.Walk v v, Odd p.length ∧ p.length = n := by
    have h : ∃ v, ∃ p : G.Walk v v, Odd p.length := by
      simpa only [SimpleGraph.two_colorable_iff_forall_loop_even, not_forall,
        Nat.not_even_iff_odd] using hG
    obtain ⟨v, p, hp⟩ := h
    exact ⟨p.length, v, p, hp, rfl⟩
  obtain ⟨v, p, ho, he⟩ := Nat.find_spec hex
  refine ⟨v, p, ho, ?_⟩
  intro w q hq
  rw [he]
  exact Nat.find_min' hex ⟨w, q, hq, rfl⟩

theorem exists_odd_cycle_of_not_two_colorable (hG : ¬ G.Colorable 2) :
    ∃ v, ∃ p : G.Walk v v, p.IsCycle ∧ IsShortestOddLoop p := by
  obtain ⟨v, p, hp⟩ := exists_shortestOddLoop hG
  exact ⟨v, p, shortestOddLoop_isCycle p hp, hp⟩

/-- A one-edge walk contains the unordered edge joining its endpoints. -/
theorem walk_end_edge_mem_of_length_one {a b : V} (p : G.Walk a b)
    (hp : p.length = 1) : s(a, b) ∈ p.edges := by
  cases p with
  | nil => simp at hp
  | cons h q =>
    cases q with
    | nil => simp
    | cons h' q' => simp only [length_cons] at hp; omega

/-- A chord splits an odd shortest loop into two strictly shorter closed walks,
one of which is odd. Thus inducedness is a conclusion, not a terminal hypothesis. -/
theorem shortestOddLoop_isChordless {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) : p.IsChordless := by
  classical
  apply Walk.isChordless_iff_forall_mem_edges.mpr
  intro a b ha hb hab
  by_contra hedge
  let q := p.rotate a ha
  have hbq : b ∈ q.support := (p.mem_support_rotate_iff a ha).mpr hb
  let l := q.takeUntil b hbq
  let r := q.dropUntil b hbq
  have hsum : l.length + r.length = p.length := by
    have h := congrArg Walk.length (q.take_spec hbq)
    simp only [length_append] at h
    simpa only [q, length_rotate] using h
  have hnotq : s(a, b) ∉ q.edges := by
    intro h
    exact hedge ((p.rotate_edges a ha).perm.mem_iff.mp h)
  have hl : 2 ≤ l.length := by
    by_contra h
    by_cases hz : l.length = 0
    · exact hab.ne (Walk.eq_of_length_eq_zero hz)
    · have ho : l.length = 1 := by omega
      exact hnotq (q.edges_takeUntil_subset_edges hbq
        (walk_end_edge_mem_of_length_one l ho))
  have hr : 2 ≤ r.length := by
    by_contra h
    by_cases hz : r.length = 0
    · exact hab.ne (Walk.eq_of_length_eq_zero hz).symm
    · have ho : r.length = 1 := by omega
      apply hnotq
      have he := q.edges_dropUntil_subset_edges hbq (walk_end_edge_mem_of_length_one r ho)
      simpa only [Sym2.eq_swap] using he
  have hodd := Nat.odd_iff.mp hp.1
  by_cases ho : Odd (l.concat hab.symm).length
  · have h := hp.2 a (l.concat hab.symm) ho
    simp only [length_concat] at h
    omega
  · have hor : Odd (r.concat hab).length := by
      rw [Nat.odd_iff] at ho ⊢
      simp only [length_concat] at ho ⊢
      omega
    have h := hp.2 b (r.concat hab) hor
    simp only [length_concat] at h
    omega

/-- The independence bound of a cycle, proved by the disjoint one-step shift. -/
theorem cycleGraph_twice_independent_card_le (m : ℕ)
    (S : Finset (Fin (m + 3)))
    (hS : (SimpleGraph.cycleGraph (m + 3)).IsIndepSet (S : Set (Fin (m + 3)))) :
    2 * S.card ≤ m + 3 := by
  classical
  let f : Fin (m + 3) → Fin (m + 3) := fun x => x + 1
  have hf : Function.Injective f := fun _ _ h => add_right_cancel h
  have hd : Disjoint S (S.image f) := by
    rw [Finset.disjoint_left]
    intro x hx hy
    obtain ⟨y, hy, rfl⟩ := Finset.mem_image.mp hy
    have hadj : (SimpleGraph.cycleGraph (m + 3)).Adj y (f y) := by
      apply SimpleGraph.cycleGraph_adj.mpr
      right
      simp [f]
    exact hS hy hx hadj.ne hadj
  have hcard := (S ∪ S.image f).card_le_univ
  rw [Finset.card_union_of_disjoint hd, Finset.card_image_of_injective S hf] at hcard
  simpa only [Fintype.card_fin, two_mul] using hcard

end EG617
