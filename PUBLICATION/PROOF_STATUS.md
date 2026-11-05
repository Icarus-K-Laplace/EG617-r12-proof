# EG617 ($r=12$) — exact mathematical and publication status

## 1. Main theorem

**Status: PROVED** in the frozen integrated proof snapshot, as a conventional informal mathematical proof supported by finite computation and an independent AI-assisted audit.

Let $c:E(K_{145})\to\{1,\ldots,12\}$ be any edge-coloring. The theorem asserts
$$
\exists S\subseteq V(K_{145}),\quad |S|=13,\quad
\{c(e):e\in E(K_{145}[S])\}\ne\{1,\ldots,12\}.
$$

Equivalently, no coloring makes every 13-set contain all 12 colors.

Proof source: commit c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2, file r12_master/workstreams/astra-global-root-integration-chat-20261031/FINAL_GLOBAL_PROOF.md.

Independent audit: commit 09a88cc4fe1e2cf1f3a87475d6484f681910b23e, file r12_master/workstreams/r12-final-certification-chat-20261031/FINAL_CERTIFICATION_REPORT.md.

## 2. Independent certification scope

The independent AI-assisted audit records CERTIFICATION = PASS for the exact pinned proof snapshot. It reports:

- 58 analytic/computational obligations in the obligation matrix;
- Q27 and Q28 finite-state sets reproduced (2 and 8 canonical states);
- 81,920 subset identities checked;
- 1,752 recurrence nodes replayed;
- all 144 outer-stop comparisons checked;
- the unique $(d,j)=(11,6)$ T61 stop eliminated by the integrated terminal argument;
- provenance and dependency-DAG checks.

The report explicitly distinguishes analytic derivations from finite computation. It does not claim a proof-assistant certificate or external human peer review.

## 3. Important theorem-domain distinctions

- **Fixed $r=12$, original $K_{145}$ coloring theorem:** PROVED in the integrated proof.
- **47-vertex low-edge obstruction:** PROVED under its exact five graph hypotheses, as recorded in the frozen low-edge proof and theorem ledger.
- **286-edge equality classification:** PROVED under the exact 47-vertex contract, as recorded in the frozen equality proof and independent audit.
- **COVER Q30 terminal:** PROVED under the exact 61-vertex E408 parent contract. The independent Q30 report states its quantifiers explicitly; it is not a classification of arbitrary decorated shells.
- **Q32 and Q33:** distinct 285-edge and 284-edge contracts. Do not conflate their labels. The integrated proof's low-edge theorem is stronger and makes the exact Q32/Q33 theorems nonessential to the final dependency path.
- **Abstract uncolored high-energy $R(4,49)$ layers E333–E340:** OPEN / not claimed solved. The original-coloring proof avoids requiring this generic theorem by proving a stronger contextual obstruction in the original full-color setting.
- **General $r$:** OPEN / outside this fixed-parameter theorem.

## 4. Formalization and external review

| Item | Status |
|---|---|
| Informal analytic proof | PROVED in pinned integrated package |
| Finite replay / certificate checks | COMPUTATIONALLY VERIFIED as described in the audit; the new supplementary arithmetic scripts are scoped to their stated finite domains |
| Independent AI-assisted audit | PASS |
| Lean 4 / Mathlib formalization | NOT YET COMPLETED; no complete kernel-checked declaration of the original K145 theorem is claimed |
| External human combinatorics referee | NOT YET COMPLETED |
| Journal peer review / acceptance | NOT YET COMPLETED |
| Public arXiv identifier | NOT YET ASSIGNED |

## 5. Approved public wording

Recommended:

> We prove the fixed twelve-color case of the Erdős–Gyárfás balanced-coloring conjecture: there is no 12-edge-coloring of $K_{145}$ in which every 13-vertex subset contains all 12 colors.

Also state in the abstract or introduction that the proof is computation-assisted and not yet proof-assistant formalized.

Do not say that the full Erdős–Gyárfás conjecture has been solved.

## 6. Fixed source identifiers

- Integrated proof: c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2
- Independent certification: 09a88cc4fe1e2cf1f3a87475d6484f681910b23e
- Q30 independent report: a0f922ad09af99575bae581864b673aa4d41f00d
- 286-edge equality source: c3d07b2ca5912b1b0c1c6998303c19c3c2911340
- COVER source: 531e41c79e08dd2bb3892ca9ba8a491a56678565
- 47-point low-edge source: 783c72090205d4bd1a6eefce1dec09e15f78e319


## 7. Post-audit qualification (5 November 2026)

A targeted interface audit of the 47-vertex E286 equality boundary, the
pointwise 287-edge core floor, and the h13 COVER Q30 terminal found no
hybrid counterexample or load-bearing interface gap in the audited chain.
The exact identity is
[
E=e(F)=91+q_p+e(C_p),
]
and the 287-edge floor is applied to every regular pivot core before
taking the maximum charge. The detailed repivot sequence, the
$|X|=3$ rho identity, and the Family I/II same-parent arguments are
recorded in `PAPER/supplement/root/E286_COVER_INTERFACE_AUDIT_20261103.md`
and `H13_Q30_X3_BRANCH_RHO_IDENTITY_20261103.md`.

This targeted result does not remove the following package-level blockers:

- The frozen 25-node `PROOF_DAG.json` omits explicit dependency nodes
  `GATE47`, `D48`, and `SHELL_MATCHING_BOUNDS`. A 28-node corrected
  proposal is included in `PAPER/supplement/root/`; it has resolved parent
  references, is acyclic, and all nodes are dependencies of
  `K145_EMPTY`. It has not yet been accepted as a semantic dependency
  map or promoted into the frozen integration snapshot.
- The full integrated root verifier has not been rerun from a fresh,
  clean checkout by this publication-corrections branch. A saved verifier
  result or a component-level replay is not a clean-room acceptance.
- The proof remains an informal mathematical proof with finite
  computational support. No Lean/Mathlib kernel certification, external
  human combinatorics review, or journal acceptance is claimed.

The fixed-$r=12$ theorem status above refers to the informal proof in the
pinned integration package and its stated audit scope. It must not be
rephrased as formal proof-assistant certification or full clean-room
reproducibility.
