module
public import EG617.Core.E286SeedLedger
public import Mathlib.Data.Fintype.Perm

@[expose] public section
set_option autoImplicit false
open scoped BigOperators

namespace EG617

/-- The eleven possible seed-support subsets, in the frozen count order:
01,02,03,12,13,23,012,013,023,123,0123. -/
def e286SupportType (i : Fin 11) : Finset (Fin 4) :=
  match i.val with
  | 0 => {0, 1}
  | 1 => {0, 2}
  | 2 => {0, 3}
  | 3 => {1, 2}
  | 4 => {1, 3}
  | 5 => {2, 3}
  | 6 => {0, 1, 2}
  | 7 => {0, 1, 3}
  | 8 => {0, 2, 3}
  | 9 => {1, 2, 3}
  | _ => {0, 1, 2, 3}

def e286SupportWeights : List ℕ := [1,1,1,1,1,1,2,2,2,2,3]

theorem e286_support_type_complete (S : Finset (Fin 4)) (hS : 2 ≤ S.card) :
    ∃! i : Fin 11, e286SupportType i = S := by
  exact (by unfold ExistsUnique; decide :
    ∀ T : Finset (Fin 4), 2 ≤ T.card → ∃! i : Fin 11, e286SupportType i = T) S hS

theorem e286_support_type_weight (i : Fin 11) :
    (e286SupportType i).card - 1 = e286SupportWeights[i.val]! := by
  exact (by decide : ∀ j : Fin 11,
    (e286SupportType j).card - 1 = e286SupportWeights[j.val]!) i

/-- Weighted surplus, with length supplied explicitly by the completeness lemma. -/
def e286WeightedSum : List ℕ → List ℕ → ℕ
  | w :: ws, x :: xs => w * x + e286WeightedSum ws xs
  | _, _ => 0

/-- All nonnegative count vectors with prescribed weighted surplus.
The bound on each first coordinate is proved in the completeness theorem. -/
def e286WeightedProfiles : List ℕ → ℕ → List (List ℕ)
  | [], b => if b = 0 then [[]] else []
  | w :: ws, b => (List.range (b + 1)).flatMap fun x =>
      if w * x ≤ b then (e286WeightedProfiles ws (b - w * x)).map (x :: ·) else []

theorem e286_weighted_profiles_complete (ws xs : List ℕ) (b : ℕ)
    (hpos : ∀ w ∈ ws, 1 ≤ w) (hlen : xs.length = ws.length)
    (hsum : e286WeightedSum ws xs = b) :
    xs ∈ e286WeightedProfiles ws b := by
  induction ws generalizing xs b with
  | nil =>
    cases xs with
    | nil =>
      have hb : b = 0 := hsum.symm
      subst b
      simp [e286WeightedProfiles, e286WeightedSum]
    | cons x xs => simp at hlen
  | cons w ws ih =>
    cases xs with
    | nil => simp at hlen
    | cons x xs =>
      have hw : 1 ≤ w := hpos w (by simp)
      have he : w * x + e286WeightedSum ws xs = b := hsum
      have hle : w * x ≤ b := by omega
      have hxx : x ≤ w * x := by simpa using Nat.mul_le_mul_right x hw
      have hx : x < b + 1 := by omega
      have htail : e286WeightedSum ws xs = b - w * x := by omega
      have hm := ih xs (b - w * x) (fun z hz => hpos z (by simp [hz]))
        (by simpa using hlen) htail
      change x :: xs ∈ (List.range (b + 1)).flatMap _
      apply List.mem_flatMap.mpr
      refine ⟨x, List.mem_range.mpr hx, ?_⟩
      rw [if_pos hle]
      exact List.mem_map.mpr ⟨xs, hm, rfl⟩

def e286CountIncidence (xs : List ℕ) (s : Fin 4) : ℕ :=
  ∑ i : Fin 11, if s ∈ e286SupportType i then xs[i.val]! else 0

/-- Exact relabeling action on multiplicities; it moves the actual support
subset by a permutation of the four seed labels. -/
def e286RelabelCounts (σ : Equiv.Perm (Fin 4)) (xs : List ℕ) : List ℕ :=
  List.ofFn fun j : Fin 11 =>
    ∑ i : Fin 11, if (e286SupportType i).image σ = e286SupportType j
      then xs[i.val]! else 0

/-- Frozen Section2: two h3, three h4, and five h5 representatives. -/
def e286SupportOrbitRepresentatives : List (List ℕ) :=
  [[1,0,0,0,0,1,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,1,1,0],
   [2,0,0,0,0,1,0,0,1,0,0],
   [1,0,1,0,0,1,1,0,0,0,0],
   [1,1,1,0,0,0,0,0,0,1,0],
   [2,1,1,0,0,1,0,0,0,0,0],
   [1,2,0,0,2,0,0,0,0,0,0],
   [1,1,1,1,1,0,0,0,0,0,0],
   [2,1,0,0,1,1,0,0,0,0,0],
   [3,0,0,0,0,2,0,0,0,0,0]]

set_option maxRecDepth 100000 in
set_option maxHeartbeats 8000000 in
theorem e286_finite_support_orbit_check :
    ∀ xs ∈ e286WeightedProfiles e286SupportWeights 5,
      (∀ s : Fin 4, 2 ≤ e286CountIncidence xs s) →
      ∃ σ : Equiv.Perm (Fin 4),
        e286RelabelCounts σ xs ∈ e286SupportOrbitRepresentatives := by
  decide

/-- Every nonnegative support multiplicity vector satisfying the exact surplus
and four seed-incidence constraints lies in one of the ten frozen orbits.
The arbitrary graph-to-count transport is a separate obligation. -/
theorem e286_support_counts_complete (xs : List ℕ)
    (hlen : xs.length = 11) (hsum : e286WeightedSum e286SupportWeights xs = 5)
    (hinc : ∀ s : Fin 4, 2 ≤ e286CountIncidence xs s) :
    ∃ σ : Equiv.Perm (Fin 4),
      e286RelabelCounts σ xs ∈ e286SupportOrbitRepresentatives := by
  have hm := e286_weighted_profiles_complete e286SupportWeights xs 5
    (by decide) hlen hsum
  exact e286_finite_support_orbit_check xs hm hinc

end EG617

