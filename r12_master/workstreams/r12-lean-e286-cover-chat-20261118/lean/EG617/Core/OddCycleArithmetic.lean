module

public import EG617.Combinatorics.TuranArithmetic

@[expose] public section
set_option autoImplicit false

namespace EG617

/-- The domain of graph applications is 2 ≤ k and 2*k+1 ≤ n. -/
def oddCycleBound (n k : ℕ) : ℕ :=
  2 * k + 1 + k * (n - (2 * k + 1)) + (n - (2 * k + 1)) ^ 2 / 4

theorem oddCycleBound_23_two : oddCycleBound 23 2 = 122 := by
  norm_num [oddCycleBound]

theorem oddCycleBound_23_ge_three (k : ℕ) (hk : 3 ≤ k)
    (hfit : 2 * k + 1 ≤ 23) : oddCycleBound 23 k ≤ 119 := by
  have : k ≤ 11 := by omega
  interval_cases k <;> norm_num [oddCycleBound]

theorem oddCycleBound_23_three : oddCycleBound 23 3 = 119 := by
  norm_num [oddCycleBound]

theorem oddCycleBound_18 (k : ℕ) (hk : 2 ≤ k)
    (hfit : 2 * k + 1 ≤ 18) : oddCycleBound 18 k ≤ 73 := by
  have : k ≤ 8 := by omega
  interval_cases k <;> norm_num [oddCycleBound]

theorem oddCycleBound_18_two : oddCycleBound 18 2 = 73 := by
  norm_num [oddCycleBound]

end EG617
