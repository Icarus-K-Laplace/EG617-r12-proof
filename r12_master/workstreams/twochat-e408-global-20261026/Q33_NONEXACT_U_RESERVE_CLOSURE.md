# Q33 global closure via the nonexact-color U-edge reserve

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL** under the registered Q33 284-edge / 31-point / 56-witness minimum-support contract, the exact-129 Type-I factor theorem, and the shell-label classification used to distinguish component witnesses from gadget witnesses.  
Headline: the registered E408 Q33 minimum-support terminal is impossible.

This theorem is independent of the Q32 285-edge contract.

## 1. The 31-point U edge floor for every non-target color

Let \(U\subset H\) be the 31-point union of the 56 selected independent four-sets. For every non-target color \(D\), the global coloring hypothesis forbids a \(D\)-independent 13-set. Hence
\[
\alpha(D[U])\le12.
\]
By Turan's theorem applied to the complement, a graph on 31 vertices with independence number at most 12 has at least
\[
p_{12}(31)=\binom{31}{2}-t_{12}(31)
\]
edges. The balanced 12-part partition of 31 has seven parts of size three and five parts of size two, so
\[
p_{12}(31)=7\binom32+5\binom22=21+5=26.
\]
Therefore every non-target color satisfies
\[
\boxed{e_D(U)\ge26.}\tag{1}
\]

## 2. How many U-edges are already owned by selected exact-color components?

Write
\[
L=\overline{H[U]},\qquad e(L)=336+\delta,\qquad \delta\le17.
\]
The 56 selected witnesses are seven from each of eight selected exact-129 colors. Let \(h\) be the number of selected witnesses that lie in the exceptional exact-color gadget rather than in an isolated exact-color \(K_5\) component.

Every selected **component witness** is the four-core-vertex part of an isolated monochromatic \(K_5\). Hence all six edges of its \(K_4\subset L\) have its exact color. Different selected component witnesses have disjoint edge sets: within one exact color their components are disjoint, and across colors an edge has a unique color.

Thus the \(56-h\) selected component witnesses already own exactly
\[
6(56-h)=336-6h
\]
distinct edges of \(L\), all in exact-129 colors.

The remaining edges of \(L\), including all six edges of every gadget witness as a deliberately generous allowance, number at most
\[
(336+\delta)-(336-6h)=\boxed{\delta+6h}.\tag{2}
\]
Every edge of every **nonexact** non-target color on \(U\) must lie in these remaining slots, because it cannot reuse an edge already monochromatic in a selected exact component color.

If \(m\) is the number of exact-129 colors, there are \(11-m\) nonexact non-target colors. Their edge sets are pairwise disjoint. Combining (1) and (2) gives the global necessary inequality
\[
\boxed{26(11-m)\le\delta+6h.}\tag{3}
\]
No edge is charged twice in (3).

## 3. Combine with the independently proved exact-color-count capacity theorem

The sibling result in this same isolated workstream, `Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md`, proves under the same Q33 minimum-support contract that
\[
\boxed{m\ne10}
\]
and hence
\[
\boxed{m\in\{8,9\}}.
\]
Its first W-capacity step already gives the weaker bound \(h\le4\); the later orthogonal-array refinement gives \(h\le3\), but the weaker bound is enough here.

Using only
\[
\delta\le17,\qquad h\le4,
\]
the right side of (3) is at most
\[
\delta+6h\le17+24=41.
\]
But:
- if \(m=9\), the left side is \(26(2)=52>41\);
- if \(m=8\), the left side is \(26(3)=78>41\).

Both possibilities are impossible. Therefore no value \(m\in\{8,9,10\}\) remains.

Hence:
\[
\boxed{\text{the registered Q33 31-point / 56-witness terminal is impossible}.}
\]

## 4. Why this closes more than the P_C=49 screen

The proof does not require a color to satisfy \(P_C=49\). It bypasses the two still-open local all-component-edge-present profiles \((4,4,1^5)\) and \((4,3,2,1^4)\): even if such a profile were locally realizable for one exact color, the **simultaneous existence of the nonexact colors on the same 31-point support** already exceeds the remaining U-edge capacity.

Thus the local P49 profile screen no longer controls the Q33 terminal once the full color system is attached.

## 5. Scope firewall

This theorem is a graph-level contradiction for the registered E408 Q33 minimum-support terminal, not a proof of the original K145 statement by itself. Promotion to a full E408 Q33 closure is valid only to the extent that the upstream E408 reduction has already proved that every Q33 terminal enters this 31-point / 56-witness contract. Promotion to EG617(r=12) additionally requires the original K145-to-E408 reduction and all other E407/E408/Q32/backend branches.

No 285-edge identity, Q32 witness theorem, support-41 theorem, or historical single-external-edge K12 claim is used.