# Fifth-Coordinate Audit: Q2 Is Bounded but Cannot Be Universally Increasing

Status: the exact formula is **PROVED_SYMBOLIC**. Universal strict increase on every nontrivial reversible Phi4-flat move is **DISPROVED AS STATED**.

## 1. Exact formula

Let

Q2(H)=sum_{v in H} kappa_v^2.

For a legal repivot p -> y with missing set S_y and core support D_y, define for z in H\D_y

delta_z = e_F(z,S_y)-e_H(z,D_y).

Then

kappa'_z = kappa_z + delta_z,

and for s in S_y,

kappa'_s = sigma_s-e_F(s,D_y).

The exact difference is

Delta Q2 =
sum_{z in H\D_y} [2 kappa_z delta_z + delta_z^2]
+ sum_{s in S_y} [sigma_s-e_F(s,D_y)]^2
- sum_{u in D_y} kappa_u^2.                                  (1.1)

This partitions the change into unchanged-core vertices transported by delta_z, vertices entering the new core from the shell, and removed core vertices. It is exact, but it has no termwise sign.

## 2. Clean-pair simplification

For a clean block D_i={x_i^0,x_i^1}, define

a_z=e_F(z,S) in {0,1},
b_{zi}=e_H(z,D_i) in {0,1}

for an endpoint z in another clean block. The clean weight equation gives

kappa_z=1-a_z,
kappa'_z=1-b_{zi}.

Therefore this endpoint's contribution to Delta Q2 is exactly

(kappa'_z)^2-kappa_z^2 = a_z-b_{zi}.                           (2.1)

Summing over all other clean endpoints yields

(number of old S-edges into those endpoints)
-
(number of target edges from those endpoints to D_i).

Either sign is possible from this local expression. The entering S vertices and all non-clean core vertices contribute the remaining terms in (1.1), whose signs are also not fixed by the clean weight equation alone.

Hence no positivity claim follows merely from weights (1,1) and pairwise matching cross graphs.

## 3. Reversibility no-go theorem

Every legal repivot is reversible. If p -> y is Phi4-flat, then q, tau, zeta and eta agree at the two states. The reverse repivot y -> p is therefore also Phi4-flat.

For any scalar statistic Q, exact reversibility gives

Delta Q(y -> p) = -Delta Q(p -> y).

It follows that the claim

Delta Phi4 = 0 implies Delta Q2 > 0 for every nontrivial terminal-preserving move

cannot hold on a reversible edge: the forward and reverse moves cannot both have strictly positive increments. If the increment is zero, neither direction improves Q2; if it is nonzero, one direction decreases Q2.

This is not a proof that Q2 is useless as a tie-breaker. It can select a maximal representative of a finite orbit. But it cannot, by itself, prove that every nontrivial Phi4-flat move strictly improves a fifth coordinate. A valid termination proof must instead show that the maximal state has an impossible terminal structure, or identify a genuinely directed operation that is not paired with its reverse.

## 4. Required next audit

For any proposed replacement fifth coordinate, explicitly check:

1. Is the move reversible?
2. Does the reverse move preserve the first four coordinates?
3. Is the proposed increment antisymmetric under reversal?
4. If the statistic is not antisymmetric, which exact state data break the symmetry?
5. Does the argument eliminate a maximal terminal, rather than merely orient edges in a finite correction graph?

Status: Q2 formula **PROVED_SYMBOLIC**; universal strict monotonicity claim **DISPROVED**; a fifth-coordinate-based terminal elimination **OPEN**.
