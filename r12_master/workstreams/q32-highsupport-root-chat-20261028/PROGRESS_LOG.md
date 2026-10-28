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
