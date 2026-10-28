# E408 Q32 low-support closure — dependency audit

Date: 2026-10-28
Status: **PASS_WITH_EXPLICIT_EXTERNAL_THEOREMS / HARDENED**
Branch: `workstream/r12-q32-caseII-v44-final-20261028`

## 1. Result audited

This workstream proves

> **E408-Q32 with `|U|=44` and `|U|=45` is impossible for `m=8,9,10`.**

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

A direct compare from the base commit through hardened head `e98b13e9df82ae47f7134098111b2a388a2655d2` found every changed path inside this directory and no sibling-workstream modification.

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

The overlapping K5

`{x_C} union (N_t\{y})`

is **not** inserted into the registered U witness family. It is used only for the zero-shell edge obstruction.

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

`e(bar(H[U]))=703-E_U-e(H[W])`.

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
- its 56-point anti-neighborhood has exactly119 D-edges;
- if the missing-edge endpoints in `K4-e` are r,s and the central vertices are c,d, the equality `e_D(S,N)=2` plus `delta(D)>=4` forces exactly one S--N edge from r and one from s and none from c,d.

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

### 4.6 Final local hardening of `(3,3,2)`

File:

`V44_M8_FINAL_LOCAL_HARDENING.md`.

This note makes two formerly compressed implications explicit:

1. three size-two L-sets with pairwise intersections at most one are the three distinct two-subsets of the nonexact-color set, so the three W--W edges receive three distinct nonexact colors and each nonexact color owns exactly one W--W edge;
2. if v were a missing endpoint of the local `K4-e` at u, the forced S--N distribution from Section4.4 would make `D[N_D(v)]` a triangle plus an isolated vertex (3 edges), contradicting the same local equality at v, which requires `K4-e` (5 edges).

Thus v is central; the third W-point is not in `N_D(u)`; the remaining three vertices of `N_D(u)` lie in U; and the local adjacency pattern contradicts the saturated `D[U]=8K4 dot-union 4K3` structure.

No new external theorem is introduced by the hardening note.

## 5. External theorem ledger

### E1. Kang--Pikhurko Theorem 1

M. Kang and O. Pikhurko, *Maximum K_{r+1}-free graphs which are not r-partite*, Matematychni Studii 24 (2005), 12--20.

Uses in this workstream:

- inherited exact129 source audit at `(61,12)`;
- new pair-rigidity anti-neighborhood count at `(56,11)`:

`t_11(56)=1425`,

`p_11(56)=1421`,

so the corresponding color graph has at least119 edges.

The primary paper was rechecked directly during the hardening audit. Its stated range is `n>=r+3`; for `r<=(n-1)/2` it gives `p_r(n)=t_r(n)-floor(n/r)+1`. The pair-rigidity use satisfies `56>=14` and `11<=27.5`.

### E2. Kang--Pikhurko Theorem 4

Used at `(56,11)` after equality `e(D[N])=119`.

The primary paper states that every extremal graph is described by the explicit construction. The eleven old parts cover55 vertices. Since the complementary color graph has clique number at most5, every old part has size exactly5. Hence the color graph is

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

Re-executed after hardening; result:

`V44_M8_CLOSURE_ARITHMETIC_OK`.

It checks:

- the m=8 multiplicity enumeration;
- `t_11(56)=1425`, `p_11(56)=1421`, and color-edge value119;
- uniqueness of `(a,b)=(5,2)` from the local integer inequalities;
- the forced S--N cross-edge distribution `(1,1,0,0)` in the local `K4-e`;
- three-color L-set intersections and all six ordered legal L-set assignments;
- that each nonexact color then owns exactly one W--W edge;
- the finite missing-endpoint neighbor count (3 edges versus 5 for `K4-e`);
- `E_U=3 => e(bar(H[U]))=700`;
- exact floor `60+2+3=65`;
- `8*65+3*60=700`;
- the 44-vertex balanced-partition arithmetic `8*4+4*3=44`, internal edge count60.

It does not mechanically verify E1--E3, the source Type-I construction, or the analytic graph implications.

## 9. Audit verdict

> **PASS_WITH_EXPLICIT_EXTERNAL_THEOREMS / HARDENED.**

The v=44 closure is source-correct relative to the registered Q32 contract and the stated external extremal theorems. The independent hardening audit found no retracted dependency and resolved the two compressed implications in the final local `K5-e` contradiction.

## 10. Source-correct v45 closure

Files: `V45_SOURCE_CORRECT_CLOSURE.md`, `Q32_130_NO_TWO_CORE_ONLY_DEG4.md`, and `verify_v45_source_correct_profiles.py`.

The v45 proof uses corrected multiplicity `n_w>=m-6`, the source degree `9-a=4+(5-a)`, the valid nonexact floors `L_8=12,L_9=7,L_10=2`, the zero-shell/pivot-edge lemma, and the 13-edge shell capacity. It does not use exceptional-vertex injectivity.

The m=9 floor is seven: the 130-edge color has minimum degree four and the 131-edge color minimum degree three. Any older `L_9=6` summary is stale; the v44 m=9 closure itself does not depend on that value.

The new 130-edge theorem says no two distinct vertices in H can both have degree four in the same 130-edge color with all four neighbors in H. The proof combines the (56,11) second-Turan equality, the local K4-e cross-edge placement, and the degree-four neighborhood lower bound.

Using this theorem:
- m=10 is excluded by shell capacity and the unique owner of pw;
- m=9 forces both W-points to be core-only degree four in the same 130-edge color;
- m=8 forces each W-point to have at least two such colors, so the two color subsets intersect.

Therefore `|U|=45` is CLOSED for m=8,9,10. The arithmetic regression returned `V45_SOURCE_CORRECT_PROFILE_ARITHMETIC_OK`; it does not mechanically verify the analytic lemma or external extremal inputs.

## 11. Remaining scope

The source-correct low-support layers `|U|=44,45` are closed. Higher supports `|U|=46,47` remain open in this workstream. Do not import the old `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md` proof as a v46 closure because it uses the retracted exceptional-vertex injectivity premise.


## 9. Direct v44 m=8 closure route (2026-10-28)

New files:
- `V44_M8_DIRECT_NO_CORE_ONLY_CLOSURE.md`;
- `verify_v44_direct_closure.py`.

The shortest m=8 route no longer needs the W-pair-rigidity / U-pool-saturation chain.

### Exact dependency chain

1. Frozen Q32 pointwise contract: residual degree60; target degree at least13; exact-color degree at least4; each of the three m=8 nonexact colors has130 edges and minimum degree at least4.
2. Corrected multiplicity: `n_w>=2).
3. Source Type-I surplus `5-a` and the zero-shell special-edge obstruction.
4. Thirteen-edge w--A shell capacity, yielding `|L(w)|>=2) at each w in W, where L(w) consists of 130-edge colors D with `d_D(w)=4) and `N_D(w) subset H`.
5. `Q32_130_NO_CORE_ONLY_DEG4.md`: no such core-only degree-four vertex can exist.

The final contradiction is therefore direct. It uses Kang–Pikhurko Theorem 1 at (56,11) and the already registered 130-edge minimum-degree-four theorem. It does not use Kang–Pikhurko Theorem 4, W-pair rigidity, exceptional-vertex injectivity, or the 700-edge U-pool saturation.

The older proof in `V44_M8_CLOSURE.md` remains an independent conditional cross-check, not a necessary dependency of the direct route.

### Verifier boundary

`verify_v44_direct_closure.py` returned `V44_DIRECT_CLOSURE_ARITHMETIC_OK`. It checks finite shell arithmetic, allowed special-parameter profiles, and the local integer edge budget. It does not verify the analytic no-core-only lemma, the source Type-I theorem, corrected multiplicity, or the published Kang–Pikhurko theorem.

No root-level theorem promotion follows: full-support Q32 / `|U|=47` remains open, so EG617(r=12) remains OPEN / NOT_CERTIFIED.


## 10. Explicit 130-edge minimum-degree chain (2026-10-28)

New file: `Q32_130_MINDEG3.md`.

This fills the previously referenced but nonlocal `s=1 pointwise theorem` dependency in the 130-edge local chain.

For a 130-edge color D with `alpha(D)<=12`, `omega(D)<=5`, a hypothesized degree d in {0,1,2} has a non-neighborhood N of size 60,59,58. Kang–Pikhurko Theorem 1 at these sizes gives induced-N edge floors 139,134,129 respectively. These already exceed130 for d=0,1, and the d=2 case gives at least129 edges in N plus the two edges incident with x, hence at least131 edges. Therefore `delta(D)>=3).

The local dependency chain is now explicit and source-linked:

1. `Q32_130_MINDEG3.md`: Theorem 1 at (60,11), (59,11), (58,11).
2. `Q32_130_MINDEG4_AND_CASEI_M8_CLOSURE.md` in the named base workstream: Theorems 1 and 4 at (57,11), using the isolated-K4 equality forced by a hypothetical degree-three vertex.
3. `Q32_130_NO_CORE_ONLY_DEG4.md`: Theorem 1 at (56,11) plus the local `K4-e` budget.
4. `V44_M8_DIRECT_NO_CORE_ONLY_CLOSURE.md`: pointwise shell normal form forces at least two prohibited incidences at every W-point.

The arithmetic regression was extended to cover the 58/59/60-point floors and re-executed successfully. This does not mechanize the analytic arguments or replace checking the cited primary Kang–Pikhurko theorem.
