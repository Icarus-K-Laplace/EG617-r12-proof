# E408 Q32 — source-complete exact-color core-edge bounds

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL structural theorem** under the Q32 residual/core contract and Kang–Pikhurko equality classification.

## 1. Setup

Let \(V=H\dot\cup O\), with \(|H|=47\), \(|O|=14\). Let C be an exact-129 non-target color on V. Balancedness gives \(\alpha(C)\le12\), and the Q32 target core has \(\alpha(H)\le4\).

The universal partition theorem V47_EXACT129_UNIVERSAL_PARTITION.md already shows that every such C induces one of:
\[
11K_4+K_3,\quad 10K_4+2K_3+K_1,\quad 11K_4+K_2+K_1.
\]
We now bound the number of C-edges inside H without assuming Type I or omega(C)<=5.

Also, since \(\alpha(C[H])\le12\), the ordinary Turán-complement floor on 47 vertices is
\[
e(C[H])\ge p_{12}(47)=\binom{47}{2}-t_{12}(47)
=1081-(11\binom42+\binom32)=69.
\]

## 2. If G=bar(C) is 12-partite

Choose a 12-partition \(P_1,\ldots,P_{12}\) of G. Each P_i is a C-clique, so \(P_i\cap H\) is independent in H and has size at most four. The intersections partition H and therefore have sizes \(4^{11},3\). They contribute exactly 69 C-edges inside H.

The partition sizes \(s_i=|P_i|\) sum to 61. Convexity gives
\[
\sum_i\binom{s_i}{2}\ge 11\binom52+\binom62=125.
\]
Since C has 129 edges total, there are at most four C-edges crossing the 12-partition. Hence
\[
\boxed{69\le e_C(H)\le73.}
\]

## 3. If G=bar(C) is not 12-partite

Kang–Pikhurko Theorem 1 applies because G is K13-free and non-12-partite. At
\[
e(G)=1830-129=1701=p_{12}(61),
\]
Theorems 4 and Lemma 5 show that G is one of the equality constructions with old part sizes
\[
(5^{12}),\quad(4,5^{10},6),\quad(4,4,5^8,6,6).
\]
The two special parts \(N_s,N_t\) have sizes respectively \((5,5)\), \((4,5)\), or \((4,4)\). Thus
\[
n_s\le5,\qquad 1\le a=|A|\le n_s-1\le4.
\]
The complement color graph C consists of the cliques \(N_i\) plus the gadget edges
\[
x(N_s\setminus A),\qquad x(N_t\setminus\{y\}),\qquad yA.
\]

Let
\[
h_i=|N_i\cap H|\le4,\qquad d_i=4-h_i\ge0.
\]
If x is outside H, \(\sum_i h_i=47\), so \(\sum_i d_i=1\) and the internal clique contribution is 69. If x is in H, \(\sum_i h_i=46\), so \(\sum_i d_i=2\); the internal clique contribution is 66 for the two-double shape and 67 for the triple shape.

Write \(d_s,d_t\) for the deficits of the two special parts and \(o_A=|A\cap O|\).

### 3.1 x outside H

All x-gadget edges leave H. Only yA can contribute, and it contributes at most a edges. Therefore
\[
69\le e_C(H)=69+\mathbf1_{y\in H}|A\cap H|
\le69+a\le73.
\]

### 3.2 x in H and y in H

The gadget edges inside H are exactly
\[
|N_s\setminus A\cap H|+|N_t\setminus\{y\}\cap H|+|A\cap H|
=h_s+h_t-1=7-d_s-d_t.
\]
Since \(d_s+d_t\le2\),
\[
5\le G_C^H\le7.
\]
Consequently:
- two-double shape: \(e_C(H)=66+G_C^H\in[71,73]\);
- triple shape: \(e_C(H)=67+G_C^H\in[72,74]\).

### 3.3 x in H and y outside H

The gadget edges inside H are
\[
G_C^H=|N_s\setminus A\cap H|+|N_t\cap H|
=h_s-(a-o_A)+h_t
=8-d_s-d_t-a+o_A.
\]
Using \(d_s+d_t\le2\), \(a\le4\), and \(0\le o_A\le a\), we obtain
\[
2\le G_C^H\le8.
\]
Consequently:
- two-double shape: the raw range is \(68\le e_C(H)\le74\), and the balanced-coloring Turán floor improves the lower endpoint to 69;
- triple shape: \(69\le e_C(H)\le75\).

## 4. Universal exact-color conclusion

Combining the 12-partite and non-12-partite cases:
\[
\boxed{69\le e_C(H)\le75\quad\text{for every exact-129 color C}.}
\]
Equivalently, for the 37-unit core gap \(g_C=e_C(H)-69\),
\[
0\le g_C\le6.
\]
The more precise placement-sensitive intervals are:

| Source case | H-partition | \(e_C(H)\) | Gap \(g_C\) |
|---|---|---:|---:|
| \(\bar C\) 12-partite | \(11K_4+K_3\) | 69–73 | 0–4 |
| nonpartite, x outside H | \(11K_4+K_3\) | 69–73 | 0–4 |
| nonpartite, x in H, y in H, two-double | \(10K_4+2K_3+K_1\) | 71–73 | 2–4 |
| nonpartite, x in H, y in H, triple | \(11K_4+K_2+K_1\) | 72–74 | 3–5 |
| nonpartite, x in H, y outside, two-double | \(10K_4+2K_3+K_1\) | 69–74 | 0–5 |
| nonpartite, x in H, y outside, triple | \(11K_4+K_2+K_1\) | 69–75 | 0–6 |

No \(\omega(C)\le5\), \(\omega(H)\le5\), or Type-I-only hypothesis is used.

## 5. Q32 witness-interface corollary

The three H-partition shapes contain respectively 11, 10, or 11 disjoint independent 4-sets. Each is a monochromatic K4 in C[H]. Therefore every exact-129 color supplies at least ten pairwise vertex-disjoint core-four witnesses.

Witnesses from distinct colors intersect in at most one vertex: otherwise a shared pair would have two colors. This is exactly the ten-witness input required by Q32_U_COLOR_RESERVE.md. The latter's condition \(\omega(C[U])\le4\) follows from \(\alpha(H)\le4\), and \(\alpha(C[U])\le12\) follows from balancedness.

This repairs the **ten-witness reserve interface** without a Type-I K5 factorization. It does not provide a distinguished special point x in the 12-partite case, nor does it supply the pivot-adjacent four-set required by the current full-support pivot-packing CSP. Those stronger interfaces must not be inferred from this theorem.

## 6. Scope

This theorem validates the exact-color core-edge cap and the ten-disjoint-K4 witness count under all source modes. It does not close Q32. The Hall/tight-part lemma forces a K6/K7 in H, which is permitted by \(\omega(H)\le11\). The full-support m=8/9 terminal remains OPEN / NOT_CERTIFIED.
