# Bounded-Allowance d1 Terminal — Exact Exchange and Remaining Obstruction

Status: **OPEN** for absolute nonextension. The d1 transition is exact, but the present inequalities only give a linear bound.

## 1. Fixed singleton class

Assume A+B and r >= 12. Fix a d1 shell class with missing shell vertex S={s}. Let its distinct q-flat core supports be D_i={u_i}, i=1,...,N, and let c be the common allowance. In the neutral-free plateau slice, the supports u_i are distinct.

Write w_x = kappa_x + e_F(x,S). For every q-flat owner,

w_{u_i}=c.

The common-S charge total is

W_1 = sum_{x in H} w_x = K+r+c.

Since the supports are distinct,

N c <= W_1 = K+r+c.

Under K <= 2r-2 this gives

(N-1)c <= 3r-2.                                                (1.1)

If c=0, row closure makes the distinct support vertices pairwise target-nonadjacent, so alpha(H)<=3 gives N<=3.

For c>=1, the low-owner clique lemma gives a second bound: p together with the N regular low owners forms a target clique. Since omega(F)<=r-1,

N <= r-2.                                                       (1.2)

Neither (1.1) nor (1.2) is an absolute bound in r for fixed positive c.

## 2. Exact one-point exchange

Repivot through owner y_i with support u_i. For every j != i, the old owner y_j remains a d1 owner in the new view:

- its new missing shell vertex is u_i;
- its new core support is u_j.

The transported excess is exact:

kappa'_z = w_z - e_H(z,u_i).

For z=u_j this becomes

kappa'_{u_j}=c-e_H(u_j,u_i),

and the new common-S weight is

w'_{u_j}=kappa'_{u_j}+e_F(u_j,u_i)=c.

Thus the whole distinct d1 class is closed under swapping the distinguished singleton S with any support u_i. The adjacency bit e_H(u_i,u_j) changes the transported excess by one but does not change the allowance.

For c=1, every pair u_i,u_j may be either a target edge or a target nonedge under the local equation: the new excess is respectively 0 or 1. Therefore the transition identities alone do not force a sparse or dense support graph.

## 3. What eta contributes

The d1 population eta is distributed over at most five singleton shell classes. Hence some class has

N >= ceil(eta/5).

For that class, (1.1) gives

c <= (3r-2)/(N-1), for N>1.

Consequently eta >= epsilon r forces c=O(1) for fixed epsilon>0. This is the proved scale-transfer statement.

However, O(1) allowance does not imply O(1) multiplicity: for every fixed c>=1, the current strongest general bound remains N<=r-2. The c=0 case is closed, but c=1,2,...,C are not.

## 4. Static local model showing the gap

A set of N distinct support vertices can be partitioned into three target cliques, giving alpha at most 3, while the owner class is a separate target clique of size N with a one-to-one owner-support incidence. The singleton transition formula remains valid because each support has common-S weight c and the transported excess changes by the adjacency bit.

This is only a local incidence model, not a construction of a full legal core satisfying every global contract. It demonstrates that the current d1 equations, alpha(H)<=3, and clique bound N<=r-2 do not by themselves force an absolute N bound.

## 5. What would close d1

A valid absorption proof must use information not captured by the one-point exchange alone. Candidate missing inputs are:

1. a sharp lower bound on shell incidences forced by all decorated support vertices when S is decorated;
2. a no-double-counting inequality combining the d1 support class, the remaining core, and the total excess K;
3. a theorem showing that the d1 exchange orbit and a clean d2 orbit must share a common charge deficit;
4. a full-graph constraint that uses alpha(F)<=4 correctly, without forbidding independent 4-sets in F.

No such inequality is currently certified.

Status: exact transition and scale transfer **PROVED_CONDITIONAL**; c=0 closure **PROVED_CONDITIONAL**; bounded-allowance d1 nonextension **OPEN**.


## 6. Round-2 independent excess budget and joint scale certificate

For every singleton support u_i, the common weight identity is

c = kappa_{u_i}+e_F(u_i,S).

Since S is a singleton, e_F(u_i,S) is 0 or 1. Hence

kappa_{u_i} in {c-1,c}.                                    (6.1)

Let K_U=sum_i kappa_{u_i}. Then the following are simultaneous necessary conditions:

- **Inherited excess:** N(c-1)<=K_U<=K<=2r-2.
- **Common-S charge:** Nc<=K+r+c<=3r-2+c.
- **Owner clique:** N<=r-2.
- **Shell incidence:** the number of supports with kappa=c-1 is at most e_F(S,H)=r+c.

The first bound is independent of the common-S charge inequality and is stronger when c>=2. In particular,

N <= min(r-2, floor((2r-2)/(c-1))) for c>=2.                (6.2)

This still permits N=Theta(r) for each fixed c, so it does not prove absolute absorption. For c=1, (6.1) gives only kappa in {0,1}; the zero-excess supports are shell-neighbours and the one-excess supports spend one unit each from K. The current cap allows both populations to be linear.

Combining this with the eta scale-transfer theorem gives a joint, exact statement. If eta>=epsilon r, some d1 class has N>=epsilon r/5. Its allowance c obeys

N(c-1)<=2r-2,  (N-1)c<=3r-2,

so c is bounded by a constant depending only on epsilon. If c>=2, the excess bound (6.2) applies; if c=1, the support population remains open. This is a second budget on the d1 class, but it does not by itself yield N=O(1).

## 7. Coupling status with the clean-pair kernel

The clean-pair Round-2 result provides a separate high-density constraint: optional block-cross degree is at most four, while any outside vertex that fails to see a whole AES part pays excess at least 3lambda-4-r>=8. These constraints do not yet imply that a d1 support class must become a clean-pair d2 class. The missing step is still a certified transition that couples the d1 singleton supports to the d2 pair-exchange orbit without assuming an unproved shared charge deficit.

Status remains **OPEN** for every fixed c>=1. No absolute N bound is certified.


## 8. Joint eta / d2 matching / d1 allowance / excess budget

This section combines the d1 and clean-pair budgets without assuming their support sets are disjoint.

Let:

- U_2 be the 2m endpoints of the clean a_2=2 matching in the high-density branch;
- b_2=e_M(S_2) in {0,1} for its distinguished shell pair;
- O_exc be the X outside-core vertices with kappa>=L, where
  L=3lambda-4-r=(r-3h-5)/2>=8 and lambda=m-r+1;
- V_1 be the N_1 distinct singleton supports in a fixed d1 class of allowance c;
- J_2=|V_1 intersect U_2| and J_X=|V_1 intersect O_exc|.

The clean shell-incidence budget gives

K_{U_2}>=2m-2r-b_2.                                           (8.1)

Every vertex in V_1 has kappa in {c-1,c}. To avoid double-counting overlaps, the union of U_2, O_exc and V_1 gives the exact necessary inequality

2m-2r-b_2 + N_1(c-1) + X L
-(c-1)J_2 - min(c-1,L)J_X <= 2r-2.                           (8.2)

The correction terms are sufficient: a d1 support overlapping U_2 can only occur for c<=2 and is charged at most c-1; an overlap with O_exc is charged by the smaller of the two lower bounds c-1 and L. U_2 and O_exc themselves are disjoint.

Since N_1>=ceil(eta/5), a weaker eta-explicit necessary inequality is

2m-2r-b_2 + ceil(eta/5)(c-1) + X L
-(c-1)J_2 - min(c-1,L)J_X <= 2r-2.                           (8.3)

In the especially useful disjoint subcase 3<=c<=L-1, both intersections vanish (kappa on U_2 is at most one; kappa on O_exc is at least L). Then

2m-2r-b_2 + ceil(eta/5)(c-1) + X L <= 2r-2,                  (8.4)

or equivalently

ceil(eta/5)(c-1)+X L <= 4r-2-2m+b_2.                         (8.5)

Because m>=ceil(4r/3+3), the right side is at most 4r/3-8+b_2. This is a genuine joint constraint: a linear eta population with c>=3 consumes the same inherited excess budget that pays for exceptional off-part vertices.

Independently, the d2 plateau matching inequality remains

ceil(N_2/(eta+1))(a_2-1) <= 4r-4+a_2+b_2,                   (8.6)

where N_2 is the number of distinct supports in the original d2 plateau and a_2 its allowance. For the clean-pair branch a_2=2 and m is the extracted matching size.

Equations (8.3) and (8.6) form the joint budget certificate for eta, matching number, allowance and excess. They are two projections of the same core budget; **do not add their left-hand sides**, because the d2 plateau charge inequality may overlap the support sets used in (8.3).

This is a new necessary inequality system, not a closure theorem. It leaves c=1, c=2 overlap cases, c>=L overlap cases, and the lower-density clean-pair branch unresolved.
