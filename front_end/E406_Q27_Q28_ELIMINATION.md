# E406 bridge — q27 and q28 are impossible

Status: `PROVED` under the explicit E406 T61 h13 contract.

Dependencies:

- `front_end/E406_CORE_MINDEG_288.md`;
- inherited 3-matching in the 13-shell missing graph;
- hereditary `D` caps;
- `alpha(M)<=10`;
- exact subset-charge identity.

## 1. PAIR-13 for q27--q31

Let p be a degree-13 E406 pivot with `q>=27`. Then its 47-core C has

`e(C)=315-q<=288`.

By `E406_CORE_MINDEG_288.md`, `delta(C)>=12`.

For a missing-shell edge uv let

`D_u=N_C(u)`, `D_v=N_C(v)`, `r=|D_u union D_v|`.

Because uv is a target nonedge and `alpha(R)<=5`, the remainder

`W=C-(D_u union D_v)`

has independence number at most3.

- If `r<=10`, then |W|>=37, contradicting `R(3,37)=empty`.
- If `r=11`, then |W|=36 and `e(W)>=234`. But

  `e(W)<=e(C)-12*11+C(11,2)<=288-132+55=211`, contradiction.

- If `r=12`, then |W|=35 and modern CORE211 gives `e(W)>=211`. But

  `e(W)<=288-144+66=210`, contradiction.

Hence

`|D_u union D_v|>=13`.

Therefore every missing-shell edge satisfies

`t_u+t_v>=13`.      (PAIR-13)

## 2. q27 is impossible

Take three disjoint M-edges and let S be their six endpoints. PAIR-13 gives

`t(S)>=39`.      (1)

The subset identity gives

`27=q>=t(S)-e_M(S)`,

so

`e_M(S)>=12`.      (2)

A missing K4 would have row-union size at least36 and hence force

`q>=36-6=30`,

so M is K4-free. Therefore the six-vertex induced graph M[S] is K4-free, and Turan gives

`e_M(S)<=12`.

Thus equality holds in (1),(2):

`t(S)=39`, `e_M(S)=12`,

and the unique extremal K4-free six-vertex graph is

`M[S]=K_{2,2,2}`.

This graph has eight triangles, and every one of its six vertices lies in exactly four of them.

Every missing triangle T has row-weight sum at least24: otherwise its three pairwise target-nonadjacent shell vertices together with an independent3-set in the uncovered core would form an independent6-set in R.

Summing over the eight triangles gives

`4*t(S) >= 8*24 =192`.

But `t(S)=39`, so the left side is156. Contradiction.

Therefore q27 is impossible.

## 3. q28: reduction to an 11-edge six-vertex graph

The same three-matching set S gives `t(S)>=39`. The subset identity yields

`e_M(S)>=11`.

Again M is K4-free, so `e_M(S)<=12`.

If `e_M(S)=12`, then M[S]=K_{2,2,2}. Its eight triangle inequalities imply

`4*t(S)>=192`,

while the subset identity gives `t(S)<=28+12=40`. Hence `4*t(S)<=160`, contradiction.

Thus

`e_M(S)=11`, `t(S)=39`,

and all outside subset-charge terms vanish.

Let H be the four-edge complement of M[S]. Since M[S] is K4-free,

`alpha(H)<=3`.

A four-edge graph on six vertices with independence number at most3 is, up to isomorphism, exactly one of

1. `K3 disjoint_union K2 disjoint_union K1`;
2. `P4 disjoint_union K2`.

Indeed, if H has an isolated vertex, the other five vertices must have independence number at most2; the unique four-edge extremal form is K3+K2. If H has no isolated vertex, the degree sum8 forces degree sequence `(2,2,1,1,1,1)`, and the only form with alpha<=3 is P4+K2.

We eliminate both.

### Type A: H=K3+K2+K1

Let the K3 vertices have weights `x1,x2,x3`; let the K2 vertices have weights `y1,y2`; let the isolated H-vertex have weight w. Put

`X=x1+x2+x3`, `Y=y1+y2`.

Every cross-component pair is an M-edge, so PAIR-13 gives:

- summing the six K3--K2 edges:

  `2X+3Y>=78`;

- summing the three K3--{w} edges:

  `X+3w>=39`.

Since `X+Y+w=t(S)=39`, the first inequality gives `Y>=2w`, while the second gives `Y<=2w`. Hence

`Y=2w`,

and equality holds in both summed edge inequalities. Consequently every K3 weight is

`x_i=13-w`,

and both K2 weights equal w.

For each choice of one K3 vertex and one K2 vertex, together with w, we obtain an M-triangle. Triangle-24 gives

`(13-w)+w+w >=24`,

hence `w>=11`.

But every K3 vertex already has missing degree3 inside M[S], so

`x_i=t_i>=3`.

Thus `13-w>=3`, i.e. `w<=10`, contradiction.

### Type B: H=P4+K2

Label the P4 as `1-2-3-4`; let 5,6 be the K2. Put

`A=t1+t4`, `B=t2+t3`, `C=t5+t6`.

The six M-triangles are obtained by choosing one of 5,6 and one of the three independent pairs `{1,3},{1,4},{2,4}` in the P4.

Summing triangle-24 over these six triangles gives

`4A+2B+3C>=144`.

Since `A+B+C=39`, this is equivalent to

`A-B>=27`.      (3)

Vertices5 and6 are M-adjacent to every P4 vertex. Let

`m=min(t1,t2,t3,t4)`.

PAIR-13 gives

`C>=2(13-m)=26-2m`.      (4)

Also `B=t2+t3>=2m`.

Using (3),(4),

`39=A+B+C >= (B+27)+B+(26-2m)`

`=53+2B-2m >=53`,

contradiction.

Therefore q28 is impossible.

## 4. E406 bridge consequence

Every E406 degree-13 pivot with q27 or q28 is impossible.

Together with `E406_LOW_Q_PROMOTION_22_26.md`, any E406 pivot with q<=28 either is impossible or can be promoted past the forbidden q27/q28 levels. Thus the remaining independent bridge levels are q29 and q30.
