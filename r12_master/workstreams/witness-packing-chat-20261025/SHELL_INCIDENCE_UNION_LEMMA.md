# Shell-incidence union lemma for E407 Q32

Date: 2026-10-25  
Status: **PROVED under the retained E407 Q32/T61 contract.** This is a support-size theorem, not a terminal exclusion.

## 1. Contract and exact edge identity

Let F be the 61-vertex E407 Q32 residual, with pivot p, shell A=N_F(p) of size 13, core H of size 47, e(F)=407, and e(H)=284. Let M be the missing-edge graph on A. The shell/core edge identity gives

\[
e(F)=13+e(F[A])+e(A,H)+e(H)
=13+(78-e(M))+e(A,H)+284.
\]

Therefore

\[
\boxed{e(A,H)=32+e(M).}
\]

Every x in H has d_H(x)>=12 and d_F(x)>=13, so x has at least one target neighbour in A. Put r_A(x)=|N_F(x) intersect A|. Then

\[
\sum_{x\in H}(r_A(x)-1)=e(A,H)-47=e(M)-15. \tag{1}
\]

This is the exact total duplicate shell-incidence budget on the 47 core vertices. It is not a budget on core edges.

For a in A, write D_a=N_F(a) intersect H. For B=A\S, the retained E407 Q32 contract has M[B] empty and |D_b|=k_b=d_M(b) in {0,1,2,3}. Let beta=e(M[S]) and B' be any subset of B. Define

\[
I(B')=\sum_{b\in B'}|D_b|,\qquad U(B')=\bigcup_{b\in B'}D_b.
\]

Since the number of B'-incidences at x is at most r_A(x),

\[
I(B')-|U(B')|
=\sum_{x:\,r_{B'}(x)>0}(r_{B'}(x)-1)
\le\sum_{x\in H}(r_A(x)-1)=e(M)-15. \tag{2}
\]

## 2. Theorem: row-support union lower bounds

**Theorem 2.1.** Under the contract above:

1. The union of all B-row core supports satisfies
   \[
   \boxed{|U(B)|\ge15-\beta.}
   \]
2. Let B_3={b in B:k_b=3}, n_3=|B_3|, and c_rest=sum over b not in B_3 of k_b. Then
   \[
   \boxed{|U(B_3)|\ge15-\beta-c_{\rm rest}.}
   \]

**Proof.** Because M[B] is empty, every edge of M is either an S-S edge or an S-B edge, so
\[
I(B)=\sum_{b\in B}k_b=e(M)-\beta.
\]
Applying (2) gives
\[
|U(B)|\ge e(M)-\beta-(e(M)-15)=15-\beta.
\]
For B_3, I(B_3)=3n_3 and e(M)=\beta+3n_3+c_rest. Substitution in (2) gives
\[
|U(B_3)|\ge3n_3-(e(M)-15)=15-\beta-c_{\rm rest}.
\]
∎

## 3. Consequences for E407 Q32 templates A and C

The retained V12 row-count contract gives:

- Template A: M[S] is empty, the B row types are 0,1,3, and n_1<=4.
- Template C: M[S] has one edge, the B row types are 0,1,3, and n_1<=4.

Thus:

- **Template A:** beta=0 and c_rest=n_1, so the union of all full (k_b=3) row supports has size at least 15-n_1>=11.
- **Template C:** beta=1 and c_rest=n_1, so the union of all full row supports has size at least 14-n_1>=10.

Both templates have n_3>=6. In particular, the full-row supports cannot all be the same 3-set. This conclusion follows from the exact global shell-incidence budget, not from an assumption that the supports are disjoint.

The bounds are tight at the level of the arithmetic ledger: Template A allows n_1=4, giving floor 11; Template C allows n_1=4, giving floor 10. The theorem does not yet classify all overlap patterns among the 3-sets.

## 4. Why this matters for the boundary attack

Every full B row b with k_b=3 is missing to all three hubs in S. The row-transversal theorem says D_b is a 3-vertex transversal of the maximum independent 4-sets in each corresponding hub core H_a. The union bounds above now say that at least 11 distinct core vertices occur among the full-row supports in A, and at least 10 in C.

This rules out the extreme “all full rows reuse the same three core vertices” escape. It does not yet rule out partial overlaps, nor does it close any of the five E407 Q32 templates.

Dependencies: the retained V12 template/count contract; the legal T61 shell/core edge identity; delta(F)>=13 and delta(H)>=12. The finite row-count enumeration remains conditional on its registered lower-order seed contracts.
