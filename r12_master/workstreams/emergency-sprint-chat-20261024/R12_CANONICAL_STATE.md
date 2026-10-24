# Emergency r=12 sprint — canonical state

Updated: 2026-10-25  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Dedicated branch: workstream/r12-emergency-sprint-20261024  
Dedicated path: r12_master/workstreams/emergency-sprint-chat-20261024/

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED.** Hard target date: 2026-10-31. No complete contradiction has been established.

## Frozen root contract

The root repository states the current dichotomy as
\[
K_{145}\text{ counterexample}\longrightarrow
\text{legal }R(4,49)\text{ residual or T61 residual}.
\]
The contextual \(R(4,49)\) branch has a short contradiction only under the exact original-coloring/F5 residual contract and the cited extremal input. The T61 branch remains the live terminal obstruction. The root theorem must not be promoted until the reduction contract, all retained dependencies, and the T61 terminal exclusion are jointly valid.

## Active mathematical frontier

1. **E407 Q32:** five retained \(\rho=0\) templates with a common regular \(K_{11}\), under the stated V12 lower-order-seed contract; same 284-edge core compatibility remains open.
2. **E408 Q32:** global seven-block near-Latin constraints are necessary, but exhaustive shell coverage is not certified. Its core has \(e(H)=285\), excess 6.
3. **E408 Q33:** the core has \(e(H)=284\), excess 4; the global seven-block/color-factor system and Q33/d3 exact budget remain necessary conditions, not a contradiction.
4. **E335 backend:** the current reported equality contract is \(q=30,e(H)=214,K=8\). It is not used as an unconditional shortcut in this front-end witness line.
5. **Shell/core witness capacity:** the retained witness lemma and cross-cut theorem are proved under their explicit T61 contracts, but do not alone exclude E407/E408.

## New result in this sprint line

R12_EXACT129_WITNESS_PACKING_STRENGTHENING.md proves, under a legal d3 shell-support split with \(M[B]=\varnothing\), that each exact-129 color has at least six no-\(S\), B-labelled \(K_5\) witness sets \(\{b\}\cup Q\). The initial seven-per-color count omitted the possibility that one no-\(S\) component contains pivot p; this has been corrected in R12_EXACT129_WITNESS_PACKING_STRENGTHENING.md. Consequently:
- E407 has at least 42 labelled witness 4-sets across its at least seven exact-129 colors;
- E408 Q33/d3 has at least 48 across its at least eight exact-129 colors;
- E407 templates A/C have at least one hub-complete witness per exact-129 color, hence at least seven hub-complete witness occurrences.

These are necessary-structure results only. They do not certify a graph-level contradiction.

## Isolation and governance

Only files under r12_master/workstreams/emergency-sprint-chat-20261024/ may be modified by this sprint line. The sibling ultimate-closure-chat-20261024 workstream is read-only for this line. No conditional E335, E407, E408, or contextual \(R(4,49)\) contract may be silently promoted to an unconditional theorem.

## Next attack

Build an exact labelled witness-overlap/capacity theorem for the 284-edge core, starting with the E407 A/C forced hub-complete occurrences and then applying the same framework to E408 Q33/d3. In parallel, audit every use of the T61 reduction against the original \(K_{145}\) hypothesis; do not substitute the open abstract E333–E340 backend for that bridge.

## Round 2 — global blocker occurrence budget and proof-audit correction

R12_E408_BLOCKER_OCCURRENCE_BUDGET.md (commit dc0c62892b3885941694f92dc9d41edbc2979761) proves, for each exact-129 color C in the outer seven-block E408 equality system,
\[
M_C\ge15+P_C,
\]
where M_C counts size-five blocker occurrences across the seven outer K12 blocks and P_C is the color-C duplicate budget among block-block edges. Summed over the m=8,9,10 exact-129 colors, this gives \(\sum M_C\ge77m-427\), i.e. 189, 266, or 343 according to m. This is a valid necessary-condition refinement; it does not close E408.

Audit correction: an attempted stronger E408 contradiction incorrectly promoted \(\omega(C[R])\le5\) on the 61-point T61 residual to a global \(\omega(C)\le5\), although outer block vertices are outside that residual. The resulting claim \(e_C(B_i,R)\ge72\) and the derived 885-edge contradiction were withdrawn. E408 Q32/Q33 remain OPEN.

The witness-packing theorem was also corrected: a no-S isolated K5 component can contain pivot p, so at most six B-labelled no-S components per exact-129 color are guaranteed without an extra lemma excluding p from such a component. The E407 A/C capacity corollary consequently gives at least one, not two, hub-complete witnesses per exact-129 color. No terminal is closed.

## New witness-overlap result (2026-10-25)

R12_WITNESS_OVERLAP_STAR_LEMMA.md records a proved structural reduction for repeated witnesses. If \(m\) witness sets share one core vertex, their other triples are disjoint and span at least \(3\binom m2\) core edges. In the extreme \(m=10\) case, either \(e(H[U])\ge144\), or \(H[U]=3K_{10}\); in the latter case the common vertex must have positive core excess. Neither branch is yet excluded.

Next attack: couple this overlap-star dichotomy to the 284-edge core's exact shell-incidence budget and the five E407 Q32 templates. The theorem remains OPEN / NOT_CERTIFIED.

## Round 3 — witness-union capacity refinement (commit cd6bf8c631bb09bb6099f5f328949553ea9c56bc)

R12_WITNESS_UNION_CAPACITY_REFINEMENT.md proves the core-capacity inequality
\[
6N\le e(\overline{H[U]})
\le \binom v2-p_4(47-v)-12v+284-E_U,
\]
for a pairwise-linear family of independent 4-sets in a legal 47-vertex, 284-edge core. The proof uses the minimum-edge Turán bound on the complement W of the witness union, and retains the nonnegative core excess \(E_U\) rather than dropping it prematurely.

**Sharpened terminal union-size contracts:**
- E407 templates A/B: if there are seven exact-129 colors, \(v\ge29\); if there are at least eight, \(v\ge31\).
- E407 templates C/D/E: with seven exact-129 colors, \(v\ge32\); with at least eight, \(v\ge33\).
- E408 Q33/d3: if \(\beta=e(M[S])=0\), \(v\ge31\); if \(\beta\ge1\), \(v\ge33\).

These refine the previous general witness-union bounds and isolate the boundary kernels, but do not eliminate them. The remaining union-size boundaries are E407 A/B with seven exact-129 colors and \(v=29\), E407 C/D/E with seven exact-129 colors and \(v=32\), and E408 Q33/d3 with \(\beta=0\) and \(v=31\).

**E408 Q32 is explicitly excluded from this application** until its own reduction certifies the required shell-support split; its core has 285 edges and excess six. No E407/E408 terminal is closed, and the root theorem remains OPEN / NOT_CERTIFIED.
