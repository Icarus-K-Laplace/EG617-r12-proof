# 286-edge support-orbit audit ledger

**Status:** PROVED_CONDITIONAL. The ten listed support orbits are exhaustive under the independent-four-set/private-clique reduction. Each is eliminated by the cited argument, conditional on the common-neighborhood bound, scalar blocker inequalities, triple-on-three-cliques lemma, and shared-incidence inequalities stated in the main proof. This ledger is an audit index, not a substitute for those analytic arguments.

## Exhaustiveness

For an independent degree-12 four-set \(I=\{s_0,s_1,s_2,s_3\}\), let \(Z\) be the vertices adjacent to at least two seeds. The 48 seed incidences cover all 43 vertices outside \(I\), since otherwise a vertex anticomplete to \(I\) would extend it to an independent five-set. The incidence surplus is therefore five:
\[
\sum_{z\in Z}(|N(z)\cap I|-1)=5.
\]
Each support has size at least two, and each seed has at least two neighbors in \(Z\), because its private clique has size at most eleven. Thus \(h=|Z|\in\{3,4,5\}\), \(\sum_i d_i=h+5\), and \(|K_i|=13-d_i\). The finite orbit verifier independently checks the complete multiset classification under permutations of the four seed labels:
- \(h=3\): 2 orbits;
- \(h=4\): 3 orbits;
- \(h=5\): 5 orbits.

## Orbit-by-orbit disposition

| # | \(h\) | Clique sizes | Support multiset | Disposition |
|---:|---:|---|---|---|
| 1 | 3 | \(11,11,11,11\) | \(\{0123,01,23\}\) | Two disjoint \(K_{11}\)-pair blockers, each costing at least 6; total at least 12. |
| 2 | 3 | \(11,11,11,11\) | \(\{01,023,123\}\) | Concentrated small-side charge at least 6 for pair \(01\), plus at least 3 on the disjoint triple \(123\) and its three cliques. |
| 3 | 4 | \(10,11,11,11\) | \(\{01,01,023,23\}\) | Pair \(23\) costs 6. Either an \(01\) point misses both supported cliques and its disjoint mixed blocker costs 4, or both \(01\) points complete \(K_0=K_{10}\), and their nonadjacent pair costs at least 7. |
| 4 | 4 | \(10,11,11,11\) | \(\{01,012,03,23\}\) | Pair \(23\) costs 6. Point \(01\) must complete \(K_0\); point \(03\) either also completes it (7-unit common-neighbor charge) or is a noncompleter with an additional \(K_0\)-completer (5-unit mixed-diamond charge), additive on \(K_3\). |
| 5 | 4 | \(10,11,11,11\) | \(\{01,02,03,123\}\) | Shared-center star inequality; standalone derivation in H4_STAR_ORBIT_RESOLUTION.md. |
| 6 | 5 | \(9,11,11,11\) | \(\{01,01,02,03,23\}\) | Pair \(23\) costs 6; the small-budget double-pair lemma forces both \(01\) points to complete \(K_9\); shared-center mixed-pair accounting then forces a \(K_{13}\). See H5_9_11_11_11_RESOLUTION.md. |
| 7 | 5 | \(10,10,11,11\) | \(P=\{01,02,02,13,13\}\) | Each doubled mixed pair has a noncompleter. Their \(f_{10,11}\) blockers are disjoint and cost \(4+4=8\); equality forces missing sizes \((2,3)\) and all excess onto the selected points, after which each companion must complete the \(K_{10}\), forcing degree 13 at a zero-excess missing vertex. Full charge accounting: `H5_P_AND_B_RESOLUTION.md`. |
| 8 | 5 | \(10,10,11,11\) | \(D=\{01,02,03,12,13\}\) | Two per-\(K_{10}\)-center charges, each at least 5, add across the \(K_{11}\) leaves. See H5_D_10_10_11_11_RESOLUTION.md. |
| 9 | 5 | \(10,10,11,11\) | \(B=\{01,01,02,13,23\}\) | Pair \(23\) costs 6; the small-budget \(10/10\) double-pair lemma forces opposite \(K_{10}\)-completion; point \(02\) then gives either a 5-unit mixed-diamond charge additive on \(K_2\), or a 7-unit common-neighbor charge. Full charge accounting: `H5_P_AND_B_RESOLUTION.md`. |
| 10 | 5 | \(10,10,11,11\) | \(C=\{01,01,01,23,23\}\) | The two points on the same \(K_{11}\)-pair are excluded by the dedicated same-pair theorem in the main proof. |

## Finite verifier scope

The frozen INDEPENDENT_VERIFIER.py independently checks:
- the complete support-orbit counts \(2,3,5\);
- the minima and equality cases of the four pair-blocker scalar functions;
- the simultaneous star and mixed-center scalar minima;
- all 10,400 subsets in the three-incidence diamond inequality;
- 139,921 ordered intersection parameter tuples for the same-\(K_{11}\)-pair lower bound, with minimum 14;
- the arithmetic of the regular four-set lower bounds and the parent edge caps.

The verifier does **not** formalize the analytic implications from the graph hypotheses to every degree charge. Those are the prose proof obligations above and remain subject to external human review.


## Final AI-assisted adversarial recheck (2026-11-01)

The ten orbit dispositions were rechecked against the main-text proof, including
zero-missing-set and complete-to-clique branches, the two-point same-pair
intersection cases, and pointwise additivity on shared $K_{10}$ centers and
$K_{11}$ leaves. A separate local enumeration reproduced the raw multiset
counts $9,40,48$ and the $S_4$ orbit counts $2,3,5$. The seven scalar blocker
functions and their equality cases were also independently recomputed over
their finite parameter ranges. No new counterexample or double-counting
defect was found in this pass.

The $47$-vertex private-neighbor decomposition used by the E286 proof is now
isolated in sections/06-equality.tex, Lemma
lem:private-neighbor-decomposition-e286; its hypotheses do not include
$e(H)\leq285$. This audit remains AI-assisted informal proof review, not
proof-assistant formalization or external human peer review. The analytic
implications remain open to specialist challenge.
