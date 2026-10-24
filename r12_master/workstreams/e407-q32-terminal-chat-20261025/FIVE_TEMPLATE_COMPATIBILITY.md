# E407 Q32 — five-template / common-core compatibility

Date: 2026-10-25  
Status: **OPEN**. The five \(\rho=0\) templates have not been eliminated.

## 1. Frozen common-core contract

All five V12 templates A–E are tested against the same hypothetical 47-vertex core \(H\):
\[
e(H)=284,\quad \delta(H)\ge12,\quad \alpha(H)\le4,\quad
\sum_{x\in H}(d_H(x)-12)=4.
\]
The seven exact-129 colors in the residual edge profile \(129^7,130^4\) give 49 linear independent 4-sets \(Q\), seven per exact-129 color. The witness support boundary under review is \(|U|=29, |W|=18\). The exact ledger is
\[
e(H[U])=112-\delta,\quad e_H(U,W)=124+\epsilon_U+2\delta,\quad
e(H[W])=48-\epsilon_U-\delta.
\]
The independently checked transversal/excess inequality is
\[
\epsilon_U+2\delta\ge9,\quad \delta+\epsilon_U\le16,
\]
so \(\delta\ge3\). This is conditional on the retained T61 reduction and exact-129 Kang–Pikhurko equality contract.

## 2. What the latest sibling work actually supplies

The emergency-sprint branch at f4c3b06891d29238d4f9cca2588f442004b6dc97 proves the stronger E407 transversal/excess bound \(\epsilon_U+2\delta\ge9\), hence \(\delta\ge3\), without assuming four-partiteness.

The ultimate-closure branch at 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 contains the exact-129 color-factor crosscut. Under its template contracts, it gives:
- A/B: at least 28 hub-complete independent 4-sets across the seven exact-129 colors;
- C/D: at least 35 hub-complete independent 4-sets;
- E with at least one full B-row: at least 35 hub-complete sets;
- E with no full B-row: at least 42 independent 4-sets hitting both endpoints of the \(P_3\).

The witness-packing branch at f5d3daa07403877ede9885e1bd5c2f46b16d81da confirms the union-size boundary and explicitly warns that the high-multiplicity witness-star dichotomy is not proved by its stated second-Turán step. This workstream does not use that unsupported dichotomy.

## 3. New common-core restriction

The new conditional theorem in FOUR_PARTITE_TERMINAL.md proves that \(\delta=16\) is automatically four-partite, and forces the exact structure:
- \(U\)-parts \(7,7,7,8\);
- exactly five cross edges in \(H[U]\), forming a matching from the 8-part to the three 7-parts;
- \(H[W]=K_5\cup K_5\cup K_4\cup K_4\);
- all five 8-part endpoints have the same \(K_4\) as their exact \(W\)-neighbourhood;
- that \(K_4\) is complete to the 8-part; every vertex in the remaining \(K_4,K_5,K_5\) components is complete to a 7-part. Labels may vary vertex-by-vertex, and a component-wide bijection is not proved.

This reduces the extreme \(\delta=16\) case to a specific labelled incidence kernel. It does not yet show the kernel conflicts with any one of templates A–E.

## 4. Template-by-template status

| Template | Existing witness consequence | New result in this line | Status |
|---|---|---|---|
| A | \(\ge28\) hub-complete \(Q\)'s | Applies the common-core \(\delta=16\) structural kernel; no row contradiction yet | OPEN |
| B | \(\ge28\) hub-complete \(Q\)'s | Same | OPEN |
| C | \(\ge35\) hub-complete \(Q\)'s | Same | OPEN |
| D | \(\ge35\) hub-complete \(Q\)'s | Same | OPEN |
| E, at least one full row | \(\ge35\) hub-complete \(Q\)'s | Same | OPEN |
| E, no full row | \(\ge42\) witnesses hitting both \(P_3\) endpoints | Same core kernel; endpoint-row compatibility not yet tested | OPEN |

## 5. What is not claimed

- No one of the five templates is closed by this theorem.
- The \(\delta=14,15\) four-partite cases remain open, with the \(W\)-profiles in NON_FOUR_PARTITE_TERMINAL.md.
- The \(\delta\le15\) non-four-partite cases remain open.
- No proof is claimed that the residual incidence design can or cannot be realized.
- E408 Q32/Q33 and the original \(K_{145}\)-to-T61 bridge are outside this line's closure claim.
