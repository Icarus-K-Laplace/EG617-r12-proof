# R12 dependency ledger

## Root assumptions
- A: Original balanced 12-edge-coloring of K145: every 13-set contains every color.
- B: Select a least-edge color G, so e(G)<=870.
- C: All induced subgraphs inherit the per-color Turan edge caps.
- D: T61 / R(4,49) residuals must retain their exact contextual contracts; an abstract graph with the same order and edge count is not automatically a legal residual.

## Dependencies and status

| Claim | Required inputs | Status in this workstream |
|---|---|---|
| Each color graph has alpha <= 12 | A | Directly checked. |
| Contextual R(4,49) residual is impossible | F5: alpha(F)<=4, delta(F)>=13; A; second-Turan bound for k=12,n=49 | PROVED_CONDITIONAL; all numerical steps checked. |
| Counterexample reduces to T61 | FRONTEND_BRIDGE_THEOREM F6–F8, 1752-node/144-stop recurrence, contextual R449 contradiction | SOURCE_REPORTED / CONDITIONAL on recurrence certificate and exact contract. |
| Three degree-12 anchors force e(H)>=214 | |H|=35, alpha<=3, omega<=11, delta>=12; three independent degree-12 vertices | PROVED_ANALYTIC in source theorem; contract is narrow and explicit. |
| Three zero-charge signatures create those anchors | Common-S row closure, nonnegative w_v=kappa_v+e_F(v,S) | PROVED_ANALYTIC under common-S contract. Does not extract common-S from arbitrary shell. |
| Collapsed signatures imply <=3 nonempty zero-skeletons | t<=2 signatures and boundary one-loss | PROVED_ANALYTIC under support contract. |
| d2/d3 transversal and owner caps | Boundary one-loss plus low-cross assumptions and hereditary packing lemmas | PROVED_ANALYTIC under stated hypotheses only. |
| Allowance/loss coverage | Exact exchange identity and common-S owner family | PROVED_ANALYTIC under common-S hypotheses; not universal extraction. |
| E407 Cell-B empty | T61 contract, sharp |W|=23 Cell-B normal form, cited Brouwer/KP extremal inputs, color-certificate lemma | PROVED_RELATIVE_TO_INPUTS; does not close E407 Q32 generally. |
| E408 Cell-B empty | T61 contract, global target degree cap <=19, Cell-B degree 20 | PROVED_RELATIVE_TO_INPUTS. |
| E408 seven-block ledger | E408 outer embedding equality ledger and one-or-two rule | PROVED; necessary constraints only. |
| V12 E407 Q32 five templates | Retained lower-order seeds and delivered V12 package | SOURCE_REPORTED; archive replay not completed in source audit. |
| E334 closure | Legal backend/V7 forcing plus source-reported V8 package | SOURCE_REPORTED at package level; graph-theoretic CORE211 obstruction is independently proved. |
| E335–E340 | Universal forcing/extraction Bridge A plus residual shallow-loss closure | OPEN. |
| EG617(r=12) | Complete original K145 -> T61 reduction and elimination of all T61 terminal states | OPEN / NOT_CERTIFIED. |

## Arithmetic audit: contextual R(4,49)

p_12(49)=12*binom(4,2)+4=76.
The second-Turan correction is floor(49/12)-1=3, so each non-target color has at least79 edges.
C(49,2)=1176; 11*79=869; the target has at most307 edges.
delta(F)>=13 gives e(F)>=ceil(637/2)=319.
Since 319>307, contradiction.

## Stale theorem wording

The support-compatibility synthesis uses the weaker anchor consequence e(H)>=213 and q<=E-304. The later K=6 full closure proves e(H)>=214 and q<=E-305 when three independent degree-12 anchors exist. The stronger bound may be used only after those anchors are actually established.

## Added dependency: shell/core witness capacity

- Source: R12_SHELL_CORE_WITNESS_LEMMA.md.
- Required upstream contract: 61-point T61 residual; alpha(F)<=5, omega(F)<=11; 47-core H with alpha(H)<=4; contextual no-R(4,49) exclusion for every 49-subset; inherited target-edge cap D(n).
- Proved outputs: t_a<=7 implies alpha(H\N_H(a))=4; every target edge in F[A] has at least one good endpoint; at least eight shell vertices are good.
- Conditional downstream specialization: in E408 Q33/d3, beta+X+G_B=3 implies all ten B rows have t_b<=6 and hence a maximum independent 4-set witness; each witness hits every S-row corresponding to an M-edge.
- Limitation: no uniqueness/coincidence theorem for the witnesses has been proved. This node does not close Q32/Q33.


## Added cross-cutting witness-capacity dependency

- Source: R12_WITNESS_CAPACITY_CROSSCUT.md.
- Inputs: T61 contract, alpha(F)<=5, omega(F)<=11, e(H)=284, delta(H)>=12, sum epsilon_H=4; exact E407/E408 row contracts as stated in the theorem file.
- Proved outputs: each independent 4-set in H hits at least three shell rows; its hit-hub set covers M[S] and contains every missing hub of its witness b; any independent triple in H_b extends to an independent 4-set when t_b<=3; nonextension at larger t_b forces t_b>=8-epsilon(X).
- E408 Q33 conditional output: at least five no-S K5 components per exact-129 color, at least 7-beta missing-hub incidences across any selected five labels, and cross-color Q-set intersections at most one.
- Limitation: the resulting scalar packing bounds are not contradictory; the same-core E407 templates and E408 Q32/Q33 remain OPEN.

## Independent replay status

V11 and V12 package SHA256 checks and their separate verifier scripts were rerun. Status is COMPUTATION_CERTIFIED for the finite state coverage only; no parent graph is claimed completed, and analytic rule applicability retains its explicit lower-order contracts.


## Added dependency: minimum-transversal boundary classification

- Source: R12_TRANSVERSAL_BOUNDARY_CLASSIFICATION.md.
- Inputs: exact-129 factor classification; seven selected Q-sets per selected color; cross-color linearity; \(\alpha(H)\le4\); core excess four; the seven-neighbour transversal theorem.
- E407 Q32 output: the 29-vertex / 49-witness boundary requires at least two complement edges not covered by the witness K4s.
- E408 Q33 output: the 31-vertex / 56-witness boundary requires \(2\delta+\epsilon_U\ge8\), and the existing core edge ledger gives \(\delta+\epsilon_U\le17\).
- Status: PROVED_CONDITIONAL necessary-structure theorem. The arithmetic verifier is a regression check only. No remaining boundary profile is eliminated by this node, and E408 Q32 is excluded from its scope.

## Audit correction: shell-incidence union lemma

- Source: R12_SHELL_INCIDENCE_UNION_AUDIT.md.
- The identity \(\sum_x(r_A(x)-1)=e(M)-15\) is exact, but comparing a support-restricted sum to the full sum requires \(r_A(x)\ge1\) off the support.
- Under the frozen contract, \(r_A(x)=0\) can occur at a core vertex with positive excess. There are at most four such vertices.
- Corrected full-row support-union floors: E407 template A >=7; template C >=6. The imported 11/10 floors are not certified unless zero-shell-support absence is proved separately.
- This audit changes no root dependency and closes no terminal.


## Added dependency: E408 Q33 four-partite S0=10 exclusion

- Source: R12_E408_Q33_FOUR_PARTITE_S0_10_EXCLUSION.md.
- Inputs: the 31-vertex/56-witness boundary; L four-partite with parts (8,8,8,7); exact D-large pair coverage; \(\alpha(H)\le4\); core excess four; the seven-neighbour floor for W.
- Intermediate constraints: \(\delta\in\{3,4,5\}\) if \(S_0=10\); at least three zero-excess vertices in D; at most three W-neighbourhoods can contain any given large part; a size-8/9 hitting set either contains all of D or a full large part.
- Output: the sole candidate degree pattern with a size-10 exceptional hitting set is contradictory in each \(s=|T_*\cap D|\in\{0,1,2\}\) case. Thus four-partite E408 Q33 has \(S_0\ge11\).
- Audit: verify_e408_q33_four_partite_s0_10.py passed integer-pattern checks; no graph-realization claim.
- Scope firewall: does not apply to non-four-partite L or E408 Q32.
