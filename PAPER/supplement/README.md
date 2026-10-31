# EG617(r=12) computational and proof-source supplement

This directory is a source-preserving bundle of selected proof and verification assets used by the manuscript. It is not a substitute for reading the analytic arguments in the main paper.

## Frozen provenance

- Integrated mathematical proof snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.
- Independent AI-assisted certification snapshot: `09a88cc4fe1e2cf1f3a87475d6484f681910b23e`.
- Adversarial Q30 referee report: `a0f922ad09af99575bae581864b673aa4d41f00d`.
- The files copied from these commits are preserved as-is except for their destination paths. Their original provenance is recorded in the directory names and this note.

## Layout

- `frontend/`: two independent recurrence implementations, replay input, recurrence proof and front-end verifier/result.
- `low/`: low-edge verifier and its result, plus the minimum-degree gate and analytic low-edge proof sources.
- `equality286/`: 286-edge equality verifier, result, checksum file and analytic classification.
- `h12/`: the 48-vertex floor and T61 degree-12 terminal closure.
- `cover/`: COVER verifier, result, case matrix, analytic theorem, dependency audit and independent Q30 referee report.
- `root/`: integrated proof, dependency DAG, source manifest, checksums, root verifier and its recorded result.

## Reproduction boundary

The Python programs use the Python standard library. Run each verifier from its own directory so that its `Path(__file__).resolve().parent` inputs and outputs resolve as intended. The front-end recurrence programs are independent integer implementations. The root verifier checks the integrated arithmetic/dependency snapshot; its own docstring expressly says it does **not** rerun the 47-vertex graph search or COVER shell search.

The COVER verifier reconstructs the finite shell states described in `cover/COVER_THEOREM.md`; it does not certify the analytic reductions leading to those states. Likewise, finite verifier PASS records do not constitute a proof-assistant kernel or independent human peer review.

Before publication, run all bundled scripts in a clean environment, record the Python version and output hashes, and reconcile each generated output with the pinned result files. The current manuscript workflow compiles the LaTeX paper only; it does not yet execute these Python verifiers.
