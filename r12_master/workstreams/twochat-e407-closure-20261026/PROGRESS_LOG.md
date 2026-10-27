# Progress log — E407 Q32 two-chat closure workstream

## 2026-10-26 — Round 1: rebuild actual frontier and unify the labelled high-k witness floor

### Repository isolation
Created branch workstream/r12-twochat-e407-closure-20261026 from main (3f42fcce5761ca2372140618adda56f95fcbe253). All writes in this workstream are restricted to r12_master/workstreams/twochat-e407-closure-20261026/. Source branches are read-only.

### Source audit
Read the actual latest heads:
- E407 terminal 79c1086efca893fad8933210a92a432457232410;
- unified witness capacity faa8183c150dd78b000d0957fa8a63cebd52e146;
- emergency sprint f4c3b06891d29238d4f9cca2588f442004b6dc97;
- ultimate closure 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40;
- main 3f42fcce5761ca2372140618adda56f95fcbe253.

Re-read E407 canonical/progress state, FIVE_TEMPLATE_COMPATIBILITY.md, all registered DELTA13/14/15/16 notes, the Round 31 two-cross-edge terminal proof, root canonical state/proof DAG, and the sibling exact-129 packing / row-transversal / witness-capacity records.

### New theorem (conditional necessary structure)
Every exact-129 color has at least six B-labelled no-S K5 components \(\{b\}\cup Q\). The V12 row-type floors force at least 6/8/6/7/5 high-k B rows in templates A/B/C/D/E. Since at most four B labels are outside the six-or-more B-labelled no-S components, each exact-129 color has at least 2/4/2/3/1 high-k no-S witnesses, respectively. A/C have at least two k=3 no-S witnesses per color, each hitting all three S rows; any additional high-k witnesses are charged only two hub hits each. In B/D/E, each selected high-k witness hits at least two S rows. The aggregate S-row hit floors per color are 6/8/6/6/2 for A/B/C/D/E. Every selected Q hits at least three shell rows total; cross-color Q intersections are at most one, and same-B-label Q sets across colors are disjoint.

Across at least seven exact-129 colors, this gives per-template floors of 14/28/14/21/7 labelled high-k witness sets and at least 42/84/42/63/21 total shell-row-hit incidences. The proof is written in FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md. It is a strict incidence reduction, not a contradiction and not a template closure.

### Exact low-delta frontier
The integer ledger was rebuilt from \(\delta+\epsilon_U\le16\), \(\epsilon_U+2\delta\ge9\), \(0\le\epsilon_U\le4\), and \(\delta\ge3\). The full feasible table is in LOW_DELTA_TERMINAL_TABLE.md. The main unresolved low-delta rows are \(\delta=13,\epsilon_U=0\), \(\delta=13,\epsilon_U=2\) with the one-cross-edge (4,4,5,5) W profile under four-partite \(L_U\), all non-four-partite \(\delta=13\) cases, and every \(\delta\le12\) case.

### Proof dependency audit
The exact-129 factorization, the five-template screen, Brouwer/Kang–Pikhurko classifications, and the Didin-dependent saturated branch are recorded separately from pure graph facts. The root main proof DAG and sibling conditional R(4,49) treatment are not silently reconciled; E407 and the original bridge remain OPEN / NOT_CERTIFIED.

### Next attack
Join the 49 support-block labels to the high-k no-S component labels and shell row sets \(D_a\), without assuming these witness families coincide. Seek a contradiction common to multiple templates or a minimal surviving incidence contract. Independently audit any candidate inequality against the exact \(D_a\) row supports before using it.


## 2026-10-26 — Round 2: verifier replay and arithmetic correction

The low-delta table was independently recomputed from the exact inequalities. There are **56**, not 57, feasible \((\delta,\epsilon_U)\) pairs. The repository verifier was corrected to assert 56; each pair satisfies
\[
e(H[U])+e(H[W])+e_H(U,W)=284.
\]
The independent Python replay checked all 56 pairs, all three edge formulas, and the lower bound \(e(H[W])\ge32\).

The five-template incidence verifier's arithmetic assertions were independently replayed as well. It confirms per-color high-k no-S witness floors \(2,4,2,3,1\), total witness floors \(14,28,14,21,7\), aggregate S-row hit floors \(42,56,42,42,14\), and total shell-row hit floors \(42,84,42,63,21\). For A/C the hub-hit calculation is corrected to charge at least two hits to every high-k witness and one additional hit to each of the at least two guaranteed k=3 witnesses; this avoids overcharging any additional k=2 rows.

Transparency: the arithmetic assertions were independently executed in the Python reasoning environment; the GitHub-hosted scripts themselves were not launched from a repository shell in this session. They remain standard-library runnable audit scripts, not graph-realization certificates.

No terminal was closed by this arithmetic replay. The global labelled-incidence join, the surviving low-delta contracts, and the original K145-to-T61 bridge remain OPEN / NOT_CERTIFIED.


## 2026-10-26 — Round 3: support omission identity and A/C component capacity

The 49 support blocks form seven disjoint 4-set blocks in each of seven color classes. Each class therefore uses 28 of the 29 points and omits exactly one point. If r_u counts how often u is omitted, and x_u counts extra support-complement edges incident to u beyond the 294 block pairs, then sum(r_u)=7, sum(x_u)=2*delta, and the exact pointwise identity is:

    d_H(u,W) = 5 + epsilon_u - 3*r_u + x_u.

The identity follows by counting the 3 block-pairs at u in every class containing u, then adding the extra complement edges. At least 22 points have r_u=0 and therefore at least five neighbours in W. The independent arithmetic replay checked all 15 omission partitions and all 56 feasible (delta, epsilon_U) profiles.

For templates A/C, let h be the number of full B rows, h>=6. A non-hub-complete B-labelled no-S component witness must hit at least h distinct B rows. The six component witnesses in a color are disjoint, while total B-to-core incidence is c_S=3h+n_1<=2h+10<4h. Therefore at most three of the six witnesses are non-hub-complete: each exact-129 color has at least three hub-complete component witnesses, at least 21 across seven colors. This is a component-witness result and does not identify those witnesses with the 49 support blocks.

LABEL_JOIN_SYSTEM.md now lists the support-block variables, shell-row variables, component witnesses, exact constraints, and the unresolved mapping between the two witness families.

The arithmetic replay passed in the Python reasoning environment. The GitHub-hosted scripts themselves were not launched from a repository shell. No E407 terminal is closed; all five global templates, surviving low-delta cases, and the original K145-to-T61 bridge remain OPEN / NOT_CERTIFIED.


## Round 4 — 2026-10-26

Added DELTA13_EPS2_K4K4K5K5_ONE_CROSS_EDGE.md. Under the four-partite support contract, the remaining delta=13, epsilon_U=2 W-profile with four clique parts of sizes 4,4,5,5 and one cross-edge is excluded. The proof separates assigned and unassigned D vertices, derives an external-edge budget of at most two in the assigned case, and shows the required K4 loads exceed the available W-excess. The exceptional unassigned case is separately excluded.

The arithmetic replay passed in Python: the edge ledger is 99+33+152=284, and every listed K4-load case requires more than the two available W-excess units. The verifier is arithmetic-only; analytic transversal steps still need independent proof review.

The four-partite delta=13, epsilon_U=2 row is now closed under the registered W-profile classification. Four-partite epsilon_U=0, non-four-partite delta=13, all delta<=12 cases, all five global shell templates, and the original K145-to-T61 bridge remain OPEN / NOT_CERTIFIED.


## Round 5 correction

The Round 3 claim of three hub-complete component witnesses per color is withdrawn. Its proof used an anticompleteness condition for other B-rows that is not in the frozen contract. The retained A/C floor is at least two hub-complete witnesses per color from the k=3 label count. The verifier no longer asserts the stronger bound. See PROOF_DEPENDENCY_AUDIT.md.


## Round 6 — A/C component bound reinstated through row-transversal theorem

The Round 5 audit found the direct independent-six justification incomplete. Re-reading the registered row-transversal theorem resolves the gap under its explicit contract: for any missing shell edge s-b, every independent 4-set in H minus D_s meets D_b when t_s<=12, using the retained R(3,35) exclusion. Since all A/C hub rows satisfy t_s<=12, a non-hub-complete component witness must hit every full B row. The c_S budget then limits non-hub-complete witnesses to at most three; the witness's own label further limits them to 10-h. The valid conditional floor is max(3,h-4) hub-complete witnesses per color. The corrected proof and arithmetic verifier are in FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md and verify_template_incidence_system.py.


## Round 7 — 2026-10-27: W-side support-block transversal capacity

**Theorem added:** every \(w\in W\) hits all 49 support blocks, so \(d_U(w)\ge7\). With \(y_w=d_U(w)-7\),
\[
\sum_W y_w=\epsilon_U+2\delta-2\ge7.
\]
For every independent 4-set \(I\subset W\), \(\sum_{w\in I}y_w\ge1\), so the zero-slack vertices induce a graph with independence number at most three. For every nonedge \(ww'\) in H[W],
\[
|N_H(w,U)\cap N_H(w',U)|\le y_w+y_{w'}.
\]
These are exact incidence consequences of the 49-block contract and \(\alpha(H)\le4\).

**Slack-one branch:** if an independent W-quadruple has total y-slack one, its four U-neighborhoods partition U into sizes 7,7,7,8. Each support block meets each part once. The three 7-parts are pairwise anticomplete K7s. If \(\epsilon_U+2\delta<16\), the 8-part is a clique or has at most one missing edge. The proof is recorded in SUPPORT_BLOCK_W_TRANSVERSAL_CAPACITY.md.

**Frontier correction:** for the minimum-slack profiles (3,3) and (4,1), total y-slack is seven, implying at least eleven zero-slack W vertices. This does not imply exactly seven positive-slack vertices or that each positive slack equals one. The verifier and note preserve this distinction.

No E407 template, low-\(\delta\) terminal, or original K145-to-T61 bridge is closed by this result. Next attack: determine whether the low-slack W graph must contain a slack-one independent quadruple, or prove the complementary domination/capacity branch impossible; then feed the resulting W-neighborhood classes into the shell row systems and the four-unit core excess ledger.
