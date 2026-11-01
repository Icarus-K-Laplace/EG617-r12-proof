# EG617(r=12) manuscript workspace

**Status: substantial source-derived working draft; not submission-ready.**

## Build layout

- `main.tex` is the paper root.
- `sections/01-introduction.tex` through `sections/09-global-and-computation.tex` contain the theorem statement and the source-derived proof.
- `references.bib` contains the currently verified bibliography.
- `PROOF_TRANSCRIPTION_LEDGER.md` maps each section to its immutable source proof.
- `REVIEW_FLAGS.md` records the remaining mathematical, computational, bibliographic and publication checks.

## Frozen mathematical sources

- Integrated proof: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`
- Independent AI-assisted certification: `09a88cc4fe1e2cf1f3a87475d6484f681910b23e`
- Q30 adversarial report: `a0f922ad09af99575bae581864b673aa4d41f00d`

## Build instructions

The manuscript source snapshot at commit `9c0e243b8970142a060bca8317ef36817837ec2d` was compiled in a clean GitHub Actions runner using TeX Live 2025 and `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` (run [41281119965](https://github.com/Icarus-K-Laplace/EG617-r12-proof/actions/runs/41281119965); 37-page PDF, 522,827 bytes). The resulting artifact's title page and updated related-work pages 1–3 were visually inspected. Later documentation-only edits do not alter the TeX source snapshot. The final `pdflatex` pass has no unresolved-reference/citation or overfull/underfull-box warnings; initial passes emitted expected warnings before BibTeX and reruns. The same run passed the integrated root verifier, clean temporary-copy reruns of the low-edge, 286-equality, q20 equality and COVER verifiers, and the standalone export verifier; it uploaded manuscript/replay and source-supplement artifacts. Pages 16–23 have been spot-checked in the final PDF; full editorial inspection remains open. This build and replay evidence does not replace mathematical review or make the draft submission-ready. The COVER theorem is stated for all residual energies `E<=408`, with `Q>=30` throughout that range and `Q>=31` at `E=408`. The h=4 equality orbit `{01,01,023,23}` is explicitly closed in `sections/06-equality.tex`, with a separate proof note at `supplement/root/frozen/eq286/H4_ORBIT_RESOLUTION.md`. A local standard BibTeX build is:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

A successful build establishes only that the source compiles. It does not certify the mathematics or make the draft submission-ready.

## Important authoring rules

1. Do not add a theorem or quantitative claim unless it is supported by the pinned proof files.
2. Keep every exact hypothesis and quantifier visible.
3. Distinguish analytic arguments from finite computation.
4. State explicitly that the final verifier does not rerun the full COVER shell search.
5. Do not claim Lean formalization, external human peer review or journal acceptance.
6. Verify every reference against its primary source.
7. The lead author and all coauthors must approve the final manuscript and assume responsibility for its correctness and disclosures.

AI systems assisted with mathematical exploration, proof transcription and manuscript preparation; AI systems are not authors.
