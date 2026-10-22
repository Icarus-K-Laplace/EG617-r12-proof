# Unified final theorem for the E332 one-high branches

Status: `PROVED`.

This note replaces most of the finite `(k,r)` casework in the one-high G=7 and G=8 analyses.

Assume the canonical E332 state with exactly one undecorated high shell vertex `a`. By `E332_G7_G8_H1_UNIFORM_REDUCTION.md`:

- `a` has missing degree12 and is universal in the missing shell;
- there is at most one low-active decorated vertex;
- if there is no active decorated vertex, only the previously listed zero-active boundary states remain;
- if there is one active decorated vertex `x`, every low-D missing edge is incident with x.

Let

- `D` be the decorated set, `k=|D|`;
- `L` the low regular set, `|L|=12-k`;
- `r=e_M(L,D)`;
- `J=M[D]`;
- `I=D\{x}`;
- `b=e_J(I)`;
- `c=d_J(x)`;
- `g_x` the decoration of x.

Because `|L|+|I|=(12-k)+(k-1)=11`, the inactive graph J[I] must contain an edge; otherwise `L union I` is an independent11-set in M. Hence `b>=1`.

For an inactive edge uv:

- both endpoints have the compulsory missing edge to the universal high a;
- their total cross-incidence to x is at most2;
- inside the b-edge inactive graph, `d_I(u)+d_I(v)<=b+1`.

We combine this with the total decoration budget.

## 1. G=7: all one-high states are empty

Here

`e(J)=11-r`,

so

`b+c=11-r`.

The active row weight is

`t_x = 1+r+c+g_x >=12`,

hence

`c >= 11-r-g_x`.

Therefore

`b = 11-r-c <= g_x`.  (1)

For an inactive edge uv, the total decoration available on its endpoints is at most

`7-g_x-(k-3)=10-k-g_x`,

because the other `k-3` inactive decorated vertices are positive.

Thus

`t_u+t_v <= 2 + (b+1) + 2 + (10-k-g_x)
            =15+b-k-g_x`.

Pair-row coverage gives `t_u+t_v>=12`, so

`b >= k+g_x-3`.  (2)

Combining (1) and (2) gives

`k<=3`.

Thus every one-active G=7 survivor must have `k=3`.

Since I then consists of two vertices and b>=1, we have `b=1`. Equations (1),(2) force

`g_x=1`.

Also `c=10-r` and `c<=2`, so `r>=8`. The one-high reduction already has `r<=8`, hence

`(k,r)=(3,8)`.

This exact cell is eliminated by the row-multiplicity repivot argument in `E332_G7_H1_FULL_CLOSURE.md`: the two inactive decorations carry total6, the active decoration is1, the two exact 24-row triangles force the active low rows into a 12-point core block, and one row has imported excess at least3; repivot then gives shell decoration at least9, contradicting the universal E332 ceiling8.

Therefore

`G=7,h=1` is empty.

Together with the h=0 and h=2 closures, the entire G=7 layer is empty.

## 2. G=8: the one-high branch reduces to one terminal

Now

`e(J)=10-r`,

so

`b+c=10-r`.

The active weight condition again gives

`1+r+c+g_x>=12`,

hence

`c>=11-r-g_x`.

Therefore

`b=10-r-c <= g_x-1`.  (3)

For an inactive edge uv, the endpoint decoration sum is at most

`8-g_x-(k-3)=11-k-g_x`.

Thus

`t_u+t_v <=2+(b+1)+2+(11-k-g_x)
           =16+b-k-g_x`.

Pair-row coverage gives

`b>=k+g_x-4`.  (4)

Combining (3),(4):

`k<=3`.

Hence every one-active G=8 survivor has `k=3` and `b=1`. Then (3),(4) force

`g_x=2`.

Also

`c=9-r<=2`,

so `r>=7`. The exact windows are only

- `(k,r)=(3,8)`;
- `(k,r)=(3,7)`.

### (3,8) is impossible

Here `c=1` and J is a two-edge path. The two inactive decorations sum6. The inactive edge has endpoint J-degrees2 and1, plus the compulsory high edge at both endpoints, so its row-weight sum is

`(1+2)+(1+1)+6=11<12`,

contradicting pair-row coverage.

### (3,7) is the unique terminal

Here `c=2`, so `J=K3`. Exact accounting gives

- active decoration2 and row weight12;
- inactive decoration sum6 and inactive-edge row-weight sum12.

The two exact 24-row triangles force the row geometry described in `E332_G8_H1_TO_H0_REDUCTION.md`. Every non-contradictory active-low repivot either exceeds the universal decoration ceiling8 immediately or produces a legitimate E332 pivot with

`G=8,h=0`.

Thus

`G=8,h=1 => G=8,h=0`

for purposes of existence.

Since `E332_G8_H0_UNIFIED_CLOSURE.md` proves the no-high family empty, the entire G=8 layer is empty.

## Conclusion

The one-high branches need no large finite `(k,r)` case split:

- `G=7,h=1` is empty by the two inequalities `b<=g_x` and `b>=k+g_x-3` plus one terminal multiplicity contradiction;
- `G=8,h=1` reduces by `b<=g_x-1` and `b>=k+g_x-4` to the unique `(3,7)` terminal, which repivots to the already empty G=8,h=0 family.

This independently strengthens the final E332 closure DAG.