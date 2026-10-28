# E408 Q32 — corrected non-full-support exceptional multiplicity

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL under the registered E408 Q32 / exact-129 Type-I factor contract.**  
This theorem does **not** use the retracted degree-9 assertion for the Kang–Pikhurko gadget.

## 1. Frozen contract

Work in the registered E408 Q32 residual contract:

- residual F has 61 vertices and target residual energy 408;
- q=32, target core H has |H|=47, e(H)=285, alpha(H)<=4, delta(H)>=12;
- total H degree excess is 6;
- shell A=N_F(p) has |A|=13;
- the number m of exact-129 non-target colors lies in {8,9,10};
- for every exact-129 color C, the Kang–Pikhurko Type-I equality graph consists of ten isolated K5s plus an 11-vertex gadget containing two further disjoint K5s and one special vertex x_C;
- hence, excluding x_C, the remaining 60 vertices are partitioned into twelve disjoint color-C K5s;
- every one of those twelve K5s meets O={p} union A, because a K5 wholly inside H would be an H-independent 5-set;
- removing the unique O-vertex from any K5 meeting O exactly once gives an independent core 4-set witness.

Let U be the union of all such single-outside core-4 witnesses over all exact colors, and put W=H\U. The independently proved low-support theorem gives |U|>=44, so |W|<=3.

The pivot p is target-adjacent to every shell vertex a in A. Therefore p and a cannot lie in the same non-target monochromatic clique. In particular, a K5 with at least two outside-H vertices contains at least two shell vertices from A and does not use p.

## 2. Pointwise exceptional-multiplicity theorem

For w in W define

n_w := |{ exact colors C : x_C = w }|.

### Theorem 2.1

For every w in W,

\[
\boxed{n_w\ge m-6.}
\]

### Proof

Fix w in W and an exact color C with x_C != w. Since x_C is the only vertex outside the twelve color-C K5s, w belongs to exactly one of those K5s, say K.

If K met O in exactly one vertex, then K\cap H would be a four-point color-C clique, hence one of the single-outside core witnesses included in U. It contains w, contradicting w in W=H\U.

Therefore K has at least two outside-H vertices. As noted above, p cannot share a non-target clique with any shell vertex, so these outside vertices include at least two distinct vertices a,b in A. Consequently wa and wb are both color-C edges.

For fixed w, different exact colors use disjoint shell neighbors: an edge wa has one unique color in the original edge-coloring. Thus every exact color with x_C != w consumes at least two distinct vertices of the 13-point shell A. Hence

\[
2(m-n_w)\le13,
\]

so m-n_w<=6 and n_w>=m-6. QED.

## 3. Global consequence

Each exact color has only one special vertex x_C. Therefore

\[
\sum_{w\in W} n_w\le m.
\]

Combining with Theorem 2.1 gives the uniform non-full-support inequality

\[
\boxed{|W|(m-6)\le m.}\tag{3.1}
\]

This is valid without exceptional-vertex injectivity and without any special-vertex degree value.

## 4. The v=44 consequences

Assume |U|=44, so |W|=3.

### Corollary 4.1 — m=10 is impossible

If m=10, Theorem 2.1 gives n_w>=4 for each of the three points of W. Therefore

\[
\sum_W n_w\ge12>10=m,
\]

contradiction.

Thus

\[
\boxed{|U|=44\Longrightarrow m\ne10.}
\]

### Corollary 4.2 — exact equality structure for m=9

If m=9, every w in W satisfies n_w>=3, while the total is at most 9. Hence equality holds everywhere:

\[
\boxed{n_w=3\quad\text{for every }w\in W,}
\]

and

\[
\boxed{x_C\in W\quad\text{for every one of the nine exact colors}.}
\]

Thus W consists of three points, each serving as the KP special vertex for exactly three exact colors.

## 5. Double/triple outside classification at v=44,m=9

Fix one of the nine exact colors C. Since x_C lies in H (indeed in W), the twelve K5s contain the remaining 46 H-vertices and 14 outside-H vertices. Every K5 contains at least one outside-H vertex, so relative to one outside vertex per K5 there are exactly two extra outside incidences.

Therefore exactly one of the following holds:

1. **double type:** ten single-outside K5s and two double-outside K5s;
2. **triple type:** eleven single-outside K5s and one triple-outside K5.

Let t be the number of triple-type exact colors.

### Theorem 5.1

Under |U|=44 and m=9,

\[
\boxed{t\le1.}
\]

### Proof

Fix w in W. Exactly three exact colors have x_C=w, so in the other six exact colors w lies in a multi-outside K5.

- In a double-type color with x_C != w, that K5 has exactly two shell vertices, so w has at least two shell neighbors of that color.
- In a triple-type color with x_C != w, there are eleven single-outside witnesses. Their 44 core vertices already equal U. The remaining H-vertices are precisely x_C and the two core vertices of the unique triple-outside K5, i.e. W. Thus w belongs to that triple-outside K5 and has three shell neighbors of color C.

Let t_w be the number of triple-type exact colors for which x_C != w. Edge-color uniqueness on the 13 shell edges from w gives

\[
12+t_w\le13,
\]

so t_w<=1 for every w in W.

Every triple-type color has x_C at one W-point and is non-special at the other two W-points, hence contributes two to \(\sum_W t_w\). Therefore

\[
2t=\sum_W t_w\le3,
\]

and t<=1. QED.

Hence at least eight of the nine exact colors are double type.

## 6. Additional degree-excess consequence

If t=1, let C be the unique triple-type color and let x_C=w_0 in W. For each of the two other points w in W\{w_0}, the six non-special exact colors already use 12 shell edges, and the triple-type color contributes the thirteenth shell edge. Therefore all 13 shell edges at w are non-target exact-color edges, so r_A(w)=0 in the target graph.

The target residual minimum-degree condition gives

\[
d_F(w)=d_H(w)+r_A(w)\ge13.
\]

Since d_H(w)=12+epsilon_w and r_A(w)=0,

\[
\boxed{epsilon_w\ge1}
\]

for both non-special W-points. Thus a triple-type color forces at least two of the six core-excess units onto W.

This is a necessary condition, not yet a contradiction.

## 7. Current frontier after this theorem

The corrected non-full-support argument establishes, without the retracted degree-9 premise:

- v=44,m=10: **PROVED_CONDITIONAL impossible**;
- v=44,m=9: three W-points each carry exactly three special-color labels; all nine special vertices lie in W; at most one exact color is triple type; at least eight are double type; if one triple type occurs, at least two core-excess units lie on W;
- v=44,m=8: still OPEN;
- v=45,46,47: still OPEN under this theorem.

The theorem does not close E408 Q32 as a whole. It is intended as the replacement for the valid shell-capacity portion of the retracted degree-9 route.