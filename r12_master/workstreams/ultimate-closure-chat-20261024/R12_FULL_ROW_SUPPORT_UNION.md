# Full-row shell-support union lower bound (E407 Q32 templates A/C)

Date: 2026-10-25  
Status: **PROVED** under the retained E407 Q32/T61 shell contract. This is a necessary-structure theorem, not a terminal exclusion.

## 1. Exact shell-incidence budget

Let F be the 61-point E407 Q32 residual, with pivot p, shell A of size 13, core H of size 47, e(F)=407, and e(H)=284. Let M be the missing-edge graph on A. Then e(A,H)=e(F)-13-(78-e(M))-284=32+e(M). Every x in H has d_H(x)>=12 and d_F(x)>=13, so it has at least one target neighbor in A. Writing r_A(x)=|N_F(x) intersect A|, we obtain sum_x(r_A(x)-1)=e(A,H)-47=e(M)-15.

For b in B=A\S, let D_b=N_F(b) intersect H and k_b=|D_b|=d_M(b) in {0,1,2,3}. Since M[B] is empty, sum_b k_b=e(M)-beta, where beta=e(M[S]).

For any B' subset B, let U(B')=union_{b in B'} D_b. The duplicate-incidence count satisfies
sum_{b in B'}|D_b|-|U(B')| <= sum_x(r_A(x)-1)=e(M)-15.
This is a shell-incidence budget, not a core-edge budget.

## 2. Union bound for full-row supports

Let B_3={b in B:k_b=3}, n_3=|B_3|, and c_rest=sum_{b not in B_3}k_b. Then sum_{b in B_3}|D_b|=3n_3 and e(M)=beta+3n_3+c_rest. Substitution gives
|union_{b in B_3} D_b| >= 15-beta-c_rest.

In template A, beta=0 and the remaining nonzero rows have size one, with n_1<=4. Hence |union D_b|>=15-n_1>=11.
In template C, beta=1 and the remaining nonzero rows have size one, again with n_1<=4. Hence |union D_b|>=14-n_1>=10.

Thus in A/C, the full-row 3-sets cannot all be the same 3-set. This conclusion permits overlaps and does not assume the supports are disjoint.

## 3. Interaction with witness transversals

Every full row b misses all three hubs. The row-transversal theorem says D_b is a 3-vertex transversal of every maximum independent four-set in each corresponding hub-avoidance core. The union bounds above show that the total full-row support occupies at least 11 distinct core vertices in A and at least 10 in C.

This rules out the extreme escape in which all full rows reuse the same three core vertices. It does not classify all overlap patterns or eliminate either template.
