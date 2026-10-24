# E408 exact-129 blocker-occurrence budget

Date: 2026-10-25  
Status: **PROVED NECESSARY-CONDITION REFINEMENT; DOES NOT CLOSE E408.**

## 1. Contract and notation

Use the E408 global seven-block equality system:
\[
K_{145}=B_0\dot\cup\cdots\dot\cup B_6\dot\cup R,
\qquad |B_i|=12,\quad |R|=61.
\]
Each \(B_i\) is a target-color \(K_{12}\), distinct pieces are target-anticomplete, every color has 870 edges globally, and
\[
e_C(R)=129+s_C,\quad s_C\ge0,\quad \sum_Cs_C=3.
\]
Thus \(m\in\{8,9,10\}\) of the eleven non-target colors are exact-129 colors.

For an exact-129 color \(C\), the registered blocker theorem says \(X_b=N_C(b)\cap R\) hits every maximum independent 12-set of \(C[R]\), \(|X_b|\ge5\), and \(|X_b|=5\) iff it is one of the ten isolated \(K_5\) components of \(C[R]\). Define
\[
m_i(C)=|\{b\in B_i:|N_C(b)\cap R|=5\}|,\qquad
M_C=\sum_{i=0}^6m_i(C).
\]
The global duplicate identity is \(P_C+R_C+s_C=62\), with \(P_C,R_C\ge0\), and
\[
e_C(B_i,R)=61+r_i(C),\qquad R_C=\sum_i r_i(C).
\]

## 2. Theorem

For every exact-129 color \(C\),
\[
\boxed{M_C\ge15+P_C.}
\]

**Proof.** In each outer block \(B_i\), the \(m_i(C)\) size-five blockers contribute five C-edges each into R; the other \(12-m_i(C)\) blocker neighborhoods have size at least six. Hence
\[
e_C(B_i,R)\ge5m_i(C)+6(12-m_i(C))=72-m_i(C).
\]
Summing over the seven blocks,
\[
427+R_C=e_C\Big(\bigcup_iB_i,R\Big)\ge504-M_C,
\]
so \(R_C\ge77-M_C\). For an exact-129 color, \(s_C=0\), so \(R_C=62-P_C\). Therefore \(62-P_C\ge77-M_C\), proving \(M_C\ge15+P_C\). \(\square\)

## 3. Aggregate consequence

The global duplicate budget gives \(\sum_C P_C=252\). For the \(11-m\) nonexact colors,
\[
\sum_{s_C>0}P_C\le62(11-m)-3,
\]
so
\[
\sum_{s_C=0}P_C\ge62m-427.
\]
Summing the theorem,
\[
\boxed{\sum_{s_C=0}M_C\ge77m-427.}
\]

| Exact-129 colors \(m\) | \(\sum_{s_C=0}P_C\) lower bound | \(\sum_{s_C=0}M_C\) lower bound |
|---:|---:|---:|
| 8 | 69 | 189 |
| 9 | 131 | 266 |
| 10 | 193 | 343 |

Since \(M_C\le70\), the inequalities are consistent and do not close E408. At \(P_C=55\), they force \(M_C=70\): every one of the ten isolated \(K_5\) components is used as a size-five blocker exactly once in every outer block.

## 4. Interpretation and limitations

This couples the number of isolated-component blocker occurrences to the number of duplicate C-edges between outer blocks. It is a stronger interface than \(R_C\ge7\) and \(P_C\le55\), but it does not imply that a component must occur in all seven blocks, nor does it contradict the seven-block near-Latin system.

This theorem concerns the **seven outer \(K_{12}\) blocks**. It is distinct from the inner shell split \(A=S\dot\cup B\) used in the T61 witness-packing theorem. Keep those two uses of B separate.

The E408 exact-129 global contradiction attempt was withdrawn: \(\omega(C[R])\le5\) does not imply \(\omega(C)\le5\) for outer vertices outside R. Do not use the invalid \(e_C(B_i,R)\ge72\) or 885-edge lower bound.
