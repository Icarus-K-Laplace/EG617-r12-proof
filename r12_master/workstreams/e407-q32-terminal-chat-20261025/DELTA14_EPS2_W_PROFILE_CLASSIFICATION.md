# Exact W-profile classification and exclusion for \(\delta=14,\epsilon_U=2\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 284-edge/core contract and Turán's theorem with its equality characterization.

## 1. The W-profile is forced by Turán equality

At \(\delta=14\), the four-partite U-complement contract gives \(e(H[U])=98\), and the exact degree ledger gives
\[
e(H[W])=32-\epsilon_U+2=32
\]
when \(\epsilon_U=2\). Equivalently, the W-side excess is \(E_W=4-\epsilon_U=2\).

Since \(\alpha(H[W])\le4\), the complement \(G=\overline{H[W]}\) is \(K_5\)-free. Turán's theorem gives
\[
e(H[W])\ge \binom{18}{2}-t_4(18)=153-121=32.
\]
Equality holds. By the equality characterization of Turán's theorem, \(G=T_4(18)\), with part sizes \(4,4,5,5\). Therefore
\[
\boxed{H[W]=K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5}
\]
with no W-cross-edges. There is no other W-profile in this row.

## 2. The forced profile is excluded by the common-neighbour capacity theorem

The retained proof in DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md, Section 5, applies to exactly this profile and \(\epsilon_U=2\). Its hypotheses match the present contract: \(|U|=29\), four U-parts \(7,7,7,8\), seven distinct small-side U-cross-edge endpoints, \(\alpha(H)\le4\), \(\omega(H)\le11\), and total core excess four.

For completeness, its capacity conclusion is
\[
|S_{4,1}|,|S_{4,2}|\le9,\qquad
|S_{5,1}|\le2+E_{5,1},\quad |S_{5,2}|\le2+E_{5,2},
\]
where \(E_{5,1}+E_{5,2}\le E_W=2\). Since the four anticomplete W-components force the four common-neighbour sets to cover \(U\),
\[
29\le\sum_s|S_s|
\le9+9+(2+E_{5,1})+(2+E_{5,2})
\le24,
\]
a contradiction.

Therefore the entire \(\delta=14,\epsilon_U=2\), four-partite branch is **EXCLUDED** under the retained contracts. This conclusion uses Turán's equality characterization to certify the unique W-profile, and the explicit common-neighbour capacity proof in the cited workstream file to exclude it.
