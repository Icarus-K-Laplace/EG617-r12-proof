# Manuscript review flags and release blockers

Updated: 2026-10-31. This is a working draft, not a claim of submission readiness.

## P0 — required before submission

1. **Full proof transcription audit.** The 286-edge equality argument and COVER terminal classification are long case analyses. The present prose follows the frozen source but still compresses several scalar inequalities and shared-incidence calculations. Expand these calculations and cross-check line by line against the pinned source and the independent certificate.
2. **Standalone computational supplement.** Bundle the recurrence implementations, canonical q27/q28 state keys, 81,920 subset checks, q20 equality structures, independent verifiers, raw outputs and SHA-256 manifest. Explain which searches were rerun and which were authenticated from frozen prior outputs. Do not imply that the final verifier reran the full COVER shell search.
3. **Clean LaTeX build.** Compile with a clean TeX Live installation, resolve all warnings/errors, check bibliography and all cross-references, inspect the resulting PDF visually, and record the TeX Live version and exact build command.
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
- Supplementary machine assets: not yet bundled.
- LaTeX compilation: not yet run.
- PDF inspection: not yet run.
- External human review: not yet obtained.
- Submission: not made.
