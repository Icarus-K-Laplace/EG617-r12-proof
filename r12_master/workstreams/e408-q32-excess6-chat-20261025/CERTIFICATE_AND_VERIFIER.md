# Certificate and verifier — E408 Q32 excess-six line

## Reproducible arithmetic verifier

Run:

    python verify_core285_capacity.py

The verifier uses only the Python standard library. It checks:

- p_4(n) values from the balanced four-clique minimum-edge formula;
- the exact Cap_285(v) integer table for v=27,…,37;
- the minimum support sizes v≥33,35,37 for m=8,9,10;
- the 14-vertex shell edge cap e(M)≥22 and the q=32 shell slack interval;
- the exact aggregate outer duplicate lower bounds and the 11/20/29 witness-blocker counts;
- the shell-support split inequalities in the M[B]=∅ branch.

Expected terminal line:

    CORE285_E408_Q32_ARITHMETIC_OK

## What is and is not certified

**Arithmetic certified by the script:** the displayed integer identities, Turán minimum-edge values, support thresholds, and aggregate floor calculations.

**Analytic proof supplied in the Markdown files:** extraction of at least eight core witnesses per exact-129 color, pairwise linearity, the 285-edge capacity inequality, the shell support parameterization, and the outer blocker-occurrence coupling.

**External/registered inputs not re-proved by the script:** the original balanced-coloring contract, the outer seven-block embedding ledger, the Kang–Pikhurko Type-I equality classification, and its contextual blocker theorem. Their use is explicit and conditional.

**Not certified:** existence or nonexistence of a 47-vertex graph realizing the surviving profiles; exhaustive coverage by a finite search; an UNSAT result; or the full EG617(r=12) theorem.

No SAT/ILP/CSP certificate is claimed because no complete instance covering every permitted shell-support pattern has yet been constructed.
