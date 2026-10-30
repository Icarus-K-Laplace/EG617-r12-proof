# Independent four-set of degree-12 vertices

Status: **PROVED**

Assume H is a simple graph with 47 vertices, 284 edges, minimum degree at least 12, and alpha(H)<=4. Define

epsilon(v)=d_H(v)-12.

Then

sum_v epsilon(v)=2e(H)-12|V(H)|=568-564=4.

Let Q={v:epsilon(v)>0} and q=|Q|. Since the total excess is four,

1<=q<=4.

Every vertex of S=V(H) minus Q has degree exactly 12.

## Claim

There is an independent set I of size four contained in S.

## Proof

Suppose H[S] has no independent four-set. Then alpha(H[S])<=3. The complement of H[S] is K4-free, so Turan's theorem gives

e(H[S]) >= p_3(47-q),

where p_3(n)=binom(n,2)-t_3(n), and t_3(n) is the balanced complete tripartite Turan number.

The edge count decomposes exactly as

e(H)=e(H[S])+sum_{v in Q}d(v)-e(H[Q]).

Since sum_Q d(v)=12q+4 and e(H[Q])<=binom(q,2),

e(H) >= p_3(47-q)+12q+4-binomial(q,2).

The four possibilities are:

| q | 47-q | balanced tripartition | p_3(47-q) | lower bound for e(H) |
|---:|---:|---|---:|---:|
| 1 | 46 | 16,15,15 | 330 | 346 |
| 2 | 45 | 15,15,15 | 315 | 342 |
| 3 | 44 | 15,15,14 | 301 | 338 |
| 4 | 43 | 15,14,14 | 287 | 333 |

Every lower bound exceeds 284, contradiction.

Therefore H[S] contains an independent four-set I, and every vertex of I has degree exactly 12. QED.

## Dependency boundary

This lemma uses only |V(H)|=47, e(H)=284, delta(H)>=12, and alpha(H)<=4. The omega(H)<=11 condition is not needed here.
