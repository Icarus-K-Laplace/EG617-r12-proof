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
- **All templates A–E, safe count:** at least seven no-S components per exact-129 color. The core part Q of a component containing pivot p is still an independent 4-set in H, so it contributes to the total Q-family even though it is not B-labelled. With exactly seven exact-129 colors, N≥49 and v≥29; with at least eight exact-129 colors, N≥56 and v≥31.
- **Audit restriction:** the stronger claim of eight no-S components per color in templates C/D/E is not certified by the current contracts. An edge among two S-vertices permits them to share a non-target K5 but does not force that co-location. Do not use N≥56 (or v≥32) for seven-color C/D/E without a separate color-specific lemma.

Thus the core-capacity theorem alone leaves the seven-exact-color boundary v=29 for every E407 template. With at least eight exact-129 colors it gives v≥31. These are necessary-structure reductions, not terminal contradictions.

### E408 Q33/d3

There are at least eight exact-129 colors because the residual has 1422 = 11·129 + 3 non-target edges. Let β = e(M[S]).

- If β=0, at most three exact-129 K₅ components can meet S, so at least seven per color are disjoint from S. Hence N≥56 and v≥31.
- If β≥1, the safe universal count remains at least seven no-S components per color; β>0 alone does not force two S-vertices to co-locate in one component. Thus N≥56 and v≥31 still hold from eight exact-129 colors, but N≥64/v≥33 is not established.

Consequently, the core-capacity boundary is v=31 for E408 Q33 regardless of β. This does not exclude the seven-block near-Latin completion or prove the remaining boundary impossible.

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

**Conditional algebra only (not an E407 C/D/E application).** If some separately certified argument supplies N=56 pairwise-linear witnesses on v=32 vertices with at most seven occurrences per vertex, then r_x=7 for every x and the witness-hitting inequality gives
```
2R + E_U ≥ 56,     R + E_U ≤ 39.
```
This would force R≥26, but the present exact-129 count contract does not establish N=56 for seven-color E407 C/D/E, so this conditional calculation is not used to shrink that terminal.

**E408 Q33/d3, eight exact colors, v=31.** Here N=56, r_x≤8 and Σr_x=224. The minimum possible square sum is 1624, so
```
Σ r_x d_R(x) + Σ r_x ε_x ≥ 56,
2R + E_U ≥ 7,     R + E_U ≤ 17.
```
As E_U≤4, at least two complement edges remain uncovered by the 56 witness K₄s. This calculation is valid for all β, using the safe seven-witness-per-color floor.

These are sharper necessary conditions on the remaining boundary kernels, not contradictions.

## 6. Non-transfer and dependencies

- **E408 Q32 is not covered.** Its core has 285 edges and excess six, and the required exhaustive shell-support split M[B]=∅ has not been certified for Q32. The 284-edge table and Q33 component counts must not be imported into Q32 without a matching reduction.
- The core-capacity and witness-hitting lemmas themselves use only e(H)=284, δ(H)≥12, α(H)≤4, and the stated pairwise-linear witness family.
- The terminal applications additionally use the retained exact-129 color-factor classification, applicable shell-support split, and component counts.
- No result here proves that any remaining union or parent graph is realizable; no E407/E408 terminal is closed.

## 7. Immediate next attack

Attack the three sharpened boundary kernels separately:
1. E407, any template, exactly seven exact-129 colors, v=29;
2. E407, at least eight exact-129 colors, v≥31;
3. E408 Q33, eight exact-129 colors, v=31 for any β.

For each, combine the near-Turán structure of the complement of H[U] with per-color parallel classes and labelled shell-row incidences. Do not assume the witness blocks form a complete transversal design unless equality in the relevant edge cap is actually forced.


## Cross-branch audit correction (2026-10-25)

The latest ultimate-closure and witness-packing sibling heads were refreshed before using this note. Their audit correctly warns that `omega(M[S])<=2` does not imply that an S-edge's endpoints lie in the same non-target K5 component. The earlier beta-sensitive claim “β≥1 gives eight no-S components per color” is withdrawn here. The core-capacity and witness-hitting theorems remain valid; only the unsupported E407 C/D/E and E408 β>0 applications are removed. See `R12_CROSS_BRANCH_AUDIT_AND_S0_REPAIR.md`.
