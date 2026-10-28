# Dependency audit — fixed r=12 after KP source correction

Updated: 2026-10-28  
Status: **EG617(r=12) OPEN / NOT_CERTIFIED. Unique currently identified live graph terminal: E408-Q32.**

## 1. Source correction and retraction boundary

Primary-source verification of Kang--Pikhurko `(61,12)` confirms the exact-129 Type-I factorization but refutes the former project claim of a universal color-degree9 exceptional vertex.

The source-correct degree pairs are

`(4+a,9-a)`, `a in {1,2,3,4}`,

namely `(5,8),(6,7),(7,6),(8,5)`.

Therefore any Q32 theorem whose contradiction requires degree9 exceptional-vertex injectivity is retracted. In particular the following are not load-bearing closure nodes:

- `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`;
- `Q32_EXACT_COLOR_COUNT_COLLAPSE.md` as a whole;
- the injectivity step of `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md`;
- the Q32 part of the historical E408 whole-layer closure/root promotion.

The source-verified factorization `10 isolated K5 dot-union G11` remains valid and is used only through explicitly audited consequences.

## 2. Root/front-end boundary

The Line-A recurrence remains computation-certified at 1,752 nodes and 144 outer comparisons under its registered inputs. The contextual `R(4,49)` alternative remains closed under its named extremal inputs.

Relative to their registered contracts, the following T61 branches remain closed:

- h12;
- h13 E397--E406;
- E407 Q31/Q32;
- E408 Q31.

Thus the live E408 charges are Q32/Q33 before the color-incidence arguments below.

## 3. E407 firewall

E407-Q32 is closed by the 29-point U-edge reserve route: 49 selected independent four-blocks own294 distinct non-target U-edges, while an unselected color requires at least `p_12(29)=22` more. This exceeds the registered complement capacity310.

This route does not use the retracted degree9 premise.

## 4. Q33 — local P_C=49 profile status

This is the independent 284-edge / excess-four contract.

At `P_C=49`, the four profiles singled out for the emergency sprint now have status:

- `(6,2,1^5)`: **PROVED_CONDITIONAL excluded** by the audited double-star theorem;
- `(7,1^6)`: **PROVED_CONDITIONAL excluded** by `Q33_P49_R7_DOUBLE_STAR_EXCLUSION.md`;
- `(4,4,1^5)`: **OPEN locally** only in the branch where all ten relevant component-representative edges are present;
- `(4,3,2,1^4)`: **OPEN locally** only in the analogous all-component-edge-present branch.

The two remaining local branches are genuine: the current double-star/blocker arguments are triggered by a missing component-representative edge. When all ten are present, the valid monochromatic-K12 star rule gives only

`d_C(z,K12)<=1`,

so a single external same-color edge is legal. The historical stronger isolation claim was false. Consequently **`P_C<=48` is not proved** and must not be used.

## 5. Q33 — global closure bypass

The local P49 gap is not load-bearing for the registered Q33 terminal.

The valid global route is:

1. `Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md` excludes `m=10` without degree9;
2. in the 31-point/56-witness terminal, let `h` be the number of selected gadget witnesses;
3. selected exact-color component witnesses occupy `336-6h` edges of `L=bar(H[U])`, whose total size is `336+delta`;
4. every nonexact color needs at least `p_12(31)=26` U-edges;
5. hence

   `26(11-m)<=delta+6h`.

With `m in {8,9}`, `delta<=17`, and `h<=4`, the right side is at most41 while the left side is78 or52.

Therefore the registered Q33 284-edge terminal is **PROVED_CONDITIONAL impossible** by `Q33_NONEXACT_U_RESERVE_CLOSURE.md`, independently of the two open local P49 profiles.

No Q33 identity is imported into Q32.

## 6. Frozen Q32 285-edge contract

For E408-Q32:

- `|H|=47`, `e(H)=285`;
- `alpha(H)<=4`, `delta(H)>=12`;
- `sum_H(d_H-12)=6`;
- `q=32`, `22<=e(M)<=32`, `e(M)+G_A=32`;
- exact-color count `m in {8,9,10}`;
- every exact-129 color supplies at least ten disjoint independent core-four witnesses;
- different exact-color witness families are pairwise linear;
- their support U satisfies `|U|>=44`.

The corrected non-full-support theorem gives, for `w in W=H\U`,

`n_w>=m-6`,

and hence `|W|(m-6)<=m`.

## 7. New Q32 all-color U-reserve theorem

`Q32_U_COLOR_RESERVE.md` is a new valid dependency.

For any exact color on U containing ten disjoint witness K4s:

| v=|U| | ordinary `p_12(v)` | exact-color floor |
|---:|---:|---:|
|44|60|**62**|
|45|63|**64**|
|46|66|66|
|47|69|69|

At v=44, the 60-edge Turan equality layer has only eight disjoint K4s. The 61-edge layer is excluded by a non-12-partite Brouwer branch or, if the complement is 12-partite, by direct part-size/cross-edge counting. At v=45, equality has only nine disjoint K4s.

If `h` exact colors supply at least eleven witnesses, then

- v=44: `e(bar(H[U]))>=660+2m+4h`;
- v=45: `e(bar(H[U]))>=693+m+2h`.

These are necessary reserve inequalities, not complete contradictions.

## 8. New 131-edge minimum-degree theorem

`Q32_131_MINDEG3_V46_M9_CLOSURE.md` proves:

> any 61-point non-target color C with `e(C)=131`, `alpha(C)<=12`, `omega(C)<=5` satisfies `delta(C)>=3`.

A hypothetical degree-two vertex has a 58-point non-neighborhood with `alpha<=11`, `omega<=5`; Brouwer forces at least129 internal edges. With the two incident edges all131 edges are exhausted, forcing its neighbors to have degree one. A second non-neighborhood bound at order59 gives at least135 total edges from a degree-one vertex, contradiction.

Thus the correct m=9 nonexact pointwise floor is

`L_9=3+3=6`.

This theorem uses no exact-129 gadget degree statement.

## 9. Case-I Q32 consequence

Case I means M has an independent10-set B and every M-edge meets `S=A\B`, `|S|=3`.

The source-correct matching theorem gives

`nu(M)>=m-n_w`,

while `nu(M)<=3`, hence

`n_w>=m-3`.

Current Case-I frontier:

- v=44: **CLOSED**;
- v=45: **CLOSED**;
- v=46,m=10: **CLOSED**;
- v=46,m=9: **CLOSED** by the new 131-edge degree theorem, since at the unique W-point
  `13+(4*9+6)+(3+3)=61>60`;
- v=46,m=8: **OPEN**, with `n_w in {5,6}`;
- v=47: **OPEN**.

## 10. Case-II Q32 frontier

Case II means `alpha(M)<=9`.

- v=44,m=10: **CLOSED**;
- v=44,m=9: **OPEN** rigid three-W-point terminal;
- v=44,m=8: **OPEN**;
- v=45,46,47: **OPEN**.

For v=44,m=9, source-correct shell-edge accounting gives:

- all-double t=0: `e(M)>=25`, `G_A<=7`;
- one-triple t=1: `e(M)>=28`, `G_A<=4`, and at least two core-excess units lie on W.

The new 131-edge floor leaves only two pointwise degree-slack units at each W-point above the baseline58. If its three special exact colors have KP parameters `a_1,a_2,a_3`, then

`sum(4-a_i)<=2`,

so the only sorted parameter triples are

`(4,4,4)`, `(4,4,3)`, `(4,4,2)`, `(4,3,3)`.

This is a reduction, not a contradiction.

## 11. Current root status

Closed under named contracts:

- contextual R449;
- h12;
- h13 E397--E406;
- E407 Q31/Q32;
- E408 Q31/Q33.

Open:

- **E408 Q32 only.**

Therefore

`EG617(r=12) = OPEN / NOT_CERTIFIED`.

## 12. Next load-bearing targets

1. Case-II `v=44,m=9`: combine the three-W KP parameter profiles, shell-edge floor, U-edge reserve, and seven-block blocker labels.
2. Case-II `v=44,m=8`: derive the corresponding special-multiplicity/multi-outside normal forms.
3. Case-I `v=46,m=8`: exploit `n_w in {5,6}` plus the three 130-edge equality/stability structures.
4. `v=47`: use all-color near-Turan/equality structure on the full core.

No branch-local root promotion is allowed until all Q32 terminals are eliminated from valid premises.
