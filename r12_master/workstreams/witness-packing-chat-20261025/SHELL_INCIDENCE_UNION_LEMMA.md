# Shell-incidence union lemma for E407 Q32 — audited correction

Date: 2026-10-25  
Status: **Exact identity PROVED; corrected union bounds PROVED under the retained V12 row contract.** The stronger numerical floors 11/10 in the earlier draft are withdrawn unless a separate theorem proves that every core vertex has a shell neighbour.

## 1. Exact shell/core incidence identity

Let F be the 61-vertex E407 Q32 residual, with pivot p, shell A=N_F(p), |A|=13, core H of size 47, e(F)=407, and e(H)=284. The shell/core edge identity gives

\[
e(F)=13+e(F[A])+e(A,H)+e(H)
=13+(78-e(M))+e(A,H)+284,
\]
where M is the missing-edge graph on A. Therefore
\[
\boxed{e(A,H)=32+e(M).}
\]
For \(r_A(x)=|N_F(x)\cap A|\),
\[
\boxed{\sum_{x\in H}(r_A(x)-1)=e(A,H)-47=e(M)-15.} \tag{1}
\]

For \(b\in B=A\setminus S\), put \(D_b=N_F(b)\cap H\). For \(B'\subseteq B\), let
\[
I(B')=\sum_{b\in B'}|D_b|,\qquad U(B')=\bigcup_{b\in B'}D_b.
\]
Then
\[
I(B')-|U(B')|
=\sum_{x\in U(B')}(r_{B'}(x)-1),\qquad
r_{B'}(x)=|N_F(x)\cap B'|.
\]

## 2. The missing nonnegative-term condition

The earlier draft compared the support-restricted sum above directly to the full sum in (1). That comparison is not valid if some \(x\notin U(B')\) has \(r_A(x)=0\), because such a vertex contributes \(-1\) to (1).

The frozen T61 contract does not imply \(r_A(x)\ge1\) for every x in H: a core vertex with no shell neighbour can still have \(d_H(x)\ge13\). Define
\[
Z=\{x\in H:r_A(x)=0\},\qquad z=|Z|.
\]
For \(x\in Z\), \(d_F(x)=d_H(x)\ge13\), so \(\epsilon_x=d_H(x)-12\ge1\). The total core excess is four; hence
\[
0\le z\le4.
\]

Now
\[
\sum_{x:r_A(x)>0}(r_A(x)-1)
=e(A,H)-(47-z)=e(M)-15+z.
\]
For \(x\in U(B')\), \(r_A(x)\ge1\) and \(r_{B'}(x)\le r_A(x)\). Thus the valid comparison is
\[
I(B')-|U(B')|\le e(M)-15+z. \tag{2}
\]
Consequently
\[
\boxed{|U(B)|\ge15-\beta-z}
\]
and, for \(B_3=\{b\in B:k_b=3\}\) with \(c_{\rm rest}=\sum_{b\notin B_3}k_b\),
\[
\boxed{|U(B_3)|\ge15-\beta-c_{\rm rest}-z}.
\]

## 3. Safe template A/C conclusions

Under the retained V12 row-count contract:
- Template A: \(\beta=0\), \(c_{\rm rest}=n_1\le4\), so \(|U(B_3)|\ge11-z\ge7\).
- Template C: \(\beta=1\), \(c_{\rm rest}=n_1\le4\), so \(|U(B_3)|\ge10-z\ge6\).

Both lower bounds exceed three, so the full-row supports cannot all be the same three core vertices. The stronger floors 11 and 10 are not certified without a separate proof that \(z=0\).

## 4. Scope

The exact edge identity and corrected union inequalities are valid. This lemma does not classify partial overlaps among full-row supports and does not close any of the five E407 Q32 templates. The independent transversal-boundary theorem and the new E408 Q33 \(S_0\ge11\) theorem do not rely on the invalid comparison. EG617(r=12) remains OPEN / NOT_CERTIFIED.
