# E406 d=2 final-rise retained-block theorem

Status: `PROVED` for the classification below. This does not yet close d=2 or E406.

Assume the E406 final-rise contract

`q_p=30 -> q_y=31`

from `E406_Q31_COEXISTENCE_REDUCTION.md`, with `d_M(y)=2`. Use the notation of `E406_FINAL_RISE_NORMAL_FORMS.md`.

Let

- `S={s1,s2}` be the old missing-neighbour pair of y;
- `D={u1,u2}=N_C(y)` be the exchanged core pair;
- `T=A\(S union {y})`, so `|T|=10`;
- `e=e_M(T)`;
- `h=G_T`;
- `e_S=e_R(S)` and `e_D=e_C(D)`, each in `{0,1}`;
- `epsilon'_S=sum_(s in S)(d_C'(s)-12)`;
- `e_SD=e_R(S,D)`.

## 1. The retained-block charge is at most8

The exact forward/reverse exchange identities specialize to

`e+h = 7 + e_S - epsilon'_S - e_SD`.   (D2-1)

The 12-set `{p,y} union T` is `K12` with exactly e missing internal T-edges. Since `omega(R)<=11`, `e>=1`. Therefore

`1 <= e+h <= 8`.   (D2-2)

In particular

`e<=8`, `h<=8-e`.

Hence at least

`10-h >= e+2`

vertices of T are undecorated degree-13 vertices in BOTH the q30 and q31 shell views.

## 2. Exact S-T and D-T target-edge budgets

Let

`A=e_R(S,T)`, `B=e_R(D,T)`.

The old q30 shell has missing-edge count

`z = 2 + (1-e_S) + (20-A) + e
   = 23-e_S-A+e`,

so its decoration sum is

`G = 30-z = 7+e_S+A-e`.

Since `G<=8`,

`A <= 1+e-e_S`.   (D2-3)

The new q31 shell similarly has

`z' = 2 + (1-e_D) + (20-B) + e
    = 23-e_D-B+e`,

hence

`G' = 31-z' = 8+e_D+B-e`.

Since `G'<=9`,

`B <= 1+e-e_D`.   (D2-4)

There is also a vertexwise form. The 12-set

`X={p,y} union T`

contains `66-e` target edges. The hereditary 13-point cap is67, so every outside vertex has at most `e+1` target neighbours in X.

A vertex of S is adjacent to p and not y, hence has at most e target neighbours in T. A vertex of D is adjacent to y and not p, hence also has at most e target neighbours in T.

Thus each individual S- or D-vertex has T-degree at most e.

The 16-set `X union S union D` gives one additional joint bound. Since `D(16)=76`,

`A+B+e_SD <= 6+e-e_S-e_D`.   (D2-5)

## 3. Joint old/new extreme-degree restriction on retained regular vertices

Take an undecorated `t in T`. Put

- `r_t=d_{M[T]}(t)`;
- `a_t=d_R(t,S)`;
- `b_t=d_R(t,D)`.

Its old and new shell missing degrees are

`d_old(t)=r_t + (2-a_t)`,

`d_new(t)=r_t + (2-b_t)`.

Both shell views have q in `{30,31}` and 47-core minimum degree at least12. Therefore the E406 extreme-degree theorem applies in both views:

`d_old(t),d_new(t) in {0,1,2,3,10,11,12}`.

Since `0<=r_t<=8`, this forces

`r_t in {0,1,2,3,8}`.   (D2-6)

Moreover:

- if `r_t=3`, then necessarily `a_t=b_t=2`; t is target-complete to both S and D;
- if `r_t=2`, then `a_t>=1` and `b_t>=1`;
- if `r_t=8`, then necessarily `a_t=b_t=0`; t is target-anticomplete to both S and D.

There are no undecorated T-vertices of internal missing degree4,5,6,7.

Writing `n_i` for the number of undecorated T-vertices with `r_t=i`, the cross-edge budgets give

`2 n_2 + 4 n_3 <= A+B <= 6+e-e_S-e_D-e_SD`.   (D2-7)

## 4. Weighted edge sum forces equality everywhere

For every missing edge `uv` of `M[T]`, the independently proved E406 row-union-13 lemma gives

`t_u+t_v>=13`.

For a T-vertex v,

`t_v = r_v + (2-a_v) + g_v <= r_v+2+g_v`,

where `a_v=d_R(v,S)` and `g_v` is its old-shell decoration. Therefore every T-edge satisfies

`(r_u+g_u)+(r_v+g_v)>=9`.

Summing over the e edges of `M[T]` gives

`9e <= sum_v r_v(r_v+g_v)`.

Now

`sum_v r_v^2 = 2e + 2*(number of unordered pairs of adjacent T-edges) <= 2e+2*C(e,2)=e^2+e`.

Also `r_v<=e`, so

`sum_v r_v g_v <= e*h`.

Using `h<=8-e`,

`sum_v r_v(r_v+g_v) <= e^2+e+eh <= 9e`.

Thus ALL inequalities are equalities.

Consequences:

1. `h=8-e`, hence by (D2-1)

   `e_S=1`, `epsilon'_S=0`, `e_SD=0`.   (D2-EQ1)

2. Every pair of T-missing edges intersects. Hence `M[T]` is an intersecting-edge graph.

3. Every positive decoration in T lies on a vertex of T-missing degree exactly e.

4. For every T-missing edge uv,

   `a_u=a_v=0`,

   and `t_u+t_v=13` exactly.

Applying the same argument in the new shell gives, on every T-missing edge,

`b_u=b_v=0`.

## 5. Exact T-block topology

For `e>=4`, a simple graph with e pairwise-intersecting edges is a star. For `e=3`, the only alternatives are a 3-star and a triangle; the triangle is impossible because `h=5>0` but equality in `sum r_v g_v<=eh` requires every decorated vertex to have T-degree e=3, while a triangle has maximum degree2. For `e=2`, the graph is a 2-star. For `e=1`, it is a single edge.

Therefore:

### e=2,...,8

`M[T] = K_(1,e) disjoint_union (9-e)K1`.

All T-decoration is concentrated on the star centre c:

`g_c=8-e`,

and every other T-vertex is undecorated.

The centre has old and new row weight10; every star leaf has old and new row weight3. The whole star component is target-anticomplete to BOTH exchanged pairs S and D.

### e=1

`M[T]=K2 disjoint_union 8K1`.

The total decoration7 is supported on the two endpoints of this unique edge, with

`g_u+g_v=7`.

Both endpoints are target-anticomplete to S and D, and their row weights sum exactly13.

So the formerly arbitrary 10-vertex retained deficit graph is completely classified.

## 6. Consequences for the exchanged pairs

From (D2-EQ1):

- S is a target edge;
- both S vertices have zero new-core excess;
- S is target-anticomplete to D.

For `e>=2`, target S-T incidences occur only on the `9-e` T-isolates. Since the old shell total decoration is

`G = h + g_S = (8-e)+g_S`,

while the exact shell count gives

`G=8+A-e`,

we obtain

`g_S=A`.

For each `s in S`, the missing edge ys and the row-union-13 lemma give `t_s>=11`. But

`t_s = 11-a_s+g_s`

because `e_S=1`. Hence `g_s>=a_s`. Summing over the pair and using `g_S=A` forces equality vertexwise:

`g_s=a_s`, `t_s=11` for each `s in S`.   (D2-EQ2)

Thus both 11-rows of S are disjoint from the 2-row D of y.

The core-excess exchange simplifies to

`epsilon_D=e_D`.

So if D is a target edge, its total old-core excess is exactly1; if D is a target nonedge, both D endpoints have old-core degree12.

## 7. Every star leaf is a q30 plateau d3 pivot

Assume `e>=2` and let l be a star leaf. Its old missing neighbours are exactly

`{c,s1,s2}`.

Their row weights are

`10,11,11`,

and among them exactly the two missing edges `cs1,cs2` occur. Therefore

`t({c,s1,s2})-e_M({c,s1,s2}) = 32-2=30`.

The subset-charge identity shows zero charge outside this triple. Repivoting at l cannot give q=31: the already proved d3 final-rise normal form would require all three removed row weights to be10, whereas here two are11. Hence

`q_l=30`.

The exact d3 plateau identity then forces the 3-row `D_l=N_C(l)` to be a K3 of old-core degree12 vertices and to be target-anticomplete to `{c,s1,s2}`.

Thus an e-star d2 final-rise state carries e simultaneous dense 3-row plateau supports, all attached to the same triple `{c,s1,s2}`.

## 8. Current d2 frontier

The d=2 final-rise problem is no longer a 10-vertex graph classification problem.

It is now exactly:

- `e=1`: one decorated edge carrying total decoration7;
- `e=2,...,8`: a star `K_(1,e)` with centre decoration `8-e`, S a target edge with exact 11-rows, and e leaf pivots of charge30 whose core supports are degree12 K3s anticomplete to a common shell triple.

The remaining task is a MULTI-SUPPORT COMPATIBILITY theorem for those e simultaneous K3 rows (plus the isolated e=1 edge case). These are exact normal forms conditional on a d2 q30->q31 final-rise edge, not merely necessary scalar states.