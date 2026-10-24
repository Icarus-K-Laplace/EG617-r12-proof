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

The \(\delta=16\) boundary is now **excluded** under the frozen core/witness contract. The proof proceeds through:
- \(U\)-parts \(7,7,7,8\);
- exactly five cross edges in \(H[U]\), matching on both sides;
- \(H[W]=K_5\cup K_5\cup K_4\cup K_4\);
- a reverse-saturation lemma: every \(W\)-vertex is complete to exactly one \(U\)-part;
- exclusion of the \((4,1)\) and \((3,2)\) endpoint splits by degree excess;
- exclusion of the final \((5,0)\) split, since three non-endpoint \(D\)-vertices must distribute across two \(K_5\) components, forcing five excess units in one component although the core has only four.

This removes only \(\delta=16\). It does not close templates A–E because \(\delta\le15\) remains possible.

## 4. Template-by-template status

| Template | Existing witness consequence | New result in this line | Status |
|---|---|---|---|
| A | \(\ge28\) hub-complete \(Q\)'s | \(\delta=16\) subcase excluded; lower-\(\delta\) cases remain open | OPEN |
| B | \(\ge28\) hub-complete \(Q\)'s | \(\delta=16\) subcase excluded; lower-\(\delta\) cases remain open | OPEN |
| C | \(\ge35\) hub-complete \(Q\)'s | \(\delta=16\) subcase excluded; lower-\(\delta\) cases remain open | OPEN |
| D | \(\ge35\) hub-complete \(Q\)'s | \(\delta=16\) subcase excluded; lower-\(\delta\) cases remain open | OPEN |
| E, at least one full row | \(\ge35\) hub-complete \(Q\)'s | \(\delta=16\) subcase excluded; lower-\(\delta\) cases remain open | OPEN |
| E, no full row | \(\ge42\) witnesses hitting both \(P_3\) endpoints | \(\delta=16\) subcase excluded; endpoint-row compatibility for lower \(\delta\) remains open | OPEN |

## 5. What is not claimed

- No one of the five templates is closed by this theorem.
- The \(\delta=14,15\) four-partite cases remain open, with the \(W\)-profiles in NON_FOUR_PARTITE_TERMINAL.md.
- The \(\delta\le15\) non-four-partite cases remain open.
- No proof is claimed that the residual incidence design can or cannot be realized.
- E408 Q32/Q33 and the original \(K_{145}\)-to-T61 bridge are outside this line's closure claim.
