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

Published reference: A. Blokhuis and F. Mazzocca, “The finite field Kakeya problem,” in M. Grötschel and G.O.H. Katona (eds.), *Building Bridges: Between Mathematics and Computer Science*, Bolyai Society Mathematical Studies 19, Springer, 2008, pp. 205–218, DOI https://doi.org/10.1007/978-3-540-85221-6_6. Preprint: https://arxiv.org/abs/0911.4370. For even q, the elementary all-direction pair-intersection bound is q(q+1)/2.

The sharp Kakeya theorem assumes the Desarguesian affine plane over a finite field and a full line in every direction; it cannot be applied to an arbitrary coloring or to two orthogonal partitions. The sharp bound is not needed for the present shell calculation: three extracted full directions would already suffice. However, no such extraction has been proved.

## 5. Prime-power warning

The existence of AG(2,q) for prime-power q does not imply that an arbitrary counterexample coloring has its vertices coordinatized by F_q^2. Even a family of mutually orthogonal partitions need not, without additional hypotheses, be the complete Desarguesian affine plane. Polynomial, character-sum, or field-incidence methods must wait until the relevant coordinates and incidence structure are proved.


## 4. Residual multinet interface from J

Source: J branch workstream/general-r-induction-compression-20261024, commit 009a546cf0d66e4060a601bba168674214e7ac6c, file ALIGNMENT_FREE_WITNESS_RIGIDITY.md, Theorems J.W1/J.W5.

Under the tight-transversal Case B contract, q=r-1 and R=V minus X have |R|=q²; for q colors i!=c, alpha(G_i[R])<=q and residual excesses b_i satisfy sum b_i<=C(q,2). At least ceil(q/2) colors have b_i<=q-2. Brouwer's threshold gives q-clique partitions for those colors; any two are orthogonal, giving a q-net with at least ceil(q/2) directions. This is a conditional consequence of J's graph-level theorem, not a claim that arbitrary colorings have such nets.

The t-net gives N(q)>=t-2>=ceil(q/2)-2 mutually orthogonal Latin squares. For q=10 (the r=11 Case B), it would imply three MOLS(10). Current source audit: Bright, Keita, and Stevens, “Myrvold's Results on Orthogonal Triples of 10 x 10 Latin Squares: A SAT Investigation,” Electronic Journal of Combinatorics 33(1) (2026), P1.30, DOI [10.37236/13960](https://doi.org/10.37236/13960), preprint [arXiv:2503.10504](https://arxiv.org/abs/2503.10504), reports the general 3-MOLS(10) existence question remains open; its SAT results resolve restricted cases only. Do not label this as a contradiction.

If alpha(G_c[R])<=q also, the edge budget forces all residual excesses to vanish, yielding a full affine plane of order q. Whether it can be extended by the 2r outside vertices under the EG617 counterexample contract remains OPEN.


## 5. MOLS consequences and exact status

The residual q-net lower bound forces N(q)>=ceil(q/2)-2 only in J's Case B.

- q=10 (r=11): this is N(10)>=3. Bright, Keita, and Stevens, *Myrvold's Results on Orthogonal Triples of 10 x 10 Latin Squares: A SAT Investigation*, EJC 33(1) (2026), P1.30, DOI [10.37236/13960](https://doi.org/10.37236/13960), report the general three-MOLS existence problem remains open. Their SAT results address restricted configurations only.
- q=14 (r=15): this is N(14)>=5. Four MOLS(14) were constructed by Todorov, *Four Mutually Orthogonal Latin Squares of Order 14*, Journal of Combinatorial Designs 20 (2012), DOI [10.1002/jcd.21298](https://doi.org/10.1002/jcd.21298). The existence of a fifth is still reported open in the MOLS literature.

Projective planes of orders 10 and 14 do not exist, so K.RM3 cannot occur for these q. The residual partial-net implications remain open rather than contradictory. No full EG617 theorem follows from these design facts.
