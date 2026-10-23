# q36 compensated d4 branch — support-class collapse

Status: `PROVED REDUCTION` under `Q36_COMPENSATED_K49_NORMAL_FORM.md`, `Q36_D4_COMPENSATED_DYNAMICS.md`, and the standard all-pivot row-closure theorem.

This eliminates every q36 compensated d4 state with two or three distinct zero-column supports. Hence every survivor has exactly one zero-support class.

## 1. Setup

Use the d4 compensated notation:

- four decorated shell vertices S form a target K4;
- nine regular columns U form a target K9;
- zero columns are the u in U with no target cross edge to S;
- every zero-column support is a K4 of H-degree12 vertices;
- distinct zero-column supports are disjoint and target-anticomplete;
- there are at most three distinct support classes.

Let the distinct supports be `D_1,...,D_k`, each of size4. Put

`L=H\(D_1 union ... union D_k)`.

Because each D_i is a zero-defect support,

`e_F(S,D_i)=0`.                                             (1)

Every vertex of D_i has H-degree12 and internal degree3. Since the D_i are pairwise anticomplete, each vertex of D_i has exactly9 H-neighbours in L. Therefore

`e_H(D_i,L)=36`                                             (2)

for every i.

The four S-vertices each have a 9-point core row, and by (1) all those rows lie in L. Thus

`sum_(v in L)e_F(v,S)=36`.                                  (3)

The CORE211 total internal excess is2 and every D_i vertex has excess0, so

`sum_(v in L)kappa_v=2`.                                   (4)

Define

`w_v=kappa_v+e_F(v,S)`.

Then from (3)--(4)

`sum_(v in L)w_v=38`.                                      (5)

For every support D_i, row closure gives

`e_H(v,D_i)<=w_v`                                          (6)

for every `v in L`.

## 2. Three support classes are impossible

Assume k=3. Then `|L|=23`.

Fix v in L. If v were not complete to any of D1,D2,D3, choose

`d_i in D_i\N_H(v)`

for i=1,2,3. Because the D_i are pairwise anticomplete,

`{v,d_1,d_2,d_3}`

would be an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore v is complete to at least one D_i. By (6),

`w_v>=4`

for every v in L.

Hence

`sum_L w_v>=23*4=92`,

contradicting (5), which gives38.

Thus

> k!=3.

## 3. A threshold lemma for two classes

We use the following elementary extremal fact.

### Lemma

Let `x_1,...,x_27` be integers in `{0,1,2,3,4}` with

`sum x_i<=38`.

Then at least153 unordered pairs `{i,j}` satisfy

`x_i+x_j<=3`.                                               (7)

### Proof

Equivalently, at most198 pairs satisfy `x_i+x_j>=4`.

For fixed total weight, shifting one unit from a smaller positive coordinate to a larger coordinate below4 cannot decrease the number of pairs with sum at least4: the larger coordinate has a superset of the threshold-neighbour set of the smaller coordinate. Repeating this compression leaves all but at most one/two residual units concentrated at weight4.

With total at most38, the extremal compressed configurations have nine 4's and residual weight at most2 among the other18 vertices. They create at most

`C(9,2)+9*18=36+162=198`

pairs of sum at least4.

Since `C(27,2)=351`, at least

`351-198=153`

pairs satisfy (7).

## 4. Two support classes are impossible

Assume k=2 and write

`a_v=e_H(v,D_1)`,
`b_v=e_H(v,D_2)`

for v in L. Now `|L|=27`.

By (2),

`sum_L a_v=sum_L b_v=36`.                                  (8)

By row closure (6),

`a_v<=w_v`, `b_v<=w_v`.

Put

`x_v=max(a_v,b_v)`.

Then `0<=x_v<=4` and, by (5),

`sum_L x_v<=38`.                                           (9)

Apply the threshold lemma. There are at least153 unordered pairs `{v,w}` in L with

`x_v+x_w<=3`.

For any such pair,

`a_v+a_w<=3`, `b_v+b_w<=3`.

If vw were a target nonedge, then in each four-set D_i the union of the two neighbourhoods has size at most3. Hence choose

`d_1 in D_1\(N(v) union N(w))`,
`d_2 in D_2\(N(v) union N(w))`.

The two D-blocks are anticomplete, and vw is a nonedge, so

`{v,w,d_1,d_2}`

would be an independent4-set in H. Contradiction.

Therefore all of these at least153 pairs are target edges of H[L].

But exact edge accounting gives

`e(H[L])=211 - 2*C(4,2) - 2*36`

`=211-12-72=127`.

Contradiction.

Thus

> k!=2.

## 5. Single-class residual

Every surviving q36 compensated d4 state has exactly one zero-column support D, a K4 of H-degree12 vertices.

Let its multiplicity be m. The D14 repivot cap from `Q36_D4_COMPENSATED_DYNAMICS.md` gives

`m<=4`.

Since there are nine columns total and at least one zero column,

`m=n_0 in {1,2,3,4}`,

with the number of active columns

`a=9-m in {8,7,6,5}`.

Thus the entire q36 d4 ceiling branch has collapsed to four channels:

- `(m,a)=(4,5)`;
- `(3,6)`;
- `(2,7)`;
- `(1,8)`.

If p is chosen with maximal zero-column count among q36 tau=4 pivots, the tertiary inequality further gives

`b>=a+1-m=10-2m`,

where b is the number of active columns whose support meets D.

Together with the D14 support-incidence cap

`J<=18-4m`,

this yields:

- m=4: `b>=2`, `J<=2`, hence exactly two active supports meet D, each in one point, and the D-repivot saturates `G'=14`;
- m=3: `b>=4`, `J<=6`, so `12<=G'<=14`;
- m=2: `b>=6`, `J<=10`, so `10<=G'<=14`;
- m=1: all eight active supports meet D, so `G'>=8`.

These four channels are the new exact q36 d4 frontier.