# q36 f=2, 2K1 far, a_F=0 — full closure of the c=8 mixed d2/d3 sector

Status: `PROVED` under `Q36_F2_2K1_A0_REDUCTION.md`, the low-allowance d3 theorems, row closure, CORE211, inherited D14, the all-pivot minimum-degree theorem, and `alpha(H[R])<=2`.

Together with `Q36_F2_2K1_A0_HIGH_C_SINGLE_CLASS_NORMAL_FORM.md`, this closes the entire c=8 branch.

## 1. Setup

Let c=8 and suppose at least one low row has missing degree2. Put n2>=1 and n3=8-n2. The decorated shell set X has size3.

The fixed 11-point remainder R satisfies `alpha(H[R])<=2` and total core excess at most2.

## 2. There is only one active d3 missing class

Suppose two decorated vertices x,z are used by d3 rows and let y be the third, inactive, decorated vertex.

For an active vertex u write

`A_u=n_u+nu_u+g_u-7`

for its exact d3 common-S allowance. Since n_x+n_z=n3, the shell ledger `G=5+n2-nu`, and `nu_x+nu_z=2nu-nu_y`, we get

`A_x+A_z = nu-nu_y-g_y-1`.                                (1)

The right side is always negative:

- for nu=0 or1 this is immediate from g_y>=1;
- for nu=2 the graph M[X] is P3, hence nu_y>=1, giving at most -1;
- for nu=3 the graph is K3, so nu_y=2, again giving at most -1.

But allowances are nonnegative. Contradiction.

Therefore all d3 rows use one active missing vertex x. Let y,z be the two inactive decorated shell vertices.

## 3. The inactive pair gives a K11-minus-edge D14 cap

Both y and z are target-adjacent to every low owner. Thus

`{p} union C union {y,z}`

is a target K11 when yz is a target edge and a K11 minus one edge when yz is missing.

For every triple T subset R, ignoring all favourable edges from y,z into T, the 14-point inherited cap gives

`54 + lambda(T) + e_H(T) <=69`,

where lambda_v is the number of the eight low supports containing v.

Since `alpha(H[R])<=2`, every triple spans at least one target edge. Hence

> `lambda(T)<=14` for every triple T subset R.               (2)

## 4. A d2 support again creates Q and B

Choose a d2 support D={u,v}.

For every regular w outside D, the d2 row-closure inequality gives `e_H(w,D)=0`. The pair D must be a target K2, otherwise a regular outside vertex gives an independent triple.

Let Q be the set of regular vertices in R\D. Then

- `|Q|>=7`;
- Q is a target clique;
- Q is target-anticomplete to D.

Put `B=R\Q`. Then `|B|<=4` and D subset B.

For any d3 support T, if T contained two Q-vertices, choose regular q in Q\T. Row closure for T gives

`e_H(q,T)<=e_F(q,x)<=1`,

while clique Q gives at least2 target edges into T. Contradiction.

Thus every d3 support contributes at least two incidences to B.

The d2 rows contribute at least two incidences through the chosen D. Hence

`lambda(B)>=16`.                                           (3)

If |B|<=3, taking a triple containing B gives lambda at least16, contradicting (2). Therefore

> `|B|=4`.                                                   (4)

## 5. Equality in CORE211 fixes the exceptional block

Since B consists of D plus exactly two vertices b1,b2 outside D, those two vertices are precisely the nonregular vertices of R\D. The total core excess is at most2, so equality is forced:

- `kappa(D)=0`;
- `kappa_b1=kappa_b2=1`.

Row closure for the d2 support gives `e_H(b_i,D)<=1`. Hence each b_i misses at least one endpoint of D. Because every q in Q is target-nonadjacent to D, `alpha(H[R])<=2` forces each b_i to be target-adjacent to every q in Q: otherwise b_i together with a missed endpoint of D and a missed q would be an independent triple.

Therefore both b1,b2 are target-complete to Q.

## 6. Every d3 support contains the whole d2 support D

Take a d3 support T and a regular q in Q\T. The row-closure bound gives

`e_H(q,T)<=e_F(q,x)<=1`.

But q is target-adjacent to every vertex of `Q union {b1,b2}`. Thus T contains at most one vertex of that set.

Since T has size3 and

`R = D disjoint_union {b1,b2} disjoint_union Q`,

T must contain both endpoints of D.

Hence every d3 support contains D.                               (5)

## 7. Decoration overflow eliminates all n2

Let e be1 if yz is a missing edge and0 otherwise. Since x is the unique active d3 missing vertex, its allowance A satisfies

`A + g_y + g_z = 6-e`.                                     (6)

The regular/decorated missing-edge inequality for a low owner and x implies A>=3. Since y,z are decorated, `g_y+g_z>=2`. Thus in every case at least two units of old shell decoration are retained when a d3 owner is repivoted.

Each endpoint of D lies in every one of the n3 d3 supports and in at least one d2 support. Since its core excess is zero by section5, its global decoration is at least n3.

Therefore any d3 repivot has

`G' >= 2 + 2 n3`.                                         (7)

Every q<=36 shell satisfies `G'<=14` by the inherited 14-point missing-edge floor.

### n2=1

Then n3=7 and (7) gives `G'>=16`, contradiction.

### n2>=3

By d2 rigidity, all d2 rows share one repeated pure K2 support, necessarily D. Thus each endpoint of D is adjacent to all eight low owners and has decoration at least7. Hence `G'>=2+14=16`, contradiction.

### n2=2

If the two d2 rows repeat D, the same decoration overflow applies.

Suppose they use distinct supports D,E. Distinct d2 supports are disjoint. We claim E subset B. If E met Q, choose regular q in Q\E. Row closure for E gives `e_H(q,E)=0`, but q is adjacent to every Q-vertex, contradiction. Thus E is disjoint from Q and, since it is disjoint from D,

`E={b1,b2}`.

But `kappa(E)=2`, while the d2 allowance in the `2K1,a_F=0` branch is at most1. Contradiction.

Thus n2=2 is also impossible.

## 8. Conclusion

No c=8 mixed d2/d3 candidate exists:

> `c=8, n2>=1` is EMPTY.

The all-d3 c=8 channel was already closed by `Q36_F2_2K1_A0_HIGH_C_SINGLE_CLASS_NORMAL_FORM.md`. Hence the entire q36 f=2, 2K1, a_F=0, c=8 layer is empty.