# Canonical State — Exact Three-Anchor Excess workstream

Branch: `workstream/general-r-three-anchor-20261024`

## Contract
Assume `r>=12`, `|V(H)|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`, and three pairwise nonadjacent degree-`r` anchors `a1,a2,a3`. Define

`K_r(H)=sum_v(d_H(v)-r)=2e(H)-r(3r-1)`.

## Current verdict

**EXACT THREE-ANCHOR EXCESS THEOREM: `INDEPENDENTLY_VERIFIED` (analytic proof audit) for every `r>=12`.**

This is a **Level-4 completion**. The publication-canonical full proof is `PUBLICATION_VERSION.md`, supported by `LEMMA_VERIFICATION.md`, `PROOF_DEPENDENCY_MAP.md`, and the local arithmetic verifier `ARITHMETIC_AUDIT.py`. `UNIFIED_SHORT_PROOF.md` remains a concise summary and omits some derivation details now supplied in the publication version.

The theorem proof does not depend on the historical fixed-`r=12` closure, computation-certified graph enumeration, or separate `r=13..16` case tables. No full graph-level SAT/ILP search was run; no external human referee certification has yet been obtained.

## Core reductions

1. `K_r` is always even, so a counterexample to `K_r>=8` has `K_r<=6`.
2. Every non-anchor meets at least one anchor.
3. With exclusive blocks `Xi`, connector count `c`, triple-connector count `t`, and deficits `d_i=(r-2)-|Xi|`:
   - `c+t=4`;
   - `d_1+d_2+d_3=c-2`;
   - only `(0,0,0)`, `(0,0,1)`, `(0,0,2)`, `(0,1,1)` occur.
4. If `q_i` is the number of connectors missing `ai`, then `q_i=d_j+d_k`, fixing every connector type multiset.
5. Pair-connector nonneighbour sets form complete bipartite rectangles, converted into excess charges `R_pq` using exact baseline external capacities.
6. Two nonadjacent connectors have a common-nonneighbour clique.
7. Two nonadjacent pair connectors missing the same anchor have disjoint nonneighbour supports.
8. Focused neighbours consume baseline external capacity and strengthen rectangle charges: `R24 -> R23 -> R22` and `R33 -> R23 -> R22`.

## Unified closures

### c=2 / deficits `(0,0,0)`
Two triple connectors, block sizes `(r-2,r-2,r-2)`.

**Closed for every `r>=12`.** If an exact-nonneighbour part `E_i` were empty, self-consistency of the remaining two parts forces

`S >= m(S+3-m) > S`,

where `m>=1` is the number of positive-excess nonneighbours in the empty part and `S>=m` their total excess. Thus all three exact-nonneighbour parts are nonempty. The cross graph on them has maximum degree two and no independent transversal; the degree-two transversal-cover lemma plus `sum|E_i|>=2r-9` gives the contradiction.

### c=3 / deficits `(0,0,1)`
One triple connector, two pair connectors, block sizes `(r-2,r-2,r-3)`.

**Closed for every `r>=12`.** Both nonfocused costs at least `2r-16>=8`; both focused violate the clique cap. In the mixed branch, the nonfocused rectangle is effective `R22`. For `r>=14` its local charge is already at least seven; `r=13` has one `(6,2,2)` equality layer, killed by forcing the triple connector to complete the opposite long block; `r=12` has only saturated-rectangle low-budget layers, all killed by the same independent-4 forcing.

### c=4 / deficits `(0,0,2)`
Four pair connectors, block sizes `(r-2,r-2,r-4)`.

**Closed for every `r>=12` by one focus-count proof.** At most two connectors focus on the short block. For `f=0` and `f=1`, additive `R24/R23` charges exceed six. For `f=2`, the only possible nonfocused pair is adjacent and same-group. For `r>=13`, choosing the smaller connector excess gives

`K >= r-6+max(k1,k2) >=7`.

At `r=12`, equality reduces to `(1,8)/(8,1)` `R22` skeletons, each impossible.

### c=4 / deficits `(0,1,1)`
Four pair connectors, block sizes `(r-2,r-3,r-3)`.

**Closed for every `r>=12` by focus-slot count.** Each deficit-1 block has at most one focus owner. For zero or one occupied focus slot, additive charges exceed six. With both occupied, every owner pattern except `V`/`W` ownership is immediately too expensive; the remaining two-U overlap branch is the same `R22` overlap as above, giving `K>=7` for `r>=13` and only the impossible `(1,8)/(8,1)` skeletons at `r=12`.

## Main files

- `PUBLICATION_VERSION.md`: full publication-grade proof version checked in the independent audit.
- `INDEPENDENT_AUDIT.md`: certification findings, exact limitations, and audit scope.
- `LEMMA_VERIFICATION.md`: full rectangle-charge additivity and empty-part proofs.
- `PROOF_DEPENDENCY_MAP.md`: theorem dependency DAG and lemma ledger.
- `ARITHMETIC_AUDIT.py` / `ARITHMETIC_AUDIT_RESULTS.md`: reproducible local arithmetic checks.
- `CONNECTOR_SKELETON_AUDIT.py` / `CONNECTOR_SKELETON_AUDIT_RESULTS.md`: exhaustive labelled connector/focus skeleton relaxations for `r=12,13,14,15`; not a whole-graph search.
- `UNIFIED_SHORT_PROOF.md`: concise proof summary; some derivation details are intentionally deferred to the full proof.
- `THEOREM.md`: theorem ledger and consequences.
- `R12_UNIFIED_CLOSURE.md`: detailed `r=12` equality analysis retained as supporting record.
- `PROOF_ATTEMPTS.md`: historical derivation and earlier boundary proofs.
- `EQUALITY_CASES.md`: equality-layer ledger.
- `COUNTEREXAMPLE_SEARCH.md`: falsification record and search limitations.
- `PROGRESS_LOG.md`: chronological progress.


## Round 2 — Exact \(K=8\) equality and near-minimal rigidity

The original theorem status above is unchanged. New results are recorded separately:

- **PROVED_ANALYTIC:** if \(K_r(H)=8\), then \(r\le13\).
- **PROVED_ANALYTIC:** \(K_r(H)\ge10\) for all \(r\ge14\), using parity and the frozen \(K_r\ge8\) theorem.
- **OPEN_GAP:** full equality classification for \(r=12,13\). No actual \(K=8\) graph has been constructed, and these strata have not all been eliminated.
- Remaining necessary strata are listed in EQUALITY_K8_CLASSIFICATION.md.
- The exact union-load accounting interface is in BACKEND_INTERFACE.md.
- The local integer/rectangle profile audit is in K8_LOCAL_PROFILE_AUDIT.py and K8_LOCAL_PROFILE_AUDIT_RESULTS.md. These are not full-graph search results.

### Remaining \(K=8\) strata

- \(c=2,(0,0,0)\): \(r=12\).
- \(c=3,(0,0,1)\): \(r=12,13\), mixed-focus branch only.
- \(c=4,(0,0,2)\): \(r=12\), \(f=0\) with same-group adjacency, \(f=1\), or \(f=2\).
- \(c=4,(0,1,1)\): \(r=12,13\), \(s=2\), with \(V/W\) owning the two deficit-one focus slots.

No whole-graph SAT/ILP search was run. The original theorem remains independently verified analytically; the Round-2 equality classification remains open.


## Next action

Prioritize the \(r=13\) mixed-focus \(c=3\) layer and the \(r=13\), \(s=2\) overlap layer in the \(c=4,(0,1,1)\) geometry. Seek either a full structural contradiction or an explicit graph realization. Do not promote a local integer/connector skeleton to a graph without checking every independent-four, clique, and degree constraint.
