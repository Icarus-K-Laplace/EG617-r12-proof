# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 repeated two-edge sharp reduction

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_A4_MULT2_TWOEDGE_REDUCTION.md`, common-S row closure, inherited D14, q36 lexicographic maximality, `alpha(F)<=4`, `alpha(H[U])<=2`, and the already proved elimination of support multiplicity at least3.

This eliminates every repeated two-edge multiplicity-two weight pattern except one exact `(0,0,2)` owner architecture.

## 1. Setup

Let D={a,b,c} be the repeated two-edge support with edges ac,bc and unique nonedge ab. The previous reduction proves

- `1<=w(D)<=2`;
- `w_c>=1`;
- all five external owners intersect D;
- at least four are one-point overlaps, all anchored at a or b;
- at most one owner has two-point overlap;
- `O_D in {5,6}`.

Thus the only weight patterns, up to swapping a,b, are

- `(0,0,1)`;
- `(0,0,2)`;
- `(1,0,1)`.

(The symmetric `(0,1,1)` is covered by swapping a,b.)

## 2. A fixed endpoint supports at most one one-point class

We use this repeatedly.

Consider two distinct one-point support classes E1,E2 both anchored at a.

If `w_b=0`, then b lies outside each support and is target-anticomplete to all petals by row closure. Since ab is a target nonedge, every petal in an a-anchor support must be target-adjacent to a; otherwise {a,b,petal} is an independent triple.

If any petal-cross pair between E1 and E2 were a target nonedge, b together with that pair would be an independent triple. Hence the two petal pairs are joined by a complete K2,2.

For a petal u of E1, the support E2 contains a plus its two petals. Therefore u has at least three target edges into E2: the edge ua and the two forced petal-cross edges. Row closure gives `w_u>=3`, and the same holds for the other petal of E1. This already makes `Delta(E1)>4`.

Hence when the opposite endpoint has weight0, there is at most one support class at a. The symmetric statement holds at b.

When the opposite endpoint has weight1, the same conclusion follows using c when `w_c=1`: the edge c-a (or c-b) exhausts c's row-closure budget, making c target-anticomplete to all petals; the forced complete petal cross graph then gives both petals weight at least2, and any nonclique support exceeds allowance4 while a K3 gives a q36 repivot with the shared D-point and positive petals decorated, increasing tau.

Thus in every weight pattern considered below:

> each endpoint anchor supports at most one distinct support class, of owner multiplicity at most2.   (1)

## 3. Pattern (0,0,1) is impossible

Here c has weight1 and both endpoints have weight0.

The edge c-a (respectively c-b) consumes c's full row-closure budget against an a-anchor (respectively b-anchor) support, so c is target-anticomplete to all petals of every one-point support.

By (1), each endpoint contributes at most2 owner incidences.

Moreover endpoint classes at a and b cannot coexist. If they did, c would be target-anticomplete to both petal pairs; alpha-two would force a complete K2,2 petal cross graph. Every petal would then have weight at least2. In an a-anchor support the two petals are both adjacent to a because b has weight0. Thus the support has at least two internal target edges and total defect at least4; if it is a K3 this is a q36 repivot with the shared a-point and both positive petals decorated, increasing tau, while if nonclique its defect exceeds4.

Therefore all one-point owners occupy at most one support class, capacity2, but at least four are required. Contradiction.

Hence `(0,0,1)` is empty.                                      (2)

## 4. Pattern (1,0,1) is impossible

Here `w_a=1`, `w_b=0`, `w_c=1`.

By (1), each endpoint anchor again has at most one support class.

An a-anchor support has both petals target-adjacent to a because b has weight0. The edge c-a exhausts c's weight1, so c is anticomplete to its petals.

For a b-anchor support, the edge c-b likewise makes c anticomplete to its petals.

If an a-anchor class and a b-anchor class coexisted, alpha-two with c would force a complete K2,2 petal cross graph. Each petal of the a-anchor support would then have weight at least2 from its two cross edges. Together with the shared point a of weight1, that support has defect at least5, impossible.

Thus at most one endpoint class can occur, capacity2, again contradicting the requirement of at least four one-point owners.

Therefore `(1,0,1)` and, symmetrically, `(0,1,1)` are empty.  (3)

## 5. Pattern (0,0,2): exact owner architecture

Now assume

`(w_a,w_b,w_c)=(0,0,2)`.

By (1), each endpoint anchor has at most one distinct class, so the total one-point owner capacity is at most4.

### O_D=5 is impossible

If `O_D=5`, there is no two-point owner and all five external owners are one-point overlaps. Capacity4 is insufficient.

Hence

> `O_D=6`.                                                     (4)

The D14 inequality from the previous reduction is

`O_D+e_F(F,D)<=6`,

so (4) forces

> `e_F(F,D)=0`.                                               (5)

Exactly one external owner has two-point overlap, and the remaining four are one-point owners.

Since each endpoint class carries at most2 owners, those four one-point owners must split exactly as

> one a-anchor class of multiplicity2 and one b-anchor class of multiplicity2.   (6)

Finally, the unique two-point overlap can only use {a,b}. A pair containing c and one endpoint leaves the other zero-weight endpoint outside the support while adjacent to c, violating row closure. The pair {a,b} leaves c outside; c has weight2 and its two target edges ca,cb exactly fit its row-closure budget.

Therefore the unique remaining architecture is:

- D={a,b,c}, edges ac,bc, nonedge ab;
- weights `(w_a,w_b,w_c)=(0,0,2)`;
- one a-anchor support class of multiplicity2;
- one b-anchor support class of multiplicity2;
- one singleton two-point-overlap support on {a,b};
- `O_D=6` and `e_F(F,D)=0`.

No other repeated two-edge multiplicity-two state survives.

This exact `2+2+1` architecture is the sole remaining repeated-support terminal in the c8 one-d2 A4 layer.