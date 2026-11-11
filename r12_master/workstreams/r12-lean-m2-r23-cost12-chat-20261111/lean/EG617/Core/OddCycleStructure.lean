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
  | nil => simp
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
    simpa [length_cons, hlen] using this

theorem exists_shortestOddLoop (hG : ¬ G.Colorable 2) :
    ∃ v (p : G.Walk v v), IsShortestOddLoop p := by
  classical
  have hex : ∃ n : ℕ, ∃ v (p : G.Walk v v), Odd p.length ∧ p.length = n := by
    have h : ∃ v (p : G.Walk v v), Odd p.length := by
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
    ∃ v (p : G.Walk v v), p.IsCycle ∧ IsShortestOddLoop p := by
  obtain ⟨v, p, hp⟩ := exists_shortestOddLoop hG
  exact ⟨v, p, shortestOddLoop_isCycle p hp, hp⟩

end EG617
