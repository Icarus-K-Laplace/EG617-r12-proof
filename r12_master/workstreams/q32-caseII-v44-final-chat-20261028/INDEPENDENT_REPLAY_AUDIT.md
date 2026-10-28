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
