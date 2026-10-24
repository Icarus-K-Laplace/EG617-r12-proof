# Cross-branch synchronization — fixed r=12

Date: 2026-10-25  
Reader branch: workstream/r12-witness-packing-chat-20261025

## Repository scan

The linked account search returned one EG617-specific repository: Icarus-K-Laplace/EG617-r12-proof. No second EG617-named repository was found. The active fixed-r=12 research lines are separate branches of this repository, so this sync freezes their exact head SHAs rather than guessing from summaries.

## Frozen sibling heads read

| Line | Head SHA | Latest headline read | Relevance to this line |
|---|---|---|---|
| Emergency r12 sprint | 87a58429070cffbd90991045e0375102fcc4ec0d | Corrected exact-129 witness packing; high-multiplicity witness-star lemma; E408 blocker-occurrence budget | Correct six B-labelled witnesses versus seven total Q-sets; found a gap in the star lemma's claimed equality dichotomy |
| Ultimate closure | 78c30e86b0f432464ca5375695da97a27b230878 | Exact-129 pairwise blocker compatibility; row-transversal theorem; Q33 high-k packing | Supplies at least one high-k no-S witness per exact-129 Q33 color, two for beta=0/1; preserves OPEN status |
| Zero-excess witness | f3c9ef6b3a4bfadad4f70a16bb0e7c6434bb0777 | Robust zero-excess independent-four theorem; scalar overlap route audited as insufficient | Combining its degree theorem with the corrected six B-labelled components gives at least two zero-excess component witnesses per exact-129 color |
| Master closure | e46da35aedce7bbaaf11756b50192bd157956239 | E335 q=30, e(H)=214, excess K=8 equality reduction | Backend reduction remains conditional and does not close the T61 E407/E408 terminal |
| Earlier emergency-chat line | 5258c5fe17af3bf17eb7a2bfb08315c9be9116cd | Hub-capacity cross-cut | Source of the previously registered universal three-shell-row support and template-specific hub floors |
| General-r adversarial audit | 7ea44fc180fcaef20283f788a2234e2a14aa78e2 | E407 Q32 and E408 Q32/Q33 still open; root bridge contracts must be explicit | Consistent with fixed-r=12 status; no new unconditional terminal exclusion |
| Astra A_ext* | ad6e4ebe152e3918b9c5fe67f461ba402b1445d8 | Minimal-rank extraction; A_ext* still open | General-r, not imported as a fixed-r=12 theorem |
| Astra D_low | c71b29d3c5b661cdcf00404e545933893c44598b | D_low proved for r>=221 under its contextual contract; 67..220 open | General-r, irrelevant to the r=12 terminal closure |

## Reconciled facts

1. **Seven total Q-sets versus six B-labelled Q-sets.** For each exact-129 color, at least seven K5 components avoid S. At most one can contain pivot p. If p is in a K5 component, it contributes p+Q with Q subset H, and at least six other components are B+Q. Thus the total independent-four packing count is at least seven, while the guaranteed labelled B count is six.
2. **Zero-excess component witnesses.** In the 284-edge core, total core excess is four, so at most four core vertices have positive excess. The six B-labelled Q-sets are disjoint within a color; at least two avoid every positive-excess vertex. This gives at least 14 zero-excess B-labelled witnesses in E407 and 16 in E408 Q33.
3. **Q33 high-k packing.** Under beta+X+G_B=3, at least five B rows have k_b>=2; after excluding at most four labels outside the no-S K5 components, every exact-129 color has at least one high-k witness, and beta=0 or 1 gives at least two.
4. **Outer-block blocker budget.** The ultimate-closure branch proves M_C>=15+P_C. This is a different B/block notation from the inner T61 shell split. No equality between these two systems is assumed.
5. **Scalar overlap route.** The zero-excess branch proves a pairwise crossing lemma and exact edge-load identity but explicitly records that the scalar degree cap is insufficient. This line therefore targets the boundary kernels and labelled shell incidence, not another unlabelled scalar sum.

## Independent proof audit: witness-star dichotomy

The emergency branch's R12_WITNESS_OVERLAP_STAR_LEMMA.md proves the basic star facts, but its further claim that an m=10 star forces either e(H[U])=135 or e(H[U])>=144 is not justified by the stated second-Turán step.

If e(H[U])<=143, then L=overline(H[U]) has at least 292 edges. Brouwer's bound forces L to be tripartite, and the ten disjoint triangles P_i force three parts of size ten. It does not force L to be complete tripartite. The valid conclusion is three K10 cliques in H[U] plus g cross-part edges, 0<=g<=8. A local model with one cross edge between vertices from different P_i has e(H[U])=136 and preserves all ten independent triples. This refutes the local inference to g=0, not the full 47-core theorem; the global degree/excess contract may still rule out these cases and requires a separate proof.

This line does not use the unsupported dichotomy.

## Current line's commits

- 8caf22a302756c3de1563eae5585543f8e25f909 — corrected witness-packing theorem, strengthened zero-excess count, boundary proof audit.
- 4234596d4f7a3a62b58037d8b3c5a6d5ac125011 — standard-library arithmetic verifier.

All substantive files are under r12_master/workstreams/witness-packing-chat-20261025/. The headline remains OPEN / NOT_CERTIFIED.


## Live refresh — 2026-10-25, second pass

The branch heads were checked again immediately before this update:

- emergency: 87a58429070cffbd90991045e0375102fcc4ec0d
- ultimate-closure: 78c30e86b0f432464ca5375695da97a27b230878
- zero-excess-witness: f3c9ef6b3a4bfadad4f70a16bb0e7c6434bb0777
- master-closure: e46da35aedce7bbaaf11756b50192bd157956239
- this workstream: ecf58c25171c51ef8750a76dee4bfc1b7615b477

### Newly imported valid structure

1. **Seven-neighbour transversal floor:** for the linear family of 49 witnesses on 29 support vertices, and 56 witnesses on 31 support vertices, no transversal of size at most six exists. Therefore every outside core vertex has at least seven neighbours into the witness support.
2. **Correct E407 boundary window:** \(\delta+\epsilon_U\le16\) and \(\epsilon_U+2\delta\ge2\). The sibling claim \(\delta\le15\) is only valid conditional on L being non-four-partite.
3. **E408 Q33 boundary window:** \(\delta+\epsilon_U\le17\); the seven-neighbour floor is automatically satisfied by the exact edge identity.
4. **Pair-indexed zero-excess hub-cover certificates:** for any two regular B-rows with row sizes at most three, a common zero-excess independent four-set exists. It must be hub-complete whenever the two rows' missed-hub sets cover S. The reported 39/17/9 counts are labelled row-pair certificates, not distinct Q-sets.
5. **High-support exact-129 dichotomy:** if h=#\{b:k_b>=2\} is at least six, every exact-129 color has a no-S K5 component labelled by a high-k row. If h=5, a low-only repeated-disjoint-witness branch remains. This is especially relevant to E407 template E and E408 Q33 with beta=2 or3.

### New audit corrections

- The ultimate-closure boundary theorem's step “if L were complete four-partite ... hence L is non-four-partite” is invalid: a four-partite graph can omit cross-part edges. The valid case split is non-four-partite (where Brouwer applies) versus a near-complete four-partite design-like branch. This line records the corrected E407 delta window \([0,16]\), not \([0,15]\).
- The zero-excess pairwise-hub-cover file claims C/D/E have at least eight K5 components avoiding S, hence seven B-labelled components. The basic component count only proves at least seven avoiding S, hence six B-labelled (one could contain p). No template-specific proof of the stronger eight-component count was found in the cited file; this line uses only the safe six-label count until such a proof is supplied.
- The earlier emergency star lemma has the same complete-partite/non-complete-partite gap. Its m=10 equality dichotomy remains unaudited and is not used here.

The full EG617(r=12) result remains OPEN / NOT_CERTIFIED.


## Live refresh — 2026-10-25, third pass

Branch heads checked after the universal S0 theorem was committed:

- emergency sprint: 70d050655f0d03c38f3fef40c4a9f936e9ed1463
- ultimate closure: 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40
- zero-excess witness: c1604037ab9045543dcb0bad805a37459b907906
- master closure: e46da35aedce7bbaaf11756b50192bd157956239
- this witness-packing line: 27eb86f5c5fe5b1f1cc0574095ac90b4b5976b71
- general-r architecture: a922c4d7646eb8d0087bde8547562c8aace02ee2
- general-r asymptotic: fa6a5f2b8b5d2a0fe821d50a4421884a69dc5366

### New fixed-r=12 developments

1. **This line: universal E408 Q33 \(S_0\ge11\).** R12_E408_Q33_UNIVERSAL_S0_11.md excludes \(S_0=10\) at the 31-point/56-witness minimum-support boundary without assuming L is four-partite. It derives a unique 7-transversal, four degree-seven W-neighbours sharing that K7, two T-type size-eight neighbourhoods, and a (4,3,3) multiplicity partition of ten R-only neighbourhoods. The resulting K12 contradicts \(\omega(H)\le11\). This is a conditional boundary theorem, not a full terminal closure.
2. **Emergency sprint: four-partite E408 Q33 \(S_0\ne11\).** R12_E408_Q33_FOUR_PARTITE_S0_11_EXCLUSION.md uses exact U-degree profiles, the 8/9-point transversal classification, full-part neighbourhood capacities, and a triangle obstruction. Its argument is internally consistent under the stated four-partite contract; the accompanying verifier checks integer profiles only. Combined with the \(S_0=10\) exclusion, the four-partite branch has \(S_0\ge12\). The non-four-partite branch remains open.
3. **Zero-excess line: E407 four-partite TD(4,7) overclaim withdrawn.** The 49 witness blocks on parts (7,7,7,8) do not force an unused eighth point. For each seven-by-eight pair type, the seven unused pairs have degree one on the seven-point side but can have nonuniform degrees on the eight-point side. Therefore the distinguished-point reduction, \(\delta\ge12\), \(\epsilon_U=16-\delta\), and the forced \(H[W]=K_5\cup K_5\cup K_4\cup K_4\) conclusion are withdrawn. The valid E407 ledger remains \(\delta\ge2\), \(\delta+\epsilon_U\le16\), and \(\epsilon_U+2\delta\ge2\).
4. **Shell-incidence correction in this line.** SHELL_INCIDENCE_UNION_LEMMA.md was corrected to account for up to four core vertices with zero shell support. Its safe E407 full-row support-union floors are 7 (template A) and 6 (template C), not the earlier unsupported 11/10.
5. **General-r branches:** the architecture and asymptotic heads have not advanced since a922c4d / fa6a5f2 in this refresh. They remain separate conditional routes and are not imported as fixed-r=12 proofs.

### Combined boundary status after reconciliation

- E408 Q33, minimum support \(v=31\): universally \(S_0\ge11\); if L is four-partite, \(S_0\ge12\). The non-four-partite \(S_0=11\) case remains OPEN, as do larger support sizes.
- E407 Q32, minimum support \(v=29\): \(\delta\ge2\), \(\delta+\epsilon_U\le16\), \(\epsilon_U+2\delta\ge2\); the four-partite and non-four-partite completions remain OPEN. Do not use the withdrawn TD(4,7) distinguished-point argument.
- E408 Q32 remains a separate 285-edge / excess-six core and is not covered by any of the 284-edge Q33 results.
- The original \(K_{145}\to T61\) reduction bridge and the complete EG617(r=12) theorem remain OPEN / NOT_CERTIFIED.


## Live refresh — 2026-10-25, fourth pass

Current sibling heads reread:
- emergency sprint: f4c3b06891d29238d4f9cca2588f442004b6dc97
- E407 Q32 terminal / Cell-B closure line: 3f42fcce5761ca2372140618adda56f95fcbe253
- zero-excess witness: 07d19abfd6c1c749c7360526e4a04a3eb865fb2e
- ultimate closure: 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40
- this witness-packing line before this sync: 6292f77598df9cf841f04b012b81f44753567cc3
- general-r architecture/asymptotic: a922c4d7646eb8d0087bde8547562c8aace02ee2 / fa6a5f2b8b5d2a0fe821d50a4421884a69dc5366

### Newly reconciled results

1. **Universal E408 Q33 minimum-support improvement:** this line now proves \(S_0=\epsilon_U+2\delta\ge12\), not merely \(\ge11\), for the 31-point/56-witness boundary. The proof is independent of L being four-partite. The non-four-partite S0=11 case is therefore closed too.
2. **E407 Q32 transversal/excess theorem:** the latest emergency line proves \(\epsilon_U+2\delta\ge9\), hence \(\delta\ge3\), for the 29-point/49-witness boundary. The proof uses disjointness of distinct 7-transversals, an omitted-point count excluding three such transversals, a charge to core excess, and the exact cross-edge budget. This supersedes the earlier \(\delta\ge2\) lower bound but does not close E407.
3. **E407 Cell-B terminal:** the E407 Q32 terminal branch's E407_CELL_B_FULL_CLOSURE.md proves the \(|W|=23\) Cell-B subdivision normal form empty relative to the stated Brouwer/Kang–Pikhurko extremal inputs and the Cell-B color-certificate lemma. Combined with the prior E408 degree-20 exclusion, the sharp \(|W|=23\) Cell-B normal form is empty for both E407 and E408. This is a separate front-end terminal, not the same as the Q32/Q33 47-core completion.
4. **E407 four-partite audit remains corrected:** the earlier TD(4,7)-plus-distinguished-unused-point inference is withdrawn. Do not use the resulting \(\delta\ge12\) or \(K_5\cup K_5\cup K_4\cup K_4\) claims.
5. **E408 Q33 remaining work:** the minimum-support ledger is now \(S_0\ge12\), \(\delta+\epsilon_U\le17\). This still leaves larger values of \(S_0\), larger support sets, and the global seven-block completion. E408 Q32 remains separate at 285 core edges/excess six.

No full E407/E408 terminal, T61-to-K145 bridge, or EG617(r=12) proof is closed.
