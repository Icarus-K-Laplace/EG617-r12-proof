# Seed-Floor Interface: Finite Geometry to Front Recurrence

Date: 2026-10-24  
Status: **NO DIRECT TRANSFER PROVED; CONTRACT MISMATCH IDENTIFIED.**

## 1. I theorem available

Under the full hypothetical-counterexample coloring contract on \(K_{r^2+1}\), the new local slack-gap theorem gives
\[
s_i(x)=e_i(V\setminus\{x\})-r\binom r2\ge r-1
\quad\text{for every }x,i.
\]
Equivalently, using \(e_i=m_r+r+a_i\),
\[
d_i(x)\le a_i+1.
\]
The proof relies on the full-color property for every \((r+1)\)-set and the low-slack block theorem on a neighborhood restriction of size exactly \(r^2\).

## 2. H seed contract is different

An H state \(J\in\mathcal C_r(a,n)\) is an arbitrary induced residual graph with
\[
|V(J)|=n=ar+O(1),\quad \alpha(J)\le a,\quad \omega(J)\le r-1,
\]
plus the inherited hereditary edge cap. It need not be a full \(r^2\)-vertex color graph \(G_i[V\setminus\{x\}]\), and its target-color independence bound is \(a<r\). The local slack \(s_i(x)\) above is not defined for such a residual in the same way.

Moreover, the low-slack decomposition in I creates monochromatic \(K_r\) blocks, whereas H's \(\omega(J)\le r-1\) explicitly forbids \(K_r\) in the residual target graph. Therefore one cannot simply transplant the I block argument into H.

## 3. What is and is not transferred

- **Transferred as a proved fact about the original full coloring:** every neighborhood-local slack is at least \(r-1\), and \(d_i(x)\le a_i+1\).
- **Not transferred:** no lower bound of the form \(B_r(a,n)\ge p_a(n)+E_a(r)\) follows from this statement alone.
- **Independent H advance:** \(M_r(2)\le2r-1\) and \(M_r(3)\le3r\) are proved for \(r\ge6\) from the inherited cap and the Andrásfai–Erdős–Sós theorem; see H's `LOW_ORDER_CUTOFF_THEOREMS.md`. They do not depend on the I theorem.

## 4. Minimal missing bridge

A valid cross-line seed theorem would need to take the I-side information on the original coloring and derive a constraint on every admissible induced residual, respecting the smaller alpha cap and the forbidden \(K_r\) condition. Until such a theorem is proved, the H seed-floor excesses remain OPEN.