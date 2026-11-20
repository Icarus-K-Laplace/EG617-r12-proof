import EG617
import Lean.Elab.Command

/- Legacy import mode deliberately loads private proof bodies transitively.
Ordinary public module imports expose theorem types but erase imported bodies.
This audit contributes no mathematical assumptions. -/
run_cmd do
  let env := (← Lean.getEnv).setExporting false
  let mut pending := #[``EG617.e286_actual_support_nine_remaining]
  let mut seen : Lean.NameSet := {}
  while !pending.isEmpty do
    let name := pending.back!
    pending := pending.pop
    if seen.contains name then continue
    seen := seen.insert name
    let some ci := env.checked.get.find? name
      | throwError "Missing dependency {name}"
    let bodyDeps := match ci with
      | .defnInfo v => v.value.getUsedConstants
      | .thmInfo v => v.value.getUsedConstants
      | .opaqueInfo v => v.value.getUsedConstants
      | .axiomInfo _ => #[]
      | _ => #[]
    let deps := (ci.type.getUsedConstants ++ bodyDeps).filter fun n =>
      n.toString.startsWith "EG617." || n.toString.startsWith "_private.EG617."
    Lean.logInfo m!"PROJECT_DEPENDENCIES {name}: {deps}"
    pending := pending ++ deps
  for required in #[``EG617.e286_actual_oriented_support_orbit,
      ``EG617.e286_first_support_orbit_impossible,
      ``EG617.e286_finite_support_orbit_check,
      ``EG617.e286_weighted_profiles_complete,
      ``EG617.e286_pair_blocker_complete,
      ``EG617.e286_k11_pair_local_charge,
      ``EG617.e286_excess_sum] do
    unless seen.contains required do
      throwError "Proof-body dependency missing: {required}"
  Lean.logInfo "E286_ELABORATED_DEPENDENCY_AUDIT_PASS"
