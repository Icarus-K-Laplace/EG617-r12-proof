# E407 Q32 — selected B-anchor floor from the exact-129 factor

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL on the frozen exact-129 factor theorem and SUPPORT_BLOCK_ANCHOR_IDENTITY.md. E407 Q32 remains OPEN.**

## 1. Contract

Fix one of the seven exact-129 non-target colors c. The retained factor theorem decomposes its 61-vertex color graph into ten pairwise-disjoint isolated K5 components and one 11-vertex exceptional gadget G_c with independence number two.

On the minimum-support boundary, seven of the ten K5 components are the selected support components

\[
Q_{c,j}\cup\{a_{c,j}\},\qquad j=1,\ldots,7,
\]

where the seven Q-blocks are disjoint 4-subsets of U covering 28 of the 29 U-points and the seven anchors a_{c,j} are distinct vertices of {p} union A. Let

\[
b_c:=|\{j:a_{c,j}\in B\}|.
\]

The shell set B has ten vertices and is a target K10. Hence every B-B edge has the target color and is absent from the color-c graph.

## 2. Main theorem: 5 <= b_c <= 7

Partition the ten B labels according to their location in the exact color-c factorization:

- b_c B-vertices lie in the seven selected K5 components;
- u_c B-vertices lie in the three unselected K5 components;
- g_c B-vertices lie in the exceptional gadget G_c.

These three classes are disjoint and exhaustive, so

\[
 b_c+u_c+g_c=10. \tag{2.1}
\]

Because B is a target clique, a color-c K5 contains at most one B vertex. Therefore

\[
 u_c\le3. \tag{2.2}
\]

Also B cap G_c is an independent set in the color-c graph. Since alpha(G_c)=2,

\[
 g_c\le2. \tag{2.3}
\]

Combining (2.1)--(2.3),

\[
\boxed{b_c\ge10-3-2=5.} \tag{2.4}
\]

There are only seven selected components, so b_c<=7. Thus

\[
\boxed{b_c\in\{5,6,7\}.} \tag{2.5}
\]

Moreover the only arithmetic placements (b_c,u_c,g_c) are

\[
(5,3,2),\ (6,2,2),\ (6,3,1),\ (7,1,2),\ (7,2,1),\ (7,3,0). \tag{2.6}
\]

This immediately makes every earlier b_c=3 or b_c=4 residual branch vacuous.

## 3. Sharp b_c=5 structure

Assume b_c=5. Then (2.6) forces u_c=3 and g_c=2. Thus all three unselected K5 components contain a B vertex, while the exceptional gadget contains two B vertices.

There are seven selected anchors total, so exactly two selected anchors lie in {p} union S.

### Lemma 3.1 — the pivot p is selected when b_c=5

Suppose p were not selected. In the 26-vertex residual factor, p must lie either in one of the three unselected K5 components or in G_c.

- It cannot lie in an unselected K5 component: each of those components already contains a B vertex, and p is target-adjacent to every shell vertex, in particular to every B vertex. A target edge cannot simultaneously be a color-c edge of the K5.
- It cannot lie in G_c: the gadget already contains two B vertices. The three vertices p,b_1,b_2 are pairwise target-adjacent (p is adjacent to all shell vertices and B is a target clique), so none of their three edges has color c. They would form an independent 3-set in G_c, contradicting alpha(G_c)=2.

Hence p must be selected. Therefore the second non-B selected anchor is exactly one S-vertex.

So

\[
\boxed{b_c=5\Longrightarrow A_c^{sel}=\{p,s_c\}\cup B_c,\quad s_c\in S,\ |B_c|=5.} \tag{3.1}
\]

In particular, in every exact-129 color there is at most one selected S-anchor: for b_c=5 this follows from (3.1), for b_c=6 there is only one selected non-B anchor total, and for b_c=7 there are none.

Thus

\[
\boxed{|A_c^{sel}\cap S|\le1\text{ for every exact-129 color }c.} \tag{3.2}
\]

Across the seven exact colors, at least 35 of the 49 selected support-block occurrences are B-anchored, and at most seven are S-anchored.

## 4. Five-template consequences on the actual 49 support blocks

Let H_{>=2}={b in B:k_b>=2} and h=|H_{>=2}|. Because each color has at least five selected B-anchor labels,

\[
|A_c^{sel}\cap H_{>=2}|\ge h+5-10=h-5. \tag{4.1}
\]

Using the audited V12 row floors gives the following lower bounds **inside the selected 49-block system**, not merely among auxiliary component witnesses:

| Template | h floor | selected high-k B-anchors per exact color | across seven colors |
|---|---:|---:|---:|
| A | 6 (all high rows have k=3) | at least 1 | at least 7 |
| B | 8 | at least 3 | at least 21 |
| C | 6 (all high rows have k=3) | at least 1 | at least 7 |
| D | 7 | at least 2 | at least 14 |
| E | 5 | no positive intersection floor | 0 from this argument |

For A/C, every selected high-k block is B-anchored with k_b=3 and is therefore hub-complete by the missing-hub six-set lemma. For B/D, every selected high-k block hits at least two S rows. These conclusions concern the genuine selected support blocks supplied by SUPPORT_BLOCK_ANCHOR_IDENTITY.md.

## 5. Correction to SELECTED_COMPONENT_RESIDUAL_PARTITION.md

The previous residual theorem allowed b_c=3,4,5,6,7 because it used only the weaker anchor floor b_c>=3. The new factor argument proves b_c=3 and b_c=4 impossible. Its conditional sections describing what would happen at b_c=3 remain logically true implications from an impossible premise but are no longer live branches.

The generic no-S residual-component floor m_c=max(0,6-b_c) must not be replaced by 8-b_c: an unselected K5 that contains B may also contain an S vertex and then need not contribute a four-point subset of H. Therefore, after this theorem, the guaranteed no-S residual floor is only

- b_c=5: m_c>=1;
- b_c=6 or 7: no positive no-S residual floor from the six-component theorem.

This firewall prevents overusing the new B-placement count.

## 6. Dependency class and scope

This is a **labelled exact-129 factor theorem**, not a pure 47-core graph theorem. It uses:

1. the exact-129 Type-I factorization into 10K5 plus an 11-vertex gadget with color independence number two;
2. the selected-support-component identity identifying the seven support blocks with seven of those K5 components;
3. the shell facts that B is a target K10 and p is target-adjacent to all shell vertices.

It does not use Brouwer, the Didin preprint, the delta=14 saturated reduction, or any low-delta W-profile classification.

It does not close any of templates A-E by itself. The next global compatibility target is to combine the 35-or-more selected B anchors, the at-most-seven selected S anchors, the template row system, and the common 284-edge core/support design.
