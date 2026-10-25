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

The \(\delta=16\) four-partite boundary is **EXCLUDED** by FOUR_PARTITE_TERMINAL.md:
- \(U\)-parts are \(7,7,7,8\);
- the five cross edges in \(H[U]\) form a matching;
- \(H[W]=K_5\cup K_5\cup K_4\cup K_4\);
- the \((4,1)\) and \((3,2)\) endpoint splits violate the four-unit excess budget;
- in the \((5,0)\) split, the endpoint \(K_4\) is forced complete to \(D\), producing a forbidden \(K_{12}\).

This closes only \(\delta=16\), not E407 Q32 overall. The \(\delta=15\) non-four-partite branch is also excluded under the retained core/witness contract by DELTA15_SECOND_TURAN_PACKING.md.

The entire \(\delta=15\) four-partite branch is now EXCLUDED by DELTA15_FOUR_PARTITE_TERMINAL.md: the final \(K_3\cup K_5^3\) profile forces all three small-part label counts to equal five, so any cross-edge endpoint has a forbidden \(K_{12}\) neighbourhood.


## 3A. Delta-14 cover-capacity result
The proofs DELTA14_EPS0_K4_PROFILE_EXCLUSIONS.md, DELTA14_EPS0_K3K4K5K6_COVER_CAPACITY.md, and DELTA14_EPS0_K3K5K5K5_CROSS_EDGE_CLOSURE.md now exclude all four W profiles in the \(\delta=14,\epsilon_U=0\), four-partite row. The last profile \(K_3\cup K_5^3\) with one W-cross-edge is excluded by a common-neighbour capacity bound of 27, below \(|U|=29\). This remains a common-core structural result; it does not close any of templates A–E.

## 4. Template-by-template status

| Template | Existing witness consequence | New result in this line | Status |
|---|---|---|---|
| A | \(\ge28\) hub-complete \(Q\)'s | \(\delta=16\) excluded; lower-\(\delta\) cases open | OPEN |
| B | \(\ge28\) hub-complete \(Q\)'s | \(\delta=16\) excluded; lower-\(\delta\) cases open | OPEN |
| C | \(\ge35\) hub-complete \(Q\)'s | \(\delta=16\) excluded; lower-\(\delta\) cases open | OPEN |
| D | \(\ge35\) hub-complete \(Q\)'s | \(\delta=16\) excluded; lower-\(\delta\) cases open | OPEN |
| E, at least one full row | \(\ge35\) hub-complete \(Q\)'s | \(\delta=16\) excluded; lower-\(\delta\) cases open | OPEN |
| E, no full row | \(\ge42\) witnesses hitting both \(P_3\) endpoints | \(\delta=16\) excluded; endpoint-row compatibility for lower \(\delta\) remains open | OPEN |

## 5. What is not claimed

- No one of the five templates is closed by this theorem.
- The \(\delta=15\) non-four-partite case is **excluded**: the Kang–Pikhurko equality reduction and incompatible (x,y) degrees into (W) rule out all three base profiles.
- At \(\delta=14,\epsilon_U=0\), all four four-partite W profiles are excluded. At \(\epsilon_U=1\), the no-cross-edge \(K_3\cup K_5^3\) and \(K_4^3\cup K_6\) profiles are excluded by DELTA14_EPS1_K3K5K5K5_NO_CROSS_EDGE.md and DELTA14_EPS1_K4K4K4K6_NO_CROSS_EDGE.md. The \((4,4,5,5)\)+one-cross-edge profile, \(\epsilon_U=2\), and non-four-partite branches remain open. The \(\delta=15\) four-partite branch is excluded.
- The \(\delta\le14\) non-four-partite cases remain open.
- No proof is claimed that the residual incidence design can or cannot be realized.
- E408 Q32/Q33 and the original \(K_{145}\)-to-T61 bridge are outside this line's closure claim.


## 3B. Delta-14, \(\epsilon_U=1\) profile

DELTA14_EPS1_K3K5K5K5_NO_CROSS_EDGE.md excludes the no-cross-edge \(K_3\cup K_5^3\) profile at \(e(H[W])=33\) by a cover bound of 28. This is one profile only; the \((4,4,4,6)\) and \((4,4,5,5)\)+one-cross-edge profiles remain open at this row.


## 3C. Delta-14, \(\epsilon_U=1\), second no-cross-edge profile

DELTA14_EPS1_K4K4K4K6_NO_CROSS_EDGE.md excludes \(H[W]=K_4^3\cup K_6\). Its key invariant is the exact number \(R\) of D-to-W edges outside each D vertex's assigned W-component:
\(R=1-2q+\sum_{d\in D}\epsilon_d\), where \(q\) is the number of D vertices assigned to \(K_6\). This forces every \(K_4\) to receive at most two D assignments, contradicting the need to assign seven or eight D vertices among three \(K_4\) components.
