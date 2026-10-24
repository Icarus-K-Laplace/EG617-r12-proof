# Fully-Decorated d2 Distinct-Support Reduction

Assumptions: A+B, `r>=12`, and a `Phi_3=(q,tau,zeta)`-maximal pivot p. Fix one d2 shell class

`S={u,v} subset X`

and consider exact classes of multiplicity one whose repivots are `Phi_3`-flat. By the exact class-neutral involution, this distinct-support plateau lies in the neutral-free slice

> **`zeta(p)=0`.**

Let Q be the simple graph on core vertices whose edges are the distinct q-flat supports `D_y`. For `x in H`, put

`w_x=kappa_x+e_F(x,S)`.

For a support `D=xy`, put

`mu(D)=1-e_H(xy) in {0,1}`.

The fixed-class q-flat equation is

> **`w_x+w_y+mu(xy)=a`.**                                    (1.1)

Row closure gives, for every support D and every `z notin D`,

> **`e_H(z,D)<=w_z`.**                                       (1.2)

The total weight is

> **`W=sum_{x in H}w_x=K+2r-2+a+b`.**                        (1.3)

---

## 2. Exact support-transition identity

Let y,z be two regular owners in the same old d2 shell class S, with core supports `D_y,D_z`. Repivot through y.

The new shell is

`A_y={p} union T_y union D_y`,

and z remains in the shell because same-class owners are target-adjacent.

Among the new shell vertices, z is missing exactly the vertices of `D_y` which were not its old core neighbours. Hence

`S_z^(y)=D_y\D_z`.

Among the new core vertices, z is adjacent exactly to the surviving old support vertices

`D_z^(y)=D_z\D_y`.

Therefore

> **`d_z^(y)=|D_y\D_z|=2-|D_y intersect D_z|`.**              (2.1)

Thus for d2 supports:

- repeated support (`|intersection|=2`) becomes a d0 transition;
- one-point overlap becomes a d1 transition;
- disjoint supports remain a d2 transition.

This is an exact correction-graph dictionary.

If all owner moves from p are `Phi_3`-flat distinct moves, then every owner-pivot has the same `(q,tau,zeta=0)`. Hence the pairwise correction transition between any two owner pivots is also `Phi_3`-flat, with its degree given by (2.1).

**Status:** `PROVED_SYMBOLIC`.

---

## 3. Allowance a=0: at most three distinct supports

If `a=0`, (1.1) forces

- `mu(D)=0`, so every support is a target edge of H;
- both support endpoints have weight zero.

Two distinct supports cannot overlap. Indeed, if `D_1={x,y}` and `D_2={x,z}`, then y is outside D2 and `w_y=0`. Row closure (1.2) gives

`e_H(y,D_2)=0`,

contradicting the target edge xy in D1.

For two disjoint supports D1,D2, any endpoint x of D1 has weight zero, so row closure against D2 gives no target edge from x to D2. Thus there are no H-edges between distinct supports.

Choosing one endpoint from each of four supports would give an independent 4-set in H, contrary to `alpha(H)<=3`.

Therefore

> **`a=0 => |E(Q)|<=3`.**                                    (3.1)

**Status:** `PROVED_CONDITIONAL`.

---

## 4. Allowance a=1: at most nine distinct supports

Equation (1.1) gives exactly two support types:

1. target edge (mu=0) with endpoint weights (0,1);
2. target nonedge (mu=1) with endpoint weights (0,0).

Hence every support contains at least one zero-weight endpoint.

For each zero-weight vertex z appearing in a support, define its support signature
`sig(z)={D_i:z in D_i}`.

Distinct zero-weight signatures are pairwise target-nonadjacent by row closure. Indeed, if two zero-weight vertices occur in the same support, that support is a target nonedge; if they do not occur together, row closure applied to a support containing one but not the other rules out a target edge between them. Since `alpha(H)<=3`, there are at most three distinct zero-weight signatures.

Fix one signature `Sigma`. If `|Sigma|>=3`, its supports share a unique zero-weight hub x and have the form
`{x,u_1},...,{x,u_k}`.
For each leaf u_i, allowance-one flatness gives `w(u_i)=1` when xu_i is a target edge and `w(u_i)=0` when xu_i is a target nonedge. Row closure applied to u_i against support {x,u_j} shows in either case that u_i u_j is a target nonedge. The leaves are therefore pairwise independent, so `k<=3`. If `|Sigma|<3`, the same bound is immediate.

Every support contains at least one zero-weight endpoint, and there are at most three distinct zero-weight signatures. Summing the at-most-three support labels per signature gives

> **`a=1 => N<=9`.**                                         (4.3)

This sharpens the earlier coarse bound 12. The argument uses only `alpha(H)<=3`, not a global `alpha(F)<=3` assumption.

**Status:** `PROVED_CONDITIONAL` on the residual core contract; no hereditary cap is used.
 
## 5. General matching bound

Let `nu(Q)` be the matching number of the distinct-support graph. For every support edge xy, (1.1) implies

`w_x+w_y=a-mu(xy)>=a-1`.

The endpoints of matching edges are disjoint, so for `a>=2`,

> **`nu(Q)(a-1)<=W`.**                                       (5.1)

Using (1.3) and the residual edge cap, the current d2 view has

`q=2r-2+a+B`,

so

`K=2(E-q-(2r^2+r+1))<=2r+10-2a-2B`.

Consequently

`W=K+2r-2+a+b<=4r+8-a+b<=4r+9-a`.

Thus

> **`nu(Q)(a-1)<=4r+9-a`.**                                  (5.2)

Any maximal matching supplies a vertex cover of Q of size at most `2nu(Q)`. Hence high allowance automatically collapses the distinct-support graph to a small hub kernel.

**Status:** `PROVED_CONDITIONAL`.

---

## 6. Additional structure at a=2

At `a=2`, support types are

- target edges with weights `(0,2)`, `(1,1)`, `(2,0)`;
- target nonedges with weights `(0,1)` or `(1,0)`.

Zero-weight support vertices are pairwise target-nonadjacent by the same row-closure argument as above, hence there are at most three.

The subgraph Q1 consisting of `(1,1)` target supports has maximum degree at most three. Indeed, if x is the center of support edges `xy_i`, then for `i!=j`, row closure from `y_i` against `{x,y_j}` gives

`e_H(y_i,{x,y_j})<=1`.

Because `y_i x` is a target edge, the leaves are pairwise target-nonadjacent; `alpha(H)<=3` gives at most three leaves.

Therefore any unbounded `a=2` distinct-support family must be assembled from

- at most three zero-weight hubs, plus
- a maximum-degree-three `(1,1)` target-support graph.

This is a substantial reduction but not yet an absolute bound.

**Status:** structural reduction `PROVED_CONDITIONAL`; full `a=2` closure `OPEN`.

---

## 7. Distinct-support hereditary capacity inequality

Let N be the number of distinct owners/supports in the fixed class, let U be the union of the core support vertices, `v=|U|`, and `e=e_H(U)`.

The induced set

`B={p} union Y union U`

has size

`t=N+v+1`.

Because p together with all low owners is a target clique, each owner has exactly its two support neighbours in U, and p has no target edge to U,

> **`e_F(B)=C(N+1,2)+2N+e`.**                                (7.1)

Whenever the hereditary residual cap applies in the range

`r<=t<2r`,

`e_F(B)<=C(t,2)-(r-1)(t-r)`.

Algebra gives

> **`N <= r-3 + (v^2-3v+8-2e)/(2(r+1-v))`.**                 (7.2)

This is exact in its stated range. As already observed in the architecture notes for common-hub capacity, it is a slope-`r` packing inequality and does not by itself yield a sufficiently-large-r contradiction.

**Status:** `PROVED_CONDITIONAL` on the stated hereditary cap/range.

---

## 8. Main-theorem impact

The distinct-support blocker is now stratified:

- `a=0`: absolute bound 3;
- `a=1`: absolute bound 9;
- `a=2`: reduced to at most three zero-weight hubs plus a max-degree-three weight-one target-support graph;
- `a>=2`: matching/vertex-cover bound (5.2), becoming strongest when allowance grows with r;
- pairwise correction geometry is exactly d0/d1/d2 according to support intersection.

Thus the first unresolved allowance layer is **a=2**, and the first unresolved correction transition generated by support overlap is **d1**.

The next useful theorem should either close the max-degree-three a=2 graph or exploit the support-transition identity to turn one-point overlaps into a d1 plateau contradiction.