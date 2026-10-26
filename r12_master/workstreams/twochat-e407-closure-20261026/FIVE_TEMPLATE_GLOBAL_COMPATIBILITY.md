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

Because B is a target clique, a single non-target-color \(K_5\) component contains at most one B vertex. Hence each exact-129 color supplies at least six distinct B labels. At least four of the ten B labels are therefore outside this no-S component family.

**Theorem 4.2 (template-uniform high-k labelled packing).** Under the shared contract and exact-129 factorization, the number of B-labelled no-S component witnesses with \(k_b\ge2\) in each exact-129 color is at least
\[
\max(0,h-4),
\]
where h is the number of high-k B rows in the shell template.

Proof: at least six distinct B labels occur in the no-S component family, so at most four B labels are missing from it. Intersecting this six-or-more-label set with the h high-k labels gives at least \(h+6-10=h-4\) high-k components. The template-specific floors give:

| Template | h floor | High-k no-S witnesses per exact-129 color | Required S-row hits per such witness |
|---|---:|---:|---:|
| A | 6 (including \(k=3\)) | 2 | 3 |
| B | 8 | 4 | at least 2 |
| C | 6 (including \(k=3\)) | 2 | 3 |
| D | 7 | 3 | at least 2 |
| E | 5 | 1 | at least 2 |

There are at least seven exact-129 colors in E407. Thus the global labelled witness counts are at least 14, 28, 14, 21, and 7 for A–E, respectively. These witnesses are disjoint within a color; across different colors their Q sets intersect in at most one vertex, since otherwise a shared edge would receive two colors. If the same B label occurs in two colors, the two Q sets are disjoint because the two corresponding \(K_5\)'s already share b and cannot share another vertex.

Each Q also hits at least three shell rows in total by Lemma 3.1. Therefore the minimum total shell-row hit incidences among these selected witnesses are 42, 84, 42, 63, and 21 for templates A–E, respectively.

## 5. What the theorem does not imply

The labelled packing bounds do not alone contradict the 47-vertex core, its four units of degree excess, or the 49-block support design. In particular:
- The selected \(\mathcal R_C\) sets are not automatically identified with every member of \(\mathcal Q_U\).
- Pairwise linearity on 47 vertices has ample scalar pair capacity for these lower bounds.
- The theorem does not prove that any one template has a legal completion, nor that a template is impossible.
- The original K145-to-T61 bridge and the V12 lower-order seed contracts remain separate.

The next required theorem is a **label-join incompatibility**: connect the per-color component labels b, the 49 support-block labels on U, the exact \(D_a\) shell rows, and the four-unit core degree ledger in a single incidence object. The current frontier is now explicitly reduced to that join plus the low-\(\delta\) case table.
