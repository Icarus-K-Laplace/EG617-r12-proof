# Fixed-r=12 Sprint — Labelled Witness-Packing Incompatibility

Date: 2026-10-25  
Branch: `workstream/r12-witness-packing-chat-20261025`

## Status summary

- **PROVED_CONDITIONAL:** each exact-129 non-target color in the E407 Q32 / E408 Q33 shell interface yields at least seven pairwise-linear independent 4-sets in the 47-core.
- **PROVED_CONDITIONAL:** the union of these witnesses has at least 29 core vertices in E407 Q32 and at least 31 core vertices in E408 Q33.
- **OPEN:** this lower bound does not yet contradict the 284-edge core. The unresolved color-count boundary is E407 `129^7,130^4` and E408 Q33 `129^8,130^3`.

This file does not claim the original EG617 theorem is proved.

## 1. Exact hypotheses

Let (F) be the 61-vertex target residual graph with the retained T61 contract. Write

[
V(F)=\{p\}\sqcup A\sqcup H,\qquad |A|=13,\quad |H|=47,
]

where (p) is adjacent in (F) to every vertex of (A) and to no vertex of (H). The core satisfies

[
\alpha(H)\le4,\quad \delta(H)\ge12,\quad e(H)=284,\quad
\sum_{x\in H}(d_H(x)-12)=4.
]

Write (A=S\sqcup B), with (|S|=3), (|B|=10), and assume (B) is a target clique, so (M[B]=\varnothing). The two interfaces considered are:

1. **E407 Q32:** (e(F)=407), all ten (B)-rows are regular and (t_b=d_F(b,H)\le3), and the retained V12 shell reduction has one of the five registered templates.
2. **E408 Q33:** (e(F)=408), with the registered Q33/d3 shell interface and (B) target-clique property. No (t_b\le3) assumption is used below for this interface.

For every non-target color (C) on (F), use the registered T61 color-factor theorem: (e(C[F])\ge129); if equality holds, (C[F]) has ten disjoint isolated (K_5) components and an 11-vertex residual gadget (U_C). Every (C)-monochromatic (K_5) is an independent 5-set in (F), because all its edges have color (C), not the target color.

The edge totals are

[
\binom{61}{2}-407=1423=11\cdot129+4,
\]
[
\binom{61}{2}-408=1422=11\cdot129+3.
]

Consequently E407 Q32 has at least seven exact-129 colors, and E408 Q33 has at least eight.

## 2. Seven-witness lemma per exact-129 color

**Lemma 2.1.** In either interface, each exact-129 color supplies at least seven distinct sets (Q\subseteq H) with (|Q|=4), (alpha(H[Q])=4), such that (Q) is anticomplete in (F) to a corresponding shell label (b\in B), except that one of the seven witnesses may instead be the (H)-part of a component (\{p\}\cup Q). The selected sets are obtained from distinct (K_5) components.

**Proof.**

The ten (K_5) components are vertex-disjoint. At most three can contain a vertex of (S), so at least seven contain no (S)-vertex.

A component with no (S)-vertex cannot consist of five vertices of (H), because that would give an independent 5-set in (H). It cannot contain both (p) and a vertex of (B), since (p) is target-adjacent to all of (A). Therefore every component with no (S)-vertex is either:

- (\{b\}\cup Q), with (b\in B) and (Q\subset H), (|Q|=4); or
- (\{p\}\cup Q), with (Q\subset H), (|Q|=4).

If (p) lies in a (K_5) component, it occupies one of the no-(S) components and contributes one (p+Q) witness; the other six or more no-(S) components give (b+Q) witnesses. If (p) lies in the gadget rather than a (K_5) component, all seven or more no-(S) components must be of the (b+Q) form. In both cases there are at least seven (Q)-sets.

Each (Q) is independent in (H) because the corresponding (K_5) is monochromatic in a non-target color. \(\square\)

## 3. Global linearity across colors

Select seven such (K_5)-component witnesses from every exact-129 color. Within a color, the components are disjoint. Across distinct colors, two components cannot share two vertices: their common edge would then have two colors. Hence any two selected (Q)-sets intersect in at most one vertex.

Let (\mathcal Q) be the resulting family, (n=|\mathcal Q|), and (V_* = \bigcup_{Q\in\mathcal Q}Q), (v=|V_*|). Every (Q) contributes six distinct edges to (\overline H[V_*]), and no edge is contributed twice. Thus

[
e(\overline H[V_*])\ge6n.
]

Also \(\alpha(H)\le4\) implies \(\overline H[V_*]\) is (K_5)-free, so Turán gives

[
e(\overline H[V_*])\le t_4(v).
]

Therefore:

- E407 Q32: (n\ge7\cdot7=49), so (e(\overline H[V_*])\ge294).
- E408 Q33: (n\ge8\cdot7=56), so (e(\overline H[V_*])\ge336).

## 4. Union-size theorem

**Theorem 4.1 (Witness-packing support lower bound).**

Under the hypotheses in Section 1,

[
\boxed{|V_*|\ge29\quad\text{for E407 Q32},}
]
and
[
\boxed{|V_*|\ge31\quad\text{for E408 Q33}.}
]

**Proof for E407 Q32.** Since (t_4(27)=273<294), we have (v\ge28). If (v=28), then (t_4(28)=294), so \(\overline H[V_*]=T_4(28)\), with four parts of size seven. There are exactly 49 witnesses and (H[V_*]) is the disjoint union of four (K_7)'s, so (e(H[V_*])=84).

Let (\epsilon_* = \sum_{x\in V_*}(d_H(x)-12)\ge0). The degree sum on (V_*) is (336+\epsilon_*), hence

[
e_H(V_*,H\setminus V_*)=336+\epsilon_*-2\cdot84
=168+\epsilon_*.
]

Writing (W=H\setminus V_*), we get

[
e(H[W])=284-84-(168+\epsilon_*)=32-\epsilon_*\le32.
]

But (|W|=19) and \(\alpha(H[W])\le4\). By the complement form of Turán's theorem,

[
e(H[W])\ge\binom{19}{2}-t_4(19)=171-135=36,
]

a contradiction. Therefore (v\ge29).

**Proof for E408 Q33.** Since (t_4(29)=315<336), (v\ge30). Suppose (v=30). Then

[
e(\overline H[V_*])\ge336,
\qquad t_4(30)=337.
]

Brouwer's non-partite Turán bound implies that a (K_5)-free graph on 30 vertices with at least (t_4(30)-\lfloor30/4\rfloor+2=332) edges is 4-partite. Thus \(\overline H[V_*]\) is 4-partite.

Every selected (K_4) witness meets each part once. Pairwise edge-disjointness therefore forces every pair of part sizes (n_i,n_j) to satisfy (n_i n_j\ge56). No partition of 30 into four positive part sizes has this property: if any part is at most six, another part is at most eight and their product is at most 48; if all parts are at least seven, the partition is either ((7,7,7,9)) or ((7,7,8,8)), each containing a pair of size-seven parts with product 49. Contradiction. Hence (v\ge31). \(\square\)

## 5. Color-count boundary and stronger conditional outcomes

The exact-129 count is not yet fixed.

- E407 Q32: if at least eight colors have exactly 129 edges, then (n\ge56); the same Turán calculation gives (v\ge31). The only unresolved edge-count profile at this stage is (129^7,130^4), for which the unconditional component packing gives (n\ge49) and (v\ge29).
- E408 Q33: if at least nine colors have exactly 129 edges, then (n\ge63); since (t_4(31)=360<378), (v\ge32). The only unresolved edge-count profile is (129^8,130^3), for which (n\ge56) and (v\ge31).

For E407 Q32 only, the regular-row extension lemma additionally says that an independent triple (X\subseteq H_b) extends to an independent 4-set in (H_b) whenever (t_b\le3): otherwise (H_b\subseteq\bigcup_{x\in X}N_H[x]), whose size is at most (39+\epsilon(X)\le43), contradicting (|H_b|\ge44). This gives a local eighth witness in many individual exact-129 colors when a (K_5) component contains one (S)-vertex and one (B)-vertex. It is **not** counted in the global linear packing above, because extension witnesses from different colors are not automatically pairwise linear.

## 6. What this does not prove

The support lower bound (v\ge29) / (v\ge31) is a new structural restriction, not a contradiction for the full 47-core. The (v\ge31) branch leaves at most 16 core vertices outside the witness union, but no theorem yet rules out that configuration.

Dependencies: retained T61 color-factor theorem; exact-129 component decomposition; legal pivot/core contract; (\alpha(H)\le4); and the stated E407 Q32 or E408 Q33 shell interface. No use is made of the invalid global assumption (\alpha(F)\le3).

## 7. Next single blocker

**Classify the (v=31), (n=56) boundary for E408 Q33 (and the analogous (v=29), (n=49) boundary for E407 Q32):** combine the near-Turán complement on (V_*), the exact core degree/excess budget, and the fact that every vertex outside (V_*) must hit every witness (Q\in\mathcal Q). A complete result must eliminate the boundary or produce an explicitly verified surviving structural kernel.
