# E408 Q32 v=44 final — progress log

Date: 2026-10-28
Branch: `workstream/r12-q32-caseII-v44-final-20261028`
Base: `937a905ed26e54ec10e9bdade1d9b655da8f6176`

## Commit / theorem ledger

### 1. m=9 zero-shell obstruction

Commit: `fa038a6df3913eae88efbe61510550edefe2e963`

File: `V44_M9_PARAMETER_SYSTEM.md`

Advance:

- proved that a special exact color with zero shell degree at w must own pw;
- therefore at most one special exact color at a fixed W-point can be zero-shell;
- six non-special exact colors consume at least twelve shell edges, forcing at least two zero-shell specials;
- concluded `|U|=44,m=9` impossible.

### 2. m=9 all-double explicit closure

Commit: `9acc4c9506fe8ac20b939c16458cd6ea9dce4095`

File: `V44_M9_ALL_DOUBLE_CLOSURE.md`

Advance:

- recorded a standalone all-double closure with no scalar shell-floor dependency.

### 3. m=9 one-triple explicit closure

Commit: `d66a60c9d5d2ba9fc2d460a3c6ce2eb5426ab972`

File: `V44_M9_TRIPLE_CLOSURE.md`

Advance:

- recorded a standalone one-triple closure;
- at each W-point non-special to the triple color, all thirteen shell edges are already occupied by non-special exact colors, making the contradiction even stronger.

### 4. m=8 normal form

Commit: `543df084ccc8d9ad3936fa9336f6724cd007bbc2`

File: `V44_M8_NORMAL_FORM.md`

Advance:

- updated nonexact pointwise floor to12 using the 130-edge min-degree-four theorem;
- reduced W multiplicities to `(2,2,2)`, `(3,2,2)`, `(3,3,2)`;
- derived n=2 shell equality and source profiles `(4,4)/(4,3)`;
- derived n=3 profile `(4,4,4)`.

### 5. full-color ownership ledger / degree-four local rigidity

Commit: `9c68db8daf06ad81798fa717999935bd927ff121`

File: `FULL_COLOR_EDGE_OWNERSHIP_LEDGER.md`

Advance:

- proved the degree-four 130-color local `K4-e` structure at n=2 W-points;
- audited outside-W exact special geometry;
- recorded that shell-only scalar/factor relaxations are feasible and therefore cannot be promoted to UNSAT.

### 6. 130-color W-pair rigidity

Commit: `d872bd5ea88d11f3e4e5de582c1ae8fd84c97fd2`

File: `V44_M8_PAIR_RIGIDITY.md`

Advance:

- used Kang--Pikhurko equality at `(56,11)` to prove:

`D degree4/core-only at u and v => uv has color D`.

This is the key graph-level coupling absent from the earlier scalar ledger.

### 7. complete m=8 closure

Commit: `ac68be5406e23cfd01f157311e33bdea863e4aff`

File: `V44_M8_CLOSURE.md`

Advance:

- proved every W-point has at least two degree4/core-only nonexact colors;
- forced all W--W edges nonexact;
- closed `(2,2,2)` and `(3,2,2)` by outside-W exact edge ownership;
- reduced `(3,3,2)` to all `a=4`, all-double exact colors with `E_U=3`, `e_H(W)=0`;
- proved each exact color uses at least65 U-edges;
- saturated the 700-edge U-complement pool;
- forced each nonexact color to `8K4 dot-union 4K3` on U;
- contradicted that equality structure with the local `K5-e` W-pair cluster.

Result:

> `|U|=44,m=8` CLOSED.

### 8. arithmetic regression verifier

Commit: `f25cb06b136e87d29b51c0120e92d03defca5c0c`

File: `verify_v44_m8_closure_arithmetic.py`

Executed in-session with output:

`V44_M8_CLOSURE_ARITHMETIC_OK`.

Scope is arithmetic/set-system only; it does not verify the external theorems or analytic graph lemmas.

### 9. normal-form promotion

Commit: `be207080bc80c823920c8f33654002622cfd38ea`

File: `V44_M8_NORMAL_FORM.md`

Advance:

- replaced the historical OPEN status with closure pointers and the final dependency chain.

### 10. final ownership ledger

Commit: `692ffbc38ac1d22a7eb0da28de746218c9a517fa`

File: `FULL_COLOR_EDGE_OWNERSHIP_LEDGER.md`

Advance:

- promoted the ledger to m=8/m=9 CLOSED;
- recorded the final pair-rigidity and U-saturation route.

### 11. canonical state

Commit: `b3a1697b1191b26772a9bf6e0b27bdcbf3035649`

File: `CANONICAL_STATE.md`

Advance:

- promoted the result from Case-II-only target to the stronger full `|U|=44` support closure;
- identified Case-II `|U|=45` as the next smallest-support OPEN Q32 layer.

### 12. dependency audit

Commit: `2d031771fbf68f5873c89f7dd218f816ea11d710`

File: `DEPENDENCY_AUDIT.md`

Advance:

- froze the allowed source-correct dependency DAG;
- documented all external theorem use;
- explicitly firewalled degree-nine / injectivity / Q33 / E407 / Case-I-cover routes;
- flagged stale upstream `L_8=9` summary bookkeeping as superseded by the proved 130-edge min-degree-four theorem (`L_8=12`).

### 13. pair-rigidity local equality hardening

Commit: `c18e964052b2df20aca24816f9f570af808b5410`

File: `V44_M8_PAIR_RIGIDITY.md`

Advance:

- expanded `(a,b)=(5,2)` into the forced S--N edge placement;
- proved the two missing-pair endpoints receive exactly one cross edge each;
- proved the two central vertices receive no cross edge and therefore have global D-degree exactly four.

This removes an implicit inference used by the final local contradiction.

### 14. final K5-e hardening

Commit: `22728f19dbfb7d261b71caf7a033c44fb9983922`

File: `V44_M8_FINAL_LOCAL_HARDENING.md`

Advance:

- proved the three size-two L-sets are exactly the three distinct two-subsets of the nonexact-color set;
- therefore each nonexact color owns exactly one W--W edge, excluding the third W-point from the relevant neighbor set;
- gave a fully explicit missing-endpoint contradiction using the forced `(1,1,0,0)` S--N cross-edge distribution;
- concluded the other three vertices of the local K4-e lie in U before invoking `D[U]=8K4 dot-union 4K3`.

### 15. verifier expansion

Commit: `e98b13e9df82ae47f7134098111b2a388a2655d2`

File: `verify_v44_m8_closure_arithmetic.py`

Advance:

- added the unique S--N cross-edge distribution check `(1,1,0,0)`;
- enumerated all six ordered legal L-set assignments and verified each nonexact color owns exactly one W--W edge;
- added the finite missing-endpoint neighbor-count regression (`3` induced edges versus `5` for `K4-e`).

Re-executed successfully with output:

`V44_M8_CLOSURE_ARITHMETIC_OK`.

### 16. branch-scope audit

Compared base `937a905ed26e54ec10e9bdade1d9b655da8f6176` to hardened head `e98b13e9df82ae47f7134098111b2a388a2655d2`.

Result:

- branch is 16 commits ahead and 0 behind;
- every changed path is under `r12_master/workstreams/q32-caseII-v44-final-chat-20261028/`;
- no sibling workstream was modified.

## Final mathematical status of this sprint

`|U|=44,m=10`: inherited CLOSED.

`|U|=44,m=9`: CLOSED in this workstream.

`|U|=44,m=8`: CLOSED in this workstream, with the final local K5-e step independently hardened.

Therefore

> **E408-Q32 / |U|=44 is CLOSED.**

The new m=8/m=9 arguments do not use the Case-I/Case-II shell dichotomy, so this is a support-level closure rather than only a Case-II closure.

## Global promotion status

Do not promote EG617(r=12) to proved.

The smallest remaining Q32 support is `|U|=45`. Inherited Case I v=45 is closed, so the next smallest-support OPEN terminal is

> **Case II / |U|=45**.

Higher-support Q32 terminals at v=46,47 also remain outside this workstream.

### 17. Source-correct v45 pointwise normal form

Files:
- `V45_SOURCE_CORRECT_CLOSURE.md`
- `verify_v45_source_correct_profiles.py`

Advance:
- corrected nonexact pointwise floors to `L_8=12`, `L_9=7`, `L_10=2`; the inherited `L_9=6` summary is stale because the 130-edge color has minimum degree four and the 131-edge color minimum degree three;
- combined `9-a=4+(5-a)` with corrected multiplicity `n_w>=m-6` to obtain `n_w in {2,3}`, `{3,4}`, `{4,5}` for m=8,9,10;
- used the zero-shell/pivot-edge obstruction and thirteen-edge shell capacity to exclude m=10 and reduce m=9 to `n_w=4` at both W-points, with every exact color double type;
- proved the m=9 normal form forces the 130-edge and 131-edge colors to be core-only at both W-points;
- reduced m=8 to at least two core-only degree-four 130-color incidences at each W-point.

### 18. New 130-edge no-pair theorem

File: `Q32_130_NO_TWO_CORE_ONLY_DEG4.md`

Advance:
- proved every degree-four vertex in a 130-edge color has at least five edges induced by its four-neighbor set;
- hardened the local `K4-e` equality/cross-edge structure at any core-only degree-four vertex;
- combined the nonadjacent and adjacent cases to prove that no two distinct core-only degree-four vertices can coexist in one 130-edge color.

This is an analytic consequence of the registered minimum-degree-four theorem and Kang–Pikhurko Theorems 1 and 4 at (56,11); no injectivity premise is used.

### 19. Full v45 support closure

Commit: `8febaee09b07788c01ec22bac2ecbfce51dc1935`

File: `V45_SOURCE_CORRECT_CLOSURE.md`

Result:

> **`|U|=45` is CLOSED for m=8,9,10 under source-correct premises.**

- m=10: both allowed multiplicities `n_w=4,5` force at least two zero-shell special colors, contradicting unique ownership of `pw`;
- m=9: shell capacity forces `n_w=4` at both W-points, all exact colors double type, and the same 130-color core-only degree-four pair contradiction;
- m=8: each W-point has at least two core-only degree-four 130 colors; two subsets of size at least two in the three-color set intersect, contradicting the no-pair theorem.

The finite profile/shell arithmetic was replayed in Python with output:

`V45_SOURCE_CORRECT_PROFILE_ARITHMETIC_OK`.

Verifier scope is arithmetic only. The analytic graph theorem and external extremal inputs remain explicit dependencies.

### Updated support frontier

The source-correct support layers `|U|=44,45` are closed. `|U|=46,47` remain open in this workstream. The old global `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md` must not be used to close v=46 because its proof depends on the retracted exceptional-vertex injectivity assertion.


### 20. Alternate v44 m=8 closure

File: `V44_M8_NO_PAIR_SHORTCUT.md`

The new no-pair theorem also shortens the existing v44 m=8 proof. The established normal form gives `|L(w)|>=2` for each of the three W-points, where L(w) is a subset of the same three 130-edge colors. Any two such sets intersect, creating two core-only degree-four vertices in one 130-edge color, which the new theorem forbids. The longer 700-edge U-pool proof is retained as an independent cross-check.


### 21. Direct no-core-only-degree-four closure for v44,m=8

New proof file:
- `V44_M8_DIRECT_NO_CORE_ONLY_CLOSURE.md`

New arithmetic regression:
- `verify_v44_direct_closure.py`

This round independently audited the existing v44 target against the stronger source-correct theorem `Q32_130_NO_CORE_ONLY_DEG4.md`. The m=8 normal form already forces at least two 130-edge colors to be degree four and core-only at every W-point:
- n_w=2: exact shell ownership fills all thirteen w--A edges and p-w; the (4,4)/(4,3) parameter profiles leave at least two nonexact colors at degree4;
- n_w=3: the three a=4 special incidences exhaust all slack; all nonexact colors have degree4 and at most one can use an O-edge.

The direct no-core-only theorem forbids even one such vertex, so m=8 closes without the previous W-pair rigidity, 700-edge U-pool saturation, or final Turan-equality chain. The older proof remains as an independent cross-check.

The m=9 row remains closed by the simpler zero-shell contradiction: six non-special exact colors consume at least12 of13 w--A edges, forcing at least two special zero-shell colors, while at most one can own p-w.

Arithmetic regression was run in Python:
`V44_DIRECT_CLOSURE_ARITHMETIC_OK`.

Commits:
- direct proof: `93a7ee2e1d7cd976ada7a4580f000e8538bdd208`;
- verifier: `b36c2370a166a964988a46ebcc3cef11708284ca`;
- verifier repeated-profile fix: `d08fd1a919e4a49eed6b5d493295cfbefb23e9ce`;
- canonical state: `8f55348f8cd75fa03975d1e8f100ef8b8392764a`;
- replay audit: `a590e83478f800a4a01554ee302d42a8e9eb2934`;
- dependency audit: `a6a53f6769e8aa92386836627a1284e55c32fe09`.

Scope remains local: `|U|=44,m=8,9` closed; m=10 inherited closed. Full-support `|U|=47` remains open, so EG617(r=12) remains OPEN / NOT_CERTIFIED.


### 22. Make the 130-edge minimum-degree chain self-contained

Added `Q32_130_MINDEG3.md` to explicitly prove the previously referenced degree-three floor. For a hypothesized degree d=0,1,2, the non-neighborhood has size 60,59,58. Kang–Pikhurko Theorem 1 yields floors 139,134,129; in the d=2 case, adding the two edges incident with x already gives at least131 edges, contradicting e(D)=130.

The resulting dependency chain is explicit:
1. `Q32_130_MINDEG3.md`: KP Theorem 1 at n=60,59,58;
2. `Q32_130_MINDEG4_AND_CASEI_M8_CLOSURE.md` (base workstream): KP Theorems 1 and4 at n=57;
3. `Q32_130_NO_CORE_ONLY_DEG4.md`: KP Theorem 1 at n=56 and the local K4-e edge budget;
4. `V44_M8_DIRECT_NO_CORE_ONLY_CLOSURE.md`: pointwise normal form forces at least two prohibited incidences at every W-point.

Extended `verify_v44_direct_closure.py` to check all extremal arithmetic values for n=58,59,60,56. Executed the exact verifier contents in a clean local Python run:
`V44_DIRECT_CLOSURE_ARITHMETIC_OK`.

This removes an implicit proof dependency from the m=8 shortcut. No global theorem promotion: the v=44 layer is closed, but full-support Q32 / v=47 remains open.
