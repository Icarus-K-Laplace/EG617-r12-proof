# Audit correction: shell-incidence support-union bound with zero-support core vertices

Date: 2026-10-25  
Status: **PROVED CORRECTION** to the imported shell-incidence union argument. The useful qualitative conclusion survives; the numeric floors 11/10 require an extra hypothesis not present in the frozen contract.

## 1. Exact identity versus invalid inequality

For E407 Q32, the shell/core edge count is exact:
\[
e_F(A,H)=32+e(M),\qquad
\sum_{x\in H}(r_A(x)-1)=e(M)-15,
\]
where \(r_A(x)=|N_F(x)\cap A|\).

For \(B'\subseteq B\), with \(D_b=N_F(b)\cap H\),
\[
I(B')-|U(B')|
=\sum_{x\in U(B')}(r_{B'}(x)-1),\qquad
I(B')=\sum_{b\in B'}|D_b|,\quad U(B')=\bigcup_{b\in B'}D_b.
\]
The imported proof bounds this by \(\sum_{x\in H}(r_A(x)-1)\). That comparison is not valid if a vertex outside \(U(B')\) has \(r_A(x)=0\), because its term \(r_A(x)-1=-1\) lowers the full sum. The frozen T61 contract does not, by itself, imply \(r_A(x)\ge1\) for every core vertex: a core vertex with \(d_H(x)\ge13\) may have no shell neighbour while still satisfying \(d_F(x)\ge13\).

## 2. Repair using the four-unit excess budget

Let \(Z=\{x\in H:r_A(x)=0\}\), \(z=|Z|\). Since \(d_F(x)=d_H(x)\ge13\) for \(x\in Z\), each such vertex has \(\epsilon_x=d_H(x)-12\ge1\). The total core excess is four, so \(z\le4\).

Now
\[
\sum_{x:r_A(x)>0}(r_A(x)-1)
=e_F(A,H)-(47-z)
=e(M)-15+z.
\]
For \(x\in U(B')\), \(r_A(x)\ge1\), and \(r_{B'}(x)\le r_A(x)\). Therefore the valid inequality is
\[
I(B')-|U(B')|\le e(M)-15+z.
\]
It follows that
\[
|U(B)|\ge15-\beta-z
\]
and, for \(B_3=\{b:k_b=3\}\) with \(c_{\rm rest}=\sum_{b\notin B_3}k_b\),
\[
|U(B_3)|\ge15-\beta-c_{\rm rest}-z.
\]

Under the retained row-count profiles:
- E407 template A: \(|U(B_3)|\ge15-0-4-4=7\).
- E407 template C: \(|U(B_3)|\ge15-1-4-4=6\).

Thus the qualitative conclusion that the full-row supports cannot all be the same 3-set remains proved. The stronger floors 11 and 10 are not certified without an added lemma establishing \(z=0\).

## 3. Scope and action

- The exact edge identity remains valid.
- The imported proof of the numerical 11/10 floors has a missing nonnegative-term condition; the existing arithmetic assertions alone do not repair it.
- Use 7 and 6 as the safe E407 A/C floors unless a separate argument proves every core vertex has a shell neighbour.
- This correction does not affect the minimum-transversal boundary classification in R12_TRANSVERSAL_BOUNDARY_CLASSIFICATION.md, which does not use the shell-incidence union inequality.
- EG617(r=12) remains OPEN / NOT_CERTIFIED.
