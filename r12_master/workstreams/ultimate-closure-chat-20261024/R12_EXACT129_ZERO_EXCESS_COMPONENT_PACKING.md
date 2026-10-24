# Exact-129 zero-excess component packing — corrected

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** on the retained T61 core contract and exact-129 K5 factor theorem. This file supersedes the withdrawn beta-sensitive draft.

## 1. Contract

Let F be a 61-vertex target residual with shell A=S dot-union B, |S|=3, |B|=10, and 47-vertex core H. Assume alpha(F)<=5, alpha(H)<=4, e(H)=284, and sum_x(d_H(x)-12)=4. For each exact-129 non-target color C, the retained factor theorem gives ten vertex-disjoint isolated K5 components and an 11-vertex exceptional gadget.

## 2. Six B-labelled components per exact-129 color

**Lemma 2.1.** Every exact-129 color has at least seven K5 components avoiding S, and at least six of these have the form {b} union Q, with b in B and Q a four-set in H.

**Proof.** There are only three vertices in S and the ten K5 components are disjoint, so at least seven components avoid S. At most one such component can contain pivot p. A component avoiding both S and p lies in B union H; it contains at most one B vertex because B is a target clique, and it cannot lie entirely in H because alpha(H)<=4. Therefore each component avoiding both S and p is {b} union Q with b in B and |Q|=4. At least six such components exist. Their B labels are distinct, their Q sets are pairwise disjoint within the color, and each Q is independent in H and target-anticomplete to b. QED.

**Important limitation.** The count is six B-labelled components, not seven. The possible seventh component can be {p} union Q, whose Q is independent in H but is not known to be anticomplete to a B row.

## 3. Zero-excess strengthening

Let X={x in H:d_H(x)>12}. Since the total core excess is four, |X|<=4. The six B-labelled Q sets are disjoint within a color, so at most four can meet X. Hence every exact-129 color has at least two B-labelled witnesses Q wholly contained in H_0=H\X, with all four vertices of core degree exactly 12.

The exact residual color totals are 1830-407=1423=11*129+4 and 1830-408=1422=11*129+3. Therefore E407 Q32 has at least seven exact-129 colors and at least 14 zero-excess B-labelled witnesses; E408 Q33 has at least eight exact-129 colors and at least 16 such witnesses.

Within one color these Q sets are disjoint. Across different colors they intersect in at most one vertex, because otherwise their common edge would have two colors.

## 4. Safe hub-complete consequence

If the shell contract has at least one full B row b (k_b=3, so b misses all three hubs), then any B-labelled witness Q that misses a hub must hit the three-element core support of b. The selected Q sets are disjoint within one color, so at most three B-labelled witnesses per exact-129 color can fail to be hub-complete. Since there are at least six B-labelled witnesses, each exact-129 color supplies at least three hub-complete B-labelled witnesses.

Thus, in E407 templates A-D and in template E when it has a full row, the safe global floor is at least 21 hub-complete B-labelled witnesses over the seven guaranteed exact-129 colors.

In template E's no-full-row case, the registered row constraints force all ten B rows to miss the two endpoints of the P3 on S. Every B-labelled Q must hit both endpoints, so the safe global floor is at least 42 endpoint-complete witnesses (six per exact-129 color).

No beta-dependent increase in the number of B-labelled components is claimed. Merely allowing two S vertices to coexist in one non-target K5 does not force them to occupy the same component.
