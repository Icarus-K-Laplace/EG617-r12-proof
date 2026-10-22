# E332 two-high extreme shells

Status: `PROVED`.

Assume the active E332 extreme-shell state and `h=2`. Then the uniform argument in `E332_G4_G5_CLOSURE.md` shows:

- the two high regular vertices `a,b` are adjacent in the missing graph to every low and every decorated vertex;
- every low has degree2 with neighbourhood `{a,b}`;
- there are no low-decorated missing edges;
- if `epsilon=1_{ab in E(M)}` and `J=M[D]`, then

`e(J)=8-G-epsilon`.

Also `J` is nonempty, otherwise `L union D` would be an independent 11-set in `M`.

For every `x in D`,

`t_x=2+d_J(x)+g_x`.

If `epsilon=0`, every J-edge together with either high vertex is an M-triangle, so triangle row coverage gives

`t_x+t_y>=13`.

If `epsilon=1`, pair-row coverage gives

`t_x+t_y>=12`.

## G=4

Closed in `E332_G4_G5_CLOSURE.md`.

## G=5

Closed in `E332_G4_G5_CLOSURE.md`.

## G=6

If `epsilon=0`, then `e(J)=2` and every edge must satisfy the stronger triangle inequality `t_x+t_y>=13`.

The two-edge graph is either `2K2` or `P3`.

- In `2K2`, each edge has endpoint J-degree sum2, so the two endpoint decorations must sum to at least7. This already exceeds the total budget6.
- In `P3`, each leaf-centre edge has J-degree sum3, so its endpoint decorations must sum to at least6. Positivity of both leaves then forces total decoration at least7.

Thus `epsilon=0` is impossible.

If `epsilon=1`, then `e(J)=1`. For its unique edge `xy`, both J-degrees are1, and pair-row coverage gives

`(3+g_x)+(3+g_y)>=12`,

so

`g_x+g_y>=6`.

Since total decoration is exactly6 and every decorated vertex has positive decoration, this forces

`k=2`, `g_x+g_y=6`.

Hence the only possible h=2,G=6 state is:

- two undecorated high vertices `a,b` with `ab in E(M)`;
- two decorated vertices `x,y` with `xy in E(M)` and `g_x+g_y=6`;
- nine undecorated lows, each with missing neighbourhood `{a,b}`;
- the four support vertices `{a,b,x,y}` induce `K4` in `M`.

Call this exact state `H2-G6-K4`.

## G=7

If `epsilon=1`, then `e(J)=0`, contradicting `alpha(M)<=10` because `L union D` would be an independent 11-set.

Thus `epsilon=0` and `e(J)=1`. Let its unique edge be `xy`. Then `d_J(x)=d_J(y)=1` and each high vertex together with `x,y` forms an M-triangle. Triangle row coverage yields

`11+(3+g_x)+(3+g_y)>=24`,

hence

`g_x+g_y>=7`.

The total decoration is7, so again positivity forces

`k=2`, `g_x+g_y=7`.

Hence the only possible h=2,G=7 state is:

- two undecorated high vertices `a,b` with `ab notin E(M)`;
- two decorated vertices `x,y` with `xy in E(M)` and `g_x+g_y=7`;
- nine undecorated lows, each with missing neighbourhood `{a,b}`;
- the four support vertices induce `K4-e` in `M`, where the missing support edge is `ab`.

Call this exact state `H2-G7-K4minusE`.

## G=8

If `epsilon=0`, then `e(J)=0`, contradicting `alpha(M)<=10`. If `epsilon=1`, the formula gives `e(J)=-1`, impossible.

Therefore no h=2,G=8 state exists.

## Final two-high classification

For the entire remaining decoration range `G=6,7,8`, an h=2 survivor must be exactly one of two states:

1. `H2-G6-K4`;
2. `H2-G7-K4minusE`.

There is no h=2 survivor for G=8.
