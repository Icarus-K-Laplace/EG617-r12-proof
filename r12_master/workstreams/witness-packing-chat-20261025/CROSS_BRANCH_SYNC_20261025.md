# Cross-branch synchronization — fixed r=12

Date: 2026-10-25  
Reader branch: workstream/r12-witness-packing-chat-20261025

## Repository scan

The linked account search returned one EG617-specific repository: Icarus-K-Laplace/EG617-r12-proof. No second EG617-named repository was found. The active fixed-r=12 research lines are separate branches of this repository, so this sync freezes their exact head SHAs rather than guessing from summaries.

## Frozen sibling heads read

| Line | Head SHA | Latest headline read | Relevance to this line |
|---|---|---|---|
| Emergency r12 sprint | 87a58429070cffbd90991045e0375102fcc4ec0d | Corrected exact-129 witness packing; high-multiplicity witness-star lemma; E408 blocker-occurrence budget | Correct six B-labelled witnesses versus seven total Q-sets; found a gap in the star lemma's claimed equality dichotomy |
| Ultimate closure | 28f47fb7c8f273e6a70bf19f4ee961e8023f5981 | Exact-129 pairwise blocker compatibility; row-transversal theorem; Q33 high-k packing | Supplies at least one high-k no-S witness per exact-129 Q33 color, two for beta=0/1; preserves OPEN status |
| Zero-excess witness | 95255a82f126fadbc8834c799df1374e5fc86fca | Robust zero-excess independent-four theorem; scalar overlap route audited as insufficient | Combining its degree theorem with the corrected six B-labelled components gives at least two zero-excess component witnesses per exact-129 color |
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
