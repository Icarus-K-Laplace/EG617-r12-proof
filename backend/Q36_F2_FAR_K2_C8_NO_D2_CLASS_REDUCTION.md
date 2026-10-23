# q36 f=2 far-target-K2 — c=8 no-d2 class reduction and low-allowance closure

Status: `PROVED REDUCTION` under `Q36_F2_SHELL_LEDGER_REDUCTION.md`, common-S row closure, q36 lexicographic maximality, inherited D14/K4-freeness, and `alpha(H)<=3`.

This treats c=8 with no d2 row, so all eight low-clique owners are d3 rows.

## 1. Exact shell data

Here

- `c=8`;
- `|X|=3`;
- `mu=0` (far pair F is a target K2);
- `delta=8`;
- every low owner belongs to a d3 missing-set class.

The f=2 shell ledger gives

`G=6+a_F-nu`.                                               (1)

For an active decorated vertex x,

`A_x=n_x+nu_x+g_x-(8+a_F)`.                                (2)

The general no-d2 reduction already proves that there are at most two active d3 classes, and if two occur then

`A_x+A_z<=1`.                                                (3)

## 2. Two active classes are impossible

Assume x,z are the two active classes and y is the third decorated vertex. Let

`n_x+n_z=8`.

The only allowance patterns allowed by (3) are `(0,0)` and `(1,0)` up to order. Keep the general symbols A_x,A_z for the calculation.

From (2),

`g_x=8+a_F+A_x-n_x-nu_x`,
`g_z=8+a_F+A_z-n_z-nu_z`.

Using `n_x+n_z=8`,

`g_x+g_z = 8+2a_F + A_x+A_z -(nu_x+nu_z)`.                 (4)

Subtracting from (1),

`g_y = -2-a_F-(A_x+A_z) + (nu_x+nu_z-nu)`.                 (5)

For three vertices x,z,y,

`nu_x+nu_z-nu = 1_{xz in M}`,

which is at most1. Since `A_x+A_z>=0` and `a_F>=0`, (5) gives

`g_y<=-1`.

But y belongs to the decorated set X, so `g_y>=1`. Contradiction.

Therefore

> all eight d3 owners belong to one common missing-set class. (6)

## 3. Allowance bound for the unique class

Let x be the unique active decorated vertex and let y,z be the two inactive decorated vertices. Then `n_x=8` and

`A=nu_x+g_x-a_F`.                                           (7)

Let

`rho=1_{yz in M}`.

Since `nu=nu_x+rho`, subtracting g_x from the total decoration gives

`g_y+g_z = G-g_x = 6-A-rho`.                               (8)

Both y,z are decorated, hence `g_y,g_z>=1`. Therefore

> `A+rho<=4`.                                                (9)

In particular

> `A<=4`, and if yz is a missing edge then `A<=3`.           (10)

Thus only allowance levels 0,1,2,3,4 are possible.

## 4. Allowance zero is impossible

For A=0 every support has defect0. Hence every support is

- a target K3;
- core-excess zero;
- target-anticomplete to the common missing set S=F union {x}.

A repeated support would repivot to q36 while retaining the two inactive decorated shell vertices and inserting three globally decorated support vertices, increasing tau. Hence all eight supports are distinct.

Proper overlap has cost2>A, so distinct supports are disjoint. Common-S row closure gives zero target cross edges between distinct supports.

Choosing one point from each of any four support blocks gives an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore

> A=0 is EMPTY.                                              (11)

## 5. Allowance one: at most three distinct support classes

Let A=1.

Proper overlap is impossible, so distinct support classes are disjoint. Joint row closure gives at most one target cross-edge between any two distinct classes.

Suppose four distinct support classes existed. Choose independently and uniformly one point from each of four triples. The expected number of target edges among the six chosen pairs is at most

`6*(1/9)=2/3<1`.

Hence some choice has no target edges, giving an independent4-set in H. Contradiction.

Thus

> there are at most three distinct support classes.          (12)

If a support repeats, full defect1 would repivot to q36 and increase tau, so every repeated support has defect0 and is a pure target K3. D14 with the target K11 shell base gives multiplicity at most3.

To carry eight owners with at most three classes and multiplicity at most3, there must be exactly three support classes with owner multiplicities

> `3+3+2`.                                                   (13)

All three are repeated defect-zero target K3s.

Because their non-missing allowance is zero, common-S row closure makes the three K3 blocks pairwise target-anticomplete.

## 6. The 3+3+2 equality state is impossible

Choose one point from each of the three K3 blocks. They form an independent3-set in H.

Let v be any core vertex outside their nine-point union. If v failed to be target-complete to each of the three blocks, choose in every block a target-nonneighbour of v. Since the blocks are pairwise target-anticomplete, these three choices together with v form an independent4-set, contradicting `alpha(H)<=3`.

Therefore every outside core vertex must be target-complete to at least one of the three target K3 blocks.

But inherited core K4-freeness forbids a core vertex from being target-complete to a target K3. Hence no outside core vertex can exist.

The core has 35 vertices while the three blocks contain only9, contradiction.

Therefore

> A=1 is EMPTY.                                              (14)

## 7. Current no-d2 frontier

The c=8 far-K2 no-d2 branch has now been reduced to

- one common d3 missing-set class containing all eight owners;
- allowance

`A in {2,3,4}`.

No fixed-remainder or pure-d2 alpha-two argument is used in this file.