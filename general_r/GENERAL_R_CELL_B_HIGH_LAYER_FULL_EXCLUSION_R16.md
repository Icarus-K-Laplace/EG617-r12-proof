# General-r Cell B high-layer full exclusion for r>=16

Status: **PROVED_RELATIVE_TO_BROUWER_SECOND_TURAN**, conditional on the Cell-B normal form, the pointwise Cell-B extension certificate, and the contextual 5r+1 terminal contract.

## Setup

Let F be a contextual target-color terminal on 5r+1 vertices with

- alpha(F)<=5,
- omega(F)<=r-1,
- delta(F)=r+1,
- e(F)<=U_(5,r)=(5r^2+7r+18)/2.

Assume the common anti-neighbourhood W of a direct near-anchor triple is in the sharp Cell-B normal form at

|W|=2r-1.

Thus

- J=bar(F[W])=S(K_(r-1,r-1));
- e_F(W)=r^2-r-1;
- with O=V(F)\W, |O|=3r+2;
- every side vertex of W has internal target degree r-1 and therefore at least2 target neighbours in O;
- the Cell-B color-certificate theorem gives d_F(o,W)<=3 for every o in O.

## 1. Alpha(O)<=3 for r>=13

Suppose Q={q1,q2,q3,q4} is target-independent in O.

Each qi has at most3 target neighbours in W, so

|N_F(Q) intersect W|<=12.

Hence at least

|W|-12=2r-13

vertices of W are target-nonadjacent to all four points of Q.

If r>=13 then

2r-13>r-1>=omega(F[W]).

Therefore those remaining W-vertices cannot form a target clique. Choose two target-nonadjacent vertices u,v among them. Then

Q union {u,v}

is a target-independent 6-set, contradicting alpha(F)<=5.

Hence

> alpha(F[O])<=3 for every r>=13.

## 2. Brouwer lower bound inside O

Let G=F[O]. Then

|G|=3r+2,
alpha(G)<=3,
omega(G)<=r-1.

Equivalently J_O=bar(G) is K4-free and alpha(J_O)<=r-1.

A 3-partite J_O would have three independent parts of total size3r+2, so one part would have size at least r+1, contradicting alpha(J_O)<=r-1. Thus J_O is not 3-partite.

Brouwer's exact second-Turan theorem for non-3-partite K4-free graphs gives

e(J_O)<=t_3(3r+2)-floor((3r+2)/3)+1.

Taking complements,

e_F(O)>=p_3(3r+2)+r-1.

Now

p_3(3r+2)=2*C(r+1,2)+C(r,2)=(3r^2+r)/2,

so

> e_F(O)>=(3r^2+3r-2)/2.

## 3. Cross-edge floor

Every one of the 2r-2 side vertices in W has internal target degree r-1, while delta(F)=r+1. Therefore each has at least2 target neighbours in O. Hence

> e_F(W,O)>=4r-4.

(The subdivision vertex may contribute additional cross edges, which only strengthens the lower bound.)

## 4. Contradiction with the contextual cap

Summing the three disjoint edge regions,

 e(F)
 >= e_F(W)+e_F(W,O)+e_F(O)
 >= (r^2-r-1)+(4r-4)+(3r^2+3r-2)/2
 = (5r^2+9r-12)/2.

But the contextual full-color cap is

 e(F)<=(5r^2+7r+18)/2.

The lower bound exceeds the upper bound by

 r-15.

Therefore for every

> **r>=16**

no high-layer Cell-B extension exists.

## Consequence

For the all-large-r 5r+1 high-minimum-degree terminal, the sharp |W|=2r-1 Cell-B design is not a finite defect family that still needs classification: it is globally impossible for every r>=16.

Thus any all-large-r downstream proof may delete the entire high Cell-B branch outright.
