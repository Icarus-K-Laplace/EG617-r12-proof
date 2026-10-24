# E408 Q33 global-compatibility — canonical state

Updated: 2026-10-25  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-e408-q33-global-compat-20261025  
Exclusive workstream path: r12_master/workstreams/e408-q33-global-compat-chat-20261025/

## Headline

**E408 Q33 remains OPEN / NOT_CERTIFIED.** This workstream has not produced a complete contradiction. It has strengthened the four-partite minimum-support boundary and made the exact cross-layer finite contract explicit.

## Frozen Q33 contract

- T61 target residual F has 61 vertices, alpha(F)<=5, omega(F)<=11, and a legal degree-13 pivot p.
- Shell A=N_F(p), |A|=13; core H=V(F)\(A union {p}), |H|=47.
- e(H)=284, delta(H)>=12, alpha(H)<=4, omega(H)<=11, and sum_H(d_H-12)=4.
- E408 Q33 has q=33, a 284-edge core, and residual non-target excess 3. There are at least eight exact-129 non-target colors.
- At the minimum-support boundary, U has 31 vertices, W=H\U has 16, and the selected family Q has 56 independent four-sets, seven from each of eight exact-129 colors. Within a color they are disjoint; across colors any two distinct sets intersect in at most one vertex.
- L=overline(H[U]), e(L)=336+delta, and S0=epsilon_U+2delta, where epsilon_U=sum_{u in U}(d_H(u)-12).

## New result in this line

Under the additional four-partite contract for L, the D-part of size 7 and the three large parts A,B,C of size 8 force

\[
\boxed{S_0\ge22}.
\]

Equivalently, the four-partite branch must have delta>=9, because epsilon_U<=4. The proof uses:
1. the eight witness triples partitioning A union B union C for each d in D;
2. the exact D-to-W degree sum 42+epsilon_D;
3. the classification of 8-point transversals;
4. an independent-transversal lemma for the three large parts;
5. the omega(H)<=11 clique cap.

This is stronger than the inherited universal bound S0>=12 and does not assume S0=11/12 is the only open layer. It still leaves the four-partite branch with S0>=22 open.

## Seven-block global system

For every non-target color C:
\[
P_C+R_C+s_C=62,\quad \sum_C P_C=252,\quad
\sum_C R_C=427,\quad \sum_C s_C=3.
\]
For exact-129 colors, s_C=0, R_C>=7, P_C<=55, and the number M_C of exact size-five blocker occurrences obeys M_C>=15+P_C. Thus the sum of P_C over exact colors is at least69, and the total exact-blocker occurrence count over at least eight exact colors is at least189.

A cross-layer lemma is proved in SEVEN_BLOCK_INCIDENCE_LEDGER.md: for each exact-129 color and each outer K12 block, at least one row neighborhood contains one of the six selected B-labelled no-S K5 components. If r_i(C)<=2 and the color has at least two high-k selected components, at least one high-k component is an exact size-five blocker in that block. These are compatibility constraints, not a contradiction. A component-representative edge between two outer blocks is not automatically a duplicate counted in P_C.

## Remaining terminal contract

Two cases remain:

1. **Non-four-partite L:** a K5-free graph on 31 vertices with 56 edge-disjoint K4 witnesses, e(L)=336+delta in [340,353], delta+epsilon_U<=17, S0>=12, and the exact vertex-incidence identities in NON_FOUR_PARTITE_TERMINAL.md. The second-Turán bound e(L)<=354 does not exclude this interval.
2. **Four-partite L:** parts 8,8,8,7, the 56 K4s are transversals, the unused pair slots between each two large parts form a perfect matching, and S0>=22 (hence delta>=9). The seven-block labeled incidence ledger remains mandatory.

The remaining task is to prove a stability/packing contradiction in Case 1 or a genuine color-labeled global contradiction in Case 2. No scalar bound alone is being promoted to closure.

## Scope firewall

This result is conditional on the retained T61, exact-129 factor, 31-point/56-witness, and outer seven-block contracts. It does not close E408 Q32 (285-edge core), E407 Q32, or the original K145 theorem. The original reduction and lower-order seeds remain separate dependencies.


## Audit correction

The earlier ten-witness-star file in the emergency sprint claims \(e(H[U])=135\) or \(e(H[U])\ge144\). Its proof only establishes that the complement L is tripartite, not that it is complete tripartite; missing cross-part edges are not ruled out. This line does not use that dichotomy. See PROOF_DEPENDENCIES.md.

## Latest isolated commits

- Four-partite bound and cross-system analysis: f392c169e549c68cff59caa7f27d968b0ee36d49
- Low-slack blocker normal form and forced component matchings: 75a7a877ab4879cf8dcc2e11e76ecfe64c582e0d
- Non-four-partite terminal contract: b36c1fd87d642186df78147aa203812a57f7ad15
- Dependency audit and pairwise-blocker integration: f272b81656d6abcee4afee5ec26b9262a47f42b0
- Progress log: 8edc7609e15a998daf7ae6365a38fde5819aee50

No graph-level contradiction or independently replayed UNSAT certificate has been produced. The terminal remains OPEN / NOT_CERTIFIED.


## New low-slack global-compatibility result

The pairwise exact-129 blocker theorem has now been integrated into SEVEN_BLOCK_INCIDENCE_LEDGER.md. For an exact-129 color C and a block with \(r_i(C)\le3\), all ten isolated K5 components are represented in exactly one row neighborhood, exactly two rows contain no full component, and each component-containing row has size at most seven. For any two blocks i,j with \(r_i(C),r_j(C)\le3\), the ten corresponding component representatives are forced C-edges forming a matching.

This sharpens the labeled finite contract: every low-slack block induces a partition of the 56 selected witness labels into 12 row classes, each class a matching of pairwise-disjoint selected Q-sets and containing at most one Q from each selected color. The crude capacity \(12\cdot7=84\) still exceeds 56, so this is not yet a contradiction.

# E408 Q33 global-compatibility — canonical state

Updated: 2026-10-25  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-e408-q33-global-compat-20261025  
Exclusive workstream path: r12_master/workstreams/e408-q33-global-compat-chat-20261025/

## Headline

**E408 Q33 remains OPEN / NOT_CERTIFIED.** This workstream has not produced a complete contradiction. It has strengthened the four-partite minimum-support boundary and made the exact cross-layer finite contract explicit.

## Frozen Q33 contract

- T61 target residual F has 61 vertices, alpha(F)<=5, omega(F)<=11, and a legal degree-13 pivot p.
- Shell A=N_F(p), |A|=13; core H=V(F)\(A union {p}), |H|=47.
- e(H)=284, delta(H)>=12, alpha(H)<=4, omega(H)<=11, and sum_H(d_H-12)=4.
- E408 Q33 has q=33, a 284-edge core, and residual non-target excess 3. There are at least eight exact-129 non-target colors.
- At the minimum-support boundary, U has 31 vertices, W=H\U has 16, and the selected family Q has 56 independent four-sets, seven from each of eight exact-129 colors. Within a color they are disjoint; across colors any two distinct sets intersect in at most one vertex.
- L=overline(H[U]), e(L)=336+delta, and S0=epsilon_U+2delta, where epsilon_U=sum_{u in U}(d_H(u)-12).

## New result in this line

Under the additional four-partite contract for L, the D-part of size 7 and the three large parts A,B,C of size 8 force

\[
\boxed{S_0\ge22}.
\]

Equivalently, the four-partite branch must have delta>=9, because epsilon_U<=4. The proof uses:
1. the eight witness triples partitioning A union B union C for each d in D;
2. the exact D-to-W degree sum 42+epsilon_D;
3. the classification of 8-point transversals;
4. an independent-transversal lemma for the three large parts;
5. the omega(H)<=11 clique cap.

This is stronger than the inherited universal bound S0>=12 and does not assume S0=11/12 is the only open layer. It still leaves the four-partite branch with S0>=22 open.

## Seven-block global system

For every non-target color C:
\[
P_C+R_C+s_C=62,\quad \sum_C P_C=252,\quad
\sum_C R_C=427,\quad \sum_C s_C=3.
\]
For exact-129 colors, s_C=0, R_C>=7, P_C<=55, and the number M_C of exact size-five blocker occurrences obeys M_C>=15+P_C. Thus the sum of P_C over exact colors is at least69, and the total exact-blocker occurrence count over at least eight exact colors is at least189.

A cross-layer lemma is proved in SEVEN_BLOCK_INCIDENCE_LEDGER.md: for each exact-129 color and each outer K12 block, at least one row neighborhood contains one of the six selected B-labelled no-S K5 components. If r_i(C)<=2 and the color has at least two high-k selected components, at least one high-k component is an exact size-five blocker in that block. These are compatibility constraints, not a contradiction. A component-representative edge between two outer blocks is not automatically a duplicate counted in P_C.

## Remaining terminal contract

Two cases remain:

1. **Non-four-partite L:** a K5-free graph on 31 vertices with 56 edge-disjoint K4 witnesses, e(L)=336+delta in [340,353], delta+epsilon_U<=17, S0>=12, and the exact vertex-incidence identities in NON_FOUR_PARTITE_TERMINAL.md. The second-Turán bound e(L)<=354 does not exclude this interval.
2. **Four-partite L:** parts 8,8,8,7, the 56 K4s are transversals, the unused pair slots between each two large parts form a perfect matching, and S0>=22 (hence delta>=9). The seven-block labeled incidence ledger remains mandatory.

The remaining task is to prove a stability/packing contradiction in Case 1 or a genuine color-labeled global contradiction in Case 2. No scalar bound alone is being promoted to closure.

## Scope firewall

This result is conditional on the retained T61, exact-129 factor, 31-point/56-witness, and outer seven-block contracts. It does not close E408 Q32 (285-edge core), E407 Q32, or the original K145 theorem. The original reduction and lower-order seeds remain separate dependencies.


## Audit correction

The earlier ten-witness-star file in the emergency sprint claims \(e(H[U])=135\) or \(e(H[U])\ge144\). Its proof only establishes that the complement L is tripartite, not that it is complete tripartite; missing cross-part edges are not ruled out. This line does not use that dichotomy. See PROOF_DEPENDENCIES.md.

## Latest isolated commits

- Four-partite bound and cross-system analysis: f392c169e549c68cff59caa7f27d968b0ee36d49
- Low-slack blocker normal form and forced component matchings: 75a7a877ab4879cf8dcc2e11e76ecfe64c582e0d
- Non-four-partite terminal contract: b36c1fd87d642186df78147aa203812a57f7ad15
- Dependency audit and pairwise-blocker integration: f272b81656d6abcee4afee5ec26b9262a47f42b0
- Progress log: 8edc7609e15a998daf7ae6365a38fde5819aee50

No graph-level contradiction or independently replayed UNSAT certificate has been produced. The terminal remains OPEN / NOT_CERTIFIED.


## New low-slack global-compatibility result

The pairwise exact-129 blocker theorem has now been integrated into SEVEN_BLOCK_INCIDENCE_LEDGER.md. For an exact-129 color C and a block with \(r_i(C)\le3\), all ten isolated K5 components are represented in exactly one row neighborhood, exactly two rows contain no full component, and each component-containing row has size at most seven. For any two blocks i,j with \(r_i(C),r_j(C)\le3\), the ten corresponding component representatives are forced C-edges forming a matching.

This sharpens the labeled finite contract: every low-slack block induces a partition of the 56 selected witness labels into 12 row classes, each class a matching of pairwise-disjoint selected Q-sets and containing at most one Q from each selected color. The crude capacity \(12\cdot7=84\) still exceeds 56, so this is not yet a contradiction.

## Latest isolated commits

- Low-slack blocker normal form and forced component matchings: 9eac2189941dafc1e75cea36ac56bde1e15105b1
- Dependency integration: b65203ae7b7354fad1849ae924347e0840c38255


## Audit repair

The first draft of the low-slack theorem incorrectly assumed that two row neighborhoods which individually contain no full K5 component must have a union containing no full component. Their union can cover a component by splitting its vertices between the two rows. The proof was repaired before finalizing the result: if there were three no-component rows, each would contribute at least six incidences to the 11-vertex gadget, forcing at least 18 gadget incidences, while the one-or-two rule allows at most \(11+r_i(C)\le14\) when \(r_i(C)\le3\). The current committed proof uses this valid incidence argument.

No full contradiction or independently replayed UNSAT certificate has been produced. The terminal remains OPEN / NOT_CERTIFIED.
