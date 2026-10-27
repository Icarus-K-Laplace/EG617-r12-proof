# E407 Q32 — five-template global labelled-incidence compatibility

Date: 2026-10-26  
Status: **PROVED_CONDITIONAL necessary-structure theorem; global template exclusion remains OPEN.**

## 1. Scope and non-identification rule

Templates A–E are alternative V12 shell states, not five structures that coexist as shell subgraphs in one graph. The question is whether each alternative can be completed using one legal 47-core H, one 29-point support U, the same 49 labelled support witnesses, and the same exact-129 color/component rules.

This note unifies two witness systems without assuming they are identical:
- \(\mathcal Q_U\): the 49 selected independent 4-sets on U, seven per exact-129 color, pairwise linear;
- \(\mathcal R_C\): the no-S \(K_5\)-component witnesses from the exact-129 factorization, written \(\{b\}\cup Q\), with \(b\in B\) and \(Q\subset H\).

Whenever the frozen source contract explicitly identifies a \(\mathcal R_C\) quadruple with a member of \(\mathcal Q_U\), that identity may be used. This theorem does not invent such an identification for components whose label has not been matched.

## 2. Shared contract

Let F be the 61-vertex T61 residual, with \(\alpha(F)\le5\), \(\omega(F)\le11\), a degree-13 pivot p, shell \(A=N_F(p)\), \(|A|=13\), and core \(H=V(F)\setminus(A\cup\{p\})\), \(|H|=47\). Assume the E407 Q32 core contract \(e(H)=284\), \(\alpha(H)\le4\), \(\delta(H)\ge12\), \(\omega(H)\le11\), and total core excess four.

Split the shell \(A=S\dot\cup B\), with \(|S|=3\), \(|B|=10\), and B a target clique. Let \(M=\overline{F[A]}\), so \(sb\in E(M)\) means s and b are nonadjacent in F, and write
\[
D_a=N_F(a)\cap H,\quad t_a=|D_a|,\quad
k_b=|N_M(b)\cap S|\le3.
\]

The V12 row-type screen gives the following necessary floors:

| Template | S-row sizes \(t_s\) | \(M[S]\) | High-k floor |
|---|---|---|---:|
| A | \((12,10,10)\) | empty | at least 6 rows with \(k_b=3\) |
| B | \((11,11,10)\) | empty | at least 8 rows with \(k_b\ge2\) |
| C | \((12,11,10)\) | one edge | at least 6 rows with \(k_b=3\) |
| D | \((11,11,11)\) | one edge | at least 7 rows among the two allowed pair-types and \(k_b=3\) |
| E | \((12,11,11)\) | \(P_3\) | at least 5 rows with \(k_b\ge2\) |

The audited row-type inequalities include A: \(3n_0+2n_1\le8\); B: \(n_2+n_3=10-n_0\ge8\); C: \(3n_0+2n_1\le9\); D: \(n_a+n_b+n_3=10-n_0\ge7\); E: \(n_2+n_3\ge5\). The full row constraints are those in the V12 replay/row-transversal records, not merely these abbreviated inequalities.

## 3. Universal shell-support and missing-hub lemmas

**Lemma 3.1 (three-row support).** Every independent 4-set \(Q\subset H\) hits at least three shell rows:
\[
|\{a\in A:Q\cap D_a\ne\varnothing\}|\ge3.
\]
Proof: if Q missed at least 11 shell vertices, those 11 vertices would form a target clique, because a nonadjacent pair missed by Q would extend Q to an independent 6-set. Together with pivot p this would create a \(K_{12}\), contradicting \(\omega(F)\le11\).

**Lemma 3.2 (every missing hub is hit).** If \(Q\subset H\) is independent of size four, Q is anticomplete to \(b\in B\), and \(sb\in E(M)\), then \(Q\cap D_s\ne\varnothing\). Otherwise \(Q\cup\{s,b\}\) is an independent 6-set in F, contradicting \(\alpha(F)\le5\).

Thus a B-labelled no-S \(K_5\) component \(\{b\}\cup Q\) with \(k_b\ge2\) gives an independent Q that hits at least \(k_b\) distinct S rows and at least three shell rows in total. In A/C, a k=3 component is hub-complete.

## 4. Exact-129 component count and cross-template theorem

**Lemma 4.1 (six B-labelled no-S components).** In every exact-129 color C, the registered factorization has ten pairwise disjoint \(K_5\) components and an 11-vertex exceptional gadget with independence number two. Since \(|S|=3\), at most three \(K_5\) components contain an S vertex, leaving at least seven components avoiding S. At most one of those can contain pivot p without B. Any remaining no-S component with neither B nor p would be a five-vertex independent set in H, contrary to \(\alpha(H)\le4\). Therefore at least six components have the form \(\{b\}\cup Q\) with \(b\in B\), \(|Q|=4\), Q independent in H and anticomplete to b.

Because B is a target clique, a single non-target-color \(K_5\) component contains at most one B vertex. Hence each exact-129 color supplies at least six distinct B labels. At most four of the ten B labels can therefore be outside this no-S component family.

**Theorem 4.2 (template-uniform high-k labelled packing).** Under the shared contract and exact-129 factorization, the number of B-labelled no-S component witnesses with \(k_b\ge2\) in each exact-129 color is at least
\[
\max(0,h-4),
\]
where h is the number of high-k B rows in the shell template.

Proof: at least six distinct B labels occur in the no-S component family, so at most four B labels are missing from it. Intersecting this six-or-more-label set with the h high-k labels gives at least \(h+6-10=h-4\) high-k components. The template-specific floors give:

| Template | High-k no-S witnesses per color | (k=3) no-S witnesses per color | S-row hit incidences per color |
|---|---:|---:|---:|
| A | at least 2 | at least 2 | at least 6 |
| B | at least 4 | not needed | at least 8 |
| C | at least 2 | at least 2 | at least 6 |
| D | at least 3 | not needed | at least 6 |
| E | at least 1 | not needed | at least 2 |

There are at least seven exact-129 colors in E407. Thus the global labelled witness counts are at least 14, 28, 14, 21, and 7 for A–E, respectively, and aggregate S-row hit incidences are at least 42, 56, 42, 42, and 14. In A/C, the k=3-specific floor guarantees at least two hub-complete witnesses per color; any additional high-k witnesses need only be charged two S-row hits each. These witnesses are disjoint within a color; across different colors their Q sets intersect in at most one vertex, since otherwise a shared edge would receive two colors. If the same B label occurs in two colors, the two Q sets are disjoint because the two corresponding \(K_5\)'s already share b and cannot share another vertex.

Each Q also hits at least three shell rows in total by Lemma 3.1. Therefore the minimum total shell-row hit incidences among these selected witnesses are 42, 84, 42, 63, and 21 for templates A–E, respectively.

**Round 6 correction: the A/C hub-complete bound is reinstated conditionally via the registered row-transversal theorem.** See the corrected proof below.

**Theorem 4.3 (A/C hub-complete component packing).** In templates A and C, let h=n3>=6 be the number of full B rows. Among the six B-labelled no-S component quadruples in each exact-129 color, at least max(3,h-4) are hub-complete.

**Proof.** If Q is not hub-complete, choose a hub s that Q misses. Since t_s<=12, the registered row-transversal theorem applies: every independent 4-set in H\D_s meets D_b for each missing shell edge sb. Hence Q hits all h full B rows and requires at least h distinct B-H incidences. The six component quadruples are disjoint within a color, while
\[
c_S=\sum_{b\in B}k_b=3h+n_1\le2h+10<4h.
\]
Thus at most three witnesses can be non-hub-complete. Also, a witness whose own B label has k_b=3 is hub-complete by Lemma 3.2. Therefore a non-hub-complete witness must use one of the 10-h low-k labels, so there are at most 10-h such witnesses. Combining the bounds gives at least \(6-\min(3,10-h)=\max(3,h-4)\) hub-complete witnesses. \(\square\)

**Dependency.** The row-transversal step uses Theorem 3.1 of R12_ROW_TRANSVERSAL_AND_Q33_PACKING.md and the retained R(3,35) exclusion, with t_s<=12. The direct independent-six argument alone does not justify hitting other B rows; the row-transversal theorem supplies that missing implication.

## 5. New support omission–degree identity

This identity uses only the frozen 49-block contract and the exact core ledger; it does **not** identify the 49 support blocks with the separate no-S \(K_5\)-component witnesses.

Let \(\mathcal Q_c=\{Q_{c,1},\ldots,Q_{c,7}\}\) be the seven support blocks in exact-129 color class c. They are pairwise disjoint, each has size four, and \(U=\bigcup_{c,j}Q_{c,j}\) has size 29. Therefore each color class omits exactly one point of U. For \(u\in U\), define
\[
r_u=|\{c:u\notin\bigcup_{j=1}^7Q_{c,j}\}|.
\]
Then
\[
\sum_{u\in U}r_u=7,\qquad m_u:=|\{Q\in\mathcal Q:u\in Q\}|=7-r_u.
\]

Write \(L=\overline{H[U]}\). The 49 blocks contribute 294 distinct edges to L. Let \(x_u\) be the number of additional L-neighbours of u not paired with u inside any selected block. Then \(x_u\ge0\), \(\sum_{u\in U}x_u=2\delta\), and the exact pointwise identity is
\[
d_L(u)=3m_u+x_u=21-3r_u+x_u.
\]
Since \(d_L(u)=28-d_{H[U]}(u)=16-\epsilon_u+d_W(u)\), where \(d_W(u)=d_H(u,W)\), we obtain:

**Theorem 5.1 (support omission–degree identity).**
\[
\boxed{d_W(u)=5+\epsilon_u-3r_u+x_u}
\]
for every \(u\in U\), with
\[
r_u,x_u,\epsilon_u\in\mathbb Z_{\ge0},\quad
\sum_U r_u=7,\quad \sum_U x_u=2\delta,\quad
\sum_U\epsilon_u=\epsilon_U.
\]

Consequences:
- At least 22 points of U have \(r_u=0\), and each such point has \(d_W(u)\ge5\).
- If \(r_u=2\), nonnegative W-degree forces \(\epsilon_u+x_u\ge1\); if \(r_u=3\), it forces \(\epsilon_u+x_u\ge4\); in general \(\epsilon_u+x_u\ge3r_u-5\).
- The sum identity recovers the exact cross-edge ledger:
  \[
  \sum_Ud_W(u)=145+\epsilon_U-21+2\delta
  =124+\epsilon_U+2\delta.
  \]

**Corollary 5.2 (four-clique W saturation budget).** Suppose, additionally, \(H[W]\) is a disjoint union of four cliques and every \(u\in U\) must be complete to at least one of those components (as follows from \(\alpha(H)\le4\)). If every component has size at least \(c_{\min}\), then \(d_W(u)\ge c_{\min}\) and
\[
\epsilon_u+x_u\ge3r_u+c_{\min}-5.
\]
Let \(k=|\{u:r_u>0\}|\le7\). Summing only over these k omitted points gives
\[
2\delta+\epsilon_U\ge21+(c_{\min}-5)k.
\]
In particular, if all four W components have size at least four, then
\[
\boxed{2\delta+\epsilon_U\ge14}.
\]
This is a necessary arithmetic screen, not a terminal exclusion by itself. It does not apply when W has cross-edges unless the required whole-component saturation is separately proved.

## 6. What the theorem does not imply

The labelled packing bounds do not alone contradict the 47-vertex core, its four units of degree excess, or the 49-block support design. In particular:
- The selected \(\mathcal R_C\) sets are not automatically identified with every member of \(\mathcal Q_U\).
- Pairwise linearity on 47 vertices has ample scalar pair capacity for these lower bounds.
- The theorem does not prove that any one template has a legal completion, nor that a template is impossible.
- The original K145-to-T61 bridge and the V12 lower-order seed contracts remain separate.

The next required theorem is a **label-join incompatibility**: connect the per-color component labels b, the 49 support-block labels on U, the exact \(D_a\) shell rows, and the four-unit core degree ledger in a single incidence object. The current frontier is now explicitly reduced to that join plus the low-\(\delta\) case table.


## 7. Cross-template W-side transversal theorem

The separate note SUPPORT_BLOCK_W_TRANSVERSAL_CAPACITY.md now supplies a common constraint for all five shell templates, using only the 49 support blocks and the core independence bound.

Every \(w\in W\) must hit every support block, hence \(d_U(w)\ge7\). Defining \(y_w=d_U(w)-7\),
\[
\sum_{w\in W}y_w=\epsilon_U+2\delta-2\ge7.
\]
Every independent 4-set \(I\subset W\) has \(\sum_{w\in I}y_w\ge1\), and every nonedge \(ww'\in E(\overline{H[W]})\) obeys
\[
|N_H(w,U)\cap N_H(w',U)|\le y_w+y_{w'}.
\]
Thus the positive-slack W vertices hit every independent 4-set of W, and nonadjacent W vertices have a bounded common U-neighborhood. This links the exact core edge ledger to the W-side independence structure without assuming any identity between support blocks and exact-129 component witnesses.

If an independent W-quadruple has total slack one, it forces a \(7,7,7,8\) partition of U with one point from each part in every support block. The three 7-parts are pairwise anticomplete K7s. If \(\epsilon_U+2\delta<16\), the 8-part is a clique or has at most one missing edge. This is a conditional structural branch, not a contradiction.

The two minimum-slack profiles are \((\delta,\epsilon_U)=(3,3),(4,1)\). They have total W-side slack seven and therefore at least eleven zero-slack W vertices. The seven slack units need not belong to seven distinct vertices; no such distribution is assumed.

Current implication: every surviving shell template must be compatible both with its row-transversal system and with this W-side common-neighborhood capacity. The exact-129 component join and the low-\(\delta\) analytic terminals remain OPEN.
