# E408 exact-129 global blocker contradiction

Date: 2026-10-25  
Status: **PROVED RELATIVE TO THE E408 OUTER-EQUALITY CONTRACT AND THE REGISTERED KANG–PIKHURKO EXACT-129 CLASSIFICATION.**  
Scope: eliminates the entire E408 layer, hence both E408 Q32 and E408 Q33/d3, if the stated parent T61/E408 contracts hold.

## 1. Exact assumptions

Let \(F\) be the 61-vertex target-color graph in an E408 T61 residual from the original balanced 12-coloring of \(K_{145}\). Use only these registered inputs:

1. \(\alpha(F)\le 5\).
2. The E408 outer equality ledger partitions the 145 vertices into seven target \(K_{12}\) blocks \(B_0,\ldots,B_6\) and a residual \(R\), with \(|R|=61\), \(e_F(R)=408\), and no target-color edges between distinct pieces.
3. The least target color has 870 edges. Since \(K_{145}\) has \(10440=12\cdot870\) edges and every color has at least as many edges as the least color, **every color has exactly 870 edges globally**.
4. For every non-target color \(C\), \(\alpha(C)\le12\). Also \(\omega(C)\le5\): a \(C\)-monochromatic \(K_6\) would be a target-independent 6-set in \(F\), contradicting \(\alpha(F)\le5\).
5. For every non-target color \(C\), \(e_C(R)=129+s_C\), with \(s_C\ge0\) and \(\sum_C s_C=3\). Thus at least eight of the eleven non-target colors satisfy \(e_C(R)=129\).
6. For any such exact-129 color, the registered Kang–Pikhurko equality classification, after the contextual clique-cap check, gives \(C[R]\) as ten isolated \(K_5\) components together with an 11-vertex gadget \(U\), where \(\alpha(C[U])=2\) and \(\omega(C[U])=5\). In particular \(\alpha(C[R])=10+2=12\).

The only external extremal input in item 6 is the registered exact-129 equality classification; no unverified Q32/Q33 enumeration is used below.

## 2. Blocker lemma strengthened by the global clique cap

Fix an exact-129 non-target color \(C\) and a vertex \(b\) in any outer block \(B_i\). Set
\[
X_b=N_C(b)\cap R.
\]

Because \(B_i\) is a target \(K_{12}\), it is independent in color \(C\). If some maximum independent 12-set \(I\) of \(C[R]\) avoided \(X_b\), then \(I\cup\{b\}\) would be a \(C\)-independent 13-set. Hence \(X_b\) is a blocker of all maximum independent 12-sets of \(C[R]\).

**Claim.** \(|X_b|\ge6\).

**Proof.** Suppose \(|X_b|\le5\). If \(X_b\) does not contain all five vertices of any isolated \(K_5\) component, then each of the ten isolated components has a vertex outside \(X_b\). If \(U\setminus X_b\) contained an independent pair in \(C[U]\), choose one vertex outside \(X_b\) from each of the ten isolated \(K_5\) components and that independent pair from \(U\). These twelve vertices form an independent 12-set of \(C[R]\) disjoint from \(X_b\), contradicting the blocker property. Thus \(U\setminus X_b\) must be a clique in \(C[U]\), so \(|U\setminus X_b|\le\omega(C[U])=5\), which forces \(|X_b\cap U|\ge6\), impossible.

Therefore any blocker of size at most five must contain an entire isolated \(K_5\) component. At size exactly five, \(X_b\) must equal that component. But then \(b\) is \(C\)-adjacent to all five vertices of that \(C\)-monochromatic \(K_5\), producing a \(C\)-monochromatic \(K_6\). This contradicts \(\omega(C)\le5\). Sizes below five are already ruled out by the first part. Therefore \(|X_b|\ge6\). \(\square\)

This strengthens the previously recorded bound \(e_C(B_i,R)\ge62\): the earlier bound allowed size-five blockers but did not use the full-color condition \(\omega(C)\le5\) on the outside vertex \(b\).

## 3. Global edge-count contradiction

For every outer block \(B_i\), the blocker lemma gives
\[
e_C(B_i,R)=\sum_{b\in B_i}|N_C(b)\cap R|
\ge12\cdot6=72.
\]
Summing over seven blocks,
\[
\sum_{i=0}^6 e_C(B_i,R)\ge7\cdot72=504.
\]

For every pair \(i<j\), each \(b\in B_i\) must have at least one \(C\)-neighbor in \(B_j\). Otherwise \(B_j\cup\{b\}\) would be a \(C\)-independent 13-set, contradicting \(\alpha(C)\le12\). Therefore
\[
e_C(B_i,B_j)\ge12,
\qquad
\sum_{i<j}e_C(B_i,B_j)\ge\binom72\cdot12=252.
\]

There are no \(C\)-edges inside any \(B_i\), because each \(B_i\) is a target-color clique. The edge sets \(E_C(R)\), \(E_C(B_i,R)\), and \(E_C(B_i,B_j)\) are pairwise disjoint. Hence
\[
\begin{aligned}
e_C(K_{145})
&\ge e_C(R)+504+252\\
&=129+504+252\\
&=885.
\end{aligned}
\]
But the E408 outer equality contract forces \(e_C(K_{145})=870\). Since \(885>870\), contradiction.

## 4. Theorem

No E408 T61 residual satisfying the exact outer-equality and exact-129 classification contracts exists. Consequently:

- **E408 Q32 is eliminated** (its core excess-6 contract is irrelevant once the global E408 contract is imposed).
- **E408 Q33/d3 is eliminated** (the beta/X/G_B shell-budget cases need not be enumerated).
- The previous weaker \(R_C\ge7\), \(P_C\le55\) blocker consequence is superseded for exact-129 colors by the stronger per-block bound \(e_C(B_i,R)\ge72\), equivalently \(r_i(C)\ge11\). Across seven blocks this would give \(R_C\ge77\), contradicting \(P_C+R_C=62\).

## 5. Boundaries and dependency audit

- This is not an E407 proof: E407 has target energy 407, so the exact seven-block outer-equality ledger and all-colors-equal-870 conclusion do not automatically apply.
- The proof does not use the V11/V12 finite shell enumeration, the five E407 templates, or the 284/285-edge core excess calculations.
- The exact-129 component classification must retain its stated Kang–Pikhurko equality-classification dependency and contextual clique-cap hypothesis.
- The original K145-to-T61 reduction remains a separate parent-contract obligation. This theorem closes the E408 branch once that branch is legally reached; it does not by itself certify the whole EG617(r=12) theorem.
