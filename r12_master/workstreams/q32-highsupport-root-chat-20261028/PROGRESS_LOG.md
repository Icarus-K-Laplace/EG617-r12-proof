# Progress log — Q32 high support + root audit

## 2026-10-28

### Branch isolation

Created `workstream/r12-q32-highsupport-root-20261028` from the latest E408-global source state. All writes are confined to `r12_master/workstreams/q32-highsupport-root-chat-20261028/`.

### v=47 near-Turan attack

Proved the source-correct exact-color placement trichotomy relative to `H` and `O={p} union A`:

- x outside H -> `(2,1^11)`, 11 witnesses, H-edge range 69--73;
- x in H / two-double -> `(2,2,1^10)`, 10 witnesses, H-edge range 69--74;
- x in H / triple -> `(3,1^11)`, 11 witnesses, H-edge range 69--75.

Derived exact-color gap cap `0<=g_C<=6` and global all-color identity `sum g_C=37`.

Classified the 69/70 near-Turan layers: common `4^11,3` partition; at 70 edges exactly one cross-part color edge; no K4 can cross parts.

Audited and corrected the explicit 69-edge Type-I placement example so it respects the rule that every p--A edge has target color. This confirms that a universal per-exact-color `+1` reserve is false.

Derived source-correct shell/core tradeoffs `g<=mu+2` (x in H), `g<=mu+1` (x outside H), and minimum exact M-edge payment at least2 (triple x-in-H at least3).

### New m=8 weighted-surplus theorem

Using the newest 130-edge minimum-degree-four theorem, proved the exact pointwise identity

`(d_F(z)-13) + sum_non-target(d_C(z)-4)=3`.

Hence every exact Type-I source parameter satisfies `a in {2,3}`. Its variable weights are `{2,3}`, so no point can host two variable occurrences. Therefore all sixteen `x_C,y_C` points of the eight exact colors are pairwise distinct.

Consequences:

- Case-II v=45,m=8 CLOSED;
- Case-II v=46,m=8 CLOSED.

This is a new source-correct replacement for the historical injectivity-style argument and does not use the withdrawn degree-nine premise.

### v=45/v=46 rigidification

For m=9 and m=10, converted corrected multiplicity `n_w>=m-6` plus the pointwise surplus budget into high-a normal forms.

m=9 at a W-point:

- `n in {3,4}`;
- n=4 -> `(a)=(4,4,4,4)`;
- n=3 -> `(4,4,4)` or `(4,4,3)`.

m=10:

- `n in {4,5}`;
- n=5 -> all a=4;
- n=4 -> `(4,4,4,4)` or `(4,4,4,3)`.

For v=46, every non-special exact color through the unique W point uses at least two distinct shell neighbours, giving the valid Case-II matching lower bound `nu(M)>=m-n_w`.

### Root audit

Verified the fail-closed root receipt and source-frozen E407 sibling hashes.

The exact frozen E407 files at commit `b36538e27dce89dfcba2aa2bfdfc29d6611a96ec` match the receipt hashes. The five-template file itself was still OPEN; therefore finite reduction to five templates is not itself a contradiction.

Verified that the later `E407_FOUR_COLOR_U_RESERVE_CLOSURE.md` genuinely bypasses template-by-template closure using the common 29-point/49-block contract:

`294 selected edges + p_12(29)=22 > 310`.

Verified that the newer V10/V11 audit supersedes the older V11 replay-pending note.

Verified the Q33 global bypass: m=10 excluded by component capacity; m=8,9 excluded by the 31-point nonexact-U reserve (`78,52 > 41`).

Installed `ROOT_DEPENDENCY_DAG.md` and `RETRACTION_FIREWALL.md`.

### Current status

`EG617(r=12) = OPEN / NOT_CERTIFIED`.

This workstream's remaining high-support frontier:

- v=47, m=8,9,10;
- Case-II v=45,m=9,10;
- Case-II v=46,m=9,10.

Sibling workstream retains sole ownership of Case-II v=44,m=8,9.

### New pivot-neighborhood packing theorem (this turn)

Added `V47_PIVOT_NEIGHBORHOOD_PACKING.md`.

Proof spine:
- every exact color C has a C-colored K4 `Q_C` contained in `N_C(p) cap H`, using the source-correct Type-I factorization;
- the sets `Q_C` are pairwise vertex-disjoint because the color-neighborhoods of p partition H;
- `alpha(H)<=4` and Konig imply at least four H-edges between each pair of Q-blocks;
- every point of R=H\\Q has at least one H-neighbor in each Q-block;
- Turan gives `e(H[R])>=p_4(|R|)`.

For m=8,9,10, the three floors sum to253. Defining edge slacks x,y,z gives `x+y+z=32`, `2x+y>=5m`, `y+2z>=D_m` with D=(18,13,8), and `x>=8,13,18` respectively. Added `verify_v47_pivot_packing.py`; local execution returned `V47_PIVOT_PACKING_ARITHMETIC_OK` with 79,61,44 scalar slack states. This confirms the scalar relaxation is feasible and must not be advertised as UNSAT.

### Independent root-dependency audit

Read the branch-local `ROOT_PROMOTION_RECEIPT.md`, the current E407 V12 reserve file, the dedicated E407 proof dependency audit, the V10/V11 independent replay audit, the Q33 capacity/reserve files, and the current Q32 core terminal.

Audit conclusions:
- The E407 four-color U-reserve arithmetic is valid under the frozen V12 `|U|=29`, 49-block contract (`294+22>310`). Parent-level closure remains conditional on V12 exhaustiveness and branch-state reconciliation; the dedicated E407 canonical still carries a stale OPEN same-core snapshot.
- The Q33 31-point nonexact-U-reserve arithmetic is valid under its contract (`m=9`: 52>41; `m=8`: 78>41). The closure file itself makes parent promotion conditional on the upstream reduction exhausting all Q33 completions through that contract. The precise exhaustive support-lifting theorem path was not identified in this pass, so the root DAG now records this as an unresolved dependency rather than silently assuming equality from a support lower bound.
- V9 replay is recorded relative to retained seeds; the newer V10/V11 replay audit supersedes the older V11 pending note and reports package-hash/replay success under retained analytic/lower-order inputs; V12 replay is source-reported by the root receipt and was not re-executed in this turn.
- The old root promotion remains withdrawn because of the KP degree-nine retraction. Root state remains OPEN / NOT_CERTIFIED.

Updated `ROOT_DEPENDENCY_DAG.md`, `RETRACTION_FIREWALL.md`, and `CANONICAL_STATE.md` to keep these contract boundaries explicit.
### Pivot-block triangle consistency (same sprint)

Added Lemma 8.1 to `V47_PIVOT_NEIGHBORHOOD_PACKING.md`: if two block-pairs incident to Q_i each have exactly four H-edges, their perfect matchings force the composed matching on the closing pair Q_j,Q_k. Otherwise Q_i minus one vertex together with the two unmatched endpoints would be an independent 5-set.

Thus every all-light triangle in the block-label graph aligns into four disjoint H-triangles; a heavy closing pair must still contain the composed matching. Since x is the number of extra Q-Q edges, the light-pair graph has at least 5,11,17 edges for m=8,9,10. These counts do not force a triangle by themselves, so the lemma is recorded as a finite compatibility constraint, not a contradiction.
### Universal zero-shell multiplicity theorem — new closure (2026-10-28)

Derived and committed the source-correct inequality `n_w >= 2m-14` for every nonempty W-point. Proof: each non-special exact color consumes at least two distinct w--A edges; at most one special exact color can have zero shell degree because any such color must own the unique edge pw.

Combined with pointwise special-surplus budgets `n_w<=r_m`, `r=(3,4,5)`:
- m=8: still closed by `n_w>=2` and each special incidence costing at least2 against budget3;
- m=9: sharpened from `n_w in {3,4}` to `n_w=4`, and all four special parameters are a=4 at each W-point;
- m=10: `n_w>=6` contradicts `n_w<=5`, so every non-full-support m=10 branch is CLOSED.

Consequences: v=45 m=10 and v=46 Case-II m=10 are now closed; the v=45 m=9 branch spends at least8 global exact-color gap units across the two disjoint special sets, and v=46 m=9 spends at least4. Full support v=47 remains unaffected because W is empty.

Updated `V45_SOURCE_CORRECT_MULTIPLICITY.md`, `V46_CASEII_CLOSURE.md`, `CANONICAL_STATE.md`, and `ROOT_DEPENDENCY_DAG.md`. No retracted KP degree-nine or exceptional-injectivity claim was used.