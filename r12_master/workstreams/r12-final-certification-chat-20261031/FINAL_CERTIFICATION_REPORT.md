# EG617(r=12) — independent certification report

**CERTIFICATION = PASS**

**Certified statement:** every12-edge-coloring of K145 has a13-vertex set missing
at least one color. Equivalently, the assumed coloring in which every13-set
contains all12 colors does not exist.

This is an independent AI-assisted mathematical audit of the pinned proof,
with newly written derivations and computation. It is not a proof-assistant
formalization, not external human peer review, and not a claim that the code
alone establishes the analytic proof. This package is intended for independent
combinatorialists to inspect and challenge. No substantial mathematical error
or unresolved load-bearing premise was found after the recorded attacks.

## Certified source and repository isolation

Repository: Icarus-K-Laplace/EG617-r12-proof.

|Object|Actual commit|
|---|---|
|Original Global Root|b0459807acd4b7e386148056ddf77d7998918893|
|Integration proof commit|c6c17bb6b1fee0e350fd0ff649680333f30c9f88|
|Pinned integration HEAD|c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2|
|Default main observed|278639de8572ffab12fe859d36f776fbb88fc4f0|
|First independent replay publication|4156032a169052444ef8b7e3d8a84448bbee16e7|

The first three commits form the direct parent chain in the order shown.
The integration HEAD was unchanged at initial and final source checks.
GitHub compare shows exactly two commits ahead of the Global Root and48 files
added, all inside the integration directory; no outside file was changed.
GITHUB_COMPARE_EVIDENCE.json preserves the actual compare response.
REMOTE_BRANCH_HEADS.tsv is the actual later remote-head snapshot. The independent
branch is `workstream/r12-final-certification-chat-20261031`, based on the pinned
integration HEAD. All new tracked changes are confined to this certification
directory. The current certification commit is identified by its PR and Git
history; this file does not pretend to know its own future commit hash.

Raw Git bytes authenticate all48 source files. All26 frozen files match their
declared originating commit, source path and Git blob; every frozen file is
included. All47 entries of the integration SHA256SUMS agree. The original
exact285 theorem is additionally authenticated at f56cc9eba646e71d63c4b55f468a2340bcdd64c2.
These checks establish provenance, not mathematical correctness.

## Mathematical audit result

The complete independent derivation is organized in three documents:

1. **LOWER_ORDER_AND_CORE_CERTIFICATE.md (L1–L6):** lower-order cap lemmas,
   the121/122 classification and12-set construction, minimum-degree gates,
   direct low-edge proof, augmentation with independently traced exact285
   theorem, and every286-edge support/intersection case.
2. **COVER_ANALYTIC_CERTIFICATE.md (C1–C8):** exact identities, global core
   interface, every low-charge reduction, exhaustive enumeration mapping,
   Q27/Q28 and B1 geometry, strong core gate, Q29 promotion, complete Q30
   classification, and both terminal contradictions.
3. **FRONTEND_H12_AND_GLOBAL_CERTIFICATE.md (F1–F5):** original coloring caps,
   contextual49 exclusion, exact extraction budget, h12 and q20 classification,
   every recurrence rule, exceptional degrees and the complete contradiction.

ANALYTIC_OBLIGATION_MATRIX.md contains58 entries:55 completed analytic/external
theorem obligations and3 explicit finite computational obligations. The latter
have separately established domain/completeness proofs; none is a stand-in for
an unproved analytic reduction. AUDIT_OBLIGATIONS.json gives the same ledger
in machine-readable form. The independent58-node dependency graph is acyclic;
the original25-node graph was also checked. Semantic dependencies were audited
in addition to that syntactic cycle check.

The critical chain is:

    original coloring -> hereditary caps and contextual49 exclusion
    lower-order + abstract285/286 obstructions -> every R(4,47) core has >=287 edges
    lower-order + AES + complete q20 argument -> R(4,48) floor310 and h12 empty
    complete recurrence/extraction -> T61 with397<=E<=408 and min degree12 or13
    energy-independent COVER -> Q>=29 -> h13 requires E>=407
    E407: Q<=29 from every core, Q>=30 from COVER
    E408: Q<=30 from every core, Q>=31 from COVER
    all T61 alternatives impossible -> K145 contradiction.

CORE211 and the matching lemmas are separated from terminal COVER to avoid
apparent file-level cycles. Contextual49 emptiness is never promoted to a
generic uncolored theorem. The original generic R(4,49) high-energy questions
may remain OPEN without affecting this chain.

## Actual independent computational evidence

Executed using Python3.12.14, standard library only, fixed random seed20261031617.
Command from the repository root:

    python -B r12_master/workstreams/r12-final-certification-chat-20261031/INDEPENDENT_REPLAY.py

No source verifier is imported, and no source enumeration helper is reused.
Reference recurrences run in separate processes only after the independent
table is computed, as comparators. The script records its own SHA256, runtime,
command, each subtask and failures. Any failed subtask now exits nonzero.

|Subtask|Executed result|
|---|---|
|Q27 row multiplicities|19,448 vectors; exactly2 canonical states|
|Q28 row multiplicities|19,448 vectors; exactly8 canonical states, including both B1|
|State reconstruction|81,920 subset identities, EDGE12, alpha(M)<=10,107 regular INS11 checks passed|
|Repivot algebra|312 instances covering d=0..12 and beta=11,12; symbolic derivation supplied separately|
|q20 replay|286 two-hub row vectors; exactly5 equality families r=6..10|
|Four-seed supports|Raw counts9/40/48; orbit counts2/3/5; exact canonical-set comparison passed|
|23-point families|61 constructed;49 valid;12 excluded by alpha>=12;263 maximal independent sets; maximum cost6|
|Finite type compatibility|20 compatible type-set pairs;10 exceptional missing-cross-edge endpoint cases;55 singleton extensions|
|Recurrence|All1,752 entries match both frozen implementations and retained data|
|Outer stops|All144 retained;143 excluded; unique d=11,j=6,a=5,n=61, floor397,budget408|
|Provenance|48 pinned files,26 frozen origins,47 recorded SHA256 values verified|
|DAG|Original25 nodes and independently reconstructed58 nodes acyclic|

INDEPENDENT_REPLAY_RESULTS.json contains complete state keys, adjacency masks,
decorations, all recurrence values and all outer stops. Scalar inequalities
are also checked across their entire bounded domains. The random algebra tests
are explicitly not searches for legal61-point witnesses.

## All fourteen acceptance conditions

|Required condition|Disposition|Evidence|
|---|---|---|
|1 COVER analytic proof|PASS|C1–C8|
|2 Complete Q27/Q28 enumeration|PASS|C3–C4 plus independent full replay|
|3 Q30 terminal classification|PASS|C7 enumerates every regular degree/high-weight cardinality; C8 excludes I/II|
|4 47-point low-edge theorem|PASS|L3–L5; both direct and augmentation routes|
|5 286-edge equality audit|PASS|L6; all ten support orbits and all missing-set intersections|
|6 h12 closure|PASS|F3; generic48-floor and inserted-hub contradiction|
|7 h13 closure|PASS|C8 and F5; pointwise bounds before maximum|
|8 Exceptional degree cases|PASS|F5; <=11 and >=14 excluded, no absent regular-pivot gap|
|9 Recurrence all nodes|PASS|F4 plus1,752-entry comparison|
|10 All144 terminal comparisons|PASS|New complete stop table; sole survivor separately eliminated|
|11 Dependency DAG acyclic|PASS|58-node reconstructed DAG and semantic review|
|12 No unclosed load-bearing premise|PASS|58-row obligation matrix; external theorem conditions verified|
|13 Independent program reproducible|PASS|Executable standard-library program; actual completed run, no source helper imports|
|14 Commit/hash traceability|PASS|Pinned source, raw Git blobs, manifest and SHA256 records|

## Failures, repairs and limits

The first integrity run failed because Windows checkout changed LF to CRLF.
This was repaired by authenticating Git object bytes and checking that checkout
differences were newline-only. The failure is retained in AUDIT_LOG.md and
COUNTEREXAMPLE_AND_GAP_REGISTER.md. No mathematical repair or alteration to
the original source proof was required. A first external PDF fetch timed out
and was subsequently resolved; it was not treated as successful inspection.

PASS here is the audit's mathematical judgment based on the documented informal
proof plus bounded exhaustive computations. It is not a guarantee of infallibility.
No formal proof kernel, external human reviewer or editorial approval is claimed.
The finite shell classification and recurrence should remain explicitly labeled
as computational components in any publication. Root promotion is recommended
through a separate review process only; no Global Root overwrite or merge is
part of this certificate.

Workflow attribution: the peer-review reporting structure is acknowledged with
the verified Scientific Agent Skills reference in PROCESS_SCOPE.md. It is not
a premise or source of any mathematical conclusion in this certificate.
