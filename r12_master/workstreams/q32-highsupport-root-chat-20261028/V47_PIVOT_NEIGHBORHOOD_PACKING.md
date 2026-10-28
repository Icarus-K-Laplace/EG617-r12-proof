# E408 Q32 — pivot-neighborhood packing theorem for full support

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL structural theorem; no Q32 closure claimed.**

This is an independent consequence of the source-correct Kang–Pikhurko Type-I factorization and the full-support 285-edge contract. It uses neither the retracted degree-nine assertion nor exceptional-vertex injectivity.

## 1. Contract

Assume
- (H) has 47 vertices, (e(H)=285), (alpha(H)\le4), and (delta(H)\ge12);
- (p) is the target-color pivot with exactly 13 target-colored edges, all to the shell (A), (|A|=13);
- (O=\{p\}\cup A), so every edge (ph), (h\in H), has one of the eleven non-target colors;
- there are (m\in\{8,9,10\}) exact-129 colors, each with the source-verified factorization (10K_5\dot\cup G_{11}), equivalently twelve disjoint color-(K_5) factors plus the special point (x_C).

## 2. Each exact color determines a pivot K4

### Lemma 2.1

For every exact color (C), there is a set (Q_C\subseteq H) such that:
1. (|Q_C|=4);
2. (Q_C) is independent in the target graph (H);
3. every edge of (Q_C) has non-target color (C);
4. (Q_C\subseteq N_C(p)\cap H).

### Proof

If (p\ne x_C), then (p) belongs to one of the twelve (C)-colored (K_5) factors. Its four other vertices are all (C)-neighbors of (p). None can lie in (A), since every (pA) edge is target-colored. They therefore all lie in (H); take them as (Q_C).

If (p=x_C), use the source-correct Type-I gadget. The four vertices (N_t\setminus\{y\}) are (C)-neighbors of (x_C=p) and form a (C)-clique. Again none lies in (A), so they all lie in (H); take this four-set as (Q_C).

In either case (Q_C) is a (C)-colored (K_4), hence a target-independent four-set. QED.

### Corollary 2.2 — cross-color vertex disjointness

For distinct exact colors (C,D), the sets (Q_C,Q_D) are vertex-disjoint.

Indeed, (Q_C\subseteq N_C(p)), (Q_D\subseteq N_D(p)), and each edge (ph) has a unique color. Thus the eleven pivot-neighborhood classes partition (H), and their selected exact-color four-sets cannot overlap.

Put
[
Q=\bigcup_{C\text{ exact}} Q_C,\qquad R=H\setminus Q,\qquad n=|R|=47-4m.
]
Then (Q) is a disjoint union of (m) independent four-sets and (n\in\{15,11,7\}).

## 3. Three forced edge reserves

### Lemma 3.1 — between two pivot blocks

For distinct exact colors (C,D),
[
e_H(Q_C,Q_D)\ge4.
]

The graph induced by (Q_C\cup Q_D) is bipartite with parts of size four, because both parts are independent. Since (alpha(H)\le4), this bipartite graph has independence number at most four. Its vertex-cover number is therefore at least four; by König's theorem it has a matching of size four. Hence it has at least four edges.

Consequently
[
e_H(Q)\ge4\binom m2.
]

### Lemma 3.2 — between pivot blocks and the remainder

Every (r\in R) has at least one neighbor in every (Q_C). Otherwise (Q_C\cup\{r\}) would be an independent five-set. Therefore
[
e_H(Q,R)\ge mn.
]

### Lemma 3.3 — internal edges of the remainder

Since (alpha(H[R])\le4), the complement of (H[R]) is (K_5)-free, so Turán's theorem gives
[
e_H(R)\ge p_4(n):=\binom n2-t_4(n).
]
For the three possible values of (n):
- (n=15): (p_4(n)=21);
- (n=11): (p_4(n)=10);
- (n=7): (p_4(n)=3).

## 4. A uniform 253-edge baseline

The three lower bounds sum to the same number in every possible exact-color count:
[
4\binom m2+m(47-4m)+p_4(47-4m)=253,
\qquad m\in\{8,9,10\}.
]

Because (e(H)=285), define nonnegative integer slacks
[
x=e_H(Q)-4\binom m2,\quad
y=e_H(Q,R)-mn,\quad
z=e_H(R)-p_4(n).
]
Then the exact edge budget is
[
\boxed{x+y+z=32.}\tag{4.1}
]

This is a new common-pool reduction: it uses (m) vertex-disjoint independent K4s selected from the pivot's color-neighborhood partition, rather than only the older pairwise-linear witness families.

## 5. Degree ledger and six-unit core excess

Write (d_H(v)=12+\epsilon_v), where (epsilon_v\ge0) and
[
\sum_{v\in H}\epsilon_v=2e(H)-12\cdot47=6.
]

The degree sum over (Q) is
[
\sum_{v\in Q}d_H(v)=43m+2x+y.
]
Since (Q) has (4m) vertices of degree at least 12,
[
\boxed{2x+y\ge5m.}\tag{5.1}
]

The degree sum over (R) is
[
\sum_{v\in R}d_H(v)=mn+y+2p_4(n)+2z.
]
Consequently,
[
\boxed{y+2z\ge D_m,}\tag{5.2}
]
where
[
D_8=18,\qquad D_9=13,\qquad D_{10}=8.
]

Moreover the degree excess splits exactly between (Q) and (R):
[
\boxed{(2x+y-5m)+(y+2z-D_m)=6.}\tag{5.3}
]
Thus
[
D_m\le y+2z\le D_m+6,
]
and, using (4.1),
[
\boxed{x\ge 26-D_m,}
]
namely
[
x\ge8\ (m=8),\qquad x\ge13\ (m=9),\qquad x\ge18\ (m=10).
]

The table summarizes the exact integer frontier:

| Exact colors (m) | (|Q|) | (|R|) | (e_H(Q)) floor | (e_H(Q,R)) floor | (e_H(R)) floor | Extra (Q)-(Q) edges (x) |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 32 | 15 | 112 | 120 | 21 | (x\ge8) |
| 9 | 36 | 11 | 144 | 99 | 10 | (x\ge13) |
| 10 | 40 | 7 | 180 | 70 | 3 | (x\ge18) |

## 6. Interpretation and boundary

For (m=10), the ten exact colors force ten disjoint independent four-sets in (H). Every pair of four-sets must have a perfect matching of (H)-edges between them; every remaining vertex must meet every four-set; and the 285-edge budget leaves at most ten units beyond the 253-edge baseline. The exact slack system above is a finite, source-correct graph-compatibility target.

This does **not** yet contradict the registered contract. In particular, the scalar system (4.1)–(5.3) has not been certified infeasible, and it must not be presented as an UNSAT certificate. The next step is to combine these pivot blocks with the exact-color (69/70) near-Turán normal forms and the shell / pointwise color-degree constraints.

## 7. Retraction firewall

No step here uses:
- a universal degree-nine KP special vertex;
- exceptional-vertex injectivity;
- a Q33 284-edge identity;
- an E407 U-reserve theorem.

EG617((r=12)) remains **OPEN / NOT_CERTIFIED**.
