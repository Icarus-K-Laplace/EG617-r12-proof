# E406 d=3 Type-A O4: eta=1 simple-four-double profile (5,6,8,8)

Status: `PROVED EMPTY`.

Dependencies:

- `E406_D3_O4_SIMPLE_ETA1_HIGHPAIR_REDUCTION.md`;
- `E406_D3_O4_SATURATED_LOW_ROW.md`;
- eta=1 O4 full-row counts `(9,10,10,10)`;
- 8-8 double-full edges are impossible.

Let A,B,C,D have pure sizes

`5,6,8,8`.

Because the pure sizes sum27, there are exactly four singleton-full partial carriers. The total partial support incidence is also4, so every singleton has exactly one partial incidence and every double has partial count0.

No singleton can be full to an 8-row. Same-row singleton carriers form a clique, hence the clique bound gives

- at most3 singleton carriers on A;
- at most2 on B.

Therefore the singleton split on `(A,B)` is either

`(2,2)` or `(3,1)`.

Let `d_i` be the degree of row i in the simple four-edge graph of double-full pairs.

## 1. A is the 9-full row

The non-pure full-row requirements are

`(4,4,2,2)`.

If the singleton split were `(3,1)`, the required double degrees would be

`(1,3,2,2)`.

The degree-3 row B must meet A,C,D. Then C,D each already have one incident edge but each needs degree2; the only single edge that could raise both is C-D, forbidden because it is an 8-8 double. Hence this split is impossible.

Thus the split is `(2,2)`. The double-degree sequence is `(2,2,2,2)`, and with C-D forbidden the unique row graph is the K2,2 between `{A,B}` and `{C,D}`.

But B has pure size6 and two singleton carriers, so `p_B+w_B=8`, and B is incident with two 6-8 doubles. This contradicts the saturated-low-row obstruction.

## 2. B is the 9-full row

Now the non-pure requirements are

`(5,3,2,2)`.

The split `(2,2)` would require double degrees `(3,1,2,2)`, which by the same degree argument as above forces the forbidden edge C-D.

Hence the split is `(3,1)`, giving double degrees `(2,2,2,2)` and again the K2,2 between `{A,B}` and `{C,D}`.

Now A has pure size5 and three singleton carriers, so `p_A+w_A=8`, yet A is incident with 5-8 doubles. Again this contradicts the saturated-low-row obstruction.

## 3. An 8-row is the 9-full row

By symmetry let C be the 9-full row. The non-pure requirements are

`(5,4,1,2)`.

### Singleton split `(2,2)`

The required double degrees are

`(3,2,1,2)`.

The degree-3 row A must meet B,C,D. Since C is then already satisfied and D still needs one further edge, the fourth edge must be B-D. In particular B is incident with a 6-8 double.

But B has pure size6 and two singleton carriers, so `p_B+w_B=8`, contradiction to the saturated-low-row obstruction.

### Singleton split `(3,1)`

The required double degrees are

`(2,3,1,2)`.

Now B must meet A,C,D, and the fourth edge is A-D. Thus A is incident with a 5-8 double.

But A has pure size5 and three singleton carriers, again `p_A+w_A=8`, contradiction.

The case with D as the 9-full row is symmetric.

## 4. Conclusion

Every location of the unique 9-full row and every allowed singleton split forces an 8-edge incident with a saturated low row. Therefore the eta=1 simple-four-double profile `(5,6,8,8)` is empty.