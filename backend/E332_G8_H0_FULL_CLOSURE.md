# E332 final closure: G=8, h=0

Status: `PROVED EMPTY`.

Assume the canonical E332 state with `G=8`, no undecorated high shell vertex (`h=0`), decorated set D of size k, and low regular set L of size `13-k`. The cases `k=3,4,5,6` are already closed in `E332_G8_H0_K3_K6_CLOSURE.md`. It remains to eliminate `k=7,8`.

Write

- `s=e_M(L,D)`;
- `J=M[D]`, so `e(J)=22-s`;
- A = active decorated vertices (those incident with L), `m=|A|`;
- I = inactive decorated vertices;
- `a=e_J(A)`, `c=e_J(A,I)`, `b=e_J(I)`.

Every active decorated vertex has row weight at least11. Pair-row coverage holds on every J-edge and every J-triangle has total row-weight at least24.

## 1. k=7

Here `|L|=6` and the decoration multiset is `(2,1,1,1,1,1,1)`.

Any J-triangle entirely inside I has row-weight at most22: each inactive J-degree is at most6, and four other decorated vertices outside the triangle consume at least four decoration units, so the triangle receives at most four decoration units. Thus `J[I]` is triangle-free.

The active row-weight sum is

`W_A = 2a+c+s+g_A`.

Since `a+c+b=22-s`, this becomes

`W_A = 22+a-b+g_A`.

Because the total decoration is8 on seven positive vertices, `g_A<=m+1`. Since every active vertex has weight at least11,

`22+a-b+g_A >=11m`.   (1)

### m>=3 is impossible

For m=3, `a<=3`, `g_A<=4`, so the left side of (1) is at most29, below33. Larger m is even worse.

### m=1 is impossible

One active vertex carries at most six low incidences, so `s<=6` and `e(J)>=16`. But a triangle-free graph on the six inactive vertices has at most9 edges, and the active vertex contributes at most six cross edges. Hence `e(J)<=15`, contradiction.

### m=2 is impossible

Now I has five vertices. Since L has six vertices, `J[I]` must contain an edge; otherwise L plus I is an independent11-set in M. Thus `b>=1`.

The two active decorations satisfy `g_A<=3`, and (1) gives

`b<=a+g_A`,

with `a<=1`.

Take an inactive edge uv. Its endpoint cross-degree sum is at most4. In a b-edge graph the internal endpoint-degree sum on an edge is at most `b+1`. The total inactive decoration is `8-g_A`; the other three inactive vertices are positive, so

`g_u+g_v <=5-g_A`.

Therefore

`t_u+t_v <=4+(b+1)+(5-g_A)=10+b-g_A`.

Pair-row coverage requires this to be at least12, hence

`b>=g_A+2`.

Together with `b<=a+g_A<=g_A+1`, contradiction.

### m=0 is impossible

Then s=0 and `e(J)=22>C(7,2)=21`.

Thus k=7 is empty.

## 2. k=8

Here `|L|=5` and every decorated vertex has decoration exactly1.

The active row-weight sum is

`W_A=2a+c+s+m=22+a-b+m`.

Hence

`22+a-b+m >=11m`.   (2)

### m>=3 is impossible

For m=3, `a<=3`, so the left side of (2) is at most28, below33. Larger m is even worse.

### m=2 is impossible

Equation (2) gives `b<=a+2<=3`.

Because L has five vertices and I has six, `b=0` would give an independent11-set, so an inactive edge uv exists.

Its endpoint cross-degree sum is at most4, its internal endpoint-degree sum is at most `b+1`, and each endpoint has decoration1. Thus

`t_u+t_v <=4+(b+1)+2=b+7<=10`,

contradicting pair-row coverage12.

### m=1 is impossible

One active vertex sees at most all five lows, so `s<=5`. Let c be its J-degree into the seven inactive vertices. The active row weight is

`t_x=c+s+1>=11`,

hence

`c+s>=10`.

Therefore

`b=e(J)-c=(22-s)-c<=12`.

Also `c<=7`, so

`b>=15-s>=10`.

Suppose `J[I]` contains a triangle. Each inactive decoration is1, so triangle-row coverage requires the sum of the three full J-degrees to be at least21; hence all three vertices have full J-degree7. They are therefore universal inside the seven-vertex inactive graph, forcing at least15 inactive edges, contradicting `b<=12`.

Thus `J[I]` is triangle-free. For an internal edge uv in a triangle-free seven-vertex graph,

`d_I(u)+d_I(v)<=7`.

Adding at most two cross incidences gives full degree sum at most9. But pair-row coverage with decorations1 requires full degree sum at least10. Contradiction.

### m=0 is impossible

Then `s=0` and J has22 edges on8 vertices. On every J-edge, pair coverage gives

`d_J(u)+d_J(v)>=10`.

If J contains a triangle, triangle-row coverage with decorations1 requires its three J-degrees to sum at least21, hence all three degrees are7. Thus every triangle would have to consist entirely of universal vertices.

If there are at most one universal vertices, J is triangle-free, impossible because a triangle-free graph on8 vertices has at most16 edges. If there are at least two universal vertices and any nonuniversal vertex exists, the two universal vertices together with it form a triangle containing a nonuniversal vertex, impossible. All eight vertices cannot be universal because J has only22 edges. Contradiction.

Thus k=8 is empty.

## Conclusion

Every G=8,h=0 state is empty.

By `E332_G8_H1_TO_H0_REDUCTION.md`, every G=8,h=1 survivor would yield a G=8,h=0 survivor. Therefore the entire G=8 decoration layer is empty.

Since the previous files prove G=4,5,6,7 empty and all other undecorated degree channels empty, there is no E332 survivor.