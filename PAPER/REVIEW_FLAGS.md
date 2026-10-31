# Manuscript review flags and release blockers

Updated: 2026-10-31. This is a working draft, not a claim of submission readiness.

## P0 — required before submission

1. **Full proof transcription audit.** The 286-edge equality argument and COVER terminal classification are long case analyses. The present prose follows the frozen source but still compresses several scalar inequalities and shared-incidence calculations. An independent 31 October adversarial pass corrected the Q30 K4-exclusion text (the outside degree-at-most-two bound now follows from the standing no-middle-degree condition and independence, not circular K4-freeness), made the Q29 maximizing-pivot quantifier explicit, and spelled out the X=3 contribution to the repivot remainder. A scope audit also widened the COVER contract to E<=408 and made Q>=30 explicit throughout that range. Further line-by-line audit remains required.
   **h=4 orbit {01,01,023,23} — closed in the manuscript on 31 October.** The incidence vector is (3,2,2,2), so K0 is a 10-clique and K1,K2,K3 are 11-cliques. A support-01 point cannot be adjacent to every vertex of K1, since that would create a K12; hence, unless it misses both supported cliques, it must be complete to K0. The two K0-completers are nonadjacent and share all ten vertices of K0, so the T=8 common-neighbor bound charges at least seven excess units, disjoint from the six-unit 23 blocker. The apparent opposite-completion subcase is therefore impossible.

2. **Standalone computational supplement.** A source-preserving bundle now exists under `PAPER/supplement/`, including the 26-entry frozen source manifest layout, recurrence inputs, low-edge/286-equality/COVER verifiers and results, case matrix, Q30 adversarial report, H12 sources, root proof DAG and checksums. CI now runs the integrated verifier plus clean temporary-copy reruns of the low-edge, 286-equality and COVER verifiers, and emits a ZIP artifact. Still outstanding: a separate canonical q27/q28 state-key export, explicit q20 adjacency-list export, and a raw 61-representative export. Do not imply that the root verifier reran the full COVER shell search.
3. **Clean LaTeX build.** A clean GitHub Actions TeX Live 2025 build succeeds at commit `67926d44543a10ff73a185f2c83d460f12a2d946` (33 pages). The final `main.log` has no unresolved references/citations or overfull/underfull boxes. The full-page contact sheet was checked and pages 1 and 24–33 were inspected at reading resolution; target-journal formatting remains outstanding.
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
- LaTeX compilation: successful at commit `67926d44543a10ff73a185f2c83d460f12a2d946` (33 pages); final references and citations resolve, with no final-log layout warnings.
- PDF inspection: selected pages 1 and 24–31 inspected; full editorial inspection remains open.
- External human review: not yet obtained.
- Submission: not made.
