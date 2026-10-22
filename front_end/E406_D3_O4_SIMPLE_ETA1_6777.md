# E406 d=3 Type-A O4: eta=1 simple-four-double profile (6,7,7,7)

Status: `PROVED EMPTY`.

Dependencies:

- `E406_D3_O4_SIMPLE_ETA1_HIGHPAIR_REDUCTION.md`;
- full-row counts `(9,10,10,10)`;
- four singleton-full partial carriers (because pure sizes sum27);
- no two singleton carriers may share a 7-row;
- every 7-7 double is an oriented high edge whose H-neighbourhood is exactly one endpoint K7;
- a singleton-bearing 7-row cannot be the hub of a high edge;
- a 7-row cannot be the hub of two distinct high edges.

Let A be the 6-row and B,C,D the three 7-rows. Write `s` for the number of singleton carriers placed on B,C,D. Since there are four singleton carriers total and each 7-row carries at most one, the remaining `4-s` singleton carriers lie on A.

Let h be the number of high edges among B,C,D.

## 1. A is the 9-full row

The non-pure full-row requirements are `(3,3,3,3)`.

Thus

`d_A = 3-(4-s)=s-1`.

The total double degree on B,C,D is `9-s`. Since every A-edge contributes one degree there,

`2h+(s-1)=9-s`,

so

`h=5-s`.

Because the three 7-rows support at most three high edges, `s>=2`.

- `s=2`: h=3, so B,C,D form a high triangle. Two of the three 7-rows carry singletons. The high edge joining those two rows has neither endpoint available as a hub, contradiction.
- `s=3`: h=2, and all three 7-rows carry singletons. Every high edge has both endpoints singleton-bearing, contradiction.

Hence A cannot be the 9-full row.

## 2. A 7-row, say B, is the 9-full row

The non-pure requirements are

`(4,2,3,3)`

on `(A,B,C,D)`.

Now

`d_A=4-(4-s)=s`.

The total degree on the three 7-rows is `8-s`. Therefore

`2h+s=8-s`,

so

`h=4-s`.

Again `1<=s<=3`.

### s=1

Then h=3: B,C,D form the complete high triangle. Exactly one 7-row carries a singleton; call it B after relabeling.

The two high edges incident with B must orient away from B, one to C and one to D. The remaining C-D high edge must orient to C or D, repeating a hub already used by the B-C or B-D edge. Repeated hubs are forbidden. Contradiction.

### s=2

Then h=2. Two 7-rows carry singletons and one, say D, is clean.

A high edge joining the two singleton rows is impossible, so both high edges must join a singleton row to D. Both are forced to orient to the only clean endpoint D, producing a repeated hub. Contradiction.

### s=3

Then h=1 and every 7-row carries a singleton. The unique high edge has no eligible hub endpoint. Contradiction.

Thus no 7-row can be the 9-full row.

## 3. Conclusion

All placements of the unique 9-full row are impossible. Therefore the eta=1 modern Type-A O4 simple-four-double profile `(6,7,7,7)` is empty.