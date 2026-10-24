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

### Publication and verification record

Proof/certificate commit:
`b74f116e5cff3dd3f6d335e27ffe7142b0454471`.
Published successfully on the requested branch on 2026-10-25.
The comparison against its base contains exactly eleven added files,
all within `general_r/workstreams/astra-dlow-terminal-20261024/`.

Verification commands: `python verify.py --write`, then
`python verify.py`. Both completed successfully. The second execution
recomputed the certificate from scratch and compared parsed JSON.

Exact checks include:
- polynomial coefficient identity for the cut capacity and contextual cap;
- all nine offset rows, with linear-in-r positive-margin certificates;
- all seven kernel sizes and the elementary random-order edge floor;
- all 33,867 labeled graphs of orders 1 through 6, filtering all 6,228
  triangle-free graphs and verifying the sparse lemma on all 866 graphs
  satisfying e-tau<=1;
- every one of the 2,048 subsets of the explicit eleven-point split-cover
  graph, certifying 29 edges, independence two, and clique number five.

The final proof has no finite graph-enumeration dependency: the sparse
lemma and the kernel capacity have complete analytic proofs. The
small-graph checks are regression and countermodel verification.

Final scope: D_low is PROVED for every integer r>=221; all high-degree
offset cells are PROVED for r>=209. The full range starting at 67 is
OPEN below these thresholds, with the eta-specific partial exclusions
listed in OFFSET_CLASSIFICATION.md. A_ext* remains OPEN.
