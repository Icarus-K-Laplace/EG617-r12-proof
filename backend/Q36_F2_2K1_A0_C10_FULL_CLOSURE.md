# q36 f=2, 2K1 far, a_F=0 — full closure of the c=10 high-c single-class terminal

Status: `PROVED` under `Q36_F2_2K1_A0_HIGH_C_SINGLE_CLASS_NORMAL_FORM.md`, row closure, CORE211, inherited D14, and `alpha(H[R])<=2`.

This closes the final all-d3 / single missing-vertex high-c branch.

## 1. Exact c=10 setup

By the high-c normal form:

- the low clique C has size10;
- X={x} is the unique decorated shell vertex;
- the far regular set F is 2K1;
- every low owner has the same missing triple S=F union {x};
- R has 11 vertices and alpha(H[R])<=2;
- x is target-adjacent to every vertex of R;
- the ten low supports D_y are 3-subsets of R;
- every support repivot has q<=35 and kappa(D)+m(D)<=2;
- CORE211 gives sum_(v in R) kappa_v<=2.

Let J be the complement of H[R]. Then J is triangle-free.

For every support D and every v in R\D, row closure reads

`e_H(v,D)<=kappa_v+1`

because v is adjacent to x and to neither far vertex. Equivalently,

> `d_J(v,D)>=2-kappa_v`.                                   (1)

We first prove that all ten supports contain one common core vertex.

## 2. Two supports cannot be disjoint

Suppose D,E are disjoint 3-supports.

There are five vertices of R outside D union E. Since total core excess is at most2, at least one such vertex w is regular; in fact at least three are regular.

By (1), w has at least two J-neighbours in D and at least two in E. Choose 2-sets D0 subset D and E0 subset E inside N_J(w).

Because J is triangle-free, there is no J-edge between D0 and E0: any such edge together with w would be a J-triangle.

Now take a vertex u in D0. Relative to support E, u has at most one possible J-neighbour in E, namely the third vertex E\E0. Thus (1) forces kappa_u>=1. The same argument applies to all four vertices of D0 union E0.

Hence total core excess is at least4, contradicting CORE211.

Therefore

> any two distinct supports intersect.                      (2)

## 3. A one-point intersection forces a universal common point

Suppose

`D={z,a,b}`, `E={z,c,d}`

with D intersect E={z}.

Let W=R\(D union E), so |W|=6. At least four vertices of W are regular.

### 3.1 Every regular w in W is J-adjacent to z

If wz were not a J-edge, then (1) would force w adjacent in J to both a,b and both c,d.

Triangle-freeness would then forbid every J-edge between {a,b} and {c,d}. Each of the four petals would consequently have at most one J-neighbour in the opposite support (possibly z), so (1) would force

`kappa_a,kappa_b,kappa_c,kappa_d >=1`,

again contradicting total excess at most2.

Thus every regular w in W satisfies wz in E(J).

### 3.2 Exactly one excess petal lies on each side

Fix a regular w in W. Because w is regular, (1) also forces at least one J-neighbour of w in {a,b} and at least one in {c,d} in addition to z.

Let wa and wc be such edges. Since wz is also an edge, triangle-freeness gives

`za=zc=ac=0` in J.

If a were regular, then relative to support E it would need at least two J-neighbours in {z,c,d}; but za=ac=0 leaves only d, impossible. Therefore kappa_a>=1. Similarly kappa_c>=1.

Thus the pair D,E already consumes the entire available excess:

- kappa_a=kappa_c=1;
- every other vertex of R has kappa=0.

The same argument applied to any regular w in W shows that a and c are the unique petals it may use: any additional J-neighbour u outside {z,a,c} is regular; triangle-freeness with wz,wa,wc would give uz=ua=uc=0, and then u would have at most one J-neighbour in D or E, contradicting (1).

Hence every regular w in W has, among R,

`N_J(w) subset {z,a,c}`

and contains all three z,a,c.

### 3.3 Every third support contains z

Let T be another support. Suppose z notin T.

At least one regular w in W lies outside T because |W|=6 and |T|=3. By (1), w needs at least two J-neighbours in T. Its only available J-neighbours are z,a,c, and z is not in T, so necessarily

`a,c in T`.

Thus T={a,c,u} for some u.

But z is regular and lies outside T. We have za=zc=0, so z has at most one J-neighbour in T, namely u. This violates (1) for z relative to T.

Therefore every support contains z.

Hence if any pair of supports intersects in exactly one point, that point is common to all ten supports.          (3)

## 4. The remaining 2-intersecting case also has a common point

Assume no two distinct supports meet in exactly one point. By (2), every two distinct supports then intersect in at least two vertices.

For 3-subsets, a standard direct classification applies. Take two distinct supports

`D={a,b,c}`, `E={a,b,d}`.

Any further support meeting both D and E in at least two vertices either contains a or b, or is one of the complementary triples on the four-set {a,b,c,d}. Consequently either

1. one of a,b belongs to every support; or
2. all four triples of the four-set {a,b,c,d} occur.

The second alternative is impossible.

Let Q={a,b,c,d}. Since total core excess is at most2, at least two vertices q in Q are regular. Each such q lies outside the support Q\{q}; by (1),

`d_(J[Q])(q)>=2`.                                          (4)

On the other hand, there are seven vertices outside Q, at least five regular. Choose one regular w outside Q. Because w lies outside each of the four triples Q\{q}, condition (1) forces w to have at least three J-neighbours in Q. Triangle-freeness makes those three neighbours an independent 3-set in J[Q].

If a graph on four vertices has an independent 3-set, all its edges are incident with the fourth vertex, so at most one vertex can have degree at least2. This contradicts (4) for at least two regular q in Q.

Therefore the four-triple alternative is impossible.

Thus in every case:

> all ten supports share one common core vertex z.          (5)

## 5. D14 kills the common-point family

For v in R let lambda_v be the number of the ten low supports containing v. Then

`sum_R lambda_v=30`.

By (5),

`lambda_z=10`.

The set `{p} union C` is a target K11: p is the original degree-13 pivot and C is the ten-point low target clique. It contributes55 target edges.

Take any low support

`D={z,u,v}`.

The 14-point set

`{p} union C union {z,u,v}`

contains

- the55 edges of the K11;
- lambda_z+lambda_u+lambda_v shell-to-core edges;
- e_H(D) internal core edges.

The inherited D14 cap is69, hence

`55+lambda_z+lambda_u+lambda_v+e_H(D)<=69`.

Since alpha(H[R])<=2, the triple D is not independent, so e_H(D)>=1. With lambda_z=10,

> `lambda_u+lambda_v<=3`.                                  (6)

In particular every non-z vertex that occurs in a support has lambda<=2.

The ten supports contribute20 petal incidences outside z. There are exactly ten vertices in R\{z}, each of petal multiplicity at most2 by (6). Therefore equality is forced globally:

> every vertex of R\{z} has lambda=2.                      (7)

But then for every support D={z,u,v},

`lambda_u+lambda_v=4`,

contradicting (6).

## 6. Conclusion

The c=10 high-c single-class state is impossible:

> `c=10` is EMPTY.

Together with the c=7, c=8 and c=9 closures, the entire all-d3 / single missing-vertex high-c sector `c>=7` of the q36 f=2, 2K1, a_F=0 branch is now closed.