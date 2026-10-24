# Kakeya Bridge Audit

Status: **The geometric lower bounds are valid under their stated hypotheses; those hypotheses have not yet been extracted from a noncompressible EG617 shell.**

## 1. Elementary partial-direction bound

Let L_1,...,L_t be sets of size q such that |L_a intersect L_b|<=1 for every a != b. Then inclusion-exclusion gives

\[
\left|\bigcup_{a=1}^t L_a\right|\ge tq-\binom t2.
\]

If these are full lines from t distinct directions in an affine plane of order q, the pairwise-intersection assumption holds. If a shell X must contain every L_a, then |X| obeys the same lower bound.

For the induction shell |X|=2q-1, three distinct-direction lines already give

\[
|X|\ge3q-3>2q-1\quad(q\ge3).
\]

Thus the minimal useful geometric target is to extract three genuinely distinct directions whose corresponding full lines must all be contained in X. Current J theorems do not provide those lines.

## 2. Full finite-field Kakeya theorem: exact scope

A Kakeya set in AG(2,q) over F_q contains a full affine line in every one of the q+1 directions. The sharp planar bound for odd q due to Blokhuis–Mazzocca is

\[
|K|\ge\frac{q(q+1)}2+\frac{q-1}2.
\]

Published reference: A. Blokhuis and F. Mazzocca, “The finite field Kakeya problem,” in M. Grötschel and G.O.H. Katona (eds.), *Building Bridges: Between Mathematics and Computer Science*, Bolyai Society Mathematical Studies 19, Springer, 2008, pp. 205–218, DOI https://doi.org/10.1007/978-3-540-85221-6_6. Preprint: https://arxiv.org/abs/0911.4370.

This result assumes the Desarguesian affine plane over a finite field and a line in every direction; it does not apply to an arbitrary coloring or merely to two orthogonal partitions. For even q, the elementary all-direction pair-intersection bound gives |K|>=q(q+1)/2.

The odd-q sharp theorem is not needed for the current shell calculation: the elementary three-direction bound is already enough if its line hypotheses can be proved.

## 3. Brouwer threshold used for local coordinatization

The low-slack extraction uses Brouwer's theorem in the following exact regime: n>=2r+1; H is K_(r+1)-free; if

\[
e(H)\ge t_r(n)-\lfloor n/r\rfloor+2,
\]

then H is r-partite.

Reference: J. Popielarz, B. Sahasrabudhe and J. Snyder, “A stability theorem for maximal K_(r+1)-free graphs,” *Journal of Combinatorial Theory, Series B* 132 (2018), Theorem 2.2, https://doi.org/10.1016/j.jctb.2018.04.001. Their statement explicitly assumes n>=2r+1. Here n=q^2 and r=q, so the condition holds for q>=3. Related extremal characterization: M. Kang and O. Pikhurko, “Maximum K_(r+1)-free graphs which are not r-partite” (2005).

## 4. Hypotheses audit

Before invoking the partial Kakeya bound, the proof must establish all of the following:

1. Each extracted block has exactly q vertices.
2. The shell must contain the whole block, not merely intersect it.
3. The selected blocks come from genuinely distinct direction classes.
4. Every pair of selected blocks intersects in at most one point.
5. The block and direction claims hold simultaneously for the same shell X.

J's current packing theorem supplies pairwise disjoint independent sets, not line families satisfying items 2–5. K's current low-slack theorem supplies two orthogonal partitions on W, the vertex set V minus {x}, not a shell containing full blocks in three directions. Therefore no Kakeya or three-line contradiction has yet been applied to the EG617 problem.
