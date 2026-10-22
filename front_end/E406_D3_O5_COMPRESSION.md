# E406 d=3: O=5 compression in the 35-point remainder

Status: `PROVED` for the Type-B O=5 closure and the Type-A reductions stated below. The d=3 class and E406 remain `OPEN`.

Assume the four-triangle compression and the saturated 35-point remainder ledger.

For x in H let

- k_x be the number of support triangles T_i to which x is complete;
- r_x the number of additional partial T-incidences;
- `O=sum(k_x-1)`;
- `R=sum r_x`.

Since every H-vertex is full to at least one T_i and the total T-H incidence count is `120+eta`,

`3O+R=15+eta`,

where `eta in {0,1}` is the internal excess of the unique possible defective support triangle.

Thus `O<=5`.

Every pure class P_i (k=1,r=0) is a clique and has size at most8.

## 1. Pair-overlap excess lemma under the modern budget

Let x be full to two rows i,j and to no other row. Put

- `p=|P_i|`, `q=|P_j|`;
- `A=P_i\N_H(x)`, `a=|A|`;
- `B=P_j\N_H(x)`, `b=|B|`;
- h = number of H-neighbours of x outside `P_i union P_j`.

Then

`eps_x = p+q-6+r_x-a-b+h`.

The bipartite graph A-B is complete, else a missing A-B edge together with x and one missed vertex from each uncovered support triangle gives an independent5-set in C.

Hence the total H-excess spent on x,A,B is at least

`Phi_{p,q}(a,b,r_x)
 = p+q-6+r_x-a-b
   + a[b-(10-p)]_+
   + b[a-(10-q)]_+`.

Consequences needed below:

- pair (8,8) costs at least `6+r_x`;
- pair (7,8) costs at least `1+r_x`;
- pair (7,7) costs at least `1+r_x`;
- pair (6,8) and (6,7) have zero-cost equality positions.

Moreover, under a **global excess budget at most3**, any (7,8) or (7,7) double-overlap vertex must itself have positive excess: if `eps_x=0`, the missing-set part alone costs at least5 for (7,8) and at least4 for (7,7).

## 2. Triple-full transversal lemma

Let x be full to three support triangles with pure classes of sizes p,q,r. Put A_i=P_i\N_H(x), with sizes a,b,c.

The unique uncovered support triangle supplies a vertex nonadjacent to x and to all three pure classes. Therefore A_1,A_2,A_3 cannot contain an independent transversal.

Choose one vertex uniformly from each A_i. Since every triple contains at least one cross edge,

`e(A1,A2)/(ab)+e(A1,A3)/(ac)+e(A2,A3)/(bc) >=1`.

Hence the number of cross edges among the three missing sets is at least

`min(ab,ac,bc)`.

On the other hand a pure vertex in a p-class has external H-degree at most

`10-p+eps_v`.

Thus the total number of cross edges among the missing sets is at most half their total available external degree.

This immediately excludes the triple-full row-size patterns

- `(8,8,8)`;
- `(7,8,8)`

under the present total H-excess budgets at most4: the missing-set sizes forced by `d_H(x)<=4` require at least32 and24 cross edges respectively, while the total external-degree budgets permit at most22 in either case.

A four-full-row vertex is even easier: its H-degree is at most1, so its nonneighbourhood in H has at least33 vertices and independence at most3, whose Turan lower edge count already exceeds `e(H)<=152`.

## 3. Type B (`eta=0`): O=5 is impossible

Here

- `R=0`;
- `e(H)=152`;
- total H-core excess is4;
- each support triangle has exactly30 H-incidences, hence every full-row count is10.

Let m be the number of multi-full H-vertices.

### m=3

The pure profile is `8,8,8,8`. The membership increments partition5 as either `(3,1,1)` or `(2,2,1)`, so a 4-full vertex or a triple-full `(8,8,8)` vertex occurs. Both are impossible by Section2.

### m=4

The pure profile is `(7,8,8,8)` and one multi-full vertex is triple-full. Any triple of four rows contains at least two of the three 8-rows, so its pure-row pattern is `(8,8,8)` or `(7,8,8)`, impossible.

### m=5

All five multi-full vertices are doubles.

The possible pure profiles are `(6,8,8,8)` and `(7,7,8,8)`.

- `(6,8,8,8)`: double-row degree sequence is `(4,2,2,2)`, forcing an 8-8 double pair. Its excess cost is at least6>4.
- `(7,7,8,8)`: avoiding the 8-8 pair forces exactly four 7-8 doubles and one 7-7 double. Under the global budget4, each of the four 7-8 doubles must itself carry positive excess, consuming all four units. The remaining 7-7 double cannot have zero excess: `eps_x=0` would force at least four pure-set excess units by the pair-overlap lemma. Contradiction.

Therefore

`Type-B + O=5` is `PROVED EMPTY`.

## 4. Type A with eta=1: strong reduction of O=5

Now

- `R=1`;
- `e(H)=151`;
- total H-core excess is3;
- the single partial incidence enters the unique internally-defective support row;
- the saturated-row identity gives `eps_x+s_D(x)=1` for every H-vertex, so every H-core excess is0 or1.

The same membership analysis eliminates:

- every m=3 state whose multi-full family contains a 4-full vertex or a `(7,8,8)/(8,8,8)` triple;
- every m=5 profile `(5,8,8,8)` (forced 8-8 double);
- every m=5 profile `(7,7,7,8)` (all five doubles are 7-7/7-8, and each must itself have positive excess, exceeding the total budget3);
- m=5 profiles `(6,8,8,8)` and `(7,7,8,8)` when the unique partial incidence sits on a double rather than on a singleton, by the same 8-8 / four-positive-double argument as Type B.

Thus every remaining eta=1,O=5 state is confined to a very small exceptional family involving

- a singleton partial carrier;
- pure profile `(6,7,8,8)` or a triple-full configuration not already covered by the `(7,8,8)` transversal lemma.

No existence is asserted. These are the only O=5 configurations still requiring a separate modern contradiction.

## 5. Consequence

The d=3 final-rise class is now reduced simultaneously by:

- four pairwise anticomplete K3 support classes;
- the saturated 35-point 151/152-edge remainder;
- exact/near D-row partition;
- `O<=5`;
- complete elimination of Type-B O=5;
- only a tiny eta=1 exceptional O=5 family.

The next step is to combine the eta=1 singleton-partial exceptional family with the exact D-row partition and the total excess3, or else descend to O<=4.