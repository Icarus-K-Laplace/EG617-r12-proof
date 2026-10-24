# R12 witness-union capacity refinement

Date: 2026-10-25  
Status: **PROVED core-capacity lemma; conditional terminal refinements**.  
Scope: E407 Q32 and E408 Q33 only where their retained shell-support contracts provide the stated numbers of exact-129 witnesses. This does not close any terminal.

## 1. Frozen core contract

Let (H) be a 47-vertex target-color core satisfying
[
e(H)=284,qquad delta(H)ge 12,qquad alpha(H)le 4.
]
Thus
[
sum_{xin V(H)}(d_H(x)-12)=2e(H)-47cdot12=4.
]
For (nge0), let (p_4(n)) be the minimum number of edges in an (n)-vertex graph with independence number at most four. By Turán's theorem for the complement, this is the edge count of a disjoint union of four cliques whose sizes differ by at most one.

Let (Q_1,ldots,Q_N) be independent 4-sets in (H) such that
[
|Q_icap Q_j|le1quad(i
e j).
]
Write (U=igcup_iQ_i), (v=|U|), (W=V(H)setminus U), and (E_U=sum_{xin U}(d_H(x)-12)ge0).

## 2. Core-capacity theorem

**Theorem.** Under the frozen core contract,
[
oxed{
6Nle e(overline{H[U]})
le inom v2-p_4(47-v)-12v+284-E_U.
}
]
In particular, the weaker bound obtained by dropping (E_U) is valid.

**Proof.**

Every (Q_i) induces a (K_4) in (overline{H[U]}). Since distinct (Q_i,Q_j) share at most one vertex, no edge belongs to two of these (K_4)'s. Hence
[
e(overline{H[U]})ge 6N. 	ag{1}
]

Set (e_U=e(H[U])), (e_W=e(H[W])), and let (e_	imes) be the number of edges between (U) and (W). Summing degrees over (U) gives
[
e_	imes=12v+E_U-2e_U.
]
Since (e(H)=284),
[
284=e_U+e_W+e_	imes
=e_W+12v+E_U-e_U.
]
Therefore
[
e_U=e_W+12v+E_U-284
ge p_4(47-v)+12v+E_U-284, 	ag{2}
]
because (alpha(H[W])le4). Subtracting (2) from (inom v2) and combining with (1) proves the theorem. (square)

## 3. Exact numerical capacity table

Define
[
C_v=inom v2-p_4(47-v)-12v+284.
]
Then (e(overline{H[U]})le C_v-E_Ule C_v).

| (v) | (p_4(47-v)) | (C_v) | Consequence |
|---:|---:|---:|---|
| 28 | 36 | 290 | 49 witnesses impossible: (6Nge294) |
| 29 | 32 | 310 | 56 witnesses impossible: (6Nge336) |
| 30 | 28 | 331 | 56 witnesses impossible: (6Nge336) |
| 31 | 24 | 353 | 64 witnesses impossible: (6Nge384) |
| 32 | 21 | 375 | 64 witnesses impossible: (6Nge384) |
| 33 | 18 | 398 | 72 witnesses impossible: (6Nge432) |

For smaller (v), the ordinary four-partite Turán bound already rules out the relevant (N). The table gives the sharper core-budget step at the boundary sizes.

## 4. Application to retained exact-129 witness families

The following applications are conditional on the retained T61 contracts and the exact-129 Kang–Pikhurko component classification. Each isolated (K_5) component disjoint from the shell support (S) supplies an independent 4-set (Qsubseteq H): its fifth vertex is either a shell label in (B) or the pivot (p); a component lying wholly in (H) would contradict (alpha(H)le4). Across distinct non-target colors, two such (Q)'s share at most one vertex, since a shared pair would assign one edge two colors.

### E407 Q32

There are at least seven exact-129 colors because the residual has (1423=11cdot129+4) non-target edges.

- **Templates A/B:** at least seven no-(S) components per exact-129 color. With exactly seven exact-129 colors, (Nge49), so (vge29). With at least eight exact-129 colors, (Nge56), so (vge31).
- **Templates C/D/E:** at least eight no-(S) components per exact-129 color. With exactly seven exact-129 colors, (Nge56), so (vge31); the eight disjoint witnesses from one color strengthen this to (vge32). With at least eight exact-129 colors, (Nge64), so (vge33).

Thus the only A/B union-size boundary not removed by this theorem is the seven-exact-color case (v=29). For C/D/E the remaining seven-exact-color boundary is (v=32). These are necessary-structure reductions, not terminal contradictions.

### E408 Q33/d3

There are at least eight exact-129 colors because the residual has (1422=11cdot129+3) non-target edges. Let (eta=e(M[S])).

- If (eta=0), at most three exact-129 (K_5) components can meet (S), so at least seven per color are disjoint from (S). Hence (Nge56) and (vge31).
- If (etage1), at most two such components can meet (S), so at least eight per color are disjoint from (S). Hence (Nge64) and (vge33).

Consequently, the unresolved union-size boundary in this application is (eta=0, v=31). This does not exclude the seven-block near-Latin completion or prove the remaining boundary impossible.

## 5. Non-transfer and dependencies

- **E408 Q32 is not covered.** Its core has 285 edges and excess six, and the required exhaustive shell-support split (M[B]=arnothing) has not been certified for Q32. The 284-edge table and Q33 component counts must not be imported into Q32 without a matching reduction.
- The core-capacity theorem itself uses only (e(H)=284), (delta(H)ge12), and (alpha(H)le4).
- The application uses the retained exact-129 color-factor classification, the applicable shell-support split, and the stated component counts.
- No result here proves that any remaining union or parent graph is realizable; no E407/E408 terminal is closed.

## 6. Immediate next attack

Attack the three sharpened boundary kernels separately:
1. E407 A/B, seven exact-129 colors, (v=29);
2. E407 C/D/E, seven exact-129 colors, (v=32);
3. E408 Q33, (eta=0), eight exact-129 colors, (v=31).

For each, combine the near-Turán structure of (overline{H[U]}) with the per-color parallel classes and the labelled shell-row incidences. Do not assume the witness blocks form a complete transversal design unless equality in the relevant edge cap is actually forced.
