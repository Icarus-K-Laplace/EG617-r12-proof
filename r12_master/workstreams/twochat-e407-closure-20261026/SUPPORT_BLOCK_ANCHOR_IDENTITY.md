# E407 Q32 — exact support-block anchor identity

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL on the frozen exact-129 factor theorem / minimum-support boundary. This resolves part of the former label-join gap; E407 remains OPEN.**

## 1. Source contract

The original E407 dependency ledger states that, on the unresolved minimum-support boundary, the exact-129 factor theorem supplies seven disjoint independent 4-set witnesses per exact-129 color, and that within a color these witnesses come from selected disjoint \(K_5\) components of that color.

Thus the 49 support blocks are not an abstract family unrelated to the exact-129 factorization. For every support block \(Q\in\mathcal Q_c\), there is a selected color-c \(K_5\) component

\[
K(Q)=Q\cup\{a(Q)\}
\]

with \(|Q|=4\) and \(Q\subset U\subset H\).

This note records the exact consequences of that identity. It does **not** assert that every no-S B-labelled component belongs to the selected 49-block family.

## 2. The fifth vertex lies outside the core

### Lemma 2.1 — anchor existence

For every support block Q,

\[
\boxed{a(Q)\in\{p\}\cup A}. \tag{2.1}
\]

**Proof.** If the fifth vertex \(a(Q)\) lay in H, then all five vertices of the non-target monochromatic \(K_5\) component would be pairwise target-nonadjacent in H. This would give an independent five-set in H, contradicting \(\alpha(H)\le4\). Hence the fifth vertex is outside H. Since

\[
V(F)=H\dot\cup A\dot\cup\{p\},
\]

it lies in \(\{p\}\cup A\). \(\square\)

Call \(a(Q)\) the **anchor label** of Q.

### Lemma 2.2 — anchors are distinct within a color

For fixed exact-129 color c, the seven anchors

\[
a(Q),\qquad Q\in\mathcal Q_c,
\]

are pairwise distinct.

**Proof.** The seven selected \(K_5\) components of one color are pairwise vertex-disjoint. \(\square\)

Thus every exact-129 color carries a 7-subset of the 14 labels

\[
\{p\}\cup S\cup B.
\]

## 3. At least three selected support blocks per color are B-anchored

The set of non-B anchor labels has size only four:

\[
\{p\}\cup S,\qquad |\{p\}\cup S|=4.
\]

Since each color has seven distinct anchor labels, at least three belong to B.

### Theorem 3.1 — selected B-anchor floor

For each exact-129 color c,

\[
\boxed{|\{Q\in\mathcal Q_c:a(Q)\in B\}|\ge3}. \tag{3.1}
\]

Across the seven exact-129 colors in E407,

\[
\boxed{\text{at least 21 of the 49 support-block occurrences are B-anchored}.} \tag{3.2}
\]

These are genuine members of the 49-block support system, not merely separate component witnesses elsewhere in H.

This is consistent with the independent exact-129 component-packing theorem, which gives at least six B-labelled no-S \(K_5\) components per color among all ten isolated components. The present theorem is different: it guarantees that at least three of the **selected seven support components themselves** are B-anchored.

## 4. Anchor-to-shell row rule

If \(a(Q)=a\in A\), then every edge from a to Q has the non-target color of the \(K_5\) component. Hence Q is target-anticomplete to a:

\[
\boxed{Q\subseteq H\setminus D_a}. \tag{4.1}
\]

Therefore the registered row-transversal theorem applies whenever \(t_a=|D_a|\le12\).

### Theorem 4.1 — labelled row propagation

Let Q be a support block anchored at \(a\in A\), with \(t_a\le12\). For every shell vertex b satisfying

\[
ab\in E(M)=E(\overline{F[A]}),
\]

we have

\[
\boxed{Q\cap D_b\ne\varnothing}. \tag{4.2}
\]

**Proof.** Equation (4.1) gives \(Q\subset H\setminus D_a\). Q is an independent 4-set in H. The row-transversal theorem for the missing shell edge ab now gives \(Q\cap D_b\ne\varnothing\). \(\square\)

In particular, if Q is anchored at \(b\in B\), then Q meets every S-row missing to b. Thus its exact B anchor label carries the same hub-hit requirement previously used only for generic B-labelled component witnesses.

## 5. Template consequences inside the selected 49 blocks

For each exact-129 color define

\[
A_c^B=\{b\in B:\text{some selected support block in color c is anchored at }b\}.
\]

Then

\[
|A_c^B|\ge3.
\]

Let

\[
B_{\ge2}=\{b\in B:k_b\ge2\},\qquad h=|B_{\ge2}|.
\]

Since \(A_c^B\subseteq B\) and \(|B|=10\),

\[
|A_c^B\cap B_{\ge2}|\ge h+3-10=h-7. \tag{5.1}
\]

Therefore:

- Template B has \(h\ge8\), so every exact-129 color contains at least **one selected support block** whose B-anchor misses at least two S hubs.
- Template D has \(h\ge7\), so the universal intersection floor is zero; a stronger conclusion needs its exact row-type split.
- Templates A/C have at least six k=3 labels, but the pure 3-of-10 selected-anchor floor does not by itself force a selected k=3 anchor. Their stronger all-component packing remains useful separately.
- Template E has \(h\ge5\); again no selected high-k anchor follows from cardinality alone.

For Template B specifically, across seven exact-129 colors there are at least seven support-block occurrences Q with a B-anchor \(b\) satisfying \(k_b\ge2\). Each such Q belongs to the 49-block system and meets at least those two S rows; by the universal shell-support theorem it meets at least three shell rows in total.

## 6. Refined label-join status

The former firewall must be split into two statements:

1. **Resolved:** every one of the 49 support blocks is the H-four-set of a selected exact-129 \(K_5\) component and therefore has a genuine anchor label in \(\{p\}\cup A\), distinct within its color class.
2. **Still open:** the set of all six-or-more B-labelled no-S components per color need not coincide with the selected seven support components, and their H-four-sets need not all lie in U. No such equality is assumed.

Thus the support-block/shell-label bridge is now real and callable, while the stronger identification with the full no-S component family remains open.

## 7. Next interface

The five-template compatibility system can now attach variables

\[
a(Q)\in\{p\}\cup S\cup B
\]

to each of the 49 blocks, with:

- seven distinct anchors per color;
- at least three B anchors per color;
- \(Q\cap D_{a(Q)}=\varnothing\) for shell anchors;
- \(Q\cap D_b\ne\varnothing\) for every missing shell edge \(a(Q)b\) when \(t_{a(Q)}\le12\);
- exact U incidence from the support-block design;
- W-side transversal and common-neighbour constraints from the current workstream.

This is strictly stronger than the previous unlabelled join system, but it is not yet a five-template contradiction.
