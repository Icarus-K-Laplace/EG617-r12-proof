# E407 Q32 — proof dependency audit

Date: 2026-10-26  
Status: **Audit in progress; no global proof certificate.**

## 1. Four contract layers

### A. Pure graph facts inside a frozen 47-core contract

Assumptions: \(|H|=47\), \(e(H)=284\), \(\alpha(H)\le4\), \(\delta(H)\ge12\), \(\sum_H(d_H-12)=4\), and inherited \(\omega(H)\le11\). The excess identity follows from the edge count:
\[
\sum_{v\in H}(d_H(v)-12)=2e(H)-12|H|=568-564=4.
\]
The clique-number bound is not implied by this calculation; it is inherited from the T61 parent with \(\omega(F)\le11\). The support ledger and Turán bound \(e(H[W])\ge32\) are pure graph consequences once the 29/18 split and \(\alpha(H[W])\le4\) are assumed.

### B. Labelled witness facts

The E407 boundary contract has 49 independent 4-sets on \(U\), seven per each of seven exact-129 colors, pairwise intersections at most one. Within one color class the seven sets are disjoint. Cross-color pairwise linearity follows from edge-color uniqueness: if two independent 4-sets shared two vertices, their common edge would belong to two distinct non-target colors.

The exact-129 component packing statement is a separate labelled fact: each exact-129 color has ten isolated \(K_5\) components plus an 11-vertex exceptional gadget with independence number two, under the registered extremal factorization. From it and \(|S|=3\), at least six no-S components per exact-129 color are B-labelled. The theorem in FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md combines these labels with the V12 row-count floors; it does not silently identify the no-S component quadruples with all 49 support blocks.

### C. External-theorem-dependent facts

- **Brouwer second-Turán bound:** used to force four-partiteness when the complement edge count exceeds \(t_4(n)-\lfloor n/4\rfloor+1\), and to classify the \(\delta=14,\epsilon_U=1\) W row. The graph must be \(K_5\)-free and the non-four-partite hypothesis must be the one to which the bound is applied.
- **Turán equality:** used for the exact \(\delta=14,\epsilon_U=2\) W profile and other equality edge counts; the equality characterization must be retained.
- **Kang–Pikhurko 2005 equality classification:** used for the \(\delta=15\) non-four-partite branch and the \(\delta=14\) augmentable-edge reduction. These are conditional on the theorem's stated \(K_5\)-free/non-four-partite/equality hypotheses.
- **Didin 2026 preprint:** the \(\delta=14\) non-four-partite \(K_5\)-saturated branch uses a component-count step from the alpha-critical reduction. The preprint proof has not been independently audited here. This branch must remain PROVED_CONDITIONAL, not unconditional PROVED.
- **R(3,35) and R(2,24) lower-order exclusions:** the row-transversal theorem uses these hereditary inputs to show every independent 4-set in \(H\setminus D_a\) hits \(D_b\) for a missing shell edge \(ab\). This is not a consequence of \(\alpha(H)\le4\) alone.

### D. Original \(K_{145}\) bridge and finite V12 screen

The main branch canonical state (main head 3f42fcce5761ca2372140618adda56f95fcbe253) and proof DAG still list E407/E408 as active T61 layers and the abstract E333–E340 backend interval as open. The FRONTEND_BRIDGE_THEOREM records a conditional/source-reported dichotomy from a hypothetical balanced \(K_{145}\) coloring to a legal \(R(4,49)\) residual or embedded T61, but explicitly leaves the end-to-end T61 bridge and conversion to seven genuine unanchored blocks open.

The V12 archive replay record reports checksum verification and independent execution of the finite kernel verifier: 8,677 weight assignments, 17,957 count states, 1,984 labelled necessary shells, 554 open states covered by five \(\rho=0\) templates. This certifies the supplied finite state coverage only. It does not independently prove every analytic screen rule, construct a completed 61-vertex parent graph, or prove all five templates impossible. The lower-order seeds and V12 elimination hypotheses retain their stated conditions.

There is a status mismatch between the root main-branch proof DAG (which retains E333–E340 as a second obligation) and an ultimate-closure workstream's conditional argument that the contextual \(R(4,49)\) branch is excluded under an exact original-coloring/F5 contract. This workstream adopts the conservative root status: neither alternative is promoted to an unconditional root proof.

## 2. Source files re-read

- E407 branch 79c1086efca893fad8933210a92a432457232410: canonical state, progress log, FIVE_TEMPLATE_COMPATIBILITY.md, all registered DELTA13/14/15/16 proof notes, and the Round 31 two-cross-edge terminal closure.
- Unified witness-capacity branch faa8183c150dd78b000d0957fa8a63cebd52e146: canonical state and progress log.
- Emergency sprint branch f4c3b06891d29238d4f9cca2588f442004b6dc97: canonical state and progress log, including the corrected exact-129 packing theorem.
- Ultimate-closure branch 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40: canonical state, proof DAG, row-transversal theorem, witness-capacity cross-cut theorem, shell-incidence audit, and V11/V12 replay record.
- Main branch 3f42fcce5761ca2372140618adda56f95fcbe253: CANONICAL_STATE.md, PROOF_DAG.md, and FRONTEND_BRIDGE_THEOREM.md.

## 3. Audit conclusion

The local \(\delta=16,15,14\) and several \(\delta=13\) W-profile closures are conditional core-level results. Round 4 additionally excludes the four-partite \(\delta=13,\epsilon_U=2\), \((4,4,5,5)\)+one-W-cross-edge profile under its explicit W-profile contract. These are not a complete E407 Q32 proof. The five shell templates remain unclosed because no proof yet joins the exact shell rows, 49 support blocks, exact-129 component labels, and the same 284-edge H into either an impossible incidence system or a verified graph realization. The original \(K_{145}\)-to-T61 bridge remains OPEN / NOT_CERTIFIED.
