# Manuscript review flags and release blockers

Updated: 2026-10-31. This is a working draft, not a claim of submission readiness.

## P0 — required before submission

1. **Full proof transcription audit.** The 286-edge equality argument and COVER terminal classification are long case analyses. The present prose follows the frozen source but still compresses several scalar inequalities and shared-incidence calculations. Expand these calculations and cross-check line by line against the pinned source and the independent certificate.
2. **Standalone computational supplement.** A source-preserving bundle now exists under `PAPER/supplement/`, including the 26-entry frozen source manifest layout, recurrence inputs, low-edge/286-equality/COVER verifiers and results, case matrix, Q30 adversarial report, H12 sources, root proof DAG and checksums. CI now runs the integrated verifier plus clean temporary-copy reruns of the low-edge, 286-equality and COVER verifiers, and emits a ZIP artifact. Still outstanding: a separate canonical q27/q28 state-key export, explicit q20 adjacency-list export, and a raw 61-representative export. Do not imply that the root verifier reran the full COVER shell search.
3. **Clean LaTeX build.** A clean GitHub Actions TeX Live 2025 build succeeds at commit `1f4862d0fe4ba0d95324da3c3173863014088634` (33 pages). The final log has no unresolved references/citations or overfull/underfull boxes. Selected pages 1 and 24–31 were visually inspected; full-page-by-page editorial inspection and target-journal formatting remain outstanding.
4. **Primary-source citation audit.** Check the exact theorem statements and parameter ranges for Brooks, Andrásfai–Erdős–Sós, and Kang–Pikhurko against the original papers. Verify the historical summary of the Erdős–Gyárfás conjecture and the Xia–Szeider preprint.
5. **Independent human review.** Obtain at least one external combinatorialist's line-by-line review. The AI-assisted certification PASS is not human peer review.

## P1 — required before public preprint

- Confirm the complete author list, author order, affiliations, corresponding author and email. This draft provisionally lists Qiankai Tong as lead author and does not invent an affiliation.
- Add a contribution statement based on actual human contributions. Do not list AI systems as authors.
- Add the journal-compliant AI-use disclosure and confirm the target venue's policy.
- Add an explicit data/code availability statement and archive the exact reproducibility bundle.
- Select a journal template only after the proof text and supplement are stable.
- Prepare a cover letter that states only the fixed-r=12 theorem and does not claim the general conjecture is solved.

## Scope statements that must not be weakened

- The result is the fixed (r=12) case only.
- The proof is an informal mathematical proof with finite computational verification; it is not Lean/Coq formalization.
- The independent certification is AI-assisted, not external human peer review.
- The abstract uncolored high-energy (R(4,49)) problem remains open/outside the dependency path; the proof uses a contextual full-coloring contradiction.
- The finite verifier does not exhaustively search all 61-vertex graphs and does not rerun the original COVER shell search.

## Current manuscript state

- Main theorem and proof architecture: drafted.
- Main proof sections: source-derived first transcription completed.
- Supplementary machine assets: source-preserving bundle in `supplement/`; CI ZIP artifact and clean verifier reruns are enabled. Canonical state-key, q20 adjacency-list and raw 61-representative exports remain open.
- LaTeX compilation: successful at commit `1f4862d0fe4ba0d95324da3c3173863014088634` (33 pages); final references and citations resolve.
- PDF inspection: selected pages 1 and 24–31 inspected; full editorial inspection remains open.
- External human review: not yet obtained.
- Submission: not made.
