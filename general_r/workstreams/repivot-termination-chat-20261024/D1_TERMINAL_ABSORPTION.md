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
