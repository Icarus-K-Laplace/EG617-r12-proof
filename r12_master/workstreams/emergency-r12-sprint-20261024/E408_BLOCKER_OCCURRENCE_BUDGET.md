# E408 exact-129 blocker-occurrence budget

Date: 2026-10-25  
Status: **PROVED NECESSARY-CONDITION REFINEMENT; DOES NOT CLOSE E408.**

## 1. Contract

Use the E408 global seven-block equality system and the registered exact-129 blocker theorem:

- \(K_{145}=B_0\dot\cup\cdots\dot\cup B_6\dot\cup R\), with seven target \(K_{12}\) blocks, \(|R|=61\);
- every color has exactly 870 edges globally;
- for each non-target color \(C\), \(e_C(R)=129+s_C\), \(\sum_Cs_C=3\);
- for each exact-129 color \(C\), every outer vertex \(b\in B_i\) has blocker \(X_b=N_C(b)\cap R\); \(|X_b|\ge5\), and \(|X_b|=5\) iff \(X_b\) is one of the ten isolated \(K_5\) components of \(C[R]\);
- \(P_C+R_C+s_C=62\), where \(P_C\) counts block-block duplicates and \(R_C=\sum_i r_i(C)\), with \(e_C(B_i,R)=61+r_i(C)\).

There are \(m\in\{8,9,10\}\) exact-129 colors.

## 2. Theorem — blocker occurrence versus duplicate budget

For an exact-129 color \(C\), define
\[
m_i(C)=|\{b\in B_i:|N_C(b)\cap R|=5\}|,
\qquad
M_C=\sum_{i=0}^6m_i(C).
\]

Then
\[
\boxed{M_C\ge 15+P_C.}
\]

**Proof.** In block \(B_i\), the \(m_i(C)\) size-five blockers each contribute five C-edges to R. Each of the other \(12-m_i(C)\) blocker neighborhoods has size at least six. Thus
\[
e_C(B_i,R)\ge5m_i(C)+6(12-m_i(C))=72-m_i(C).
\]
Summing over the seven blocks,
\[
427+R_C=e_C\Big(\bigcup_i B_i,R\Big)\ge504-M_C,
\]
so \(R_C\ge77-M_C\). Since \(s_C=0\) and \(P_C+R_C=62\), we have \(R_C=62-P_C\). Therefore
\[
62-P_C\ge77-M_C,
\]
which rearranges to \(M_C\ge15+P_C\). \(\square\)

## 3. Cross-color aggregate consequence

Since \(\sum_C P_C=252\), and the \(11-m\) nonexact colors satisfy
\[
\sum_{C:s_C>0}P_C\le\sum_{C:s_C>0}(62-s_C)=62(11-m)-3,
\]
the exact-129 colors satisfy
\[
\sum_{C:s_C=0}P_C\ge62m-427.
\]
Consequently,
\[
\boxed{\sum_{C:s_C=0}M_C\ge77m-427.}
\]

The three possible cases give:

| Number \(m\) of exact-129 colors | Lower bound on total \(P_C\) over exact colors | Lower bound on total size-five blocker occurrences |
|---:|---:|---:|
| 8 | 69 | 189 |
| 9 | 131 | 266 |
| 10 | 193 | 343 |

For each exact-129 color, \(M_C\le70\), since each of seven blocks has at most ten size-five blockers. These bounds are internally consistent; they do not by themselves contradict E408.

## 4. Structural meaning and open interface

A size-five blocker is a complete isolated \(K_5\) component of \(C[R]\). Thus \(M_C\) counts the number of block/component incidences across the seven outer blocks. The inequality says that a color using many duplicate edges among outer blocks must also reuse many isolated \(K_5\) components as blockers across the seven blocks.

At the endpoint \(P_C=55\), the inequality forces \(M_C\ge70\), and the per-block cap gives \(M_C=70\): every one of the ten isolated \(K_5\) components is a size-five blocker for exactly one vertex in every outer block. This is an exact equality consequence, not a contradiction.

The next step would have to show that the resulting cross-block incidence system cannot simultaneously realize the required \(P_C\) duplicate edges for all colors and the shell/core witness constraints. No such incompatibility is proved here.
