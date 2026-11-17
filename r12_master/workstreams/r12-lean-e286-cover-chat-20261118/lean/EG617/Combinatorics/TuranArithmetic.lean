module

public import Mathlib.Combinatorics.SimpleGraph.Extremal.Turan
public import Mathlib.Tactic.IntervalCases
public import Mathlib.Tactic.NormNum

@[expose] public section

set_option autoImplicit false
set_option maxHeartbeats 0

namespace EG617

/-- The number of edges inside twelve parts whose sizes differ by at most one.
For `n = 12 * q + s`, with `s < 12`, this is
`12 * choose q 2 + q * s`. -/
def tau12 (n : ℕ) : ℕ :=
  12 * Nat.choose (n / 12) 2 + (n / 12) * (n % 12)

/-- Exact complement identity on the full range needed for vertex subsets of `Fin 145`.

The bound is explicit: every natural number from zero through 145 is covered by
`interval_cases`. Each resulting closed arithmetic equality is proved using
`norm_num`, after rewriting with Mathlib's exact Turan-number formula.
This uses neither an external oracle nor native evaluation. -/
theorem tau12_add_turanNumber (n : ℕ) (hn : n ≤ 145) :
    tau12 n + SimpleGraph.turanNumber n 12 = Nat.choose n 2 := by
  rw [SimpleGraph.turanNumber_eq]
  interval_cases n <;> norm_num [tau12, Nat.choose_two_right]

end EG617
