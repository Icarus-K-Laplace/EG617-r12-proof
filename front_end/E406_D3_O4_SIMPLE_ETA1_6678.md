# E406 d=3 Type-A O4: eta=1 simple-four-double profile (6,6,7,8)

Status: `PROVED EMPTY`.

Dependencies:

- `E406_D3_O4_SIMPLE_ETA1_HIGHPAIR_REDUCTION.md`;
- `E406_D3_O4_SATURATED_LOW_ROW.md`;
- eta=1 O4 full-row counts `(9,10,10,10)`;
- every 7-8 double is an oriented 7-hub and a singleton-bearing 7-row cannot be that hub.

Let A,B,C,D have pure sizes

`6,6,7,8`.

The pure sizes sum27, so there are exactly four singleton-full carriers. Since total partial support incidence is4, each singleton has one partial incidence and every double has partial count0.

No singleton can be full to D. A 7-row carries at most one singleton, while each 6-row carries at most two. Hence either

1. `w_C=0` and `(w_A,w_B)=(2,2)`;
2. `w_C=1` and `(w_A,w_B)=(1,2)` up to swapping A,B.

## 1. Case `w_C=0`

Both A and B are saturated `(p,w)=(6,2)` rows. By the saturated-low-row obstruction neither can meet the 8-row D by a double.

If D is not the unique 9-full row, its non-pure demand is `10-8=2`, so it requires double degree2. Its possible neighbours are A,B,C; the A-D and B-D edges are forbidden by saturated-low-row rigidity, leaving only C-D, a single edge. Impossible.

Therefore D must be the 9-full row. Its required double degree is1, and hence the unique D-edge is C-D.

The non-pure requirements are then `(4,4,3,1)`. Subtracting singleton counts `(2,2,0,0)` gives double degrees

`(2,2,3,1)`.

After the edge C-D, the remaining three edges on A,B,C must realize degrees `(2,2,2)`, hence they form the triangle

`A-B, A-C, B-C`.

But A-C and B-C are 6-7 doubles incident with saturated `(6,2)` rows, forbidden by the saturated-low-row obstruction. Contradiction.

## 2. Case `w_C=1`

Up to swapping A,B, let

`w_A=1, w_B=2, w_C=1`.

The 7-row C is singleton-bearing. Therefore a 7-8 double C-D is impossible: every 7-8 double has forced hub P_C, while singleton-bearing 7-hubs are forbidden.

The saturated row B also cannot meet D by a 6-8 double.

Hence D can be joined by a double only to A. Therefore its double degree is at most1. It follows that D must again be the unique 9-full row, with double degree exactly1 and edge A-D.

The non-pure requirements `(4,4,3,1)` minus singleton counts `(1,2,1,0)` give double degrees

`(3,2,2,1)`.

After A-D, the remaining three edges on A,B,C must realize residual degrees `(2,2,2)`, hence again form the triangle

`A-B, A-C, B-C`.

In particular B-C is a 6-7 double incident with the saturated `(6,2)` row B, contradicting the saturated-low-row obstruction.

The symmetric singleton split is identical.

## 3. Conclusion

Both possible singleton distributions are impossible. Therefore no eta=1 Type-A O4 simple-four-double state with pure sizes `(6,6,7,8)` exists.