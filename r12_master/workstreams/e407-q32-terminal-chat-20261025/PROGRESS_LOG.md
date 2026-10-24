# E407 Q32 terminal — progress log

## 2026-10-25 — Round 1

### New mathematical result

**Proved conditionally:** the delta=16 minimum-support boundary is automatically four-partite and reduces to one labelled core kernel.

The proof uses the 49 linear K4 witnesses, the exact core ledger, Brouwer's second-Turan bound, equality in Turan on 18 vertices, and the total degree-excess budget. It excludes endpoint splits (4,1) and (3,2) for the five cross edges in H[U].

The sole surviving endpoint allocation is (5,0): all five distinct D-endpoints have the same K4 as their exact W-neighbourhood, and that K4 is complete to D. Each vertex in the other three W-components must be complete to a 7-part; labels may vary within a component, and no component-wide bijection is proved.

### Verification

Ran the local arithmetic/kernel audit script. Output: E407_DELTA16_STRUCTURAL_KERNEL_ARITHMETIC_OK.

The script checks exact edge ledgers, integer partition profiles, and finite excess inequalities. It does not verify graph realization, all graph-theoretic lemmas, or the original K145 theorem.

A reverse-saturation lemma was also proved: every vertex of W is complete to exactly one U-part. The proof handles the exceptional possibility of a 13-neighbour W-vertex and excludes it by the four-endpoint K4 degree contradiction.

### Global effect

- New closed contracts: 1 structural reduction (delta=16 boundary).
- Fully excluded E407 templates: 0.
- Remaining E407 minimum-support branches: delta<=15 (four-partite and non-four-partite), plus the surviving delta=16 kernel.
- E408 Q32/Q33: untouched.
- Original T61-to-K145 bridge: still OPEN / NOT_CERTIFIED.

### Next attack

Combine the forced vertex-level U-part neighbourhoods and common-K4 endpoint structure with the exact row/hub requirements of templates A-E. In parallel, use the near-Turan classification for delta=14,15 to bound the remaining cross edges in H[W]. Do not claim any template closed until an actual incompatibility proof is obtained.


## 2026-10-25 — Round 2: delta=16 excluded

### New mathematical result

The previous round's labelled \(\delta=16\) kernel is now eliminated completely under the frozen E407 Q32 core/witness contract.

The key missing terminal step was the \((5,0)\) endpoint split. In that case:
1. The \(K_4\) containing all five \(D\)-endpoints cannot be complete to a 7-part (that would require at least three excess units at each of its four vertices), so it is complete to \(D\).
2. The other \(K_4\) and both \(K_5\) components cannot be complete to \(D\), and reverse saturation forces every vertex of those components to be complete to a 7-part.
3. The three non-endpoint vertices of \(D\) each have five neighbours in \(W\), hence each is complete to one of the two \(K_5\) components. Two must choose the same \(K_5\).
4. Every vertex of that \(K_5\) then has at least seven neighbours in a small part plus two \(D\)-neighbours, so it needs at least one degree-excess unit. Five vertices require at least five excess units, contradicting the core's total excess four.

The \((4,1)\) and \((3,2)\) splits remain excluded by the earlier degree-excess arguments. Thus all three possible endpoint splits are impossible and \(\delta=16\) is excluded.

### Verification scope

The arithmetic verifier is being updated to include the final \(5>4\) excess contradiction. The mathematical proof is in FOUR_PARTITE_TERMINAL.md. The verifier is a consistency check only and does not independently certify graph-realization or the upstream T61 / exact-129 inputs.

### Global effect

- E407 Q32: \(\delta=16\) boundary closed by contradiction under the retained core/witness contract.
- E407 Q32 overall: **OPEN / NOT_CERTIFIED**.
- Remaining core-ledger values: \(\delta\le15\), including four-partite and non-four-partite branches.
- E408 Q32/Q33 and the original \(K_{145}\)-to-T61 bridge: untouched and still open.

### Next attack

Prioritize \(\delta=15\) first: it is the sharp second-Turán boundary for a non-four-partite \(K_5\)-free graph on 29 vertices, while the four-partite branch has only one degree-excess unit on \(U\). Then handle \(\delta=14\), and only after those near-extremal cases inspect \(\delta\le13\). Do not infer the remaining \(\delta\le15\) cases are excluded by the \(\delta=16\) argument.
