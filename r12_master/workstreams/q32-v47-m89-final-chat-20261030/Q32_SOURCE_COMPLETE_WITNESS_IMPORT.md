# Q32 source-complete witness interface — parent import candidate

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL structural import; no Q32 closure claimed.**

## 1. What the parent currently needs

The parent Q32 core terminal records that every exact-129 color supplies at least ten pairwise-disjoint independent core-four witnesses, and Q32_U_COLOR_RESERVE.md uses exactly this ten-K4 input. The old parent wording attributes it to a universal Type-I twelve-K5 factorization. That attribution is too strong for EG617: the balanced-coloring hypotheses do not imply Type I for every exact color.

The new source-complete argument proves the required ten-K4 conclusion without Type I.

## 2. Exact-129 source-complete partition

For every exact-129 color C on the 61-point residual:
- balancedness gives alpha(C)<=12;
- if bar(C) is 12-partite, the 12 independent parts of bar(C) induce 11K4+K3 on H;
- if bar(C) is not 12-partite, Kang–Pikhurko Theorems 1, 4 and Lemma 5 give all three equality profiles, whose part intersections with H induce one of 11K4+K3, 10K4+2K3+K1, 11K4+K2+K1.

The full proof and incidence arithmetic are in V47_EXACT129_UNIVERSAL_PARTITION.md.

## 3. Ten disjoint core-four witnesses

Every part in the induced H-partition is a C-clique and hence an independent set in H. The three possible shapes contain respectively:
- 11 disjoint 4-sets;
- 10 disjoint 4-sets;
- 11 disjoint 4-sets.

Therefore every exact-129 color supplies at least ten vertex-disjoint monochromatic C-K4s inside H.

If C and D are distinct colors, a C-K4 and a D-K4 cannot share two vertices, because their common pair would have two colors. Thus the witness family is pairwise linear across colors.

This is exactly the witness input required by Q32_U_COLOR_RESERVE.md. Its other hypotheses are:
- alpha(C[U])<=12 from balancedness;
- omega(C[U])<=4 because alpha(H)<=4 and U⊂H.

No omega(C)<=5, omega(H)<=5, or Type-I source mode is used.

## 4. Source-complete core-edge bound

V47_EXACT129_CORE_EDGE_BOUNDS.md also proves, for every exact color,
\[
69\le e_C(H)\le75.
\]
The upper bound is source-complete across:
- 12-partite complement;
- non-12-partite profiles (5^12), (4,5^10,6), and (4,4,5^8,6,6);
- all allowed placements of the special point x and the gadget vertex y.

The corresponding gap \(g_C=e_C(H)-69\) lies in [0,6], as required by the 37-unit parent ledger.

## 5. What this does NOT supply

The 12-partite complement case has no canonical special point x. The theorem therefore does not prove:
- a special-point multiplicity bound \(n_w\ge m-6\);
- a universal pivot-adjacent K4 \(Q_C\) for a fixed outside pivot p;
- the pivot-pair perfect-matching system used in the current v=47 CSP;
- the non-full-support closure \(v=44,45,46\) when those proofs use special-point labels;
- the full-support m=8 or m=9 contradiction.

The current high-support Type-I solver/verifier remain restricted diagnostics. The source-complete ten-witness theorem is a valid parent import for the reserve lemma, not a Q32 closure theorem.

## 6. Parent-facing recommended correction

In Q32_CORE285_TERMINAL.md, replace the sentence “the valid Type-I equality structure gives twelve disjoint color-K5s plus the special vertex x” with:

> For each exact-129 color, the source-complete exact-129 partition theorem (including both the 12-partite complement case and all Kang–Pikhurko non-12-partite equality profiles) induces one of three independent-part partitions of H. Hence every exact color supplies at least ten disjoint monochromatic core K4 witnesses, pairwise linear across colors. The theorem does not supply a universal special point x or a fixed-pivot K4.

Keep the special-point multiplicity and pivot-adjacency arguments as separate dependencies; do not derive them from the ten-witness theorem.

## 7. Status

This is a source-complete repair of the **ten-witness / core-edge interface**. The forced K6/K7 in H is allowed under omega(H)<=11. E408/Q32 full support remains OPEN / NOT_CERTIFIED, and the parent root branch has not been modified.
