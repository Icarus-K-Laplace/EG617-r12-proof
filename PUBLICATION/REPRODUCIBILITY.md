# Reproducibility and verification

## Frozen source objects

- Integrated proof: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`
- Independent certification: `09a88cc4fe1e2cf1f3a87475d6484f681910b23e`

Use a full clone of the repository so Git object provenance checks can access the pinned source commits.

## Independent certification replay

The certification report records Python 3.12.14 and the standard library only.

From the repository root, after checking out the certification commit or its branch:

```bash
python -B r12_master/workstreams/r12-final-certification-chat-20261031/INDEPENDENT_REPLAY.py
```

The script computes its independent finite tables and checks the recorded certificates. It does not import the original verifier or reuse the original enumeration helper. It records the finite arrays, all 1,752 recurrence entries and all 144 outer stops. Runtime/environment fields may vary; compare mathematical arrays and state keys.

The script's scope is not an exhaustive search over all 61-vertex graphs. It replays the bounded finite obligations after the analytic reductions and completeness mappings documented in the certification report.

## Integrated verifier

From a full clone with the integrated proof branch fetched:

```bash
python -B r12_master/workstreams/astra-global-root-integration-chat-20261031/INDEPENDENT_VERIFIER.py
```

Read the corresponding `VERIFICATION_RESULT.json`, `FRONTEND_REPLAY.json`, `SHA256SUMS.txt`, and `SOURCE_MANIFEST.json`. The independent certification report explains precisely which checks are replayed and which graph searches are not rerun.

## What a successful replay means

A successful run confirms the specified finite arithmetic/state checks and file provenance. It does not by itself prove the analytic reductions, replace human mathematical review, or create a Lean proof. The analytic derivations and the graph-to-state completeness arguments must be read in the frozen proof and certification documents.

## Suggested clean-checkout procedure

```bash
git clone https://github.com/Icarus-K-Laplace/EG617-r12-proof.git
cd EG617-r12-proof
git fetch origin workstream/r12-final-certification-chat-20261031
git checkout 09a88cc4fe1e2cf1f3a87475d6484f681910b23e
python -B r12_master/workstreams/r12-final-certification-chat-20261031/INDEPENDENT_REPLAY.py
```

If the repository is still private, the GitHub account must have access. After a public release, the same pinned commit remains the reproducibility target.

## Provenance

The integrated proof's `SOURCE_MANIFEST.json` records frozen source commits, paths and Git blob identities. The certification package records raw Git object checks and SHA256 manifests. Always cite the pinned commit rather than a moving branch head.

## Post-audit supplementary arithmetic checks (5 November 2026)

The publication supplement contains two additional standard-library Python checkers:

```bash
python -B PAPER/supplement/root/RECHECK_E286_COVER_INTERFACE_20261103.py
python -B PAPER/supplement/root/RECHECK_H13_Q30_X3_BRANCH.py
```

The first checks the ten four-seed support orbits, listed scalar minima, shared-center overlap inequalities, the E407/E408 pivot ledger, and the d=2 K4 repivot arithmetic. The second checks all 36 positive pair-type distributions in the h13 Q30 |X|=3 local rho identity. Their recorded JSON outputs are included next to the scripts.

These scripts verify only their finite arithmetic/quotient domains. They do not search all 47- or 61-vertex graphs, establish the analytic completeness of the graph reductions, or execute the integrated root verifier. Regenerate the JSON outputs when reproducing the scripts; do not treat the checked-in outputs as evidence of a fresh clean-room run.

## Current clean-room boundary

The integrated root verifier has not yet been executed from a fresh checkout as part of the 5 November publication-corrections branch. A clean-room acceptance must pin the exact integration commit, fetch all source commits required by the manifest, run the integrated verifier and the independent replay, capture environment and exit codes, and compare regenerated outputs. The verifier itself is a finite arithmetic/provenance checker, not a proof-assistant kernel.
