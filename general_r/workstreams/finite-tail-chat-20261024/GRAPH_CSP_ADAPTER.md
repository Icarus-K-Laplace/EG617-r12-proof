# Graph/CSP Adapter Plan

## Status

**DESIGN CONTRACT ONLY — NO GRAPH-LEVEL INSTANCE OR UNSAT CLAIM EXISTS.**

The current endpoint-domain module is a verified scalar necessary-condition module. It must not be presented as a graph-level CSP, and no endpoint-specific clean-pair, d1, d2, d3, or design-terminal closure is inserted until its analytic theorem gate is discharged.

## Adapter pipeline

1. Load the immutable per-r theorem gate and assumption ledger.
2. Select only modules whose premises are certified for this exact r, or label the whole instance conditional.
3. Build a deterministic colored-incidence variable map.
4. Add only constraints whose exact theorem statement and source commit are registered.
5. Apply only symmetry reductions with independently checked witnesses.
6. Canonicalize and hash the complete CSP/CNF.
7. Generate a proof certificate (bounded enumeration, LRAT/DRAT, or exact integer/rational certificate).
8. Replay with an independent verifier.
9. Run theorem promotion; do not infer graph nonexistence from solver status alone.

## Planned endpoint modules

| module | intended mathematical input | current status | activation rule |
|---|---|---|---|
| d0 neutral symmetry | proved d0 normalization/equivalence theorem | OPEN | do not encode as graph constraint |
| d1 shell classes | conditional shell-incidence theorem gives at most 5 shell classes; bounded-allowance nonextension is separate | shell-count arithmetic module `D1_SHELL_CLASS_BOUND_V1` certified conditionally; multiplicity closure OPEN | activate only with A+B; never infer absolute owner multiplicity |
| d2 support pairs | proved support-pair/charge theorem | OPEN | no guessed pair compatibility clauses |
| d3 closure | sibling d3/common-S theorem with all premises | CONDITIONAL; integration pending | list exact assumptions and r-range |
| high-endpoint kernel | proved bounded-kernel/owner theorem | CONDITIONAL; integration pending | attach source commit and witness checker |
| design terminal | robust design nonextension theorem | OPEN | do not encode nonextension as an axiom |

The table describes interfaces to implement, not facts already proved by this workstream.

## Canonical variable map requirements

Every graph-level variable must have a stable identifier derived from:
- parameter r;
- role (pivot, shell, core, color, support class);
- canonical position within a verified labeling;
- module/version identifier.

The map must be serialized into the instance. The verifier must reject duplicate identifiers, missing domains, inconsistent color counts, and any constraint that references an undeclared variable.

## SAT and exact certificates

For a future SAT instance, record:
- deterministic DIMACS generator version;
- complete variable map;
- CNF SHA-256;
- solver and version as provenance only;
- full LRAT proof (preferred) or DRAT proof plus reproducible checking/conversion;
- proof-checker version/hash;
- independent replay receipt.

For bounded enumeration, record the deterministic successor rule and a digest of every canonical state or a Merkle-style complete enumeration transcript. For ILP, require an exact integer/rational infeasibility witness; floating-point logs are not accepted.

## Hard prohibition

Never add a conjectural endpoint closure, clean-pair nonextension, bounded-allowance d1 closure, or design-terminal nonextension as a CNF clause merely because it is expected to be true. The source theorem and its assumption IDs must precede the clause in the theorem ledger. An UNSAT proof under an unproved clause certifies only the augmented conditional system, not EG617(r).


## Round 2 — admission matrix and symmetry witness interface

The parameter gate is now an explicit upstream adapter:

1. validate `PARAMETER_ADMISSION_MATRIX.json` with `PARAMETER_ADMISSION_VERIFIER.py`;
2. query exact r/module/profile;
3. reject theorem-level admission below r=12 unless a separate parameter-specific reduction is registered;
4. preserve RC and ANCHOR_K8 as explicit assumptions when their broad contracts are not discharged;
5. only then generate a local conditional module certificate.

A graph-level witness schema and small exhaustive reference verifier now exist. They check role-preserving vertex bijections, color-class-preserving color bijections, exact colored-edge incidence, indexed constraints, canonical encodings, one witness per state, and pairwise inequivalence of representatives. The K3/two-color fixture is only a test of this interface. It is not a graph-level EG617 instance, and no SAT/UNSAT search was started.
