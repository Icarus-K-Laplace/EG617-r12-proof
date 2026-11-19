module
public import EG617
public meta import Lean.Elab.Command

/- The audit reads elaborated theorem types and proof terms. It is not a source
text dependency scan and contributes no mathematical assumptions. -/
run_cmd do
  let env ← Lean.getEnv
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
      | _ => #[]
    let deps := (ci.type.getUsedConstants ++ bodyDeps).filter fun n =>
      n.toString.startsWith "EG617." || n.toString.startsWith "_private.EG617."
    Lean.logInfo m!"PROJECT_DEPENDENCIES {name}: {deps}"
    pending := pending ++ deps
  Lean.logInfo "E286_ELABORATED_DEPENDENCY_AUDIT_PASS"
