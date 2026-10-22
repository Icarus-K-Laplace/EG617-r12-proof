# High-backend V3 joint-pivot geometry — canonical reconstruction

Status: `PROVED` under the standard legal `R(4,49)` backend contract and the all-pivot 35-core minimum-degree12 theorem.

Scope: `333<=E<=340`. This file proves structural exchange and joint-row theorems only; it does not close an edge layer.

## 1. Setup and exact exchange

Let `F` be a legal 49-point residual with

- `alpha(F)<=4`, `omega(F)<=11`;
- `delta(F)=13`;
- inherited density caps;
- for every degree-13 pivot r, its 35-core `H_r` has `delta(H_r)>=12` and `e(H_r)>=211`.

Fix a degree-13 pivot p. Write

- `A=N(p)`, `H=V(F)\N[p]`;
- `M=complement(F[A])`;
- `g_v=d_F(v)-13`, `t_v=d_M(v)+g_v`;
- `q=e(M)+G_A`;
- `tau_p=|A intersect X|`, where X is the set of globally decorated vertices.

For a regular shell vertex y put

`S_y=N_M(y)`, `T_y=A\(S_y union {y})`, `D_y=N_H(y)`, `d=|S_y|=|D_y|`.

The new shell/core are exactly

`A_y={p} disjoint_union T_y disjoint_union D_y`,

`H_y=(H\D_y) disjoint_union S_y`.

For `v in H` set `kappa_v=d_H(v)-12`, and for a support D put

`m(D)=binom(|D|,2)-e_H(D)`.

Let

`B_y=e_M(T_y)+G_Ty`,

`P_y=B_y+kappa(D_y)+m(D_y)+e_F(S_y,D_y)`.

Every term of P_y is nonnegative. Exact edge partition gives

`q_y=d(13-d)+P_y`,                                      (1)

and exact decoration-count transport gives

`tau_y-tau_p=|D_y intersect X|-|S_y intersect X|`.       (2)

No profitability assumption is used.

## 2. Exact third-viewpoint formula

Let y,z be distinct regular vertices of A and suppose yz is a target edge. Put

`a=|S_y|`, `b=|S_z|`, `o=|S_y intersect S_z|`, `h=|D_y intersect D_z|`.

In the y-view, z remains in the shell and direct set tracking gives

`S_z^y=(T_y intersect S_z) disjoint_union (D_y\D_z)`,

`D_z^y=(D_z\D_y) disjoint_union (S_y\S_z)`,

hence

`d_z^y=a+b-o-h=|S_y union S_z|-h`.                        (3)

Applying (1) in the y-view yields the exact second-view charge. Decorations are global degree labels and travel with vertices; they are not recalculated from core degrees.

If yz is a target nonedge, z belongs to the y-core instead. The adjacent formula must not be applied in that view.

## 3. Nonadjacent regular codegree rigidity

For any degree-13 pivot r and any target nonneighbor v of r,

`d_(H_r)(v)=d_F(v)-|N_F(v) intersect N_F(r)|`.

Since `delta(H_r)>=12`,

`|N_F(v) intersect N_F(r)|<=1+g_v`.                       (4)

In particular, two nonadjacent regular vertices have at most one common target neighbour.

For regular shell vertices y,z with yz in M, counting their common neighbours through p, A and H yields

`14-|S_y union S_z|+|D_y intersect D_z|<=1`.

Because the union lies inside the 13-shell, equality constraints force

`S_y union S_z=A`,

`D_y intersect D_z=empty`.                                (5)

This is an exact zero-gap relation between distinct shell rows.

## 4. Regular-pivot metric partition

For every degree-13 pivot r define

`C_r=N_F[r]`

and for regular r,s

`delta(r,s)=|C_r triangle C_s|/2=14-|C_r intersect C_s|`.

This is a pseudometric. True twins have distance0.

For adjacent regular r,s, `delta(r,s)` is the missing degree of s in r's shell. Equation (1) gives

`delta(r,s)(13-delta(r,s))<=q_s`.

For nonadjacent regular r,s, (4) gives `delta(r,s)>=13`.

Hence if every regular pivot satisfies `q<=35`, every positive distance is either at most3 or at least10. If every q<=38, every positive distance is at most4 or at least9.

In the q<=35 regime define r~s iff `delta(r,s)<=3`. Triangle inequality and the forbidden gap show this is an equivalence relation. Each class is a target clique of size at most11.

An outside regular vertex meets a class either in at most one vertex or in the whole class; otherwise two hit vertices and one missed vertex violate (4). If a class has size at least4, every outside regular vertex meets it at most once.

## 5. Row closure

Let y be a regular shell vertex and let `v in H\D_y`. Since v remains in the y-core,

`d_(H_y)(v)>=12`.

Comparing old and new core degrees gives

`e_H(v,D_y)<=kappa_v+e_F(v,S_y)`.                          (6)

For two regular shell vertices y,z with support size `b=|D_z|` and overlap `h=|D_y intersect D_z|`, summing (6) over `D_z\D_y` gives

`h(b-h)<=kappa(D_z\D_y)+e_F(S_y,D_z\D_y)+m(D_z)`.          (7)

No assumption `S_y=S_z` is needed.

There is also an exact global-decoration identity. With `U=D_y union D_z`,

`sum_(v in U) g_v = kappa(U)+h+e_F(U,A\{y,z})`.            (8)

Thus every support-overlap vertex is globally decorated.

## 6. Common-S equal/disjoint theorem

Suppose regular shell vertices `y_i` share the same missing set S of size d. Put

`s=q-d(13-d)`,

`B=e_M(A\S)+G_(A\S)`,

`u_i=kappa(D_i)+e_F(S,D_i)`.

At a maximum-q pivot, (1) gives

`u_i+m(D_i)<=s-B`.                                         (9)

If two supports overlap in h points, (7) becomes

`h(d-h)<=s-B`.                                             (10)

Therefore if

`s-B<d-1`,

proper overlap is impossible: two supports are either equal or disjoint.

For distinct disjoint supports, applying row closure in both directions gives

`e_H(D_i,D_j)<=min(u_i,u_j)<=s-B`.                         (11)

This is the common-S joint-row theorem used in the high layers.

## 7. Exact core-cut identity

Let `D_1,...,D_l` be distinct disjoint supports of common size d. Put

`U=union D_i`, `Z=H\U`, `n=35-ld`,

`m_U=sum_i m(D_i)`,

`c=sum_(i<j)e_H(D_i,D_j)`,

`K=sum_(v in H)kappa_v=2e(H)-420=2(E-301-q)`.

Degree counting in U and Z yields exactly

`K=ld(25-d)-420+2kappa(U)+2m_U-2c+2e_H(Z)`.                (12)

Since `alpha(H[Z])<=3`,

`e_H(Z)>=p_3(n)`,

where `p_3(n)` is the balanced-three-clique lower bound.

Using (9) and (11) in (12) gives

`K>=ld(25-d)-420+2p_3(35-ld)-l(l-1)(s-B)`.                (13)

A stronger form retains the individual `kappa`, `m` and `min(u_i,u_j)` terms.

## 8. Consequences for common 9- and 10-point rows

For three d=9 supports, (13) gives

`K>=26-6(q-36-B)`.

Across E333--E340, the available K is too small for three distinct supports in every q36--q38 state. Hence:

> A common nine-point missing neighbourhood has at most two distinct core supports.

For three d=10 supports, (13) gives

`K>=34-6(q-30-B)`,

which is equivalent to

`E+2q>=408+3B`.                                            (14)

Thus every q<=33 state has at most two distinct d10 supports.

## 9. Forbidden all-distinct regular K4 for qmax<=33

Assume four regular vertices form a target K4 and every pair lies in different close metric classes. Choose p of largest q within the four and call the other vertices y1,y2,y3.

Each far pair has at most two common neighbours, already supplied by the other two K4 vertices. Hence at p the three missing sets are the same ten-set and the three 10-point supports are mutually disjoint.

Applying (14) to these three supports gives

`E+2q_p>=408+3B>=408`.

But for `E<=340` and `q_p<=33`,

`E+2q_p<=406`.

Contradiction.

Therefore no such regular K4 exists.

## Boundary

These results are structural only. They do not prove that every maximum pivot generates three common supports, nor do they close E333 or any higher edge layer.
