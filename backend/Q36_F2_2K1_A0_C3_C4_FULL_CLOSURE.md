# q36 f=2, 2K1 far, a_F=0 — full closure of pure-d2 c=3 and c=4

Status: `PROVED` under `Q36_F2_2K1_A0_PURE_D2_TERMINALS.md` and the global independence bound `alpha(F)<=4`.

## 1. Common observation

In the `2K1,a_F=0` branch the two far shell vertices `a,b` are target-nonadjacent and are target-anticomplete to

- every decorated shell vertex in X;
- every d2 core support, because the exact d2 formula has `e_F(F,D)=0`.

Therefore, if X contains a target-nonedge `x1x2` and one support endpoint d is target-nonadjacent to both x1,x2, then

`{a,b,d,x1,x2}`

is an independent5-set, contradicting `alpha(F)<=4`.

## 2. c=4

`Q36_F2_2K1_A0_PURE_D2_TERMINALS.md` gives the exact c=4 state

- `nu=e_M(X)=6`;
- `e_F(D,X)=0`;
- all four d2 owners share one pure K2 support D.

Since nu=6, M[X] has an edge x1x2. Every endpoint d of D is target-nonadjacent to all of X. Hence the common observation gives an independent5-set.

Thus

> `c=4` is EMPTY.

## 3. c=3

The exact terminal has

`nu in {4,5}` and `e_F(D,X)<=nu-4`.

### nu=4

Then `e_F(D,X)=0`. Since M[X] has four edges, choose any missing edge x1x2 and any d in D. The common observation gives an independent5-set.

### nu=5

Now `e_F(D,X)<=1`. Hence at least one endpoint d of the two-point support D has no target neighbour in X at all. Since M[X] has five edges, choose any missing edge x1x2. Again `{a,b,d,x1,x2}` is independent.

Therefore

> `c=3` is EMPTY.

## 4. Consequence

The entire `2K1,a_F=0` branch is now reduced to the pure-d2 cases

`c in {1,2}`.

All states with `c>=3` are empty.