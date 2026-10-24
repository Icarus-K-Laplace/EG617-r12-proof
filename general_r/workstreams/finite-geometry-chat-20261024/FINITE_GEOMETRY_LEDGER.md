# Finite-Geometry Ledger

## 1. Brouwer threshold: exact assumptions

The local low-slack theorem uses Brouwer's non-r-partite Turan threshold in the form stated by Popielarz–Sahasrabudhe–Snyder, JCTB 132 (2018), Theorem 2.2:

If n>=2r+1 and H is K_(r+1)-free on n vertices, then

\[
e(H)\ge t_r(n)-\lfloor n/r\rfloor+2
\]

implies H is r-partite.

Reference: https://doi.org/10.1016/j.jctb.2018.04.001. The condition n>=2r+1 is explicit. Here n=q^2 and r=q, so q>=3 suffices. Related extremal characterization: M. Kang and O. Pikhurko, “Maximum K_(r+1)-free graphs which are not r-partite” (2005).

## 2. Exact and near-exact color restrictions

For a q^2-point restriction, m_q=q*C(q,2) is the minimum edge count of a color graph with independence number at most q. If its slack s is at most q-2, the complement crosses Brouwer's threshold and the color graph partitions into q K_q blocks with s cross-block defect edges.

A greedy independent-transversal argument improves the extra-vertex near-line forcing to q-s attachments. In particular, s=0 would force a monochromatic K_(q+1), so every local slack in a genuine counterexample is at least one.

Two positive low-slack colors yield two orthogonal partitions. They do not alone yield a full affine plane, a complete net, or field coordinates.

## 3. Partial Kakeya / line-union inequality

If L_1,...,L_t are q-point sets with |L_a intersect L_b|<=1 for all a != b, then

\[
|\bigcup_a L_a|\ge tq-\binom t2.
\]

This is elementary inclusion-exclusion. It applies to full lines from distinct directions in an affine plane. For t=3 it gives |union|>=3q-3, which exceeds a shell of size 2q-1 for every q>=3.

The key missing premise is not the inequality: it is extraction of three full size-q blocks from distinct directions that the same shell must contain. The current compression theorem gives disjoint independent sets or private witnesses, not such lines.

## 4. Full finite-field Kakeya theorem: scope

A Kakeya set in AG(2,q) over F_q contains a full affine line in every one of the q+1 directions. For odd q, Blokhuis–Mazzocca prove the sharp bound

\[
|K|\ge\frac{q(q+1)}2+\frac{q-1}2.
\]

Reference: A. Blokhuis and F. Mazzocca, “The Finite Field Kakeya Problem,” arXiv:0911.4370. This assumes the Desarguesian affine plane over a finite field and a full line in every direction; it cannot be applied to an arbitrary coloring or to two orthogonal partitions. For even q, the elementary all-direction pair-intersection bound is q(q+1)/2.

The sharp Kakeya theorem is not needed for the present shell calculation: three extracted full directions would already suffice. However, no such extraction has been proved.

## 5. Prime-power warning

The existence of AG(2,q) for prime-power q does not imply that an arbitrary counterexample coloring has its vertices coordinatized by F_q^2. Even a family of mutually orthogonal partitions need not, without additional hypotheses, be the complete Desarguesian affine plane. Polynomial, character-sum, or field-incidence methods must wait until the relevant coordinates and incidence structure are proved.
