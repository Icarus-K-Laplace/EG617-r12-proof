# Fixed-r=12 Sprint — Labelled Witness Packing and Core-Support Bounds

Date: 2026-10-25  
Branch: workstream/r12-witness-packing-chat-20261025

## Status

- **PROVED_CONDITIONAL:** each exact-129 color supplies at least seven independent four-sets in the 47-core, but only six are guaranteed to have labels in the ten-vertex shell set B.
- **PROVED_CONDITIONAL:** in the 284-edge core, each exact-129 color supplies at least two B-labelled witness four-sets whose vertices all have core degree 12. Thus there are at least 14 such witnesses in E407 Q32 and at least 16 in E408 Q33.
- **PROVED_CONDITIONAL:** the full seven-set-per-color family has union size at least 29 in E407 Q32 and at least 31 in E408 Q33. If E407 has at least eight exact-129 colors, its union also has size at least 31.
- **OPEN:** the boundary kernels are not excluded. The only residual edge-count profiles not removed by the support bound are \(129^7,130^4\) for E407 Q32 and \(129^8,130^3\) for E408 Q33.

All claims below retain the T61 and exact-129 factor contracts. This is not a proof of the original EG617 theorem.

## 1. Frozen hypotheses

Let F be a 61-vertex target residual, with a legal degree-13 pivot p, shell A=N_F(p), |A|=13, and core H=V(F)\(A union {p}), |H|=47. The retained contract includes

\[
\alpha(F)\le5,\quad \omega(F)\le11,\quad
\alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12.
\]

For E407 Q32 and E408 Q33, the core has

\[
e(H)=284,\qquad
\sum_{x\in H}(d_H(x)-12)=2e(H)-47\cdot12=4.
\]

Write A=S dot-union B, where |S|=3 and |B|=10, with B a target clique. Let X={x in H:d_H(x)>12}. Since every positive excess is an integer,

\[
|X|\le\sum_{x\in H}(d_H(x)-12)=4.
\]

For each exact-129 non-target color C, assume the retained constrained second-Turán/Kang–Pikhurko factor theorem: C[F] has ten vertex-disjoint isolated K5 components and an 11-vertex exceptional gadget U_C. Every such K5 is target-independent.

## 2. Correct component count: seven Q-sets, six B-labelled Q-sets

**Lemma 2.1.** Every exact-129 color C supplies at least seven distinct independent four-sets Q contained in H, pairwise disjoint within C, arising from K5 components that avoid S. At least six of these have the labelled form {b} union Q with b in B and b anticomplete to Q. The possible seventh is the H-part of a component {p} union Q.

**Proof.** The ten K5 components are disjoint and there are only three vertices in S, so at least seven components avoid S. At most one of these contains p. A component containing p cannot contain any vertex of A, because p is target-adjacent to all of A; its other four vertices therefore lie in H and give a set Q. Every other component avoiding S and p lies in B union H. It cannot contain two B vertices because B is a target clique, and it cannot lie entirely in H because that would be a target-independent five-set in H. Hence it has exactly one b in B and four vertices Q in H. This gives at least six B-labelled components and at least seven Q-sets total. ∎

If p lies in U_C rather than in a K5 component, all seven or more components avoiding S are B-labelled. The conservative count used below is seven total Q-sets and six B-labelled Q-sets per exact-129 color.

For two selected Q-sets from different colors, the intersection has size at most one: if they shared two core vertices, their common edge would be assigned two non-target colors. Within a color, the selected components are disjoint. Thus the family of all selected Q-sets is linear (pairwise intersections at most one).

## 3. Zero-excess strengthening

**Lemma 3.1.** In the 284-edge core, each exact-129 color has at least two B-labelled witnesses {b} union Q for which every q in Q has d_H(q)=12.

**Proof.** By Lemma 2.1, there are at least six B-labelled Q-sets disjoint within the color. At most |X|≤4 of these disjoint sets can meet X: each set that meets X uses at least one distinct vertex of X. Therefore at least two of the six Q-sets lie wholly in H\X, and all four vertices of each have core degree 12. ∎

Consequences under the exact-129 color-count contract:

- E407 Q32 has at least seven exact-129 colors, hence at least 14 pairwise-linear zero-excess B-labelled witnesses.
- E408 Q33 has at least eight exact-129 colors, hence at least 16 such witnesses.

These are actual monochromatic K5-component witnesses, so their cross-color intersection cap is valid. This improves the one-zero-excess-witness lower bound in the sibling zero-excess workstream by combining its degree theorem with the corrected six-B-label component count.

## 4. Turán support bound for the union of all seven Q-sets per color

Let \(\mathcal Q\) contain seven selected Q-sets from every exact-129 color, including the possible p+Q set. Let m=|\(\mathcal Q\)| and V_* be their union, with v=|V_*|. Since the family is linear, each Q contributes six distinct edges to \(\overline H[V_*]\), and no edge is counted twice. Therefore

\[
e(\overline H[V_*])\ge6m.
\]

Since \(\alpha(H)\le4\), the graph \(\overline H[V_*]\) is K5-free, so

\[
e(\overline H[V_*])\le t_4(v),
\]

where t_4(v) is the balanced complete four-partite Turán edge count.

The exact color totals on F are

\[
\binom{61}{2}-407=1423=11\cdot129+4,
\]
\[
\binom{61}{2}-408=1422=11\cdot129+3.
\]

Thus E407 has at least seven exact-129 colors and E408 has at least eight.

### Theorem 4.1 (union-size lower bounds)

- E407 Q32: m≥49 and v≥29.
- E408 Q33: m≥56 and v≥31.
- If E407 has at least eight exact-129 colors, then m≥56 and v≥31.
- If E408 has at least nine exact-129 colors, then m≥63 and v≥32.

**Proof, E407 with seven exact-129 colors.** Since 6m≥294 and t_4(27)=273, v≥28. Suppose v=28. Then t_4(28)=294, so \(\overline H[V_*]\) is the extremal complete balanced four-partite graph with four parts of size seven. Hence H[V_*] is four disjoint K7s and e(H[V_*])=84.

Let \(\epsilon_*=\sum_{x\in V_*}(d_H(x)-12)\ge0\) and W=H\V_*. The degree sum on V_* is 336+\(\epsilon_*\), so

\[
e_H(V_*,W)=336+\epsilon_*-2\cdot84=168+\epsilon_*.
\]

Therefore

\[
e(H[W])=284-84-(168+\epsilon_*)=32-\epsilon_*\le32.
\]

But |W|=19 and \(\alpha(H[W])\le4\), so the complement form of Turán gives

\[
e(H[W])\ge\binom{19}{2}-t_4(19)=171-135=36,
\]

a contradiction. Thus v≥29.

**Proof, E408 Q33 or E407 with at least eight exact-129 colors.** Here 6m≥336. Since t_4(29)=315, v≥30. Suppose v=30. Then e(\(\overline H[V_*]\))≥336, while t_4(30)=337. Brouwer's second-Turán bound says a K5-free non-four-partite graph on 30 vertices has at most \(337-\lfloor30/4\rfloor+1=331\) edges. Hence \(\overline H[V_*]\) is four-partite.

Every Q in \(\mathcal Q\) is a K4 in \(\overline H[V_*]\), so it uses one vertex from each part. Since there are at least 56 Q-sets and their edges are pairwise disjoint, every pair of parts of sizes \(n_i,n_j\) must satisfy \(n_i n_j\ge56\). If any part has size at most six, another has size at most eight and their product is at most 48. If every part has size at least seven, the only partitions of 30 are (7,7,7,9) and (7,7,8,8), each containing a pair of parts of product 49. Both contradict \(n_i n_j\ge56\). Hence v≥31.

For E408 with at least nine exact-129 colors, 6m≥378>t_4(31)=360, so v≥32. ∎

## 5. Exact unresolved color-count boundary

The residual non-target edge excess over 11 times 129 is four for E407 and three for E408.

- E407 is not removed by this theorem only at the profile \(129^7,130^4\). If there are eight or more exact-129 colors, v≥31.
- E408 Q33 is not removed only at \(129^8,130^3\). If there are nine or more exact-129 colors, v≥32.

The support theorem is not a graph-completion UNSAT certificate. In the two remaining profiles, it only proves v≥29 / v≥31 respectively.

## 6. Imported E408 Q33 high-k and outer-block constraints

The latest ultimate-closure workstream proves under the Q33/d3 contract that at least five B-rows have k_b≥2. At most four B labels can lie outside the no-S K5 components of an exact-129 color, so:

- each exact-129 color has at least one high-k, no-S B-labelled witness;
- if beta=0 or 1, it has at least two;
- each such witness hits at least two S-rows and at least three shell rows in total.

Separately, the outer seven-block E408 analysis proves \(M_C\ge15+P_C\), where M_C counts size-five blocker occurrences and P_C is the outer-block duplicate count. These outer-block constraints are not silently identified with the inner shell labels B. A joint contradiction linking the two systems remains open.

## 7. Cross-branch proof audit: high-multiplicity star lemma

The latest emergency branch's file R12_WITNESS_OVERLAP_STAR_LEMMA.md correctly proves that m witness sets sharing a core vertex x have disjoint remaining triples P_i, that \(\alpha(H[\cup P_i])\le3\), and that \(e(H[\cup P_i])\ge3\binom m2\).

However, its claimed m=10 dichotomy

\[
e(H[U])=135\quad\text{or}\quad e(H[U])\ge144
\]

does not follow from the stated second-Turán step. If e(H[U])≤143, the complement L has at least 292 edges, so Brouwer forces L to be tripartite. The ten disjoint triangles P_i imply its three parts each have size ten, but tripartite does not mean complete tripartite. The valid conclusion is that H[U] consists of three K10s plus g cross-part edges with \(0\le g\le8\). The local configuration “three K10s plus one cross edge whose endpoints lie in different P_i” has e(H[U])=136, all P_i remain independent triples, and \(\alpha(H[U])=3\); hence the inference to g=0 is not justified by the local argument alone.

This identifies a proof gap in that dichotomy, not a counterexample to the full 47-core theorem. The full global degree/excess contract might still exclude g=1,...,8, but that exclusion must be proved separately. This workstream does not use the unsupported dichotomy.

## 8. Next mathematical target

The next target is the boundary kernel, not more scalar incidence sums:

1. For E407, analyze v=29 with 49 linear K4 witnesses, the 284-edge core, and the exact shell-row transversals.
2. For E408 Q33, analyze v=31 with 56 linear K4 witnesses, the zero-excess subfamily, high-k row labels, and the seven-block duplicate system.
3. Charge every core edge and every shell-core edge with explicit multiplicity. Do not sum local witness costs across overlapping sets without a proved multiplicity bound.

EG617(r=12) remains OPEN / NOT_CERTIFIED.
