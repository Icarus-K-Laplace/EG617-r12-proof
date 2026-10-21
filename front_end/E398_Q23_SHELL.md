# E398 exact q23 shell — complete closure

Status: `PROVED`.

## Local cell

Let `R` be a T61 residual with `E=398`. The previously proved excess-neighbour argument gives degree multiset

`14^3,13^58`.

Take a degree-13 pivot `p` adjacent to one of the three degree-14 vertices. Then

`q=23`, `z=22`, `G=1`, `e(C47)=284`.

Let `A=N(p)` be the 13-shell, `M=complement(R[A])`, and let `x in A` be the unique degree-14 shell vertex. Thus `g_x=1`, every other shell decoration is zero, and `e(M)=22`.

Because `p` is adjacent to every shell vertex and `omega(R)<=11`, the target graph `R[A]` cannot contain a K11. Equivalently

`alpha(M)<=10`.

## Classification theorem

The q23 local equations force

`M = (K_{2,11} + centre edge) - one cross edge`.

Its degree multiset is

`12,11,2^10,1`.

In particular the 11 vertices off the two centres are pairwise nonadjacent in M, so

`alpha(M)>=11`.

This contradicts `alpha(M)<=10`. Therefore the q23 local cell is impossible.

## Proof of the forced normal form

### 1. M is K4-free and not triangle-free

An M-K4 gives four pairwise target-nonadjacent shell vertices. Their core rows must cover at least36 of the 47 core vertices; otherwise the uncovered core contains an independent2-set, producing an independent6-set in R. Thus for its four vertices S,

`q >= t(S)-e_M(S) >=36-6=30`,

contradicting q23. Hence M is K4-free.

The h13 shell matching lemma supplies a 3-matching. If M were triangle-free, the six matching endpoints have total row weight at least33 and span at most9 missing edges, giving

`q>=33-9=24`,

again impossible. Hence M contains a triangle T.

### 2. A triangle leaves an independent 10-set outside

Put `B=A\T`, |B|=10, `c=e_M(T,B)`, `u=e_M(B)`. Since e(M)=22,

`c+u=19`.

The three core rows of T must cover at least24 core vertices, otherwise T plus an independent3-set in the uncovered core gives an independent6-set. Hence `t(T)>=24`.

If the decorated x is outside T, this gives c>=18 and u<=1. If x lies in T, c>=17 and u<=2.

Suppose `rs` is an M-edge inside B. K4-freeness gives each endpoint at most2 neighbours in T. Since u<=2, an undecorated B-vertex has weight at most4, and even a decorated B-vertex has weight at most5. Therefore `t_r+t_s<=9`, contradicting the pair-row cover requirement `t_r+t_s>=11` for every M-edge.

Thus `u=0`, so `c=19`. The ten B-vertices are independent in M; nine have two neighbours in T and one has one neighbour in T.

### 3. One triangle vertex has no B-neighbour

At least eight of the nine 2-neighbour B-vertices are undecorated, hence have weight2. Any triangle vertex adjacent to one of them must therefore have weight at least9.

If all three triangle vertices met such an ordinary B-vertex, their total weight would be at least27. But with c=19,

- `t(T)=25` if x is outside T;
- `t(T)=26` if x lies in T.

So some triangle vertex has no ordinary 2-neighbour in B.

It also cannot be adjacent only to the unique 1-neighbour B-vertex, nor solely to a decorated outside vertex: the corresponding edge-weight sum is strictly below11. Hence one triangle vertex has no B-neighbour at all.

The other two triangle vertices carry all19 T-B incidences. One meets all ten B-vertices and the other meets nine. Including their triangle edges, their M-degrees are12 and11; the third triangle vertex has degree2; among B there are nine degree2 vertices and one degree1 vertex.

Thus M is exactly `(K_{2,11}+centre edge)-one cross edge`.

### 4. Final contradiction

The 11 non-centre vertices are independent in M. Hence `alpha(M)>=11`. But `alpha(M)<=10` because an independent11-set in M is a target K11 inside the shell, and adding pivot p would create a target K12, forbidden by `omega(R)<=11`.

Contradiction.

## Consequence for T61

Every degree14 vertex in an E398 graph has at least12 degree13 neighbours. Choosing any such neighbour creates the impossible q23 local cell above. Therefore

`T61(E398)=empty`.
