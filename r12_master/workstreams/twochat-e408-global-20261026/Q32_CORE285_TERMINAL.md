# E408 Q32 — independent 285-edge terminal

Updated: 2026-10-28  
Status: **OPEN / NOT_CERTIFIED.**

## 1. Retraction notice

The previous version of this file claimed that the registered E408-Q32 residual was impossible via `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`. That closure used a false source statement: a universal color-degree9 exceptional vertex in the Kang--Pikhurko Type-I exact-129 equality construction.

Primary-source audit shows that the relevant variable gadget degrees are

`(4+a,9-a)`, `a in {1,2,3,4}`,

namely `(5,8),(6,7),(7,6),(8,5)`. There is no universal degree9 vertex.

Therefore the old exact-color-count closure and every step using degree9 exceptional-vertex injectivity are **RETRACTED as Q32 closure theorems**. Historical files remain for audit only.

## 2. Frozen live Q32 contract

Only the 285-edge contract is used here:

`|V(H)|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`,

`sum_H(d_H-12)=6`.

For a maximum-Q32 degree-13 pivot,

`q=32`, `22<=e(M)<=32`, `e(M)+G_A=32`.

The E408 outer ledger gives eleven non-target colors with

`e_C(R)=129+s_C`, `s_C>=0`, `sum_C s_C=3`,

so the number `m` of exact-129 colors belongs to `{8,9,10}`.

No 284-edge/Q33 identity is imported.

## 3. Source-correct witness interface

For each exact-129 color, the valid Type-I equality structure gives twelve disjoint color-K5s plus the special vertex x. The registered Q32 capacity theorem therefore supplies at least ten disjoint independent core-four witnesses per exact color, pairwise-linear across colors.

If U is the union of all such witnesses and W=H\U, then

`|U|>=44`.

The corrected non-full-support theorem gives, for `w in W`, with `n_w` the number of exact colors whose special vertex equals w,

`n_w>=m-6`,

and

`|W|(m-6)<=m`.

At `|U|=44` this already excludes `m=10`; for `m=9`, all nine special vertices lie in W, exactly three at each W-point, and at most one exact color is triple-outside.

## 4. Shell split and currently closed subcases

The Q32 shell classification has two branches.

### Case I

M has an independent 10-set B. Writing S=A\B, `|S|=3`, every M-edge meets S. The source-correct matching theorem yields

`nu(M)>=m-n_w`,

while `nu(M)<=3`, hence `n_w>=m-3`.

Consequences already proved in this workstream:

- v=44: impossible;
- v=45: impossible;
- v=46,m=10: impossible;
- v=46,m=9: OPEN rigid equality terminal;
- v=46,m=8: OPEN with `n_w in {5,6}`;
- v=47: OPEN.

For v=46,m=9 the exact pointwise degree equality forces six special exact colors of degree5 (KP parameter a=4), three non-special exact colors of degree4, nonexact degrees3 and2, target degree13, and an S-to-distinct-B matching from the three non-special double-shell K5s.

### Case II

`alpha(M)<=9`. Current state:

- v=44,m=10: impossible;
- v=44,m=9: OPEN rigid three-W-point terminal;
- v=44,m=8: OPEN;
- v=45,46,47: OPEN.

## 5. New all-color U-reserve theorem

`Q32_U_COLOR_RESERVE.md` proves a source-correct coupling between exact witness K4s and the nonexact color floors in the *same* complement-edge pool.

If an exact color contains ten disjoint witness K4s in U, then

- v=44: `e_C(U)>=62` (ordinary `p_12(44)=60`);
- v=45: `e_C(U)>=64` (ordinary `p_12(45)=63`);
- v=46: `e_C(U)>=66`;
- v=47: `e_C(U)>=69`.

If an exact color supplies at least eleven witness K4s, then at v=44,45 it uses at least66 U-edges.

With h the number of exact colors supplying at least eleven witnesses:

### v=44

`e(bar(H[U])) >= 660+2m+4h`,

hence

`E_U+e(H[W])+2m+4h <=43`.

For the rigid m=9 branch:

- all-double t=0: `e(bar(H[U]))>=678`;
- one-triple t=1: `e(bar(H[U]))>=682`.

### v=45

`e(bar(H[U])) >= 693+m+2h`,

hence

`E_U+e(H[W])+m+2h <=42`.

These are necessary conditions, not contradictions.

## 6. Additional v=44,m=9 shell floor

`Q32_V44_M9_SHELL_EDGE_FLOOR.md` gives independently:

- t=0: `e(M)>=25`, `G_A<=7`;
- t=1: `e(M)>=28`, `G_A<=4`, and at least two core-excess units lie on W.

This theorem uses the corrected Type-I gadget and does not assume Case I.

## 7. Exact remaining mathematical terminal

The current shortest Q32 gap is not a scalar capacity inequality. It is the graph-level compatibility of:

1. the 285-edge / six-excess core;
2. the exact-color witness K4 packing and the new U-edge reserve;
3. the corrected Type-I double/triple multi-outside placements;
4. the 13-point shell color-edge budget;
5. the seven outer K12 blocker/duplicate system.

Highest-priority local terminals are:

- Case-II v=44,m=9 (three W points, three special labels per W, t=0 or1);
- Case-II v=44,m=8;
- Case-I v=46,m=9 and m=8;
- full support v=47.

No finite integer table satisfying only the scalar inequalities is treated as a graph realization, and no absence of candidates is treated as UNSAT without a complete verifier/reduction.

## 8. Global scope

E408 Q33 remains closed by its separate 284-edge nonexact-U-reserve route. E408 Q32 is **OPEN** after the source correction. Therefore this workstream does not certify EG617(r=12).
