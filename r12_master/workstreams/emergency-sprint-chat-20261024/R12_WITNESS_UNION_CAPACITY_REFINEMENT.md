# R12 witness-union capacity refinement

Date: 2026-10-25  
Status: **PROVED core-capacity and witness-hitting lemmas; conditional terminal refinements.**  
Scope: E407 Q32 and E408 Q33 only where their retained shell-support contracts provide the stated exact-129 witness counts. This does not close any terminal.

## 1. Frozen core contract

Let H be a 47-vertex target-color core satisfying

```
e(H) = 284
minimum degree δ(H) ≥ 12
independence number α(H) ≤ 4
```

The total core excess is exactly four:
```
Σ over x in H of ε_x = 2e(H) − 47·12 = 4,
where ε_x = d_H(x) − 12 ≥ 0.
```

Let p4(n) be the minimum number of edges in an n-vertex graph with independence number at most four. It is the edge count of a disjoint union of four cliques whose sizes differ by at most one.

Let Q₁,…,Q_N be independent 4-sets in H such that any two distinct sets share at most one vertex. Write U = union of all Q_i, v = |U|, W = V(H) minus U, and E_U = Σ over x in U of ε_x.

## 2. Core-capacity theorem

**Theorem.** Under the frozen core contract,

```
6N ≤ e(complement of H[U])
   ≤ binom(v,2) − p4(47−v) − 12v + 284 − E_U.
```

In particular, dropping E_U gives a valid weaker bound.

**Proof.**

Each Q_i induces a K₄ in the complement of H[U]. Since distinct Q_i and Q_j share at most one vertex, none of these K₄s shares an edge with another. Hence the complement has at least 6N edges.

Set e_U = e(H[U]), e_W = e(H[W]), and let e_cross be the number of edges between U and W. Summing degrees over U gives
```
e_cross = 12v + E_U − 2e_U.
```
Since e(H)=284,
```
284 = e_U + e_W + e_cross
    = e_W + 12v + E_U − e_U.
```
Thus
```
e_U = e_W + 12v + E_U − 284
    ≥ p4(47−v) + 12v + E_U − 284,
```
because α(H[W])≤4. Subtracting from binom(v,2) and combining with the K₄ packing lower bound proves the theorem. ∎

## 3. Exact numerical capacity table

Define
```
C_v = binom(v,2) − p4(47−v) − 12v + 284.
```
Then e(complement of H[U]) ≤ C_v − E_U ≤ C_v.

| v | p4(47−v) | C_v | Consequence |
|---:|---:|---:|---|
| 28 | 36 | 290 | 49 witnesses impossible: 6N ≥ 294 |
| 29 | 32 | 310 | 56 witnesses impossible: 6N ≥ 336 |
| 30 | 28 | 331 | 56 witnesses impossible: 6N ≥ 336 |
| 31 | 24 | 353 | 64 witnesses impossible: 6N ≥ 384 |
| 32 | 21 | 375 | 64 witnesses impossible: 6N ≥ 384 |
| 33 | 18 | 398 | 72 witnesses impossible: 6N ≥ 432 |

For smaller v, the ordinary four-partite Turán bound already rules out the relevant N. The table gives the sharper core-budget step at the boundary sizes.

## 4. Application to retained exact-129 witness families

These applications are conditional on the retained T61 contracts and the exact-129 Kang–Pikhurko component classification. Each isolated K₅ component disjoint from shell support S supplies an independent 4-set Q inside H: its fifth vertex is either a shell label in B or the pivot p; a component lying wholly in H would contradict α(H)≤4. Across distinct non-target colors, two such Qs share at most one vertex, since a shared pair would assign one edge two colors.

### E407 Q32

There are at least seven exact-129 colors because the residual has 1423 = 11·129 + 4 non-target edges.

- **Templates A/B:** at least seven no-S components per exact-129 color. With exactly seven exact-129 colors, N≥49, so v≥29. With at least eight exact-129 colors, N≥56, so v≥31.
- **Templates C/D/E:** at least eight no-S components per exact-129 color. With exactly seven exact-129 colors, N≥56, so v≥31; the eight disjoint witnesses from one color strengthen this to v≥32. With at least eight exact-129 colors, N≥64, so v≥33.

Thus the only A/B union-size boundary not removed by this theorem is the seven-exact-color case v=29. For C/D/E the remaining seven-exact-color boundary is v=32. These are necessary-structure reductions, not terminal contradictions.

### E408 Q33/d3

There are at least eight exact-129 colors because the residual has 1422 = 11·129 + 3 non-target edges. Let β = e(M[S]).

- If β=0, at most three exact-129 K₅ components can meet S, so at least seven per color are disjoint from S. Hence N≥56 and v≥31.
- If β≥1, at most two such components can meet S, so at least eight per color are disjoint from S. Hence N≥64 and v≥33.

Consequently, the unresolved union-size boundary in this application is β=0, v=31. This does not exclude the seven-block near-Latin completion or prove the remaining boundary impossible.

## 5. Witness-hitting inequality

Let L be the complement of H[U]. Let L₀ be the union of the edge sets of the N witness K₄s, and let R be the number of edges of L not covered by L₀. For x in U, let r_x be the number of witness sets containing x and let d_R(x) be its degree in the leftover graph. Because the witness K₄s are edge-disjoint,
```
d_L(x) = 3r_x + d_R(x).
```
Also
```
d_L(x) = v−1−d_H[U](x)
        = v−13−ε_x+d_W(x),
```
so
```
d_W(x) = 3r_x + d_R(x) − v + 13 + ε_x.
```

Every w in W must have a neighbor in every Q_i; otherwise Q_i together with w is an independent 5-set in H. Therefore
```
Σ over x in U of r_x d_W(x) ≥ N(47−v).
```
Substituting the preceding degree identity and using Σ r_x = 4N gives the exact necessary inequality
```
Σ r_x d_R(x) + Σ r_x ε_x
    ≥ N(3v−5) − 3Σ r_x².
```

This inequality couples witness overlap, uncovered complement edges, and core excess. It does not assume distinct witness neighborhoods or disjoint neighborhoods.

### Boundary consequences

**E407 A/B, seven exact colors, v=29.** Here N=49, r_x≤7 and Σr_x=196. Convexity gives Σr_x²≥1330. Hence the witness-hitting inequality gives
```
Σ r_x d_R(x) + Σ r_x ε_x ≥ 28.
```
Since Σd_R(x)=2R, this implies 14R+7E_U≥28, or
```
2R + E_U ≥ 4,     R + E_U ≤ 16.
```
The second inequality is the core-capacity bound C₂₉=310 with e(L)=294+R.

**E407 C/D/E, seven exact colors, v=32.** Here N=56, r_x≤7 and Σr_x=224 across 32 vertices, so every r_x=7. The witness-hitting inequality yields
```
14R + 7E_U ≥ 392,
2R + E_U ≥ 56,     R + E_U ≤ 39.
```
As E_U≤4, at least 26 complement edges remain uncovered by the 56 witness K₄s.

**E408 Q33/d3, β=0, eight exact colors, v=31.** Here N=56, r_x≤8 and Σr_x=224. The minimum possible square sum is 1624, so
```
Σ r_x d_R(x) + Σ r_x ε_x ≥ 56,
2R + E_U ≥ 7,     R + E_U ≤ 17.
```
As E_U≤4, at least two complement edges remain uncovered by the 56 witness K₄s.

These are sharper necessary conditions on the remaining boundary kernels, not contradictions.

## 6. Non-transfer and dependencies

- **E408 Q32 is not covered.** Its core has 285 edges and excess six, and the required exhaustive shell-support split M[B]=∅ has not been certified for Q32. The 284-edge table and Q33 component counts must not be imported into Q32 without a matching reduction.
- The core-capacity and witness-hitting lemmas themselves use only e(H)=284, δ(H)≥12, α(H)≤4, and the stated pairwise-linear witness family.
- The terminal applications additionally use the retained exact-129 color-factor classification, applicable shell-support split, and component counts.
- No result here proves that any remaining union or parent graph is realizable; no E407/E408 terminal is closed.

## 7. Immediate next attack

Attack the three sharpened boundary kernels separately:
1. E407 A/B, seven exact-129 colors, v=29;
2. E407 C/D/E, seven exact-129 colors, v=32;
3. E408 Q33, β=0, eight exact-129 colors, v=31.

For each, combine the near-Turán structure of the complement of H[U] with per-color parallel classes and labelled shell-row incidences. Do not assume the witness blocks form a complete transversal design unless equality in the relevant edge cap is actually forced.
