# E408 Q32 v=44 final — dependency audit

Date: 2026-10-28
Status: **PASS_WITH_EXPLICIT_EXTERNAL_THEOREMS**
Branch: `workstream/r12-q32-caseII-v44-final-20261028`

## 1. Result audited

This workstream proves

> **E408-Q32 with `|U|=44` is impossible for `m=8,9,10`.**

The new proofs close m=8 and m=9 without using the Case-I / Case-II shell dichotomy. The m=10 exclusion is inherited from corrected multiplicity.

No claim is made that E408-Q32 as a whole or EG617(r=12) is closed.

## 2. Base branch and write isolation

Base branch read:

`workstream/r12-twochat-e408-global-20261026`

Base commit used to create this branch:

`937a905ed26e54ec10e9bdade1d9b655da8f6176`.

Only files under

`r12_master/workstreams/q32-caseII-v44-final-chat-20261028/`

were created or modified by this workstream.

## 3. Source-correct imported internal results

### 3.1 Exact-129 source audit

Imported from

`KANG_PIKHURKO_EXACT129_SOURCE_AUDIT.md`.

Used facts:

- exact129 color graph is `10 isolated K5 dot-union G11`;
- excluding the special x, the other60 vertices partition into twelve color-K5 factors;
- source parameter `a in {1,2,3,4}`;
- special degree is `9-a`;
- source cross edges in the original color include `y--P`, `x--(N_s\P)`, `x--(N_t\{y})`;
- every gadget vertex other than the isolated-part vertices has degree at least5 when old parts have size5.

### 3.2 Degree-nine retraction

Imported from

`KP_DEGREE9_RETRACTION_AND_E408_Q32_REOPEN.md`.

Firewall enforced:

- no universal degree-nine special point;
- no exceptional-vertex injectivity;
- no stale exact-color-count collapse.

### 3.3 Corrected non-full-support multiplicity

Imported from

`Q32_CORRECTED_NONFULL_SUPPORT_MULTIPLICITY.md`.

Used facts:

- registered U is generated from single-outside core-four witnesses of the twelve factor K5s;
- for `w in W`, `n_w>=m-6`;
- if an exact color is non-special at w, w lies in a multi-outside factor and has at least two shell neighbors in that color;
- for v=44,m=9, every W-point has exactly three special exact labels.

Important scope firewall:

The new overlapping K5

`{x_C} union (N_t\{y})`

is **not** silently inserted into the registered U witness family. It is used only for the zero-shell edge obstruction.

### 3.4 130-edge minimum degree four

Imported from

`Q32_130_MINDEG4_AND_CASEI_M8_CLOSURE.md`.

Used fact:

> every 130-edge non-target residual color has minimum degree at least4.

Therefore in m=8 the pointwise nonexact floor is

`L_8=4+4+4=12`.

This theorem supersedes older/stale bookkeeping that used `L_8=9`.

### 3.5 U-edge identity / ordinary floor

Imported from

`Q32_U_COLOR_RESERVE.md`.

Used facts:

- ordinary 44-vertex non-target floor `p_12(44)=60`;
- exact v=44 core identity

`e(bar(H[U]))=703-E_U-e_H(W)`.

The older exact-color floor62 is not the final m=8 contradiction; the final `(3,3,2)` branch proves the stronger Type-I-specific floor65.

## 4. New internal lemmas proved in this workstream

### 4.1 Zero-shell special-edge obstruction

File:

`V44_M9_PARAMETER_SYSTEM.md`.

If `x_C=w in H` and w has no C-neighbor in A, then pw has color C.

Dependencies:

- Type-I adjacency `x_C--(N_t\{y})`;
- `N_t` is a C-K5 factor;
- `alpha(H)<=4`;
- `O={p} union A`.

No external theorem beyond the already-audited Type-I source is newly invoked.

### 4.2 m=9 closure

Files:

- `V44_M9_PARAMETER_SYSTEM.md`;
- `V44_M9_ALL_DOUBLE_CLOSURE.md`;
- `V44_M9_TRIPLE_CLOSURE.md`.

Dependencies:

- corrected m=9 multiplicity;
- six non-special exact colors each consume at least two shell edges;
- zero-shell obstruction.

Not used:

- degree-nine exceptional vertex;
- parameter-profile case split;
- old shell scalar floor;
- U-reserve;
- seven-block labels;
- Case-II `alpha(M)<=9`.

### 4.3 m=8 normal form

File:

`V44_M8_NORMAL_FORM.md`.

Dependencies:

- `L_8=12` from 130-edge minimum degree four;
- corrected multiplicity;
- zero-shell obstruction;
- source special excess `5-a`.

### 4.4 130-color local rigidity and W-pair rigidity

Files:

- `FULL_COLOR_EDGE_OWNERSHIP_LEDGER.md`;
- `V44_M8_PAIR_RIGIDITY.md`.

At a degree-four/core-only W-point for a 130-edge color D:

- its four-neighbor set induces `K4-e`;
- its 56-point anti-neighborhood has exactly119 D-edges.

For two degree-four/core-only W-points u,v in the same D:

> uv must have color D.

External dependency here is explicit: Kang--Pikhurko Theorems 1 and4 at `(n,r)=(56,11)`.

### 4.5 m=8 full closure

File:

`V44_M8_CLOSURE.md`.

The partition closures depend on:

- W-pair rigidity;
- exact special-location factor ownership;
- the 285-edge six-excess core identity;
- source Type-I `a=4` gadget geometry in the final branch;
- ordinary Turan equality at44 vertices.

No SAT/ILP nonexistence result is used.

## 5. External theorem ledger

### E1. Kang--Pikhurko Theorem 1

M. Kang and O. Pikhurko, *Maximum K_{r+1}-free graphs which are not r-partite*, Matematychni Studii 24 (2005), 12--20.

Uses in this workstream:

- inherited exact129 source audit at `(61,12)`;
- new pair-rigidity anti-neighborhood count at `(56,11)`:

`t_11(56)=1425`,

`p_11(56)=1421`,

so the corresponding color graph has at least119 edges.

### E2. Kang--Pikhurko Theorem 4

Used at `(56,11)` after equality `e(D[N])=119`.

The eleven old parts cover55 vertices. Since the complementary color graph has clique number at most5, every old part has size exactly5. Hence the color graph is

`9 isolated K5 dot-union G11`,

and every degree-four vertex lies in an isolated K5.

### E3. Ordinary Turan equality theorem

Used only in the final `(3,3,2)` saturation:

A 44-vertex graph D with `alpha(D)<=12` and exactly60 edges has complement equal to the balanced 12-partite Turan graph, so

`D=8K4 dot-union 4K3`.

## 6. Explicit non-dependencies / forbidden routes

The final proof does **not** use:

- the retracted universal degree-nine exceptional vertex;
- exceptional-vertex injectivity;
- stale `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`;
- stale v=45 injectivity reductions;
- E407 284-edge identities;
- Q33 284-edge identities;
- Case-I three-point shell cover;
- Case-II `alpha(M)<=9`;
- seven-block blocker labels;
- SAT/ILP UNSAT claims.

The result is therefore stronger than the originally requested Case-II closure: it excludes the whole v=44 support layer.

## 7. Stale upstream bookkeeping detected

The source workstream's `CANONICAL_STATE.md` contains historical lines with older nonexact floors such as `L_8=9`. Those lines are superseded by the specifically requested and later theorem file

`Q32_130_MINDEG4_AND_CASEI_M8_CLOSURE.md`,

which proves all three m=8 nonexact colors have minimum degree at least4 and hence `L_8=12`.

This workstream uses the theorem file, not the stale summary line.

## 8. Verifier audit

File:

`verify_v44_m8_closure_arithmetic.py`.

Executed in-session; result:

`V44_M8_CLOSURE_ARITHMETIC_OK`.

It checks:

- the m=8 multiplicity enumeration;
- `t_11(56)=1425`, `p_11(56)=1421`, and color-edge value119;
- uniqueness of `(a,b)=(5,2)` from the local integer inequalities;
- three-color L-set intersections;
- `E_U=3 => e(bar(H[U]))=700`;
- exact floor `60+2+3=65`;
- `8*65+3*60=700`;
- the 44-vertex balanced-partition arithmetic `8*4+4*3=44`, internal edge count60.

It does not mechanically verify E1--E3 or the analytic graph implications.

## 9. Audit verdict

> **PASS_WITH_EXPLICIT_EXTERNAL_THEOREMS.**

The v=44 closure is source-correct relative to the registered Q32 contract and the stated external extremal theorems. No retracted dependency was used.