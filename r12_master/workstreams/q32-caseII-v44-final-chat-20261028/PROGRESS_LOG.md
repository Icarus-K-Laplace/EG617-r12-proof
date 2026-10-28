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

## Final mathematical status of this sprint

`|U|=44,m=10`: inherited CLOSED.

`|U|=44,m=9`: CLOSED in this workstream.

`|U|=44,m=8`: CLOSED in this workstream.

Therefore

> **E408-Q32 / |U|=44 is CLOSED.**

The new m=8/m=9 arguments do not use the Case-I/Case-II shell dichotomy, so this is a support-level closure rather than only a Case-II closure.

## Global promotion status

Do not promote EG617(r=12) to proved.

The smallest remaining Q32 support is `|U|=45`. Inherited Case I v=45 is closed, so the next smallest-support OPEN terminal is

> **Case II / |U|=45**.

Higher-support Q32 terminals at v=46,47 also remain outside this workstream.