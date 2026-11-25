import EG617
import Lean.Elab.Command

/- Legacy import mode deliberately loads private proof bodies transitively.
Ordinary public module imports expose theorem types but erase imported bodies.
This audit contributes no mathematical assumptions. -/
run_cmd do
  let env := (← Lean.getEnv).setExporting false
  let mut pending := #[``EG617.e286_actual_support_D_or_C]
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
      ``EG617.e286_h4_star_orbit_impossible,
      ``EG617.e286_center_lane_bound,
      ``EG617.e286_h5_nine_or_B_impossible,
      ``EG617.e286_shared_leaf_forces_completion,
      ``EG617.e286_h5_P_impossible,
      ``EG617.e286_doubled_mixed_charge_five,
      ``EG617.e286_doubled_pair_completion,
      ``EG617.e286_threshold_scalar_rigidity,
      ``EG617.e286_h4_second_orbit_impossible,
      ``EG617.e286_extra_completer_split,
      ``EG617.e286_f10_11_extra_completer_minimum,
      ``EG617.e286_shared_leaf_pair_charge,
      ``EG617.e286_shared_leaf_pointwise,
      ``EG617.e286_first_support_orbit_impossible,
      ``EG617.e286_finite_support_orbit_check,
      ``EG617.e286_weighted_profiles_complete,
      ``EG617.e286_pair_blocker_complete,
      ``EG617.e286_k11_pair_local_charge,
      ``EG617.e286_excess_sum,
      ``EG617.e286_private_mixed_pair_dichotomy,
      ``EG617.e286_k10_k11_pair_local_charge,
      ``EG617.e286_f10_11_minimum,
      ``EG617.e286_double_count_actual_witnesses,
      ``EG617.e286_ten_clique_completers_excess,
      ``EG617.e286_third_support_orbit_impossible,
      ``EG617.e286_three_k11_local_charge,
      ``EG617.e286_ordered_three_cliques_obstruction,
      ``EG617.e286_private_pair_concentrated_charge,
      ``EG617.e286_second_support_orbit_impossible] do
    unless seen.contains required do
      throwError "Proof-body dependency missing: {required}"
  Lean.logInfo "E286_ELABORATED_DEPENDENCY_AUDIT_PASS"
