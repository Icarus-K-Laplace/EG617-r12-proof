# E408 Q33 core almost-regular normal form

Status: **PROVED_RELATIVE_TO THE RETAINED Q33 CORE MINIMUM-DEGREE INTERFACE**. The full-color consequences use the independently proved E408 target maximum-degree theorem.

## 1. Exact 47-core excess

At a degree13 pivot of an E408 T61 residual,

`E=91+q+e(C)`.

If `q=33`, then

> `e(C)=284`.

The retained V11 interface applies at this edge count and gives

> `delta(C)>=12`.

Therefore

`sum_(x in C)(d_C(x)-12)=2*284-47*12=4`.

Hence the positive core excess multiset is one of the five integer partitions of4:

- `(4)`;
- `(3,1)`;
- `(2,2)`;
- `(2,1,1)`;
- `(1,1,1,1)`.

In particular:

> **at least43 of the47 core vertices have exact core degree12.**

## 2. Complement normal form

Let

`L=bar(C)`.

Since `alpha(C)<=4`, L is K5-free. Since `omega(C)<=11`,

`alpha(L)<=11`.

A core vertex of degree `12+epsilon` has L-degree

`46-(12+epsilon)=34-epsilon`.

Thus

- `Delta(L)=34`;
- total deficiency from degree34 is exactly4;
- at least43 vertices have degree34.

Equivalently L is a 47-point K5-free graph with alpha at most11 that is within four degree-defect units of 34-regularity.

This is a finite almost-regular graph-theoretic interface for Q33.

## 3. Every degree12 core vertex must be hit by the shell

The independently proved full-color theorem gives, for E408,

`13<=d_F(v)<=19`

for every vertex of the61-point target residual F.

For a core vertex x with `d_C(x)=12`, the pivot p is target-nonadjacent to x, so its remaining target degree must be supplied by shell neighbours. Therefore every one of the at least43 core-degree12 vertices has at least one target neighbour in the 13-point shell.

Consequently the union of the thirteen shell rows covers at least43 distinct core labels.

Let

`t(A)=sum_(a in A)|N_C(a)|`

be the total shell--core incidence count.

Since `t_a=d_M(a)+g_a`,

`t(A)=2e(M)+G_A`.

Also `q=e(M)+G_A=33`, so

> `t(A)=e(M)+33`.

Coverage of at least43 distinct core labels yields

> **`e(M)>=10`.**

## 4. Additional d3-candidate strengthening

Assume there is a regular missing-degree3 candidate y with

`S=N_M(y)`, `B=A\S`, `|S|=3`, `|B|=10`.

V11 proves `M[B]=empty` and the exact inserted-row equations

`t_a=10+d_(M[S])(a)+e_R(a,D)+eta_a`.

The independently proved E408 global maximum-degree bound `Delta(F)<=19` gives

`g_a<=6`.

Writing

`c_a=e_M(a,B)`,

and using `t_a=d_M(a)+g_a=d_(M[S])(a)+c_a+g_a`, we obtain pointwise

> **`c_a+g_a=10+e_R(a,D)+eta_a`.**

Hence

> **`c_a>=4+e_R(a,D)+eta_a`.**

Summing over the three hubs gives

`e_M(S,B)>=12+b+eta`.

In particular any Q33 d3 candidate forces

> **`e(M)>=12`.**

## 5. Completion interface

Any genuine E408 Q33 completion therefore must satisfy simultaneously:

1. a 47-core with total degree excess exactly4 and at least43 degree12 vertices;
2. complement K5-free, alpha<=11, max degree34, total degree deficiency4;
3. shell rows covering at least43 distinct core labels;
4. shell missing graph with at least10 edges, and at least12 if a d3 candidate exists;
5. global target maximum degree19;
6. the seven-block near-Latin completion constraints from `E408_GLOBAL_SEVEN_BLOCK_EQUALITY_SYSTEM.md`.

This is strictly stronger than the scalar Q33 shell interface and should be used in any subsequent Q33 compatibility analysis.
