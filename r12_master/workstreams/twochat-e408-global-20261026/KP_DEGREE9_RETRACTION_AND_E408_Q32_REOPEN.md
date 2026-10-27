# KP degree-9 retraction and E408-Q32 reopen

Updated: 2026-10-27
Status: **RETRACTION / FAIL-CLOSED PROMOTION CORRECTION**

## 1. Error found by primary-source audit

The published Kang--Pikhurko Type-I equality construction for the `(n,r)=(61,12)` exact-129 color is correctly identified by the project as

`10 isolated K5 + 11-vertex exceptional gadget`.

However, several later E408 files additionally asserted that the gadget has a distinguished vertex of **color-degree 9**. That extra assertion is false.

In the Kang--Pikhurko construction, start from the complete 12-partite complement graph with twelve 5-parts, choose special parts `N_s,N_t`, a vertex `y in N_t`, and a nonempty proper subset `A subset N_s`. Add a new vertex `x`, connect `x` in the complement to `A union {y}` and to all ten ordinary parts, and delete the complement edges between `y` and `A`.

Let `a=|A|`. Because `A` is nonempty and proper,

`a in {1,2,3,4}`.

Take the complement back to the original exact-129 color graph `C`. Then:

- every vertex in the ten isolated K5 components has color-degree4;
- every vertex of `N_s` except for the special redistribution described below has total gadget degree5, and in fact every vertex of `N_s` has degree5 after accounting for `x/y`;
- the four vertices of `N_t\{y}` have degree5;
- `deg_C(y)=4+a`;
- `deg_C(x)=9-a`.

Thus the two variable degrees are

- `a=1`: `(deg y,deg x)=(5,8)`;
- `a=2`: `(6,7)`;
- `a=3`: `(7,6)`;
- `a=4`: `(8,5)`.

There is **no degree-9 vertex** in any legal Type-I equality graph.

The total degree is still 258, as required by 129 edges.

## 2. Exact files invalidated

The following local claims use the false degree-9 premise in a load-bearing way and are therefore retracted as closure theorems:

1. `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`
   - retracted conclusion: exceptional vertices of distinct exact colors are globally injective because each allegedly contributes color-degree9.

2. `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`
   - retracted conclusion: the cases `m=8,9,10` are excluded by counting forced low-degree occurrences at those exceptional vertices.

3. `E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md`
   - retracted as a whole-layer closure because its decisive `m=8,9,10` contradictions import the same false exceptional-degree statement.

4. `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md`
   - retracted as a Q32 closure route because it calls `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md` to obtain the missing global distinctness.

These files remain preserved for audit history. They must not be cited as proved closure statements unless rewritten from valid premises.

## 3. Claims that survive the audit

The primary-source audit confirms the following exact-129 facts:

- the Kang--Pikhurko equality classification applies at `(61,12)`;
- the only contextual equality type surviving `omega(C)<=5` is `(5^12)`;
- every exact-129 non-target color is `10 isolated K5 + 11-vertex exceptional gadget`;
- the gadget contains two 5-cliques plus the extra vertex `x`;
- the gadget has independence number at most2.

Therefore component/witness arguments that use only this factorization remain available.

In particular:

- the E407 Q32 one-color U-reserve contradiction is unaffected;
- the E408 Q33 `m=10` component-capacity exclusion is unaffected;
- the subsequent Q33 nonexact-U reserve contradiction is unaffected;
- the E408 Q32 285-edge core/witness-capacity theorems that do not invoke degree9 remain available as necessary-structure results.

## 4. Correct current E408 frontier

The earlier V9/V11 front-end reduction leaves E408 maximum charge in

`Q in {31,32,33}`

after lower-charge elimination.

- `Q=31`: remains closed by the independently replayed V11 route under its named inputs.
- `Q=33`: remains closed by the component-capacity + nonexact-U reserve route, which does not use degree9.
- `Q=32`: **REOPENED**.

Thus the only currently identified graph-theoretic terminal in the branch-local fixed-r=12 root chain is

`E408 / h13 / maximum Q=32 / 285-edge core / excess six`.

## 5. Root theorem promotion is withdrawn

Because E408-Q32 is reopened, the branch-local claims

- `EG617(r=12): PROVED_CONDITIONAL + COMPUTATION_CERTIFIED`, and
- `no OPEN graph terminal remains`

are withdrawn.

Correct status after this audit:

`EG617(r=12): OPEN / NOT_CERTIFIED`.

More precisely, all currently audited branches except E408-Q32 remain closed relative to their named dependencies.

## 6. New highest-leverage target

Repair E408-Q32 without using exceptional degree9.

The strongest surviving Q32 interface currently known is the 285-edge core/witness system:

- `|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`;
- total core excess6;
- exact-color count `m in {8,9,10}`;
- each exact color supplies at least ten pairwise-disjoint independent core4 witnesses;
- across colors the witness family is pairwise linear;
- total support size `v>=44` by the low-support triple-pair theorem;
- exact complement-capacity identity
  `6N <= C(v,2)-p_4(47-v)-12v+285-E_U`.

This is now the canonical attack surface.

## 7. Fail-closed rule

Any future Q32 closure must explicitly avoid the false degree9 premise or prove a replacement statement directly from the correct Kang--Pikhurko gadget.

No theorem may infer exceptional-vertex injectivity merely from the Type-I equality classification.
