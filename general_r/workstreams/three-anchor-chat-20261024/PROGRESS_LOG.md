# Progress log

## 2026-10-24 — initialization

- Created isolated branch `workstream/general-r-three-anchor-20261024` from `workstream/general-r-architecture-20261024`.
- Reverified the anchor-incidence partition symbolically: `c+t=4`, `d_1+d_2+d_3=c-2`, four block patterns only.
- Derived the exact connector-miss identity `q_i=d_j+d_k`, fixing the connector type multiset for every pattern.
- Complement formulation initially gave an analytic large-r theorem via Andrasfai–Erdos–Sos.

## 2026-10-24 — parity collapse

- Observed that `K_r=2e-r(3r-1)` is always even.
- Therefore the contradiction branch is `K<=6`, not `K<=7`.
- This removed the entire apparent `K=7` equality layer.

## 2026-10-24 — rectangle/focus machinery

- Proved the exact anchor partition and pair-connector rectangle lemma.
- Converted rectangle obligations into excess charges using baseline external capacities `2+d_i`.
- Proved charge additivity for rectangles with disjoint opposite blocks.
- Proved the common-nonneighbour clique lemma.
- Proved same-missing-anchor disjointness for nonadjacent pair connectors.

## 2026-10-24 — first parameterized closure

- Closed `c=2` for every `r>=12` using a degree-two tripartite transversal-cover argument.
- Closed `c=3` for every `r>=13`.
- Closed both `c=4` geometries first for large `r`, then analytically compressed the boundary to every `r>=13`.
- This produced a Level-3 theorem when composed with the parent project's existing `r=12` closure.

## 2026-10-24 — Level-4 r=12 absorption

- Reopened only the proof-engineering residue at `r=12`; no historical fixed-r case table was imported.
- `c=3`, `(10,10,9)`: mixed focus reduces to effective `R22`; every low-budget layer has a saturated rectangle vertex, forcing an impossible complete/almost-complete cover of the opposite 10-block.
- `c=4`, `(10,10,8)`: classified by `f=0,1,2` focused connectors. `f=0,1` die by additive charge; `f=2` reduces to the two exact `(1,8)/(8,1)` equality skeletons, both eliminated analytically.
- `c=4`, `(10,9,9)`: classified by `s=0,1,2` occupied focus slots. All but one ownership pattern die by additive charge; the final two-U overlap reduces to the same `(1,8)/(8,1)` skeletons and is eliminated by independent-4 forcing.
- Added `R12_UNIFIED_CLOSURE.md`.

## 2026-10-24 — unified short-proof audit

- Re-audited the full theorem instead of stopping at Level 4.
- Replaced the old `r=13..16` c=4 boundary stack by a uniform focus-count proof:
  - `(0,0,2)` is handled by `f=0,1,2` focused connectors for all `r>=12`;
  - `(0,1,1)` is handled by `s=0,1,2` occupied focus slots for all `r>=12`;
  - for `r>=13`, the only overlap branch dies from the single inequality `K>=r-6+max(k1,k2)>=7`;
  - `r=12` leaves only `(1,8)/(8,1)` equality skeletons.
- Strengthened the `c=2` proof. If an exact-nonneighbour part `E_i` were empty, let `m` be the number of positive-excess nonneighbours in that block and `S` their total excess. Self-consistency of the two remaining exact-nonneighbour blocks gives

  `S >= m(S+3-m)`,

  while `S>=m`, so the right side exceeds `S` by at least `2m`. Contradiction.
- With all three `E_i` nonempty, the degree-two tripartite cover lemma and the global lower bound `sum|E_i|>=2r-9` close `c=2` cleanly.
- Added `UNIFIED_SHORT_PROOF.md` as the canonical 2–6-page-style analytic proof.

## Current milestone

> **Exact Three-Anchor Excess Theorem is `PROVED_ANALYTIC` for every `r>=12`.**

The preferred proof is now `UNIFIED_SHORT_PROOF.md`. It does not rely on computation-certified steps, the historical fixed-`r=12` case closure, or separate `r=13..16` case tables.

## Next target

No theorem gap remains in this workstream. The highest-value action is external/independent proof review before the theorem is promoted upstream as a hard dependency for the general-r backend.


## 2026-10-24 — independent proof certification

- Fetched and read the complete contents of CANONICAL_STATE.md, UNIFIED_SHORT_PROOF.md, THEOREM.md, PROOF_ATTEMPTS.md, EQUALITY_CASES.md, COUNTEREXAMPLE_SEARCH.md, and R12_UNIFIED_CLOSURE.md before deciding the audit verdict.
- Independently re-derived the anchor incidence identities, all four geometries, the rectangle excess formula, all threshold inequalities, and the additivity conditions.
- Confirmed the Empty-Part Self-Consistency Lemma. Expanded the derivation from E1 empty through S >= m(S+3-m) > S.
- Filled a presentation gap in the c=2 degree-two cover branch: when two E-parts have size at most two, the explicit connector count gives r <= K+5 <= 11.
- Added PUBLICATION_VERSION.md with the full proof, LEMMA_VERIFICATION.md with the charge/additivity and empty-part derivations, PROOF_DEPENDENCY_MAP.md, INDEPENDENT_AUDIT.md, and ARITHMETIC_AUDIT.py / ARITHMETIC_AUDIT_RESULTS.md.
- Executed the committed arithmetic verifier's source in Python. All eight threshold inequalities passed over 10,000 positive-integer pairs; all zero-charge characterizations passed over 1 <= a,b <= 100; c=3 boundary relaxations and c=4 equality relaxations matched the proof's listed signatures.
- The analytic proof audit found no OPEN_GAP or DISPROVED lemma. The theorem status is now INDEPENDENTLY_VERIFIED in the analytic-proof-audit sense.
- Explicit limitation: no full graph-level SAT/ILP search was run; no Z3, OR-Tools, or PySAT backend was installed. This is not a computational proof. External human referee review remains advisable.
- Actual GitHub commit SHAs for the audit sequence:
  - ARITHMETIC_AUDIT.py: 585beaf726f6d9758d02696a5293af1fe9dede9b
  - LEMMA_VERIFICATION.md: 19c90e4e334c32cc63999a1227e90646e7e8a387
  - PROOF_DEPENDENCY_MAP.md: 22d1ce381400698d831b67ddcbd0c51da1e9efb3
  - PUBLICATION_VERSION.md: b9faa08e691f9c054a66a674b7d998fc21d80db9; expanded in 88f906099acabee72769b6a0d3b2508f8f66bbf8 and 065f43cac86d1f6aa5228e00d5d3d76913fd5df2
  - ARITHMETIC_AUDIT_RESULTS.md: e41ef17fe5750f1cc06f2ed1c58470aacb4f834b
  - INDEPENDENT_AUDIT.md: b1bd7a918afa0000cab5cca9531e2acea9ab6e2c
  - CANONICAL_STATE.md: 437aeecaafd0db7d55bf47cb68b4131229355979
  - THEOREM.md: ab9f6dbbd5c0dc8527ef94117bec7c91c143a6b6
  - COUNTEREXAMPLE_SEARCH.md: b0890dae2b597fe100235dec67b9fdd4badc5bcb


## 2026-10-24 — connector-skeleton enumeration and final audit polish

- Added CONNECTOR_SKELETON_AUDIT.py and ran the committed source in Python.
- Enumerated all 8 labelled c=3 connector graphs and all 64 labelled c=4 connector graphs, all connector excess allocations with total at most six, and all allowed focus-owner assignments for r=12,13,14,15 under local rectangle relaxations.
- Results: c=3 has 44 relaxed low-budget skeletons at r=12, 4 at r=13, and none at r=14,15; c=4 (0,0,2) has only two r=12 two-focus overlap relaxations; c=4 (0,1,1) has only two r=12 two-slot overlap relaxations; no c=4 relaxed low-budget skeleton remains at r=13,14,15. The survivors match the already-analysed equality signatures, not actual graph counterexamples.
- Added CONNECTOR_SKELETON_AUDIT_RESULTS.md and linked the artifact from canonical state, the dependency map, and the falsification ledger.
- Corrected mathematical notation escaping in LEMMA_VERIFICATION.md and range notation in ARITHMETIC_AUDIT_RESULTS.md; re-fetched the final stored contents after updates.
- Latest follow-up commits:
  - CONNECTOR_SKELETON_AUDIT.py: bb302be3c055fe7fa9eb521e77ee6451988bf71a
  - CONNECTOR_SKELETON_AUDIT_RESULTS.md: 525a555eebf2662ea2212c2a6df3c1169fd1fa2a
  - LEMMA_VERIFICATION.md notation repair: a57b4f65065438f78c30c85f0ca7e4bf25bc1abc
  - ARITHMETIC_AUDIT_RESULTS.md notation repair: 962a03f965d395868ea0d472736c1410cf90510a
  - INDEPENDENT_AUDIT.md skeleton-search update: 825e8aa6611ee2595141b57a20c7ebd50adb535f
  - CANONICAL_STATE.md artifact index update: bccfcc73fda70a67694500cd39f5d4b2cbcdbd7f
  - COUNTEREXAMPLE_SEARCH.md skeleton-search update: d636a3efe2b9324df46083da90ff0a439bd9f34b
  - PROOF_DEPENDENCY_MAP.md skeleton-audit row: 2584d8b12f808d5c59132e44a8635b0fecfb1878
- Final limitation remains unchanged: no full graph-level SAT/ILP search and no external human referee certification.


## 2026-10-24 — final publication-proof line audit

- Re-read the final stored PUBLICATION_VERSION.md after the arithmetic and skeleton checks.
- Added explicit budget-exhaustion statements in both r=12 overlap branches: once k1+k2 plus the rectangle charge reaches six, all other vertices, including focused connectors, must be exact. This makes the degree counts used in the equality contradictions explicit.
- Expanded the c=4 (0,0,2) orientation (8,1) degree count and the c=4 (0,1,1) orientation degree counts so the saturated-vertex contradictions can be checked without inference.
- Made the R_pq zero-set characterization explicit in the publication proof.
- Final follow-up commits:
  - PUBLICATION_VERSION.md: 1490c51be95b614d514130f0950c16bcca978d80; 032d66697fd59a408256f2de248a4cff76b750bc; ae2308009c1d223642aa16d9b65c4cad55bfe00b
- Final proof status remains INDEPENDENTLY_VERIFIED in the analytic-audit sense. Full graph-level SAT/ILP search and external human referee certification remain explicitly unclaimed.


## 2026-10-24 — final equality-branch explicitness

- Added an explicit exactness conclusion in both r=12 overlap branches: the two connector excesses plus the six-unit rectangle charge exhaust K, so every other vertex (including focused connectors) is exact.
- Expanded the second c=4 overlap derivation to show the degree inequality, the max-charge bound, the positive-excess exclusion, and the remaining (1,8)/(8,1) signatures without relying on an implicit “same argument”.
- Final publication proof commits: 032d66697fd59a408256f2de248a4cff76b750bc; 7b3628dd01cfb5788b4c49674bd65cf29c9c9ef4; 94f5fbd6fa2e2c0ff0fb79c28dd84c34e5d4e79c; 9725336511b03575d241703565eced6fb8bc4aa0.


## 2026-10-24 — final wording consistency check

- Aligned LEMMA_VERIFICATION.md wording with the committed arithmetic script: the script enumerates and asserts the 19 c=3, r=12 signatures; the complete table is displayed in PUBLICATION_VERSION.md, while the script's stdout reports the count and exceptional rows rather than printing every row.
- Commit: b5a8845c3e0d373d0afbea6bb051671bc1d3c81c


## 2026-10-24 — Round 2: exact \(K=8\) rigidity

- Read the current branch versions of CANONICAL_STATE.md, PUBLICATION_VERSION.md, INDEPENDENT_AUDIT.md, LEMMA_VERIFICATION.md, PROOF_DEPENDENCY_MAP.md, EQUALITY_CASES.md, COUNTEREXAMPLE_SEARCH.md, THEOREM.md, and PROGRESS_LOG.md before starting the equality-layer work.
- Kept the frozen \(K\ge8\) theorem unchanged; did not repeat the \(K\le6\) contradiction proof.
- Re-derived the exact pair-connector degree identity
  \[
  a+b=r-2-d_i-d_j+\gamma_z+n_k-x_z
  \]
  and wrote the backend-safe per-vertex union-load interface \(x_v\ge(|F_v|-(2+d_i))_+\), with each forced external neighbour included only once.
- Proved the new analytic boundary theorem \(K=8\Rightarrow r\le13\). By parity and the frozen theorem, this gives the genuine strengthening \(K\ge10\) for every \(r\ge14\).
- Closed the \(c=2,r=13\) equality layer by exact equality in the transversal-cover count and the second connector's impossible demand for at least sixteen exclusive neighbours.
- Exhausted the \(c=3,r=14\) local \(R_{22}\) profile list (23 profiles) and eliminated it using common-nonneighbour cliques and saturated rectangle vertices. Also eliminated the sole \(r=15\) profile and all \(r\ge16\) profiles.
- Eliminated \(c=4,(0,0,2)\) two-focus equality at \(r=13,14\), and \(c=4,(0,1,1)\) two-slot equality at \(r=14\), using exact degree equations plus opposite-block external-incidence deficits.
- Remaining \(K=8\) necessary strata are now restricted to \(r=12,13\): \(c=2,r=12\); \(c=3,r=12,13\) mixed-focus; \(c=4,(0,0,2),r=12\) with \(f=0,1,2\) as specified in EQUALITY_K8_CLASSIFICATION.md; and \(c=4,(0,1,1),r=12,13,s=2\) with \(V/W\) owning the two deficit-one focus slots. These are necessary conditions only; no graph realization is claimed.
- Added EQUALITY_K8_CLASSIFICATION.md, NEAR_MINIMAL_EXCESS_RIGIDITY.md, BACKEND_INTERFACE.md, K8_LOCAL_PROFILE_AUDIT.py, and K8_LOCAL_PROFILE_AUDIT_RESULTS.md; updated canonical state, theorem ledger, equality cases, audit, dependency map, and counterexample-search ledger.
- Executed an independent local integer-profile check. It verified the complete 23-row \(c=3,r=14\) list, the sole \(r=15\) profile, no \(r=16\) profile, and the one-sided \(c=4\) overlap profiles at \(r=13,14\). This is not a whole-graph search.
- Full \(K=8\) classification remains OPEN for \(r=12,13\); \(K\ge10\) is **not** claimed for those parameters. No whole-graph SAT/ILP search was run.
- Key Round-2 commits:
  - K8_LOCAL_PROFILE_AUDIT.py: c5aa3f8e6c72b6d5fb56e2abffa8e5b8859fbb6b; output fix: 1336cbfd9368bce2e15a69393892b7b59aa20935
  - K8_LOCAL_PROFILE_AUDIT_RESULTS.md: 38c2119bcc397ef93306689ee26a22c99a684f7a; formatting fix: 8ee83eabb83e22499b14663fc127ed4072404b05
  - THEOREM.md: a99b2e7f2df4ed7b1c93683bdde304c9e9207046
  - CANONICAL_STATE.md: 9621b306ea119c5b2d7a6153fa9e42b77246daa3; artifact index: 3ca7eddc9a48311db8646821a481aedfc396e20f
  - EQUALITY_CASES.md: 31ccb83099dddc94304823c1e64d4c2e90211343
  - COUNTEREXAMPLE_SEARCH.md: 3d978805e37976fa7402dd2ff1a480a7bd2c0d5d
  - INDEPENDENT_AUDIT.md: d976ce72c32696774c575dbfdd63e961ba12f302
  - PROOF_DEPENDENCY_MAP.md: 26a321fd296155ee8a97a75e2e720c470866cd03
  - EQUALITY_K8_CLASSIFICATION.md: d1b6d132df67268d9097b111634165edc65b8b67; status corrections: aa7334366517f4d703608faf0c62537000dd4ddd, b2c9cbf67ce7bce4b4d35aa7e889edaed503f5a8
- Pre-log branch head was b2c9cbf67ce7bce4b4d35aa7e889edaed503f5a8. The next commit records this progress entry.


## 2026-10-24 — post-audit consistency fixes

- Re-examined the \(r=13,c=4,(0,0,2),f=2\) overlap proof. Corrected the equality description: the two large rectangle sides need not be nested; the singleton's **union load** determines its excess. The external-incidence contradiction remains valid using the union size \(q+2\le10\) and at most two opposite-block connector neighbours.
- Corrected the final equality-layer wording to state precisely that \(K\ge10\) is proved for \(r\ge14\), while the \(r=12,13\) equality layer remains OPEN.
- Re-ran the local integer-profile assertions in Python: \(c=3,r=14\) has exactly 23 profiles, \(r=15\) has the single \((8,0,0,2,2,0,8)\) profile, and \(r=16\) has none; the \(c=4\) \(r=13,14\) overlap assertions also passed. Results output ordering was aligned with the committed script.
- Follow-up commits:
  - union-load correction in EQUALITY_K8_CLASSIFICATION.md: b07c97ff5fe69bf22464c8a26155fa8ca805694e
  - K=10 scope correction in EQUALITY_K8_CLASSIFICATION.md: 34510e37da00f92b2336e5a9f07c38e716d1fa40
  - exact profile output ordering: 67fb8defa7ac67fd43c9194486bae2d0a471c366
- Pre-log branch head: 67fb8defa7ac67fd43c9194486bae2d0a471c366.
