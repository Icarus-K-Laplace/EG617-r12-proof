# Progress log — Astra-2 D_low terminal

## 2026-10-24: source freeze and independent derivation

- Created the requested branch from main
  b98bea36e36a033100b8bf09a599897cb5afd7de.
- Read the requested design-terminal and asymptotic assets; froze
  source versions recorded in SOURCE_LOCK.json.
- Audited the product-cover quantifier and split-cover pitfalls.
- Derived sparse-color matching, five-anchor extension, actual
  bounded kernel, and unique-edge all-color cut capacity.
- Obtained uniform exclusion r>=221, with high-degree exclusion
  r>=209 and eta-specific improvements. No claim for the full range
  beginning at 67 and no claim that A_ext* is proved.
- Four proof files were saved locally; a subsequent write was
  interrupted by a usage-limit approval failure. No remote proof
  commit had been made at that interruption.

## 2026-10-25: resumed audit and publication

- Re-read all saved proofs and independently checked the exact cut
  algebra, sparse-component exhaustion, anchor counts, and thresholds.
- Rechecked the latest D and E heads. The D branch retracts a distinct
  r>=6212 argument; the E branch still leaves low-offset hub exclusion
  open. Neither update is a dependency of the new kernel proof.
- Completed all eight required mathematical documents. Only this
  workstream directory is modified.
- Verification and publication commit SHAs are recorded below as
  they are completed. The proof is analytic; finite verification
  supplements rather than substitutes for the argument for all r.
