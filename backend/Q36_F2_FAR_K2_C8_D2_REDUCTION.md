# q36 f=2 far-target-K2 — c=8 with one d2 row

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_D2_GLOBAL_REDUCTION.md`, the master f=2 ledger, common-S row closure, CORE211, inherited D14, lexicographic q36 maximality, and `alpha(H)<=3`.

This treats c=8 and n2=1. It proves that the seven d3 owners form one missing-set class and that its allowance is in {2,3,4}.

## 1. Setup

Here c=8 and |X|=3. The far pair F is a target K2. Let D0 be the unique d2 support.

By `Q36_F2_FAR_K2_D2_GLOBAL_REDUCTION.md`:

- `a_F=0`;
- D0 is a pure target K2 of globally regular vertices;
- D0 is target-anticomplete to F and to every decorated shell vertex in X;
- the remaining seven low owners are d3 rows;
- d3 rows use at most two decorated missing vertices.

The set

`B0={p} union C union F`

is a target K11.

For a d3 class with active decorated vertex x let A_x denote its common-S allowance.

If two classes x,z occur, the general class-sum bound and |X|=3 give

`A_x+A_z<=nu-2<=1`.                                        (1)

Thus the two-class allowance pattern is either (0,0) or (1,0), up to order.

## 2. Allowance-zero classes have at most two owners

Let x be a class with A_x=0.

Every support E in this class has defect0, hence

- H[E]=K3;
- kappa(E)=0;
- e_F(F union {x},E)=0;
- its repivot has q=36.

A repeated support is impossible by lexicographic maximality: repivoting removes x, retains the other two decorated vertices of X, and a repeated support would insert three globally decorated core vertices, raising tau above3.

Proper overlap is impossible because h(3-h)=2>A_x. Hence all supports in the class are distinct, disjoint, and pairwise target-anticomplete.

Moreover row closure against the pure d2 support D0 gives

`e_H(D0,E)<=kappa(E)+e_F(F,E)=0`.

Thus D0 is target-anticomplete to every allowance-zero support.

If three such supports existed, choosing one vertex from D0 and one vertex from each of the three K3 supports would give an independent4-set in H, contradicting alpha(H)<=3.

Therefore

> an allowance-zero d3 class has at most2 owners.             (2)

## 3. Allowance-one classes have at most two distinct supports

Let z be a class with A_z=1.

Proper overlap is again impossible because the overlap cost2 exceeds the allowance. Distinct support classes are disjoint, and common-S row closure gives at most one target edge between any two distinct supports.

For each support E in this class, row closure against D0 gives

`e_H(D0,E)<=kappa(E)+e_F(F,E)<=Delta(E)<=1`.                (3)

Suppose three distinct supports E1,E2,E3 existed. Choose independently and uniformly

- one vertex from the 2-set D0;
- one vertex from each Ei.

The expected number of target edges among the four selected vertices is at most

`3*(1/9)+3*(1/6)=5/6<1`:

- the three Ei--Ej pairs contribute at most1/9 each;
- the three D0--Ei pairs contribute at most1/6 each.

Hence some choice has zero target edges, an independent4-set in H. Contradiction.

Thus

> an allowance-one class has at most2 distinct support classes. (4)

## 4. Repeated allowance-one supports have multiplicity at most three

If an allowance-one support E repeats, full defect1 would keep q=36 while retaining the two inactive decorated shell vertices and inserting three decorated support vertices, increasing tau. Hence a repeated support has defect0.

Therefore every repeated allowance-one support is a pure target K3 with

- kappa(E)=0;
- e_F(F union {z},E)=0;
- q=35.

Let its owner multiplicity be m. The K11 base B0 and D14 give

`3m + O_E + e_F(F,E) + e_H(E) <=14`.

Dropping the nonnegative terms O_E and e_F(F,E), and using e_H(E)=3, gives

`3m+3<=14`,

hence

> m<=3.                                                       (5)

## 5. Two d3 classes are impossible

Assume two classes occur.

### Pattern (0,0)

By (2), each class has at most2 owners, so together they carry at most4 of the seven d3 owners. Impossible.

### Pattern (1,0)

The allowance-zero class has at most2 owners, so the allowance-one class has at least5 owners.

By (4) it uses at most two distinct supports, and by (5) each repeated support has multiplicity at most3. Thus the only possible owner distributions are 3+2 or 3+3, so both support classes are repeated pure K3s.

Let E1,E2 be those two repeated K3 supports and let E0 be any support from the nonempty allowance-zero class.

We have:

- D0 is target-anticomplete to E0,E1,E2;
- E1 and E2 are target-anticomplete because a repeated defect-zero support has zero common-S cross allowance;
- for v in E0, row closure against Ei gives
  `e_H(v,Ei)<=kappa_v+e_F(v,F union {z})<=1`,
  because E0 has kappa_v=0, is target-anticomplete to F and to its own active missing vertex, and can meet the other active vertex z at most once.

Hence

`e_H(E0,Ei)<=3` for i=1,2.

Choose uniformly one vertex from each of the four blocks

`D0, E0, E1, E2`.

All pair contributions vanish except E0--E1 and E0--E2, whose expected contributions are at most1/3 each. Total expectation is at most2/3<1. Thus some choice is an independent4-set in H, contradiction.

Therefore:

> two d3 missing-set classes are impossible.                 (6)

## 6. A single class cannot have allowance0 or1

Now all seven d3 owners belong to one class.

- If A=0, every support is a distinct disjoint K3 and four supports already yield an independent4-set in H. Impossible.
- If A=1, by (4) there are at most two distinct support classes, and by (5) each class has multiplicity at most3. Hence the class can carry at most6 owners, not seven.

Therefore

> A>=2.                                                       (7)

## 7. Upper bound A<=4

Let x be the unique active decorated vertex. Since n_x=7 and |X|=3,

`A=7+nu_x+g_x-8=nu_x+g_x-1`.

Write Y=X\{x}. The exact shell ledger is

`G=7-nu`.

Both Y-vertices are decorated, so `G_Y>=2`; hence

`g_x<=5-nu`.

Therefore

`A<=nu_x+4-nu<=4`.                                          (8)

Combining (7)--(8):

> every c=8 far-K2 candidate with one d2 row has exactly one d3 missing-set class and allowance
>
> `A in {2,3,4}`.                                           (9)

This file is a reduction, not a full closure of those three terminal allowance levels.