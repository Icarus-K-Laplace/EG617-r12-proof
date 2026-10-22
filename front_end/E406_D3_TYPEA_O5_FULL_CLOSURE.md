# E406 d=3 Type-A: complete O=5 closure

Status: `PROVED EMPTY` for the complete Type-A `O=5` layer under the d=3 q31 platform contract. `E406` remains `OPEN`.

Dependencies:

- `E406_D3_FOUR_TRIANGLE_COMPRESSION.md`;
- `E406_D3_REMAINDER_SATURATION.md`;
- `E406_D3_O5_COMPRESSION.md`;
- `alpha(C)<=4`, `omega(C)<=11`;
- the pure-class clique lemma already used in the O5 compression.

Notation follows the previous files. The four pairwise anticomplete support triangles are `T_1,...,T_4`; `H` is the 35-point remainder. For a vertex x in H, `k_x` is its number of full support rows, `r_x` its partial support incidence count,

`O=sum(k_x-1)`, `R=sum r_x`,

and

`3O+R=15+eta`.

For Type A, at most one support triangle is defective. Write `eta` for its internal core-excess contribution and `xi` for its shell-D cross defect, with `eta+xi<=1`.

We close every state with `O=5`.

## 1. The eta=0 branch is already covered by the H-side O5 proof

If `eta=0` and `O=5`, then `R=0`. The H-side contract is exactly

- four pairwise anticomplete K3 support rows;
- `e(H)=152`;
- total H-core excess4;
- 120 T-H incidences;
- every support row has exactly10 full H-vertices.

These are exactly the hypotheses used in Section 3 of `E406_D3_O5_COMPRESSION.md` to eliminate the Type-B `O=5` layer. That proof uses only the H-side row/pure-class/excess data, not the Type-B shell-side decoration pattern. Hence it applies verbatim here.

Therefore every Type-A `eta=0, O=5` state is empty.

It remains to treat `eta=1`. Then

- `R=1`;
- `e(H)=151`;
- total H-core excess is3;
- every H-vertex satisfies `eps_x+s_D(x)=1`, hence `eps_x in {0,1}`.

The single partial support incidence is carried by a singleton-full-row vertex.

## 2. Exact eta=1 O5 families

The membership analysis in `E406_D3_O5_COMPRESSION.md`, together with the triple-transversal capacity bound, leaves only the following three families.

### Family A

Pure profile `(6,8,8,8)`, with exactly

- one triple-full vertex of type `(6,8,8)`;
- three double-full vertices;
- one singleton-full partial carrier.

### Family B

Pure profile `(7,7,8,8)`, with exactly

- one triple-full vertex of type `(7,7,8)`;
- three doubles;
- one singleton-full partial carrier.

### Family C

Pure profile `(6,7,8,8)`, with

- five double-full vertices;
- one singleton-full partial carrier.

No other eta=1,O=5 membership profile survives the preceding O5 compression.

## 3. The surviving triple-full vertices spend one excess unit

Consider a triple-full vertex x with pure-row sizes `(6,8,8)` or `(7,7,8)`.

If `eps_x=0`, then its H-degree is3. Let `A_i` be its missing set in the three pure classes. The triple-transversal lemma requires enough cross edges among the three missing sets to hit every independent transversal.

Using the pure-vertex external-degree capacities, the maximum available number of such cross edges is one smaller than the transversal lower bound in both patterns. Thus `eps_x=0` is impossible.

Hence every surviving triple-full vertex has

`eps_x=1`.      (TRIPLE-ONE)

This is the only fact from the detailed triple calculation needed below.

## 4. Family B is impossible

The `(7,7,8)` triple already consumes one of the three H-excess units by (TRIPLE-ONE).

Every remaining double lies on a pair of rows of type

- `(7,7)`,
- `(7,8)`, or
- `(8,8)`.

An `(8,8)` double costs at least6 units by the pair-overlap lemma and is impossible outright. Under a global excess budget at most3, every `(7,7)` or `(7,8)` double must itself have positive excess.

There are three doubles, so together with the triple they require at least4 H-excess units, contradicting the exact total3.

Therefore Family B is empty.

## 5. Family A is impossible

Let A denote the 6-row and B,C,D the three 8-rows. The singleton partial carrier cannot be full to an 8-row: a singleton full to row i is complete to `P_i union T_i`, so `|P_i|<=7`. Hence the singleton is full to A.

The required non-pure full-row degrees are `(4,2,2,2)`. Removing the singleton leaves degree demand

`(3,2,2,2)`

for the triple plus the three doubles.

The triple has type `(6,8,8)`, so after removing it the three doubles have degree sequence

`(2,1,1,2)`

up to permuting B,C,D.

An `(8,8)` double costs at least6, exceeding the two excess units left after the triple. Thus every double would have to be incident with the 6-row A.

But A has remaining double-degree only2, whereas the three doubles contribute six endpoints. After using the two A-incidences, the remaining two endpoints necessarily form an `(8,8)` double. Contradiction.

Hence Family A is empty.

## 6. Family C: exact double multigraph

Let A,B,C,D denote pure-row sizes

`6,7,8,8`.

An `(8,8)` double is impossible because its pair-overlap cost is at least6>3. Let `w` be the singleton partial carrier. Since a singleton cannot be full to an 8-row, w is full to A or B.

We use the following elementary equality consequences of the pair-overlap lemma.

### 6.1 A 7-8 double of excess1 with no remaining pure excess

Let x be full to a 7-class P_B and an 8-class P_C. Since x has six support-triangle neighbours and `eps_x=1`,

`d_H(x)=7`.

Let a,b be the numbers of missed vertices in P_B,P_C and h the number of H-neighbours outside these pure classes. Then

`a+b=8+h`.

The missing sets are completely joined. Their pure-vertex excess cost is at least

`a[b-3]_+ + b[a-2]_+`.

If `a>=1`, this quantity is at least4. Hence whenever at most one global excess unit remains outside x, necessarily

`a=0, b=8, h=0`,

so

`N_H(x)=P_B`.      (78-EQ)

### 6.2 A 6-8 double of excess0 with at most two remaining excess units

Let z be full to a 6-class P_A and an 8-class. If `eps_z=0`, then `d_H(z)=6`. With analogous notation,

`a+b=8+h`,

and the pure-set excess cost is at least

`a[b-4]_+ + b[a-2]_+`.

If `a>=1`, this lower bound is at least3. Thus under a remaining global budget at most2,

`a=0,b=8,h=0`,

hence

`N_H(z)=P_A`.      (68-EQ)

### Case C1: w is full to the 6-row A

After removing w, the five doubles have row degrees

`(3,3,2,2)`.

With the C-D `(8,8)` pair forbidden, the degree equations force exactly two 7-8 doubles and one A-B double. In particular there are exactly two bad 7-8 doubles.

Each 7-8 double must have positive excess, hence (because every H-excess is0 or1) has excess exactly1. Together they consume two of the three H-excess units, so at most one unit remains elsewhere. By (78-EQ), both have

`N_H(x_1)=N_H(x_2)=P_B`.

They are nonadjacent and anticomplete to

`U=H\(P_B union {x_1,x_2})`, `|U|=26`.

If U contained an independent triple, together with x_1,x_2 it would give an independent5-set in C. Therefore `alpha(U)<=2`.

By Mantel applied to the complement,

`e(U) >= C(26,2)-floor(26^2/4)=325-169=156`.

But `e(H)=151`. Contradiction.

Hence Case C1 is impossible.

### Case C2: w is full to the 7-row B

After removing w, the five double degrees are

`(4,2,2,2)`.

Again forbidding the C-D `(8,8)` edge, the degree equations force

- exactly one 7-8 double;
- exactly three 6-8 doubles;
- one 6-7 double.

The unique 7-8 double has positive excess1.

If at least two of the three 6-8 doubles have excess0, then by (68-EQ) two of them have common H-neighbourhood exactly P_A. They are nonadjacent and anticomplete to the 27-point set

`U=H\(P_A union {z_1,z_2})`.

Thus `alpha(U)<=2`, so

`e(U)>=C(27,2)-floor(27^2/4)=351-182=169>151`,

a contradiction.

Therefore at least two of the three 6-8 doubles have excess1. Together with the unique 7-8 double they consume all three H-excess units. Consequently every other H-vertex, including the singleton w and all pure vertices, has excess0.

Now the unique 7-8 double x satisfies (78-EQ) with no pure excess available, so

`N_H(x)=P_B`.

The singleton w has one full support row and the unique partial support incidence. Since `eps_w=0`,

`d_H(w)=12-4=8`.

The singleton-full-row lemma makes w complete to all seven vertices of P_B, so w has exactly one H-neighbour n outside P_B. Also xw is a nonedge because `N_H(x)=P_B`.

Set

`U=H\(P_B union {x,w,n})`.

Then `|U|=25`, and both x and w are anticomplete to U and nonadjacent to each other. Hence an independent triple in U would create an independent5-set in C. Therefore `alpha(U)<=2`.

Mantel gives

`e(U)>=C(25,2)-floor(25^2/4)=300-156=144`.

The pure class P_B is a K7, contributing21 further H-edges disjoint from E(U). Hence

`e(H)>=144+21=165`,

contradicting `e(H)=151`.

Thus Case C2 is impossible.

Therefore Family C is empty.

## 7. Conclusion

Every Type-A d3 state with `O=5` is impossible:

- `eta=0`: inherited H-side O5 contradiction;
- `eta=1`: Families A,B,C are all empty.

Hence

> **TYPE-A O5 CLOSURE. Every surviving Type-A d=3 q31 platform satisfies `O<=4`.**

Together with `E406_D3_TYPE_B_CLOSURE.md`, the complete d=3 final-rise frontier is now reduced to Type-A states with `O<=4`.