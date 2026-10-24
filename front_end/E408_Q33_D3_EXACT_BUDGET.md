# E408 / Q33 / d3 — exact shell-budget collapse

Status: **PROVED CONDITIONAL ON THE RETAINED V11 Q33 INTERFACE**. This note strengthens the scalar Q33 normal form. It does **not** claim that the Q33/d3 family is empty.

## 1. Frozen interface

Let F be the 61-vertex h13 T61 target residual with

- e(F)=408 and delta(F)=13;
- a legal degree-13 pivot p;
- shell A=N_F(p), |A|=13;
- core H=V(F)\(A union {p}), |H|=47;
- q=e(M)+G_A=33, where M=bar(F[A]), g_a=d_F(a)-13>=0, and G_A=sum_{a in A} g_a;
- e(H)=284, delta(H)>=12, and sum_{x in H}(d_H(x)-12)=4.

The inherited D(14)=69 cap gives e(M)>=22. The Q33 interface supplies a support S subset A of size3, B=A\S of size10, M[B]=empty, and for a in S the exact row equations

t_a=10+d_{M[S]}(a)+X_a,

where t_a=|N_F(a) intersect H|=d_M(a)+g_a, X_a=e_R(a,D)+eta_a>=0, and eta_a>=0. Put

- beta=e_M(S);
- c_a=e_M(a,B);
- c_S=sum_{a in S} c_a=e_M(S,B);
- X=sum_{a in S} X_a;
- G_S=sum_{a in S}g_a;
- G_B=sum_{b in B}g_b.

Since M[B]=empty, e(M)=c_S+beta. Also d_M(a)=d_{M[S]}(a)+c_a. Comparing the two formulas for t_a gives the pointwise identity

**(1)**  c_a+g_a=10+X_a.

## 2. The exact three-unit correction identity

Summing (1) over S gives

**(2)**  c_S+G_S=30+X.

On the other hand, q=33 and M[B]=empty give

**(3)**  33=e(M)+G_A=c_S+beta+G_S+G_B.

Substitute (2) into (3):

> **(4)  beta + X + G_B = 3.**

This is exact, not an inequality. In particular, all internal missing edges of S, all row correction terms X_a, and all decorations on B consume the same three-unit budget.

Since beta,X,G_B are nonnegative integers, the only four cases are:

| beta=e(M[S]) | X+G_B | c_S lower bound from e(M)>=22 | G_A=33-e(M) |
|---:|---:|---:|---:|
| 0 | 3 | c_S>=22 | 3..11 |
| 1 | 2 | c_S>=21 | 2..11 |
| 2 | 1 | c_S>=20 | 1..11 |
| 3 | 0 | c_S>=19 | 0..11 |

The bound on c_S is e(M)=c_S+beta>=22. The upper endpoint G_A<=11 follows from the same inequality.

## 3. Consequences for the ten B-rows

For b in B put k_b=d_M(b)=|N_M(b) intersect S|. Since M[B]=empty,

- 0<=k_b<=3;
- t_b=k_b+g_b;
- sum_{b in B}k_b=c_S.

From (4), G_B=3-beta-X<=3. At most G_B vertices of B can have positive decoration, so

> **at least 10-G_B=7+beta+X vertices of B are regular** (g_b=0).

Also, if n_2 is the number of B-vertices with k_b>=2, then

c_S=sum_b k_b <= 10+2 n_2,

because each of the ten vertices with k_b<=1 contributes at most1, while a vertex with k_b>=2 contributes at most3. Thus

n_2 >= ceil((c_S-10)/2) >= ceil((12-beta)/2).

Subtracting the at-most G_B decorated vertices gives the following guaranteed number of **regular** B-vertices with k_b>=2:

| beta | total B-vertices with k_b>=2 | regular B-vertices with k_b>=2 |
|---:|---:|---:|
| 0 | at least 6 | at least 3 |
| 1 | at least 6 | at least 4 |
| 2 | at least 5 | at least 4 |
| 3 | at least 5 | at least 5 |

So every Q33/d3 candidate has at least three regular B-vertices with at least two missing incidences into S; the beta=3 case has at least five.

The pointwise identity (1), together with c_a<=10 and the full-color cap g_a<=6, also gives

> **4+X_a <= c_a <=10**, and **g_a>=X_a**.

Finally, the S-row sizes are fixed by the support pattern:

**(5)**  sum_{a in S} t_a = 30+2 beta+X = 33+beta-G_B,

while the total shell-core incidence count is

**(6)**  sum_{a in A}t_a=e(M)+33.

## 4. Core excess identity

The 47-core has total degree excess four over12. Therefore the sum of its degrees in F (core edges plus shell incidences) gives

sum_{x in H}(d_F(x)-13)
= [2e(H)+sum_{a in A}t_a]-13*47
= [568+(e(M)+33)]-611
= **e(M)-10**.

Consequently the Q33/d3 shell forces at least12 units of total target-degree excess on the 47 core, since e(M)>=22. This is consistent with, but sharper than, merely saying that the 43 degree-12 core vertices must each receive at least one shell incidence.

## 5. Retained row-union filters

Where the retained V11 row-union lemmas apply, every edge ab in M forces t_a+t_b>=13. For a regular b in B, t_b=k_b, so if ab is a missing edge:

- t_a=10 forces k_b=3;
- t_a=11 forces k_b>=2;
- t_a>=12 forces k_b>=1.

If beta=1 and z in B has k_z=2, then the unique M[S]-edge uv together with z forms a triangle in M. Under the retained R(2,23) exclusion, t_u+t_v+t_z>=25; because t_u=11+X_u, t_v=11+X_v and t_z=2+g_z, this gives the exact necessary condition

> **X_u+X_v+g_z>=1.**

These are conditional on the cited retained lower-order row-union seeds; equation (4) and the budget table are pure consequences of the Q33 shell equations and e(M)>=22.

## 6. What this closes—and what it does not

**Closed:** the Q33/d3 scalar allowance is no longer an unconstrained sum of many nonnegative terms. It is exactly the four-case budget (4), with the row-count consequences above.

**Still OPEN:** these necessary conditions do not alone contradict any of beta=0,1,2,3. A valid full closure must still combine them with the actual 284-edge core adjacency structure and the seven-block global near-Latin/color-completion system. The table is a necessary-condition classification, not a list of realizable graphs.
