# E406 d=3 Type-A: modern O=4 interface

Status: `PROVED` under the four-triangle compression and saturated remainder ledger. This does not yet close the whole O=4 layer.

Let `T_1,...,T_4` be the four pairwise anticomplete K3 support classes, H the 35-point remainder, and

`O=sum_x(k_x-1)`, `R=sum_x r_x`.

Assume a surviving Type-A state with `O=4`.

The master incidence identity is

`3O+R=15+eta`.

Therefore

`R=3+eta`.

The H-side ledger from `E406_D3_REMAINDER_SATURATION.md` gives

- `e(H)=152-eta`;
- `sum_H eps=4-eta`;
- `eta in {0,1}`.

## 1. Full-row counts are always (9,10,10,10)

Each pure support triangle has exactly30 H-incidences. If `eta=1`, the unique internally-defective support triangle has31 H-incidences.

For row i write

- `a_i` for the number of H-vertices full to T_i;
- `r_i` for the number of partial incidences entering T_i.

Then

`3a_i+r_i=30` for a pure row,

and, when eta=1,

`3a_i+r_i=31` for the defective row.

### eta=0

Here `sum r_i=R=3` and each r_i is divisible by3. Hence exactly one row has

`r_i=3, a_i=9`,

and the other three have

`r_j=0, a_j=10`.

### eta=1

Here `sum r_i=4`. Pure-row partial totals are multiples of3; the defective-row partial total is congruent1 mod3. Therefore there are only two possibilities:

1. defective row has `r=1,a=10`, one pure row has `r=3,a=9`, others `(r,a)=(0,10)`;
2. defective row has `r=4,a=9`, all pure rows `(0,10)`.

Thus in every modern Type-A O4 state

`(a_1,a_2,a_3,a_4)=(9,10,10,10)`

up to row permutation.

## 2. Modern budgets are strictly stronger than historical S30 O4

The historical S30 O4 interface used

- 35-point H;
- full-row counts `(9,10,10,10)`;
- four pairwise anticomplete K3 rows;
- `e(H)=153`;
- total H excess6;
- total partial incidence3.

The modern E406 Type-A O4 interface instead has

- eta=0: `e(H)=152`, total excess4, `R=3`;
- eta=1: `e(H)=151`, total excess3, `R=4`.

Therefore historical O4 lemmas may be reused only when their hypotheses depend solely on the shared incidence definitions and alpha/clique facts. Historical CLOSED labels are not imported.

## 3. Immediate simple-four-double consequence: (4,8,8,8) is impossible

Assume the O4 multiplicity type consists of four double-full vertices whose row-pair graph is simple, and pure sizes are `(4,8,8,8)`.

No singleton partial carrier can be full to an 8-class: a singleton full to row i is complete to `P_i union T_i`, so `p_i<=7`.

Also an 8-8 double is impossible under either modern excess budget because the pair-overlap lower bound is at least6.

Hence every double edge would have to join the 4-row to an 8-row.

If the 4-row is the 9-full row, the three 8-rows each need two non-pure full memberships, so their required double degrees sum to6, while four edges incident with the 4-row supply only four such incidences.

If an 8-row is the 9-full row, the three 8-rows need double degrees `1,2,2`, summing to5, again exceeding the four incidences supplied by four edges through the 4-row.

Contradiction.

Thus the modern simple-four-double profile `(4,8,8,8)` is `PROVED EMPTY`.

## 4. Current target

After the complete O5 closure, every remaining d3 Type-A final-rise state lies in `O<=4`.

For O4, the next objective is to exploit the exact `(9,10,10,10)` interface and the modern excess budget3/4 to eliminate the remaining multiplicity types. The old S30 O4 archive is used only as a lemma reservoir / provenance source.