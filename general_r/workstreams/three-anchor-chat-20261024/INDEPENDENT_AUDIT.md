# Independent audit — Exact Three-Anchor Excess Theorem

## Verdict

**THEOREM STATUS: INDEPENDENTLY_VERIFIED (analytic proof audit).**

The theorem
\[
r\ge12,\quad |V(H)|=3r-1,\quad \alpha(H)\le3,\quad
\omega(H)\le r-1,\quad \delta(H)\ge r
\]
with three pairwise nonadjacent degree-r anchors implies
\[
K_r(H)=2e(H)-r(3r-1)\ge8
\]
passes the line-by-line mathematical audit recorded in this workstream. No false lemma or surviving local equality case was found. The anchor partition, rectangle charge, additivity, empty-part self-consistency, all four geometry closures, and all \(r=12,13\) boundary cases have been re-derived.

The label means that the proof was re-derived and checked separately from the prior “PROVED_ANALYTIC” assertion in this audit. It does **not** mean an external human referee has certified the argument. A second human review remains advisable before journal submission.

## Scope actually read

The full contents of the following seven files were fetched from branch workstream/general-r-three-anchor-20261024 and reviewed:

| File | Blob SHA-1 at audit start |
|---|---|
| CANONICAL_STATE.md | 7664613e03dfd1b3bc56693ee1295060f60e9ca3 |
| UNIFIED_SHORT_PROOF.md | 50a9683aa3279bc95ab708ef77cb425570a05090 |
| THEOREM.md | 7f68075e7ea3d2b21535ffc984bb977fffbca2b0 |
| PROOF_ATTEMPTS.md | 601c7abdb78dc35c5b8b3163839e4e387247f940 |
| EQUALITY_CASES.md | 7ef60c42478c8a7e3e0615e31ecaea52bcb7b632 |
| COUNTEREXAMPLE_SEARCH.md | ba22d2f96077c0d43c739cae8e20797525433eb7 |
| R12_UNIFIED_CLOSURE.md | a3cb9bb139a9e6c65a988547587e5cdace340715 |

## Findings by priority

### 1. Anchor partition — VERIFIED

The identities \(c+t=4\), \(\sum d_i=c-2\), and \(q_i=d_j+d_k\) follow exactly from anchor incidence and the anchor degree equations. The four geometries are exhaustive and mutually exclusive. No hidden \(r=12\) assumption enters this reduction.

### 2. Rectangle charge and additivity — VERIFIED

For a pair connector \(z\), the nonneighbour sets in its two incident exclusive blocks form a complete bipartite graph. Every vertex-side term in
\[
R_{pq}(a,b)=a(b-p)_++b(a-q)_+
\]
is justified by the exact external-degree formula. Charging both endpoints of a forced edge is correct because \(K\) is a sum of vertex excesses.

The phrase “charges add” in the earlier short proof was too compressed for publication use. The precise condition is now stated and proved in LEMMA_VERIFICATION.md: rectangles sharing a block add when their opposite blocks are disjoint, via
\[
(u+v-p)_+\ge(u-p)_++(v-p)_+.
\]
Nonadjacent same-missing-anchor connectors have disjoint supports. Adjacent same-group connectors are not incorrectly charged additively; the proof uses \(k_1+k_2+\max(R_1,R_2)\) and then resolves equality.

All eight threshold inequalities and all four zero-charge characterizations were checked algebraically and cross-checked over \(1\le a,b\le100\).

### 3. Empty-Part Self-Consistency Lemma — VERIFIED

The \(c=2\) empty-part argument is valid. The exact derivation is in LEMMA_VERIFICATION.md and PUBLICATION_VERSION.md. In particular:
- \(E_1=\varnothing\) forces \(A_1=X_1\setminus N(p)\ne\varnothing\) by the clique cap;
- every vertex of \(A_1\) is positive-excess;
- the connector degree gives \(n_2+n_3=m+k_p-\varepsilon-1\);
- the remaining-part lower bound is \(s\ge r-1-m-K+\varepsilon+k_q+S\ge5\);
- the independent-4 condition makes \(B_2-B_3\) complete;
- maximum cross-degree two yields at least \(s\) cross-neighbors for every \(x\in A_1\);
- hence \(S\ge m(S+3-m)>S\), since \(S\ge m\ge1\).

No repair to the mathematics was needed.

### 4. \(c=2\) transversal-cover and size branch — VERIFIED, presentation repaired

The old short proof did not spell out the degree count yielding \(r\le K+5\le11\) when two \(E_i\) parts have size at most two. The count is valid:
\[
n_1+n_2\ge2r-8-|P|\ge2r-8-(K-k_p-k_q),
\]
while \(n_1+n_2\le r+k_p-3-\varepsilon\). Combining gives \(r\le K+5-k_q-\varepsilon\le11\). The degree-two transversal-cover lemma's omitted details have also been filled in. The alternative \((1/2,3,3)\) patterns have total size at most eight, contradicting \(\sum|E_i|\ge2r-9\ge15\).

### 5. \(c=3\) geometry — VERIFIED

The two-nonfocused branch has additive charge at least \(2r-16\ge8\). Two focused connectors either form a forbidden \(r\)-clique or have a common-nonneighbour clique larger than \(r-1\). The mixed branch uses the correct reduced capacities \(R_{22}\). The \(r=13\) layer is uniquely \((k,\gamma,a,b,n_2)=(6,0,2,2,0)\) and contradicts the triple connector's degree. The \(r=12\) arithmetic table has 19 relaxed signatures; every one is removed by a saturated rectangle vertex, except the one-neighbor \((6,0,2,2,1)\) signature, which is separately eliminated by the exact focused-connector degree. These details are expanded in PUBLICATION_VERSION.md.

### 6. \(c=4,(0,0,2)\) geometry — VERIFIED

At most two connectors focus on the short block. The \(f=0,1\) branches are eliminated by the stated additive charges. At \(f=2\), cross-group or nonadjacent same-group pairs cost at least eight. The adjacent same-group branch gives \(K\ge r-6+\max(k_1,k_2)\ge7\) for \(r\ge13\). At \(r=12\), the only local equality orientations are \((1,8)\) and \((8,1)\); overlap equality forces identical orientation, singleton, and support. The first creates an independent 4-set by saturation; the second creates an oversized common-nonneighbour clique whose exact rectangle vertex would need nine cross-neighbors despite one slot already being used.

### 7. \(c=4,(0,1,1)\) geometry — VERIFIED

The two incident-owner focus slots cannot each have two owners. The \(s=0,1\) cases close by additive local costs. For \(s=2\), the four owner patterns are exhaustive; three are over budget, and the remaining \(V/W\) ownership pattern reduces to the same \(R_{22}\) overlap inequality. The \(r=12\) equality orientations are independently eliminated by saturated-vertex independent 4-sets.

### 8. Parity and integer boundaries — VERIFIED

Every excess is nonnegative; \(K\) is even; excluding \(K\le6\) proves \(K\ge8\). The inequalities for \(r\ge13\) and the only \(r=12\) equality signatures have been checked. No \(r=13\) or \(r\ge14\) integer boundary is left.

## Computational status and limitations

The local arithmetic verifier passed all checks recorded in ARITHMETIC_AUDIT_RESULTS.md. CONNECTOR_SKELETON_AUDIT.py also enumerated every labelled c=3/c=4 connector adjacency graph, allowed focus-owner assignment, and connector-excess allocation for r=12,13,14,15 under the local rectangle relaxation; the outputs are in CONNECTOR_SKELETON_AUDIT_RESULTS.md. Its only low-budget c=4 survivors are the already-analyzed r=12 two-focus overlap signatures, and its r=13 c=3 survivors are variants of the single (6,0,2,2,0) signature. These are relaxed skeleton checks, not graph enumeration.

**No full graph-level SAT/ILP counterexample search was run.** No Z3, OR-Tools, or PySAT backend was installed. The proof is not being certified by computation, and no graph-level exhaustive-search claim is made. This limitation does not leave a mathematical proof gap because the theorem's proof is analytic; it does mean the requested independent graph-constraint search remains unperformed.

## Which file is publication-canonical?

- PUBLICATION_VERSION.md is the detailed, independently checked proof version.
- LEMMA_VERIFICATION.md gives the charge-additivity proof, complete empty-part derivation, and the degree-two cover proof.
- PROOF_DEPENDENCY_MAP.md records the dependencies and status of every substantive lemma.
- ARITHMETIC_AUDIT.py and ARITHMETIC_AUDIT_RESULTS.md provide the reproducible local arithmetic cross-check.
- CONNECTOR_SKELETON_AUDIT.py and CONNECTOR_SKELETON_AUDIT_RESULTS.md enumerate connector adjacency/focus skeleton relaxations; they are not a whole-graph search.

UNIFIED_SHORT_PROOF.md remains a concise summary; by itself it omits some derivation details that are now supplied in the publication version and helper-lemma file.

## Final certification statement

**Analytic theorem: INDEPENDENTLY_VERIFIED.**  
**Full graph-level counterexample search: VERIFIED_WITH_LIMITATIONS (not run).**  
**External human referee certification: not yet obtained.**

No OPEN_GAP or DISPROVED mathematical lemma remains in the stated theorem proof.
