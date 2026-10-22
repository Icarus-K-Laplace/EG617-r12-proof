# E406 d=3 Type-A O4: saturated low-row obstruction

Status: `PROVED` under the eta=1 simple-four-double contract in the cases stated below.

Let P be a pure class of size p and suppose its row contains exactly w singleton-full carriers, with

`p+w=8`.

The only instances needed are

- `(p,w)=(5,3)`;
- `(p,w)=(6,2)`.

Let Q be an 8-class and let x be a double-full vertex on the P-row and Q-row. Assume the global eta=1 O4 contract:

- total H-excess3;
- every H-vertex has `eps<=1`;
- singleton-full carriers on one row form a clique;
- the relevant partial-incidence budget satisfies `r_x+r_u<=2` for every singleton u on the P-row (this is automatic in the `(5,6,8,8)` and `(6,6,8,8)` applications below).

Then no such x exists.

## 1. Missing-set rigidity

Put

- `a=|P\N_H(x)|`;
- `b=|Q\N_H(x)|`;
- r = partial support incidence of x;
- h = H-neighbours of x outside `P union Q`.

Since x is full to two support triangles,

`eps_x = p+2+r-a-b+h <=1`.

The missing pure sets are completely joined.

Every vertex of P already has

`(p-1)+w = 7`

fixed H-neighbours inside its pure clique and among the same-row singleton carriers. Thus it has only `2+eps` slots for further H-neighbours. Every Q-vertex likewise has only `2+eps` external slots beyond its K8 clique.

Consequently the excess spent on x and the two missing pure sets is at least

`h+p+2+r-a-b + a[b-2]_+ + b[a-2]_+`.

Together with the global three-unit excess budget and `eps_x<=1`, this forces `a=0`.

Indeed, for a>=1 the exact inequality `a+b>=p+1+r+h` coming from `eps_x<=1` substituted into the displayed lower bound gives at least4 units in both p=5 and p=6 cases.

Therefore x is complete to P.

Moreover

`b >= p+1+r+h`.

Hence x misses at least

- six Q-vertices when p=5;
- seven Q-vertices when p=6;

and has at most `2-r` H-neighbours outside P in the p=5 case, at most `1-r` in the p=6 case.

## 2. x must meet every same-row singleton

Fix a singleton-full carrier u on the P-row and suppose xu is a nonedge.

Because all same-row singleton carriers form a clique, u already has

`p+(w-1)=7`

H-neighbours in P and among its same-row singleton companions.

Also

`d_H(u)=9+eps_u-r_u <=9`,

so u has at most two further H-neighbours outside that fixed set.

Let R,S be the two support rows different from the common P-row and the Q-row. Since `r_x+r_u<=2`, in each K3 row `T_R,T_S` there is a vertex missed by both x and u. Call them t_R,t_S.

The Q-class has eight vertices. The missing-set bound above shows that x misses at least six of them, while u is adjacent to at most two Q-vertices. Hence there is z in Q nonadjacent to both x and u.

Since z is pure to the Q-row, it is anticomplete to T_R and T_S. The four support triangles are pairwise anticomplete. Thus

`{x,u,z,t_R,t_S}`

is an independent5-set, contradiction.

Therefore x is adjacent to every same-row singleton carrier.

## 3. K12 contradiction

The set

`P union T_P union W`

is a clique of size

`p+3+w = 11`.

By Section1 x is complete to P and by definition is full to T_P. Section2 makes x adjacent to every member of W. Hence adding x produces a K12, contradicting `omega(C)<=11`.

Therefore a saturated low row with `p+w=8` cannot be incident with a double to an 8-class.