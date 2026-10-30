# Local check log

Date: 2026-10-30 UTC

## Dependency-free checks

The same logic committed in `verify_m89_pivot_matching.py` was run in the available Python runtime.

```text
m=8: scalar_states=79, x=[8,23], y=[0,24], z=[0,12]
m=9: scalar_states=61, x=[13,25], y=[0,19], z=[0,9]
mu_4(t): [4, 6, 8, 8, 10, 10, 12, 12, 12, 13, 13, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16]
matching_composition_local_obstruction_cases: 2304
source_profiles: x in O -> 11 single-outside witnesses;
                x in H two-double -> 10; x in H triple -> 11
m=8 canonical color vector sum=1830
m=9 canonical color vector sum=1830
```

Result: all local checks passed.

Additional independent local check: the 2,304 local matching-composition obstruction cases were rebuilt explicitly as 12-vertex graphs; in each case the missing composed edge creates an independent 5-set. The μ4(t) table was re-enumerated over all 65,536 K4,4 edge sets.

A guarded-cut audit found and repaired an earlier overconstraint: composition edges and multi-projection capacities are now implications guarded by the same selected pivot blocks and both incident pairs remaining exactly four-edge pairs.

The source-core exact accounting and conditional 69/70 near-Turan partition constraints were added. The partition constraints now apply to all eleven non-target colors. The independent verifier reconstructs the 11K4+K3 partition from the color graph for every low-layer candidate, then checks source-witness alignment for exact colors. These additions were statically inspected; the full solver and full candidate verifier have not been run.

## Full solver

```text
Python import check: ModuleNotFoundError: No module named 'z3'
```

The full CSP was not run. No solver version, SAT/UNSAT output, proof log, or full candidate is available. No UNSAT certificate is claimed.
