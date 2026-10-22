# E406 d=3 Type-A O4: eta=1 simple-four-double full closure

Status: `PROVED EMPTY` for the complete **simple** four-double branch under the modern eta=1 O4 contract.

Here `simple` means the four double-full vertices correspond to four distinct row pairs.

## 1. Base reduction

`E406_D3_O4_SIMPLE_ETA1_HIGHPAIR_REDUCTION.md` proves that every eta=1 simple-four-double pure profile is empty except

- `(5,6,8,8)`;
- `(6,6,8,8)`;
- `(6,6,7,8)`;
- `(6,7,7,7)`.

The reduction uses the exact eta=1 budget

- `e(H)=151`;
- total H-core excess3;
- full-row counts `(9,10,10,10)`;
- total partial support incidence4;
- pointwise `eps<=1`;

and establishes the 7-7 / 7-8 hub rigidity, no repeated 7-hub, no singleton-bearing 7-hub, and no two singleton carriers on one 7-row.

## 2. The four residual profiles

### `(6,7,7,7)`

Closed in `E406_D3_O4_SIMPLE_ETA1_6777.md` by row-degree balance plus the 7-hub restrictions.

### `(6,6,8,8)`

Closed in `E406_D3_O4_SIMPLE_ETA1_6688.md`.

The three singleton carriers split `(1,2)` across the two 6-rows. The two-singleton 6-row must meet an 8-row by a double. The saturated-low-row theorem forces that double to be complete to the K6 and then forces adjacency to both singleton carriers, producing a K12.

### `(5,6,8,8)`

Closed in `E406_D3_O4_SIMPLE_ETA1_5688.md`.

Every allowed location of the unique 9-full row forces an 8-edge incident with a saturated low row `(p,w)=(5,3)` or `(6,2)`, contradicting `E406_D3_O4_SATURATED_LOW_ROW.md`.

### `(6,6,7,8)`

Closed in `E406_D3_O4_SIMPLE_ETA1_6678.md`.

The singleton distribution is either `(2,2,0)` on the two 6-rows and 7-row, or `(1,2,1)` up to swapping the 6-rows. The saturated `(6,2)` row cannot meet a 7- or 8-row. Row-degree balance then forces exactly such an edge in every case.

## 3. Conclusion

No eta=1 modern Type-A O4 state exists whose four O-units are carried by four double-full vertices on four distinct row pairs.

Together with `E406_D3_O4_SIMPLE_ETA0_FULL_CLOSURE.md`, the **entire simple-four-double O4 branch is empty for both eta=0 and eta=1**.

This theorem does not by itself eliminate a non-simple four-double row-pair multigraph with repeated row pairs, nor the `one triple + two doubles` or `two triples` O4 multiplicity types. Those remain separate obligations unless independently excluded.