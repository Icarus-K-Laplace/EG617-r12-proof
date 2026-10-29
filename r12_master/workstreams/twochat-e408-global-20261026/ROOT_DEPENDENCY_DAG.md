# EG617 fixed r=12 — root dependency DAG (independent fail-closed audit)

Updated: 2026-10-29  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-twochat-e408-global-20261026  
Audited HEAD before this audit commit: bb8b1e696ecf199f337d8d0db69d00132191f80f  
Status: **OPEN / NOT_CERTIFIED — FAIL-CLOSED**  
Promotable root receipt: **NOT ISSUED**

## Status vocabulary

- **PROVED** — unconditional derivation from stated hypotheses.
- **PROVED_CONDITIONAL** — valid only under explicit local/parent/external hypotheses.
- **COMPUTATION_CERTIFIED** — exact finite computation independently replayed from identified inputs; it does not prove an analytic parent-coverage theorem.
- **OPEN** — a required theorem, artifact, replay, or parent-coverage edge is missing.
- **RETRACTED** — a prior load-bearing inference is invalid and cannot be used.

## Dependency DAG

~~~mermaid
flowchart TD
  K[Hypothetical balanced 12-edge-colouring of K145] --> FE[Front-end exact recurrence and dichotomy]
  FE --> R449[Contextual R(4,49) exclusion<br/>PROVED_CONDITIONAL]
  FE --> T61[T61 residual, 397<=E<=408]
  T61 --> H12[h12 closure<br/>PROVED_CONDITIONAL]
  T61 --> LOW[E397-E406 closures<br/>PROVED_CONDITIONAL]
  T61 --> E407[E407 / h13]
  T61 --> E408[E408 / h13]
  E407 --> Q31a[E407 Q31 / V10-V11<br/>COMPUTATION_CERTIFIED + CONDITIONAL]
  E407 --> V12[V12 finite screen<br/>OPEN: source/replay missing]
  V12 --> CONTRACT29[29-point / 49-block parent contract<br/>OPEN at parent coverage]
  CONTRACT29 --> RES29[Local reserve 294+22>310<br/>PROVED_CONDITIONAL]
  E408 --> Q31b[E408 Q31 / V11<br/>COMPUTATION_CERTIFIED + CONDITIONAL]
  E408 --> Q32NF[Q32 v=44,45,46; all m=8,9,10<br/>PROVED_CONDITIONAL via sibling imports]
  E408 --> Q32FS[Q32 full support v=47<br/>OPEN: m=8,9 and part of m=10]
  E408 --> Q33[E408 Q33: e(H)=284, excess=4]
  Q33 --> MIN31[56-witness support v>=31]
  MIN31 --> LOCAL31[Exact v=31 reserve<br/>PROVED_CONDITIONAL]
  MIN31 --> PROMOTE[Support promotion v>31<br/>OPEN]
  PROMOTE --> HIGH[High-support scalar reserve<br/>only m=8 at v=32 excluded]
  Q32FS --> ROOT[EG617(r=12) root theorem<br/>OPEN / NOT_CERTIFIED]
  RES29 --> ROOT
  LOCAL31 --> ROOT
  HIGH --> ROOT
~~~

## Root chain and edge ledger

| ID | Parent-to-child obligation | Status | Source and precise limitation |
|---|---|---|---|
| FE-1 | Hypothetical balanced K145 counterexample reduces to contextual R(4,49) or embedded T61 | PROVED_CONDITIONAL + COMPUTATION_CERTIFIED under named inputs | front_end/FRONTEND_BRIDGE_THEOREM.md; front_end/ASSUMPTION_LEDGER.md. The reported exact recurrence has 1,752 nodes and 144 stopping comparisons; this finite certificate is distinct from the later T61 graph closures. |
| FE-2 | Contextual R(4,49) alternative is impossible | PROVED_CONDITIONAL | front_end/CONTEXTUAL_R449_FULL_COLOR_IMPOSSIBILITY.md and front_end/ASSUMPTION_LEDGER.md. Brouwer/second-Turán assumptions retain their recorded order, clique, and non-partite hypotheses; this audit does not re-prove the external theorem. |
| T61-1 | Actual-minimum-degree-12 T61 branch | PROVED_CONDITIONAL | T61_H12_CLOSURE.md under its registered core/extremal assumptions. |
| T61-2 | h13 energies E397-E406 | PROVED_CONDITIONAL | T61_H13_LOW_LAYER.md, E401_E404_CANONICAL_CLOSURE.md, E405_FULL_CLOSURE_CANONICAL.md, E406_FULL_CLOSURE.md; each source's own contract remains in force. |
| E407-31 | E407 Q31 closure | PROVED_CONDITIONAL + COMPUTATION_CERTIFIED under V10/V11 inputs | V10 archive SHA256 e83e2907d541b38304746e855af52b5e21b6500a35cb0fdb676a4f6a7601303a; V11 archive SHA256 27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4; V11 certificate SHA256 0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b. External/analytic inputs remain conditional. |
| E407-32-V12 | V12 computation enumerates all relevant kernels/states/shells and maps all reported survivors to five templates | OPEN | Reported archive SHA256 0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36; reported certificate SHA256 cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30; counts 8,677 / 17,957 / 1,984 / 554 are source reports only. No archive, manifest, or verifier found in any of the 30 branch trees; source report explicitly says INDEPENDENT_REPLAY_PENDING. |
| E407-32-LOCAL | Given exactly 29 support points, 49 pairwise edge-disjoint selected four-blocks, and the complement-edge ledger e(L_U)<=310, one unselected color needs p12(29)=22 edges | PROVED_CONDITIONAL | E407_FOUR_COLOR_U_RESERVE_CLOSURE.md; 49*C(4,2)=294 and 294+22=316>310. This is a local contradiction, not proof of the parent contract. |
| E407-32-TEMPLATE-CONTRACT | A legal completion of any one V12 template has the 29-point/49-block support object and selected-component anchor identity | PROVED_CONDITIONAL | FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md and SUPPORT_BLOCK_ANCHOR_IDENTITY.md in sibling branch workstream/r12-twochat-e407-closure-20261026. This interface depends on the retained V12 analytic/minimum-support chain and exact-129 factor theorem; it does not certify the finite survivor mapping. |
| E407-32-V12-PROMOTION | Every legal E407 Q32 parent is covered by the complete V12 finite screen and maps to a template A-E | OPEN | Archive, manifest, and verifier are absent; V12_V8_SOURCE_REPORTED_AUDIT.md says INDEPENDENT_REPLAY_PENDING. The reported 554 survivor-to-template mapping has not been independently replayed. The sibling's broader compatibility workstream remains OPEN / NOT_CERTIFIED. |
| E408-31 | E408 Q31 closure | PROVED_CONDITIONAL + COMPUTATION_CERTIFIED under V11 inputs | V10_V11_Q31_INDEPENDENT_REPLAY_AUDIT.md; retain its named analytic and external assumptions. |
| E408-32-NONFULL | E408 Q32 supports v=44,45,46 are impossible for every m in {8,9,10} | PROVED_CONDITIONAL (read-only sibling import) | Low-support branch workstream/r12-q32-caseII-v44-final-20261028 at 9afd7c1a59056052974f9dc78933010d10e88bba and high-support branch workstream/r12-q32-highsupport-root-20261028 at c6500b24dc78cd4c56cd90219080003aeb8e3cb5. See Q32_NONFULL_SUPPORT_SIBLING_IMPORT_AUDIT.md for the proof-to-row map. This root branch did not independently re-prove every analytic lemma. |
| E408-32-FULL | E408 Q32 full support v=47 | OPEN | Latest high-support sibling HEAD c6500b24dc78cd4c56cd90219080003aeb8e3cb5 has corrected source-outside-profile validation, malformed-witness checks, and a wired monochromatic-K6 separator. However, model and verifier still encode target count 398+m with color 11 fixed at 132, wrong for m=8,9. The exact count-vector regression validates bookkeeping only; no full Z3 solve or graph-level UNSAT certificate exists. m=8,9 remain open; for m=10, chi(complement residual)>=5 is closed but chi<=4 remains open. No Q33 excess-four identity is imported. |
| E408-33-SUPPORT | Eight selected exact-129 colors supply 56 selected component/gadget witnesses with support v>=31 | PROVED_CONDITIONAL | R12_ZERO_EXCESS_WITNESS_THEOREM.md and the retained exact-129 factor theorem. The lower bound v>=31 does not imply v=31. |
| E408-33-LOCAL | Under exactly v=31 and the registered 284-edge/56-witness ledger, nonexact-color reserve excludes m=8,9 and the separate component-capacity theorem excludes m=10 | PROVED_CONDITIONAL | Q33_NONEXACT_U_RESERVE_CLOSURE.md and Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md. Uses p12(31)=26, delta<=17, h<=4; no degree-nine assumption. |
| E408-33-PROMOTION | Every Q33 parent has a selected 56-witness union of exactly 31 points, or all larger supports are excluded | OPEN | No equality/support-promotion theorem found. Independent necessary-capacity replay excludes m=8,9 at v=31 and m=8 at v=32 only; m=9,10 at v=32 and m=8,9,10 for v>=33 remain open under this scalar reserve. |
| KP-1 | Exact-129 Type-I factorization | PROVED_CONDITIONAL | KANG_PIKHURKO_EXACT129_SOURCE_AUDIT.md. The cited equality structure gives ten isolated K5 components plus an 11-vertex gadget under the recorded hypotheses. |
| KP-2 | Universal degree-nine exceptional vertex and exceptional-injectivity closure | RETRACTED | KP_DEGREE9_RETRACTION_AND_E408_Q32_REOPEN.md; correct variable degree pairs are (5,8), (6,7), (7,6), (8,5). |
| EXT-1 | Turán floors and small overlap-profile minimizations used by the reserve table | PROVED for the displayed arithmetic | verify_q33_high_support_u_reserve.py; independently replayed with Python standard library. This does not certify a graph realization or parent coverage. |
| EXT-2 | Brouwer/second-Turán, Kang–Pikhurko, and other external extremal/Ramsey inputs | PROVED_CONDITIONAL | front_end/ASSUMPTION_LEDGER.md and KANG_PIKHURKO_EXACT129_SOURCE_AUDIT.md record sources and parameter maps. The present audit does not strengthen the external theorem hypotheses. |

## V12 artifact search record

Repository-wide branch inventory returned 30 branches. All 30 branch trees were searched for T61_H13_V12.zip and V12-related manifest/verifier/certificate names. No matching archive, manifest, or verifier was found. The only V12-named path is consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md, whose status is SOURCE_REPORTED / INDEPENDENT_REPLAY_PENDING. GitHub releases endpoint: 0 releases. Commit-history query for exact path T61_H13_V12.zip: 0 commits. Reported hashes are not treated as proof of file availability or replay.

## Root promotion rule

A root receipt cannot be promoted until all of these gates close:

1. E408 Q32 source-correct 285-edge/excess-six graph terminal.
2. E407 Q32 V12 artifact/replay and independent verification that every legal parent/survivor maps to a template A-E; the template-local support contract remains conditional on its registered inputs.
3. E408 Q33 universal 31-point support selection theorem or complete proof excluding all remaining v=32..47 cases.

The exact-129 factor theorem may be used under its source hypotheses. Degree-nine exceptional-vertex claims may not be used. A successful local reserve inequality cannot replace a missing parent-coverage edge.


## 14. Q32 support-layer integration — 2026-10-29

The old single E408-32 row is split into a conditional non-full-support closure and the remaining full-support gate. This is status reconciliation, not a new root theorem. Sibling sources remain read-only; the current root workstream does not claim independent proof-assistant verification of the imported analytic lemmas.


## 15. Full-support CSP audit gate — 2026-10-29

The high-support sibling's vertex-labelled CSP is not a proof artifact until its E408 count vector is corrected for m=8,9 and its independent verifier accepts every source-permitted outside-count placement. No solver output is imported at this stage.


## 16. Latest full-support CSP source audit — 2026-10-29

The latest read-only sibling is workstream/r12-q32-highsupport-root-20261028 at c6500b24dc78cd4c56cd90219080003aeb8e3cb5. Its independent candidate verifier now accepts the registered source-correct outside-count modes and has regression fixtures. The E408 count-vector mismatch remains in both model and verifier. See Q32_FULLSUPPORT_CSP_SOURCE_AUDIT.md and verify_q32_fullsupport_count_vector_contract.py. No solver output is imported.


## 17. Latest full-support CSP source audit — 2026-10-29

The read-only high-support sibling is now at c6500b24dc78cd4c56cd90219080003aeb8e3cb5. The source-mode checker is corrected and the model now wires in a monochromatic-K6 separator. The E408 count-vector mismatch remains in both model and independent verifier for m=8,9. No solver output is imported.
