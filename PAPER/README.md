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

The source was successfully compiled in a clean GitHub Actions runner using TeX Live 2025 and `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` (33-page PDF; successful snapshot `1f4862d0fe4ba0d95324da3c3173863014088634`). The final `.log` has no unresolved references/citations and no overfull/underfull box warnings; selected pages 1 and 24–31 were visually inspected. The same CI run passed the integrated root verifier and independently reran the low-edge, 286-equality, and COVER verifiers. The workflow also emits a source-supplement ZIP artifact. A local standard BibTeX build is:

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
