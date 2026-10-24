# Audit correction — attempted E408 exact-129 global blocker contradiction WITHDRAWN

Date: 2026-10-25  
Status: **INVALID ATTEMPT; NOT A THEOREM.** This correction supersedes the initial contents of this file committed as `2d57b3dbed53d51b9e9154afc2654c810950c4e6`.

## 1. The exact error

The attempted argument incorrectly promoted the local bound
\[
\omega(C[R])\le5
\]
to a global bound \(\omega(C)\le5\), by reasoning from \(\alpha(F)\le5\).

Here \(F\) is the 61-vertex T61 residual, and \(R\subseteq V(F)\) is its 61-point vertex set in the E408 outer decomposition. The seven outer target \(K_{12}\) blocks \(B_0,\ldots,B_6\) are **outside** \(F\). Therefore the fact that \(C[R]\) has no \(K_6\) does not prohibit a color-\(C\) \(K_6\) consisting of one outer block vertex \(b\in B_i\) plus a \(K_5\) component in \(R\).

The original counterexample condition only gives \(\alpha(C)\le12\) globally. It permits a color-\(C\) \(K_6\). Thus a blocker neighbourhood \(N_C(b)\cap R\) of size five equal to an isolated \(K_5\) component is **not** ruled out by the T61 residual condition.

The invalid line was:
> “A \(C\)-monochromatic \(K_6\) would be a target-independent 6-set in \(F\), contradicting \(\alpha(F)\le5\).”

That implication applies only when all six vertices lie inside \(F\). It does not apply to an outer vertex \(b\notin V(F)\).

## 2. Consequence

The proposed lower bound
\[
e_C(B_i,R)\ge72
\]
does not follow. The valid registered blocker bound remains
\[
e_C(B_i,R)\ge62,\qquad r_i(C)\ge1,
\]
because at most ten vertices of \(B_i\) can use distinct size-five K5-component blockers, while at least two must have blocker size at least six.

Accordingly, the derived bounds \(R_C\ge77\), \(e_C(K_{145})\ge885\), and the claimed elimination of E408 Q32/Q33 are **withdrawn**. No E408 terminal has been closed by this attempt.

## 3. What remains valid

- The exact-129 classification of \(C[R]\) as ten isolated K5 components plus the 11-vertex exceptional gadget remains valid under its registered Kang–Pikhurko equality-classification and contextual clique-cap assumptions.
- A maximum independent 12-set of \(C[R]\) must be hit by \(N_C(b)\cap R\) for every outer vertex \(b\), because otherwise it plus \(b\) is a global \(C\)-independent 13-set.
- A blocker has size at least five; size five forces it to be exactly one isolated K5 component.
- The seven-block duplicate budget \(P_C+R_C+s_C=62\), the bound \(R_C\ge7\), and \(P_C\le55\) for exact-129 colors remain the valid registered conclusions.
- E408 Q32/Q33 remain OPEN. The next useful theorem must use the global \(\alpha(C)\le12\) condition correctly and must not infer a global \(\omega(C)\le5\).
