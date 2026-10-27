# E407 Q32 — repeated-anchor transversal packing

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL on the frozen exact-129 selected-component identity and the retained row-transversal theorem. Necessary structure only; E407 remains OPEN.**

## 1. Setup

Work under the current E407 Q32 minimum-support contract. There are seven exact-129 color classes. For every exact color `c`, its seven selected support blocks are pairwise-disjoint independent four-sets in `U`, and every selected block `Q` is the core part of an isolated color-`c` `K5`

\[
Q\cup\{a(Q)\},\qquad a(Q)\in\{p\}\cup A.
\]

For a shell anchor `a in A`, write

\[
D_a=N_F(a)\cap H,\qquad t_a=|D_a|.
\]

For a label `a in {p} union A`, let

\[
m_a:=|\{c:\text{one selected support block of color }c\text{ is anchored at }a\}|.
\]

There is at most one such block in a fixed color because the seven selected anchors in one exact color are distinct.

In E407 Q32, for every `b in B`, the frozen shell contract gives

\[
t_b=k_b:=|N_M(b)\cap S|\le3.
\]

We use the retained row-transversal theorem: if `ab in E(M)` and `t_a<=12`, then every independent four-set in `H\D_a` meets `D_b`.

## 2. Same-anchor blocks are disjoint across colors

### Lemma 2.1

Fix an anchor label `a in {p} union A`. Selected support blocks anchored at `a` in two different exact colors are disjoint.

### Proof

Suppose color-`c` block `Q_c` and color-`d` block `Q_d`, `c!=d`, are both anchored at `a` and share `u in U`. Since `Q_c union {a}` is a color-`c` `K5`, the edge `au` has color `c`. Since `Q_d union {a}` is a color-`d` `K5`, the same edge `au` has color `d`. Edge-color uniqueness gives a contradiction. Therefore `Q_c intersect Q_d` is empty. QED.

Consequently a repeated anchor of multiplicity `m_a` owns exactly `4m_a` distinct support points.

### Corollary 2.2 — shell-row avoidance packing

If `a in A`, every block anchored at `a` is target-anticomplete to `a`, hence lies in `U\D_a`. Thus

\[
\boxed{4m_a\le29-|D_a\cap U|.}\tag{2.1}
\]

In particular `m_a<=7`.

## 3. Pointwise anchor injectivity

### Lemma 3.1

Fix `u in U`. Across all selected support blocks containing `u`, the anchor labels are pairwise distinct.

### Proof

Blocks of one exact color are disjoint, so at most one block of a given color contains `u`. If two different colors used the same anchor `a`, then exactly as in Lemma 2.1 the edge `au` would receive both colors. QED.

If `r_u` is the number of exact color classes omitting `u`, then `u` belongs to exactly `7-r_u` support blocks. Therefore `u` sees exactly `7-r_u` distinct selected anchor labels through those blocks.

This is a genuine labelled-incidence constraint: the 196 support-block point incidences form a simple bipartite incidence graph between `U` and the fourteen possible outside-core anchor labels.

## 4. Oriented missing-edge capacity

### Theorem 4.1 — repeated-anchor transversal capacity

Let `a,b in A` satisfy

\[
ab\in E(M),\qquad t_a\le12.
\]

Then

\[
\boxed{m_a\le |D_b\cap U|\le t_b.}\tag{4.1}
\]

### Proof

Every support block `Q` anchored at `a` is an independent four-set contained in `H\D_a`. The row-transversal theorem therefore gives

\[
Q\cap D_b\ne\varnothing.
\]

By Lemma 2.1, the `m_a` blocks anchored at `a` are pairwise disjoint. Hence their intersections with `D_b` require at least `m_a` distinct points of `D_b`. Because every such block lies in `U`, those points lie in `D_b\cap U`. Thus

\[
m_a\le |D_b\cap U|\le|D_b|=t_b.
\]

QED.

### E407 specialization

For `s in S` and `b in B` with `sb in E(M)`, all E407 B rows satisfy `t_b=k_b<=3`, while every S-row has size at most 12. Orienting the theorem from `s` to `b` gives

\[
\boxed{m_s\le k_b.}\tag{4.2}
\]

Thus:

- if `s` has a missing B-neighbor with `k_b=1`, then `m_s<=1`;
- if its smallest missing B-row has `k_b=2`, then `m_s<=2`;
- otherwise any missing full row gives `m_s<=3`.

Conversely, orienting from `b` to `s` gives

\[
\boxed{m_b\le |D_s\cap U|\le t_s}\tag{4.3}
\]

for every missing pair `sb`.

Equations (4.2)-(4.3) are simultaneous: the same repeated-anchor block family must be a disjoint transversal packing for every row opposite its anchor in `M`.

## 5. Immediate global multiplicity consequences

The selected-B-anchor theorem gives at least five selected B anchors in each of the seven exact colors. Hence

\[
\sum_{b\in B}m_b\ge35.
\]

Since every `m_b<=7` and `|B|=10`:

1. some B label has `m_b>=4`;
2. in fact at least **two** B labels have `m_b>=4`.

For (2), if at most one label had multiplicity at least four, then the total would be at most

\[
7+9\cdot3=34,
\]

contradicting the lower bound 35.

The template-specific high-`k` selected-anchor floors sharpen this:

- A/C: at least seven selected high-`k` (indeed `k=3`) B-anchor occurrences among the seven exact colors, so some full B row is selected in at least two colors.
- B: at least 21 selected `k>=2` B-anchor occurrences. Since there are at most ten B labels, some high-`k` B row is selected in at least three colors.
- D: at least 14 selected `k>=2` B-anchor occurrences, so some high-`k` B row is selected in at least two colors.
- E: the current five-B-anchor intersection bound alone does not force a selected high-`k` row.

For templates A/C, every `k=3` row is missing to every S hub; hence every S hub has a missing B-neighbor with `k_b=3`, and (4.2) gives the uniform bound

\[
\boxed{m_s\le3\quad\text{for all }s\in S.}\tag{5.1}
\]

Any actual lower-`k` row missing to a hub improves this bound automatically.

## 6. Audit and scope

The proof uses exactly two labelled inputs beyond the pure graph contract:

1. **selected-component identity:** every one of the 49 support blocks is the H-four-set of a selected isolated exact-color `K5` with a genuine outside-core anchor;
2. **row-transversal theorem:** under the retained `R(3,35)` exclusion, every independent four-set in `H\D_a` meets `D_b` when `ab` is a shell missing edge and `t_a<=12`.

The E407 equality `t_b=k_b<=3` is explicitly recorded in the audited row-transversal source.

No external extremal theorem beyond the already-registered inputs used to establish those two parent contracts is newly invoked here. The argument does not use the Didin-dependent delta=14 saturated branch.

This theorem does **not** exclude a shell template by itself. It upgrades the five-template problem from an unlabelled anchor count to a simple anchor-point incidence system with oriented row capacities. A terminal contradiction still has to combine these capacities with the 29-point support design, W-side slack/core structure, or the exact residual `3K5 + G11` factor.
