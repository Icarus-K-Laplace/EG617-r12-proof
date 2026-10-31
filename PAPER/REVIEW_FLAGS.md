# Manuscript review flags and release blockers

Updated: 2026-11-01. This is a working draft, not a claim of submission readiness.

## P0 — required before submission

1. **Full proof transcription audit.** The 286-edge equality argument and COVER terminal classification are long case analyses. The present prose follows the frozen source but still compresses several scalar inequalities and shared-incidence calculations. An independent 31 October adversarial pass corrected the Q30 K4-exclusion text (the outside degree-at-most-two bound now follows from the standing no-middle-degree condition and independence, not circular K4-freeness), made the Q29 maximizing-pivot quantifier explicit, and spelled out the X=3 contribution to the repivot remainder. A scope audit also widened the COVER contract to E<=408 and made Q>=30 explicit throughout that range. Further line-by-line audit remains required.
   **h=4 orbit {01,01,023,23} — closed in the manuscript on 31 October.** The incidence vector is (3,2,2,2), so K0 is a 10-clique and K1,K2,K3 are 11-cliques. A support-01 point cannot be adjacent to every vertex of K1, since that would create a K12; hence, unless it misses both supported cliques, it must be complete to K0. The two K0-completers are nonadjacent and share all ten vertices of K0, so the T=8 common-neighbor bound charges at least seven excess units, disjoint from the six-unit 23 blocker. The apparent opposite-completion subcase is therefore impossible.
The h=4 star orbit {01,02,03,123} is also now expanded in the manuscript. The shared-center degree count gives \(\sum_{K_0}\epsilon\geq\sum_i a_i(b_i-1)\), even when the missing sets overlap; together with the support-point and leaf-missing-set charges this yields \(T\geq\sum_i g(a_i,b_i)\), where every nonempty \(A_i\) contributes at least six. This proves at most one nonempty \(A_i\), after which the common-neighbor bound closes the remaining cases. A standalone derivation is at \`supplement/root/frozen/eq286/H4_STAR_ORBIT_RESOLUTION.md\`.
The h=5 \((9,11,11,11)\) orbit \(\{01,01,02,03,23\}\) has also been expanded: after the \(23\) six-unit charge and the small-budget double-pair lemma, the two mixed points are controlled by a shared-center count on \(K_0\); two nonempty missing sets would cost at least \(5+5\), while one nonempty set combines with the \(23\) blocker through the corrected shared-leaf inequality. See \`supplement/root/frozen/eq286/H5_9_11_11_11_RESOLUTION.md\`.
The h=5 pattern \(D=\{01,02,03,12,13\}\) has now been rewritten as a per-\(K_{10}\)-center argument: two completing mixed points cost at least seven, one completer plus one noncompleter costs at least five, and two noncompleters cost at least eight by pointwise/shared-leaf accounting. The two center charges add to at least ten. A standalone derivation is at \`supplement/root/frozen/eq286/H5_D_10_10_11_11_RESOLUTION.md\`.

2. **Standalone computational supplement.** A source-preserving bundle now exists under `PAPER/supplement/`, including the 26-entry frozen source manifest layout, recurrence inputs, low-edge/286-equality/COVER verifiers and results, case matrix, Q30 adversarial report, H12 sources, root proof DAG and checksums. CI now runs the integrated verifier plus clean temporary-copy reruns of the low-edge, 286-equality and COVER verifiers, and emits a ZIP artifact. Still outstanding: a separate canonical q27/q28 state-key export, explicit q20 adjacency-list export, and a raw 61-representative export. Do not imply that the root verifier reran the full COVER shell search.
3. **Clean LaTeX build.** The latest verified GitHub Actions build is run `41218517505` at commit `3629609835f8c67951ed0b8fba126acd24780e85` (34 pages). I downloaded and inspected its `main.log`; the final log has zero LaTeX/package warnings, unresolved references/citations, or overfull/underfull boxes. Pages 16–22 were also inspected as a contact sheet. The subsequent manuscript edit at `c16fa2203219da450a06b8f214cda0f8274a4f07` expands the Kang–Pikhurko argument and has not yet been rebuilt; rerun CI before treating the current HEAD as build-certified. Target-journal formatting remains outstanding.
4. **Primary-source citation audit.** Kang–Pikhurko is now checked directly against the primary 2005 PDF: Theorem 1 applies at (n,r)=(25,2), and the manuscript spells out why the complement is triangle-free and non-bipartite before using the exact bound 145; see `supplement/root/frozen/eq286/KANG_PIKHURKO_25_VERTEX_APPLICATION.md`. Still check Brooks, Andrásfai–Erdős–Sós, the historical summary of the Erdős–Gyárfás conjecture, and the Xia–Szeider preprint.
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
- LaTeX compilation: latest successful build is commit `3629609835f8c67951ed0b8fba126acd24780e85` (34 pages); final references/citations and layout warnings are clean. The newer Kang–Pikhurko paragraph edit is pending rebuild.
- PDF inspection: pages 1 and 24–33 were previously inspected; pages 16–22 were inspected in the latest 34-page artifact. Full editorial inspection remains open.
- External human review: not yet obtained.
- Submission: not made.
