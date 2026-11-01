# Manuscript review flags and release blockers

Updated: 2026-11-01. This is a working draft, not a claim of submission readiness.

## P0 — required before submission

1. **Full proof transcription audit.** The 286-edge equality argument and COVER terminal classification are long case analyses. An independent 1 November pass proved the independent degree-12 four-set exists by Brooks' theorem, then isolated the private-neighbor decomposition as a standalone structural lemma with no e(H)<=285 hypothesis; it also added an analytic derivation of all ten support orbits (not merely a program-generated orbit count). It also expanded the h=5 pattern D proof into a pointwise shared-K10 excess inequality and an explicit shared-K11 additivity argument. The earlier 31 October adversarial pass corrected the Q30 K4-exclusion text, made the Q29 maximizing-pivot quantifier explicit, and spelled out the X=3 contribution to the repivot remainder. A scope audit widened the COVER contract to E<=408 and made Q>=30 explicit throughout that range. The seven scalar blocker minima now have full positive-integer case splits in `supplement/root/frozen/eq286/SCALAR_BLOCKER_MINIMA.md`. The h=5 D shared-center argument is expanded pointwise in the main text and standalone note. The same-K11-pair terminal now has a standalone exhaustive disjoint-charge proof in `supplement/root/frozen/eq286/SAME_K11_PAIR_OBSTRUCTION.md`. Patterns P and B now have standalone disjoint-charge proofs in `supplement/root/frozen/eq286/H5_P_AND_B_RESOLUTION.md`. The final 286-edge adversarial sweep is complete as an AI-assisted pass (1 November 2026): all ten orbits were rechecked for zero-missing-set and complete-to-clique cases, same-pair intersections, and shared-clique overlap accounting. An independent local enumeration reproduced the raw support counts 9/40/48, orbit counts 2/3/5, and all seven scalar minima/equality cases. No new counterexample or double-counting issue was found. This is not proof-assistant formalization or external human peer review. The E286 private-neighbor decomposition is now stated independently in Lemma lem:private-neighbor-decomposition-e286 of sections/06-equality.tex, with no e(H)<=285 dependency. External human line-by-line review remains open.
   **h=4 orbit {01,01,023,23} — closed in the manuscript on 31 October.** The incidence vector is (3,2,2,2), so K0 is a 10-clique and K1,K2,K3 are 11-cliques. A support-01 point cannot be adjacent to every vertex of K1, since that would create a K12; hence, unless it misses both supported cliques, it must be complete to K0. The two K0-completers are nonadjacent and share all ten vertices of K0, so the T=8 common-neighbor bound charges at least seven excess units, disjoint from the six-unit 23 blocker. The apparent opposite-completion subcase is therefore impossible.
The h=4 star orbit {01,02,03,123} is also now expanded in the manuscript. The shared-center degree count gives \(\sum_{K_0}\epsilon\geq\sum_i a_i(b_i-1)\), even when the missing sets overlap; together with the support-point and leaf-missing-set charges this yields \(T\geq\sum_i g(a_i,b_i)\), where every nonempty \(A_i\) contributes at least six. This proves at most one nonempty \(A_i\), after which the common-neighbor bound closes the remaining cases. A standalone derivation is at \`supplement/root/frozen/eq286/H4_STAR_ORBIT_RESOLUTION.md\`.
The h=5 \((9,11,11,11)\) orbit \(\{01,01,02,03,23\}\) has also been expanded: after the \(23\) six-unit charge and the small-budget double-pair lemma, the two mixed points are controlled by a shared-center count on \(K_0\); two nonempty missing sets would cost at least \(5+5\), while one nonempty set combines with the \(23\) blocker through the corrected shared-leaf inequality. See \`supplement/root/frozen/eq286/H5_9_11_11_11_RESOLUTION.md\`.
The h=5 pattern \(D=\{01,02,03,12,13\}\) has now been rewritten as a per-\(K_{10}\)-center argument: two completing mixed points cost at least seven, one completer plus one noncompleter costs at least five, and two noncompleters cost at least eight by pointwise/shared-leaf accounting. The two center charges add to at least ten. A standalone derivation is at \`supplement/root/frozen/eq286/H5_D_10_10_11_11_RESOLUTION.md\`.

2. **Standalone computational supplement.** A source-preserving bundle now exists under `PAPER/supplement/`, including the 26-entry frozen source manifest layout, recurrence inputs, low-edge/286-equality/COVER verifiers and results, case matrix, Q30 adversarial report, H12 sources, root proof DAG and checksums. CI now runs the integrated verifier plus clean temporary-copy reruns of the low-edge, 286-equality, q20 equality and COVER verifiers, and emits a ZIP artifact. The standalone exports are now present: `cover/Q27_Q28_CANONICAL_STATE_KEYS.json` contains all ten q27/q28 canonical necessary shell states (2+8), and `frontend/T61_H_ROW_LEDGER.json` contains the exact 61 scalar recurrence rows for h=0,...,60. `VERIFY_PUBLIC_EXPORTS.py` checks source equality, Git-blob provenance and S3 canonicality, and CI runs this check. Important scope distinction: the 61-row file is a scalar h-ledger, not 61 adjacency-list graph witnesses. The five q20 adjacency-list normal forms are exported in `supplement/h12/Q20_EQUALITY_ADJACENCY_LISTS.json`; CI runs `VERIFY_Q20_EQUALITY.py` over all five forms and 40 leaf-repivot upper bounds. The workflow path filter now includes all supplement files, so changes to verifiers and JSON inputs trigger CI. Do not imply that the root verifier reran the full COVER shell search.
3. **Clean LaTeX build.** The manuscript source snapshot `9c0e243b8970142a060bca8317ef36817837ec2d` was built successfully in GitHub Actions run `41281119965` using TeX Live 2025; it produced a 37-page PDF (522,827 bytes). The final `pdflatex` pass has no unresolved-reference/citation or overfull/underfull-box warnings. The same run passed the integrated root verifier, clean temporary-copy reruns of the low-edge, 286-equality, q20 equality and COVER verifiers, and the standalone public-export verifier. It uploaded manuscript/replay and source-supplement artifacts. Pages 16–23 and the updated pages 1–3 have been visually spot-checked; full editorial inspection remains open. Target-journal formatting remains outstanding.
4. **Primary-source citation audit — complete (1 November 2026).** The Erdős–Gyárfás original (1999), Conjecture 1 p. 80 and Lemmas 1–2 pp. 84–85, confirms the formulation and the established cases r=3,4. Brooks' original 1941 paper was checked in the full reprint in Stiebitz et al., Appendix A.1, pp. 537–540: maximum degree at most n>2 and no connected component an n-simplex imply an n-coloring; for H[X], n=12 and omega(H[X])<=11 exclude a K13 component. The original Andrásfai–Erdős–Sós paper, Theorem 1.1 p. 207, gives K4-free plus delta>5n/8 implies 3-partite; the application has n=35, delta=22, and 8*22=176>175. The original Kang–Pikhurko PDF, Theorem 1 p. 13, gives p_r(n)=t_r(n)-floor(n/r)+1 for n>=r+3 and r<=(n-1)/2; at (n,r)=(25,2), this is 156-12+1=145. The Xia–Szeider arXiv preprint 2610.24484 (v1, 17 October 2026), abstract and Theorem 1, states the r=5 result and its Lean/SAT certificate architecture; the introduction now explicitly identifies it as an arXiv preprint rather than implying journal publication. Bibliographic metadata in references.bib was cross-checked against the primary records. The bibliography and introduction now also record the public 2026 claims for fixed r=5,...,11, distinguishing the Sneiderman r=5--9 artifacts from the Terpstra/Codex r=10,11 pre-review release and the secondary claim index. This source audit does not replace external human peer review.
5. **Independent human review.** Obtain at least one external combinatorialist's line-by-line review. The AI-assisted certification PASS is not human peer review.

## External prior-art audit (1 November 2026)

The public claims index now records unrefereed 2026 claims for every fixed parameter
$r=5,\ldots,11$. The Sneiderman repository contains individual $r=5,6,7,8,9$
manuscripts and proof artifacts; the Terpstra Research repository contains the
pre-review $r=10,11$ artifact. Multiple additional independent $r=5$ write-ups
are also catalogued. The introduction cites these as claims only and explicitly
states that none is used as a premise in this proof. Do not describe $r=12$ as
the "next" fixed case, and do not claim novelty beyond the scoped public search.

A further caution concerns the Sneiderman $r=7,8,9$ source snapshots. An
AI-assisted screening note by the Erdős Problems project reports a shared
inference gap in the Kang--Pikhurko equality discussion at $m=ar+1$: the total
size $ar$ of the old parts does not, by itself, imply that every old part has
size $r$. The reported repair is to split into (i) a part larger than $r$, which
already gives a forbidden target clique, and (ii) all parts of size at most $r$,
where equality of the total forces every part to have size $r$. The same note
says the linked July 2026 release sources do not contain the repair and that a
later 25 July version does; the current public r7-r8 source snapshot fetched for
this audit still displays the unqualified inference. The screening note is
explicitly not human peer review. Our proof does not cite or use these
Sneiderman arguments. A targeted scan of our current Sections 3--4 did not
find this exact old-part inference, but this is not a substitute for the
independent line-by-line audit required in P0 item 1.

The Terpstra r10/r11 repository labels its release pre-review and not
proof-assistant formalized or externally peer reviewed. It reports separate
clean-room computational audits, while also disclosing a repaired executable
omission in a frozen r11 audit script. This is recorded as a claim and a
reproducibility artifact, not an accepted theorem.

The broad least-color/minimum-degree/clique-packing architecture with
simultaneous cross-color density constraints is already present in the
r10/r11 claim. The present manuscript therefore claims the fixed-r=12
terminal argument, not novelty of that general reduction template.

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
- Supplementary machine assets: source-preserving bundle in `supplement/`; CI ZIP artifact and clean verifier reruns are enabled. q20 adjacency-list export, ten q27/q28 canonical necessary-state keys, and the 61-row T61 h-ledger are all present. `VERIFY_PUBLIC_EXPORTS.py` and CI check their exact source equality, Git-blob provenance and canonicality. The T61 `core` entries preserve the earlier recurrence seeds (308/284 for h=12/13); later independent lemmas strengthen the abstract floors to 310/287. These are scalar recurrence records, not full graph witnesses.
- LaTeX compilation: latest successful TeX source snapshot is `9c0e243b8970142a060bca8317ef36817837ec2d` (37 pages; 522,827 bytes), Actions run `41281119965`; final TeX pass is clean. The integrated root verifier, low-edge, 286-equality, q20 equality, COVER, and standalone public-export verifier all passed. Pages 1–3 were visually checked after updating the title date and prior-art positioning.
- PDF inspection: pages 16–23 have been spot-checked in the current 37-page artifact. Full editorial inspection remains open.
- External human review: not yet obtained.
- Submission: not made.
