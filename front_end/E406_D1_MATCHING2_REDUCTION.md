# E406 d=1 final-rise: matching-two reduction

Status: `PROVED` under the explicit E406 q30->q31 boundary contract. This does not yet close d=1 or E406.

Let `p` be the q30 pivot, `y` the adjacent q31 pivot, and suppose the boundary distance is d=1. Write

- `S={s}` for the unique old-shell missing neighbour of y;
- `D={u}` for the unique old-core neighbour exchanged out;
- `T=A\{y,s}`, so `|T|=11`;
- `J=M[T]`, `m=e(J)`;
- `k=eps_C(u)>=1`;
- `a=1_{su in E(R)}`;
- `G_T=sum_{v in T} g_v`.

The exact one-swap excess identity gives `eps_C'(s)=k-1`, and the old row weight of s is

`t_s=11+k+a`.

If `r=e_M(s,T)`, then `1+r+g_s=t_s`, so

`r+g_s=10+k+a`.

Using q=30,

`30=1+r+m+g_s+G_T`,

hence

`m+G_T=19-k-a`.       (D1-BASE)

The 13-point hereditary cap on `{p,y} union T` gives `m>=11`.

## 1. Remove the exchanged endpoint bits

For v in T put

`h_v=d_J(v)+g_v`.

In the old p-shell the full row weight is

`t_v=h_v+1_{sv in E(M)}`.

For every J-edge xy the E406 PAIR-13 lemma gives `t_x+t_y>=13`. Each endpoint indicator contributes at most1, hence

`h_x+h_y>=11`.       (D1-PAIR11)

Also

`sum_{v in T} h_v = 2m+G_T = m+19-k-a`.       (D1-SUM)

## 2. The matching number is at most three

Four disjoint J-edges would, by (D1-PAIR11), require endpoint h-weight at least44.

But (D1-BASE) gives `m<=19-k-a`, and therefore

`sum_T h <= (19-k-a)+(19-k-a) <=36`

because `k>=1` and `a>=0`.

Thus `nu(J)<=3`.

Since `m>=11`, `nu(J)=1` is impossible: a simple graph with matching number1 is a star or a triangle and has at most10 edges on11 vertices.

Hence initially

`nu(J) in {2,3}`.

## 3. Matching number three is impossible

Assume `nu(J)=3` and fix a maximum matching of three edges. Let X be its six endpoints. X is a vertex cover of J.

The three matching edges are disjoint, so (D1-PAIR11) gives

`sum_{x in X} h_x >=33`.       (1)

Because X is a vertex cover,

`sum_{x in X} d_J(x)=m+e_J(X)`.

Thus

`sum_X h = m+e_J(X)+G_X
          <= m+15+G_T
          =34-k-a`,

using `e_J(X)<=C(6,2)=15`, `G_X<=G_T`, and (D1-BASE).

Combining with (1), `k+a<=1`. Since k>=1,

`k=1, a=0`.

Now the lower and upper bounds are both33, so every inequality is equality. In particular

- `e_J(X)=15`;
- `G_X=G_T`.

Therefore `J[X]=K6`. But an edge of J is a target nonedge, so the six vertices of X form an independent 6-set in the T61 residual, contradicting `alpha<=5`.

Hence

`nu(J)!=3`.

Therefore every d1 final rise satisfies

`nu(J)=2`.       (D1-MATCH2)

## 4. The exchanged core excess is tiny

Let X now be the four endpoints of a maximum matching of size2. Again X is a vertex cover.

The two matching edges give

`sum_X h >=22`.

On the other hand

`sum_X h
 <= m+C(4,2)+G_T
 =25-k-a`.

Hence

`k+a<=3`.

The boundary `k+a=3` is impossible. Equality would be forced throughout, so

- `J[X]=K4`;
- all T-decoration lies on X;
- `sum_X h=22`.

But every one of the six K4 edges satisfies `h_i+h_j>=11`. Summing over all six edges gives

`3 sum_X h >=66`.

Since `sum_X h=22`, equality holds on every edge, so every pair has sum11. This would force all four integer h-values to equal 11/2, impossible.

Therefore

`k+a<=2`.       (D1-KA2)

Since `k>=1` and `a in {0,1}`, the only remaining exchange parameter pairs are

`(k,a)=(1,0),(2,0),(1,1)`.

## 5. Current d1 normal form

Every d1 q30->q31 final rise is now a matching-two small-cover system:

- `J=M[T]` has 11 vertices and at least11 edges;
- `nu(J)=2`;
- the four endpoints of a maximum matching form a vertex cover;
- `m+G_T=19-k-a`;
- `k+a<=2`;
- only `(k,a)=(1,0),(2,0),(1,1)` remain.

This is the preferred starting point for the final d1 closure.