# E406 d=3 Type-A O4: eta=1 one-triple + two-double closure

Status: `PROVED EMPTY` under the modern Type-A O4 eta=1 contract.

## 0. Contract

Assume:

- four pairwise anticomplete support triangles `T_1,...,T_4`;
- H has 35 vertices and 151 edges;
- total H-core excess is 3;
- full-row counts are `(9,10,10,10)`;
- total partial support incidence is `R=4`;
- `O=4` is realized by exactly one triple-full H-vertex and two double-full H-vertices;
- every H-vertex is full to at least one support row;
- pure classes are cliques of size at most 8;
- same-row singleton-full carriers together with the pure class and support triangle obey the K12 cap.

Write `p_i` for the pure-class size of row i, `s_i` for the number of singleton-full carriers on row i, `m_i` for the number of the three multi-full vertices that are full to row i, and let `delta_i=1` for the unique 9-full row and `0` otherwise.

Put `d_i=8-p_i`.

## 1. Exact row-degree theorem

The number of non-pure full memberships required by row i is

`(10-delta_i)-p_i = 2+d_i-delta_i`.

Hence

`s_i = 2+d_i-delta_i-m_i`.

Because `P_i union T_i` is a clique and the same-row singleton-full carriers form a clique complete to `P_i union T_i`, K12-freeness gives

`p_i+3+s_i<=11`,

so

`s_i<=8-p_i=d_i`.

Therefore

`m_i>=2-delta_i`.

The triple contributes three full memberships and the two doubles four more, so

`sum_i m_i=7`.

But

`sum_i (2-delta_i)=1+2+2+2=7`.

Thus equality holds row by row:

`m_i=2-delta_i`,

and consequently

`s_i=d_i`.

So:

- the 9-full row has multi-degree exactly 1;
- each 10-full row has multi-degree exactly 2;
- each row is saturated: `p_i+s_i=8`, so `P_i union W_i union T_i` is a K11.

Now classify the multi-full hypergraph. If the triple contained the 9-full row, that row would already have its unique multi incidence, so neither double could meet it. The other three rows would each need one further incidence, but two doubles supply four endpoints among those three rows, impossible.

Hence the triple omits the 9-full row. Write that row as A and the other rows as B,C,D. The triple is exactly BCD. Each of B,C,D then needs one additional multi incidence and A needs one. Therefore the two doubles form a perfect matching of the four rows. After relabelling B,C,D:

`triple = BCD`,

`doubles = AB and CD`.      (HYPERGRAPH)

This exact hypergraph is the only possible one-triple/two-double incidence pattern.

## 2. Pure profiles

Let `w=sum_i s_i`. Since `s_i=d_i`,

`w=sum_i d_i=32-sum_i p_i`.

Every singleton-full carrier uses at least one partial incidence, and `R=4`, so `0<=w<=4`.

Thus the sorted pure profiles are precisely the partitions of deficits `w<=4` from four 8-rows:

- w=0: `(8,8,8,8)`;
- w=1: `(7,8,8,8)`;
- w=2: `(6,8,8,8)`, `(7,7,8,8)`;
- w=3: `(5,8,8,8)`, `(6,7,8,8)`, `(7,7,7,8)`;
- w=4: `(4,8,8,8)`, `(5,7,8,8)`, `(6,6,8,8)`, `(6,7,7,8)`, `(7,7,7,7)`.

We eliminate all of them using only already-proved local lemmas.

## 3. Reusable local lemmas

We use:

1. triple-transversal exclusion: a triple of row sizes `(8,8,8)` or `(7,8,8)` is impossible;
2. an 8-8 double is impossible under the total excess-3 eta=1 budget;
3. eta=1 high-pair rigidity: every 7-8 or 7-7 double has exact H-neighbourhood equal to a K7 endpoint hub and excess 1;
4. a singleton-bearing 7-row cannot be such a high-pair hub;
5. saturated-low-row obstruction: when a row has `(p,s)=(6,2)` or `(5,3)`, it cannot support the required 6/5-to-7/8 double in the applications below;
6. every row participates in exactly one of the two doubles by (HYPERGRAPH).

## 4. Elimination by deficit level

### w=0: `(8,8,8,8)`

The triple BCD is `(8,8,8)`, impossible.

### w=1: `(7,8,8,8)`

If A is the 7-row, BCD is `(8,8,8)`.
If A is an 8-row, BCD is `(7,8,8)`.
Both are impossible.

### w=2

#### `(6,8,8,8)`

If A is the 6-row, BCD is `(8,8,8)`.
If A is an 8-row, the perfect matching AB/CD contains an 8-8 double because only one row has size below 8.
Contradiction.

#### `(7,7,8,8)`

If A is a 7-row, BCD contains `(7,8,8)`, impossible.
If A is an 8-row, avoiding an 8-8 double forces both doubles to be 7-8. Both 7-rows have one singleton (`s=d=1`), so neither can serve as the forced K7 hub of its 7-8 double. Contradiction.

### w=3

#### `(5,8,8,8)`

If A is the 5-row, BCD is `(8,8,8)`.
If A is an 8-row, the perfect matching contains an 8-8 double.

#### `(6,7,8,8)`

If A is the 6-row, BCD is `(7,8,8)`, impossible.
If A is the 7-row, avoiding an 8-8 double forces a 7-8 double incident with A; A contains its singleton, so its forced 7-hub is forbidden.
If A is an 8-row, every perfect matching avoiding 8-8 contains a 7-8 double incident with the singleton-bearing 7-row. Contradiction.

#### `(7,7,7,8)`

Every double in the perfect matching is 7-7 or 7-8. Every 7-row has a singleton. Thus every high double has no admissible 7-hub endpoint. Contradiction.

### w=4

#### `(4,8,8,8)`

If A is the 4-row, the triple is `(8,8,8)`.
Otherwise the perfect matching contains an 8-8 double.

#### `(5,7,8,8)`

If A is 5, the triple is `(7,8,8)`.
If A is 7 or 8, every perfect matching avoiding 8-8 contains a 7-8 double incident with the singleton-bearing 7-row. Contradiction.

#### `(6,6,8,8)`

Every perfect matching avoiding 8-8 consists of two 6-8 doubles. Each 6-row has exactly two singleton carriers. The saturated-low-row obstruction excludes such a double. Contradiction.

#### `(6,7,7,8)`

The 6-row has exactly two singleton carriers and must participate in one double. Its partner has size 7 or 8, and the strengthened saturated-low-row obstruction excludes the corresponding 6-7/6-8 double. Contradiction.

#### `(7,7,7,7)`

Both doubles are 7-7. Every 7-row has a singleton, so neither endpoint of either double is an admissible oriented hub. Contradiction.

## 5. Conclusion

All possible pure profiles are impossible. Therefore

> **ETA1 TRIPLE-DOUBLE CLOSURE. No modern Type-A d=3 O4 state with eta=1 can realize the multiplicity type one triple + two doubles.**

The remaining O4 work is eta=0 for this multiplicity type and the two-triple multiplicity type.