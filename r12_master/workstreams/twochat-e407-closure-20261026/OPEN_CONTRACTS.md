# E407 Q32 — open contracts and minimum missing implications

Date: 2026-10-26  
Status: **OPEN / NOT_CERTIFIED.**

## C1. Same-core labelled-incidence join — primary blocker

Need one explicit incidence object containing simultaneously:
- the 47-vertex target core H and its 284 edges, minimum degree 12, alpha at most 4, inherited clique bound 11, and four-unit degree excess;
- the support U of size 29 and W=H\U of size 18;
- the 49 selected independent 4-sets on U, with seven blocks per exact-129 color, omitted point per class, and pairwise linearity;
- the five alternative shell-template row systems \(D_a=N_F(a)\cap H\), with the correct row sizes and M[S] pattern;
- the ten \(K_5\) components and exceptional gadget for every exact-129 color, including the pivot/S/B labels;
- edge uniqueness, row-hit constraints, common-neighbour sets, W-component labels, and the four-unit degree-excess distribution.

Current proven output: FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md gives the per-color high-k component floor 2,4,2,3,1 for A–E. The conditional A/C bound max(3,h-4) is now proved via the registered row-transversal theorem under the R(3,35) contract; the direct independent-six proof route was corrected. The support omission-degree identity is also proved. LABEL_JOIN_SYSTEM.md records the variable families and equations. Missing implication: the support blocks, shell rows, component labels, and same H must be joined into either a certified contradiction or an explicit legal realization.

## C2. Witness identity / overlap contract

Do not assume the 49 support blocks \(\mathcal Q_U\) are identical to every high-k no-S component quadruple \(\mathcal R_C\). For each exact-129 color, record which of its ten \(K_5\) components supplies each selected support block, which shell label (S, B, pivot, or no shell label) the component carries, and how its four core vertices meet U/W. The support system cannot be closed by counting an unlabelled union alone.

## C3. V12 template screen dependency

The five A–E templates cover the 554 finite-screen survivors under the V12 lower-order seed and analytic-screen contract. The independent replay certifies finite coverage of the supplied state model, not the analytic elimination rules or existence/impossibility of a common-core completion. A proof of the retained lower-order seeds and each screen hypothesis remains part of the parent dependency chain.

## C4. Low-\(\delta\) terminal

The exact integer table is in LOW_DELTA_TERMINAL_TABLE.md. Frontier notes:
- \(\delta=13,\epsilon_U=0\), including four-partite and non-four-partite \(L_U\);
- See Round 4 proof note; this previously listed four-partite W-profile is no longer open.
- \(\delta=13\) non-four-partite \(L_U\) for all feasible \(\epsilon_U\);
- every \(\delta\le12\) case. No reduction for \(\delta=13\) may be extrapolated to \(\delta\le12\).

## C5. Conditional \(\delta=14\) saturated dependency

The non-four-partite \(\delta=14\) saturated branch is excluded only conditional on the alpha-critical reduction and the Didin 2026 preprint component-count theorem. Until that theorem is independently audited under its exact hypotheses, retain PROVED_CONDITIONAL.

## C6. Parent bridge and root theorem

The 47-core contract is a T61-derived local contract. The original \(K_{145}\)-to-T61 implication, including the recurrence archive, lower-order seed dependencies, and conversion to the seven genuine unanchored blocks, is not certified end-to-end here. Root main also still lists E408 and E333–E340 as obligations. Neither E407 closure alone nor the local core contract proves EG617(r=12).


Round 4 update: the four-partite delta=13, epsilon_U=2 profile with W equal to K4+K4+K5+K5 and one cross-edge is now excluded under the registered profile contract. The non-four-partite delta=13 cases and every delta<=12 case remain open.


## C7. W-side support-block transversal join

Every \(w\in W\) has \(d_U(w)\ge7\), and \(Y=\sum_W(d_U(w)-7)=\epsilon_U+2\delta-2\ge7\). Every independent W-quadruple has total Y-slack at least one; every nonadjacent W-pair has U-neighborhood intersection at most the sum of its individual slacks.

For the minimum-slack profiles \((3,3)\) and \((4,1)\), Y=7 and at least eleven W vertices have zero slack. The remaining issue is to exploit the zero-slack neighborhood classes and the degree caps \(d_W(w)=5+\epsilon_w-y_w\). Do not assume the seven units of Y are spread across seven vertices.

If an independent W-quadruple has total slack one, a \(7,7,7,8\) support transversal design is forced, including three pairwise anticomplete K7 parts and the R-side omission restrictions in SUPPORT_BLOCK_W_TRANSVERSAL_CAPACITY.md. The open alternative is that every independent triple in \(W_0\) is met by every \(y=1\) vertex, so no slack-one quadruple exists. Neither branch has yet been excluded.


## C8. Low-slack zero-neighborhood class structure

When \(\epsilon_U+2\delta<16\), the zero-slack W vertices have at most three distinct U-neighborhoods; vertices with the same neighborhood form a clique, and distinct neighborhoods are disjoint 7-point transversals. For the minimum-slack profiles (3,3) and (4,1), there are at least eleven zero-slack vertices but at most three neighborhood classes. The remaining problem is to combine these class sizes, the exact W degree sequence \(d_W(w)=5+\epsilon_w-y_w\), and \(\alpha(H[W])=4\). No contradiction has yet been derived for the branch in which all independent W-quadruples have total slack at least two.


## C9. Minimum-slack multiplicity

For the two profiles \((3,3)\) and \((4,1)\), total W-side slack is seven, but it cannot be concentrated on a single vertex. At least two vertices have positive slack and at least eleven have zero slack. The remaining possible distributions of the seven units, together with the at-most-three zero-neighborhood clique classes, must be reconciled with \(\alpha(H[W])=4\). A slack-one independent W-quadruple is still not guaranteed.

## C10. Minimum-slack exact-core branch

`MINIMUM_SLACK_EXACT_CORE.md` closes the structural classification of the **slack-one independent-four-set branch** for \(\epsilon_U+2\delta=9\).

If such a quadruple exists, then \(L_U=\overline{H[U]}\) is exactly four-partite with parts \((7,7,7,8)\), the size-eight part is a target K8, and all extra complement edges lie among the 21 missing T-R partner pairs. The three seven-parts are target K7s and pairwise target-anticomplete.

For \((\delta,\epsilon_U)=(4,1)\), only omission pattern \((1^7,0)\) survives; there are three exact target K11s \(T_i\cup C_i\), the residual set N has size six, and the unique zero-omission R-point has exactly N as its W-neighborhood.

For \((3,3)\), only \((2,1^5,0^2)\) and \((1^7,0)\) remain. The first forces three K11s and |N|=6; the second has class sizes \((4,4,4)\) or \((4,4,3)\).

The remaining minimum-slack blocker is therefore precise: either exclude these finite exact-core kernels by shell-template compatibility, or prove that every independent W-four-set has total slack at least two and then close that complementary domination branch. No claim is made that either task is already solved.
