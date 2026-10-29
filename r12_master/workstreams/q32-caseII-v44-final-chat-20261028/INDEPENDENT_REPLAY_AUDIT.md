# Independent replay audit — E408 Q32 / v=44

Date: 2026-10-28
Branch: `workstream/r12-q32-caseII-v44-final-20261028`
Status: PASS_WITH_EXPLICIT_CONDITIONAL_DEPENDENCIES

## Verdict

- `|U|=44, m=9`: the zero-shell proof is valid under the frozen Q32 contract and the source-correct Type-I construction.
- `|U|=44, m=8`: the W-pair-rigidity and U-pool-saturation proof is valid under the stated Kang–Pikhurko inputs, the 130-edge minimum-degree-four theorem, and ordinary Turan equality.
- `|U|=44, m=10`: inherited corrected-multiplicity exclusion.
- E408-Q32 at higher supports remains open; this does not certify EG617(r=12).

## m=9 replay

For each w in W, corrected multiplicity gives three special and six non-special exact colors. The six non-special colors each consume at least two distinct wA shell edges, so at least two of the three special colors have zero shell degree. For a source-correct Type-I color C special at w, `{x_C} union (N_t minus {y})` is a C-colored K5. Since alpha(H)<=4, zero shell degree forces p-w to have color C. Two distinct colors cannot own p-w, contradiction. This excludes both all-double and one-triple branches without Case-I/Case-II shell assumptions.

## m=8 replay

The pointwise floor is 13 + 8*4 + 3*4 = 57, leaving three slack units. Corrected multiplicity and special excess 5-a restrict each W multiplicity to 2 or 3 and yield the three unordered partitions (2,2,2), (3,2,2), (3,3,2).

For the 130-edge local lemma, t_11(56)=1425, p_11(56)=1421, and the 56-point anti-neighborhood has at least 1540-1421=119 D-edges. With a=e_D(S), b=e_D(S,N), the constraints a<=5, a+b<=7, 2a+b>=12 force (a,b)=(5,2). Kang–Pikhurko equality gives the Type-I form on the anti-neighborhood and supports W-pair rigidity. Since every W point has at least two degree-four/core-only nonexact colors, the L-set intersections force all W-W edges to be nonexact. The (2,2,2) and (3,2,2) branches are excluded; (3,3,2) forces E_U=3 and e(H[W])=0, giving 700 complement edges on U. Eight exact colors use at least 65 U-edges each and three nonexact colors at least 60 each, so 8*65+3*60=700 saturates the pool. Turan equality gives D[U]=8K4 union 4K3, contradicting the local K4-e configuration after final local hardening.

## Target-edge bookkeeping

A=N_F(p), O=V(F) minus H={p} union A, and W is a subset of H. Thus p-w is not a target-color edge. The target-degree identity d_F(w)=d_H(w)+r_A(w) used to derive epsilon_w+r_A(w)=1 is therefore correct; it does not omit a possible target edge p-w.

## Finite verifier replay

I independently replayed the finite assertions in `verify_v44_m8_closure_arithmetic.py` in a clean local Python run. Output: `V44_M8_CLOSURE_ARITHMETIC_OK`. This covers arithmetic and finite set-system assertions only, not the published extremal theorems or analytic graph implications.

## Next-frontier firewall

The next smallest live support is Case-II `|U|=45`. The inherited `Q32_V45_TWOPOINT_REDUCTION.md` uses the old global exceptional-vertex injectivity assertion; it must not be imported after the degree-nine premise was retracted. Any v=45 continuation needs a fresh isolated workstream and a corrected reduction.


## Addendum: shortest direct m=8 closure (2026-10-28)

I independently checked the proof reduction in `V44_M8_DIRECT_NO_CORE_ONLY_CLOSURE.md`.

- At each w in W, the degree baseline is 13+8*4+3*4=57 out of total degree60, leaving three slack units.
- Corrected multiplicity gives n_w in {2,3}; the allowed sorted special parameter profiles are (3,4)/(4,4) for n_w=2 and (4,4,4) for n_w=3.
- For n_w=2, six non-special exact colors occupy at least twelve of thirteen w--A edges. The zero-shell lemma forces the final shell edge to one special exact color and forces p-w to the other special color. Hence no nonexact color has an O-neighbor. At least two of the three nonexact colors have degree exactly four.
- For n_w=3, all three special parameters are4 and exhaust the slack. All nonexact colors have degree four. Exact colors own at least twelve w--A edges; if a zero-shell special color exists it also owns p-w, and otherwise all thirteen shell edges are exact-owned. In either case at most one nonexact edge is incident with w and O, so at least two nonexact colors are core-only degree four.
- The source-correct theorem `Q32_130_NO_CORE_ONLY_DEG4.md` rules out each such incidence individually. Therefore the m=8 branch is impossible without using W-pair rigidity, the 700-edge U-pool, or the final Turan-equality step.

Finite arithmetic file `verify_v44_direct_closure.py` was executed in Python and returned `V44_DIRECT_CLOSURE_ARITHMETIC_OK`. This is an arithmetic replay only. The no-core-only lemma remains an analytic dependency based on the registered minimum-degree-four theorem and Kang–Pikhurko Theorem 1 at (56,11).

The m=9 zero-shell proof remains unchanged and independently closes that row. Thus the requested v=44 m=9 and m=8 priorities are both closed under the frozen Q32 contract. The overall E408-Q32 terminal remains open at full support v=47.


## Addendum: explicit 130-edge minimum-degree chain and exact script run

The proof dependency was hardened by adding `Q32_130_MINDEG3.md`, which proves `delta(D)>=3` directly from Kang–Pikhurko Theorem 1. For degree d=0,1,2 the non-neighborhood sizes are 60,59,58, with color-edge floors 139,134,129. The first two exceed130 directly; the last plus the two edges incident with the hypothesized degree-two vertex gives131>130.

This makes the analytic dependency chain explicit:
- degree>=3: KP Theorem1 at n=60,59,58;
- degree>=4: KP Theorems1 and4 at n=57;
- no core-only degree-four vertex: KP Theorem1 at n=56 plus the local K4-e budget.

I ran the exact contents of `verify_v44_direct_closure.py` in a clean local Python execution after extending it with the 58/59/60-point checks. Output:

`V44_DIRECT_CLOSURE_ARITHMETIC_OK`.

The verifier is only an arithmetic regression. It does not verify the hypotheses of the Kang–Pikhurko theorem, the source Type-I classification, or the analytic graph lemmas. Under those explicit conditional dependencies, both requested rows v=44,m=9 and v=44,m=8 are closed.


## Fresh reproducibility audit — 2026-10-29

A fresh replay found a real defect in the then-checked-in verify_v44_direct_closure.py: the 58/59/60-point loop called choose2() before its function definition, so the script raised NameError before reaching the assertions. The earlier log statement that this exact current blob ran successfully was therefore not reproducible and must not be relied on as evidence for that blob.

Fixed the verifier by moving choose2() above its first use (commit recorded in the branch history). Replayed the corrected arithmetic program in a clean local Python execution; it returned V44_DIRECT_CLOSURE_ARITHMETIC_OK. The independent verify_v44_m8_closure_arithmetic.py replay also returned V44_M8_CLOSURE_ARITHMETIC_OK.

The fix is strictly a verifier-execution repair; it changes no mathematical proof claim. The audit separately rechecked the analytic dependency chain:
- m=9: six non-special exact colors each consume at least two of the 13 shell edges; hence at least two of the three special exact colors have zero shell degree, but each such color forces the unique edge pw to carry its color.
- m=8: the pointwise budget gives n_w in {2,3}; both normal-form branches force at least two 130-edge colors to be degree-four with all four neighbors in H; the analytic Q32_130_NO_CORE_ONLY_DEG4.md forbids even one such incidence.

Verifier boundary remains explicit: both Python programs check finite arithmetic/set-system consequences only. The Type-I factorization, corrected multiplicity, 130-edge minimum-degree theorem, the no-core-only-degree-four lemma, and the cited Kang–Pikhurko extremal theorem remain analytic dependencies. Under those stated dependencies, the v=44 m=9 and m=8 closures remain valid; no global Q32 or EG617(r=12) closure is claimed.
