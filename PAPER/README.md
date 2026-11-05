# EG617(r=12) manuscript workspace

**Status: working draft; not submission-ready.**

- `main.tex` contains the title, abstract, main theorem, introduction draft, proof architecture and initial reproducibility/limitations sections.
- `references.bib` contains verified bibliographic records for the foundational and directly relevant papers currently cited.
- The detailed proof sections still need a line-by-line transcription and editorial pass against the pinned integrated proof and certification package.

## Build status

The LaTeX source has **not yet been compiled** in a clean TeX environment. Once a TeX Live installation with BibTeX is available, build from this directory with:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

A successful build will only establish document compilation; it will not certify the mathematical proof or make this draft submission-ready.

## Frozen mathematical sources

- Integrated proof: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`
- Independent certification: `09a88cc4fe1e2cf1f3a87475d6484f681910b23e`

## Important authoring rules

1. Do not add a theorem or quantitative claim unless it is supported by the pinned proof files.
2. Keep all exact hypotheses visible when stating graph lemmas.
3. Distinguish analytic proof from finite computation.
4. Do not claim Lean formalization, external human peer review or journal acceptance.
5. Verify every reference and every attribution before arXiv submission.
6. Final human author(s) must approve the complete manuscript and assume responsibility for it.

## Post-audit supplementary package (5 November 2026)

The manuscript now summarizes the E286 equality boundary, the pointwise
287-edge core floor, the exact pivot/repivot identities, and the h13 Q30
subcases. Supporting detail and finite arithmetic checkers are in
`supplement/root/`:

- `E286_COVER_INTERFACE_AUDIT_20261103.md`
- `H13_Q30_X3_BRANCH_RHO_IDENTITY_20261103.md`
- `PROOF_DAG_CORRECTED_PROPOSAL.md` and `.json`
- `RECHECK_E286_COVER_INTERFACE_20261103.py`
- `RECHECK_H13_Q30_X3_BRANCH.py`
- corresponding recorded JSON outputs and `DAG_DEPENDENCY_CORRECTION_NOTE_20261105.md`

The frozen 25-node proof DAG remains unchanged. The 28-node proposal has
resolved parent references, is acyclic, and every node is a dependency of
`K145_EMPTY), but semantic review and promotion remain pending. The full
root verifier has not been rerun from a fresh clean checkout by this update.
Neither the supplementary scripts nor the AI-assisted audit constitute a
Lean kernel proof or external human peer review.

The manuscript is produced with AI assistance under human author supervision; AI systems are not authors.
