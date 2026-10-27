# Dependency audit — fixed r=12 after KP source correction

Updated: 2026-10-27
Status: **EG617(r=12) OPEN / NOT_CERTIFIED. Unique currently identified live graph terminal: E408-Q32.**

## 1. Audit correction

Primary-source verification of the Kang--Pikhurko `(61,12)` equality construction confirms the exact-129 Type-I factorization but refutes the project claim that its exceptional gadget contains a color-degree9 vertex.

See `KP_DEGREE9_RETRACTION_AND_E408_Q32_REOPEN.md`.

Consequently the former E408 whole-layer exact-color-count closure and all Q32 arguments depending on exceptional-degree9 injectivity are retracted as closure theorems.

## 2. Valid KP interface

For every exact-129 non-target color C on the 61-point residual:

- `C = 10 isolated K5 dot-union G11`;
- `G11` contains two further 5-cliques and the added vertex x;
- the exact published Type-I construction is the unique Kang--Pikhurko equality type compatible with `omega(C)<=5`.

If `a=|A| in {1,2,3,4}` is the proper-subset parameter in the published construction, the two variable color degrees are

`4+a` and `9-a`,

so the possible pairs are `(5,8),(6,7),(7,6),(8,5)`. No degree9 vertex exists.

Source audit: `KANG_PIKHURKO_EXACT129_SOURCE_AUDIT.md` plus its companion verifier.

## 3. Root/front-end boundary

The finite Line-A recurrence remains computation-certified:

- package SHA256 `8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac`;
- 1,752 recurrence nodes;
- 144 outer comparisons;
- 73 manifest files checked with zero errors;
- unique no-R(4,49) stop `(11,6,5,61)`, energy interval397..408;
- independent replay PASS.

The contextual R(4,49) alternative remains closed relative to its named external/extremal inputs. Historical OPEN bridge candidates in `front_end/ASSUMPTION_LEDGER.md` are not imported into the current shortest chain.

## 4. T61 branches still closed

Relative to their registered contracts:

- h12 closed;
- h13 E397--E400 closed;
- E401--E404 closed;
- E405 closed;
- E406 closed.

This leaves E407 and E408.

## 5. E407 remains closed

### Q31
V10/V11 replay + analytic common-K10 capacity remain unaffected by the KP degree correction.

Frozen hashes:

- V10 archive `e83e2907d541b38304746e855af52b5e21b6500a35cb0fdb676a4f6a7601303a`;
- V11 archive `27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4`;
- V11 certificate `0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b`.

### Q32
V12 replay leaves554 states in five templates. The later common-support interface gives `|U|=29`, 49 selected independent 4-blocks, and `e(overline(H[U]))<=310`.

The 49 blocks own294 distinct selected-color edges. Since only seven selected colors are used among eleven non-target colors, one unselected color D exists. `alpha(D[U])<=12` gives `e_D(U)>=p_12(29)=22`, so

`e(overline(H[U]))>=294+22=316>310`.

This route uses only the valid exact-129 factor/support identity and does not use exceptional degree9. Hence E407-Q32 remains closed.

## 6. E408 charge partition after correction

The earlier V9/V11 reduction leaves maximum charge in `{31,32,33}` after lower-charge elimination.

### Q31
Remains closed by the independently replayed V11 route under its named inputs.

### Q33
Remains closed. Its load-bearing route is:

1. `Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md`: excludes m=10 through isolated-K5/component witness packing; no exceptional-degree9 premise.
2. `Q33_NONEXACT_U_RESERVE_CLOSURE.md`: with m in {8,9}, uses `delta<=17`, `h<=4`, and the nonexact-color U-edge reserve inequality to contradict capacity.

### Q32
**REOPENED.**

The following prior Q32 closure routes are invalid as written because they consume degree9 injectivity:

- `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`;
- `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`;
- `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md` at its injectivity step;
- the Q32 part of the former E408 whole-layer exact-count closure.

## 7. Surviving E408-Q32 285-edge interface

Read-only source branch:

`workstream/r12-e408-q32-excess6-20261025`

Key source:

`r12_master/workstreams/e408-q32-excess6-chat-20261025/CORE285_CAPACITY_THEOREM.md`

Surviving necessary structure:

- `|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`;
- total degree excess6;
- exact-color count `m in {8,9,10}`;
- every exact color supplies at least ten disjoint independent core4 witnesses;
- witness families across colors are pairwise linear;
- if N is total witnesses and `U` their union, `v=|U|`, then

  `6N <= e(overline(H[U]))`

  and

  `6N <= C(v,2)-p_4(47-v)-12v+285-E_U`;

- low-support triple-pair capacity strengthens to `v>=44`;
- at v=44, additional exact normal form constraints are available but no contradiction is currently certified.

None of these statements needs the false degree9 premise.

## 8. Correct current root status

Closed:

- contextual R449;
- h12;
- h13 E397--E406;
- E407 Q31/Q32;
- E408 Q31/Q33.

Open:

- **E408 Q32 only.**

Therefore

`EG617(r=12) = OPEN / NOT_CERTIFIED`.

## 9. Highest-leverage next theorem

> **E408-Q32 285-edge global compatibility theorem.** No 47-vertex core with 285 edges and total excess six can support the exact-color witness system forced by `m in {8,9,10}`, the correct Kang--Pikhurko Type-I factors, the shell-support classification, and all nonexact-color U-edge requirements.

Immediate strategy:

1. classify `v=44,45,46,47` rather than revisiting already excluded `v<44`;
2. quantify when an exact color must supply 11 rather than 10 witnesses;
3. add the `11-m` nonexact-color Turan edge floors on U to the complement capacity;
4. exploit the correct gadget variable-degree pairs only through valid degree budgets;
5. keep Q32 excess-six identities isolated from Q33/E407 excess-four identities.

## 10. Promotion rule

No branch-local root promotion is allowed until Q32 is closed from valid premises. Any newly discovered source mismatch fail-closes the affected theorem immediately.
