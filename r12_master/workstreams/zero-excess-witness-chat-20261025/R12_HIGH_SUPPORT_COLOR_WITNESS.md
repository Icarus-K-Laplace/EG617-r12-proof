# R12 high-support exact-129 witness dichotomy

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** on the retained exact-129 factor theorem and the stated Q32/Q33 shell contracts.  
Purpose: turn the edge floor and the exact Q33 budget into a forced labelled witness, or a repeated-disjoint-witness branch.

## 1. Frozen notation

Let \(F\) be the 61-point T61 residual, with pivot \(p\), shell \(A=S\dot\cup B\), \(|S|=3\), \(|B|=10\), and 47-point core \(H\). Let \(M\) be the missing target graph on \(A\), and for \(b\in B\) write
\[
k_b=d_M(b)=|N_M(b)\cap S|,\qquad 0\le k_b\le3.
\]
The retained shell contracts give \(M[B]=\varnothing\). Put
\[
\mathcal H=\{b\in B:k_b\ge2\},\quad h=|\mathcal H|.
\]
Let \(C\) be an exact-129 non-target color. The retained Kang–Pikhurko factor theorem gives ten isolated \(K_5\) components and an 11-point exceptional gadget \(U_C\) with \(\alpha(C[U_C])=2\).

Because \(B\) is a target clique, it is independent in every non-target color, so \(|B\cap U_C|\le2\). Hence at least eight \(B\)-vertices lie in the ten isolated \(K_5\) components. At most three of those components can contain an \(S\)-vertex. Therefore at least five isolated \(K_5\) components have the form
\[
\{b\}\cup Q,\qquad b\in B,\quad Q\subset H,\quad |Q|=4,
\]
with no \(S\)-vertex. Call these the **no-S components**. Their four-point sets \(Q\) are independent in \(H\) and anticomplete to their label \(b\).

Across different colors, two such \(Q\)-sets intersect in at most one vertex: if they shared two core vertices, their common edge would receive two colors. For a fixed label \(b\), the \(Q\)-sets attached to \(b\) in different colors are actually disjoint, because they also share \(b\), and sharing any additional core vertex would duplicate an edge \(bq\).

## 2. High-label count

Since \(k_b\le1\) off \(\mathcal H\) and \(k_b\le3\) on \(\mathcal H\),
\[
\sum_{b\in B}k_b\le (10-h)+3h=10+2h. \tag{1}
\]

### E407 Q32

Here \(e(M)\ge22\), and the template-specific support contract has \(c_S=e_M(S,B)=e(M)-e(M[S])\).

- Templates A/B have \(e(M[S])=0\), so \(c_S\ge22\), hence \(h\ge6\).
- Templates C/D have \(e(M[S])=1\), so \(c_S\ge21\), hence \(h\ge6\).
- Template E has \(e(M[S])=2\), so \(c_S\ge20\), hence \(h\ge5\).

The inequality \(c_S\le10+2h\) is applied to \(c_S=\sum_b k_b\).

### E408 Q33

The exact budget is
\[
\beta+X+G_B=3,\qquad \beta=e(M[S]),\qquad c_S=e_M(S,B)\ge22-\beta.
\]
Therefore
\[
h\ge\left\lceil\frac{c_S-10}{2}\right\rceil
\ge\left\lceil\frac{12-\beta}{2}\right\rceil.
\]
Thus \(h\ge6\) for \(\beta=0,1\), and \(h\ge5\) for \(\beta=2,3\).

## 3. Hub-forced witness theorem

**Lemma.** If \(h\ge6\), then every exact-129 color has at least one no-S component \(\{b\}\cup Q\) with \(k_b\ge2\).

**Proof.** There are at least five no-S components, and their \(B\)-labels are distinct within one color. If all five labels had \(k_b\le1\), there would be at most \(10-h\le4\) available labels, impossible. \(\square\)

For any such component with \(k_b\ge2\), the four-set \(Q\) must hit every hub in \(N_M(b)\cap S\). Otherwise, if \(s\in N_M(b)\cap S\) is also anticomplete to \(Q\), then \(Q\cup\{b,s\}\) is target-independent of size six, contradicting \(\alpha(F)\le5\). Therefore this \(Q\) hits at least two distinct \(S\)-rows. The universal shell-support lemma also gives at least three distinct shell rows hit by \(Q\).

Consequences:
- E407 Q32 templates A–D: every exact-129 color supplies a no-S independent-four witness hitting at least two hubs.
- E408 Q33 with \(\beta=0,1\): every exact-129 color supplies such a witness.
- E407 template E and E408 Q33 with \(\beta=2,3\): the same conclusion holds whenever \(h\ge6\).

The residual non-target excess is four in E407 Q32, so at least seven colors are exact-129. It is three in E408 Q33, so at least eight colors are exact-129. Hence the first group yields at least seven/eight hub-forced colored witnesses, respectively.

## 4. Exact \(h=5\) boundary dichotomy

The only unresolved high-label count is \(h=5\):
- E407 template E, where \(c_S\ge20\);
- E408 Q33 with \(\beta=2\) or \(3\), where \(c_S\ge20\) or \(19\).

Let \(L=B\setminus\mathcal H\) be the five low labels, each with \(k_b\le1\). In each exact-129 color, select five no-S components, and call that color **low-only** if all five labels are in \(L\). Since \(|L|=5\), a low-only color's selected label set is exactly \(L\).

Let \(c\ge7\) be the number of exact-129 colors in E407 Q32, or \(c\ge8\) in E408 Q33; let \(m\) be the number of low-only colors. Then:

1. Each of the \(c-m\) non-low-only colors supplies a hub-forced no-S witness \(Q\) with \(k_b\ge2\), hence a witness hitting at least two hubs.
2. For every low label \(b\in L\), the \(m\) low-only colors supply \(m\) pairwise vertex-disjoint independent four-sets \(Q_{b,C}\subset H\), each anticomplete to \(b\). Disjointness follows from unique edge ownership because the corresponding \(K_5\) components all contain the same \(b\).
3. Since \(c\ge7\), either \(m\ge4\) or \(c-m\ge4\). Therefore **at least one of the following must hold**:
   - at least four exact-129 colors have a no-S witness forced to hit at least two hubs; or
   - each of the five low labels has at least four pairwise disjoint independent-four witnesses in its core antineighborhood.

For E408 Q33, \(c\ge8\) gives the same four-witness threshold. This dichotomy is exact and does not assume that witnesses from different colors are disjoint unless they share the same \(B\)-label.

## 5. How to use this next

The high-label branch should be combined with the template-specific hub-cover lower bounds in R12_WITNESS_CAPACITY_CROSSCUT.md and the actual 284-edge core adjacency structure. The repeated-disjoint branch should be analyzed as a small residual \(Z=H\setminus\bigcup Q_i\) with each outside vertex adjacent to every selected independent-four set; it must not be discarded merely because the \(Q_i\)'s are disjoint.

This is a new necessary-structure theorem, not a terminal contradiction. E407 Q32 and E408 Q32/Q33 remain OPEN.
