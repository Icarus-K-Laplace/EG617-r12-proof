# E332 closure of the exact H2-G7-K4minusE cell

Status: `PROVED EMPTY`.

Start from the exact state reduced in `E332_H2_G7_ROW_CLASS_REDUCTION.md`:

- two high regular shell vertices `a,b`, each with row weight11;
- two decorated vertices `x,y`, with total decoration7 and `X=D_x`, `Y=D_y`, `X cap Y=empty`, `|X|+|Y|=13`;
- nine low regular vertices, each with missing neighbourhood `{a,b}`;
- every low row is a 2-vertex H-edge lying in `P=X union Y`;
- any two distinct low-row edges are vertex-disjoint.

Therefore the nine lows split into row classes indexed by pairwise-disjoint H-edges in P. Let one such row edge be

`E={c,d}`

with multiplicity `m>=1`.

## 1. Global degree of a row endpoint

Both c and d have core degree12.

Because distinct low-row edges are disjoint, a row endpoint belongs to no low row outside its own class. Hence c is adjacent in F to exactly

- the m low shell vertices in its row class;
- exactly one of x or y, because P=X disjoint-union Y;
- no a or b, since every low row is disjoint from A=D_a and B=D_b;
- no pivot p, because p is anticomplete to the old 35-core.

Thus the total degree of c in F is

`d_F(c)=12+m+1=13+m`.

The same holds for d.

So if c,d enter a shell around another degree-13 pivot, their decoration values are both exactly m.

## 2. Repivot at a low vertex is a q=30 plateau

Choose a low vertex u in the row class E.

For u we have

- `d_M(u)=2`;
- `S=N_M(u)={a,b}`;
- `t_a+t_b=22`;
- `e_M(S)=0`.

The standard repivot lower bound gives

`q_u-q >= 2(13-2)-22 = 0`.

The old pivot has q=30. For every legitimate degree-13 pivot in E332,

`332=91+q_u+e(H_u)`

and CORE211 gives `e(H_u)>=211`; hence `q_u<=30`.

Therefore

`q_u=30`.

So repivot at every low is an exact q30 plateau.

## 3. Decoration overflow

The new shell at pivot u removes the regular shell vertices a,b,u and inserts the two core vertices c,d, while x,y remain shell vertices.

The old decoration total is7, carried by x,y. The new vertices c,d each have global excess m, as proved above. Hence the new shell decoration total is

`G_u=7+2m`.

Since `m>=1`,

`G_u>=9`.

But every legitimate E332 shell satisfies

`q_u=z_u+G_u`,

with the inherited shell floor `z_u>=22`. Since `q_u=30`, necessarily

`G_u<=8`.

Contradiction.

Therefore no row class can exist, although there are nine lows. Hence the exact `H2-G7-K4minusE` state is impossible.

## Conclusion

`H2-G7-K4minusE` is `PROVED EMPTY`.

After the previous closures, the entire E332 frontier is now reduced to only three branches:

1. `G=7,h=1`;
2. `G=8,h=0`;
3. `G=8,h=1`.
