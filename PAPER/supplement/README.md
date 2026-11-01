# EG617(r=12) computational and proof-source supplement

This directory is a source-preserving bundle of selected proof and verification assets used by the manuscript. It is not a substitute for reading the analytic arguments in the main paper.

## Frozen provenance

- Integrated mathematical proof snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.
- Independent AI-assisted certification snapshot: `09a88cc4fe1e2cf1f3a87475d6484f681910b23e`.
- Adversarial Q30 referee report: `a0f922ad09af99575bae581864b673aa4d41f00d`.
- The files copied from these commits are preserved as-is except for their destination paths. Their original provenance is recorded in the directory names and this note.

## Layout

- `frontend/`: two independent recurrence implementations, replay input, recurrence proof, and the standalone 61-row T61 h-ledger export. The 61 rows are scalar recurrence rows for h=0,...,60, not graph witnesses. Its `core` column preserves the earlier recurrence seeds (308/284 at h=12/13); later separate theorems strengthen the abstract 48/47-point floors to 310/287. The integrated root verifier is in `root/`.
- `low/`: low-edge verifier and its result, plus the minimum-degree gate and analytic low-edge proof sources.
- `equality286/`: 286-edge equality verifier, result, checksum file and analytic classification.
- `h12/`: the 48-vertex floor and T61 degree-12 terminal closure.
- `cover/`: COVER verifier, result, case matrix, analytic theorem, dependency audit, independent Q30 referee report, and the standalone q27/q28 canonical necessary-state keys.
- `root/`: integrated proof, dependency DAG, source manifest, checksums and root verifier. Its `frozen/` subdirectory mirrors all 26 source-manifest entries at the exact relative paths expected by the verifier.

## Reproduction boundary

The Python programs use the Python standard library. Verify the standalone T61 and q27/q28 exports from the repository root with `python3 -B PAPER/supplement/VERIFY_PUBLIC_EXPORTS.py`; it checks exact source equality, Git-blob provenance, and S3 canonicality. The T61 export is the original recurrence ledger: its core entries are historical seed bounds, not the later strengthened abstract floors. Run the integrated verifier from `root/` with `python3 -B INDEPENDENT_VERIFIER.py`. It checks all 26 Git-blob hashes, replays the three recurrence implementations, reruns the retained COVER state verifier, checks the low-order finite routines, and validates the dependency DAG. For standalone low-edge, 286-equality and COVER reruns, use temporary copies of `root/frozen/low`, `root/frozen/eq286` and `root/frozen/cover`; those scripts overwrite their adjacent result JSONs, so do not run them in-place before the root source-hash check. The root verifier expressly does **not** rerun the 47-vertex graph search or COVER shell search.

The COVER verifier reconstructs the finite shell states described in `root/frozen/cover/COVER_THEOREM.md`; it does not certify the analytic reductions leading to those states. The 104 repivot checks are generic algebra tests, not legal-parent witnesses. Likewise, finite verifier PASS records do not constitute a proof-assistant kernel or independent human peer review.

The manuscript CI now compiles the paper, runs the root verifier, reruns low-edge/286-equality/COVER verifiers on temporary copies, and uploads both the PDF/replay outputs and a ZIP of this supplement. Record the exact workflow run and output hashes before publication.
