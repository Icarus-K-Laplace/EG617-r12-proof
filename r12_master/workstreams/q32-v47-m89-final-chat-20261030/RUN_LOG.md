# Local check log

Date: 2026-10-30 UTC

## Dependency-free checks

The same logic committed in `verify_m89_pivot_matching.py` was run in the available Python runtime.

```text
m=8: scalar_states=79, x=[8,23], y=[0,24], z=[0,24]
m=9: scalar_states=61, x=[13,25], y=[0,19], z=[0,19]
mu_4(t): [4, 6, 8, 8, 10, 10, 12, 12, 12, 13, 13, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16]
matching_composition_cases: 2304
source_profiles: x in O -> 11 single-outside witnesses;
                x in H two-double -> 10; x in H triple -> 11
m=8 canonical color vector sum=1830
m=9 canonical color vector sum=1830
```

Result: all local checks passed.

## Full solver

```text
Python import check: ModuleNotFoundError: No module named 'z3'
```

The full CSP was not run. No solver version, SAT/UNSAT output, proof log, or full candidate is available. No UNSAT certificate is claimed.
