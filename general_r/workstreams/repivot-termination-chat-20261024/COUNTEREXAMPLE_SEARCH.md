# Counterexample Search and Independent Audit — Clean-Pair Round 2

Status: **No full legal-core counterexample found; no all-r contradiction certified.** This is an audit log, not a theorem asserting existence or nonexistence.

## 1. Frozen graph-level contract

All candidate checks retain

|H|=3r-1, alpha(H)<=3, omega(H)<=r-1, delta(H)>=r,
K=sum_{v in H}(d_H(v)-r)<=2r-2.

The global residual graph has alpha(F)<=4. No argument in this file uses alpha(F)<=3.

The static block relaxation from CLEAN_PAIR_GRAPH_MODEL.md is not a full legal core: it does not specify all outside-core adjacencies, degree excesses, or the complete hereditary contract.

## 2. Independent six-pair audit

The six type classes are A0,A1,B0,B1,C0,C1, with cross-part H relations:

- matching M: A0--B0, A1--C0, B1--C1;
- optional O: A0--C1, A1--B1, B0--C0;
- empty: A0--B1, A1--B0, A0--C0, A1--C1, B0--C1, B1--C0.

A symbolic enumeration checked all nine witness pairs T0 x T1, where T0=(A0,B1,C0) and T1=(A1,B0,C1). The three same-part pairs are (A0,A1), (B1,B0), (C0,C1). Each of the six off-part pairs leaves two residual class triples; every such triple has exactly one M relation, one O relation, and one empty relation. The audit passed all six cases and both residual triples per case.

This validates the *type relation table* only. It does not imply the outside vertex is nonadjacent to the residual triple: an outside vertex may have additional neighbours in classes other than its selected witnesses. Therefore the stronger claim “every outside vertex sees an entire part” is **not established** and is explicitly not used.

## 3. Correct off-part witness lemma

The class-assignment slacks satisfy sum u_T=4 in each witness triple, so every optional H-degree is at most four.

If an outside vertex o has no pair of fully-seen witness classes from the same part, choose any witness pair from T0,T1. The pair is off-part. In one residual triple with relation pattern M,O,empty, if o had fewer than a-4 neighbours in the union of those three classes, every residual class would still have at least five vertices. We could choose:

1. a vertex in one optional endpoint class;
2. a non-neighbour in the other optional endpoint class, since its optional degree is at most four;
3. a vertex in the matching class other than the unique block mate.

These three vertices are pairwise H-nonadjacent and nonadjacent to o, violating alpha(H)<=3. Thus

d_H(o,U)>=3a-4,
kappa_o>=3lambda-4-r>=8.

For X such exceptional vertices,

X(3lambda-4-r)<=K_O<=2r-2-K_U.

This is the correct replacement for the invalid all-parts claim. Since h=r+1-2a, the exact bound is X<=floor((4r-4-2K_U)/(r-3h-5)); the denominator is at least 16 in the high-density branch. X can still be linear near a=ceil(r/3)+4.

## 4. Boundary checks

### h=2

Here all part deficits s_i vanish, and no outside vertex can see a whole part because each part is a clique of size r-1. Hence X=2. Also lambda=(r-1)/2, so each exceptional outside vertex has

kappa_o >= 3(r-1)/2 -4-r = (r-11)/2.

Therefore K_O>=r-11. This is a genuine lower bound but does not contradict K<=2r-2 after accounting for K_U. The h=2 endpoint remains OPEN.

### h=3

The deficit vector is a permutation of (1,0,0). If X=0, the two zero-deficit parts cannot receive assigned outside vertices, so all three outside vertices see the unique part of size r-2. Its assignment slack is zero, forcing all its vertices to have kappa=1 and no optional or foreign-assignment edges. Also omega(H[O])<=1, so O is an independent triple. Every vertex in the other two parts must have at least one neighbour in O, else it forms an independent 4-set with O. Hence

e_H(U,O)>=3(r-2)+2(r-1)=5r-8.

Since e_H(O)=0, K_O>=2r-8. But K_U>=r-2, so K>=3r-10>2r-2 for r>=12. Thus **h=3 with X=0 is impossible**.

If X>=1, this proof no longer applies. The h=3 case remains OPEN.

## 5. Candidate constructions and why they are not certified counterexamples

A natural relaxation is to take three target cliques A,B,C of sizes r-1-s_i, pair their vertices by AB/AC/BC blocks, and let most outside vertices see one entire part. The exact necessary counts are

s_A+s_B+s_C=h-2,
g_i=s_i+2-u_i,
sum_i u_i=4+X,
u_i>=0,

where X outside vertices are exceptional. The optional block-cross graph has maximum degree four, and the no-double-counting identity is

2 e_opt + E_foreign = K_U + sum_i n_i(u_i-1).

This relaxation has not been completed to a graph satisfying all core degrees, alpha/clique caps, and excess budget simultaneously. It is not a counterexample.

A second naive relaxation sets X=0 and makes each O_i a clique. It immediately fails the clique cap whenever u_i<2, because U_i union O_i would have size r+1-u_i and be a clique. Making O_i non-clique requires compensating cross edges or excess; those costs are not yet enough to prove a general contradiction.

## 6. Remaining search targets

1. Show that exceptional vertices cannot occupy the allowed excess budget at scale X=Theta(r), or improve the lower bound kappa_o>=3lambda-4-r using the full residual neighbourhood.
2. Combine the exact class-assignment slack sum 4 with the part-assignment slack sum 4+X and the d1 population eta.
3. Use the inherited clique constraint omega(H[O_i])<=s_i together with the O-graph's alpha constraint, without treating a local block relaxation as a full core.
4. For h=2, use K_O>=r-11 together with a lower bound on K_U or cross-incidence to obtain a contradiction; the current bound alone is insufficient.
5. For h=3, eliminate X>=1 or account for its excess more sharply.

Current status: finite type-table audit **PASS**; off-part excess lemma **PROVED_CONDITIONAL**; full legal-core counterexample **NOT FOUND**; Clean-Pair Nonextension **OPEN**.


## 7. Shell-incidence cross-check

For the clean a_2=2 family, every endpoint has kappa_x=1-e_F(x,S_2), and e_F(S_2,H)=2r+b_2. Thus

K_U>=2m-2r-b_2.

The exceptional outside vertices are disjoint from U and each pays at least L=3lambda-4-r, where lambda=m-r+1. Consequently

2m-2r-b_2+X L<=2r-2,

or

X<=floor(2(r-1+h+b_2)/(r-3h-5)).

This sharpens the prior K_U-free estimate to X<=r/6+O(1) near the lower AES threshold. It still allows a linear exceptional set and does not certify a contradiction.

For h=2, the bound K_U>=r-3-b_2 and K_O>=r-11 imply only K>=2r-14-b_2, which remains below the allowed cap 2r-2. This endpoint is still open.
