# Q33 cross-color exceptional-gadget intersection theorem

Updated: 2026-10-26  
Status: **PROVED_CONDITIONAL** under the registered exact-129 Type-I factor theorem. This is a global compatibility lemma, not a terminal contradiction.

## 1. Contract

Let \(\mathcal C_0\) be the exact-129 non-target colors, with \(m=|\mathcal C_0|\in\{8,9,10\}\). For each \(C\in\mathcal C_0\), the exact-129 factor theorem partitions the 61-point residual \(R\) into ten isolated \(C\)-colored \(K_5\) components and an 11-vertex exceptional gadget \(U_C\), with
\[
\alpha(C[U_C])\le2.
\]
Let \(G_C=U_C\cap H\) be the gadget's core vertices. Define the full core component support
\[
A_C=H\setminus G_C,
\qquad A=\bigcup_{C\in\mathcal C_0}A_C.
\]
This support includes every core vertex in any isolated component, including vertices from components with more than one shell vertex. It is not the 31-point minimum witness support.

## 2. Pairwise gadget intersection

**Theorem 2.1.** For distinct exact-129 colors \(C,D\),
\[
\boxed{|U_C\cap U_D|\le5.}
\]

**Proof.** Put \(J=U_C\cap U_D\). If \(|J|\ge6\), then \(\alpha(C[J])\le2\), so \(\overline{C[J]}\) is triangle-free. Since the coloring assigns every edge a unique color, \(D[J]\) is a subgraph of \(\overline{C[J]}\); hence \(D[J]\) is triangle-free. But also \(\alpha(D[J])\le2\). Ramsey's theorem \(R(3,3)=6\) says that every graph on six vertices contains a triangle or an independent triple. Thus no graph on \(|J|\ge6\) can be both triangle-free and have independence number at most two. Contradiction. \(\square\)

The proof uses only the exact-129 gadget independence bound and the unique-color property; it does not depend on any P49 profile.

## 3. Common core gadget intersection has size at most two

**Theorem 3.1.** The common core gadget set
\[
W_*=\bigcap_{C\in\mathcal C_0}G_C
\]
satisfies
\[
\boxed{|W_*|\le2.}
\]

**Proof.** Suppose three distinct core vertices \(x,y,z\) lie in every \(G_C\). They then lie in every exceptional gadget \(U_C\). Since \(\alpha(C[U_C])\le2\), at least one of the three edges \(xy,xz,yz\) must have color \(C\), for every exact-129 color \(C\). But each of these three edges has exactly one color, so at most three distinct colors can satisfy that condition. This contradicts \(m\ge8\). \(\square\)

## 4. Global support consequence

Because \(A_C=H\setminus G_C\),
\[
A=\bigcup_C(H\setminus G_C)
=H\setminus\bigcap_CG_C
=H\setminus W_*.
\]
Therefore
\[
\boxed{|A|\ge45.}
\]

This is a support floor for the union of *all core vertices in the ten isolated components* across exact-129 colors. It is stronger than the 31-point minimum support of the six/seven labelled four-set witnesses, but it is a different object.

## 5. Exact limitations

- The result does not say every point of \(A\) belongs to a four-point witness \(Q\subset H\). A component containing multiple shell vertices contributes only a smaller core subset.
- The theorem does not close either remaining P49 all-component-edge-present profile by itself.
- The 41-point omission theorem from the unified witness-capacity workstream cannot be invoked merely from \(|A|\ge45\); its \(U\) is the union of ten four-set witnesses per exact color, not this full component support.
- Q32's 285-edge/excess-six contract is outside the scope of this proof.
