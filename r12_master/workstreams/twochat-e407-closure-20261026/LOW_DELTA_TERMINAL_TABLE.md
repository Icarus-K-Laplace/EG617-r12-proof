# E407 Q32 — exact delta / U-excess terminal table

Date: 2026-10-26  
Status: **Finite budget table verified; graph terminals remain OPEN where listed.**

## 1. Exact formulas

Let \(L_U=\overline{H[U]}\) and \(\delta=e(L_U)-294\). The 49 linear independent 4-sets use 294 distinct pairs of \(L_U\). The exact core ledger is
\[
e(H[U])=112-\delta,\quad e(H[W])=48-\epsilon_U-\delta,\quad
e_H(U,W)=124+\epsilon_U+2\delta.
\]
The 18-vertex W graph has \(\alpha(H[W])\le4\), hence \(e(H[W])\ge32\) by Turán's theorem. Consequently \(\delta+\epsilon_U\le16\). The independently established E407 transversal/excess theorem gives \(\epsilon_U+2\delta\ge9\), and \(\delta\ge3\). Together with \(0\le\epsilon_U\le4\), the exact integer possibilities are:

| \(\delta\) | Feasible \(\epsilon_U\) | \(e(H[U])\) | \(e(H[W])\) | \(e_H(U,W)\) |
|---:|---|---:|---:|---:|
| 3 | 3, 4 | 109 | 42, 41 | 133, 134 |
| 4 | 1, 2, 3, 4 | 108 | 43, 42, 41, 40 | 133, 134, 135, 136 |
| 5 | 0–4 | 107 | 43–39 | 134–138 |
| 6 | 0–4 | 106 | 42–38 | 136–140 |
| 7 | 0–4 | 105 | 41–37 | 138–142 |
| 8 | 0–4 | 104 | 40–36 | 140–144 |
| 9 | 0–4 | 103 | 39–35 | 142–146 |
| 10 | 0–4 | 102 | 38–34 | 144–148 |
| 11 | 0–4 | 101 | 37–33 | 146–150 |
| 12 | 0–4 | 100 | 36–32 | 148–152 |
| 13 | 0–3 | 99 | 35–32 | 150–153 |
| 14 | 0–2 | 98 | 34–32 | 152–154 |
| 15 | 0–1 | 97 | 33–32 | 154–155 |
| 16 | 0 | 96 | 32 | 156 |

For rows with a range, the endpoints follow increasing \(\epsilon_U\); the verifier checks every individual integer pair, not just the displayed interval.

## 2. Current terminal status table

All entries below retain the E407 Q32 parent/core/witness contract. “Conditional” records dependence on the named extremal theorem or reduction; it does not mean unconditional certification.

| \(\delta\) and branch | Current status | Exact remaining issue |
|---|---|---|
| 16 | EXCLUDED | \(e(L_U)=310\) forces four-partiteness by Brouwer; the 7,7,7,8 endpoint kernel yields \(K_{12}\). |
| 15, four-partite \(L_U\) | EXCLUDED | W-profile saturation plus the final \(K_3\cup K_5^3\) endpoint argument. |
| 15, non-four-partite \(L_U\) | EXCLUDED UNDER KP | Uses the Kang–Pikhurko non-four-partite second-Turán equality classification. |
| 14, four-partite \(L_U\), \(\epsilon_U=0,1,2\) | EXCLUDED | All W profiles in each exact row have proof files; \(\epsilon_U=1\) profile exhaustiveness uses Brouwer, \(\epsilon_U=2\) uses Turán equality. |
| 14, non-four-partite \(L_U\), augmentable nonedge | EXCLUDED UNDER KP/BROUWER | Augmentable-edge reduction and common-neighbour closure. |
| 14, non-four-partite \(L_U\), \(K_5\)-saturated | PROVED_CONDITIONAL | Depends on alpha-critical reduction and Didin 2026 preprint component-count theorem, not independently audited here. |
| 13, four-partite \(L_U\), \(\epsilon_U=1\) | EXCLUDED | No-cross profiles and all three W-cross-edge profiles are closed by DELTA13 files, including Round 31. |
| 13, four-partite \(L_U\), \(\epsilon_U=2\) | EXCLUDED under stated profile contract | No-cross profiles and the one-cross-edge profile are excluded in Round 4. |
| 13, four-partite \(L_U\), \(\epsilon_U=3\) | EXCLUDED | Exact W edge count 32 forces \(2K_4\cup2K_5\) with no cross-edge, excluded by the no-cross theorem. |
| 13, four-partite \(L_U\), \(\epsilon_U=0\) | OPEN | W edge count 35; no exhaustive W-profile closure in the current files. |
| 13, non-four-partite \(L_U\) | OPEN | \(e(L_U)=307\) does not force four-partiteness; no complete non-four-partite classification is closed. |
| \(\delta\le12\) | OPEN | The \(\delta=13\) classifications do not transfer. Exact budget rows are listed above. |
| Five shell templates A–E, any surviving row | OPEN | Need one common labelled incidence proof tying shell rows, 49 support blocks, exact-129 component labels, and the same H. |
| Original K145-to-T61 bridge | OPEN / NOT_CERTIFIED | Parent recurrence and its lower-order dependencies are not certified end-to-end here. |

## 3. Important contract distinction

The \(\delta\)-classification above concerns the 29-point support graph \(L_U=\overline{H[U]}\). The five templates A–E concern the *different* 13-vertex shell missing graph \(M=\overline{F[A]}\). Do not conflate these two complement graphs or infer that closing a W clique profile closes a shell template.

Likewise, excluding a local \(H[W]\) profile under the four-partite \(L_U\) assumption does not exclude a non-four-partite \(L_U\) realization unless a separate theorem forces four-partiteness at that \(\delta\).
